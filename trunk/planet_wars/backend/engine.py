import math
import os
import signal
import shlex
import subprocess
import time
from user_sadbox import Sadbox

# Reads a text file that contains a game state, and returns the game state. A
# game state is composed of a list of fleets and a list of planets.
#   map: an absolute or relative filename that point to a text file.
def read_map_file(map):
  fleets = []
  planets = []
  f = open(map)
  for line in f:
    tokens = line.lower().strip().split(" ")
    if len(tokens) == 0:
      pass
    elif tokens[0] == "p":
      planets.append({
        "x" : float(tokens[1]),
        "y" : float(tokens[2]),
        "owner" : int(tokens[3]),
        "num_ships" : int(tokens[4]),
        "growth_rate" : int(tokens[5])
      })
    elif tokens[0] == "f":
      fleets.append({
        "owner" : int(tokens[1]),
        "num_ships" : int(tokens[2]),
        "source" : int(tokens[3]),
        "destination" : int(tokens[4]),
        "total_trip_length" : int(tokens[5]),
        "turns_remaining" : int(tokens[6])
    })
  return planets, fleets

# Carries out the point-of-view switch operation, so that each player can
# always assume that he is player number 1. There are three cases.
# 1. If pov < 0 then no pov switching is being used. Return player_id.
# 2. If player_id == pov then return 1 so that each player thinks he is
#    player number 1.
# 3. If player_id == 1 then return pov so that the real player 1 looks like
#    he is player number "pov".
# 4. Otherwise return player_id, since players other than 1 and pov are
#    unaffected by the pov switch.
def switch_pov(player_id, pov):
  if pov < 0:
    return player_id
  if player_id == pov:
    return 1
  if player_id == 1:
    return pov
  return player_id

# Generates a string representation of a planet. This is used to send data
# about the planets to the client programs.
def serialize_planet(p, pov):
  owner = switch_pov(int(p["owner"]), pov)
  message = "P " + str(p["x"]) + " " + str(p["y"]) + " " + str(owner) + \
    " " + str(int(p["num_ships"])) + " " + str(int(p["growth_rate"]))
  return message.replace(".0 ", " ")

# Generates a string representation of a fleet. This is used to send data
# about the fleets to the client programs.
def serialize_fleet(f, pov):
  owner = switch_pov(int(f["owner"]), pov)
  message = "F " + str(owner) + " " + str(int(f["num_ships"])) + " " + \
    str(int(f["source"])) + " " + str(int(f["destination"])) + " " + \
    str(int(f["total_trip_length"])) + " " + str(int(f["turns_remaining"]))
  return message.replace(".0 ", " ")

# Gets a list of orders from the given client.
def get_orders_from_client(client):
  orders = []
  while True:
    line = client.read_line()
    if line is None:
      time.sleep(0)
      continue
    if line.lower() == "go":
      break
    tokens = line.split(" ")
    if len(tokens) == 3:
      orders.append({
        "source" : int(tokens[0]),
        "destination" : int(tokens[1]),
        "num_ships" : int(tokens[2])
      })
  return orders

# Calculates the travel time between two planets. This is the cartesian
# distance, rounded up to the nearest integer.
def travel_time(a, b):
  dx = b["x"] - a["x"]
  dy = b["y"] - a["y"]
  return int(math.ceil(math.sqrt(dx * dx + dy * dy)))

# Processes the given order, as if it was given by the given player_id. If
# everything goes well, returns True. Otherwise, returns False.
def issue_order(order, player_id, planets, fleets, order_strings):
  source_planet = planets[order["source"]]
  destination_planet = planets[order["destination"]]
  if source_planet["owner"] != player_id:
    return False
  if order["num_ships"] > source_planet["num_ships"]:
    return False
  source_planet["num_ships"] -= order["num_ships"]
  t = travel_time(source_planet, destination_planet)
  fleets.append({
    "source" : order["source"],
    "destination" : order["destination"],
    "num_ships" : order["num_ships"],
    "owner" : source_planet["owner"],
    "total_trip_length" : t,
    "turns_remaining" : t
  })
  order_strings.append(str(order["source"]) + "." + \
    str(order["destination"]) + "." + str(order["num_ships"]))

# "a" is an array. This method returns the number of non-zero elements in a.
def num_non_zero(a):
  return len([x for x in a if x != 0])

