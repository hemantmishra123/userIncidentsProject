from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from.custombackend.authenticate import BackendModel
from django.views.generic import CreateView,TemplateView
from .serializers import UserIncidentsSerializer
from random import randint
from.models import *
from datetime import datetime



def generateString(user):
    string = "RMG" + ''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) + "2022"
    incident_objects = Incident.objects.filter(user_id = user).all()

    for user_info in incident_objects:
        if string == user_info.incident_id:
            generateString(user)

    return string

"""Api return for Home_Page"""
class HomePage(TemplateView):
    template_name = "index.html"


"""Api for Creating a New User"""
class CreateUser(APIView):
    def post(self,request,*args,**kwargs):
        user_data = request.data
        #checking if user exist or not if exist then integrity error will be occured.
        user = User.objects.filter(username = user_data["username"]).first()

        if not user:
            if user_data["password"] == user_data["repassword"]:
                user = User(username = user_data["username"], password = user_data["password"])
                user.save()
                return Response("user is created sucessfully")
        
            else:
                return Response("password Does Not Match")
        else:
            return Response("User is already Exist.")


"""Api for login to Existing User"""
class UserLogin(APIView):
    def post(self,request,*args,**kwargs):
        user_data = request.data
        username = user_data["username"]
        password = user_data["password"]
        
        #TODO created a authenticate instance for checking 
        #IF USER Is exist or not with the login credentials.
        #If user login return a user_instance object and otherwise None.
        authenticate_instance = BackendModel()

        user=authenticate_instance.Authenticate(username, password)
        print(user)
        if user:
            login(request, user)
            print(request.user)
            return HttpResponse('ok')
        else:
            return Response("user is not valid")


"""Api for creating a Incident for the Login User"""
class UserIncidents(APIView):
    """ Returning the all incidents of the logined user """
    def get_data(self):
        query=Incident.objects.filter(user = request.user).all()
        return query 

    def get(self, request, *args, **kwargs):
        incidents = self.get_data()
        serializeData= UserIncidentsSerializer(incidents,many=True)
        return Response(serializeData.data)


    """Logined user is creating the incident & testing with postman"""
    def post(self,request,*args,**kwargs):
        print(request.user)
        data = request.data
        user = User.objects.get(username = request.user)
        reporter_name  = data["reporter_name"]
        incident_details = data["incident_details"]
        reported_date = datetime.now()
        priority = data["priority"]
        incident_status = data["incident_status"]

        #creating incident instance for logined user.
        #generate the incident_id First for the incident.
        string = generateString(user)

        incident = Incident(incident_id = string, user_id = user, reporter_name = reporter_name, incident_details=incident_details, reported_date=reported_date,priority=priority,incident_status=incident_status)
        incident.save()
        user_incident = UserProfile()
        user_incident = incident
        user_incident.save()
        return Response("post request get sucessfull")
