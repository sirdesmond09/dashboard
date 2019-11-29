from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Lawyers(models.Model):
    firstname             = models.CharField(max_length = 50)
    lastname              = models.CharField(max_length = 50)
    email                 = models.EmailField(max_length = 250)
    # gender        = models.CharField(max_length = 50)
    phone                 = models.CharField(max_length = 50)
    password              = models.CharField(max_length = 100)
    


    def __str__(self):
        return(f"{self.firstname} {self.lastname}")


class Users(models.Model):
    firstname             = models.CharField(max_length = 50)
    lastname              = models.CharField(max_length = 50)
    email                 = models.EmailField(max_length = 250)
    # gender        = models.CharField(max_length = 50)
    phone                 = models.CharField(max_length = 50)
    password              = models.CharField(max_length = 100)
    confirm_password      = models.CharField(max_length = 100)


    def __str__(self):
        return(f"{self.firstname} {self.lastname}")

# @receiver(post_save,  sender = Lawyers)
# def create_auth_token(sender, created = False, **kwargs):
    
#      if created:
#          Token.objects.create()

