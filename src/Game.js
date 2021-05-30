import { INVALID_MOVE } from "boardgame.io/core";
import { TurnOrder } from "boardgame.io/core";

const init_state = [
  1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0,
  -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, 0, -1, -1,
];

export const Expendibots = {
  setup: () => ({ cells: init_state }),

  turn: {
    moveLimit: 1,
    order: TurnOrder.CUSTOM(["1", "-1"]),
  },

  moves: {
    clickCell: (G, ctx, id) => {
      console.log(ctx, id);
      G.cells[id] = ctx.currentPlayer;
    },
  },
};
