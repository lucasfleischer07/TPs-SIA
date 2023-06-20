import numpy as np
from numpy import random, matmul, mean, sum as npsum
from scipy.optimize import minimize
from qiskit.algorithms.optimizers import ADAM
from scipy import optimize


LATENT_CODE_LENGTH = 2

class Autoencoder:

    FUNCTIONS = {
        "identity": {
            "f": lambda h: h,
            "fp": lambda h: 1
        },
        "logistic": {
            "f": lambda h, betha: 1 / (1 + np.exp(-2 * h * betha)),
            "fp": lambda h, betha: 2 * betha * (1 / (1 + np.exp(-2 * h * betha))) * (
                    1 - (1 / (1 + np.exp(-2 * h * betha))))
        },
        "tanh": {
            "f": lambda h, betha: np.tanh(h * betha),
            "fp": lambda h, betha: betha * (1 - (np.tanh(h * betha) ** 2))
        }
    }

    def __init__(self, config, layers_selected, input_length):
        self.layers = self.create_hidden_layers(input_length, layers_selected)
        self.config = config
        self.min_error = config.min_error
        self.learning_rate = config.learning_rate
        self.max_iter = config.max_iter
        self.iteration = 0
        self.dimentions = []
        self.weights = self.create_weights(self.layers)
        self.activate = self.FUNCTIONS[config.function]['f']
        self.activate_derivative = self.FUNCTIONS[config.function]['fp']
        self.function = config.function
        if self.function != 'identity':
            self.betha = config.betha
        

    #Creamos las layers, con la entrada, el encoder, el espacio latente, el decoder y la salida
    def create_hidden_layers(self,input_length, hidden_layers):
        layers = []
        layers.append(input_length)
        layers.extend(hidden_layers)
        layers.append(LATENT_CODE_LENGTH)
        # layers.extend(hidden_layers[::-1])
        layers.extend(list(reversed(hidden_layers)))
        layers.append(input_length)
        return layers

    #tiene como entrada los x de datos y salida el espacio latente
    def encode(self, input_x):
        encoding_weights = self.weights[:len(self.weights) // 2]  # Obtener los pesos hasta el espacio latente
        return self.get_output(input_x, encoding_weights)

    #tiene como entrada los x del espacio latente Z y salida el espacio x'
    def decode(self, data_x_in_latent_code):
        encoding_weights = self.weights[len(self.weights) // 2:]  # Obtener los pesos hasta el espacio latente
        return self.get_output(data_x_in_latent_code, encoding_weights)


    #usamos una funcion de optimizacion para ajustar los pesos y los sesgos de la red para minimizar el error entre las salidas predichas y las salidas deseadas
    def train(self, input_x, input_y):
        X = self.array_resize(self.weights)
        #data_trained = minimize(self.calculate_error, X, method='L-BFGS-B',
        #            args=(input_x, input_y),
        #            jac=None, bounds=None,tol=None,callback=self.print_step,
        #            options={'disp': False, 'gtol': self.config.min_error, 'maxiter': self.config.max_iter})
        data_trained = minimize(self.calculate_error, X, method='Powell',
                          args=(input_x, input_y),
                          jac=None, bounds=None,
                          tol=None,
                          callback=self.print_step,
                          options={'disp': True, 'xtol': self.config.min_error, 'maxiter': self.config.max_iter})
        self.assign_weights(data_trained.x)


    def print_step(self, x):
        print('Iteration: ' + str(self.iteration))
        self.iteration += 1

    #crea una matriz de pesos inicializada aleatoriamente para cada capa de una red neuronal. (en -1 a 1)
    def create_weights(self, layers):
        weights = []
        #recorre cada layer, pero evita la de salida
        for i in range(len(layers) - 1):
            self.dimentions.append((layers[i + 1], layers[i]))
            weights.append(np.random.uniform(low=-1, high=1, size=(layers[i + 1], layers[i])))

        return np.array(weights, dtype=object)

    # toma una lista de matrices de pesos y las concatena en un solo vector unidimensional.
    #uso flatten() de numpy para convertir cada matriz en un vector unidimensional. 
    def array_resize(self, weights):
        flattened_weights = [w.flatten() for w in weights]
        return np.concatenate(flattened_weights, axis=0)
        
 
    def assign_weights(self, weights):
        self.weights = np.array(self.weights_resize(weights), dtype=object) #me falta resizear los pesos
        
    def calculate_error(self, x, x_data, y_expected):
        weights = self.weights_resize(x)
        output = np.array([self.get_output(data, weights) for data in x_data])
        error = np.mean(np.sum((y_expected - output) ** 2, axis=1) / 2)
        #print('The error is: ' + str(error))
        return error

    def weights_resize(self, weights_array):
        weights = []
        start_idx = 0
        for dim in self.dimentions:
            flattened_dim = dim[0] * dim[1]
            end_idx = start_idx + flattened_dim
            weights.append(weights_array[start_idx:end_idx].reshape(dim))
            start_idx = end_idx
        return weights

    def get_output(self, input, weights):
        output_value = input.reshape((len(input), 1))
        for neuron_weight in weights:
            if self.function == "identity":
                output_value = self.activate(matmul(neuron_weight,output_value))
            else:
                output_value = self.activate(matmul(neuron_weight,output_value),self.betha)
        return output_value.flatten()

    #Makes the complete run through the Decoder with a input and returns output
    def complete_get_output(self, input):
        return self.get_output(input, self.weights)