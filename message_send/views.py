from rest_framework import viewsets
from .models import Client, Mailing, Message


class ClientViewSet(viewsets.ModelViewSet):
    '''Client api base(link /api/v1/client'''

    queryset = Client.objects.all()
    serializer_class = Client


class MessageViewSet(viewsets.ModelViewSet):
    '''Message api base(link /api/v1/Message'''

    queryset = Message.objects.all()
    serializer_class = Message


class MailingViewSet(viewsets.ModelViewSet):
    '''Message  api (link /api/v1/mailing'''

    queryset = Mailing.objects.all()
    serializer_class = Mailing
