from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX
# GET '/teams'
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

# SHOW
# GET '/teams/<id>'
@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select(id)
    game = team_repository.game(team)
    return render_template("teams/show.html", team = team, games = games)

# CREATE
# POST '/teams'
# Receive the data from the form to put into the db
# to access info from a form, you need to add "request" to the import from flask request at top of page
# you then access the key of each form input from the new.html file and relevant form method
@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    team_name = request.form['team_name']

    team = Team(team_name, wins)
    team_repository.save(team)
    return redirect('/teams')


# EDIT
# GET '/teams/<id>/edit'
@teams_blueprint.route("/teams/<id>/edit", methods=["GET"])
def edit_team(id):
    team = team_repository.select(id)
    # users = user_repository.select_all() - this was in the edit function for the tasks.app
    return render_template("teams/edit.html", team = team) #also inside bracket was users = users


# UPDATE
# PUT '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    team_name = request.form['team_name']

    team = Team(team_name, wins)
    team_repository.update(team)
    return redirect("/teams")


# DELETE 
# POST '/teams/<id>'
@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")