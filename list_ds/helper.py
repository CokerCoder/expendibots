import math
import numpy as np


def convert_pos(pos):
    return (7-pos[1])*8+pos[0]


def convert_index(index):
    return (index%8, 7-index//8)


def euclidean(pos1, pos2):
    distance = math.sqrt((pos1[-2] - pos2[-2]) ** 2 + (pos1[-1] - pos2[-1]) ** 2)
    return distance


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


def boom(state, pos):

    if state[convert_pos(pos)] == 0:
        return
    
    state[convert_pos(pos)] = 0

    affected = explosion_range(pos)
    for affected_piece in affected:
        boom(state, affected_piece)


def move(state, n, old_pos, new_pos, colour):

    # add n to new position
    new_index = convert_pos(new_pos)
    state[new_index] += colour * n

    # remove n from old position
    old_index = convert_pos(old_pos)
    state[old_index] -= colour * n


def available_actions(state, colour):

    actions = []

    for idx, val in enumerate(state):

        if val*colour <= 0:
            continue

        x, y = convert_index(idx)

        actions.append(("BOOM", (x, y)))
        for d in range(1, abs(val) + 1):
            for w in range(1, abs(val) + 1):
                adj_cells = [(x + w, y), (x, y + w), (x - w, y), (x, y - w)]
                for (new_x, new_y) in adj_cells:
                    if check_availability((new_x, new_y)) and state[convert_pos((new_x, new_y))]*colour >= 0:
                        actions.append(("MOVE", d, (x, y), (new_x, new_y)))
    return actions


def distance(state):

    black = []
    white = []
    for idx, val in enumerate(state):
        if val > 0:
            black.append(convert_index(idx))
        if val < 0:
            white.append(convert_index(idx))

    minimum_dis = float("inf")
    total_dis = 0
    total = 0

    for b in black:
        for w in white:
            dis = euclidean(b, w)
            total_dis += dis
            total += 1
            if dis < minimum_dis:
                minimum_dis = dis
    
    avg_distance = total_dis / total

    return minimum_dis, avg_distance


def attack_range(state):
    
    return 0


def feature_set(state, colour):

    num_diff = sum(state) * colour 
    
    minimum_dis, avg_dis = 0, 0

    attack_diff = 0

    return [num_diff, minimum_dis, avg_dis]


# Evaluate function to calculate current board state for a player
# Ver 2.0
def evaluate(state, colour):

    # if lose
    if (colour==1 and colour*max(state)<=0) or (colour==-1 and colour*min(state)<=0):
        return float('-inf')

    # if win
    elif (colour==1 and colour*min(state)>=0) or (colour==-1 and colour*max(state)>=0):
        return float('inf')

    # if draw
    elif len(set(state)) == 0:
        return 0

    features = np.array(feature_set(state, colour))

    coeff = [1, 0, 0]

    _coeff = np.array(coeff)

    # Using simple linear model
    points = np.dot(features, _coeff)
    
    return points


def is_over(state):
    return True if (max(state)<=0 or min(state)>=0) else False


def new_state(state, colour, action):
    candidate_state = state[:]

    if action[0] == 'BOOM':
        boom(candidate_state, action[1])
    elif action[0] == 'MOVE':
        move(candidate_state, action[1], action[2], action[3], 1 if colour=="black" else -1)

    return candidate_state
