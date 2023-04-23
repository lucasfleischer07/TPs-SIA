import numpy as np

from src.perceptron import Perceptron

class StepPerceptron(Perceptron):

    def __init__(self, learning_rate, epochs):
        super().__init__(learning_rate, "STEP", epochs)


    #  Opcion 1 (Otro TP)
    # def activation(self, excitation):
    #     return 1.0 if excitation >= 0.0 else -1.0

    #  Opcion 2 (Chat)
    def activation(self, x):
        return np.where(x >= 1, 1, -1)

    # Otro TP
    def error(self, w):
        error = 0
        for i in range(len(self.training)):
            excitation = np.inner(self.training[i], w)
            output = self.activation(excitation)
            error += (self.expected_output[i] - output) ** 2
        return error / len(self.training)
