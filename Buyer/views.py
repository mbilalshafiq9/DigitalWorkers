from django.shortcuts import render,redirect
from django.contrib import messages
# from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from Buyer.models import Buyer,Work,Message
from Worker.models import Offer,Order, Review, Worker
from django.db.models import Count , Q
from Middlewares.auth_buyer import auth_middleware
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
# Create your views here.
# dashboard
@auth_middleware
def dashboard(request):
        context={
            "works":Work.objects.filter(posted_by=request.user)
        }
        return render(request,"Buyer/dashboard.html", context)

@auth_middleware
def posted_works(request):
    # if request.method == "POST" and request.POST['accept_order']:
    #     oid=request.POST['oid']
    #     order=Order.objects.get(id=oid)
    #     order.status="completed"
    #     order.save()
    #     messages.success(request, 'Order Accepted Successfully!')
    #     return redirect("posted_works")
    if request.method == "POST" and request.POST['review']:
        wid=request.POST['workerid']
        oid=request.POST['orderid']
        rate=request.POST['rate']
        description=request.POST['description']
        worker=User.objects.get(id=wid)
        order=Order.objects.get(id=oid)
        buyer=User.objects.get(id=request.user.id)
        review =Review(buyer=buyer,worker=worker,order=order,rating=rate,description=description)
        review.save() 
        messages.success(request, 'Review submitted successfully')
        return redirect("posted_works")
    context={
        "works_ava":Work.objects.filter(posted_by=request.user).filter(status="available").annotate(offer_count=Count('offer')).order_by('-posted_at'),
        "orders":Order.objects.filter(order_by=request.user).filter(status="active").order_by('-ordered_at'),
        "orders_com":Order.objects.filter(order_by=request.user).filter(status="completed").order_by('-ordered_at'),
        "reviews":Review.objects.filter(buyer=request.user)
    }
    return render(request,"Buyer/posted_works.html", context)

@auth_middleware
def work_offers(request):
    # Show Offers
    if request.method=="GET":
        wid=request.GET['wid']
        work=Work.objects.get(id=wid)
    # Accept Offer into Order
    if request.method=="POST":
        wid=request.POST['wid']
        work=Work.objects.get(id=wid)
        work.status='assigned'
        work.save()
        oid=request.POST['oid']
        offer=Offer.objects.get(id=oid)

        order =Order(offer=offer,order_by=request.user,order_to=offer.offer_by)
        order.save()  
        messages.success(request, 'Offer is Accepted. Get your Order Done!')
        return redirect("posted_works")
    context={
        "work":work,
        "offers":Offer.objects.filter(work=work).order_by('-offer_at'),
    }
    return render(request,"Buyer/offers.html", context)

@auth_middleware
def orders(request):
    if request.method == "POST" :
        oid=request.POST['oid']
        order=Order.objects.get(id=oid)
        order.status="completed"
        order.save()
        messages.success(request, 'Order Accepted Successfully!')
        return redirect("posted_works")
    context={
        "works_ava":Work.objects.filter(posted_by=request.user).filter(status="available").annotate(offer_count=Count('offer')).order_by('-posted_at'),
        "orders":Order.objects.filter(order_by=request.user).filter(status="active").order_by('-ordered_at'),
        "orders_com":Order.objects.filter(order_by=request.user).filter(status="completed").order_by('-ordered_at')
    }
    return render(request,"Buyer/posted_works.html", context)

@auth_middleware
def profile(request):
    if request.method=="POST":
        name=request.POST['name']
        user=User.objects.get(id=request.user.id)
        user.name=name
        user.save()
        buyer=Buyer.objects.get(user=request.user)
        buyer.phoneno=request.POST['phoneno']
        buyer.city=request.POST['city']
        buyer.gender=request.POST['gender']
        buyer.address=request.POST['address']
        buyer.save()
        messages.success(request, 'Profile Updated Successfully!')
        return redirect("profile")
    context={
        "buyer":Buyer.objects.get(user=request.user)
    }
    return render(request,"Buyer/profile.html", context)

@auth_middleware
def change_password(request):
    if request.method=="POST":
        old_pass=request.POST['old_pass']
        if authenticate(email=request.user.email,password=old_pass):
            new_pass=request.POST['new_pass']
            confirm_pass=request.POST['confirm_pass']
            if new_pass != confirm_pass:
                messages.error(request, 'Confirm Password is Not Matched with new password!')
                return redirect("change_password")
            else:
                u = User.objects.get(id=request.user.id)
                u.set_password(new_pass)
                u.save()
                return redirect("logout")
        else:
            messages.error(request, 'Old Password does not match!')
            return redirect("change_password")

    context={
        "buyer":Buyer.objects.get(user=request.user)
    }
    return render(request,"Buyer/change_password.html", context)

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
        return redirect("/buyer/inbox?sender="+rid)
    if request.method=="GET" and request.GET.get('sender'):
        sender=request.GET.get('sender') 
    else:
        sender=1
    sender=User.objects.get(id=sender)
    contacts = Message.objects.filter( Q(reciever=request.user) | Q(sender=sender) )
    senders = contacts.values_list('sender__id', flat=True).distinct()
    user = User.objects.filter(id__in=senders)
    context={
        "contacts":user,
        "sender":sender,
        "inboxs":Message.objects.filter( Q(reciever=request.user) & Q(sender=sender) | Q(sender=request.user) & Q(reciever=sender) ).order_by("sent_at"),
    }
    return render(request,"Buyer/inbox.html", context)

    