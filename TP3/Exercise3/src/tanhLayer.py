import numpy as np

from src.layer import Layer

class TanhLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        return np.tanh(0.9 * excitation)

    def derivative(self, exitated_val):
        return 0.9 * ( 1 - np.tanh(0.9 * exitated_val) ** 2)
    
    def propagate(self, x):
        return super().propagate(x)