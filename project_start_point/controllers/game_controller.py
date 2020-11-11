from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.game import Game
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games", __name__)

# INDEX
# GET '/games'
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games = games)

# SHOW
# GET '/games/<id>'
@games_blueprint.route("/games/<id>")
def show(id):
    game = game_repository.select(id)
    teams = game_repository.teams(game)
    return render_template("games/show.html", game = game, teams = teams)

# CREATE
# POST '/games'
# Receive the data from the form to put into the db
# to access info from a form, you need to add "request" to the import from flask request at top of page
# you then access the key of each form input from the new.html file and relevant form method
@games_blueprint.route("/games",  methods=['POST'])
def create_game():
    team1 = request.form['team1']
    team2 = request.form['team2']
    game_week = request.form['game_week']
    league = request.form['league']
    team = request.form['team']

    team = team_repository.select(team_id)
    league = league_repository.select(league_id)
    game = Game(team1, team2, game_week, league)
    game_repository.save(game)
    return redirect('/games')

# SHOW (result)
# GET '/games/<id>' and apply game_winner(id)