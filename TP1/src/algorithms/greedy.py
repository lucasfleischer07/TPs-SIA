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


from fillZone import COLORS
from heuristic import heuristic_1



def fill_zone_greedy(grid): #inicializo la grilla 
    target_color = grid[0][0] 
    not_visited = [(0, 0)]
    visited = set()
    best_color=COLORS[0]
    best_score=0
    solution=[]


    # while not_visited:
    #     current_x, current_y = not_visited.pop()

    #     if (current_x, current_y) in visited: #si fue visitada la salteo
    #         continue

    #     visited.add((current_x, current_y))

    #     # seleciona el color que mas celdas tengan al rededor de la celda inicial
    #     color_counts = {}
    #     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #arriba, derecha, abajo, izquierda
    #         x, y = current_x + dx, current_y + dy
    #         if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] != fill_color): #ver que este en grilla
    #             color_counts[grid[y][x]] = color_counts.get(grid[y][x], 0) + 1

    #     # selecciona el color que mas aparece
    #     best_color = target_color
    #     for color in color_counts:
    #         if color_counts[color] > color_counts[best_color]:
    #             best_color = color

    #     # Update el juego y lo rellena con el best color
    #     grid[current_y][current_x] = fill_color

    #     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #         x, y = current_x + dx, current_y + dy
    #         if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == best_color:
    #             not_visited.append((x, y))
    while(check_game_over(grid)):
        best_score =0          
        for color in COLORS:
            score=heuristic_1(grid[0][0],color,grid)
            if(score>best_score):
                best_score = score
                best_color = color
                
        fill_connected_cells(grid,best_color)
        solution.append(best_color)
    return solution

def fill_connected_cells(grid,new_color):
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

def check_game_over(grid):
        for row in range(len[grid]):
            for column in range(len[grid]):
                if grid[row][column] != grid[0][0]:
                    return False
        return True