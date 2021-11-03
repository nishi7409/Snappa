from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import *

# Create your views here.
class Logout(APIView):
    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class GenerateUserInformation(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if (User.objects.filter(username=str(request.data.username)).count == 1):
                print("The user has a saved User object")
            elif (User.objects.filter(username=str(request.data.username)).count == 0):
                print("The user does not have a saved User object")
                user = User(username=str(request.data.username), email=str(request.data.email))
                user.save()
            else:
                print("Theoretically, this should **NEVER** be the case (where there are two objects with the same username)")
        print("Huh, how did I get here? (GET request)")