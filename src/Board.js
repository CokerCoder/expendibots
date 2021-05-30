import React from "react";

export default function ExpendibotsBoard(props) {
  function onClick(id) {
    // check cell
    console.log(id);
    console.log(props.ctx);
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
    </div>
  );
}
