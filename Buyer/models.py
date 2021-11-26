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

# class Order(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
#     ordered_at=models.DateTimeField(auto_now_add=True)
#     status=models.CharField(max_length=60, null=True, default='active')

#     def __str__(self):
#         worker=self.offer
#         return worker