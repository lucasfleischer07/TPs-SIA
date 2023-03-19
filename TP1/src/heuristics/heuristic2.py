"""
Idea para la heuristica 2
------
Debe ser admisible ---> h(n) <= costo a la solucion para todo n
la idea para la segunda heuristica es mas simple, menos compleja pero mas rapida de calcular.
La idea es la siguiente, basicamente calculo cuantos espacios del color que estoy evaluando hay (sin tener en
cuenta el caso de querer pasar al color en el que ya estaba previamente ) y devuelvo ese puntaje
Por lo tanto el que menos colores restantes tenga sera el elegido
Ejemplo:

   Dada la siguiente grilla, si se quiere calcular la herustica de un nuevo color verde, en este caso el valor 
   Devuelto sera 3, ya que hay 3 celdas verdes sin tomar
        y
   x  |  rojo | verde     | rojo   |
      |  azul |  rojo     | verde   |  
      | verde | amarillo  | blanco |
"""


# TODO: ESTO NO ANDA TODAVIA
def heuristic_2(current_color, node_new_color, grid):
    extention_counter = 0  # Contador de extensiones
    
    # Itero sobre los todo el grid buscando las ubicaciones
    if (current_color == node_new_color):
        return 0
    
    for row in range(len(grid[1])):
        for column in range(len(grid[1])): 
            if grid[row][column] == node_new_color:
                extention_counter += 1
    
    if (extention_counter == 0):
        return 0
    else:
        return extention_counter