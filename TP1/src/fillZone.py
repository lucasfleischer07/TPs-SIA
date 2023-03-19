import arcade
import random
import copy

from src.utils.colorFile import COLORS
from src.algorithms.greedy import fill_zone_greedy
from src.algorithms.bfs import fill_zone_bfs
from src.algorithms.dfs import fill_zone_dfs

CELL_SIZE = 50
MARGIN = 25
GENERAL_OUTLINE = 4
SQUARE_OUTLINE = 1.5


def create_grid(num,count_of_colors):
    grid = []
    for row in range(num):
        grid.append([])
        for column in range(num):
            grid[row].append(random.randint(0, count_of_colors-1))
    return grid
       


class FillZone(arcade.Window):
    def __init__(self, num, mode, algorythm, count_of_colors):
        super().__init__(max((num * CELL_SIZE) + (MARGIN * 2),((MARGIN * 2)+count_of_colors*CELL_SIZE)), (num * CELL_SIZE) + (MARGIN * 3)+CELL_SIZE, "Fill Zone")
        arcade.set_background_color(arcade.color.GRAY)
        self.movements = 0
        self.num = num
        self.mode = mode
        self.algorythm = algorythm
        self.count_of_colors = count_of_colors
        self.grid = create_grid(num,count_of_colors)
        self.index = 0
        self.end=0
        gridAux=copy.deepcopy(self.grid)
        if mode == 2:
            # Este es el A*
            # if algorythm == 1:
            #     self.solution = fill_zone_greedy(self.grid)
            # Este es el BFS
            if algorythm == 2:
                results = fill_zone_bfs(gridAux, count_of_colors)
                self.solution = results[0]
                self.total_time = results[1]
                self.nodes_expanded = results[2]
                self.nodes_border = results[3]
            # Este es el DFS
            elif algorythm == 3:
                results = fill_zone_dfs(gridAux, count_of_colors)
                if results == False:
                    self.error = True
                else:
                    self.solution = results[0]
                    self.total_time = results[1]
                    self.nodes_expanded = results[2]
                    self.nodes_border = results[3]
            # Este es el GREEDY
            elif algorythm == 4:
                results = fill_zone_greedy(gridAux, count_of_colors)
                self.solution = results[0]
                self.total_time = results[1]
                self.nodes_expanded = results[2]
                self.nodes_border = results[3]
            
                

    def on_mouse_press(self,x,y,button,modifiers):
        if(self.end == 1):
            self.close()
            return
        
        if(self.mode==1 and x>MARGIN and y>MARGIN+self.num*CELL_SIZE+MARGIN and x< self.count_of_colors*CELL_SIZE+MARGIN and y<MARGIN+self.num*CELL_SIZE+MARGIN+CELL_SIZE):
            if(button == arcade.MOUSE_BUTTON_LEFT):
                column=(x-MARGIN)//CELL_SIZE
                if(column != self.grid[0][0]):
                    self.fill_connected_cells(column)
                    self.movements+=1
                    if(self.check_game_over()):
                        self.close()
        else :
            if(self.mode == 2):
                self.fill_connected_cells(self.solution[self.index])
                self.index+=1
                if(self.index > len(self.solution)-1):
                    self.end = 1
                    print("\n\nEL ALGORITMO TERMINO!!!\n")
                    print("- Resolvio el problema en: " + str(len(self.solution)) + " pasos")
                    print("- El tiempo de procesamiento fue de: {:.8f} segundos".format(self.total_time))
                    print("- La cantidad de nodos expandidos fueron: " + str(self.nodes_expanded))
                    print("- La cantidad de nodos frontera fueron: " + str(self.nodes_border))

                 
                    
    def check_game_over(self):
        for row in range(self.num):
            for column in range(self.num):
                if self.grid[row][column] != self.grid[0][0]:
                    return False
        return True
    


    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_grid()
        
    

    def draw_grid(self):
        for square in range(self.count_of_colors):
            arcade.draw_rectangle_filled(
                square * CELL_SIZE+ MARGIN + CELL_SIZE / 2,
                self.num * CELL_SIZE + MARGIN*2 + CELL_SIZE / 2,
                CELL_SIZE, CELL_SIZE, COLORS[square]
            )
            arcade.draw_rectangle_outline(
                square * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                self.num * CELL_SIZE + MARGIN*2 + CELL_SIZE / 2,
                CELL_SIZE, CELL_SIZE, arcade.color.BLACK, SQUARE_OUTLINE)
        for row in range(self.num):
            for column in range(self.num):
                color=COLORS[self.grid[row][column]]
                arcade.draw_rectangle_filled(
                    column * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                    (self.num-1-row) * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                    CELL_SIZE, CELL_SIZE, color)
                arcade.draw_rectangle_outline(
                    column * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                    (self.num-1-row) * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                    CELL_SIZE, CELL_SIZE, arcade.color.BLACK, SQUARE_OUTLINE)
        arcade.draw_rectangle_outline(
            (self.num * CELL_SIZE + MARGIN*2) / 2,
            (self.num * CELL_SIZE + MARGIN*2) / 2,
            self.num * CELL_SIZE, self.num * CELL_SIZE,
            arcade.color.BLACK, GENERAL_OUTLINE)



    def fill_connected_cells(self,new_color):
            # Get the color of the upper left cell
            old_color = self.grid[0][0]
            # Create a queue to keep track of cells to be filled
            queue = [(0, 0)]

            # Fill the upper left cell with the new color
            self.grid[0][0] = new_color

            # Continue filling cells until the queue is empty
            while queue:
                # Get the next cell to be filled from the queue
                row, column = queue.pop(0)

                # Check the neighboring cells for the same color as the upper left cell
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    # Calculate the coordinates of the neighboring cell
                    neighbor_row, neighbor_column = row + i, column + j

                    # Check if the neighboring cell is within the bounds of the grid
                    if (0 <= neighbor_row < len(self.grid)) and (0 <= neighbor_column < len(self.grid[0])):
                        # Check if the neighboring cell has the same color as the upper left cell
                        if self.grid[neighbor_row][neighbor_column] == old_color:
                            # Fill the neighboring cell with the new color
                            self.grid[neighbor_row][neighbor_column] = new_color

                            # Add the neighboring cell to the queue to be filled
                            queue.append((neighbor_row, neighbor_column))
