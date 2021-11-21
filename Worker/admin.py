from django.contrib import admin

# Register your models here.
from Worker.models import Worker,Offer

admin.site.register(Worker)
admin.site.register(Offer)