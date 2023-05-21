import numpy as np
import matplotlib.pyplot as plt
from statistics import mean


# Verifica si el promedio de los datos es casi cero, dentro de un umbral muy pequeño. 
# Esto puede ser utilizado como una condición para determinar si los datos cumplen con ciertas características 
# o propiedades esperadas en el algoritmo de Oja.
def valid_data_with_mean(data):
    mean_aux = 0
    for i in range(len(data[0])):       # Itero sobre cada columna de datos
        aux = data[:, i]
        mean_aux += mean(aux)           # Calculo el promedio utilizando la funcion mean y se la sumo
    return np.abs(mean_aux) < 0.000001


def train_oja(data_standarized, learning_rate, weights, max_epochs):
    if not valid_data_with_mean(data_standarized):
        print("Mean must be 0 for inputs")
        return
    
    for epochs in range(max_epochs):
        for data in data_standarized:
            s = np.dot(weights, data)
            weights = weights + learning_rate * s * (data - s * weights)
    
    return weights