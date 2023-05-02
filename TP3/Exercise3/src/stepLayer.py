import numpy as np

from src.layer import Layer

class StepLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        return np.where(excitation >= 1, 1, -1)
    def derivative(self, exitated_val):
        return 1
    
    def propagate(self, x):
        return super().propagate(x)
    