from django.contrib import admin

# Register your models here.
from Home.models import User, Service

admin.site.register(User)
admin.site.register(Service)