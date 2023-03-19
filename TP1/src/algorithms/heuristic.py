"""
Idea para la heuristica 1
------
Debe ser admisible ---> h(n) <= costo a la solucion para todo n
Desde el color actual, cuantas posiciones van a cambiar con el cambio de color
Ejeplo:

   Dada la siguiente grilla, si se quiere calcular la herustica de un nuevo color verde, en este caso el valor devuelto
   Sera 2, ya que el verde se expandira por el rojo y tomara la celda (0,1) y la celda (2,0)
      y
   |  rojo | verde  | rojo   |
   --------------------------|
   |  rojo |  rojo  | azul   |
 x --------------------------|  
   | verde |amarillo| blanco |
"""
#Primero lo que quiero obtener son todas las celdas vecinas a la zona tomada
#Para esto vamos a ir buscando como se expande la zona tomada y agregando a 
#un contador la cantidad de vecino q sumariamos a la zona nueva

def heuristic_1(current_color, node_new_color, grid):
    visited_coords = set()      # Conjunto de posiciones visitadas
    current_coord = (0,0)       # Coordenada inicial
    waiting_list = []           # Lista de espera
    waiting_list.append((0,0))  # Se agrega la coordenada inicial a la lista de espera
    extention_counter = 0       # Contador de extensiones

    # Búsqueda en anchura
    while non_visited_zone(current_coord, current_color, grid, visited_coords, waiting_list):
        current_x, current_y = current_coord
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid)  and (grid[y][x] not in visited_coords) and (grid[y][x] != current_color)): # Ver que este en grilla
                visited_coords.add((x,y))
                if (grid[y][x] == node_new_color):
                    extention_counter += 1

    return extention_counter



def non_visited_zone(current_coord, current_color, grid, visited, waiting_list):
    if waiting_list.len() == 0:
        return False
    
    current_coord = waiting_list.pop()  # Sacar la siguiente posición de la lista de espera
    visited.add(current_coord)          # Agregar la posición a las posiciones visitadas
    current_x, current_y = current_coord
    
    # Agregar a la lista de espera todas las posiciones adyacentes que tengan el mismo color que la posición actual
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == current_color and (grid[y][x] not in waiting_list) and (grid[y][x] not in visited) ): # Ver que este en grilla
                waiting_list.add(x, y)

    return True