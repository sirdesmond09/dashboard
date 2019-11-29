from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate 
from .models import *

class LawyersSerializers(serializers.ModelSerializer):
    firstname             = serializers.CharField(required = False)
    lastname              = serializers.CharField(required = False)
    email                 = serializers.CharField(required = False)
    phone                 = serializers.CharField(required = False)
    password              = serializers.CharField(required = False)
    class Meta:
        model  = Lawyers
        fields = '__all__' 


class LawyerAuthSerializers(serializers.Serializer):
    email                 = serializers.CharField(required = True)
    password              = serializers.CharField(required = True)
    
    def validate(self, data):
        email    = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            lawyer = authenticate(email = email, password = password)
            if lawyer:
                pass
            else:
                msg = "Criendtials not correct"
                raise exceptions.ValidationError(msg)

        else:
            msg = "Must provide Email and Password"
            raise exceptions.ValidationError(msg)