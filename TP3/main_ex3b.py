from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.linearLayer import LinearLayer
from Exercise3.src.reluLayer import ReLuLayer
from Exercise3.src.sigmoidalLayer import SigmoidalLayer
from Exercise3.src.tanhLayer import TanhLayer

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
    layer1=SigmoidalLayer(16,35)
    layer2=ReLuLayer(1,16)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(0.01,layers,5000,0.02,0,0)
    x=data
    y=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])
    perceptron.train(x[2:],y[2:])
    perceptron.test(x[:2],y[:2])
    

if __name__ == "__main__":
    main()