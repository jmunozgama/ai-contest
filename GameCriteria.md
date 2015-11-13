# Game Criteria #



Whenever we put on a new contest, the first step is to choose a contest problem. In these AI contests, the problem generally takes the form of a simple game. This page contains some guidelines and criteria for evaluating the quality of proposed contest problems.

Whenever making an argument about the quality of a game, consider referring to these criteria or some other reasonable set of criteria. Whenever attempting to argue that some game is better than another game, consider structuring your argument around these criteria.

## Easy ##

Hard problems are scary. Even if a problem is familiar and interesting, people will still walk away if they think that
  * they are unable to create a serious entry, or
  * it would take too much time to create a serious entry.

## Familiar ##

People are more likely to participate in a contest if they are more familiar with the problem. Familiar games include Rock Paper Scissors, Chess, Survivor, and Billiards. Unfamiliar games include Least Unique Positive Integer and Blokus.

The key questions are
  * What percentage of people recognize the game's name?
  * What percentage of people would call themselves somewhat familiar with the rules or basic premise of the game?

Here, "people" is understood to mean "people who have at least basic programming experience". We don't care whether your mom would recognize the game, because there's no way she is going to participate in the contest anyways.

## Interesting ##

Interesting problems are those that a large percentage of people with basic programming experience will enjoy reading about. Taking a straw poll among the contest staff or some other group of programmers is usually a good way to measure the level of interest in a problem.

Invalid ways to measure the interesting-ness of a problem include:
  * your personal level of interest in the problem
  * the depth or elegance of the problem in game-theoretic terms
  * how many papers have been written about the game

What matters is what percentage of people with basic programming experience would see the problem on the internet and say "Oh cool!".

Examples of sexy problems are Go, Real-Time Strategy games, and Tron. A good example of an un-sexy problem is Least Unique Positive Integer. It's deeply awesome from a game-theoretic point of view, but it's unlikely to catch fire and go viral on the internet.

## Technically Feasible ##

In an ideal world, this would not be a factor. Sadly, in the real world it is. It's important to consider
  * whether we can run the contest using the resources we have available, and
  * the amount of time it takes to implement the contest.

Keep in mind that there is a tradeoff between
  * the computational intensity of accurately testing an entry, and
  * the speed with which we can deliver quality feedback to contestants.

## Non-trivial ##

Make really sure that there is no way to "solve" the problem. It's bad if partway through the contest someone comes up with "the best possible solution". If many people find a perfect or near-perfect solution, the rankings at the top of the leaderboard become random for all practical purposes.

Games like Tic-Tac-Toe are obvious examples of bad choices. However, even deep games like Rock Paper Scissors can turn into a disaster, since there are solutions that are very close to being perfect, even if they're not exactly perfect.

## Fun to Watch ##

A big booster of interest in the contest is interesting visualizations.