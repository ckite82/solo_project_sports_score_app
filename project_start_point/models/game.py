class Game:

    def __init__(self, team1, team2, league, winner = None, id = None):
        self.team1 = team1
        self.team2 = team2 
        self.league = league
        self.winner = winner
        self.id = id 

# do I need to create objects for a team3 and team4?
# given that a game is only played between two teams, I shouldn't
