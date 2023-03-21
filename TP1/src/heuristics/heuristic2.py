"""
Idea para la heuristica 2
------
Debe ser admisible ---> h(n) <= costo a la solucion para todo n
la idea para la segunda heuristica es mas simplemente, se calculan cuantos colores restantes quedan en el nodo 
y se devuelve ese numero, que si o si es menor o igual a la cantidad de pasos que hay que hacer hasta finalizar
el juego
"""
from src.algorithms.utils.fillFunctions import fill_connected_cells

def get_user_positions(user_owner_positions,color,grid):
    pending_nodes = [(0,0)]
    while pending_nodes:
        current = pending_nodes.pop()
        current_x, current_y = current
        user_owner_positions.add((current_x,current_y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[x][y] == color and ((x,y) not in pending_nodes) and tuple([x,y]) not in user_owner_positions ): # Ver que este en grilla
                pending_nodes.append((x, y))


# TODO: ESTO NO ANDA TODAVIA
def heuristic_2(node_new_color, grid, colorAmount):
    user_owner_positions = set()
    
    get_user_positions(user_owner_positions, node_new_color, grid)
    colorsFound = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) not in user_owner_positions:
                if len(colorsFound) == colorAmount:
                    break
                if grid[i][j] not in colorsFound:
                    colorsFound.append(grid[i][j])
                 
        if len(colorsFound) == colorAmount:
            break
    print(str(colorsFound))
    return len(colorsFound)