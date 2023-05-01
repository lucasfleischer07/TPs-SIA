import numpy as np
import copy
from abc import ABC, abstractmethod

def __init__(self,nodes,inputSize):
    self.nodes=nodes
    self.inputSize=inputSize
    self.weights=(np.random.rand(inputSize, nodes)-0.5)/2
    self.firstMomentums=np.zeros(nodes)
    self.secondMomentums=np.zeros(nodes)
    self.bias=(np.random.rand(nodes)-0.5)/2

@abstractmethod
def activation(self, excitation):
    pass


@abstractmethod
def derivative(self, exitated_val):
    pass 

def propagate(self,x):
    propagateResults=np.array([])
    for i in range(self.nodes):
        propagateResults=np.append(propagateResults,self.activation(np.inner(x,self.weights[i])-self.bias[i]))
    return propagateResults



