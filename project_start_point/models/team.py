class Team:
    def __init__(self, team_name, wins = None, id = None):
        self.team_name = team_name
        self.wins = wins
        self.players = []
        self.id = id