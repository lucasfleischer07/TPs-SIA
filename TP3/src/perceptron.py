import numpy as np
from abc import ABC, abstractmethod 

class Perceptron(ABC):
    def _init_(self, training_array, expected_output, learning_rate, perceptron_type):
        # TODO: Ver el martes el tema del intervalo de pesos

        self.training_array = np.array(list(map(lambda t: np.append(t, [1]), training_array)), dtype=float)
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None
        self.perceptron_type = perceptron_type
    

    @abstractmethod
    def activation(self, excitation):
        pass
    
    # Del chat
    def train(self, x, y, epochs=100):
        i = 0
        for epoch in range(epochs):
            i += 1
            error = 0
            for i in range(len(x)):
                output = self.activation(np.dot(x[i], self.weights))    
                delta = self.learning_rate * (y[i] - output)
                self.weights += delta * x[i]
                error += int(delta != 0.0)
            if error == 0:
                break
        return i,self.weights

    def plot(self, X):

