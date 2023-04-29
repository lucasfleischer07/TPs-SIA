import numpy as np

from src.perceptron import Perceptron

class NoLinearPerceptron(Perceptron):

    def __init__(self, learning_rate, epochs, beta, min_error, min_val, max_val ):
        super().__init__(learning_rate, "NO_LINEAR", epochs, min_error)
        self.beta = beta
        self.min_val = min_val - 0.10*(max_val-min_val)
        self.max_val = max_val + 0.10*(max_val-min_val)


    def activation(self, exitated_val):
        return (np.tanh(self.beta * exitated_val) + 1) * 0.5 * (self.max_val - self.min_val) + self.min_val


    def error(self,x,y,w):
        error = 0
        for i in range(len(x)):
            output = np.inner(x[i], w)
            error += np.power((y[i] - output), 2)
        return  error / 2


    def derivative_activation(self, exitated_val):
        return self.beta * ( 1 - np.tanh(self.beta * exitated_val) ** 2)
        