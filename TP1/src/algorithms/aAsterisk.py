# A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final state. 

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
def fill_zone_aStar(grid,colorAmount): 
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    visited= set()
    best_color=0
    best_score=0
    MAX_SCORE = len(grid)*len(grid)
    total_time = 0
    nodes_expanded_amount = 0
    nodes_border_amount = 0
    state = Node(grid,grid[0][0],None)
    pending_nodes=set()
    heuristic=0
    solution=[]
    while(check_game_over(state.getGrid())==False):
        nodes_border_amount += (colorAmount - 1)
        best_score = MAX_SCORE        
        visited.add(state)
        nodes_expanded_amount += 1
        get_node_succesors(state,state.getColor(),colorAmount,visited,pending_nodes)
        for node in pending_nodes:
            heuristic=heuristic_1(node.getColor(),node.getGrid(),colorAmount)
            if(heuristic+node.getCost() < best_score):
                state=node
                best_score=heuristic+node.getCost()
        pending_nodes.remove(state)
    rebuildSolution(state,solution)
    end_time = time.time()
    total_time = end_time - start_time
    return solution, total_time, nodes_expanded_amount, nodes_border_amount , True

def get_node_succesors(parent_node,currentColor,colorAmount,visited,pending_nodes):
    for color in range(colorAmount):
        if color != currentColor:
            gridCopy = copy.deepcopy(parent_node.getGrid())
            newNode = Node(fill_connected_cells(gridCopy,color),color,parent_node,parent_node.getCost()+1)
            if  newNode not in visited:
                pending_nodes.add(newNode)

def rebuildSolution(final_node,solution):
    current_node = final_node
    while current_node.getParent() != None:
        solution.append(current_node.getColor())
        current_node = current_node.getParent()
    solution.reverse()
    print(solution)