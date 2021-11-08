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
            "leagueOwnerUsername"
            "username"
        ]