from django.core.serializers import serialize
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail
# Create your views here.

# class RoomView(views.APIView):
#     def get
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
@api_view(['GET','POST'])
def RoomView(request):
    if request.method == 'GET':
        list_rooms = Room.objects.all()
        serializer = RoomSerializer(list_rooms,many=True)

        return Response(serializer.data)

    if request.method == 'POST':

        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


