import json
from asyncio import sleep
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room
from django.core.mail import send_mail

class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        list_rooms_people = self.scope['user']
        list_model = Room.objects.filter(name = self.room_name)
        if list_model:
            print(list_rooms_people)
            self.room_group_name = f'room_{self.room_name}'

            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )

        self.accept()
        send_mail(
            "Webapp",
            "You connected",
            settings.EMAIL_HOST_USER,
            ['ntr.0707@mail.ru']
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'hello_message',
                'message': 'hello user'
            }
        )

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def hello_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    # def chat_message(self, event):
    #     """
    #     Called when someone has messaged our chat.
    #     """
    #     # Send a message down to the client
    #     self.send(text_data=json.dumps({
    #         "room": event["room_id"],
    #         "username": event["username"],
    #         "message": event["message"],
    #     }))
