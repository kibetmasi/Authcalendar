from django.contrib import admin
from events.models import Appointments, AppointmentsBoard, AppointmentsTraining
from . import *
# Register your models here.
admin.site.register(Appointments)
admin.site.register(AppointmentsBoard)
admin.site.register(AppointmentsTraining)
admin.site.site_header  =  "Pesapal Scheduler Administration" 
admin.site.site_url = "https://pesapalscheduler.netlify.app/"
