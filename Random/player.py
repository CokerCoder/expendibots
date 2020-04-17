from Random.helper import *
from random import randrange


class ExamplePlayer:
    def __init__(self, colour):
        self.colour = colour
        self.board = \
            [[Spot("black", 1) if ((y == 6 or y == 7) and (x != 2 and x != 5))
              else Spot("white", 1) if ((y == 0 or y == 1) and (x != 2 and x != 5))
            else None for y in range(8)] for x in range(8)]

        self.black = [(0, 7), (1, 7), (3, 7), (4, 7), (6, 7), (7, 7), (0, 6), (1, 6), (3, 6), (4, 6), (6, 6), (7, 6)]
        self.white = [(0, 1), (1, 1), (3, 1), (4, 1), (6, 1), (7, 1), (0, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0)]

    def action(self):

        possible_actions = available_actions(self.board, self.colour, getattr(self, self.colour))
        return possible_actions[randrange(0, len(possible_actions))]

    def update(self, colour, action):

        if action[0] == 'BOOM':
            boom(self.board, action[1], self.black, self.white)
        elif action[0] == 'MOVE':
            move(self.board, action[1], action[2], action[3], colour, getattr(self, colour))
