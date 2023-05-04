from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.linearLayer import LinearLayer
from Exercise3.src.reluLayer import ReLuLayer
from Exercise3.src.sigmoidalLayer import SigmoidalLayer
from Exercise3.src.tanhLayer import TanhLayer
from src.utils import get_accuracy_even
from src.utils import plot_errors

import numpy as np
import json


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
    beta1 = float(data_from_json["beta1"])
    beta2 = float(data_from_json["beta2"])
    min_error = float(data_from_json["min_error"])
    optimization_method = str(data_from_json["optimisation_method"] )
    momentum = float(data_from_json["momentum"] )

    return learning_rate, epochs_amount, beta1, beta2, min_error,optimization_method,momentum

def main():
    data = read_and_load_txt_data()
    learning_rate, epochs_amount, beta1, beta2, min_error,optimization_method,momentum = read_and_load_json_data()
    layer1=SigmoidalLayer(16,35)
    layer2=ReLuLayer(1,16)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(learning_rate,layers,epochs_amount,min_error,beta1, beta2,optimization_method,momentum)
    x=data
    y=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])
    error_in_epochs = perceptron.train(x[2:],y[2:])
    results = perceptron.test(x[:2],y[:2])
    plot_errors(error_in_epochs,"MultiLayer Perceptron b")
    print("Linear Accuracy: " + str(get_accuracy_even(results,y[:2])))

if __name__ == "__main__":
    main()