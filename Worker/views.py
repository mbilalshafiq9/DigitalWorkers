from django.shortcuts import render
from Buyer.models import Buyer,Work

# Create your views here.
# dashboard
def dashboard(request):
    context={
        "works":Work.objects.filter(posted_by=request.user)
    }
    return render(request,"index.html", context)