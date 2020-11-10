import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Aberdeen Roughnecks", 8)

    def test_team_has_name(self):
        self.assertEqual("Aberdeen Roughnecks", self.team.team_name)

    def test_team_has_game_wins(self):
        self.assertEqual(8, self.team.game_wins)
        