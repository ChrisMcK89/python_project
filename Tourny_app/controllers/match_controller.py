from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
from models.player import Player
import repositories.match_repostitory as match_repository
import repositories.player_repository as player_repository
import pdb


matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()

    matches_and_players = []
    for match in matches:
        new_dict = {}
        new_dict['match'] = match
        new_dict['player1'] = player_repository.select(match.player1_id)
        new_dict['player2'] = player_repository.select(match.player2_id)
        matches_and_players.append(new_dict)
    

    return render_template("matches/index.html", matches_and_players = matches_and_players)

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
    matches = match_repository.select(id)

    new_dict = {}
    new_dict['match'] = matches
    new_dict['player1'] = player_repository.select(matches.player1_id)
    new_dict['player2'] = player_repository.select(matches.player2_id)

    winner_name = ""

    if int(new_dict['match'].result) == new_dict['player1'].id:
            winner = (new_dict['player1'].name)
            winner_name = winner
    elif int(new_dict['match'].result) == new_dict['player2'].id:
            winner = (new_dict['player2'].name)
            winner_name = winner

    return render_template("matches/show.html", match = new_dict, winner = winner_name)

@matches_blueprint.route("/matches/<id>/p1w")
def result(id):
    match_repository.play_match(id, 1)
    return redirect("/matches")
    

@matches_blueprint.route("/matches/<id>/p2w")
def results(id):
    match_repository.play_match(id, 2)
    return redirect("/matches")
