from NeCho.helper import *


class MinimaxAgent:

    def __init__(self, max_depth, colour):

        self.max_depth = max_depth
        self.colour = colour

    def choose_action(self, state):

        eval_score, selected_action = self._minimax(0, state, self.colour)

        return selected_action

    def _minimax(self, current_depth, state, colour):

        if current_depth == self.max_depth or is_over(state):
            return evaluate(state, self.colour), ""

        possible_actions = available_actions(state, colour)

        best_value = float('-inf') if colour == self.colour else float('inf')
        action = ""

        for possible_action in possible_actions:

            candidate_state = new_state(state, colour, possible_action)

            eval_child, action_child = self._minimax(current_depth + 1, candidate_state,
                                                     "white" if colour == "black" else "black")

            if colour == self.colour and best_value < eval_child:
                best_value = eval_child
                action = possible_action

            elif (colour != self.colour) and best_value > eval_child:
                best_value = eval_child
                action = possible_action

        return best_value, action
