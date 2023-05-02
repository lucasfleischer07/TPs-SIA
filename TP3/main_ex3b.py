from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.linearLayer import LinearLayer
from Exercise3.src.reluLayer import ReLuLayer
from Exercise3.src.sigmoidalLayer import SigmoidalLayer

import numpy as np


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

def main():
    data = read_and_load_txt_data()
    layer1=ReLuLayer(16,35)
    layer2=SigmoidalLayer(1,16)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(0.01,layers,10000,0.02,0,0)
    x=data[8:]
    y=np.array([[1],[-1],[1],[-1],[1],[-1],[1],[-1]])
    perceptron.train(x,y)

if __name__ == "__main__":
    main()