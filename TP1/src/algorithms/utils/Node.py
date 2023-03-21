import copy
from src.algorithms.utils.fillFunctions import fill_connected_cells


class Node:

    def __init__(self, grid, color, parent,cost=0):
        self.grid = grid
        self.parent = parent
        self.color = color
        self.cost=cost

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.grid == other.grid and self.cost==other.cost

    def __hash__(self):
        if(self.cost==0):
            return hash(str(self.grid))
        return hash(str(self.grid)+str(self.cost))

    def getParent(self):
        return self.parent
    
    def getGrid(self):
        return self.grid
    
    def getColor(self):
        return self.color

    def getCost(self):
        return self.cost
    
    def getNodeScore(self):
        visited = set()
        pending = []
        pending.append((0,0))
        scoreCounter = 0 
        while pending:
            currentCoord = pending.pop()
            scoreCounter +=1
            row,column = currentCoord
            visited.add((row,column))
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_row, neighbor_column = row + i, column + j
                # Check if the neighboring cell is within the bounds of the grid
                if (0 <= neighbor_row < len(self.grid)) and (0 <= neighbor_column < len(self.grid[0]) and self.grid[neighbor_row][neighbor_column] == self.color and (neighbor_row,neighbor_column) not in visited):
                    pending.append((neighbor_row,neighbor_column))
                
        return scoreCounter
    
    def getSon(self,color):
        return Node(fill_connected_cells(copy.deepcopy(self.grid),color),color,self)
    def getSonWithCost(self,color):
        return Node(fill_connected_cells(copy.deepcopy(self.grid),color),color,self)