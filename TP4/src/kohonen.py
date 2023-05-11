import numpy as np
import matplotlib.pyplot as plt
from statistics import mean,stdev


def init_weights(size, data):
    weights=np.zeros((size**2, len(data[0])))
    choices=np.zeros(size**2)
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j]=data[np.random.choice(len(data))][j]
    return weights,choices
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def find_winner(weights, x):
    distances = [euclidean_distance(weights[i], x) for i in range(len(weights))]
    return np.argmin(distances)

def estandarizeData(data,dataSize,ParametersSize):
    for i in range(ParametersSize):
        m=mean(data[:,i])
        s=stdev(data[:,i])
        for j in range(dataSize):
            data[j][i]=(data[j][i]-m)/s
    print(data)
    return data
        

def train_kohonen(data, size, iterations, learning_rate, initial_radius, final_radius):
    dataSize=len(data)
    parametersSize=(len(data[0]))
    estandarizedData=estandarizeData(data,dataSize,parametersSize)
    weights,choices = init_weights(size, estandarizedData)
    radius=initial_radius
    decay=iterations / np.log(initial_radius / final_radius)
    for i in range(iterations):
        x = data[np.random.choice(len(data))]
        winner = find_winner(weights, x)
        choices[winner]+=1
        for j in range(len(weights)):
            if j!=winner:
                if np.sum(np.abs(weights[winner] - weights[j])) < radius:
                    weights[j]=weights[j]+learning_rate*(x-weights[j])
        weights[winner]=weights[winner]+learning_rate*(x-weights[winner])
        radius = initial_radius / (1 + i/decay)
    return weights,choices