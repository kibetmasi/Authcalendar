from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from softdelete.models import SoftDeleteObject

# Create your models here.

# Model for HQ
class Appointments(SoftDeleteObject ,models.Model):  
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30)
 
    class Meta:
        verbose_name_plural = "HQ appointments"

    def __str__(self):
        return f"{self.user} has booked a schedule titled {self.title}"


# Model for Kabarnet<Training room>
class AppointmentsTraining(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30)
 
    class Meta:
        verbose_name_plural = "Kabarnet - Training room"

    def __str__(self):
        return f"{self.user} has booked a schedule titled {self.title}"


# Model for Kabarnet<Boardroom>
class AppointmentsBoard(models.Model): 
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30)
 
    class Meta:
        verbose_name_plural = "Kabarnet - Board room"

    def __str__(self):
        return f"{self.user} has booked a schedule titled {self.title}"


    