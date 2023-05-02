import numpy as np

from src.layer import Layer

class SenoidalLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        return 1 if np.sin(excitation) >= 0 else -1
    
    def derivative(self, exitated_val):
        return np.cos(exitated_val)
    
    def propagate(self, x):
        return super().propagate(x)