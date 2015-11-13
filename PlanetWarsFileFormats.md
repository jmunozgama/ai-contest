# Planet Wars File Formats #

This page contains a specification of all the file formats used in the Planet Wars contest. Currently, there are two. The Point-in-Time Format is used to communicate the state of a game of Planet Wars at a given point of time. It is also used to specify Planet Wars maps, since maps are a starting state for a game. The Game Playback format is used to record an entire game of Planet Wars, for later playback and visualization.



## Planet Wars Point-in-Time Format ##

This is a text format which specifies the state of a game of Planet Wars at a single point in time. This format is used in two main places. The first is to specify Planet Wars maps, since maps are just a starting game state. The second is to communicate between the game engine and the client programs (end-user submissions). Basically, the game engine sends a description of the game state to each client, and waits for orders from each client.

Lines are separated by a single newline character, Linux style. Each line gives information about a planet or an in-transit fleet. Lines that describe a planet start with a character 'P'. Lines that describe a fleet start with a character 'F'. All characters in a line after a '#' character should be ignored by the parser. Blank lines and lines composed only of whitespace are okay. Non-whitespace lines that do not describe a planet or a fleet should generate an error.

Planets have x and y coordinates, an owner, a number of ships, and a growth rate. The coordinates can be any real numbers, and don't have to be integers. The owner is an integer. An owner value of zero indicates that the planet is neutral. The growth rate is the number of new ships that appear on that planet each turn if it is owned by a non-neutral player. For example, here are some valid planet lines:

```
# Some example planets
P 0 0 1 34 2 # Player one's home planet.
P 7 9 2 34 2 # Player two's home planet.
P 3.14 2.71 0 15 5 # A neutral planet with real-number coordinates.
```

Planets are implicitly numbered starting from zero, in the order that they are encountered in the file.

When players give the order to send ships from one planet to another, they create a fleet. Fleets can take several turns to reach their destination, so they become part of the game state while they are in transit. Fleets are represented by lines that start with a character 'F'. A fleet has
  * an owner (integer),
  * a number of ships (integer),
  * a source planet (integer),
  * a destination planet (integer),
  * a total trip length (integer), and
  * a number of turns remaining before arrival (integer).
For example, here is a complete valid file, based on the example planets from above:

```
# Some example planets
P 0 0 1 34 2 # Player one's home planet.
P 7 9 2 34 2 # Player two's home planet.
P 3.14 2.71 0 15 5 # A neutral planet with real-number coordinates.

F 1 15 0 1 12 2 # Player one has sent some ships to attack player two.
F 2 28 1 2 8 4 # Player two has sent some ships to take over the neutral planet.
```

The above example is composed of three planets. One is owned by player one, another is owned by player two. Between them is a neutral planet. In addition to the forces owned by each of the two players on the planets themselves, the two players each have fleets in transit. Player one has a fleet of 15 ships that is about to arrive at player two's home planet. Player two has a fleet of 28 ships that is half way to the neutral planet.

## Planet Wars Playback Format ##

This format is meant to be a complete record of a game of Planet Wars. It will be used primarily to visualize games so that end users can see a playback of their games. Since game playback information will be stored using a string of characters in a MySQL database, newline characters will not be used.

There are two main sections, separated by vertical bar character ('|'). The first section is a description of the starting state of the game, which is just a list of planets. Planets are delimited from each other by colons (':'). The fields of the planets are delimited by commas (','). The second major section is a list of frames, delimited by colon characters.

Each frame is a comma-delimited list. The first n elements specify the current state of each planet, where n is the number of planets. Since the position and size of the planets don't change from one turn to the next, only the owner and the number of ships are specified, like "2.37". The following elements of the list is a list of fleets. The individual fields within each fleet are delimited by periods.