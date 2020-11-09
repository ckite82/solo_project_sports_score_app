from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.league import League
import repositories.league_repository as league_repository
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

league_blueprint = Blueprint("league", __name__)

@league_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues = leagues)

# NEW
# GET '/leagues/new'
@leagues_blueprint.route("/leagues/new", methods=['GET'])
def new_task():
    teams = team_repository.select_all()
    games = game_repository.select_all()
    return render_template("leagues/new.html", teams = teams, games = games)

# need to get my head around what routes are actually required, need to get started on html for now.
