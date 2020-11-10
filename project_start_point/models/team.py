class Team:
    def __init__(self, team_name, game_wins, id = None):
        self.team_name = team_name
        self.game_wins = game_wins
        self.players = []
        self.id = id