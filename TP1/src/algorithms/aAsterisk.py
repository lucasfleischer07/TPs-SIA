# A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final state. 

def fill_zone_Astar(grid, start_x, start_y, target_color):

    # Define the heuristic function as Manhattan distance
    def heuristic(cell):
        #uso heuristica Manhattan, suma ambsoluta de la diferencia de la fila y columna entre ambas celdas
        return abs(cell.x - target_x) + abs(cell.y - target_y) # estima la distancia entre la current cell y mi target cell


    # Define a function to calculate the cost of moving from one cell to another, which depends on the color of the two cells. 
    # For example, the cost could be zero if the two cells have the same color, or one if they have different colors.
    def cost(current, neighbor):
        return 0 if current.color == neighbor.color else 1

   #hasta aca llegue
