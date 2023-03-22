# recordatorio: el algoritmo BFS encuentra el camino más corto desde un nodo raíz a todos los demás nodos en una estructura de grafo o árbol.

import copy
import time
import pdb
from src.algorithms.utils.Node import Node
from src.algorithms.utils.fillFunctions import fill_connected_cells
from src.algorithms.utils.fillFunctions import check_game_over


def fill_zone_bfs(grid,colors): # esta funcion nos genera la grilla inicial, definimos las coordenadas y al color que quiero cambiar.
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    total_time = 0
    visited = set()
    pending_nodes = [ Node(grid, grid[0][0],None)]
    done = False
    nodes_expanded_amount = 0
    nodes_border_amount = 0
    solution = []
    
    while 1:
        while(pending_nodes):
            current_node = pending_nodes.pop()
            nodes_expanded_amount += 1
            visited.add(current_node)
            if check_game_over(current_node.getGrid()):
                rebuildSolution(current_node,solution)
                end_time = time.time()
                total_time = end_time - start_time
                return solution, total_time, nodes_expanded_amount, nodes_border_amount , True
        nodes_border_amount= nodes_expanded_amount*(colors-1)
        get_node_succesors(current_node,current_node.getColor(),colors,visited,pending_nodes)
    
                
def rebuildSolution(final_node,solution):
    current_node = final_node
    while current_node.getParent() != None:
        solution.append(current_node.getColor())
        current_node = current_node.getParent()
    solution.reverse()


def get_node_succesors(parent_node,currentColor,colorAmount,visited,pending_nodes):
    for color in range(colorAmount):
        if color != currentColor:
            gridCopy = copy.deepcopy(parent_node.getGrid())
            newNode = Node(fill_connected_cells(gridCopy,color),color,parent_node)
            if parent_node.getNodeScore() < newNode.getNodeScore() and newNode not in visited:
                pending_nodes.append(newNode)