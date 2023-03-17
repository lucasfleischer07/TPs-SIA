import arcade
import random

ROWS = 10
COLS = 10
CELL_SIZE = 50
MARGIN = 25
GENERAL_OUTLINE = 4
SQUARE_OUTLINE = 1.5
COLORS=[arcade.color.PINK, arcade.color.BLUE, arcade.color.RED, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.WHITE]
def create_grid():
    grid = []
    for row in range(ROWS):
        grid.append([])
        for column in range(COLS):
            grid[row].append(random.randint(0,5))
        global selected_color
        selected_color=grid[0][0]
    return grid
       

def setup():
    arcade.open_window((COLS * CELL_SIZE) + (MARGIN * 2), (ROWS * CELL_SIZE) + (MARGIN * 2), "Fill Zone")
    arcade.set_background_color(arcade.color.GRAY)
    arcade.schedule(update, 1/60)
    global grid
    grid = create_grid()
    global selected_color
    selected_color = grid[0][0]

def draw_grid():
    for row in range(ROWS):
        for column in range(COLS):
            color=COLORS[grid[row][column]]
            arcade.draw_rectangle_filled(
                column * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                row * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                CELL_SIZE, CELL_SIZE, color)
            arcade.draw_rectangle_outline(
                column * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                row * CELL_SIZE + MARGIN + CELL_SIZE / 2,
                CELL_SIZE, CELL_SIZE, arcade.color.BLACK, SQUARE_OUTLINE)
    arcade.draw_rectangle_outline(
        (COLS * CELL_SIZE + MARGIN*2) / 2,
        (ROWS * CELL_SIZE + MARGIN*2) / 2,
        COLS * CELL_SIZE, ROWS * CELL_SIZE,
        arcade.color.BLACK, GENERAL_OUTLINE)
            
def on_mouse_press(x, y, button, modifiers):
    print("Mouse clicked at ({}, {})".format(x, y))
    if(x>MARGIN and y>MARGIN and x< ROWS*CELL_SIZE+MARGIN and y<COLS*CELL_SIZE+MARGIN):
        if(button == arcade.MOUSE_BUTTON_LEFT):
            column = (x-MARGIN) // CELL_SIZE
            row = (y-MARGIN) // CELL_SIZE
            if(grid[row][column] != selected_color):
                fill_connected_cells(grid[row][column])
                selected_color = grid[0][0]

def fill_connected_cells(new_color):
    print("fill conected cells")
    # Get the color of the upper left cell
    old_color = grid[0][0]

    # Create a queue to keep track of cells to be filled
    queue = [(0, 0)]

    # Fill the upper left cell with the new color
    grid[0][0] = new_color

    # Continue filling cells until the queue is empty
    while queue:
        # Get the next cell to be filled from the queue
        row, column = queue.pop(0)

        # Check the neighboring cells for the same color as the upper left cell
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Calculate the coordinates of the neighboring cell
            neighbor_row, neighbor_column = row + i, column + j

            # Check if the neighboring cell is within the bounds of the grid
            if (0 <= neighbor_row < len(grid)) and (0 <= neighbor_column < len(grid[0])):
                # Check if the neighboring cell has the same color as the upper left cell
                if grid[neighbor_row][neighbor_column] == old_color:
                    # Fill the neighboring cell with the new color
                    grid[neighbor_row][neighbor_column] = new_color

                    # Add the neighboring cell to the queue to be filled
                    queue.append((neighbor_row, neighbor_column))
    
def update(delta_time):
    if check_game_over():
        arcade.close_window()
    arcade.start_render()
    draw_grid()
    arcade.finish_render()

def check_game_over():
    for row in range(ROWS):
        for column in range(COLS):
            if grid[row][column] != grid[0][0]:
                return False
    return True

def fillZone():
    setup()
    arcade.run()