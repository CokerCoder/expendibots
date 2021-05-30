from Human.helper import *


class ExamplePlayer:

    def __init__(self, colour):

        self.colour = colour
        self.state = {
            "black": [[1, 0, 7], [1, 1, 7], [1, 3, 7], [1, 4, 7], [1, 6, 7], [1, 7, 7], [1, 0, 6], [1, 1, 6], [1, 3, 6],
                      [1, 4, 6], [1, 6, 6], [1, 7, 6]],
            "white": [[1, 0, 1], [1, 1, 1], [1, 3, 1], [1, 4, 1], [1, 6, 1], [1, 7, 1], [1, 0, 0], [1, 1, 0], [1, 3, 0],
                      [1, 4, 0], [1, 6, 0], [1, 7, 0]]
        }

    def action(self):

        all_possible_actions = available_actions(self.state, self.colour)
        print("You can take one of the following actions:")
        for i in range(1, len(all_possible_actions) + 1):
            print("{}: {}".format(i, all_possible_actions[i - 1]))
        index = int(input("Please choose an action (type in the index): "))

        return all_possible_actions[index - 1]

    def update(self, colour, action):
        if action[0] == 'BOOM':
            boom(self.state, action[1])
        elif action[0] == 'MOVE':
            move(self.state, action[1], action[2], action[3], colour)
