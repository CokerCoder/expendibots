from copy import deepcopy
from MCTS.helper import *

class MCTS():

    def __init__(self, state, currentPlayer):

        self.state = state
        self.currentPlayer = currentPlayer


    def getCurrentPlayer(self):
        # 1 for maximiser, -1 for minimiser
        return self.currentPlayer

    def check_availability(self, pos):
        if (pos[0] < 0) or (pos[1] < 0) or (pos[0] > 7) or (pos[1] > 7):
            return False
        return True

    def getPossibleActions(self):

        black = [tuple(b[1:]) for b in self.state["black"]]
        white = [tuple(w[1:]) for w in self.state["white"]]
        actions = []

        colour = "black" if self.currentPlayer == 1 else "white"

        for [n, x, y] in self.state[colour]:
            actions.append(("BOOM", (x, y)))
            for d in range(1, n + 1):
                for w in range(1, n + 1):
                    possible_moves = [(x + w, y), (x, y + w), (x - w, y), (x, y - w)]
                    for (new_x, new_y) in possible_moves:
                        if self.check_availability((new_x, new_y)) and (
                                False if (colour == "black" and (new_x, new_y) in white)
                                else False if (colour == "white" and (new_x, new_y) in black)
                                else True
                        ):
                            actions.append(("MOVE", d, (x, y), (new_x, new_y)))
        return actions


    def takeAction(self, action):
        newState = deepcopy(self)
        if action[0] == "BOOM":
            boom(newState.state, action[1])
        elif action[0] == "MOVE":
            move(newState.state, action[1], action[2], action[3], 
            "black" if self.currentPlayer == 1 else "white")
        newState.currentPlayer = self.currentPlayer * -1
        return newState


    def isTerminal(self):
        if len(self.state["black"]) == 0 or len(self.state["white"]) == 0:
            return True
        return False


    def getReward(self):
        # only needed for terminal states
        if self.state["black"]:
            return 1
        if self.state["white"]:
            return -1
        return 0