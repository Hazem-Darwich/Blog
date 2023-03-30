from django.contrib import admin
from django.urls import path, include
from accounts.views import SignupView
  
urlpatterns = [  
    path("signup" , SignupView.as_view() , name = "signup"),
    path("accounts/" , include("django.contrib.auth.urls"))
]