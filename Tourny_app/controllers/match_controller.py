from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
from models.player import Player
import repositories.match_repostitory as match_repository
import repositories.player_repository as player_repository


matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches = matches)

@matches_blueprint.route("/matches/create", methods=['GET'])
def new_match():
    players = player_repository.select_all()
    return render_template("matches/create.html", all_players = players)

@matches_blueprint.route("/matches", methods=['POST'])
def post_create_match():
    player_1 = request.form['player_1']
    player_2 = request.form['player_2']
    match = Match(player_1, player_2)
    match_repository.create_match(match)
    return redirect("/matches")

@matches_blueprint.route("/matches/<id>")
def show(id):
    match = match_repository.select(id)
    return render_template("matches/show.html", match = match)