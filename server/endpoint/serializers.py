from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            "username",
            "email"
        ]

class LeagueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = [
            "ownerUsername",
            "leagueName"
        ]

class LeagueAddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username"
        ]
        extra_kwargs = {
            "ownerUsername": {"required": True}   
        }

class LeagueGetActiveUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ["leagueName"]

class DoesLeagueExistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username"
        ]
