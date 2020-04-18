import math
from copy import deepcopy
import numpy as np

def euclidean(pos1, pos2):
    distance = math.sqrt((pos1[-2] - pos2[-2]) ** 2 + (pos1[-1] - pos2[-1]) ** 2)
    return distance


# Check if the location is available
def check_availability(pos):
    if (pos[0] < 0) or (pos[1] < 0) or (pos[0] > 7) or (pos[1] > 7):
        return False
    return True


def explosion_range(pos):
    exp_range = []
    for row in range(3):
        for col in range(3):
            check_pos = (pos[0] - 1 + col, pos[1] - 1 + row)
            if check_availability(check_pos) and (check_pos != pos):
                exp_range.append(check_pos)
    return exp_range


# Computer the number of systems of a given color that the current state has
def compute_system(state, colour):
    systems = []
    prev = []
    for piece in [tuple(p[1:]) for p in state[colour]]:
        curr_system = compute_system1(state, colour, [], prev, piece)
        if curr_system:
            systems.append(curr_system)
    return len(systems)


# helper function to recursively compute the systems
def compute_system1(state, colour, curr_system, prev, coord):
    if coord in prev:
        return []
    curr_system.append(coord)
    prev.append(coord)

    for exp in explosion_range(coord):
        if exp not in [tuple(p[1:]) for p in state[colour]]:
            continue
        if exp in prev:
            continue
        compute_system1(state, colour, curr_system, prev, exp)
    return curr_system


# Explosion function, will affect the surrounding pieces and recursively explode
def boom(state, pos):
    black = [tuple(b[1:]) for b in state["black"]]
    white = [tuple(w[1:]) for w in state["white"]]
    if pos not in black and pos not in white:
        return
    if pos in black:
        del state["black"][black.index(pos)]
    else:
        del state["white"][white.index(pos)]

    affected = explosion_range(pos)
    for affected_piece in affected:
        boom(state, affected_piece)


# Move n white/black tokens from old_pos to new_pos
def move(state, n, old_pos, new_pos, colour):
    pieces = [tuple(p[1:]) for p in state[colour]]

    # add n to new position
    if new_pos in pieces:
        new_index = pieces.index(new_pos)
        state[colour][new_index][0] += n
    elif new_pos not in pieces:
        state[colour].append([n, new_pos[0], new_pos[1]])

    # remove n from old position
    old_index = pieces.index(old_pos)
    state[colour][old_index][0] -= n
    if state[colour][old_index][0] == 0:
        del state[colour][old_index]


# Self implement function to list all the possible moves of a given piece
def available_actions(state, colour):
    black = [tuple(b[1:]) for b in state["black"]]
    white = [tuple(w[1:]) for w in state["white"]]
    actions = []
    for [n, x, y] in state[colour]:
        actions.append(("BOOM", (x, y)))
        for d in range(1, n + 1):
            possible_moves = [(x + d, y), (x, y + d), (x - d, y), (x, y - d)]
            for (new_x, new_y) in possible_moves:
                if check_availability((new_x, new_y)) and (
                        False if (colour == "black" and (new_x, new_y) in white)
                        else False if (colour == "white" and (new_x, new_y) in black)
                        else True
                ):
                    actions.append(("MOVE", d, (x, y), (new_x, new_y)))
    return actions


def find_token_num(state,colour):
    num = 0
    for token in state[colour]:
        num += token[0]
    return num

def point_in_stack(state,colour):
    num = 0
    for token in state[colour]:
        if token[0] != 0:
            num += 0.7**(token[0])
    return num


# Evaluate function to calculate current board state for a player
# Ver 1.1.1
def evaluate(state, colour):
    if colour == "black":
        enemy = "white"
    else:
        enemy = "black"


    if len(state[colour]) == 0:
        return -10
    elif len(state[enemy]) == 0:
        return 10
    elif len(state[colour]) == len(state[enemy]) and len(state[colour]) == 0:
        return 0
    else:
        enemy_sys = compute_system(state,enemy)
        colour_sys = compute_system(state,colour)
        if len(state[colour]) > enemy_sys:
            colour_enough = 1
        else:
            colour_enough = 0

        if len(state[enemy]) > colour_sys:
            enemy_enough = 1
        else:
            enemy_enough = 0


        points = 1.5*colour_enough-1.5*enemy_enough+\
                 colour_sys-enemy_sys+\
                 find_token_num(state,colour)-find_token_num(state,enemy)+\
                 point_in_stack(state,colour)-point_in_stack(state,enemy)

        # Simply return the difference of their number of tokens
        return points


def is_over(state):
    return True if not state["black"] else True if not state["white"] else False


def new_state(state, colour, action):
    candidate_state = deepcopy(state)

    if action[0] == 'BOOM':
        boom(candidate_state, action[1])
    elif action[0] == 'MOVE':
        move(candidate_state, action[1], action[2], action[3], colour)

    return candidate_state
