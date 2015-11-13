# Contest Architecture #

This page is designed to answer the following questions:
  * How does the contest back-end work?
  * Which systems make up the contest back-end, and how do they fit together?
  * When a contestant submits their code on the website, where does it go?

![http://csclub.uwaterloo.ca/~j3camero/ContestDataflow.png](http://csclub.uwaterloo.ca/~j3camero/ContestDataflow.png)

_The contest feedback loop. Users submit their code, and within minutes receive feedback in the form of updated rankings._

The following is a list of the biggest systems that comprise the contest backend.
  * [Website](Website.md): the website is how users interact with the contest system.
  * [Auto-Compile System](AutoCompileSystem.md): takes some source code files, figures out which language they're written in, and compiles them.
  * [Tournament Manager](TournamentManager.md): gets the list of currently active submissions. Uses a pairing algorithm to choose pairs of submissions to play against one another. Invokes the [Game Engine](GameEngine.md) to make the game happen. Stores the game outcome in the database, where the [Ranking System](RankingSystem.md) will find it a short while later.
  * [Ranking System](RankingSystem.md): uses a ranking algorithm to compute the best possible rankings, given the list of game outcomes in the database.