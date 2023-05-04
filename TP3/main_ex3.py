from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.tanhLayer import TanhLayer
from Exercise3.src.reluLayer import ReLuLayer
from src.utils import get_accuracy_xor
from src.utils import plot_errors
import numpy as np
import json

def read_and_load_json_data():
    with open('./Exercise3/config1.json', 'r') as config_file:
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
    learning_rate, epochs_amount, beta1, beta2, min_error,optimization_method,momentum = read_and_load_json_data()
    layer1=TanhLayer(2,2)
    layer2=TanhLayer(1,2)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(learning_rate,layers,epochs_amount,min_error,beta1,beta2,optimization_method,momentum)
    x=np.array([[1,1],[0,0],[1,0],[0,1]])
    y=np.array([[-1],[-1],[1],[1]])
    error_in_epochs = perceptron.train(x,y)
    #results = perceptron.test(x[:2],y)
    plot_errors(error_in_epochs,"MultiLayer Perceptron a")
    #print("Linear Accuracy: " + str(get_accuracy_xor(results,y[:2])))

if __name__ == "__main__":
    main()