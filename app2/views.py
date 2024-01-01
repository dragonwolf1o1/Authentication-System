from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import time
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Please provide right credentials!")
            return redirect('login')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        if password!=cpassword:
            messages.error(request,"Password and Confirm password is not same!")
            return redirect('register')
        
        elif User.objects.filter(username=username).exists():
            messages.error(request,'This Username already used!')
            return redirect('register')
        
        elif User.objects.filter(email=email).exists():
            messages.error(request,'This email already used!')
            return redirect('register')
        
        else:
            user_cre=User.objects.create_user(username,email,password)
            user_cre.save()
            asa=messages.success(request,'User created successfully!')
            return redirect('login')


    return render(request,'register.html')
