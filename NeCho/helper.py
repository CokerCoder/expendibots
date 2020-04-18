import math


# Calculate the euclidean distance between 2 tokens, given as (x, y) format.
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


# Evaluate function to calculate current board state for a player
# Ver 1.1.1
def evaluate(state, colour):
    points = len(state["black"]) - len(state["white"])
    # Simply return the difference of their number of tokens
    return points if colour == "black" else -points
