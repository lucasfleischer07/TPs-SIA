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
        deltas=[np.zeros((self.layers[i].nodes)) for i in range(len(self.layers))]
        prevDeltas=np.array([])
        for i in range(len(self.layers)-1, -1, -1):
            #get all deltas 

            for j in range(self.layers[i].nodes):

                if i==len(self.layers)-1:
                    

                    deltas[i][j]=self.layers[i].derivative(results[i][j])*(y[j]-results[i][j])
                    
                else:

                    deltas[i][j]=self.layers[i].derivative(results[i][j])*(sum(self.layers[i+1].weights[:,j] * deltas[i+1]))

            #update node weights
        for i in range(len(self.layers)-1, -1, -1):
            for j in range(self.layers[i].nodes):
                for s in range(len(self.layers[i].weights[j])):
                    if i==0:

                        self.layers[i].weights[j,s]+=self.learningRate*deltas[i][j]*x[s]
                    else:

                        self.layers[i].weights[j,s]+=self.learningRate*deltas[i][j]*results[i-1][s]
                self.layers[i].bias[j]+=self.learningRate*deltas[i][j]
        

    def train(self,x,y):
        errors=[0]
        for epoch in range(self.epochs):
            if epoch % 1000 ==0:
                print("epoch "+str(epoch))
                print(errors[epoch])
            for i in range(len(x)):
                propagateResults=self.fowardPropagate(x[i])
                errors.append(sum(np.abs(np.subtract(propagateResults[len(propagateResults)-1],y[i]))))
                self.backwardsPropagate(propagateResults,x[i],y[i])
        allResults=[]
        for i in range(len(x)):
            results=self.fowardPropagate(x[i])
            allResults.append(results[len(results)-1])
            print("input="+str(i)+"output=")
            for elem in results[len(results)-1]:
                print("{:.4f}".format(elem))
            print( " expected output= " + str(y[i]))
        print("error entrenamiento="+str(sum(sum(np.abs(np.subtract(allResults,y))))))
    def test(self,x,y):
        print("TEST")
        allResults=[]
        for i in range(len(x)):
            results=self.fowardPropagate(x[i])
            allResults.append(results[len(results)-1])
            print("input="+str(i)+"output=")
            for elem in results[len(results)-1]:
                print("{:.4f}".format(elem))
            print( " expected output= " + str(y[i]))
        print("error test="+str(sum(sum(np.abs(np.subtract(allResults,y))))))

        
        

        

               
