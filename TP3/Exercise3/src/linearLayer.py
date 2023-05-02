
from src.layer import Layer

class LinearLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        return excitation
    
    def derivative(self, exitated_val):
        return 1
    
    def propagate(self, x):
        return super().propagate(x)
    