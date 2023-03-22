"""
Idea para la heuristica 3
------
Debe ser admisible ---> h(n) <= costo a la solucion para todo n
Desde el color actual, cuantas posiciones van a cambiar con el cambio de color
Ejemplo:

   Dada la siguiente grilla, si se quiere calcular la herustica de un nuevo color verde, en este caso el valor devuelto
   Sera 2, ya que el verde se expandira por el rojo y tomara la celda (0,1) y la celda (2,0)
   El valor devuelto son las ubicaciones restantes
        y
   x  |  rojo | verde     | rojo   |
      |  rojo |  rojo     | azul   |  
      | verde | amarillo  | blanco |
"""
# Primero lo que quiero obtener son todas las celdas vecinas a la zona tomada
# Para esto vamos a ir buscando como se expande la zona tomada y agregando a 
# un contador la cantidad de vecino q sumariamos a la zona nueva


def heuristic_3(node_new_color, grid, colorAmoun):
    visited_coords = set()            # Conjunto de posiciones visitadas
    current_coord = [0, 0]            # Coordenada inicial como lista en lugar de tupla
    waiting_list = [(0, 0)]           # Lista de espera, del current color que faltan por analizar
    extention_counter = 0             # Contador de extensiones
    current_color = grid[0][0]
    total_covered_spaces = 0
    # Búsqueda en anchura
    while non_visited_zone(current_coord, current_color, grid, visited_coords, waiting_list):
        total_covered_spaces += 1
        current_x, current_y = current_coord
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid)  and ((x,y) not in visited_coords) and (grid[x][y] != current_color)): # Ver que este en grilla
                visited_coords.add((x,y))
                if (grid[x][y] == node_new_color):
                    extention_counter += 1
    total_covered_spaces += extention_counter
    return (len(grid) * len(grid[0])) - total_covered_spaces



def non_visited_zone(current_coord, current_color, grid, visited, waiting_list):
    if len(waiting_list) == 0:
        return False
    
    current_coord[:] = waiting_list.pop()   # Modificar los valores de current_coord usando la notación [:]
    visited.add(tuple(current_coord))      # Convertir la lista de coordenadas en una tupla antes de agregarla a visited
    current_x, current_y = current_coord
    
    # Agregar a la lista de espera todas las posiciones adyacentes que tengan el mismo color que la posición actual
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[x][y] == current_color and ((x,y) not in waiting_list) and tuple([x,y]) not in visited ): # Ver que este en grilla
                waiting_list.append((x, y))

    return True