DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255)
);
-- can't recall if I need to add my empty lists, I don't think they are needed, but need to check on this

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    team1 VARCHAR(255),
    team2 VARCHAR(255),
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE 
);
-- not sure if I need to reference my winner object, currently represented as winner = None in the Game class
-- have a look back at the 'on delete cascade' command to remember the reasoning for it

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    league_name VARCHAR(255),
    game_week VARCHAR(255),
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);
-- can't recall if I need to add my empty lists, I don't think they are needed, but need to check on this
-- have a look back at the 'on delete cascade' command to remember the reasoning for it