from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic import View
from django.core.exceptions import ValidationError
from django import forms

class SignupView(View) :

    def post (self , request) :
        form = SignupForm(request.POST)
        if form.is_valid() :
                form.save() 
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                email = form.cleaned_data.get("email")
                user = authenticate(request , username = username , password = password , email = email)
                if user is not None  :
                    login(request , user)
                    return redirect("home")



        return render(request, 'accounts/signup.html' , {"form" : form})   


    def get (self , request) : 
        form  = SignupForm()
        return render(request , "accounts/signup.html" , {"form" : form})
    
