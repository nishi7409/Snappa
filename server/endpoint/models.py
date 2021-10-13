from django.db import models
from django.db.models.fields import UUIDField

class Scoreboard(models.Model):
    stat1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat3 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat4 = models.IntegerField(null=False, blank=False, default=0, editable=True)

class User(models.Model):
    # id = models.UUIDField(blank=False, null=False, primary_key=True, default=UUIDField.uuid4, editable=False)
    firstName = models.CharField(blank=False, null=False, editable=True, max_length=255)
    lastName = models.CharField(blank=False, null=False, editable=True, max_length=255)
    username = models.CharField(blank=False, null=False, editable=True, max_length=10)
    phoneNumber = models.IntegerField(null=False, blank=False, editable=True)
    email = models.CharField(blank=False, null=False, editable=True, max_length=255)
    # gameHistory = models.ManyToManyField(Game)

class Team(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    user1 = models.ManyToManyField(User, related_name="User_1")
    user2 = models.ManyToManyField(User, related_name="User_2")
    scoreboard = models.ManyToManyField(Scoreboard)

class Game(models.Model):
    team1 = models.ManyToManyField(Team, related_name="Team_1")
    team2 = models.ManyToManyField(Team, related_name="Team_2")
    scoreboard = models.ManyToManyField(Scoreboard)