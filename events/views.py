from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from events.models import Appointments
from events.permissions import ReadOnly
from .serializers import AppointmentSerializers, UserSerializer, App
from rest_framework import generics


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.filter()
    serializer_class = AppointmentSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class AppView(generics.ListAPIView):
    serializer_class = App

    def get_queryset(self):
        user = self.request.user
        return Appointments.objects.filter(user=user)

class AppView2(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = App

    def get_queryset(self):
        user = self.request.user
        return Appointments.objects.filter(user=user)
