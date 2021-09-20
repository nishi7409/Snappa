from django.db import models
from django.db.models.fields import UUIDField


class User(models.Model):
    id = models.UUIDField(blank=False, null=False, primary_key=True, default=UUIDField.uuid4, editable=False)
    firstName = models.CharField(blank=False, null=False, editable=True)
    lastName = models.CharField(blank=False, null=False, editable=True)
    username = models.CharField(blank=False, null=False, editable=True)
    phoneNumber = models.IntegerField(null=False, blank=False, editable=True)
    email = models.CharField(blank=False, null=False, editable=True)
    gameHistory = models.ManyToManyField(Game)

class Team(models.Model):
    name = models.CharField(null=False, blank=False)
    user1 = models.ManyToManyField(User)
    user2 = models.ManyToManyField(User)
    scoreboard = models.ManyToManyField(Scoreboard)

class Game(models.Model):
    team1 = models.ManyToManyField(Team)
    team2 = models.ManyToManyField(Team)
    scoreboard = models.ManyToManyField(Scoreboard)
    
class Scoreboard(models.Model):
    stat1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat3 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat4 = models.IntegerField(null=False, blank=False, default=0, editable=True)
