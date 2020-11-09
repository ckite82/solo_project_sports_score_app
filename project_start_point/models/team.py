class Team:
    def __init__(self, team_name, league, id = None):
        self.team_name = team_name
        self.league = league
        self.players = []
        self.id = id