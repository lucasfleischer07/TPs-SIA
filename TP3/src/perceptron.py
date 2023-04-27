import numpy as np
import copy
from abc import ABC, abstractmethod 

class Perceptron(ABC):
    def __init__(self, learning_rate, perceptron_type, epochs):
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None
        self.perceptron_type = perceptron_type
        self.epochs = epochs
    

    @abstractmethod
    def activation(self, excitation):
        pass
    

    def train(self, x, y):
        pass