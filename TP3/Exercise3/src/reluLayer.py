
from src.layer import Layer

class ReLuLayer(Layer):
    def __init__(self,nodes,inputSize):
        super().__init__(nodes,inputSize)

    def activation(self, excitation):
        return max(0,excitation)
    
    def derivative(self, exitated_val):
        return 1 if exitated_val > 0 else 0
    
    def propagate(self, x):
        return super().propagate(x)