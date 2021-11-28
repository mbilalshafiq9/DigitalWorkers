from django.contrib import admin

from Buyer.models import Buyer, Message, Work
from Worker.models import Order
# Register your models here.

admin.site.register(Buyer)
admin.site.register(Work)
admin.site.register(Order)
admin.site.register(Message)