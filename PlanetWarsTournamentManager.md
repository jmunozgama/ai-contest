# Planet Wars Tournament Manager #

This page discusses the Planet Wars Tournament Manager. It is a script that determines matchups between submissions for the current round and invokes the game engine with each matchup and collects the results.


# What is the Tournament Manager? #
It accesses the contest database once per round to get a list of current submission and generates pairs of submissions. Each pair of submissions is then sent to the game engine for gameplay. The tournament manager then interprets the results and adds an entry to the contest database for each game that occurs.

# Invoking the Tournament Manager #
Before invoking the tournament manager, there must be a file named db\_stuff in the same directory as pw\_mgr.py and it must contain exactly 4 lines in the following order:

dbhost<br>
dbname<br>
user<br>
password<br>

Where dbhost is the name of the host where the database is stored, dbname is the name of the database, user is the username used to access the database and password is that user's password. The lines may not contain any extra characters.<br>
<br>
To invoke the tournament manager, type ./pw_mgr.py