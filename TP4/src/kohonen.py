import numpy as np
import matplotlib.pyplot as plt
from statistics import mean,stdev
import seaborn as sn


def init_weights(size, data):
    weights = np.zeros((size**2, len(data[0]))) #25 filas 7 columnas
    choices = np.zeros(size**2)

    # weights = np.zeros((size, len(data[0]))) #25 filas 7 columnas
    # choices = np.zeros(size)

    for i in range(len(weights)): #da 25 (k^2)
        for j in range(len(weights[i])):
            weights[i][j] = data[np.random.choice(len(data))][j]
    
    return weights, choices

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def find_winner(weights, x):
    distances = [euclidean_distance(weights[i], x) for i in range(len(weights))]
    return np.argmin(distances)

#centrar los datos alrededor de cero y escalarlos para que tengan una varianza unitaria. media cero y varianza uno en cada columna. 
def estandarize_data_func(data, dataSize, ParametersSize):
    for i in range(ParametersSize):
        m = mean(data[:,i])
        s = stdev(data[:,i])
        for j in range(dataSize):
            data[j][i]=(data[j][i]-m)/s
    return data

def is_coord_valid(i, j,size):
    return 0 <= i < size and 0 <= j < size
def getNeighbours(winner,k,radius):
        base_i=winner % k
        base_j=np.floor(winner/k)
        neighbours = []
        for i in range(int(base_i - radius), int(base_i + radius + 1)):
            for j in range(int(base_j - radius), int(base_j + radius + 1)):
                if (i - base_i) ** 2 + (j - base_j) ** 2 <= radius ** 2 and is_coord_valid(i, j,k):
                    if (j*k)+i not in neighbours:
                        neighbours.append((j*k)+i)
        return neighbours

def train_kohonen(data, size, iterations, learning_rate, initial_radius, final_radius,countries):
    dataSize=len(data)
    parametersSize=(len(data[0]))
    estandarize_data = estandarize_data_func(data, dataSize, parametersSize)
    weights, choices = init_weights(size, estandarize_data)
    radius = initial_radius
    decay = iterations / np.log(initial_radius / final_radius)
    distances=[]
    for i in range(iterations):
        x = estandarize_data[np.random.choice(len(estandarize_data))]
        winner = find_winner(weights, x)
        choices[winner] += 1 #cuantos datos caen a tal neurona
        neighbours=getNeighbours(winner,size,radius)
        for j in range(len(neighbours)):
                weights[neighbours[j]] = weights[neighbours[j]] + learning_rate*(x-weights[neighbours[j]])          
        radius = initial_radius / (1 + i/decay)
        if radius<1:
            radius=1
    results = [[] for _ in range(size**2)]

    
    for i in range(len(estandarize_data)):
        winner=find_winner(weights, estandarize_data[i])
        results[winner].append(countries[i])
    for i in range(len(weights)):
        aux=[]
        neighbours=getNeighbours(i,size,1)
        for j in range (len(neighbours)):
            aux.append(euclidean_distance(weights[i],weights[neighbours[j]]))
        distances.append(mean(aux))
    return weights, choices, results,distances


def plot_heatmap_kohonen(results, k, learn_rate):
    matrix = np.zeros((k, k))

    # Iteramos sobre los elementos del array 'results'
    for i in range(len(results)):
        # Si el array interno no está vacío
        if results[i]:
            # Obtenemos la posición en la matriz correspondiente
            row = i // k
            col = i % k
            # Agregamos la cantidad de elementos en la posición correspondiente
            matrix[row][col] += len(results[i])

    plt.title(f"Classification heatmap. Learn_rate: {learn_rate}")
    sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    plt.show()



def plot_countries_in_nodes(results, k, learn_rate):
    matrix = np.zeros((k, k))
    matrix_countries_per_node = np.empty((k, k), dtype=str)
    # Iteramos sobre los elementos del array 'results'
    for i in range(len(results)):
        # Si el array interno no está vacío        
        if results[i]:
            # Obtengo el string de los paises de ese node
            node_text = str(results[i])
            # Obtenemos la posición en la matriz correspondiente
            row = i // k
            col = i % k

            # Agregamos la cantidad de elementos en la posición correspondiente
            matrix[row][col] += len(results[i])
            # Agregamos los paises del nodo en la posición correspondiente
            matrix_countries_per_node[row][col] = node_text

    plt.title(f"Classification heatmap. Learn_rate: {learn_rate}")
    ax = sn.heatmap(matrix, cmap='YlGnBu', annot=True)

    for i in range(k):
        for j in range(k):
            ax.text(j + 0.5, i + 0.5, matrix_countries_per_node[i][j] , ha='center', va='center', color='black', fontsize=8)
    plt.show()

def plotVariableHeatMap(weights,k,name):
    grid = np.reshape(weights, (k, k))
    plt.imshow(grid, cmap='YlGnBu', interpolation='nearest')
    plt.grid(color='black', linewidth=2)
    plt.colorbar()
    plt.xticks([])
    plt.yticks([])
    # Add labels and title
    plt.title(name+' heatmap')

    # Show the plot
    plt.show()
    
def plotDistanceHeatMap(distances,k):
    grid = np.reshape(distances, (k, k))
    plt.imshow(grid, cmap='YlGnBu', interpolation='nearest')
    plt.grid(color='black', linewidth=2)
    for i in range(k):
        for j in range(k):
            plt.text(j, i, f'{distances[j % k+(k-1)*i]:.2f}', ha='center', va='center', color='black')
    plt.colorbar()
    plt.xticks([])
    plt.yticks([])
    # Add labels and title
    plt.title('Neighbour distance heatmap')

    # Show the plot
    plt.show()



def plot_countries_in_nodes(results, k, learn_rate):
    matrix = np.zeros((k, k))
    matrix_countries_per_node = np.empty((k, k) ,dtype=np.dtype('U100'))
    # Iteramos sobre los elementos del array 'results'
    for i in range(len(results)):
        # Si el array interno no está vacío        
        if results[i]:
            row = i // k
            col = i % k
            # Agregamos la cantidad de elementos en la posición correspondiente
            matrix[row][col] += len(results[i])
            # Agregamos los paises del nodo en la posición correspondiente
            matrix_countries_per_node[row][col] = re.sub(r"[\[\]']", "", str(results[i]))  


    plt.title(f"Classification heatmap. Learn_rate: {learn_rate}")
    print('la matris de texto es: ' + str(matrix_countries_per_node))
    ax = sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    for i in range(k):
        for j in range(k):
            text = matrix_countries_per_node[i][j]
            text_wrapped = textwrap.fill(text, width=22)  # Ajusta el ancho de las líneas según tus necesidades
            ax.text(j + 0.5, i + 0.70, text_wrapped, ha='center', va='center', color='black', fontsize=8)
    plt.show()