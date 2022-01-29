from db.run_sql import run_sql
from models.match import Match
from models.player import Player

def create_match(match):
    sql = "INSERT INTO matches (player1_id, player2_id) VALUES (%s, %s) RETURNING *"
    values = [match.player1_id, match.player2_id]
    results = run_sql(sql, values)
    match.id = results[0]['id']
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['player1_id'], result['player2_id'], result['id'])
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        match = Match(row['player1_id'], row['player2_id'], row['id'])
        matches.append(match)
    return matches

