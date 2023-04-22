import numpy as np

class Perceptron:
    def _init_(self, input_size):
        self.weights = np.random.uniform(-0.5, 0.5, input_size)
        self.learning_rate = 0.1
    
    
    def activation(self, x):
        return np.where(x >= 0, 1, -1)
    

    def train(self, x, y, epochs=100):
        for epoch in range(epochs):
            error = 0
            for i in range(len(x)):
                output = self.activation(np.dot(x[i], self.weights))
                delta = self.learning_rate * (y[i] - output)
                self.weights += delta * x[i]
                error += int(delta != 0.0)
            if error == 0:
                break
    

    def predict(self, x):
        return self.activation(np.dot(x, self.weights))