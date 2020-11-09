from db.run_sql import run_sql
from models.team import Team
from models.game import Game
from models.league import League
# have imported all classes just in case I need access to them at a later stage

def save(team):
    sql = "INSERT INTO teams(team_name) VALUES ( %s ) RETURNING id;"
    values = [team.team_name]
    results = run_sql( sql, values )
    team.id = results[0]['id']
    return team
# above function will save each team that is created in the console.py file - team1, team2, etc.

def select_all():
    teams = []

    sql = "SELECT * FROM teams;"
    results = run_sql(sql)

    for row in results:
        team = Team(row['team_name'], row['id'])
        teams.append(team)
    return teams
# above will allow all teams to be displayed

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s;"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['team_name'], result['id'])
    return team
# above will allow any specific team to be displayed based on team_id

def delete_all():
    sql = "DELETE FROM teams;"
    run_sql(sql)
# above will delete all teams before the DB is populated

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s;"
    values = [id]
    run_sql(sql, values)
# above will delete any specific team based on team_id