# recordatorio: el algoritmo DFS encuentra todos los nodos en una estructura de grafo o árbol, explorando uno de los caminos más profundos antes de retroceder. 

import copy
import time


class Node:
    
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.grid == other.grid

    def __hash__(self):
        return hash(self.grid)

    def getParent(self):
        return self.parent


#   Funcion recursiva para ir probando todos los caminos en forma dfs, para poder hacer 
#   backtracking voy a tener que pasar copys 
#   Una vez se llega a un resultado, se devuelve:
#    [True, Lista de pasos invertida, cantidad de nodos evaluados en total, cantidad de nodos frontera en total]
def fill_zone_recursive(grid,colorAmount):
    
    nodes_eval = 0
    for color in range(colorAmount):
        if grid[0][0] != color: 
            nodes_eval += 1
            grid_copy = copy.deepcopy(grid)
            fill_connected_cells(grid,color)
            if check_game_over(grid) == False:
                result = fill_zone_recursive(grid_copy,colorAmount)
                if result == False: 
                    continue
                if result[1] == True:
                    return True, result[1].append(color), result[2] + nodes_eval, result[3] + colorAmount - 1
            else:
                return True,[color],nodes_eval,colorAmount - 1
    return False


def fill_zone_dfs(grid,colorAmount): #inicializo la grilla     
    start_time = time.time()
    total_time = 0
    result = fill_zone_recursive(grid,colorAmount)
    end_time = time.time()
    total_time = end_time - start_time
    if result == False:
        return False
    return result[1],total_time,result[2],result[3],result[0]


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

"""
def fill_zone_dfs(grid, x, y, target_color, fill_color, visited): #inicializo la grilla 
    
    
    
    
    
    
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])): #chequeos en grilla q este todo ok
        return
    
    if (x, y) in visited: # se fija q no haya sido visitada previamente
        return
    
    if grid[x][y] != target_color: # se fija si el color de la posicion en la que estoy es igual al color inicial
        return
    
    visited.add((x, y))
    grid[x][y] = fill_color #cambia al color que quiero
    
    fill_zone_dfs(grid, x-1, y, target_color, fill_color, visited) # up
    fill_zone_dfs(grid, x+1, y, target_color, fill_color, visited) # down
    fill_zone_dfs(grid, x, y-1, target_color, fill_color, visited) # left
    fill_zone_dfs(grid, x, y+1, target_color, fill_color, visited) # right

    # de esta manera va a explorar los caminos mas profundos
"""

