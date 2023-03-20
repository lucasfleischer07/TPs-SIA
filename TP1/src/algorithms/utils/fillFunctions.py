def fill_connected_cells(grid, new_color):
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
    return grid


def check_game_over(grid):
        for row in range(len(grid)):
            for column in range(len(grid)):
                if grid[row][column] != grid[0][0]:
                    return False
        return True