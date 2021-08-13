import unittest
from models.league import League

class TestLeague(unittest.TestCase):

    def setUp(self):
        self.league = League("NFC Division 1", "Aberdeen Roughnecks")

    def test_league_has_name(self):
        self.assertEqual("NFC Division 1", self.league.league_name)
        
    def test_league_has_team(self):
        self.assertEqual("Aberdeen Roughnecks", self.league.team)
