from django.db import models
# from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.fields import BooleanField
from Buyer.models import Work
# Create your models here.

class Worker(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    phoneno = models.IntegerField( null=True)
    cnic = models.IntegerField( null=True)
    gender = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=120, null=True)
    skills = models.TextField()
    cnic_back_pic = models.ImageField(null=True, upload_to="uploads/")
    cnic_front_pic = models.ImageField(null=True, upload_to="uploads/")
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        worker=self.user.name+" - "+self.user.email
        return worker

class Offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    budget = models.IntegerField( null=True)
    due_date = models.DateTimeField( null=True)
    description = models.TextField( null=True)
    offer_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    offer_at = models.DateTimeField(auto_now_add=True)
    offer_to = models.CharField(max_length=120, null=True)
    is_accepted=models.BooleanField( default=False)

    def __str__(self):
        offer=self.description
        return offer

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    order_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,related_name='order_by')
    order_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,related_name='order_to')
    ordered_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=60, null=True, default='active')

    def __str__(self):
        order=self.offer.description
        return order
