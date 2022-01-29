from db.run_sql import run_sql
from models.player import Player
# from models.match import Match

def save(player):
    sql = "INSERT INTO players (name, character) VALUES (%s, %s) RETURNING id"
    values = [player.name, player.character]
    results = run_sql(sql, values)
    player.id = results[0]['id']
    return player

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['name'], result['character'], result['id'])
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['name'], row['character'], row['id'])
        players.append(player)
    return players

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)