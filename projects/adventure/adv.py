from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Graph, Queue, Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"


# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Helper function to get reverse of given direction
# used in case we can't move in a specified direction and we have to
def reverse_dir(dir):
    if dir == "n":
        return "s"
    elif dir == "s":
        return "n"
    elif dir == "w":
        return "e"
    elif dir == "e":
        return "w"

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room

# we will put all the moves in a stack
moves = Stack()


# end point: the number of visited rooms is the total number of rooms
while len(visited_rooms) < len(world.rooms):
    # get the exits from the current toom
    exits = player.current_room.get_exits()
    # instantiate a list for possible directions
    available_directions = []
    # loop through all the exits from the room
    for exit in exits:
        # if the room in the direction of the exit has not been visited
        # append to available directions
        if (exit is not None) and (player.current_room.get_room_in_direction(exit) not in visited_rooms):
           available_directions.append(exit)
    # set current room as visited
    visited_rooms.add(player.current_room)

    # if there is any direction to move in
    if len(available_directions) > 0:
        # pick a random direction
        random_direction_index = random.randint(0, len(available_directions) -1)
        # push that direction onto moves stack
        moves.push(available_directions[random_direction_index])
        # the player travels in that direction
        player.travel(available_directions[random_direction_index])
        # and we add the direction to the traversal path
        traversal_path.append(available_directions[random_direction_index])

    # otherwise
    # if there are no other available directions
    else:
        # get the last m0ve made
        last_move = moves.pop()
        # the player travels in the reverse direction of last move
        player.travel(reverse_dir(last_move))
        # and we add the move to the traversal path
        traversal_path.append(reverse_dir(last_move))

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
