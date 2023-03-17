# recordatorio: el algoritmo DFS encuentra todos los nodos en una estructura de grafo o árbol, explorando uno de los caminos más profundos antes de retroceder. 


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


