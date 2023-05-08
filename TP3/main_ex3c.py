from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.linearLayer import LinearLayer
from Exercise3.src.reluLayer import ReLuLayer
from Exercise3.src.sigmoidalLayer import SigmoidalLayer
from src.utils import get_accuracy_numbers
from src.utils import plot_errors

import json
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

def read_and_load_json_data():
    with open('./Exercise3/config2.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    learning_rate = float(data_from_json["learning_rate"])
    epochs_amount = int(data_from_json["epochs"])
    min_error = float(data_from_json["min_error"])
    optimization_method = str(data_from_json["optimisation_method"] )
    momentum = float(data_from_json["momentum"] )

    return learning_rate, epochs_amount, min_error,optimization_method,momentum

def addNoise(data,prob):
    for image in data:
        for pixel in image:
            if np.random.rand()<prob:
                if pixel==1:
                    pixel=0.0
                else:
                    pixel=1.0
    return data

def main():
    data = read_and_load_txt_data()
    learning_rate, epochs_amount, min_error,optimization_method,momentum = read_and_load_json_data()
    layer1=SigmoidalLayer(5,35)
    layer2=SigmoidalLayer(10,5)
    layer3=ReLuLayer(10,10)
    layers=np.array([layer1,layer2,layer3])
    perceptron=MultilayerPerceptron(learning_rate,layers,epochs_amount,min_error,optimization_method,momentum)
    data=addNoise(data,0.15)
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
    expected_result = np.array([0,1,2,3,4,5,6,7,8,9])
    error_in_epochs = perceptron.train(x[:8],y[:8])
    result = perceptron.test(data[8:],y[8:])
    plot_errors(error_in_epochs,"MultiLayer Perceptron c")
    print("results son:" + str(result))
    print("Linear Accuracy: " + str(get_accuracy_numbers(result,expected_result[8:])))

if __name__ == "__main__":
    main()


