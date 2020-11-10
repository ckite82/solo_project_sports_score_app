from db.run_sql import run_sql
from models.game import Game
from models.team import Team
from models.league import League
import repositories.game_repository as game_repository
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
# have imported all classes just in case I need access to them at a later stage

def save(game):
    sql = "INSERT INTO games (team1, team2, game_week, league_id) VALUES ( %s, %s, %s, %s ) RETURNING id;"
    values = [game.team1, game.team2, game.game_week, game.league.id]
    results = run_sql(sql, values)
    game.id = results[0]['id']
    return game
# above function will save each game that is created in the console.py file - game1, game2, etc.

def select_all():
    games = []

    sql = "SELECT * FROM games;"
    results = run_sql(sql)

    for row in results:
        game = Game(row['team1'], row['team2'], row['game_week'], row['league_id'], row['id'])
        games.append(game)
    return games
# above will allow all games to be displayed

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s;"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['team1'], result['team2'], result['game_week'], result['league_id'], result['id'])
    return game
# above will allow any specific game to be displayed based on team_id

def delete_all():
    sql = "DELETE FROM games;"
    run_sql(sql)
# above will delete all games before the DB is populated
# not sure if this function would be required but wanted to have the option available

def delete(id):
    sql = "DELETE FROM games WHERE id = %s;"
    values = [id]
    run_sql(sql, values)
# above will delete any specific game based on team_id
# not sure if this function would be required but wanted to have the option available
