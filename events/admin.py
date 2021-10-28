from django.contrib import admin

from events.models import Appointments
from . import *
# Register your models here.
admin.site.register(Appointments)
admin.site.site_header  =  "Pesapal Scheduler Admin" 