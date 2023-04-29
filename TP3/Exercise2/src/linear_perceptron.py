import numpy as np

from src.perceptron import Perceptron

class LinearPerceptron(Perceptron):

    def __init__(self, learning_rate, epochs, min_error):
        super().__init__(learning_rate, "LINEAR", epochs, min_error)


    def activation(self, x):
        return x


    def error(self,x,y,w):
        error = 0
        for i in range(len(x)):
            output = np.inner(x[i], w)
            error = error + ((y[i] - output) ** 2)
        return  error / 2


    # def error(self, x, y, w):
    #     output = np.dot(x, w)
    #     error = np.sum(np.square(y - output)) / 2
    #     return error

    # def error(self, x, y, w):
    #     output = np.dot(x, w)
    #     error = np.linalg.norm(y - output) ** 2 / 2
    #     return error

    def derivative(self, exitated_val):
        return 1

