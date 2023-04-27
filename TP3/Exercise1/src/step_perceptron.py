import numpy as np

from src.perceptron import Perceptron

class StepPerceptron(Perceptron):

    def __init__(self, learning_rate, epochs):
        super().__init__(learning_rate, "STEP", epochs)


    def activation(self, x):
        return np.where(x >= 1, 1, -1)

    def train(self, x, y):
        j = 0
        #Agrega un X0=1 a cada entrada
        x = np.array(list(map(lambda t: np.append(t, [-0.2]), x)), dtype=float)
        error_in_epochs = []
        error = 0
        weights = np.random.rand(len(x[0]))/3
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