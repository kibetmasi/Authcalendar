from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=30)
 
    def __str__(self):
        return f"{self.user} has booked a schedule titled {self.title}"