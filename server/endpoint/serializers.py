from django.db.models import fields
from rest_framework import serializers
from .models import *

"""
Serializer to make sure input (JSON) is valid with the correct passed in keys
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            "username",
            "email"
        ]

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            "username"
        ]

class LeagueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = [
            "ownerUsername",
            "leagueName"
        ]
        # extra key that *could* be useful
        extra_kwargs = {
            "teamLength": {"required": True}
        }

class LeagueAddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username"
        ]
        # extra key that *could* be useful
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

class SubmitLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = [
            "leagueName",
            "ownerUsername"
        ]

class DeleteLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username"
        ]

class addTeamToLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "name",
        ]

        # extra_kwargs = {
        #     "ownerUsername": {"required": True}   
        # }