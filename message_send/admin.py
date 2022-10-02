from django.contrib import admin
from .models import Client, Mailing, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['phone_number',
'operator_code',
'tag',
'time_location']



@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = [

'filters',
'start_date',
'end_date',
'start_time',

        'message_id',
'end_time']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['date',
'send_status',
                    'text',
'client_id']
