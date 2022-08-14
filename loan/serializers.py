#to tanslate the code to json to react and make create and update easy
from json import load
from rest_framework import serializers
from .models import loan

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model=load
        fields='__all__'
