from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            "username",
            "email"
        ]

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username"
        ]