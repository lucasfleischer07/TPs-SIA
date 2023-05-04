import numpy as np
import json
import csv

from Exercise2.src.linear_perceptron import LinearPerceptron
from Exercise2.src.no_linear_perceptron import NoLinearPerceptron
from src.utils import plot_errors
from src.utils import get_accuracy
from src.utils import get_accuracy_non_lineal
from src.utils import escalate

def read_and_load_csv_data():
    with open('Exercise2/docs/TP3-ej2-conjunto-pruebas.csv', 'r') as csv_file:
        plots = csv.reader(csv_file, delimiter=',')
        next(plots)   # Para skipear la linea de x1,x2,x3 e y

        data = []
        expected_output = []

        for row in plots:
            # data.append([float(row[0]), float(row[1]), float(row[2])])
            # expected_output.append(float(row[3]))
        
            # Para el de pruebas
            data.append([float(row[0])])
            expected_output.append(float(row[1]))

        csv_file.close()

    return data, expected_output


def read_and_load_json_data():
    with open('./Exercise2/config.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    learning_rate = float(data_from_json["learning_rate"])
    perceptron = str(data_from_json["perceptron"])
    epochs_amount = int(data_from_json["epochs"])
    beta = float(data_from_json["beta"])
    min_error = float(data_from_json["min_error"])
    test_size = int(data_from_json["test_size"])

    return learning_rate, perceptron, epochs_amount, beta, min_error, test_size


def main(): 
    data, expected_output = read_and_load_csv_data()
    learning_rate, perceptron, epochs_amount, beta, min_error, test_size = read_and_load_json_data()

    if(perceptron == 'LINEAR'):
        perceptron = LinearPerceptron(learning_rate, epochs_amount, min_error)
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:test_size], expected_output[:test_size])
        print("error in epochs " + str(error_in_epochs))
        accuracy = get_accuracy(expected_output[test_size:], perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights))
        print("Linear Accuracy: " + str(accuracy))
        print("The evaluate results are: " + str(perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights)))
        print("The expected results are: " + str(expected_output[test_size:]))
        plot_errors(error_in_epochs, "Linear Perceptron")
    elif(perceptron == 'NO_LINEAR'):
        expected_output = escalate(expected_output)
        perceptron = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output), (expected_output))
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:test_size], expected_output[:test_size])
        print("error in epochs " + str(error_in_epochs))
        accuracy = get_accuracy_non_lineal(expected_output[test_size:], perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights))
        print("No linear Accuracy: " + str(accuracy))
        print("The evaluate results are: " + str(perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights)))
        print("The expected results are: " + str(expected_output[test_size:]))
        plot_errors(error_in_epochs,"Non Linear Perceptron")
    else:
        print("Perceptron not found")
        exit(1)


if __name__ == "__main__":
    main()