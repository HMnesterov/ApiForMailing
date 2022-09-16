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
'text',
'filters',
'start_date',
'end_date',
'start_time',
'end_time']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['date',
'send_status',
'mailing_id',
'client_id']
