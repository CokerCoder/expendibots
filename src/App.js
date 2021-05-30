import { Client } from "boardgame.io/react";
import { Expendibots } from "./Game";
import ExpendibotsBoard from "./Board";

const App = Client({ game: Expendibots, board: ExpendibotsBoard, debug: true });

export default App;
