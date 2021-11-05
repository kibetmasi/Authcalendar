from django.contrib import admin
from events.models import ( 
        Appointments, 
        AppointmentsBoard, AppointmentsTraining, 
        FormAdminModel, FormAdminModel, notes, 
        NotesModel
        )
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Appointments, FormAdminModel)
admin.site.register(AppointmentsBoard)
admin.site.register(AppointmentsTraining)
admin.site.register(notes, NotesModel)
admin.site.site_header  =  "Pesapal Scheduler Administration" 
admin.site.site_url = "https://pesapalscheduler.netlify.app/"