# Tournament
This app uses a PostgreSQL database and python to manage players in a tournament, the matches between the players and the scoring.

The app currently supports one tournament only. In order to use the same database for another tournament, the data needs to be deleted before new players are added.

#App Contents
##The app contains the following files
1. tournament.sql - Contains all the sql statements to create the database an the tables required for the tournament
2. tournament.py - Contains all the functions that will be required to insert and get data from the database.
3. tournament_test.py - Contains all the tests that in turn call the methods in tournament.py for adding, deleting and getting data from the db.

#To run the app
1. Install [Git](https://git-scm.com/downloads).
2. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
3. Clone this git repository - [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) 
4. Launch the Vagrant VM
5. Change the current working directory to the path containing the files from the app
6  Use \i tournament.sql to import and runt he sql commands to create the databse and tables
7. Use python tournament_test.py to test all the functions in tournament.py. 
8. You can also look [here](https://www.udacity.com/wiki/ud197/install-vagrant) for more detailed instructions on how to install and run Vagrant.


