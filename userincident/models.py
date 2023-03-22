from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime

#Incident Data_Model
class Incident(models.Model):
    incident_id = models.CharField(max_length=200, null = True, default=None)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    reporter_name = models.CharField(max_length=150, null=True, default=None)
    incident_details = models.TextField(null = True, default=None)
    reported_date = models.DateField(null = True) 
    priority = models.CharField(max_length=150, null = True, default=None) #it could be high ,low & medium.
    incident_status = models.CharField(max_length=150, null = True, default=None) #it could be closed or progress



class UserProfile(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null =True)
