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
        

def train_kohonen(data, size, iterations, learning_rate, initial_radius, final_radius,countries):
    dataSize=len(data)
    parametersSize=(len(data[0]))
    estandarize_data = estandarize_data_func(data, dataSize, parametersSize)
    print(estandarize_data)
    weights, choices = init_weights(size, estandarize_data)
    radius = initial_radius
    decay = iterations / np.log(initial_radius / final_radius)
    for i in range(iterations):
        x = data[np.random.choice(len(data))]
        winner = find_winner(weights, x)
        choices[winner] += 1 #cuantos datos caen a tal neurona
        for j in range(len(weights)):
            if j != winner:
                if np.sum(np.abs(weights[winner] - weights[j])) < radius:
                    weights[j] = weights[j] + learning_rate*(x-weights[j])
        weights[winner] = weights[winner] + learning_rate*(x-weights[winner])
        radius = initial_radius / (1 + i/decay)
    results = [[] for _ in range(size**2)]

    
    for i in range(len(estandarize_data)):
        winner=find_winner(weights, estandarize_data[i])
        results[winner].append(countries[i])
        
    return weights, choices, results


def plot_heatmap(results, k, learn_rate):
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


