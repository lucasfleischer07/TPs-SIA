import numpy as np
import json

from Exercise1.src.step_perceptron import StepPerceptron
from src.utils import plot_graph
from src.utils import plot_errors


def set_initial_data(operation):
    if(operation == "and"):
        training_array = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
        expected_output = np.array([-1, -1, -1, 1])
        return training_array, expected_output
    elif(operation == "xor"):
        training_array = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
        expected_output = np.array([1, 1, -1, -1])
        return training_array, expected_output
    else:
        return [], []


def main(): 
    with open('./Exercise1/config.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    learning_rate = float(data_from_json["learning_rate"])
    operation = str(data_from_json["operation"])
    epochs_amount = int(data_from_json["epochs"])
    training_array, expected_output = set_initial_data(operation)

    if(len(training_array) == 0 or len(expected_output) == 0):
        print("Invalid operation")
        return

    perceptron = StepPerceptron(learning_rate, epochs_amount)
    epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(training_array, expected_output)

    plot_graph(training_array, expected_output, final_weights)
    plot_errors(error_in_epochs)
    print("Error min: " + str(min(error_in_epochs)))
    print("Min weight: ", final_weights)


if __name__ == "__main__":
    main()