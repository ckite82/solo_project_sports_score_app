class League:

    def __init__(self, league_name, game_week, team, id = None):
        self.league_name = league_name
        self.game_week = game_week
        self.team = team
        self.schedule = []
        self.standings = []
        self.id = id 
