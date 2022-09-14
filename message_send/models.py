from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    phone_number = models.CharField(validators=[RegexValidator(r'7\d{10}')], max_length=11)
    operator_code = models.CharField(max_length=30)
    tag = models.CharField(max_length=15)
    time_location = models.DateField()


class Mailing(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    clients = models.ManyToManyField(Client, related_name='all_clients')
    end_date = models.DateField()
    time_date = models.TimeField()


class Message(models.Model):
    date = models.DateField(auto_now_add=True)
    send_status = models.BooleanField()
    mailing_id = models.ForeignKey(Mailing, related_name='message', on_delete=models.SET_NULL, null=True)
    client_id = models.ForeignKey(Client, related_name='client_message',on_delete=models.SET_NULL, null=True)

