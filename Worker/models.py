from django.db import models
# from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.fields import BooleanField
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
