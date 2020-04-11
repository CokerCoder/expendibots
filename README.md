# Expendibots

## Data Structure

We brake the program down into the following Python Classes for a better maintenance  

Similar structure written in Java can be found here: <https://www.geeksforgeeks.org/design-a-chess-game/>

- ### Board

  To represent a game board by initializing a **2D-array of Spots** and may have methods relating to the state of the board

- ### Spot

  To represent a cell in the board, can either have 0 or more white/black tokens, and may record the number of that token on this cell

- ### Token

  To represent a token and its position, may have methods relating to stack operations

- ### Move

  To represent a token movement, including any relevant moving methods 

- ### Boom

  To represent a token explosion, including any relevant exploding methods

- ### Player

  Main class will be called during the game, keep asking the actions and then updates the board state



