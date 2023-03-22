from django.urls import path
from.views import *

urlpatterns = [
    path('',HomePage.as_view(), name="HomePage"),
    path('create_user/',CreateUser.as_view(), name ="createUser"),
    path('login_user/',UserLogin.as_view(), name ="loginUser"),
    path('user_incident/',UserIncidents.as_view(), name ="user_incidents")
]