from django.contrib.auth.models import User
from django.db import models
from rest_framework import fields, serializers
from .models import Appointments
from datetimerange import DateTimeRange
from django.core.exceptions import ValidationError

from django.db.models import fields, Q 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
 
class AppointmentSerializers(serializers.ModelSerializer,):
    user = serializers.StringRelatedField(many=False)
    # user=UserSerializer()
    # room=RoomSerializer()
    def validate(self,obj): #SANITY CHECKKSSSSSSSSS!!!!!!!!!!!
        start=obj['start']
        end=obj['end']
        if start and end:
            if Appointments.objects.filter(
                models.Q(end__gt=start, start__lt=end) | models.Q(end__gt=end, start__lt=end) | models.Q(start__gt=start, end__lt=end)
            ).exists():
                print("clash exists here")
                raise ValidationError('Event times overlap with existing record!')
        return super(AppointmentSerializers, self).validate(obj)
    class Meta:
        model = Appointments
        fields = "__all__"



class App(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appointments
        fields = "__all__"