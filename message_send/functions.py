import time

import self
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODg0ODksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkhlaHdpcW5kIn0.L3pi1pw6ahJ_ATncYRTAkmW2uoioGD-38cdtXMEt_9U'
from .celery import app
import requests
from celery.utils.log import get_task_logger
import pytz
from .models import Client, Mailing, Message
import datetime
@app.task(bind=True, retry_backoff=True)
def send_post_date(msg, user, instance, address):
    timezone = pytz.timezone(user.time_location)
    now = datetime.datetime.now(timezone)

    if instance.time_start <= now <= instance.time_end:
         headers = {"Authorization":
                   f'Bearer {token}'}
         requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg.text, 'headers': headers})
         print(address, {'user_phone': user.phone_number, 'msg': msg.text})
    else:
        return self.retry(60)


