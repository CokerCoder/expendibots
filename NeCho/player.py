from copy import deepcopy

from NeCho.helper import *


class ExamplePlayer:

    def __init__(self, colour):

        self.colour = colour

        self.board = \
            [[Piece("black", 1) if ((y == 6 or y == 7) and (x != 2 and x != 5))
              else Piece("white", 1) if ((y == 0 or y == 1) and (x != 2 and x != 5))
            else None for y in range(8)] for x in range(8)]

        self.black = [(0, 7), (1, 7), (3, 7), (4, 7), (6, 7), (7, 7), (0, 6), (1, 6), (3, 6), (4, 6), (6, 6), (7, 6)]
        self.white = [(0, 1), (1, 1), (3, 1), (4, 1), (6, 1), (7, 1), (0, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0)]

    def action(self):

        possible_actions = available_actions(self.board, self.colour, getattr(self, self.colour))

        # Action Ver 0: Choose random move
        # return possible_actions[randrange(0, len(possible_actions))]

        # Action Ver 1: Choose the move which benefit the most, consider only one move further
        max_point = -9999
        max_action = None
        for possible_action in possible_actions:

            # In the case using a 2D array, deepcopy must be used since a 2D array contains objects and we want the
            # value not by its reference pointer so that we can modify without affecting the original one
            # but this method is slow...
            candidate_board = deepcopy(self)

            if possible_action[0] == 'BOOM':
                boom(candidate_board.board, possible_action[1], candidate_board.black, candidate_board.white)
            elif possible_action[0] == 'MOVE':
                move(candidate_board.board, possible_action[1], possible_action[2], possible_action[3], self.colour,
                     getattr(candidate_board, self.colour))

            # calculate
            point = evaluate(candidate_board.board, self.colour, candidate_board.black, candidate_board.white)
            if point > max_point:
                max_point = point
                max_action = possible_action

        return max_action if max_action else possible_actions[0]

    def update(self, colour, action):

        if action[0] == 'BOOM':
            boom(self.board, action[1], self.black, self.white)
        elif action[0] == 'MOVE':
            move(self.board, action[1], action[2], action[3], colour, getattr(self, colour))
