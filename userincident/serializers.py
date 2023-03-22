from rest_framework import serializers
from.models import *
from django.contrib.auth.models import User

class UserIncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields =['user_id', 'incident_id','reporter_name','incident_details','reported_date', 'priority' , 'incident_status']
