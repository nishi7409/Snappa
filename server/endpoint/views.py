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

# Generate user objects when user registers for an account
class GenerateUserObject(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            #checks to see if user already exisits
            if (len(User.objects.filter(username=str(request.data['username']))) == 1):
                return Response(data={"response": False, "error": "There was already a saved User object for this user"})
            #otherwise creates a new user
            elif (len(User.objects.filter(username=str(request.data['username']))) == 0):
                user = User(username=str(request.data['username']), email=str(request.data['email']), stat1=0, stat2=0, stat3=0, stat4=0, stat5=0, stat6=0, stat7=0, stat8=0, stat9=0, stat10=0, stat11=0)
                user.save()
                return Response(data={"response": True, "error": "Created a User object for this user"})
            else:
                return Response(data={"response": True, "error": "THIS SHOULDN'T APPEAR"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GenerateUserStats sends all stats of a user to the API endpoint under the URL getUserStats/ in JSON format
# Inputs:
#   User
# Outputs:
#   stats of the user
class GenerateUserStats(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = StatSerializer(data = request.data)
        tmpName = str(request.data['username'])
        if serializer.is_valid():
            if (len(User.objects.filter(username = tmpName)) == 1):
                tmpUser = User.objects.get(username = tmpName)
                #returns the stats of the user (shots, table hits, points, clinks, dunks, potential points, catches, drops, table hit percentage, potential point percentage)
                return Response(data={  "stat1" : tmpUser.stat1,
                                        "stat2" : tmpUser.stat2,
                                        "stat3" : tmpUser.stat3,
                                        "stat4" : tmpUser.stat4,
                                        "stat5" : tmpUser.stat5,
                                        "stat6" : tmpUser.stat6,
                                        "stat7" : tmpUser.stat7,
                                        "stat8" : tmpUser.stat8,
                                        "stat9" : tmpUser.stat9,
                                        "stat10" : tmpUser.stat10,
                                        "stat11" : tmpUser.stat11})

            else:
                return Response(data={"response": True, "error": "This user does not exist"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Creating a league object based off passed in JSON key information
class LeagueCreate(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = LeagueCreateSerializer(data=request.data)
        if serializer.is_valid():
            #check if league has already been started
            if (len(League.objects.filter(ownerUsername=str(request.data['ownerUsername']))) >= 1):
                return Response(data={"response": False, "error": "User already started a league"})
            #Checks to see if a unique league name was used
            elif (len(League.objects.filter(leagueName=str(request.data['leagueName']))) >= 1):
                return Response(data={"response": False, "error": "League name has been used previously"})
            #creates league
            else:
                league = League(ownerUsername=str(request.data['ownerUsername']), leagueName=str(request.data['leagueName']), started=0, teamLength=int(request.data['teamLength']))
                league.save()
                return Response(data={"response": True, "error": "Created league for user", "leagueName": str(request.data['leagueName'])})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add a user to a league
class LeagueAddUser(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = LeagueAddUserSerializer(data=request.data)
        if serializer.is_valid():
            #checks for invalid username
            if (len(League.objects.filter(ownerUsername=request.data['ownerUsername'])) == 0):
                return Response(data={"response": False, "error": "League owner username is invalid"})
            else:
                #adds user to the league league
                currentLeague = League.objects.get(ownerUsername=request.data['ownerUsername'])
                newUser = User.objects.get(username=request.data['username'])
                # we're just going to assume user wasn't added previously
                currentLeague.allUsers.add(newUser)
                currentLeague.save()
                return Response(data={"response": True, "error": "Added user to league object", "leagueName": currentLeague.leagueName})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all active league users (all users that have joined the league)
class GetActiveLeagueUsers(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = LeagueGetActiveUsersSerializer(data=request.data)
        if serializer.is_valid():
            #checks for valid league name
            if (len(League.objects.filter(leagueName=request.data['leagueName'])) == 0):
                return Response(data={"response": False, "error": "The data for the requested league doesn't exist"})
            else:
                #returns all users of the league
                allUsers = []
                for x in League.objects.get(leagueName=request.data['leagueName']).allUsers.all():
                    allUsers.append(x.username)
                return Response(data={"response": True, "error": allUsers, "leagueOwner": League.objects.get(leagueName=request.data['leagueName']).ownerUsername, "startedStatus": League.objects.get(leagueName=request.data['leagueName']).started, "teamLength": int(League.objects.get(leagueName=request.data['leagueName']).teamLength)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Checks if league exists
class DoesLeagueExist(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = DoesLeagueExistSerializer(data=request.data)
        if serializer.is_valid():
            #checks if the user is a league owner
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User doesn't own any leagues"})
            #checks how many teams are in the league and returns the league name and the number of teams
            allTeams = []
            for x in League.objects.get(ownerUsername=request.data['username']).allTeams.all():
                allTeams.append(x)
            if (len(allTeams) == 0):
                lengthTeams = 0
            else:
                lengthTeams = 1
            return Response(data={"response": True, "error": "User owns a leagues", "leagueName": League.objects.get(ownerUsername=request.data['username']).leagueName, "startedStatus": int(League.objects.get(ownerUsername=request.data['username']).started), "lengthTeams": lengthTeams})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Activates a league
class SubmitLeague(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = SubmitLeagueSerializer(data=request.data)
        if serializer.is_valid():
            #checks for user initialization of league
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User has not initialized a league yet"})
            #checks if user is the league owner
            elif (League.objects.get(leagueName=request.data['leagueName']).ownerUsername != request.data['username']):
                return Response(data={"response": False, "error": "You are not owner of this league"})
            #makes sure that league is not already in play
            elif (League.objects.get(ownerUsername=request.data['username']).started == 1):
                return Response(data={"response": False, "error": "League has already been started"})
            #starts the league 
            currentLeague = League.objects.get(ownerUsername=request.data['username'])
            currentLeague.started = 1
            currentLeague.save()
            return Response(data={"response": True, "error": "Started league"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create a team and add to league
class addTeamToLeague(APIView):
    def post(self, request, format=None):
        serializer = addTeamToLeagueSerializer(data=request.data)
        print("YES?")
        if serializer.is_valid():
            print("YES?2")
            if (len(League.objects.filter(ownerUsername=request.data['ownerUsername'])) == 0):
                return Response(data={"response": False, "error": "This league doesn't exist"})
            if (len(Team.objects.filter(name=request.data['name'])) != 0):
                return Response(data={"response": False, "error": "This team name is taken"})
            print("YES?3")
            currentTeam = Team(name = str(request.data['name']), user1 = User.objects.get(username=str(request.data['user1'])), user2 = User.objects.get(username=str(request.data['user2'])))
            print("YES?4")
            currentTeam.save()
            league = League.objects.get(ownerUsername=request.data['ownerUsername'])    
            league.allTeams.add(currentTeam)
            print("YES?5")
            return Response(data={"response": True, "error": "Successfully added the team"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Deletes a league
class DeleteLeague(APIView):
    def post(self, request, format=None):
        # serializer checks if the passed in data (json object) meets the desired requirements
        serializer = DeleteLeagueSerializer(data=request.data)
        if serializer.is_valid():
            #checks to see if user owns the league
            if (len(League.objects.filter(ownerUsername=request.data['username'])) == 0):
                return Response(data={"response": False, "error": "User doesn't own any leagues"})
            #Deletes the league
            League.objects.filter(ownerUsername=request.data['username']).delete()
            return Response(data={"response": True, "error": "Deleted league owned by user"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class enterStats(APIView):
    def post(self, request, format=None):
        
        serializer = enterStatsSerializer(data=request.data)
        if serializer.is_valid():
            if (len(Team.objects.filter(name = request.data['team'])) == 0):
                return Response(data={"response": False})

            tmpTeam = Team.objects.get(name = request.data['team'])
            if (tmpTeam.user1 == request.data['player']): 
                tmpTeam.user1.stat2 += request.data['shot']
                tmpTeam.user1.stat3 += request.data['tablehit']
                tmpTeam.user1.stat4 += request.data['point']
                tmpTeam.user1.stat5 += request.data['clink']
                tmpTeam.user1.stat6 += request.data['dunk']

            else:
                tmpTeam.user2.stat2 += request.data['shot']
                tmpTeam.user2.stat3 += request.data['tablehit']
                tmpTeam.user2.stat4 += request.data['point']
                tmpTeam.user2.stat5 += request.data['clink']
                tmpTeam.user2.stat6 += request.data['dunk']
            
            tmpTeam.team1Scoreboard += request.data['point']

            return Response(data={"response": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
