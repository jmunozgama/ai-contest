# How to Contribute #

You are here because you want to help improve the contest for the benefit of all. This is a Noble quest, and your efforts are fully encouraged. Here are a few tips and rules, to help keep things from descending into chaos. Please follow them religiously.

## For People Who Are New to the Project ##

You are probably a participant in the AI Challenge. You have some coding experience, and you want to help make the contest better. But you don't know any contest administrators, committers, or contributors. You're not quite sure how to get "in" to the project so that you can start contributing code. This section is for you. Here is how to get "in".
  1. Download an IRC client. This is a program that will allow you to chat with other people working on the contest.
  1. Use your IRC client to connect to irc.freenode.net. Join the room #aichallenge. This is where you will find other contestants, committers, and admins hanging out. Introduce yourself, tell everyone what you want, and ask some questions. Get to know people.
  1. Read the ai-contest project Wiki. You don't have to read it all. Just the stuff that you're curious about. Nothing formal.
  1. Check out the source code and explore it. You can find instructions about how to check out the code under the Source tab.
  1. File an issue. If you find a problem with the contest or you have an idea to make it better, file an issue at http://code.google.com/p/ai-contest/issues/list. You will get a lot more attention if you create a patch file that improves the issue and attach it to the issue as you're filing it. Consult with people in the IRC channel as you go.
  1. Fix someone else's issue. If you see an issue that has no patch file attached, and you think you know how to fix it, give it a try. Leave a comment on the issue and attach a patch file of your changes. People will love you if you do this.
  1. Ask to become a committer. You can do this in the IRC channel. It's probably a good idea to contribute a few changes through patch files before asking for committer access.

## For Contributors ##

You want to contribute code to the contest, but you do not have committer access to the code repository.
  1. Check out the code
  1. Make your changes locally
  1. Test your changes
  1. Create a patch file
  1. Create an issue in the issue tracker with a detailed description of the problem you have solved, and attach the patch file.
  1. Get a committer to make a branch out of your patch, and start a code review on that branch.
  1. If the change is well received, an admin will merge it into trunk, and your changes will go live shortly afterwards.

## For Committers ##

**Do not ever commit any changes to the trunk.** The only people who are allowed to commit to trunk are contest admins. You have committer access, so you _can_ commit to trunk, but you must not. This is not because we don't trust you. You are a great coder, so you feel like you should be allowed to make a small change without bothering to create a whole new branch. But still, you won't do it. Sometimes you see a contest admin make little changes to trunk, but you will not do this, no matter how good a coder you are, and no matter how small a change you are making.

Instead of causing havoc by having a bunch of people all committing to trunk, we will use branches for every change. When you want to make a change, you must follow this procedure.
  1. mkdir mychange (create a directory in which to make your change)
  1. cd mychange (switch to that directory)
  1. svn checkout https://ai-contest.googlecode.com/svn/ . --username myusername (use this command to check out the code instead of the one from the Source tab in Google Code)
  1. svn copy trunk/ branches/mychange/ (create a new branch for your change)
  1. svn commit -m "Creating a new branch to work on mychange. Describe the change and its purpose so that people know what this branch is for." (do not forget this step. It is important that you commit after creating the branch, but before making any changes to the branch)
  1. cd branches/mychange/ (go to your branch)
  1. Make your changes inside your newly created branch.
  1. Compile and test your changes. If necessary, produce some evidence that your changes work as they are meant to.
  1. svn commit -m "Describe your change"

Never run svn commit in the root directory. The root directory is the one that contains trunk, branches, tags, and wiki. This could cause you to accidentally commit a change to trunk. If you do this, the world will end.

Once you have followed the above procedure, you will have a branch which contains perfect code that implements your change. Now you have to get the change code reviewed. If the change gets a positive code review from a contest admin, then the admin will merge the change into trunk, and push the new trunk to the live contest servers. To start the code review:
  1. Click on the "Source" tab in Google Code
  1. Click on "Request code review"
  1. Fill out the form, and select a reviewer. This reviewer does not have to be an admin.
  1. Check out these guidelines: http://code.google.com/p/support/wiki/CodeReviews
  1. If the change gets a positive review from a contest admin, it will be merged with the trunk and pushed to the live contest servers.

This process sounds kind of daunting, but it's not actually that time consuming. It's only a half-dozen extra shell commands. It ends up improving the whole project because
  * There are not a whole bunch of people trying to commit to trunk at the same time
  * It ensures collaboration
  * Every module and corner of the repository is familiar to at least two developers. There are no mysterious corners of the repo that contain code that only one person understands enough to maintain.
  * Raises the quality and maintainability of code, and reduces the number of bugs and undesirable side effects

## For Code Reviewers ##

Dont' be afraid to give a score of "Negative" to a change that you are reviewing if you disagree with it. On the flip side, don't take a negative review personally. Developers need to disagree about the wisdom of changes. There needs to be a lively debate. Negative reviews are a perfectly friendly part of that debate.

If you agree with the change in general, but it's not quite ready to be merged into trunk, assign a score of "Neutral". It is normal for a review to go through several rounds of receiving a Neutral score before being ready to be merged into the trunk. A change should only be merged into trunk once it is
  * well tested
  * perfectly legible and clear, with comments where necessary. Style is important.

Virtually all changes have some kinds in them. The review process usually goes through a few rounds. Once the change is ready to be merged into trunk, give it a Positive review. If the reviewer is not an admin, then an admin will come along at this point and review the change before merging it into trunk.