import numpy as np
import copy
from abc import ABC, abstractmethod 

class Perceptron(ABC):
    def __init__(self, learning_rate, perceptron_type, epochs):
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None
        self.perceptron_type = perceptron_type
        self.epochs = epochs
    

    @abstractmethod
    def activation(self, excitation):
        pass
    

    def train(self, x, y):
        j = 0
        #Agrega un X0=1 a cada entrada
        x = np.array(list(map(lambda t: np.append(t, [1]), x)), dtype=float)
        error_in_epochs = []
        error = 0
        weights = np.random.rand(len(x[0]))
        for epoch in range(self.epochs):
            j += 1
            error = 0
            for i in range(len(x)):
                output = self.activation(np.dot(x[i], weights))    
                delta = self.learning_rate * (y[i] - output)
                weights += delta * x[i]
                error += int(delta != 0.0)
            error_in_epochs.append(error)
        
            if error == 0:
                break

        return j,weights,error_in_epochs,error