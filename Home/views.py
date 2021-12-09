from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib import messages
from Home.models import Service
from Worker.models import Review, Worker,Offer, Review
from django.db.models import Count, Q
from Buyer.models import Buyer, Work
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
# Home Page
def index(request):
    context={
        "services":Service.objects.all()
    }
    return render(request,"index.html", context)

# Login Function to handle login request
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        if user is not None:
            authlogin(request,user)
            if user.role=='worker':
                messages.success(request, 'Your are login Successfully.')
                return redirect('home_profile')
            else:
                messages.success(request, 'Your are login Successfully.')
                return redirect('index')
        else:
            messages.error(request, 'Invalid login Details. Please Try Again!')
            return redirect('login')
    # Redirect if logged user open login page
    if request.user.is_authenticated:
        return redirect("index")
    else:
        return render(request,"login.html")

# Register Function to handle Registration request
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_pass=request.POST.get('confirm_pass')
        role=request.POST.get('role')
        #check fields
        if User.objects.filter(email=email):
            messages.error(request, 'Email Already Exist. Try another')
            return redirect('register')
        if password!=confirm_pass :
            messages.error(request, 'Password is not matched with Confirm Password')
            return redirect('register')
        nuser =User.objects.create_user(name,email,role,password)
        nuser.save()
        luser=User.objects.filter(is_active=True).order_by('-id')[0]
        if role == 'buyer':
            buyer =Buyer(user=luser)
            buyer.save()
        else:
            buyer =Worker(user=luser)
            buyer.save()
        messages.success(request, 'Your Account is created sucessfully.')
        return redirect('login')
    return render(request,"register.html")

def logout(request):
    authlogout(request)
    messages.warning(request, 'Your are logout successfully')
    return render(request,"login.html")
# Find Work Function
def find_work(request):
    if request.method=="POST":
        workid=request.POST['work']
        work=Work.objects.get(id=workid)
        price=request.POST['price']
        due_date=request.POST['due_date']
        offer_to=request.POST['offer_to']
        description=request.POST['description']
        offer_by=request.user
        offer =Offer(budget=price,due_date=due_date,description=description,work=work,offer_by=offer_by,offer_to=offer_to)
        offer.save()
        messages.success(request, 'Offer Send Successfully. Wait for Buyer Message')
        return redirect("find_work")
    work_list=Work.objects.filter(status="available").annotate(offer_count=Count('offer')).order_by('-posted_at')
     #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(work_list, 8)
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        works = paginator.page(1)
    except EmptyPage:
        works = paginator.page(paginator.num_pages)
    if request.user.is_authenticated:
        offers=Offer.objects.filter(offer_by=request.user).values_list('work_id', flat=True)
    else:
        offers=Offer.objects.filter(offer_by=0).values_list('work_id', flat=True)
    context={
        "works":works,
        "work_offers":offers
    }
    return render(request,"find_work.html",context)
