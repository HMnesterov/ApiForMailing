
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Mailing, Message
from rest_framework.generics import ListCreateAPIView
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = Message

class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = Mailing


class BookApiView(APIView):
    def post(self, request):

        print(f'Запрос получен! {request.data}')
        return Response({'request': 'запрос принят!'})




