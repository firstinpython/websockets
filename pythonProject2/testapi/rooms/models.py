from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(to=User)

    def __str__(self):
        return self.name