# POST A TASK Function
def post_work(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        location=request.POST['location']
        budget=request.POST['budget']
        deadline=request.POST['deadline']
        serviceid=request.POST['service']
        service=Service.objects.get(id=serviceid)
        posted_by=request.user
        work =Work(title=title, description=description,location=location,budget=budget,deadline=deadline,service=service,posted_by=posted_by)
        work.save()
        messages.success(request, 'Task is Posted Successfully!')
        return redirect("posted_works")
    # Check if Only Buyer is logged in 
    if request.user.is_authenticated and request.user.role == 'buyer':
        context={
            "services":Service.objects.all()
        }
        return render(request,"post_work.html",context)
    else:
        messages.warning(request, 'Your need to login as Buyer to Post Task!')
        return redirect('login')

def search(request):
    if request.method=="GET":
        query=request.GET['query']
        location=request.GET['location']
        budget=request.GET['budget']
        maxv=budget.split("-",1)[1]
        minv=budget.rpartition('-')[0]
    if request.user.is_authenticated:
        offers=Offer.objects.filter(offer_by=request.user).values_list('work_id', flat=True)
    else:
        offers=Offer.objects.filter(offer_by=0).values_list('work_id', flat=True)
        
    context={
        "works":Work.objects.filter(Q(status="available") & Q(title__contains=query) & Q(location__contains=location) & Q(budget__gte=minv) & Q(budget__lte=maxv)).annotate(offer_count=Count('offer')).order_by('-posted_at'),
        "work_offers": offers
    }
    return render(request,"find_work.html",context)


def profile(request):
    if request.method=="POST":
        worker=Worker.objects.get(user=request.user)
        if(worker):
            worker.phoneno=request.POST['phoneno']
            worker.cnic=request.POST['cnic']
            worker.gender=request.POST['gender']
            worker.city=request.POST['city']
            worker.address=request.POST['address']
            worker.skills=request.POST['skills']
            worker.cnic_back_pic=request.FILES.get('cnic_back_pic', 'images/blog-1.jpg')
            worker.cnic_front_pic=request.FILES.get('cnic_front_pic', 'images/blog-1.jpg')
            worker.save()
            messages.success(request, 'Profile is Upated sucessfully.')
            return redirect('index')
        else:
            user=request.user
            phoneno=request.POST['phoneno']
            cnic=request.POST['cnic']
            gender=request.POST['gender']
            city=request.POST['city']
            address=request.POST['address']
            skills=request.POST['skills']
            cnic_back_pic=request.FILES.get('cnic_back_pic', 'images/blog-1.jpg')
            cnic_front_pic=request.FILES.get('cnic_front_pic', 'images/blog-1.jpg')
            worker =Worker(user=user, phoneno=phoneno,cnic=cnic,gender=gender,city=city,address=address,skills=skills,cnic_front_pic=cnic_front_pic,cnic_back_pic=cnic_back_pic)
            worker.save()
        messages.success(request, 'Profile is Upated sucessfully.')
        return redirect('index')

    context={
        "services":Service.objects.all()
    }
    return render(request,"profile.html", context)

def about(request):
    return render(request,"about.html")

# Find Worker Function
def find_worker(request):
    worker_list=Worker.objects.all()
    reviews=Review.objects.all()
     #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(worker_list, 8)
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        works = paginator.page(1)
    except EmptyPage:
        works = paginator.page(paginator.num_pages)
    context={
        "worker":works,
        "services":Service.objects.filter(is_active=True),
        "reviews":reviews,
    }
    return render(request,"find_worker.html",context)

# Find Work Function
def search_worker(request):
    if request.method=="GET":
        query=request.GET['query']
        service=request.GET['service']
        rating=request.GET['rating']
        worker_list=Worker.objects.filter(  Q(skills__contains=service) )
        reviews=Review.objects.all()
        #Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(worker_list, 8)
        try:
            works = paginator.page(page)
        except PageNotAnInteger:
            works = paginator.page(1)
        except EmptyPage:
            works = paginator.page(paginator.num_pages)
        context={
            "worker":works,
            "services":Service.objects.filter(is_active=True),
            "reviews":reviews,
        }
        return render(request,"find_worker.html",context)


def forgot_pass(request):
    if  request.method == 'POST' and request.POST['email']:
        email=request.POST['email']
        find_user=User.objects.filter(email=email)
       
        # body='<h3>Hi, Click on the following link to reset. <br> Dont Share this link with anyone. Thanks</h3> <br><h4> Best Regards: Blog to Glob</h4>'
        if find_user:
            body='<div style="background-color:#edf2f7; color:#3d4852;padding:5% 10%; font-family: Roboto, Helvetica, Arial, sans-serif">'
            body=body+'<a href="" style="text-style:none;"><h1 style="text-align:center">Digital Workers</h1></a>'
            body=body+'<div style="background-color:white;padding:2% 5%;border:1px solid gray">'
            body=body+'<h2>Hello '+find_user[0].name+'!</h2> <h2>Have you forgot your Password?</h2>'
            body=body+'<p style="font-size:18px">Dont Worry! We are help to help you. Just  <a href="http://127.0.0.1:8000/reset_password?email='+email+'&pass='+find_user[0].password+'">Click Here</a> to reset your password and Keep enjoying our services. Thanks have a nice day</p><br><hr>'
            body=body+'<p style="font-size:18px">Regards,<br> Digital Workers</p>  </div>'
            msg=EmailMultiAlternatives('Reset Password Link',body,'Digital Workers',[email])
            msg.attach_alternative(body, "text/html")
            msg.send()
            messages.success(request, 'Password Reset link is sent to your mail Sucessfully. Check your Mail inbox')
            return redirect("login")
        else:
            messages.error(request, 'Email is not registered. Type Carefully!')
            return redirect("login")
    return render(request,"login.html")

def reset_pass(request):
    if request.method=='POST':
        email=request.POST['email']
        old_pass=request.POST['old_pass']
        password=request.POST['pass']
        confirm_pass=request.POST['confirm_pass']
        if password != confirm_pass:
            messages.error(request, 'Confirm Password is not same as new password!')
            return redirect('/reset_password?email='+email+'&pass='+old_pass+'')
        else:
            user=User.objects.get(email=email,password=old_pass)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password changed sucessfully!')
            return redirect("login")
    return render(request,"reset_password.html")
            
