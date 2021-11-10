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
        serializer = LeagueCreateSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=str(request.data['ownerUsername']))) >= 1):
                return Response(data={"response": False, "error": "User already started a league"})
            elif (len(League.objects.filter(leagueName=str(request.data['leagueName']))) >= 1):
                return Response(data={"response": False, "error": "League name has been used previously"})
            else:
                league = League(ownerUsername=str(request.data['ownerUsername']), leagueName=str(request.data['leagueName']), started=0)
                league.save()
                return Response(data={"response": True, "error": "Created league for user", "leagueName": str(request.data['leagueName'])})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeagueAddUser(APIView):
    def post(self, request, format=None):
        serializer = LeagueAddUserSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=request.data['ownerUsername'])) == 0):
                return Response(data={"response": False, "error": "League owner username is invalid"})
            else:
                currentLeague = League.objects.get(ownerUsername=request.data['ownerUsername'])
                newUser = User.objects.get(username=request.data['username'])
                # we're just going to assume user wasn't added previously
                currentLeague.allUsers.add(newUser)
                currentLeague.save()
                return Response(data={"response": True, "error": "Added user to league object", "leagueName": currentLeague.leagueName})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetActiveLeagueUsers(APIView):
    def post(self, request, format=None):
        serializer = LeagueGetActiveUsersSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(leagueName=request.data['leagueName'])) == 0):
                return Response(data={"response": False, "error": "The data for the requested league doesn't exist"})
            else:
                allUsers = []
                for x in League.objects.get(leagueName=request.data['leagueName']).allUsers.all():
                    allUsers.append(x.username)
                return Response(data={"response": True, "error": allUsers, "leagueOwner": League.objects.get(leagueName=request.data['leagueName']).ownerUsername, "startedStatus": League.objects.get(leagueName=request.data['leagueName']).started})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoesLeagueExist(APIView):
    def post(self, request, format=None):
        serializer = DoesLeagueExistSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User doesn't own any leagues"})
            allTeams = []
            for x in League.objects.get(ownerUsername=request.data['username']).allTeams.all():
                allTeams.append(x)
            if (len(allTeams) == 0):
                lengthTeams = 0
            else:
                lengthTeams = 1
            return Response(data={"response": True, "error": "User owns a leagues", "leagueName": League.objects.get(ownerUsername=request.data['username']).leagueName, "startedStatus": int(League.objects.get(ownerUsername=request.data['username']).started), "lengthTeams": lengthTeams})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmitLeague(APIView):
    def post(self, request, format=None):
        serializer = SubmitLeagueSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User has not initialized a league yet"})
            elif (League.objects.get(leagueName=request.data['leagueName']).ownerUsername != request.data['username']):
                return Response(data={"response": False, "error": "You are not owner of this league"})
            elif (League.objects.get(ownerUsername=request.data['username']).started == 1):
                return Response(data={"response": False, "error": "League has already been started"})
            currentLeague = League.objects.get(ownerUsername=request.data['username'])
            currentLeague.started = 1
            currentLeague.save()
            return Response(data={"response": True, "error": "Started league"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteLeague(APIView):
    def post(self, request, format=None):
        serializer = DeleteLeagueSerializer(data=request.data)
        if serializer.is_valid():
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User doesn't own any leagues"})
            League.objects.filter(ownerUsername=request.data['username']).delete()
            return Response(data={"response": True, "error": "Deleted league owned by user"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)