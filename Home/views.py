from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib import messages
from Home.models import Service
from Worker.models import Worker
from Buyer.models import Buyer, Work
import random
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
# Home Page
def index(request):
    context={
        "services":Service.objects.all()
    }
    return render(request,"index.html", context)


def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        if user is not None:
            authlogin(request,user)
            if user.role=='worker':
                messages.success(request, 'Your are login Successfully.')
                return redirect('profile')
            else:
                messages.success(request, 'Your are login Successfully.')
                return redirect('index')
        else:
            messages.error(request, 'Invalid login Details. Please Try Again!')
            return redirect('login')
    return render(request,"login.html")


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
        messages.success(request, 'Your Account is created sucessfully.')
    
    return render(request,"register.html")

def logout(request):
    authlogout(request)
    messages.warning(request, 'Your are logout successfully')
    return render(request,"login.html")

def find_work(request):
    colors = {
        "Cleaner": "info",
        "Event Planner": "warning",
        "Electrician": "danger",
        }
    context={
        "colors":colors,
        "works":Work.objects.filter(status="available")
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




