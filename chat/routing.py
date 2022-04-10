from django.urls import path

from . import consumers

websocket_urlspatterns = [
    path('ws/socket-server/', consumers.ChatConsumer.as_asgi())
]