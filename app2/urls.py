from django.contrib import admin
from django.urls import path, include
from app2 import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginuser,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutuser,name='logout')

]
