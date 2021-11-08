from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('createUserObject/', GenerateUserObject.as_view()),
    path('getUserStats/', GenerateUserStats.as_view()),
]
