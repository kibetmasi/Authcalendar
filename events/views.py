from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from events.models import Appointments
from events.permissions import ReadOnly
from .serializers import AppointmentSerializers, UserSerializer, App
from rest_framework import generics
from .forms import RegisterForm
from django.contrib.auth import login, authenticate

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class AppView(generics.ListCreateAPIView):
    serializer_class = App

    def get_queryset(self):
        user = self.request.user
        return Appointments.objects.filter(user=user)

class AppView2(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = App

    def get_queryset(self):
        user = self.request.user
        return Appointments.objects.filter(user=user)

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect('https://pesapalscheduler.netlify.app/')

        return redirect("https://pesapalscheduler2.herokuapp.com/register/")

    else:
	    form = RegisterForm()
    return render(response, "django_registration/registration_form.html", {"form":form})