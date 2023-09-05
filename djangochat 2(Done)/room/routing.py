from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/message/<str:user_name>/', consumers.IndivConsumer.as_asgi()),
]