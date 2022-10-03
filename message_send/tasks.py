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

count = 1
@app.task(bind=True, retry_backoff=True)
def send_post_date(self, msg, user, instance, address="http://127.0.0.1:8000/test/"):


    now = datetime.time()
    from .models import Client, Mailing
    user = Client.objects.get(pk=user)
    instance = Mailing.objects.get(pk=instance)

    if True:
        headers = {"Authorization": f'Bearer {token}'}
        print(f'Trying to send a message to {user}...')
        try:

             requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg, 'headers': headers})
             print(f'Successfully! {user} has accepted the message!')
        except:
            print(f'Something goes wrong, i will try to do this again')
            return self.retry(countdown=60)




    else:

        return self.retry(countdown=60)
# celery -A message_send worker -l info --max-memory-per-child=10000
#pip install eventlet
#celery -A message_send  worker --loglevel=info -P eventlet
#celery -A message_send worker --loglevel=info --pool=solo
#celery -A yourapp.celery worker --loglevel=info --pool=solo