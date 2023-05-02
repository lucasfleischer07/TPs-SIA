import math

from src.layer import Layer

class SigmoidalLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        s = 1 / (1 + math.exp(-excitation))
        return s
    
    def derivative(self, exitated_val):
        s = self.activation(exitated_val)
        ds = s * (1 - s)
        return ds
     
    def propagate(self, x):
        return super().propagate(x)