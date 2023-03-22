from django.contrib.auth.models import User

class BackendModel:
    #TODO Custom Authenticate Model
    #If user exist return user otherwise return None.
    def Authenticate(self, username, password):
        user = User.objects.filter(username = username).first()
        if user:
            if user.password == password:
                return user
            else:
                return None
        else:
            return None