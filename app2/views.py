from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import time
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/register')
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
            return redirect('login')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password!=cpassword:
            return HttpResponse("Password and Confirm pass is not equal:")
        else:
            user_cre=User.objects.create_user(username,email,password)
            user_cre.save()
            return redirect('login')


    return render(request,'register.html')
