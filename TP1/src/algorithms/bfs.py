# recordatorio: el algoritmo BFS encuentra el camino más corto desde un nodo raíz a todos los demás nodos en una estructura de grafo o árbol.

import copy
import time
import pdb
from src.algorithms.utils.fillFunctions import fill_connected_cells
from src.algorithms.utils.fillFunctions import check_game_over

def fill_zone_bfs(grid,colors): # esta funcion nos genera la grilla inicial, definimos las coordenadas y al color que quiero cambiar.
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    
    solutions = [[]]
    solutionsAux = []
    gridAux = []
    nodes_expanded_amount = 0
    nodes_border_amount = 0
    
    pdb.set_trace()
    print(grid)
    
    while(1):
        solutionAux=[]
        for color in range(colors):
            for solution in solutions:
                if(len(solution)==0 or solution[len(solution)-1] != color):
                    solutionAux.append(solution+[color])
                    nodes_border_amount += 1
        print(solutionAux)
        solutions = copy.deepcopy(solutionAux)
        print(solutions)
        for solution in solutions:
            gridAux = copy.deepcopy(grid)
            nodes_expanded_amount+=1
            for color in solution:
                if color!=gridAux[0][0]:
                    gridAux = fill_connected_cells(gridAux,color)
            if(check_game_over(gridAux)):
                end_time = time.time()
                total_time = end_time - start_time
                return solution, total_time, nodes_expanded_amount, nodes_border_amount
                

    
    #target_color = grid[x][y] # target color es el color de la primera celda (verde ponele)
    #visited = set() # seteamos una lista de celdas visitadas
    #queue = [(x, y)]
    #while queue: # va a terminar cuando no haya mas celdas q visitar
    #    x, y = queue.pop(0)
    #    if (x, y) in visited: # si ya fue visitada la salteo
    #        continue
    #    visited.add((x, y))
    #    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): #chequeo que este dentro de la grilla 
    #        continue
    #    if grid[x][y] != target_color: # si el color de la celda es distinto a verde (el de la celda inicial) la salteo xq no se puede cambiar al fill color (rojo ponele)
    #        continue
    #    grid[x][y] = fill_color # si la celda en la q estoy es del target color (osea verde) la cambio a fill color osea rojo
    #    queue.append((x+1, y))
    #    queue.append((x-1, y))
    #    queue.append((x, y+1))
    #    queue.append((x, y-1))

    #    return grid


