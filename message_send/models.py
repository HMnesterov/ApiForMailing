from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import pytz
d = [(f'{i[0]}', i) for i in pytz.all_timezones]

class Client(models.Model):
    phone_number = models.CharField(validators=[RegexValidator(r'7\d{10}')], max_length=11)
    operator_code = models.CharField(max_length=30)
    tag = models.CharField(max_length=15)
    time_location = models.CharField(choices=d, max_length=100)


class Mailing(models.Model):

    text = models.TextField(max_length=1000)
    filters = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Message(models.Model):
    date = models.DateField(auto_now_add=True)
    send_status = models.BooleanField(default=False)
    mailing_id = models.ForeignKey(Mailing, related_name='message', on_delete=models.SET_NULL, null=True)
    client_id = models.ForeignKey(Client, related_name='client_message',on_delete=models.SET_NULL, null=True)

@receiver(signal=post_save, sender=Mailing)
def mailing_was_saved(sender, instance, created,  **kwargs):
    if created:
        from .functions import send_post_date
        send_post_date(instance)

