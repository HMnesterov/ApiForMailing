from rest_framework.serializers import ModelSerializer

from .models import Client, Mailing, Message


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
