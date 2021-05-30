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