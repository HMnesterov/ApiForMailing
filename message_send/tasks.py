from celery import Celery, shared_task
from time import sleep
import os
import requests
from retry import retry
import datetime
import pytz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.settings')

app = Celery('API')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@shared_task
def sleepy(sec):
    sleep(sec)
    return

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODg0ODksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkhlaHdpcW5kIn0.L3pi1pw6ahJ_ATncYRTAkmW2uoioGD-38cdtXMEt_9U'
@app.task(bind=True, retry_backoff=True)
def send_post_date(msg, user, instance, address="http://127.0.0.1:8000/add_item/"):
    timezone = pytz.timezone(user.time_location)
    now = datetime.datetime.now(timezone)

    if instance.time_start <= now <= instance.time_end:
         headers = {"Authorization":
                   f'Bearer {token}'}
         requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg.text, 'headers': headers})

    else:
        sleep(60 * 60)
        send_post_date(msg, user, instance, address)