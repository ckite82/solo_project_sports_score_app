from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.game import Game
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games", __name__)

@game_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games = games)

@game_blueprint.route("/games/<id>")
def show(id):
    game = game_repository.select(id)
    teams = game_repository.teams(game)
    return render_template("games/show.html", game = game, teams = teams)
# not sure i understand this route fully, need to review again.