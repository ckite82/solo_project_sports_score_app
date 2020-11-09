import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Aberdeen Roughnecks", "NFC Division 1")

    def test_team_has_name(self):
        self.assertEqual("Aberdeen Roughnecks", self.team.team_name)

    def test_team_has_league(self):
        self.assertEqual("NFC Division 1", self.team.league)
        