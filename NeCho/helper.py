# Check if the location is available
def check_availability(pos):
    if (pos[0] < 0) or (pos[1] < 0) or (pos[0] > 7) or (pos[1] > 7):
        return False
    return True


def explosion_range_new(pos, board):
    list2 = []
    for row in range(3):
        for col in range(3):
            check_pos = (pos[0] - 1 + col, pos[1] - 1 + row)
            if check_availability(check_pos) and (not (row == col == 1)) and (board[check_pos[0]][check_pos[1]] is not None):
                list2.append(check_pos)
    return list2


# Explosion function, will affect the surrounding tokens and recursively explode
def boom(board, pos, black, white):
    if board[pos[0]][pos[1]] is None:
        return
    remove_token(board, pos, black, white)
    affected = explosion_range_new(pos, board)
    for affected_token in affected:
        boom(board, affected_token, black, white)


# Helper function to remove the affected tokens from the board dic and the black and white token lists respectively
def remove_token(board, pos, black, white):
    colour = board[pos[0]][pos[1]].colour
    if colour == 'black':
        black.remove((pos[0], pos[1]))
    elif colour == 'white':
        white.remove((pos[0], pos[1]))
    board[pos[0]][pos[1]] = None
