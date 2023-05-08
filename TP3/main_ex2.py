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
    with open('Exercise2/docs/TP3-ej2-conjunto.csv', 'r') as csv_file:
        plots = csv.reader(csv_file, delimiter=',')
        next(plots)   # Para skipear la linea de x1,x2,x3 e y

        data = []
        expected_output = []

        for row in plots:
            data.append([float(row[0]), float(row[1]), float(row[2])])
            expected_output.append(float(row[3]))
        
            # Para el de pruebas
            # data.append([float(row[0])])
            # expected_output.append(float(row[1]))

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


# def main(): 
#     data, expected_output = read_and_load_csv_data()

#     learning_rate = 0.00001
#     perceptron = "NO_LINEAL"
#     epochs_amount = 70000
#     beta = 0.8
#     min_error = 0.02
#     test_size1= 27
#     test_size2= 23
#     test_size3= 15

#     expected_output1 = escalate(expected_output)
#     expected_output2 = escalate(expected_output)
#     expected_output3 = escalate(expected_output)

#     perceptron1 = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output1), (expected_output1))
#     epochs_taken1, final_weights1, error_in_epochs1, final_error1 = perceptron1.train(data[:test_size1], expected_output1[:test_size1])
#     accuracy1 = get_accuracy_non_lineal(expected_output1[test_size1:], perceptron1.evaluate(data[test_size1:],expected_output1[test_size1:],final_weights1))

#     perceptron2 = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output2), (expected_output2))
#     epochs_taken2, final_weights2, error_in_epochs2, final_error2 = perceptron2.train(data[:test_size2], expected_output2[:test_size2])
#     accuracy2 = get_accuracy_non_lineal(expected_output2[test_size2:], perceptron2.evaluate(data[test_size2:],expected_output2[test_size2:],final_weights2))

#     perceptron3 = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output3), (expected_output3))
#     epochs_taken3, final_weights3, error_in_epochs3, final_error3 = perceptron3.train(data[:test_size3], expected_output3[:test_size3])
#     accuracy = get_accuracy_non_lineal(expected_output3[test_size3:], perceptron3.evaluate(data[test_size3:],expected_output3[test_size3:],final_weights3))
    
#     errors = [(error_in_epochs1, 'TrainingSize='+str(test_size1)), (error_in_epochs2, 'TrainingSize='+str(test_size2)), (error_in_epochs3, 'TrainingSize='+str(test_size3))]
    
#     plot_errors(errors,"Non Linear Perceptron")

# def main(): 
#     data, expected_output = read_and_load_csv_data()

#     learning_rate1 = 0.01
#     learning_rate2 = 0.001
#     learning_rate3 = 0.0001
#     learning_rate4 = 0.00001
#     perceptron = "NO_LINEAL"
#     epochs_amount = 70000
#     beta = 0.8
#     min_error = 0.02
#     test_size= 15

#     expected_output1 = escalate(expected_output)
#     expected_output2 = escalate(expected_output)
#     expected_output3 = escalate(expected_output)
#     expected_output4 = escalate(expected_output)

#     perceptron1 = NoLinearPerceptron(learning_rate1, epochs_amount, beta, min_error, (expected_output1), (expected_output1))
#     epochs_taken1, final_weights1, error_in_epochs1, final_error1 = perceptron1.train(data[:test_size], expected_output1[:test_size])
#     accuracy1 = get_accuracy_non_lineal(expected_output1[test_size:], perceptron1.evaluate(data[test_size:],expected_output1[test_size:],final_weights1))

#     perceptron2 = NoLinearPerceptron(learning_rate2, epochs_amount, beta, min_error, (expected_output2), (expected_output2))
#     epochs_taken2, final_weights2, error_in_epochs2, final_error2 = perceptron2.train(data[:test_size], expected_output2[:test_size])
#     accuracy2 = get_accuracy_non_lineal(expected_output2[test_size:], perceptron2.evaluate(data[test_size:],expected_output2[test_size:],final_weights2))

#     perceptron3 = NoLinearPerceptron(learning_rate3, epochs_amount, beta, min_error, (expected_output3), (expected_output3))
#     epochs_taken3, final_weights3, error_in_epochs3, final_error3 = perceptron3.train(data[:test_size], expected_output3[:test_size])
#     accuracy3 = get_accuracy_non_lineal(expected_output3[test_size:], perceptron3.evaluate(data[test_size:],expected_output3[test_size:],final_weights3))

#     perceptron4 = NoLinearPerceptron(learning_rate4, epochs_amount, beta, min_error, (expected_output4), (expected_output4))
#     epochs_taken4, final_weights4, error_in_epochs4, final_error4 = perceptron4.train(data[:test_size], expected_output4[:test_size])
#     accuracy4 = get_accuracy_non_lineal(expected_output4[test_size:], perceptron4.evaluate(data[test_size:],expected_output4[test_size:],final_weights4))
    
