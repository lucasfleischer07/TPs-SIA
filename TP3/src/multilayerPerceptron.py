import numpy as np
import copy
from abc import ABC, abstractmethod

class MultilayerPerceptron(ABC):
    def __init__(self, learning_rate, layers, epochs, error_min,beta1,beta2):
        self.learningRate = learning_rate
        self.error_min = error_min
        self.w_min = None
        self.epochs = epochs
        self.layers=layers
        self.prevFirstMomentum=0
        self.prevSecondMomentum=0
        self.beta1=beta1
        self.beta2=beta2
        

    def fowardPropagate(self,x):
        propagateResults=[np.zeros((1, self.layers[i].nodes)) for i in range(len(self.layers))]
        for i in range(len(self.layers)):
            if i == 0:
                propagateResults[i]=self.layers[i].propagate(x)
            else:
                propagateResults[i]=self.layers[i].propagate(propagateResults[i-1])
        return propagateResults

    #https://www.youtube.com/watch?v=boP3O89rErA&ab_channel=BitBoss
    def backwardsPropagate(self,results,x,y):
        deltas=np.array([])
        prevDeltas=np.array([])
        for i in range(len(self.layers)-1, -1, -1):
            #get all deltas  
            for j in range(self.layers[i].nodes):
                if i==len(self.layers)-1:
                    deltas=np.append(deltas,self.layers[i].derivative(results[i][j])*(y[j]-results[i][j]))
                    
                else:
                    deltas=np.append(deltas,self.layers[i].derivative(results[i][j])*(sum(self.layers[i+1].weights[:,j] * prevDeltas)))
            
            #update node weights
            for j in range(self.layers[i].nodes):
                for s in range(len(self.layers[i].weights[j])):
                    if i==0:
                        self.layers[i].weights[j,s]+=self.learningRate*deltas[j]*x[s]
                    else:
                        self.layers[i].weights[j,s]+=self.learningRate*deltas[j]*results[i-1][s]
                self.layers[i].bias[j]+=self.learningRate*deltas[j]
            prevDeltas=deltas.copy()

    def train(self,x,y):
        print("START WEIGHT")
        for layer in self.layers:
            print(layer.weights)


        for epoch in range(self.epochs):
            for i in range(len(x)):
                propagateResults=self.fowardPropagate(x[i])
                self.backwardsPropagate(propagateResults,x[i],y[i])
        for i in range(len(x)):
            print("input="+str(x[i])+"output="+ str(self.fowardPropagate(x[i])[1]))

        print("END WEIGHT")
        for layer in self.layers:
            print(layer.weights)
        
        

        

               
