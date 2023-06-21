import numpy as np
from numpy import mean, sum as npsum

from src.utils import hexa_to_bin_array, mutate_pattern, adapt_pattern2
from src.include.font import font
from src.algorithms.Autoencoder import Autoencoder
from src.JsonConfig import JsonConfig
from src.plots import plot_letters_patterns_with_noise, plot_letters_patterns, graph_multi_heatmap


def __main__():
    f = open('config.json')
    config = JsonConfig(f.read())
    f.close()

    data = []
    letters_patterns = []
    letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']
    num_bytes_to_change = 0

    for letter in font:
        aux = hexa_to_bin_array(letter)
        data.append(np.concatenate(aux))  # Data es un array que dentro contiene otros arrays de longitud 35 (7x5), no es una matriz, es un vector de vectores
        letters_patterns.append(aux)

    # Hago un diccionario con clave valor para la letra que me dan, el vector que le voy a asignar
    letters_dict = dict(zip(letters, letters_patterns))

    autoencoder = Autoencoder(config, config.layers, len(data[0]))


# ---------- aca muto la data con la que voy a entrenar --------
    letters_patterns_mutated_to_train = []
    data_to_train = []
    # for i in range(0, 1):
    letters_patterns_mutated_to_train.extend(mutate_pattern(data[:10], num_bytes_to_change))
    data_to_train.extend(data[:10])

# ----------------- entrno al autoencoder con la data que mute arriba --------
    plot_letters_patterns_with_noise(letters_patterns_mutated_to_train)
    plot_letters_patterns_with_noise(data_to_train)
    autoencoder.train(letters_patterns_mutated_to_train, data_to_train)


# ------------------ muto data nueva y se la paso al autoencoder ------------
    letters_patterns_mutated_to_train2 = []
    # for i in range(0, 1):
    letters_patterns_mutated_to_train2.extend(mutate_pattern(data[:10], num_bytes_to_change))
    data_to_train.extend(data[:10])

    plot_letters_patterns_with_noise(letters_patterns_mutated_to_train2)

# -------------- veo que me devuelve el autoencoder
    patterns = []
    for i in range(len(data[:10])):
        patterns.append(autoencoder.complete_get_output(letters_patterns_mutated_to_train2[i])) 
    # graph_multi_heatmap(patterns)
    # patterns = adapt_pattern2(np.array(patterns))
    print(patterns)
    # plot_letters_patterns_with_noise(patterns)
    error = mean((npsum((data[:10] - patterns) ** 2, axis=1) / 2))
    print("Train error with mutated trained patterns: " + str(error))


if __name__ == "__main__":
    __main__()