#     errors = [(error_in_epochs1, 'LearningRate='+str(learning_rate1)), (error_in_epochs2, 'LearningRate='+str(learning_rate2)), (error_in_epochs3, 'LearningRate='+str(learning_rate3)), (error_in_epochs4, 'LearningRate='+str(learning_rate4))]
    
#     plot_errors(errors,"Non Linear Perceptron")

def main(): 
    data, expected_output = read_and_load_csv_data()

    learning_rate = 0.01
    perceptron = "NO_LINEAL"
    epochs_amount = 20000
    beta1 = 0.2
    beta2 = 0.4
    beta3 = 0.6
    beta4 = 0.8

    min_error = 0.02
    test_size= 15

    expected_output1 = escalate(expected_output)
    expected_output2 = escalate(expected_output)
    expected_output3 = escalate(expected_output)
    expected_output4 = escalate(expected_output)

    perceptron1 = NoLinearPerceptron(learning_rate, epochs_amount, beta1, min_error, (expected_output1), (expected_output1))
    epochs_taken1, final_weights1, error_in_epochs1, final_error1 = perceptron1.train(data[:test_size], expected_output1[:test_size])
    accuracy1 = get_accuracy_non_lineal(expected_output1[test_size:], perceptron1.evaluate(data[test_size:],expected_output1[test_size:],final_weights1))

    perceptron2 = NoLinearPerceptron(learning_rate, epochs_amount, beta2, min_error, (expected_output2), (expected_output2))
    epochs_taken2, final_weights2, error_in_epochs2, final_error2 = perceptron2.train(data[:test_size], expected_output2[:test_size])
    accuracy2 = get_accuracy_non_lineal(expected_output2[test_size:], perceptron2.evaluate(data[test_size:],expected_output2[test_size:],final_weights2))

    perceptron3 = NoLinearPerceptron(learning_rate, epochs_amount, beta3, min_error, (expected_output3), (expected_output3))
    epochs_taken3, final_weights3, error_in_epochs3, final_error3 = perceptron3.train(data[:test_size], expected_output3[:test_size])
    accuracy3 = get_accuracy_non_lineal(expected_output3[test_size:], perceptron3.evaluate(data[test_size:],expected_output3[test_size:],final_weights3))

    perceptron4 = NoLinearPerceptron(learning_rate, epochs_amount, beta4, min_error, (expected_output4), (expected_output4))
    epochs_taken4, final_weights4, error_in_epochs4, final_error4 = perceptron4.train(data[:test_size], expected_output4[:test_size])
    accuracy4 = get_accuracy_non_lineal(expected_output4[test_size:], perceptron4.evaluate(data[test_size:],expected_output4[test_size:],final_weights4))
    
    errors = [(error_in_epochs1, 'Beta='+str(beta1)), (error_in_epochs2, 'Beta='+str(beta2)), (error_in_epochs3, 'Beta='+str(beta3)), (error_in_epochs4, 'Beta='+str(beta4))]
    
    plot_errors(errors,"Non Linear Perceptron")


# def main(): 
#     data, expected_output = read_and_load_csv_data()
#     learning_rate, perceptron, epochs_amount, beta, min_error, test_size = read_and_load_json_data()

#     if(perceptron == 'LINEAR'):
#         perceptron = LinearPerceptron(learning_rate, epochs_amount, min_error)
#         epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:test_size], expected_output[:test_size])
#         print("error in epochs " + str(error_in_epochs))
#         accuracy = get_accuracy(expected_output[test_size:], perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights))
#         print("Linear Accuracy: " + str(accuracy))
#         print("The evaluate results are: " + str(perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights)))
#         print("The expected results are: " + str(expected_output[test_size:]))
#         plot_errors(error_in_epochs, "Linear Perceptron")
#     elif(perceptron == 'NO_LINEAR'):
#         expected_output = escalate(expected_output)
#         perceptron = NoLinearPerceptron(learning_rate, epochs_amount, beta, min_error, (expected_output), (expected_output))
#         epochs_taken, final_weights, error_in_epochs, final_error = perceptron.train(data[:test_size], expected_output[:test_size])
#         print("error in epochs " + str(error_in_epochs))
#         accuracy = get_accuracy_non_lineal(expected_output[test_size:], perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights))
#         print("No linear Accuracy: " + str(accuracy))
#         print("The evaluate results are: " + str(perceptron.evaluate(data[test_size:],expected_output[test_size:],final_weights)))
#         print("The expected results are: " + str(expected_output[test_size:]))
#         plot_errors(error_in_epochs,"Non Linear Perceptron")
#     else:
#         print("Perceptron not found")
#         exit(1)


if __name__ == "__main__":
    main()