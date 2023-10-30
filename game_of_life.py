import ast
import logging, sys

#Logging level set to ERROR, set to DEBUG for debugging, eventually we need to write to a file
logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

def game_of_life():
    rows, cols = (10, 10)
    next_state_matrix = [[0]*cols for _ in range(rows)]
    number_of_states = 50
    next_state_list = []
    state_counter = 0

    print("Please enter the coordinates of live cells for Game of Life ex: [[1, 1],[1, 2]]")
    user_input = input() 
    #TODO: To validate the user input and check if it has got only coordinates in the given format
    lists=ast.literal_eval(user_input)
    #iterate over the next number of states and check the game of life conditions and print next state
    while state_counter < number_of_states:
        gol_matrix = [[0]*cols for _ in range(rows)]
    
        create_initial_state(gol_matrix, lists)
        logging.debug("%s",gol_matrix)
        next_state_list = []
        

        for i in range(rows):
            for j in range(cols):
                alive_count = calculate_alive_count(rows, cols, gol_matrix, i, j)
                #Determine the adjacent cells for each cell and check make them alive or dead based on the conditions
                if alive_count < 2:
                        next_state_matrix[i][j]= 0
                elif alive_count == 2 or alive_count == 3:
                        next_state_matrix[i][j]= 1
                elif alive_count > 3:
                        next_state_matrix[i][j]= 0
                #logging.debug(alive_count,"count of alive cells")
                #logging.debug(i,j,"current cell")
                
        logging.debug("The next state of the matrix %s",next_state_matrix)
    
        state_counter = state_counter+1
        for i in range(rows):
            for j in range(cols):
                if next_state_matrix[i][j] == 1:
                    next_state_list.append([i,j])

        print(next_state_list)            
        #Assign the next state to the current list to help process the future states
        lists = next_state_list


#parse the live cells from user and map to the game matrix by setting the cell value to 1(0 for dead cell)
def create_initial_state(arr, lists):
    for i in lists:
        x,y = 0,0
        for j in i:
            if x == 0:
                x = j
            else:
                y = j
        arr[x][y] = 1

#Given a game matrix and the coordinate(cell) pair determine if the cell should be alive or dead by returing alive count
def calculate_alive_count(rows, cols, arr, i, j):
    adj = []

    alive_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, rows)  
            rangeY = range(0, cols)  
            (newX, newY) = (i+dx, j+dy)  
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
                alive_count = alive_count + arr[newX][newY]
    if(i,j) in adj:
        adj.remove((i,j))
    logging.debug("The adjoining vertices for the given co-ordinates %s,%s is %s",i,j,adj)    
    return alive_count


#start the game
game_of_life()