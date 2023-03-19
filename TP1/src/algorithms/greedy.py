# The Greedy algorithm works by evaluating all the possible choices available at each step and selects the one that appears to be the best based on the current information available.
# no asegura una solucion optima


#para este algoritmo vamos a necesitar una heuristica que nos diga cual es la mejor opcion para elegir el color, y se va a basar en lo mas
#simple: cual es el color mas recurrente al rededor de la celda inicial.

#      y
#   |       |(0,1)  |
#   -----------------------
#   |(-1,0) |  fija |(1,0)|
# x -----------------------  
#   |       |(0,-1) | |

import time

from src.utils.colorFile import COLORS
from src.heuristics.heuristic1 import heuristic_1
from src.heuristics.heuristic2 import heuristic_2

# Inicializo la grilla 
def fill_zone_greedy(grid,colorAmount): 
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    
    best_color=0
    best_score=0
    solution=[]

    total_time = 0
    nodes_expanded_amount = 0
    nodes_border_amount = 0

    while(check_game_over(grid)==False):
        nodes_border_amount += (colorAmount - 1)
        best_score = 0          

        for color in range(colorAmount):
            if(color!=grid[0][0]):
                score = heuristic_1(grid[0][0],color,grid)
                if(score>best_score):
                    best_score = score
                    best_color = color        
        grid=fill_connected_cells(grid,best_color)
        solution.append(best_color)
        nodes_expanded_amount += 1
    
    end_time = time.time()
    total_time = end_time - start_time
    return solution, total_time, nodes_expanded_amount, nodes_border_amount , True



def fill_connected_cells(grid, new_color):
    # Get the color of the upper left cell
    old_color = grid[0][0]
    # Create a queue to keep track of cells to be filled
    queue = [(0, 0)]

    # Fill the upper left cell with the new color
    grid[0][0] = new_color

    # Continue filling cells until the queue is empty
    while queue:
        # Get the next cell to be filled from the queue
        row, column = queue.pop(0)

        # Check the neighboring cells for the same color as the upper left cell
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Calculate the coordinates of the neighboring cell
            neighbor_row, neighbor_column = row + i, column + j

            # Check if the neighboring cell is within the bounds of the grid
            if (0 <= neighbor_row < len(grid)) and (0 <= neighbor_column < len(grid[0])):
                # Check if the neighboring cell has the same color as the upper left cell
                if grid[neighbor_row][neighbor_column] == old_color:
                    # Fill the neighboring cell with the new color
                    grid[neighbor_row][neighbor_column] = new_color

                    # Add the neighboring cell to the queue to be filled
                    queue.append((neighbor_row, neighbor_column))
    return grid



def check_game_over(grid):
        for row in range(len(grid)):
            for column in range(len(grid)):
                if grid[row][column] != grid[0][0]:
                    return False
        return True