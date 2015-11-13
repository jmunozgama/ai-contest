

# Simple RTS #

  * Real-time strategy game
  * Square tiles
  * Each tile is passable or non-passable (land and water)
  * Each unit has some properties
    * HP
    * Firepower
    * Range
    * Speed
  * To make things more complicated...
    * Purchase new units
    * Occupy points of interest
    * Collect resources
    * Take away perfect information

# Chess #

  * Very straight-forward
  * The rules are widely known
  * Lots of resources on the internet

# Tron #

  * This was the game for the Google AI Challenge 2010. Very popular, highly viral.

# Simple Shooter #

  * All ideas are on the table here
  * Could be on a discrete map or a continuous map
  * Could be perfect information or fog-of-war environment
  * Could be maze-like environment or more open
  * Would be interesting if it was multiplayer

# Least Unique Positive Integer #

  * Multiplayer game
  * Each player picks a positive integer. The lowest unique integer wins.
  * Interesting from a game theoretic point of view, but could turn out to have relatively trivial solution.
  * Not very sexy. It's not visual, there are no guns or explosions.

# Maze Escape #

  * Find your way out of a maze with imperfect information.
  * Your character gets dropped into a random position in a maze, and has to find their way out.
  * Could be a discrete tile-based environment or a continuous environment.
  * How much information should the player have? The distance in front of him, and maybe a bit more?

# Go #

  * Very difficult problem.
  * Won't attract many entries, sucks for beginners.
  * However, would draw a lot of interest. It is widely known that Go is a big challenge for AI techniques.

# Blokus #

  * Really interesting turn-based strategy game with high branching factor.
  * Very visual. Makes for great playbacks.
  * Would be like chess, but wouldn't turn into an AlphaBeta pissing contest because of the high branching factor.

# Risk #

  * Classic strategy game.
  * Should we allow inter-player communication? If so, I think this game basically turns into Survivor (see below).

# Rock Paper Scissors #

  * This was the problem from the first ever Google AI Challenge.
  * It's a very deep opponent modeling problem.
  * Trouble is, it's not too terribly interesting.

# Survivor #

  * Game of pure negotiation.
  * Many bots take part. At each round, the bots all vote and one bot is kicked out of the game.
  * Between rounds of voting, the bots have an opportunity to send each other messages.
  * Careful consideration should be given to the sort of messages that the bots are able to send each other.

# Backgammon #

  * Backgammon sucks.

# Canadian Checkers #

  * Just like normal checkers, except on a 10x10 board.
  * 8x8 checkers is solved, but 10x10 is not.

# Multi-Agent Battle #

  * Basically just like the Simple Shooter idea, except each bot gets to control many agents.
  * This could take the form of directing a naval fleet (if we want 2D) or a space-based fleet (if we want 3D).
  * 2D is cool because it's easily visualized in a web browser, and thus easily debugged.
  * 3D is cool because it probably would spur a lot of really neat computational-geometry-based algorithms.

# Billiards #

  * With imperfect information.
  * The bots get to say where they want to aim, but gaussian noise with a known standard deviation is added to their commands.
  * Like a human player, it's all about choosing the best shot which also has some likelihood of turning out as planned.

# Manhunt/Hide&Seek #
  * A two+ player game.
  * One player is called the predator, and the remaining players are called the prey.
  * The goal of the prey could be one of many things - get to a specific region on the map, survive for a certain number of turns, etc.
  * Game is played on a 2D randomly generated map. The catch is that the predator has incomplete information about the location of the prey - they can only see the prey if the prey is within line of sight.
  * The predator (optionally?) knows the layout of the map.
  * The prey on the  other hand can see where the predator is at all times (or not).
  * Each turn, the predator moves up to two squares, and the prey moves up to one square. The prey moves first.
  * If the predator moves on top of any of the prey, that prey is out of the game.

# Scrabble #

Scrabble is one of these games that is not amenable to brute-force Minimax search. Despite years of research, it appears as though competitive humans still slaughter the best Scrabble programs. Scrabble contains many interesting CS problems.

# Hex #

Invented by John Nash. Looks like a really cool game. Since it favors the first player to move, the pie rule must be used for the first move, which could be confusing to contestants. The game is solved up to a size of 9x9, so much bigger boards would have to be used, just to be safe.

# Dots and Boxes #

This is the game that every kid has played on long car rides. Starting with an empty grid of dots, players take turns, adding a single horizontal or vertical line between two unjoined adjacent dots. A player who completes the fourth side of a box earns one point and takes another turn. (The points are typically recorded by placing in the box an identifying mark of the player, such as an initial). The game ends when no more lines can be placed. The winner of the game is the player with the most points.

The game is very familiar to most people, has not been solved except for rather small boards, is not amenable to brute-force Minimax search. The downside is that it may take quite a lot of time for a new contestant to make the jump from random play to somewhat satisfying strategic play. Here are some strategies:
  * Randomly select a legal move.
  * Sort the moves based on the maximum number of sides the modified boxes will have, in the following order: 4, 2, 1, 3. Then choose the best move. Basically, take any trivially completable boxes, and avoid creating boxes with three sides.
  * Minimax search
  * Add reasoning about chains of moves. The endgame often ends up being a bunch of chains, or "hallways" of moves. Reason about these as a whole, rather than worrying about individual moves.

# Reversi #

This is a game where computers have easily beaten the best humans since 1990. On the standard 8x8 board, it is thought that the game is drawn. This makes it a decent candidate as a "fair" game. The downside is that this would turn into a Minimax bakeoff, with very little in the way of innovative algorithms.