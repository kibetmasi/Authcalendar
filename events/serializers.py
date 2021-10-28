from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import Appointments
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
 
class AppointmentSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Appointments
        fields = "__all__"

class App(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"