from django.db import models
from django.db.models.fields import NullBooleanField, UUIDField, related
from uuid import uuid4

"""
- id --> user id
- username --> user's username
- email --> user's email
- stat1 through 11 --> statistical data that map to leaderboard imports
"""
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

"""
- stat1 through 4 --> statistical data that map to game scores
- totalPoints --> all the stats added up
"""
class GameScoreboard(models.Model):
    totalPoints = models.IntegerField(null=False, blank=False, default=0, editable=True)

"""
- name --> team name
- user1 --> username of first player on team
- user2 --> username of second player on team
- team1Scoreboard --> ManyToMany relationship to GameScoreboard (a team has a scoreboard tracker)
"""
class Team(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    user1 = models.OneToOneField(User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.OneToOneField(User, related_name="user2", on_delete=models.CASCADE)
    team1Scoreboard = models.ManyToManyField(GameScoreboard, related_name="team1Scoreboard")

"""
- team1 --> OneToOne relationship to a team object
- team2 --> OneToOne relationship to another team object
- winner --> OneToOne relationship to the winning team object
"""
class Game(models.Model):
    gameID = models.IntegerField(blank=False, null=False, editable=True, default=0)
    team1 = models.OneToOneField(Team, related_name="team1", on_delete=models.CASCADE)
    team2 = models.OneToOneField(Team, related_name="team2", on_delete=models.CASCADE)
    winnerTeam = models.CharField(blank=False, null=False, editable=True, default="N/A", max_length=256)

"""
(currently not being used-- more for the future)
- option1 through 3 --> specific option triggers for a bracket/team
"""
class LeagueOptions(models.Model):
    option1 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    option2 = models.IntegerField(null=False, blank=False, default=0, editable=True)
    option3 = models.IntegerField(null=False, blank=False, default=0, editable=True)

"""
- ownerUsername --> league owner username
- leagueName --> league name
- leagueOptions --> ManyToMany relationship to LeagueOptions object (not really being utilized right now)
- teamLength --> Integer field representing how many teams exist in league
- allUsers --> ManyToMany relationship to all users in league
- allteams --> ManyToMany relationship to all teams in league
- allGames --> ManyToMany relationship to all games occuring in league
- started --> boolean statement that determines if the league started or not 
"""
class League(models.Model):
    ownerUsername = models.CharField(blank=False, null=False, editable=False, max_length=256)
    leagueName = models.CharField(blank=False, null=False, editable=True, max_length=256)
    leagueOptions = models.ManyToManyField(LeagueOptions)
    teamLength = models.IntegerField(null=False, blank=False, default=0, editable=True)
    allUsers = models.ManyToManyField(User)
    allTeams = models.ManyToManyField(Team)
    allGames = models.ManyToManyField(Game)
    started = models.IntegerField(blank=False, null=False, editable=True, default=0)
    challongeID = models.IntegerField(null=False, blank=False, default=1, editable=True)
    challongeURL = models.CharField(null=False, blank=False, editable=True, default="EMPTY", max_length=256)