# recordatorio: el algoritmo BFS encuentra el camino más corto desde un nodo raíz a todos los demás nodos en una estructura de grafo o árbol.

def fill_zone_bfs(grid, x, y, fill_color): # esta funcion nos genera la grilla inicial, definimos las coordenadas y al color que quiero cambiar.
   
    """
    Fill a zone in a 2D grid with a specified color, starting from a given point using BFS algorithm.
    grid: a 2D list representing the grid
    x: x-coordinate of the starting point
    y: y-coordinate of the starting point
    fill_color: the color to fill the zone with
    """

    target_color = grid[x][y] # target color es el color de la primera celda (verde ponele)
    visited = set() # seteamos una lista de celdas visitadas
    queue = [(x, y)]
    while queue: # va a terminar cuando no haya mas celdas q visitar
        x, y = queue.pop(0)
        if (x, y) in visited: # si ya fue visitada la salteo
            continue
        visited.add((x, y))
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): #chequeo que este dentro de la grilla 
            continue
        if grid[x][y] != target_color: # si el color de la celda es distinto a verde (el de la celda inicial) la salteo xq no se puede cambiar al fill color (rojo ponele)
            continue
        grid[x][y] = fill_color # si la celda en la q estoy es del target color (osea verde) la cambio a fill color osea rojo
        queue.append((x+1, y))
        queue.append((x-1, y))
        queue.append((x, y+1))
        queue.append((x, y-1))

        return grid