
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import pytz

from message_send.tasks import send_post_date

d = [(f'{i[0]}', i) for i in pytz.all_timezones]

class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_number = models.CharField(validators=[RegexValidator(r'7\d{10}')], max_length=11)
    operator_code = models.CharField(max_length=30)
    tag = models.CharField(max_length=15)
    timezone = models.CharField(verbose_name='Time zone', max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return f"{self.phone_number}"





class Message(models.Model):
    date = models.DateField(auto_now_add=True)
    send_status = models.BooleanField(default=False)
    text = models.TextField(max_length=1000)
    client_id = models.ManyToManyField(Client, related_name='client_message')

    def __str__(self):
        return f'{self.text}'


class Mailing(models.Model):

    filters = models.CharField(max_length=1000, blank=True)

    start_time = models.DateTimeField()


    end_time = models.DateTimeField()
    message_id = models.ForeignKey(Message, related_name='message', on_delete=models.SET_NULL, null=True)








@receiver(signal=post_save, sender=Mailing)
def mailing_was_saved(sender, instance, created,  *args, **kwargs):
    text = instance.message_id.text
    if created:

        for user in instance.message_id.client_id.all():

            send_post_date.apply_async([text, user.pk, instance.pk])
        Message.objects.filter(pk=instance.message_id.pk).update(send_status=True)