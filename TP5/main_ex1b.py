import numpy as np
from numpy import mean, sum as npsum

from src.utils import hexa_to_bin_array, mutate_pattern
from src.include.font import font
from src.algorithms.Autoencoder import Autoencoder
from src.JsonConfig import JsonConfig


def __main__():
    f = open('config.json')
    config = JsonConfig(f.read())
    f.close()

    data = []
    letters_patterns = []
    letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']
    num_bytes_to_change = 10

    for letter in font:
        aux = hexa_to_bin_array(letter)
        data.append(np.concatenate(aux))  # Data es un array que dentro contiene otros arrays de longitud 35 (7x5), no es una matriz, es un vector de vectores
        letters_patterns.append(aux)

    # Hago un diccionario con clave valor para la letra que me dan, el vector que le voy a asignar
    letters_dict = dict(zip(letters, letters_patterns))

    autoencoder = Autoencoder(config, config.layers, len(data[0]))


    letters_patterns_mutated_to_train = []
    data_to_train = []
    for i in range(0, 2):
        letters_patterns_mutated_to_train.extend(mutate_pattern(data, num_bytes_to_change))
        data_to_train.extend(data)
    autoencoder.train(letters_patterns_mutated_to_train, data_to_train)

    # ! Si anda mal esto, descomentar el for de arriba y probar de 0 a 5 o sino de 0 a 10
    # letters_patterns_mutated_to_train = mutate_pattern(data, num_bytes_to_change)
    # data_to_train = data
    # autoencoder.train(mutate_pattern(data, num_bytes_to_change), data)

    patterns = []
    for i in range(len(data)):
        patterns.append(autoencoder.complete_get_output(data[i])) 
    patterns = np.array(patterns)
    error = mean((npsum((data - patterns) ** 2, axis=1) / 2))
    print("Train error with original patterns: " + str(error))

    patterns_trained = []
    for i in range(len(data)):
        patterns_trained.append(autoencoder.complete_get_output(letters_patterns_mutated_to_train[i]))
    patterns_trained = np.array(patterns_trained)
    error = mean((npsum((data - patterns_trained) ** 2, axis=1) / 2))
    print("Train error with mutated trained patterns: " + str(error))

    # generate a new set
    letters_patterns_mutated = mutate_pattern(data, num_bytes_to_change)

    patterns_new_set = []
    for i in range(len(data)):
        patterns_new_set.append(autoencoder.complete_get_output(letters_patterns_mutated[i])) 
    patterns_new_set = np.array(patterns_new_set)
    error = mean((npsum((data - patterns_new_set) ** 2, axis=1) / 2))
    print("Train error with new mutated patterns: " + str(error))

    


if __name__ == "__main__":
    __main__()