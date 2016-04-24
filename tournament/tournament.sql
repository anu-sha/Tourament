-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--creating the database

create database tournament

--creating the players table

create table players(
	id serial primary key,
	name text)


--create the matches table

create table matches(
	winner integer references players(id),
	loser integer references players(id),
	match_id serial primary key)

--player matches view to return the list of players and total number of matches played

create view player_matches as
	select players.id, players.name, coalesce(count(matches.match_id),0) as num_matches 
	from players left join matches
	on players.id=matches.winner or players.id=matches.loser
	group by players.id
	order by num_matches

--player wind view to return the list of players and their total wins	

create view player_wins as
	select players.id, players.name, coalesce(count(matches.winner),0) as num_wins 
	from players left join matches
	on matches.winner=players.id
	group by players.id
	order by players.id


--player standings view that uses both player_matches and player_wins view to return players,wins and matches
create view player_standings as
	select player_matches.id, player_matches.name, player_wins.num_wins as wins, player_matches.num_matches as matches
	from player_matches join player_wins
	on player_matches.id=player_wins.id
	order by wins desc



	