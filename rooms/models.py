from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    users = models.ManyToManyField(User)
    message = models.CharField(max_length=9120)

    def __str__(self):
        return self.pk


class Message(models.Model):
    message = models.CharField(max_length=9120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}- {self.user.message}"


