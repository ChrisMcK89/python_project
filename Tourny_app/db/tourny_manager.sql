DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  character VARCHAR(255)
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  player1_id INT REFERENCES players(id),
  player2_id INT REFERENCES players(id),
  result INT
);
