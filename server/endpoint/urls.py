from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('createUser/', GenerateUserObject.as_view()),
    path('createLeague/', LeagueCreate.as_view()),
    path('leagueAddUser/', LeagueAddUser.as_view()),
    path('allLeagueUsers/', GetActiveLeagueUsers.as_view()),
    path('doesLeagueExist/', DoesLeagueExist.as_view()),
    path('submitLeague/', SubmitLeague.as_view())
]