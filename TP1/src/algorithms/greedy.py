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


def fill_zone_greedy(x, y, fill_color, grid): #inicializo la grilla 

    target_color = grid[x][y] 
    not_visited = [(x, y)]
    visited = set()


    while not_visited:
        current_x, current_y = not_visited.pop()

        if (current_x, current_y) in visited: #si fue visitada la salteo
            continue

        visited.add((current_x, current_y))

        # seleciona el color que mas celdas tengan al rededor de la celda inicial
        color_counts = {}
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] != fill_color): #ver que este en grilla
                color_counts[grid[y][x]] = color_counts.get(grid[y][x], 0) + 1

        # selecciona el color que mas aparece
        best_color = target_color
        for color in color_counts:
            if color_counts[color] > color_counts[best_color]:
                best_color = color

        # Update el juego y lo rellena con el best color
        grid[current_y][current_x] = fill_color

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_x + dx, current_y + dy
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == best_color:
                not_visited.append((x, y))
