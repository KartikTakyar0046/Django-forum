from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField()
    publisher=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
