class Spot:
    def __init__(self, colour, n):
        self.colour = colour
        self.n = n


# Check if the location is available
def check_availability(pos):
    if (pos[0] < 0) or (pos[1] < 0) or (pos[0] > 7) or (pos[1] > 7):
        return False
    return True


def explosion_range(board, pos):
    exp_range = []
    for row in range(3):
        for col in range(3):
            check_pos = (pos[0] - 1 + col, pos[1] - 1 + row)
            if check_availability(check_pos) and (check_pos != pos):
                exp_range.append(check_pos)
    return exp_range


# Explosion function, will affect the surrounding pieces and recursively explode
def boom(board, pos, black, white):
    if board[pos[0]][pos[1]] is None:
        return
    remove_token(board, pos, black, white)
    affected = explosion_range(board, pos)
    for affected_piece in affected:
        boom(board, affected_piece, black, white)


# Helper function to remove the affected pieces from the board and the black and white lists respectively
def remove_token(board, pos, black, white):
    colour = board[pos[0]][pos[1]].colour
    if colour == 'black':
        black.remove((pos[0], pos[1]))
    elif colour == 'white':
        white.remove((pos[0], pos[1]))
    board[pos[0]][pos[1]] = None


# Move n white/black tokens from old_pos to new_pos
def move(board, n, old_pos, new_pos, colour, pieces):
    if old_pos == new_pos:
        return

    (old_x, old_y) = old_pos
    (new_x, new_y) = new_pos

    board[old_x][old_y].n -= n
    if board[old_x][old_y].n == 0:
        pieces.remove(old_pos)
        board[old_x][old_y] = None

    if board[new_x][new_y] is not None:
        board[new_x][new_y].n += n
    elif board[new_x][new_y] is None:
        board[new_x][new_y] = Spot(colour, n)

    if new_pos not in pieces:
        pieces.append(new_pos)


# Self implement function to list all the possible moves of a given piece
def available_actions(board, colour, pieces):
    actions = []
    for (x, y) in pieces:
        actions.append(("BOOM", (x, y)))
        stack = board[x][y].n
        for d in range(1, stack + 1):
            possible_moves = [(x + d, y), (x, y + d), (x - d, y), (x, y - d)]
            for (new_x, new_y) in possible_moves:
                if check_availability((new_x, new_y)) and \
                        ((board[new_x][new_y] is None) or board[new_x][new_y].colour == colour):
                    actions.append(("MOVE", d, (x, y), (new_x, new_y)))
    return actions
