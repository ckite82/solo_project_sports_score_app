from db.run_sql import run_sql
from models.league import League
from models.game import Game
from models.team import Team
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
# have imported all classes just in case I need access to them at a later stage

def save(league):
    sql = "INSERT INTO leagues(league_name, team_id) VALUES ( %s, %s ) RETURNING id;"
    values = [league.league_name, league.team.id]
    results = run_sql(sql, values)
    league.id = results[0]['id']
    return league
# above function will save the league that is created in the console.py file

def select_all():
    leagues = []

    sql = "SELECT * FROM leagues;"
    results = run_sql(sql)

    for row in results:
        league = League(row['league_name'], row['team_id'], row['id'])
        leagues.append(league)
    return leagues
# above will allow all leagues to be displayed
# not sure if this function is needed or not

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s;"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['league_name'], result['team_id'], result['id'])
    return league
# above will allow any specific league to be displayed based on league_id
# again, not sure if this function is really required at this stage

def delete_all():
    sql = "DELETE FROM leagues;"
    run_sql(sql)
# above will delete all leagues before the DB is populated

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s;"
    values = [id]
    run_sql(sql, values)
# above will delete any specific league based on league_id
# again, doubt this is required just now