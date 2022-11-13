Welcome! It`s my project that can help you with Mailing<3.
How to use this?
1.Set your own link to make a post tasks in settings.
2.You should connect another service to send messages.
3.You can change models in databases(for example, change 'phone_number' to email, but in this case you may replace all 'phone_number' to email in project.

How to launch this app:
1)install redis and launch it using a command 'redis-server'
2)python manage.py makemigrations => python manage.py migrate
3)create your own database(not sqlite3, because this database hasn`t might)
4)celery -A message_send worker --loglevel=info --pool=solo
5)python manage.py runserver
Enjoy this!)'''
