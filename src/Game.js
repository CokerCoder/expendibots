import { INVALID_MOVE } from "boardgame.io/core";
import { TurnOrder } from "boardgame.io/core";

// use a single array to store current state
// negative for player 0 and positive for player 1
const init_state = [
  -1, -1, 0, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,
];

export const Expendibots = {
  setup: () => ({
    cells: init_state,
    selected: null,
    action: null,
  }),

  turn: {
    // a move consists of selecting the token and move the token
    moveLimit: 2,
    order: TurnOrder.CUSTOM(["1", "-1"]),
  },

  moves: {
    selectToken: (G, ctx, id) => {
      if (G.cells[id] * ctx.currentPlayer <= 0) {
        return INVALID_MOVE;
      } else {
        G.selected = id;
      }
      console.log(G.selected);
    },
    chooseAction: (G, ctx, action) => {
      if (action === "move") {
        G.action = "move";
      } else {
        G.action = "explode";
      }
    },
    moveAmount: (G, ctx, id) => {},
    moveTo: (G, ctx, id) => {
      G.cells[id] = G.cells[G.selected];
      G.cells[G.selected] = 0;
      G.selected = null;
    },
  },
};
