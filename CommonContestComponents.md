# Common Contest Components #



Many contests have similar components. This page is a place to discuss such components, with the goal of generalizing them for use with new contests. There is not much point in duplicating effort by having each contest have its own tournament manager, compile pipeline, sandboxing system, etc.

## Submit & Compile System ##

The submit and compile system includes:
  * the "Submit Your Code" form on the contest's website
  * the database that keeps track of the submissions
  * the server-side scripts that identify which language a submission is written in and compile it
  * any crontab entries that keep the compile pipeline moving along

Most contests will want to have a submit and compile system. Chances are, the same exact system will work for just about any contest.

## Health Monitoring Scripts ##

We don't always notice right away when things break or are about to break. It is handy to have some scripts that periodically test whether various different systems are working. For example, we might want to have scripts that test
  * new account creation works
  * code submission works
  * new entries actually show up on the leaderboard and don't get randomly suspended
  * new entries are getting a decent amount of play
  * rankings are stable (with particular attention paid to the top of the leaderboard)
  * disk space usage is not approaching 100% of the allowed limit. This one caused a minor disaster in the Winter 2010 Google AI Challenge, so we want to watch this.

Basically, we want to keep an eye on anything that could go wrong or break. Instead of waiting for the deluge of user complaints on the forums, these sorts of scripts help us to fix things before they break. This can go a long way towards creating a more professional image for the contests, since they won't earn a reputation as being flimsy, flaky, or prone to downtime.

By the way, "just write code that doesn't break", "be more careful", "just avoid doing X" or similar strategies are not serious proposals for reducing downtime and breakages. Automated testing is key. Everybody makes mistakes.

## Starter Packages ##

While each contest needs its own starter packages, those starter packages have some elements in common. In particular, writing input/output code that does not suffer from buffering issues can be much trickier than you think.

It's very important that we not release starter packages that suffer from input/output buffering issues. This can cause endless frustration to potentially hundreds of users, whose submissions are being suspended through no fault of their own. We may want to create a set of standard I/O routines for each of the languages that we commonly support in order to avoid this problem as best we can. This would basically take the form of an implementation of non-buffered writeline() and readline() methods for the most popular languages.

## Sandbox ##

Some sort of library or package to sandbox the execution of untrusted code (such as users' submissions) would be great. That way we don't have to MacGyver something using Systrace or SMACK every time we want to have a new contest. Granted, it isn't that hard to set up. However, it would be great if random people from the internet could write secure contest engines for us without knowing that Systrace or SMACK even exists. This would go a long way towards encouraging community participation.

## Tournament Manager ##

TMs can probably be reused for the majority of contests. Most contests will involve a game where each game is one-on-one, and several games make up a tournament. In these cases, a properly general TM can take 90% of the tedium out of writing a new TM for each contest.

## Website ##

Each contest has to have different content. However, content is by far the easiest and quickest part of the website creation. Ideally, the authors of new contests would spend almost zero time "setting up" the contest's website, and more time writing interesting content for their contest. Most websites will have these elements:
  * leaderboard
  * forums
  * common look-and-feel with the main website
  * navbar
  * login/logout
  * code submission form