import arcade
import random

CELL_SIZE = 50
MARGIN = 25
GENERAL_OUTLINE = 4
SQUARE_OUTLINE = 1.5
COLORS=[arcade.color.PINK, arcade.color.BLUE, arcade.color.RED, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.WHITE]


def create_grid(num):
    grid = []
    for row in range(num):
        grid.append([])
        for column in range(num):
            grid[row].append(random.randint(0,5))
    return grid
       

class FillZone(arcade.Window):
    def __init__(self, num, mode, count_of_colors):
        super().__init__(max((num * CELL_SIZE) + (MARGIN * 2),((MARGIN * 2)+len(COLORS)*CELL_SIZE)), (num * CELL_SIZE) + (MARGIN * 3)+CELL_SIZE, "Fill Zone")
        arcade.set_background_color(arcade.color.GRAY)
        self.movements=0
        self.num = num
        self.mode = mode
        self.count_of_colors = count_of_colors
        self.grid = create_grid(num)
        


    def on_mouse_press(self,x,y,button,modifiers):
        if(x>MARGIN and y>MARGIN+self.num*CELL_SIZE+MARGIN and x< len(COLORS)*CELL_SIZE+MARGIN and y<MARGIN+self.num*CELL_SIZE+MARGIN+CELL_SIZE):
            if(button == arcade.MOUSE_BUTTON_LEFT):
                column=(x-MARGIN)//CELL_SIZE
                if(column != self.grid[0][0]):
                    self.fill_connected_cells(column)
                    self.movements+=1
                    if(self.check_game_over()):
                        self.close()
                    
                    
                    
    def check_game_over(self):
        for row in range(self.num):
            for column in range(self.num):
                if self.grid[row][column] != self.grid[0][0]:
                    return False
        return True
    


    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        
    

    def draw_grid(self):
        for square in range(len(COLORS)):
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
