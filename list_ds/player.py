from list_ds.helper import *
from list_ds.agent import MinimaxABAgent

class ExamplePlayer:

    def __init__(self, colour):

        self.colour = 1 if colour == "black" else -1
        self.state = [
                        1, 1, 0, 1, 1, 0, 1, 1,
                        1, 1, 0, 1, 1, 0, 1, 1,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        -1, -1, 0, -1, -1, 0, -1, -1,
                        -1, -1, 0, -1, -1, 0, -1, -1,
                    ]

    def action(self):

        # Choose appropriate depth based on the number of pieces left on the board
        num_pieces = sum([abs(x) for x in self.state])
        
        if num_pieces > 15:
            minimax_agent = MinimaxABAgent(2, self.colour)
        elif 13 <= num_pieces <= 15:
            minimax_agent = MinimaxABAgent(3, self.colour)
        elif 7 <= num_pieces <= 12:
            minimax_agent = MinimaxABAgent(4, self.colour)
        elif 4 <= num_pieces <= 6:
            minimax_agent = MinimaxABAgent(7, self.colour)
        elif 1 <= num_pieces <= 3:
            minimax_agent = MinimaxABAgent(9, self.colour)
        else:
            minimax_agent = MinimaxABAgent(1, self.colour)

        action = minimax_agent.choose_action(self.state)

        return action


    def update(self, colour, action):
        if action[0] == 'BOOM':
            boom(self.state, action[1])
        elif action[0] == 'MOVE':
            move(self.state, action[1], action[2], action[3], 1 if colour=="black" else -1)
