
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import pytz

from message_send.tasks import send_post_date

d = [(f'{i[0]}', i) for i in pytz.all_timezones]

class Client(models.Model):
    phone_number = models.CharField(validators=[RegexValidator(r'7\d{10}')], max_length=11)
    operator_code = models.CharField(max_length=30)
    tag = models.CharField(max_length=15)
    time_location = models.CharField(choices=d, max_length=100)

    def __str__(self):
        return f"{self.phone_number}"





class Message(models.Model):
    date = models.DateField(auto_now_add=True)
    send_status = models.BooleanField(default=False)
    text = models.TextField(max_length=1000)
    client_id = models.ManyToManyField(Client, related_name='client_message')


class Mailing(models.Model):

    filters = models.CharField(max_length=1000, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    message_id = models.ForeignKey(Message, related_name='message', on_delete=models.SET_NULL, null=True)

@receiver(signal=post_save, sender=Mailing)
def mailing_was_saved(sender, instance, created,  **kwargs):
    text = instance.message_id.text
    if created:
        print(instance.message_id.client_id.all())
        for user in instance.message_id.client_id.all():
            print(user, 'Это пользователь!')
            send_post_date(text, user, instance)






