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
import copy



from src.utils.colorFile import COLORS
from src.heuristics.heuristic1 import heuristic_1
from src.heuristics.heuristic2 import heuristic_2
from src.heuristics.heurisitic3 import heuristic_3
from src.algorithms.utils.fillFunctions import fill_connected_cells
from src.algorithms.utils.fillFunctions import check_game_over
from src.algorithms.utils.Node import Node

# Inicializo la grilla 
def fill_zone_greedy(grid,colorAmount): 
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    used_nodes= set()
    best_color=0
    best_score=0
    solution=[]
    MAX_SCORE = len(grid)*len(grid)
    total_time = 0
    nodes_expanded_amount = 0
    nodes_border_amount = 0
    state = Node(grid,grid[0][0],None)
    while(check_game_over(state.getGrid())==False):
        nodes_border_amount += (colorAmount - 1)
        best_score = MAX_SCORE        
        used_nodes.add(state)
        for color in range(colorAmount):
            if(color!=state.getColor()):
                
                auxState = state.getSon(color) 
                #score = heuristic_1(color,auxState.getGrid(),colorAmount)
                score = heuristic_2(color,auxState.getGrid(),colorAmount)
                #score = heuristic_3(color,auxState.getGrid(),colorAmount)
                if score<=best_score and auxState not in used_nodes:
                    best_score = score
                    best_color = color        
        state = state.getSon(best_color) 
        solution.append(best_color)
        nodes_expanded_amount += 1
    
    end_time = time.time()
    total_time = end_time - start_time
    return solution, total_time, nodes_expanded_amount, nodes_border_amount , True



