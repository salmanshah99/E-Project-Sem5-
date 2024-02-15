from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect


# from Admin import User


# Create your views here.

def home(request):
    return render(request,"Home.html")
def modes(request):
    return render(request,"modes.html")
def register(request):
    return render(request,"register.html")
def register_submit(request):
    # data={}
    data = {
        "username": request.POST.get("username"),
        "email": request.POST.get("email"),
        "password": request.POST.get("password"),
    }
    user = User.objects.create(**data)
    user.set_password(request.POST.get("password"))
    user.save()
    return render(request, "Login.html")

def login(request):
    return render(request,"Login.html")
def login_submit(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(password=password, username=username)
    if user is None:
        # messages.error(request, 'Invalid Credentials')
        return redirect("login")
    else:
        return redirect("home")