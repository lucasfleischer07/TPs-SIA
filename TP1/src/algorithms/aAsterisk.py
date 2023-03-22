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
def fill_zone_aStar(grid, colorAmount, heuristic_type): 
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
    pending_nodes=[]
    pending_nodes.append(state)
    best_heuristic=0
    heuristic=0
    solution=[]

    if(heuristic_type == 1):
        state.setHeuristic(heuristic_1(state.getColor(),state.getGrid(),colorAmount))
    elif(heuristic_type == 2):
        state.setHeuristic(heuristic_2(state.getColor(),state.getGrid(),colorAmount))
    else:
        state.setHeuristic(heuristic_3(state.getColor(),state.getGrid(),colorAmount))



    while(check_game_over(state.getGrid())==False):
        nodes_border_amount += (colorAmount - 1)
        best_score = MAX_SCORE 
        best_heuristic = MAX_SCORE       
        visited.add(state)
        pending_nodes.remove(state)
        nodes_expanded_amount += 1
        get_node_succesors(state, state.getColor(), colorAmount, visited, pending_nodes, heuristic_type)
        for node in pending_nodes:
            heuristic=node.getHeuristic()
            if(heuristic+node.getCost() <= best_score):
                if(heuristic < best_heuristic):
                    state=node
                    best_score=heuristic+node.getCost()
                    best_heuristic=node.getHeuristic()
    rebuildSolution(state,solution)
    end_time = time.time()
    total_time = end_time - start_time
    return solution, total_time, nodes_expanded_amount, nodes_border_amount , True

def get_node_succesors(parent_node, currentColor, colorAmount, visited, pending_nodes, heuristic_type):
    for color in range(colorAmount):
        if color != currentColor:
            gridCopy = copy.deepcopy(parent_node.getGrid())
            newNode = Node(fill_connected_cells(gridCopy,color),color,parent_node,parent_node.getCost()+1)
            if  newNode not in visited:
                if(heuristic_type == 1):
                    newNode.setHeuristic(heuristic_1(newNode.getColor(),newNode.getGrid(),colorAmount))
                elif(heuristic_type == 2):
                    newNode.setHeuristic(heuristic_2(newNode.getColor(),newNode.getGrid(),colorAmount))
                else:
                    newNode.setHeuristic(heuristic_3(newNode.getColor(),newNode.getGrid(),colorAmount))

                pending_nodes.append(newNode)


def rebuildSolution(final_node,solution):
    current_node = final_node
    while current_node.getParent() != None:
        solution.append(current_node.getColor())
        current_node = current_node.getParent()
    solution.reverse()