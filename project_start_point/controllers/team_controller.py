from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select(id)
    game = team_repository.game(team)
    return render_template("teams/show.html", team = team, games = games)
# not sure i understand this route fully, need to review again.
