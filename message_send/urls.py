from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from message_send.views import ClientViewSet, MessageViewSet, MailingViewSet

router_for_message = routers.DefaultRouter()
router_for_client = routers.DefaultRouter()
router_for_mailing = routers.DefaultRouter()
router_for_client.register(r'client', ClientViewSet, basename='client')
router_for_client.register(r'mailing', MailingViewSet, basename='mailing')
router_for_client.register(r'message', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_for_message.urls)),
    path('api/v1/', include(router_for_client.urls)),
    path('api/v1', include(router_for_mailing.urls)),
]