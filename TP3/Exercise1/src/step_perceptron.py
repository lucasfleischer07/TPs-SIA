import numpy as np

from src.perceptron import Perceptron

class StepPerceptron(Perceptron):

    def __init__(self, learning_rate, epochs):
        super().__init__(learning_rate, "STEP", epochs, 0)


    def activation(self, x):
        return np.where(x >= 1, 1, -1)


    def derivative(self, exitated_val):
        return 1

    # Retorna la cantidad de errores
    def error(self,x,y,w):
        error = 0
        for i in range(len(x)):
            excitation = np.inner(x[i], w)
            output = self.activation(excitation)
            error += int((y[i] - output) != 0.0)
        return error 