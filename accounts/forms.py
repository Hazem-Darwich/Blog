from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator , RegexValidator

class SignupForm(UserCreationForm) : 
    email = forms.EmailField(required=True , label = "Email address" ,
    widget = forms.EmailInput(attrs={"placeholder" : "Example@gmail.com"}))

    class Meta :
        model = User
        fields = ("first_name" , "last_name" , "username" , "email")

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
      
    #     if not email.endswith("@gmail.com"):
    #         raise forms.ValidationError("Invalid Email Must Be Ends with gmail.com")

    #     return email
