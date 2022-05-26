from email import message
from os import name
from django.db import models

# Create your models here.
class Contact1(models.Model):
    name = models.TextField('Сообщение')
    email = models.EmailField('Email почта', max_length=255)
    adress = models.TextField('Сообщение')
    messages = models.TextField('Сообщение')
    sent_at = models.DateTimeField(auto_now_add=True)
    