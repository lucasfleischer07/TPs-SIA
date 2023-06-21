import numpy as np
from numpy import mean, sum as npsum
import json
from src.utils import hexa_to_bin_array, mutate_pattern
from src.include.font import font
from src.algorithms.Autoencoder_VAE import Autoencoder_VAE
from src.JsonConfig import JsonConfig


    

def __main__():
    with open('config2.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    iterations = int(data_from_json["max_iter"])

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

    VAE = Autoencoder_VAE(len(data[0]),iterations)

    VAE.train(data)

    # ! Si anda mal esto, descomentar el for de arriba y probar de 0 a 5 o sino de 0 a 10
    # letters_patterns_mutated_to_train = mutate_pattern(data, num_bytes_to_change)
    # data_to_train = data
    # autoencoder.train(mutate_pattern(data, num_bytes_to_change), data)
    latent_random_values = np.random.normal(size=(10, 2))

    patterns = []
    for i in range(len(latent_random_values)):
        patterns.append(VAE.generate_samples(latent_random_values[i])) 
    
    print(str(patterns))

    


if __name__ == "__main__":
    __main__()