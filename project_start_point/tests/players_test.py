import unittest
from models.players import Players

class TestPlayers(unittest.TestCase):

    def setUp(self):
        self.quarter_backs = {
            "Tampa" : "Tom Brady", 
            "Green Bay" : "Aaron Rodgers", 
            "New Orleans" : "Drew Brees", 
            "Seattle" : "Russel Wilson"
            }

    def test_team_has_qb(self):
        name = get_gb_quarter_back_name(self.quarter_backs)
        self.assertEqual("Aaron Rodgers", name)

    def test_tampa_has_qb(self):
        name = get_tampa_quarter_back_name(self.quarter_backs)
        self.assertEqual("Tom Brady", name)

        