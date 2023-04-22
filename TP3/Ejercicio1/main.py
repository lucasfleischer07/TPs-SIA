import numpy as np
import json


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
    with open('./config.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    learning_rate = float(data_from_json["learning_rate"])
    generation = int(data_from_json["generation"])
    operation = str(data_from_json["operation"])

    training_array, expected_output = set_initial_data(operation)

    if(len(training_array) == 0 or len(expected_output) == 0):
        print("Invalid operation")
        return


    # weights = perceptron(input_data, expected_data, learning_rate, epochs)

    # print("weights: ", weights)
    # print("Accuracy perceptron:", accuracy(expected_data, weights))

if __name__ == "__main__":
    main()