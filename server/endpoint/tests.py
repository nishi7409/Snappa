from logging import StringTemplateStyle
from django.test import TestCase
from .models import *

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "ChrisNg", email="chris2001ng@Hotmail.com", stat1=0, stat2=0, stat3=0, stat4=0, stat5=0, stat6=0, stat7=0, stat8=0, stat9=0, stat10=654, stat11=0)
        User.objects.create(username = "Nishi", email="nishipoo@gmail.com", stat1=101, stat2=102, stat3=230, stat4=23, stat5=43, stat6=5, stat7=6, stat8=87, stat9=76, stat10=3542, stat11=3132)
        User.objects.create(username = "vinnypo", email="vinvin@Hotmail.com", stat1=0, stat2=120, stat3=0, stat4=23, stat5=0, stat6=0, stat7=0, stat8=0, stat9=0, stat10=0, stat11=0)
        User.objects.create(username = "jojo", email="jojo@gmail.com", stat1=1012, stat2=1012, stat3=230, stat4=23, stat5=43, stat6=5, stat7=6, stat8=87, stat9=76, stat10=3542, stat11=3132)
        user1 = User.objects.get(username = "ChrisNg")
        user2 = User.objects.get(username = "Nishi")
        user3 = User.objects.get(username = "vinnypo")
        user4 = User.objects.get(username = "jojo")

        GameScoreboard.objects.create(boardid = "score1")
        score1 = GameScoreboard.objects.get(boardid = "score1")
        GameScoreboard.objects.create(boardid = "score2")
        score2 = GameScoreboard.objects.get(boardid = "score2")

        Team.objects.create(name = "CnN", user1 = user1, user2 = user2)
        Team.objects.create(name = "VnJ", user1 = user3, user2 = user4)
        team1 = Team.objects.get(name = "CnN")
        team2 = Team.objects.get(name = "VnJ")
        team1.team1Scoreboard.add(score1)
        team2.team1Scoreboard.add(score2)

        Game.objects.create(gameid = "game1", team1 = team1, team2 = team2, winner = team1)

        League.objects.create(ownerUsername="ChrisNg", leagueName="AmazingLeague", teamLength=10, started=0)

    def test_four_users(self):
        self.assertEqual(len(User.objects.all()), 4)

    def test_user_stats(self):
        user1 = User.objects.get(username = "ChrisNg")
        user2 = User.objects.get(username = "Nishi")
        self.assertEqual(user1.stat1, 0)
        self.assertEqual(user2.stat1, 101)

    def test_league_created(self):
        self.assertEqual(len(League.objects.all()), 1)

    def test_league_created_name(self):
        self.assertEqual(League.objects.get(ownerUsername="ChrisNg").leagueName, "AmazingLeague")

    def test_game(self):
        game = Game.objects.get(gameid = "game1")
        score = game.team1.team1Scoreboard.get(boardid = "score1")
        score.stat1 += 1
        self.assertEqual(score.stat1, 1)

        score.stat1 += 123
        self.assertEqual(score.stat1, 124)