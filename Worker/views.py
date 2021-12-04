from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from Buyer.models import Work,Message,Service
from Worker.models import Offer,Order, Review,Worker
from django.db.models import Count , Q
from Middlewares.auth_worker import auth_middleware
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
# Create your views here.
# dashboard
@auth_middleware
def dashboard(request):
        context={
            "works":Work.objects.filter(posted_by=request.user)
        }
        return render(request,"Worker/dashboard.html", context)

@auth_middleware
def offers(request):
    print("Worker offers called")
    context={
        "offers":Offer.objects.filter(offer_by=request.user).order_by('-offer_at'),
    }
    return render(request,"Worker/offers.html", context)

@auth_middleware
def orders(request):
    if request.method == 'GET' and request.GET.get('order_id'):
        oid =request.GET.get('order_id') 
        order=Order.objects.get(id=oid)
        review = Review.objects.get(order=order) 
        return JsonResponse({"status":200,"rating":review.rating})
    context={
        "orders_ava":Order.objects.filter(order_to=request.user).filter(status="active").order_by('-ordered_at'),
        "orders_com":Order.objects.filter(order_to=request.user).filter(status="completed").order_by('-ordered_at'),
    }
    return render(request,"Worker/orders.html", context)

@auth_middleware
def skills(request):
    worker=Worker.objects.get(user=request.user)
    if request.method == "POST":
        worker.skills=request.POST['skills']
        worker.save()
        messages.success(request, 'Skills Updated Successfully!')
        return redirect("skills")
    context={
        "services":Service.objects.all().order_by('created_at'),
        "worker":worker
    }
    return render(request,"Worker/skills.html", context)

@auth_middleware
def profile(request):
    if request.method=="POST":
        name=request.POST['name']
        user=User.objects.get(id=request.user.id)
        user.name=name
        user.save()
        worker=Worker.objects.get(user=request.user)
        worker.phoneno=request.POST['phoneno']
        worker.cnic=request.POST['cnic']
        worker.city=request.POST['city']
        worker.gender=request.POST['gender']
        worker.address=request.POST['address']
        worker.save()
        messages.success(request, 'Profile Updated Successfully!')
        return redirect("worker_profile")
    context={
        "worker":Worker.objects.get(user=request.user)
    }
    return render(request,"Worker/profile.html", context)

@auth_middleware
def verification(request):
    if request.method=="POST":
        worker=Worker.objects.get(user=request.user)
        worker.cnic_back_pic=request.FILES.get('cnic_back_pic', 'images/blog-1.jpg')
        worker.cnic_front_pic=request.FILES.get('cnic_front_pic', 'images/blog-1.jpg')
        worker.save()
        messages.success(request, 'Profile Updated Successfully!')
        return redirect("worker_profile")
    context={
    "worker":Worker.objects.get(user=request.user)
    }
    return render(request,"Worker/verification.html", context)

@auth_middleware
def change_password(request):
    if request.method=="POST":
        old_pass=request.POST['old_pass']
        if authenticate(email=request.user.email,password=old_pass):
            new_pass=request.POST['new_pass']
            confirm_pass=request.POST['confirm_pass']
            if new_pass != confirm_pass:
                messages.error(request, 'Confirm Password is Not Matched with new password!')
                return redirect("worker_change_password")
            else:
                u = User.objects.get(id=request.user.id)
                u.set_password(new_pass)
                u.save()
                return redirect("logout")
        else:
            messages.error(request, 'Old Password does not match!')
            return redirect("change_password")

    context={
        "worker":Worker.objects.get(user=request.user)
    }
    return render(request,"Worker/change_password.html", context)

@auth_middleware
def inbox(request):
    if request.method=="POST":
        rid=request.POST['rid']
        reciever=User.objects.get(id=rid)
        message=request.POST['message']
        sender=request.user
        inbox =Message(sender=sender,reciever=reciever,message=message)
        inbox.save()
        messages.success(request, 'Message Sent Successfully!')
        return redirect("/worker/inbox?sender="+rid)
    if request.method=="GET" and request.GET.get('sender') :
        sender=request.GET.get('sender') 
    else:
        sender=1
    sender=User.objects.get(id=sender)
    contacts = Message.objects.filter(reciever=request.user)
    senders = contacts.values_list('sender__id', flat=True).distinct()
    user = User.objects.filter(id__in=senders)
    context={
        # "contacts":Message.objects.filter(sender__in=user).order_by('-sent_at').distinct(),
        "contacts":user,
        "inboxs":Message.objects.filter( Q(reciever=request.user) & Q(sender=sender) | Q(sender=request.user) & Q(reciever=sender) ).order_by("sent_at"),
    }
    return render(request,"worker/inbox.html", context)

    