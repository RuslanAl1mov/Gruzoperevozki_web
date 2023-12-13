from django.contrib.auth.backends import BaseBackend
from passlib.apps import django_context

from .models import User


class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check the username/password and return a User.
        if username is not None and password is not None:
            doctor_obj = User.objects.filter(username=username).first()
            doctor = User.objects.filter(username=username).values()
            if len(doctor) != 0:
                doctor_info = doctor[0]
                if doctor_info['username'] == username and django_context.verify(password, doctor[0]['password']):
                    return doctor_obj
                else:
                    return None
        else:
            return None



