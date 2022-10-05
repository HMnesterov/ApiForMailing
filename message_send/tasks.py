import pytz

import requests
import datetime

from message_send.celery import app


from API.settings import url_address
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODg0ODksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkhlaHdpcW5kIn0.L3pi1pw6ahJ_ATncYRTAkmW2uoioGD-38cdtXMEt_9U'




@app.task(bind=True, retry_backoff=True)
def send_post_date(self, msg, user, instance, address=url_address):
    from .models import Client, Mailing
    user = Client.objects.get(pk=user)

    instance = Mailing.objects.get(pk=instance)
    timezone = pytz.timezone(user.timezone)
    time = datetime.datetime.now(timezone)

    if instance.start_time > time:
        '''Retrying every hour'''
        return self.retry(60 * 60)
    elif instance.start_time <= time <= instance.end_time:
        headers = {"Authorization": f'Bearer {token}'}
        print(f'Trying to send a message to {user}...')
        try:
            requests.post(url=address, data={'user_phone': user.phone_number, 'msg': msg, 'headers': headers})
            print(f'Successfully! User has accepted the message!')
        except:
            print(f'Something goes wrong, i will try to do this again')
            return self.retry(countdown=60)
    else:
        print('Time for sending has gone. It`s over!')



'''How to launch this app:
1)install redis and launch it using a command 'redis-server'
2)celery -A message_send worker --loglevel=info --pool=solo
3)flower -A my_supper_app --port=5555
4)python manage.py runserver
Enjoy this!)'''
