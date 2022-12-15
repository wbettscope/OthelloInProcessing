# Othello in Processing
Will Betts Cope CMSCH107A Final Project. Fully functional Othello game complete with a GUI, basic computer opponent, and World Othello Federation rules (https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english).

## Installation
1. Follow the download and installation instructions for Procesing version 3.5.4 and its Python language mode (https://www.geeksforgeeks.org/how-to-set-up-python-mode-for-processing/)
2. Download all code files from this repository and place them in the same folder

## Usage
1. Open file 'OthelloInProcessing.pyde' in Processing
 - This file connects to 'A_Piece.py,' 'B_Square.py,' 'C_Board.py,' 'D_Othello.py,' and 'E_CPU.py' via imports
2. Press 'Run'

## Interface
1. To play a move, click within the desired square
 - A piece will only be played if the desired move is legal (squares with transparent gray pieces denote legal moves)
 - The color of the piece to be played next is indicated by the color of the transparent piece following the mouse
2. If no moves are legal, click on the "No Moves" circle in the top left corner (or anywhere else on the screen)
3. By default, the program will play against the user, playing the white pieces - Press any valid key to toggle this feature
 - On the program's turn, the red highlighted square numbers display the location of the program's intended move (to be played by the user)
 - If the program has no legal moves, it will highlight the coordinates (1,1), prompting the user to click on the "No Moves" square
4. When the game ends, the winner and score are displayed as "[Winner] Wins! [Winner's score] : [Loser's score]"

## Unit Testing
- Usual cases and major extremes tested visually
