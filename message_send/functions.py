from django.db.models import Q
from celery import app
import requests
from celery.utils.log import get_task_logger
import pytz
from .models import Client, Mailing, Message
import datetime

def send_post_date(msg, user, instance, address):
    timezone = pytz.timezone(user.time_location)
    now = datetime.datetime.now(timezone)

    if instance.time_start <= now <= instance.time_end:
         requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg.text})


