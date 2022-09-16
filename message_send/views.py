from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, Mailing, Message

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Message

class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = Mailing

    @action(methods=['post'], detail=True)
    def post(self, *args, **kwargs):
        if df





