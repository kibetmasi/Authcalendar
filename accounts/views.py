from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from accounts.models import *
from .forms import *

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, f"Your account has been created successfully. Contact admin to activate it")
            return redirect('list')
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {'form':form})