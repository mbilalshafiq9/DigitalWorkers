from django.db import models

from django.conf import settings
from django.db.models.fields import BooleanField
from Home.models import Service
# Create your models here.

class Buyer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    phoneno = models.IntegerField( null=True)
    gender = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=120, null=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        worker=self.user.name+" - "+self.user.email
        return worker

class Work(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120, null=False)
    budget = models.IntegerField( null=True)
    deadline = models.DateTimeField( null=True)
    location = models.CharField(max_length=120, null=True)
    description = models.TextField( null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    posted_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    posted_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=60, null=True, default='available')

    def __str__(self):
        worker=self.title
        return worker

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="sender")
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True , related_name="reciever")
    message = models.TextField( null=True)
    sent_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(null=True, default=False)

    def __str__(self):
        message=self.message
        return message

