from celery import shared_task
from time import sleep

import requests
import datetime
import pytz

from message_send.celery import app


@shared_task
def sleepy(sec):
    sleep(sec)
    return


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODg0ODksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkhlaHdpcW5kIn0.L3pi1pw6ahJ_ATncYRTAkmW2uoioGD-38cdtXMEt_9U'


@app.task(bind=True, default_retry_delay=5 * 60)
def send_post_date(self, msg, user, instance, address="http://127.0.0.1:8000/test/"):
    print(user)
    timezone = pytz.timezone(user.time_location)
    now = datetime.datetime.now(timezone)

    if instance.time_start <= now <= instance.time_end:
        headers = {"Authorization":
                       f'Bearer {token}'}
        requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg, 'headers': headers})

    else:
        self.retry(60)
