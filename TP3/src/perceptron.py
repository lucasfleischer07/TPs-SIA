import numpy as np
import copy
from abc import ABC, abstractmethod 

class Perceptron(ABC):
    def __init__(self, learning_rate, perceptron_type, epochs, error_min):
        self.learning_rate = learning_rate
        self.error_min = error_min
        self.w_min = None
        self.perceptron_type = perceptron_type
        self.epochs = epochs
    

    @abstractmethod
    def activation(self, excitation):
        pass

    
    @abstractmethod
    def derivative(self, exitated_val):
        pass    
    

    def train(self, x, y):
        j = 0
        # Agrega un X0=1 a cada entrada
        x = np.array(list(map(lambda t: np.append( [-1],t), x)), dtype=float)
        error_in_epochs = []
        error = 0
        weights = np.random.rand(len(x[0]))/10
        for epoch in range(self.epochs):
            j += 1
            error = 0
            for i in range(len(x)):
                # print("X["+str(i)+"]: " + str(x[i]))
                # print("Y["+str(i)+"]: " + str(y[i]))

                output = self.activation(np.inner(x[i], weights))   
                delta = self.learning_rate * (y[i] - output) * self.derivative(output)
                
                #print("DIFERENCIA["+str(i)+"]: " + str(y[i] - output))
                # print("OUTPUT["+str(i)+"]: " + str(output))
                #print("DELTA W["+str(i)+"]: " + str(delta * x[i]))
                print("WEIGHTS PRE CAMBIO "+str(weights))
                weights += (delta * x[i])
                print("WEIGHTS POST CAMBIO "+str(weights))
            
            error = self.error(x,y,weights)
            error_in_epochs.append(error)

            if error <= self.error_min:
                break

            print("NEW WEIGHTS "+str(weights))

        return j,weights,error_in_epochs,error


    # cuanto mas cercano a cero es mejor, habria q cambiarlo para que cuanto mayor mejor 
    # ahora devuelve el accurance de todo el cjto de datos
    # Recieves the testing set and trained wheigts, returns the results calculated
    def evaluate(self, x, y, train_wheigts):
        complete_x = np.array(list(map(lambda t: np.append( [-1],t), x)), dtype=float) #agrega el uno al ppio
        results = []
        for i in range(len(complete_x)):
            excitation = np.inner(complete_x[i], train_wheigts)
            results.append(self.activation(excitation))
        print("\nRESULTS: " + str(results))
        print("\nY: " + str(y))
        return (1 / len(x)) * sum(abs(np.array(results) - np.array(y)))
