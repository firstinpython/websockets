from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    path('room/<str:room_name>/', consumers.RoomConsumer.as_asgi()),
]