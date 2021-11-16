# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import BooleanField
# Create your models here.

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField( max_length=120, null=False, unique=True)
    image = models.ImageField(null=True, upload_to="icons/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        services=self.name
        return services




# Custom User Model
class MyUserManager(BaseUserManager):
    def create_user(self, name, email,role, password=None):
        if not email:
            return ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,name,role,email,password):
        user = self.create_user(
            email= self.normalize_email(email),
            password=password,
            name=name,
            role=role
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=60, unique=True, blank=False)
    date_joined =models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now=True,blank=True)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    role = models.CharField(max_length=30, default='User', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= [ 'name','role']

    objects  = MyUserManager()
    
    def __str__(self):
        return self.name+" - "+self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True