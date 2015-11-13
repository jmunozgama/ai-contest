# Introduction #

My idea is basically to stop running the bots on our only server available.
Move all the sandboxes on other servers that were volunteered, these servers don't necessarily need a lot of bandwidth(ex: hypertriangle.com, corn-syrup, a few others). The main server can still have mysqld, httpd and the Tournament Manager, but it doesn't have to consume its CPU for the bots.


# Details #
Each of the servers could have a sandbox setup, and have the main server ssh in a sandbox, copy the bot in it, then run it. Each volunteered node could have multiple of these sandboxes. Example: ssh hypertriangle.com -p 4201 could access the first sandbox on hypertriangle.


# Issues #
  * Uploading/Dowloading of bots to the sandboxes could consume too much bandwidth for the main server. **Comeback:** bandwidth for the server is 4TB/month, bandwidth for hypertriangle is 200GB/month, the nodes will have that issue much sooner.

**Implication for node owners:**
  * They can't compete.
  * There might be security problems associated with this.

# Bandwidth Usage Estimate #

A glance at the existing submissions reveals that a safe upper bound on the average size of an uncompressed submission is 1 MB.

## Sandboxes ##
Bandwidth cost for **each sandbox** from nodes (assuming 1MB/bot and 100 steps(1 second each)/game):

**26.2GB**: http://www.wolframalpha.com/input/?i=1MB+/+(1sec+*++100)+*+month

**Note:** This figure can go up dramatically because bots might be a lot faster than 1 second per turn.

Multiply this by the number of sandboxes you want to have on your node.

## Main Server ##
As of right now, we are averaging about 12 games per minute. Call it 15. Therefore the bandwidth would be:

**1.296 TB/month**: http://www.wolframalpha.com/input/?i=(2+*+1MB+*+15/minute)+*+month.

This is a sizeable portion of our allowed bandwidth per month (currently 4 TB/month). It's a risk that we might use too much bandwidth, but we won't risk going over our cap in the first few days. Therefore it is not very risky to implement decentralization right now. Also, we can probably get scp to do a bit of compression on the bots to reduce the impact.