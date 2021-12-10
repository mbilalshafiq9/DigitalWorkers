from django.contrib import admin

# Register your models here.
from Worker.models import Worker,Offer, Review, Commission,Commission_Paid

admin.site.register(Worker)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Commission)
admin.site.register(Commission_Paid)
