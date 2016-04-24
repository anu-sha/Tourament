#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    #connect to database
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #execute query to delete all records
    c.execute("delete from matches") 
    DB.commit()
    #close the connection
    DB.close()
    


def deletePlayers():
    """Remove all the player records from the database."""
    #connect to database
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #execute query to delete all records
    c.execute("delete from players")
    DB.commit()
    #close the connection
    DB.close()



def countPlayers():
    """Returns the number of players currently registered."""
    #connect to the database
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #execute query to select all records
    c.execute("select * from players")
    rows=c.fetchall()
    result=0
    #if the result of the query fetch is null then there are no players in the table
    if not rows:
        result=0
    else:
        result=len(rows)
    DB.commit()
    #close the connection
    DB.close()
    #return the number of rows
    return result

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    #connect to the database
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #execute the insert with the player's name
    add_player=("insert into players(name) values(%s)")
    c.execute(add_player,(name,))
    DB.commit()
    #close the connection
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    #connect to the database and obtain the cursor
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #execute the select query
    c.execute("select * from player_standings")
    #assign the results of the query to players
    players=c.fetchall()
    DB.commit()
    #close the database connection
    DB.close()
    return players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #connect to the database and obtain the cursor
    DB=psycopg2.connect("dbname=tournament")
    c=DB.cursor()
    #use the insert query to add the winner and loser and execute the command
    insert_match='insert into matches values(%s,%s)'
    c.execute(insert_match,(winner,loser))
    #commit the insert
    DB.commit()
    #close the connection
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    #get player standings and iterate over to them
    pairings=[]
    #get player standings
    standings=playerStandings()
    #find the number of players obtained from playerstandings
    player_count=len(standings)
    #iterate over each player incrementing in steps of 2 as we are
    #assigning adjacent players to a game
    for i in range(0,player_count,2):
        #create the tuple for the match
        match_players=(standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1])
        #add the match tuple to the pairings list
        pairings.append(match_players)
    #return the pairings    
    return pairings



