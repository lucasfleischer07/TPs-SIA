import numpy as np
import json
import csv

from Exercise2.src.linear_perceptron import LinearPerceptron
from Exercise2.src.no_linear_perceptron import NoLinearPerceptron
from src.utils import plot_accuracies


def escalate(data):
    min_expected = min(data)
    max_expected = max(data)

    data = np.array(data)
    data = 2 * ((data - min_expected) / (max_expected - min_expected)) - 1

    return data


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
    beta = float(data_from_json["beta"])
    min_error = float(data_from_json["min_error"])

    return learning_rate, perceptron, epochs_amount, beta, min_error


def main(): 
    data, expected_output = read_and_load_csv_data()
    learning_rate, perceptron, epochs_amount, beta, min_error = read_and_load_json_data()

    if(perceptron == 'LINEAR'):
        perceptron = LinearPerceptron(learning_rate, epochs_amount, min_error)
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:22], expected_output[:22])
        print("The amount of epochs are: " + str(epochs_taken) + " with errors: " + str(error_in_epochs))
        print("The evaluate results are: " + str(perceptron.evaluate(data[22:],expected_output[22:],final_weights)))
        print("The expected results are: " + str(expected_output[22:]))
        #print("\nLinear Error: " + str(perceptron.evaluate(data[22:],expected_output[22:],final_weights)))
    elif(perceptron == 'NO_LINEAR'):
        
        expected_output = escalate(expected_output)
        print("El conjunto de results queda: " + str(expected_output) )
        perceptron = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output), (expected_output))
        epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:22], expected_output[:22])
        # print("The amount of epochs are: " + str(epochs_taken) + " with errors: " + str(error_in_epochs))
        print("Los errores fueron: " + str(error_in_epochs) )
        print("La cantidad de epocas son: " + str(epochs_taken))
        print("The evaluate results are: " + str(perceptron.evaluate(data[22:],expected_output[22:],final_weights)))
        print("The expected results are: " + str(expected_output[22:]))
        # print("\nNo Linear Error: " + str(perceptron.evaluate(data[22:],expected_output[22:],final_weights)))
    else:
        print("Perceptron not found")
        exit(1)


if __name__ == "__main__":
    main()