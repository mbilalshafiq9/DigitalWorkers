from django.shortcuts import render,redirect
from django.contrib import messages
# from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from Buyer.models import Buyer,Work
from Worker.models import Offer
from django.db.models import Count
# Create your views here.
# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        context={
            "works":Work.objects.filter(posted_by=request.user)
        }
        return render(request,"Buyer/dashboard.html", context)
    else:
        messages.error(request, 'You need to login first!')
        return redirect("login")

def posted_works(request):

    context={
        "works_ava":Work.objects.filter(posted_by=request.user).filter(status="available").annotate(offer_count=Count('offer')).order_by('-posted_at'),
        "works_ass":Work.objects.filter(posted_by=request.user).filter(status="assigned").annotate(offer_count=Count('offer')).order_by('-posted_at'),
        "works_com":Work.objects.filter(posted_by=request.user).filter(status="completed").annotate(offer_count=Count('offer')).order_by('-posted_at')
    }
    return render(request,"Buyer/posted_works.html", context)

def work_offers(request):
    if request.method=="GET":
        wid=request.GET['wid']
        work=Work.objects.get(id=wid)
    context={
        "work":work,
        "offers":Offer.objects.filter(work=work).order_by('-offer_at'),
    }
    return render(request,"Buyer/offers.html", context)