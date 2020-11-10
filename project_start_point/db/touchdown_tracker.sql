DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS leagues;


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    game_wins INTEGER
);
-- can't recall if I need to add my empty lists


CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    league_name VARCHAR(255),
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);
-- have a look back at the 'on delete cascade'


CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    team1 VARCHAR(255),
    team2 VARCHAR(255),
    game_week VARCHAR(255),
    winner VARCHAR(255),
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);
-- not sure if I need to reference my winner object, currently represented as 'winner = None' in the Game class
-- have a look back at the 'on delete cascade' command to remember the reasoning for it