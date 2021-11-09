from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from softdelete.models import SoftDeleteObject

import randomcolor


# Model for HQ
class Appointments(SoftDeleteObject ,models.Model):  
    rand_color = randomcolor.RandomColor()
    x = (rand_color.generate())

    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30, default=x)
    class Meta:
        verbose_name_plural = "HQ appointments"
    def __str__(self):
        day_name = self.start.strftime("%A")
        date_name = self.start.strftime("%m/%d/%Y")
        start_time = self.start.strftime("%X")
        end_time = self.end.strftime("%X")
        return f"{self.user} has booked a schedule titled '{self.title}' on {day_name}, {date_name} at {start_time} and {end_time}"

class FormAdminModel(admin.ModelAdmin):
    search_fields = ('start',)
    list_display = ('user', 'title', 'start', 'end')
    list_filter = ("start", 'user')


class notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(blank=True, max_length=500)
    class Meta:
        verbose_name_plural = "Deletion notes"
class NotesModel(admin.ModelAdmin):
    list_display = ('user', 'notes')
    list_filter = ('user',)

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


    