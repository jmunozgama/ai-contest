# Planet Wars Game Engine #

This page discusses the Planet Wars game engine. How to invoke it, how to interpret its output. To be clear, this page is about the server-side game engine, not the Java game visualizer distributed with the starter packages.

## What is the Game Engine? ##

The Planet Wars game engine is a Python program that plays a game given a map file and a list of bots. It is used to play tournaments between all the submissions that contestants in the AI contest have submitted on the website. The engine is part of the contest back-end. For a broader discussion of the entire contest back-end, see [this article](ContestArchitecture.md).

## Invoking the Engine ##

The engine only compiles and runs under linux-based systems. For best results, use Ubuntu or some similar operating system. Here's how to check out the code, compile it, and invoke the engine:
```
svn checkout http://ai-contest.googlecode.com/svn/trunk/ ai-contest-read-only
cd ai-contest-read-only
make
cd planet_wars/engine
python engine.py ../maps/king_of_the_hill.txt 1000 100 . ./simple_bot . ./simple_bot
```
The above example plays a simple strategy against itself on a simple map.

You can get some information about the arguments accepted by the engine by invoking it without any command-line arguments.

## Interpreting the Output of the Engine ##

The engine outputs general freeform text over the stderr channel. This is mostly debugging information, and can be safely ignored. The main engine output is through the stdout channel, and has a well-defined structure. Each line of output takes the following form:
```
name:value
```
Generally, if the game goes well and terminates normally, the output will look like the following. In the following example, the output indicates that the second player won the game.
```
winner:2
playback:some big long string
```
Here are the currently defined key:value pairs, and what they mean:
  * **winner**: the value is an integer, indicating which player won the game. A value of zero indicates a drawn game. A drawn game usually happens because the game ran past the maximum allowed number of turns without a player winning, and all the players were tied in terms of number of ships.
  * **playback**: the value will be a big long string of funny characters. This string contains information that can used to play back the entire game later. To learn about the format of this string, check out [PlanetWarsFileFormats](PlanetWarsFileFormats.md).
  * **timeout**: the value is an integer, indicating that the given player was disqualified for taking too long to make their move.
  * **fail**: the value is an integer, indicating that the given player was not alive at the end of the game for whatever reason.
  * **minor\_security**: the value is an integer. The engine disqualified the given player for committing what looks like a minor security violation. This should be treated leniently. The tournament manager should probably not instantly disqualify the player, but should assign it a "strike".
  * **major\_security**: the value is an integer. The engine is quite sure that the given player committed a security violation which is intentionally malicious. The tournament manager should consider immediately suspending the offending submission, and maybe even banning the submitting user's account.