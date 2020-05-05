from MCTS.agent import MCTS
from MCTS.mcts import mcts
from MCTS.helper import *


class ExamplePlayer:

    def __init__(self, colour):

        self.currentPlayer = 1 if colour == "black" else -1

        self.state = {
            "black": [[1, 0, 7], [1, 1, 7], [1, 3, 7], [1, 4, 7], [1, 6, 7], [1, 7, 7], [1, 0, 6], [1, 1, 6], [1, 3, 6],
                      [1, 4, 6], [1, 6, 6], [1, 7, 6]],
            "white": [[1, 0, 1], [1, 1, 1], [1, 3, 1], [1, 4, 1], [1, 6, 1], [1, 7, 1], [1, 0, 0], [1, 1, 0], [1, 3, 0],
                      [1, 4, 0], [1, 6, 0], [1, 7, 0]]
        }


    def action(self):

        ## key used for importing/exporting from/to json
        format_list = []
        format_list.append(sorted(self.state["black"]))
        format_list.append(sorted(self.state["white"]))
        format_list.append(self.currentPlayer)

        format_key = str(format_list)

        '''
        ### Search action from model

        import json

        with open('MCTS/model.txt') as json_file:
            if json_file:
                model = json.load(json_file)
                if format_key in model:
                    # print("found this move in the model!!")
                    action = model[format_key]
                    if action[0] == "BOOM":
                        return ("BOOM", tuple(action[1]))
                    else:
                        return ("MOVE", action[1], tuple(action[2]), tuple(action[3]))
        '''


        currentState = MCTS(self.state, self.currentPlayer)

        agent = mcts(timeLimit=1000)
        action = agent.search(initialState=currentState)


        '''
        ### Export result

        import json

        with open('MCTS/model.txt') as json_file:
            if json_file:
                json_decoded = json.load(json_file)

        json_decoded[format_key] = action

        with open('MCTS/model.txt', 'w') as json_file:
            json.dump(json_decoded, json_file)
        '''


        return action


    def update(self, colour, action):
        if action[0] == 'BOOM':
            boom(self.state, action[1])
        elif action[0] == 'MOVE':
            move(self.state, action[1], action[2], action[3], colour)
