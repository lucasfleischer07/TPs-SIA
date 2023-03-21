# recordatorio: el algoritmo DFS encuentra todos los nodos en una estructura de grafo o árbol, explorando uno de los caminos más profundos antes de retroceder. 

import copy
import time

from src.algorithms.utils.Node import Node
from src.algorithms.utils.fillFunctions import fill_connected_cells
from src.algorithms.utils.fillFunctions import check_game_over




#   Funcion que utiliza un tipo de dato Nodo, con registro de su padre y algunas cuestiones mas
#   permite una vez se haya la solucion, podes hacer backtracking hasta el primer nodo
#   Una vez se llega a un resultado, se devuelve:
#    [True, Lista de pasos invertida, cantidad de nodos evaluados en total, cantidad de nodos frontera en total]

def fill_zone_dfs(grid, colorAmount):
    # Inicio el tiempo para ver cuanto tarde en procesarlo y hacerlo
    start_time = time.time()
    total_time = 0
    visited = set()
    pending_nodes = [ Node(grid, grid[0][0],None)]
    done = False
    nodes_expanded_amount = 0
    nodes_border_amount = 0
    solution = []
    while not done:
        current_node = pending_nodes.pop()
        nodes_expanded_amount += 1
        visited.add(current_node)
        if check_game_over(current_node.getGrid()):
            rebuildSolution(current_node,solution)
            done = True
        else:
            nodes_border_amount += colorAmount -1
            get_node_succesors(current_node,current_node.getColor(),colorAmount,visited,pending_nodes)
    
    end_time = time.time()
    total_time = end_time - start_time

    return solution, total_time, nodes_expanded_amount, nodes_border_amount , True




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


