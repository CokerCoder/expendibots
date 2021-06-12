import React from "react";
import Button from "@material-ui/core/Button";

export default function ExpendibotsBoard(props) {
  function onClick(id) {
    console.log(id);
    console.log(props);

    if (props.G.selected == null) {
      props.moves.selectToken(id);
    } else if (props.G.action == null) {
      // props.chooseAction
    } else {
      props.moves.moveTo(id);
    }

    // props.moves.clickCell(id);
  }

  const cellStyle = {
    border: "1px solid",
    width: "50px",
    height: "50px",
    textAlign: "center",
    cursor: "pointer",
  };

  const boardStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  };

  // initialize board
  let tbody = [];
  for (let i = 0; i < 8; i++) {
    let cells = [];
    for (let j = 0; j < 8; j++) {
      const id = 8 * i + j;
      cells.push(
        <td style={cellStyle} key={id} onClick={() => onClick(id)}>
          {props.G.cells[8 * i + j] === 0 ? null : props.G.cells[8 * i + j]}
        </td>
      );
    }
    tbody.push(<tr key={i}>{cells}</tr>);
  }

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Expendibots</h1>
      <div style={boardStyle}>
        <table id="board">
          <tbody>{tbody}</tbody>
        </table>
      </div>
      <div>
        <Button
          variant="contained"
          color="primary"
          disabled={props.G.selected == null}
        >
          Move
        </Button>
        <Button
          variant="contained"
          color="secondary"
          disabled={props.G.selected == null}
        >
          Explode
        </Button>
      </div>
    </div>
  );
}
