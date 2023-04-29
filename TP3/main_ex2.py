import numpy as np
import json
import csv

from Exercise2.src.linear_perceptron import LinearPerceptron
from Exercise2.src.no_linear_perceptron import NoLinearPerceptron
from src.utils import plot_accuracies


def read_and_load_csv_data():
    with open('Exercise2/docs/TP3-ej2-conjunto.csv', 'r') as csv_file:
        plots = csv.reader(csv_file, delimiter=',')
        next(plots)   # Para skipear la linea de x1,x2,x3 e y

        data = []
        expected_output = []

        for row in plots:
            print(row)
            data.append([float(row[0]), float(row[1]), float(row[2])])
            expected_output.append(float(row[3]))

        csv_file.close()

    return data, expected_output


def read_and_load_json_data():
    with open('./Exercise2/config.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    learning_rate = float(data_from_json["learning_rate"])
    perceptron = str(data_from_json["perceptron"])
    epochs_amount = int(data_from_json["epochs"])
    beta = int(data_from_json["beta"])
    min_error = int(data_from_json["min_error"])

    return learning_rate, perceptron, epochs_amount, beta, min_error
    

def main(): 
    data, expected_output = read_and_load_csv_data()
    learning_rate, perceptron, epochs_amount, beta, min_error = read_and_load_json_data()

    if(perceptron == 'LINEAR'):
        perceptron = LinearPerceptron(learning_rate, epochs_amount, min_error)
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:22], expected_output[:22])
        print("The amount of epochs are: " + str(epochs_taken) + " with errors: " + str(error_in_epochs))
        print("linear error: " + str(perceptron.evaluate(data[22:],expected_output[22:],final_weights)))
    elif(perceptron == 'NO_LINEAR'):
        perceptron = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, min(expected_output), max(expected_output))
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:22], expected_output[:22])
    else:
        print("Perceptron not found")
        exit(1)


if __name__ == "__main__":
    main()