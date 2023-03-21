"""
Idea para la heuristica 3
------
Se estima cuantos pasos van a faltar para llegar a la ubicacion mas lejana del 
"""
import networkx as nx

def get_user_positions(user_owner_positions,color,grid):
    pending_nodes = [(0,0)]
    while pending_nodes:
        current = pending_nodes.pop()
        current_x, current_y = current
        user_owner_positions.add((current_x,current_y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Arriba, derecha, abajo, izquierda
            x, y = current_x + dx, current_y + dy
            if(0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[x][y] == color and ((x,y) not in pending_nodes) and tuple([x,y]) not in user_owner_positions ): # Ver que este en grilla
                pending_nodes.append((x, y))


def heuristic_1(node_new_color, grid, colorAmount):
    playerPosition = (len(grid)+1, len(grid)+1)
    graph = GraphGenerator(grid,playerPosition)
    SCORE = 0
    optionsDict = dict(nx.all_pairs_dijkstra(graph))
    maxValue = 0
    for key in optionsDict[playerPosition][SCORE]:
        if optionsDict[playerPosition][SCORE][key] > maxValue:
            maxValue = optionsDict[playerPosition][SCORE][key]
    return maxValue





def GraphGenerator(grid, playerPosition):
    graph = nx.Graph()
    graph.add_node(playerPosition)
    user_owner_positions = set()
    
    get_user_positions(user_owner_positions, grid[0][0], grid)

    for i in range(len(grid)):
        for j in range(len(grid)):
            currPosition = (i,j)
            if currPosition not in user_owner_positions:
                graph.add_node(currPosition)
                if i > 0:
                    top = (i - 1 ,j)
                    graph.add_node(top)
                    if top in user_owner_positions:
                        graph.add_edge(playerPosition, currPosition, weight=1)
                    elif grid[i][j] == grid[i - 1 ][j] :
                        graph.add_edge(currPosition, top, weight=0)
                    else:
                        graph.add_edge(currPosition, top, weight=1)

                if j > 0:
                    left = (i,j - 1) 
                    graph.add_node(left)
                    if left in user_owner_positions:
                        graph.add_edge(playerPosition, currPosition, weight=1)
                    elif grid[i][j] == grid[i][j - 1] : 
                        graph.add_edge(currPosition, left, weight=0)
                    else:
                        graph.add_edge(currPosition, left, weight=1)

                if j < len(grid[i]) - 1 :
                    right = (i,j + 1) 
                    graph.add_node(right)
                    if right in user_owner_positions:
                        graph.add_edge(playerPosition, currPosition, weight=1)
                    elif grid[i][j] == grid[i][j + 1] :  
                        graph.add_edge(currPosition, right, weight=0)
                    else:
                        graph.add_edge(currPosition, right, weight=1)

                if i < len(grid) - 1:
                    down = (i + 1 ,j) 
                    graph.add_node(down)
                    if down in user_owner_positions:
                        graph.add_edge(playerPosition, currPosition, weight=1)
                    elif grid[i][j] == grid[i + 1 ][j] :
                        graph.add_edge(currPosition, down, weight=0)
                    else:
                        graph.add_edge(currPosition, down, weight=1)
    return graph

