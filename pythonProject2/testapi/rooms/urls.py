from django.urls import path
from .views import RoomView

urlpatterns = [
    path("create/",RoomView, name="room-create")
]