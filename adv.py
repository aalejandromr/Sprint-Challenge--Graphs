from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print(player.current_room)

current_node = 0
queue = Queue()
queue.enqueue(current_node)
stack = Stack()
visited = set()
# test = world.rooms[0]

# print(test.n_to)

while queue.size() > 0:
    #BFT
    current_node = queue.dequeue()

    if current_node in visited:
        # Stop iteration, and last, queue.size() will be 0
        continue

    visited.add(current_node)

    exits_available = world.rooms[current_node].get_exits()

    for exit_ in exits_available:
        next_node = world.rooms[current_node].get_room_in_direction(exit_)
        if next_node.id not in visited:
            queue.enqueue(next_node.id)
            # Stop iteration, and last, queue.size() will be 0
            stack.push((next_node.id, next_node.get_exits()))

    while stack.size() > 0:

        current_move = stack.pop()

        if current_move[0] in visited:
            continue

        visited.add(current_move[0])

        for inner_exists in current_move[1]:
            inner_next_node = world.rooms[current_move[0]].get_room_in_direction(inner_exists)

            if inner_next_node.id not in visited:
                traversal_path.append(inner_exists)
                stack.push((inner_next_node.id, inner_next_node.get_exits()))

print(traversal_path)
print(len(traversal_path))
print(len(visited))
print(len(room_graph))

# Obtengo primer node
# Lo pongo en un queue
# hago dequeue
# lo agrego a visited
# Aqui es donde tengo que agarrar las exists del current_node
# agrego exists al stack
## esto no se: Y volver a generar un numero int random de rango 0 a len(exits) - 1
# Mientras el stack no este vacio
# obtener posibles exits del current_node dentro del otro loop en la current_exit hasta que el stack este vacio
# repetir



# # TRAVERSAL TEST - DO NOT MODIFY
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
