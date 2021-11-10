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
    stat5 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat6 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat7 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat8 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat9 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat10 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat11 = models.IntegerField(null=False, blank=False, default=0, editable=True)

class GameScoreboard(models.Model):
    stat1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat3 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    stat4 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    totalPoints = models.IntegerField(null=False, blank=False, default=0, editable=True)

class Team(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    user1 = models.OneToOneField(User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.OneToOneField(User, related_name="user2", on_delete=models.CASCADE)
    team1Scoreboard = models.ManyToManyField(GameScoreboard, related_name="team1Scoreboard")

class Game(models.Model):
    team1 = models.OneToOneField(Team, related_name="team1", on_delete=models.CASCADE)
    team2 = models.OneToOneField(Team, related_name="team2", on_delete=models.CASCADE)
    winner = models.OneToOneField(Team, related_name="winnerTeam", on_delete=models.CASCADE)

class LeagueOptions(models.Model):
    option1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    option2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    option3 = models.IntegerField(null=False, blank=False, default=0, editable=True)

class League(models.Model):
    ownerUsername = models.CharField(blank=False, null=False, editable=False, max_length=256)
    leagueName = models.CharField(blank=False, null=False, editable=True, max_length=256)
    leagueOptions = models.ManyToManyField(LeagueOptions)
    allUsers = models.ManyToManyField(User)
    allTeams = models.ManyToManyField(Team)
    allGames = models.ManyToManyField(Game)
