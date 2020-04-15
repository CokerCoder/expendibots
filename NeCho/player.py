from copy import deepcopy

from NeCho.helper import *


class ExamplePlayer:
    def __init__(self, colour):
        self.colour = colour
        self.board = Board()

    def action(self):

        possible_actions = available_actions(self.board.board, self.colour, getattr(self.board, self.colour))

        # Action Ver 0: Choose random move
        # return possible_actions[randrange(0, len(possible_actions))]

        # Action Ver 1: Choose the move which benefit the most, consider only one move further
        max_point = 0
        max_action = None
        for possible_action in possible_actions:
            candidate_board = Board()
            candidate_board.board = deepcopy(self.board.board)
            candidate_board.black = deepcopy(self.board.black)
            candidate_board.white = deepcopy(self.board.white)

            if possible_action[0] == 'BOOM':
                boom(candidate_board.board, possible_action[1], candidate_board.black, candidate_board.white)
            elif possible_action[0] == 'MOVE':
                move(candidate_board.board, possible_action[1], possible_action[2], possible_action[3], self.colour,
                     getattr(candidate_board, self.colour))

            # calculate
            point = calc_points(candidate_board.board, self.colour)
            if point > max_point:
                max_point = point
                max_action = possible_action

        return max_action

    def update(self, colour, action):

        if action[0] == 'BOOM':
            boom(self.board.board, action[1], self.board.black, self.board.white)
        elif action[0] == 'MOVE':
            move(self.board.board, action[1], action[2], action[3], colour, getattr(self.board, colour))
