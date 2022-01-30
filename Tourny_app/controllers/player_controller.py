from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players = players)

@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select(id)
    return render_template("players/show.html", player = player)

@players_blueprint.route("/players/newplayer", methods=['GET'])
def new_player():
    return render_template("players/newplayer.html")


@players_blueprint.route("/players", methods=['POST'])
def create_player():
    name = request.form['name']
    character = request.form['character']
    player = Player(name, character)
    player_repository.save(player)
    return redirect("/players")
    