from django.db import models
from django.db.models.fields import UUIDField, related
from uuid import uuid4

class User(models.Model):
    id = models.UUIDField(blank=False, null=False, primary_key=True, default=uuid4, editable=False)
    username = models.CharField(blank=False, null=False, editable=True, max_length=256)
    email = models.CharField(blank=False, null=False, editable=True, max_length=256)
    stat1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat3 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat4 = models.IntegerField(null=False, blank=False, default=0, editable=True)

class GameScoreboard(models.Model):
    stat1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat3 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat4 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    totalPoints = models.IntegerField(null=False, blank=False, default=0, editable=True)

class Team(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    user1 = models.ForeignKey(User, related_name="user1")
    user2 = models.ForeignKey(User, related_name="user2")
    team1Scoreboard = models.ManyToManyField(GameScoreboard, related_name="team1Scoreboard")

class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name="team1")
    team2 = models.ForeignKey(Team, related_name="team2")
    winner = models.ManyToManyField(Team, related_name="winnerTeam")