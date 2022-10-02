from celery import shared_task
from time import sleep

import requests
import datetime

from message_send.celery import app



@shared_task
def sleepy(sec):
    sleep(sec)
    return


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODg0ODksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkhlaHdpcW5kIn0.L3pi1pw6ahJ_ATncYRTAkmW2uoioGD-38cdtXMEt_9U'


@app.task(bind=True, autoretry_for=(Exception('1'),))
def send_post_date(self, msg, user, instance, address="http://127.0.0.1:8000/test/"):
    now = datetime.time()
    from .models import Client, Mailing
    user = Client.objects.get(pk=user)
    instance = Mailing.objects.get(pk=instance)
    try:
        if not instance.start_time <= now <= instance.end_time:
            print(1)
            sleep(60 * 60)
            raise Exception('1')

        headers = {"Authorization":
                       f'Bearer {token}'}
        print(1)
        requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg, 'headers': headers})

    except Exception:
        pass
