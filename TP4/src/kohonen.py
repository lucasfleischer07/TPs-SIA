import numpy as np
import matplotlib.pyplot as plt


def init_weights(size, data):
    weights=np.zeros(size**2, data.shape[1])
    for i in range(weights):
        for j in range(weights[i]):
            weights[i][j]=data[np.random.choice(data.shape[0])][j]

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def find_winner(weights, x):
    distances = [euclidean_distance(weights[i], x) for i in range(len(weights))]
    return np.argmin(distances)

def estandarizeData(data):
    for i in range(data.shape[1]):
        mean=np.sum(data[:,i])/data.shape[0]
        deviation=np.sqrt(np.sum(data[:i]-mean)/data.shape[0])
        for j in range(data.shape[0]):
            data[j][i]=(data[j][i]-mean)/deviation
    return data
        

def train_kohonen(data, size, iterations, learning_rate,initialRadius,finalRadius):
    estandarizedData=estandarizeData(data)
    weights = init_weights(size, estandarizedData)
    radius=initialRadius
    decay=iterations / np.log(initialRadius / finalRadius)
    for i in range(iterations):
        x = data[np.random.choice(estandarizeData.shape[0])]
        winner = find_winner(weights, x)
        for j in range(estandarizedData.shape[0]):
            if j!=winner:
                if np.abs(weights[winner] - weights[j]) < radius:
                    weights[j]=weights[j]+learning_rate*(x-weights[j])
        radius = initialRadius / (1 + i/decay)
    return weights