# Performs the logic needed to advance the state of the game by one turn.
# Fleets move forward one tick. Any fleets reaching their destinations are
# dealt with. If there are any battles to be resolved, then they're taken
# care of.
def do_time_step(planets, fleets):
  attackers = dict()
  traveling_fleets = []
  for f in fleets:
    f["turns_remaining"] -= 1
    if f["turns_remaining"] > 0:
      traveling_fleets.append(f)
    else:
      dest = f["destination"]
      owner = f["owner"]
      if dest not in attackers:
        attackers[dest] = dict()
      if owner not in attackers[dest]:
        attackers[dest][owner] = 0
      attackers[dest][owner] += f["num_ships"]
  fleets = traveling_fleets
  for i, p in enumerate(planets):
    if i not in attackers:
      continue
    defender = p["owner"]
    defending_forces = p["num_ships"]
    if defender in attackers[i]:
      defending_forces += attackers[i][defender]
      del attackers[i][defender]
    attacking_players = [key for key, value in attackers[i].items()]
    attacking_forces = [value for key, value in attackers[i].items()]
    current_attacker = 0
    while defending_forces > 0 and sum(attacking_forces) > 0:
      if attacking_forces[current_attacker] == 0:
        continue
      attacking_forces[current_attacker] -= 1
      defending_forces -= 1
      current_attacker += 1
      if current_attacker >= len(attacking_players):
        current_attacker = 0
    if sum(attacking_forces) > 0:
      while num_non_zero(attacking_forces) > 1:
        if attacking_forces[current_attacker] == 0:
          continue
        attacking_forces[current_attacker] -= 1
        if current_attacker >= len(attacking_players):
          current_attacker = 0
      for i in range(len(attacking_players)):
        if attacking_forces[i] > 0:
          p["owner"] = attacking_players[i]
          p["num_ships"] = attacking_forces[i]
    else:
      p["owner"] = defender
      p["num_ships"] = defending_forces
  return planets, fleets

# Calculates the number of players remaining
def remaining_players(planets, fleets):
  players = set()
  for p in planets:
    players.add(p["owner"])
  for f in fleets:
    players.add(f["owner"])
  players.discard(0)
  return players

# Returns a string representation of the entire game state.
def serialize_game_state(planets, fleets, pov):
  message = "\n".join([serialize_planet(p, pov) for p in planets]) + \
    "\n" + "\n".join([serialize_fleet(f, pov) for f in fleets]) + "\ngo\n"
  return message.replace("\n\n", "\n")

# Turns a list of planets into a string in playback format. This is the initial
# game state part of a game playback string.
def planet_to_playback_format(planets):
  planet_strings = []
  for p in planets:
    planet_strings.append(str(p["x"]) + "," + str(p["y"]) + "," + \
      str(p["owner"]) + "," + str(p["num_ships"]) + "," + \
      str(p["growth_rate"]))
  return ":".join(planet_strings)

# Turns a list of planets into a string in playback format. This is the initial
# game state part of a game playback string.
def fleets_to_playback_format(planets):
  fleet_strings = []
  for p in planets:
    fleet_strings.append(str(p["owner"]) + "." + str(p["num_ships"]) + "." + \
      str(p["source"]) + "." + str(p["destination"]) + "." + \
      str(p["total_trip_length"]) + "." + str(p["turns_remaining"]))
  return ",".join(planet_strings)

# Represents the game state in frame format. Represents one frame.
def frame_representation(planets, fleets):
  planet_string = \
    ",".join([str(p["owner"]) + "." + str(p["num_ships"]) for p in planets])
  return planet_string + "," + fleets_to_playback_format(fleets)

# Plays a game of Planet Wars.
#   map: a full or relative path to a text file containing the map that this
#        game should be played on.
#   max_turn_time: the maximum amount of time each player gets to finish each
#                  turn. A player forfeits the game if they run over their
#                  time allocation.
#   max_turns: the max length of a game in turns. If the game isn't over after
#              this many turns, the player with the most ships wins.
#   players: a list of dictionaries, each of which has information about one
#            of the players. Each dictionary should have the following keys:
#            path: the path where the player's files are located
#            command: the command that invokes the player, assuming the given
#                     path is the current working directory.
def play_game(map, max_turn_time, max_turns, players):
  planets, fleets = read_map_file(map)
  playback = planet_to_playback_format(planets) + "|"
  clients = []
  print "starting client programs"
  for i, p in enumerate(players):
    client = Sadbox(working_directory=p["path"],
                    shell_command=p["command"],
                    security_on=True)
    if client.is_alive:
      print "    started player " + str(i+1)
      clients.append(client)
    else:
      print "    failed to start player " + str(i+1)
  print "waiting for players to spin up"
  time.sleep(3)
  turn_number = 1
  turn_strings = []
  while turn_number <= max_turns and \
    len(remaining_players(planets, fleets)) > 1:
    order_strings = []
    for i, c in enumerate(clients):
      message = serialize_game_state(planets, fleets, i+1)
      print "engine > player" + str(i+1) + ":"
      print message
      c.write(message)
    time.sleep(1)
    for i, c in enumerate(clients):
      print "getting orders from player " + str(i+1)
      orders = get_orders_from_client(c)
      for order in orders:
        issue_order(order, i+1, planets, fleets, order_strings)
    planets, fleets = do_time_step(planets, fleets)
    turn_strings.append(frame_representation(planets, fleets))
    turn_number += 1
  for c in clients:
    c.kill()
  playback += ":".join(turn_strings)
  victors = remaining_players(planets, fleets)
  outcome = dict()
  if len(victors) == 1:
    outcome["winner"] = victors.pop()
  else:
    outcome["winner"] = 0
  outcome["playback"] = playback
  return outcome

def main():
  players = [
    {"path" : "../submissions/122743/.", "command" : "java -jar MyBot.jar"},
    {"path" : "../submissions/122743/.", "command" : "java -jar MyBot.jar"}
  ]
  print "game result: " + \
    str(play_game("../maps/king_of_the_hill.txt", 1000, 10, players))

if __name__ == "__main__":
  main()