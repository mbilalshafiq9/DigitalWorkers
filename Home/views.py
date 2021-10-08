from django.shortcuts import render

# Create your views here.
# Home Page
def index(request):
    # context={
    #     "blogs":Blog.objects.all()
    # }
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def logout(request):
    return render(request,"index.html")