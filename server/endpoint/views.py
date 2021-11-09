from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import *
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.
class GenerateUserObject(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email')
        },
        
    ))
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if (len(User.objects.filter(username=str(request.data['username']))) == 1):
                return Response(data={"response": False, "error": "There was already a saved User object for this user"})
            elif (len(User.objects.filter(username=str(request.data['username']))) == 0):
                user = User(username=str(request.data['username']), email=str(request.data['email']), stat1=0, stat2=0, stat3=0, stat4=0)
                user.save()
                return Response(data={"response": True, "error": "Created a User object for this user"})
            else:
                return Response(data={"response": True, "error": "THIS SHOULDN'T APPEAR"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeagueCreate(APIView):
    def post(self, request, format=None):
        serializer = LeagueCreateSerializer(data = request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=str(request.data['ownerUsername']))) >= 1):
                return Response(data={"response": False, "error": "User already started a league"})
            else:
                league = League(ownerUsername=str(request.data['ownerUsername']), leagueName=str(request.data['leagueName']))
                league.save()
                return Response(data={"response": True, "error": "Created league for user"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeagueAddUser(APIView):
    def post(self, request, format=None):
        serializer = LeagueAddUserSerializer(data = request.data)
        if serializer.is_valid():
            currentLeague = League.objects.get(ownerUsername=request.data['ownerUsername'])
            newUser = User.objects.get(username=request.data['username'])
            # we're just going to assume user wasn't added previously
            currentLeague.allUsers.add(newUser)
            currentLeague.save()
            return Response(data={"response": True, "error": "Added user to league object"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)