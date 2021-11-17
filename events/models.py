from datetime import date
from django.contrib.admin.helpers import InlineAdminFormSet
from django.contrib.admin.options import InlineModelAdmin
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.http import request
from softdelete.models import SoftDeleteObject

import random


class Appointments(SoftDeleteObject ,models.Model):  
    chars = '0123456789ABCDEF'
    x = '#'+''.join(random.sample(chars,6))

    user=models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30, default=x, editable=False)
    class Meta:
        verbose_name_plural = "HQ appointments"
    def __str__(self):
        x = self.user 
        day_name = self.start.strftime("%A")
        date_name = self.start.strftime("%m/%d/%Y")
        start_time = self.start.strftime("%X")
        end_time = self.end.strftime("%X")
        return str(self.user)
        # return f"{self.user} has booked a schedule titled '{self.title}' on {day_name}, {date_name} at {start_time} and {end_time}"

class notes(models.Model):
    user=models.ForeignKey(Appointments, on_delete=models.DO_NOTHING,  )
    notes = models.TextField(blank=True, max_length=500)
    class Meta:
        verbose_name_plural = "Deletion notes"
class tab(admin.TabularInline):
    model = notes
    extra = 0
class NotesModel(admin.ModelAdmin):
    list_display = ('user', 'notes')
    list_filter = ('user',)

class FormAdminModel(admin.ModelAdmin):
    inlines = [tab]
    search_fields = ('start',)
    list_display = ('user', 'title', 'start', 'end')
    list_filter = ("start", 'user')




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


    