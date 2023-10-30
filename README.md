# game_of_life
Coding Exercise - Game Of Life

****************************************************************
Coding Exercise - Game Of Life.
Rules:
Given a 200*200 square cells, each cell is in one of two possible states, alive or dead, or "populated" or
"unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or
diagonally adjacent. At each step in time, the following transitions occur:
Any live cell with fewer than two live neighbours dies in the next generation as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies in the next generation, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell in the next generation, as if by reproduction.
*****************************************************************

Instructions for running the program:

Required Softwares :

    Python 3

Installation and Getting Started Steps for running the programme

    Check out the source from git hub
    Run the following command "python game_of_life.py

Input

The programme shall prompt to enter the co-ordinates of the game(Game Of Life) in the format [[1,1]]

Output

The prgramme shall print the next 100 possible states of the game and exit.

Note: The debug level is set to ERROR, set to DEBUG in the code to display the messages while debugging.

Explanation of Code

There are three main functons
create_initial_state : This function helps to create the initial state of game matrix and sets the cells alive/dead based on the user input provided

calculate_alive_count : Given a cell and the matrix, the function calculates the number of cells that are alive based on the game conditions. This happens by taking in to account all the cells surrounding the given cell(diagnoally, vertically and horizontally)

game_of_life : This is the main method that loops through the state count and each time prints the next possible state.

Known things - There needs to be further testing associated with the programme and unit test cases to be written to help cover the edge case scenarios.
    Further the user input also needs to be validated to check for correctness.
