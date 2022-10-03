from django.contrib import admin
from .models import Client, Mailing, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['phone_number',
'operator_code',
'tag',
'timezone']



@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = [

'filters',


'start_time',

        'message_id',
'end_time']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['date', 'send_status', 'text',
]

    list_editable = ['send_status', 'text',]
    ordering = [ 'send_status', 'text',]


    filter_horizontal = ['client_id',]
    list_filter = [ 'send_status', 'text', ]
    list_per_page = 5
    fields = [ 'send_status', 'text', 'client_id',]
    exclude = []