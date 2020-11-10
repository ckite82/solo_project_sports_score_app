import unittest
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Team1", "Team2", "game week 8", "NFC Division 1")

    def test_game_has_team1(self):
        self.assertEqual("Team1", self.game.team1)

    def test_game_has_team2(self):
        self.assertEqual("Team2", self.game.team2)

    def test_game_has_game_week(self):
        self.assertEqual("game week 8", self.game.game_week) 

    def test_game_has_league(self):
        self.assertEqual("NFC Division 1", self.game.league)
        