import random
from models.team import Team

class Game:

    def __init__(self, team1, team2, game_week, league, winner = None, id = None):
        self.team1 = team1
        self.team2 = team2 
        self.game_week = game_week
        self.league = league
        self.winner = winner
        self.id = id 

    def game_winner(self):
        winner = random.randint(0,1)
        if 0 == winner:
            self.winner = self.team1
        else:
            self.winner = self.team2

    # def game_winner(self):
    #     winner = None
    #     if team1 == 0 and team2 == 1:
    #         winner = random.randint(0,1)
    #     return winner
    
