from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    password1   =   forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder':"Enter Password"
    }))
    password2   =   forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder':"Confirm Password"
    }))
    class Meta:
        model   =   User
        fields  =   ['first_name','last_name','email','password1','password2']