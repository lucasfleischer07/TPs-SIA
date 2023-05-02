from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.linearLayer import LinearLayer
from Exercise3.src.reluLayer import ReLuLayer
from Exercise3.src.sigmoidalLayer import SigmoidalLayer

import numpy as np
import random


def read_and_load_txt_data():
    with open('Exercise3/docs/TP3-ej3-digitos.txt', 'r') as txt_file:
        lines = txt_file.readlines()
        matriz = []
        matriz_actual = []

        for linea in lines:
            if linea.strip() == "":
                matriz.append(matriz_actual)
                matriz_actual = []
            else:
                elementos = linea.split()
                for elemento in elementos:
                    matriz_actual.append(float(elemento))
                

        matriz.append(matriz_actual)
        data = np.array(matriz)
        filas = data.shape
        #print("numero de cols" + str(cols))
        #data = np.concatenate(matriz, axis=1)
        #data = np.transpose(matriz)
    return data
def addNoise(data,prob):
    for image in data:
        for pixel in image:
            if np.random.rand()<prob:
                print("added noise")
                print(pixel)
                if pixel==1:
                    pixel=0.0
                else:
                    pixel=1.0
                print(pixel)
    return data
def main():
    data = read_and_load_txt_data()
    layer1=SigmoidalLayer(5,35)
    layer2=SigmoidalLayer(10,5)
    layer3=ReLuLayer(10,10)
    layers=np.array([layer1,layer2,layer3])
    perceptron=MultilayerPerceptron(0.01,layers,30000,0.02,0,0)
    data=addNoise(data,0.00)
    x=data[:8]
    y=[]
    
    for i in range(10):
        result=[]
        for j in range(10):
            if j==i:
                result.append(1)
            else:
                result.append(0)
        y.append(result)

    perceptron.train(x,y[:8])
    perceptron.test(data[8:],y[8:])
    

if __name__ == "__main__":
    main()


