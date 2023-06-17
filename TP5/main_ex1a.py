import numpy as np
from numpy import mean, sum as npsum

from src.utils import hexa_to_bin_array
from src.include.font import font
from src.JsonConfig import JsonConfig
from src.algorithms.Autoencoder import Autoencoder



def __main__():
    f = open('config.json')
    config = JsonConfig(f.read())
    f.close()

    data = []
    letters_patterns = []
    # letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']
    letters = ['@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']','^','_']
    for letter in font:
        aux = hexa_to_bin_array(letter)
        data.append(np.concatenate(aux))
        letters_patterns.append(aux)

    # Hago un diccionario con clave valor para la letra que me dan, el vector que le voy a asignar
    letters_dict = dict(zip(letters, letters_patterns))

    autoencoder = Autoencoder(config, config.layers, len(data[0]))
    #chequear xq ahora esta todo en un array (?)
    autoencoder.train(data, data)

    # -----------------  item b   -----------------------

    #Verificamos el error obtenido al evaluar las letras
    letter_recostructed = []
    for letter in data:
        letter_recostructed.append(autoencoder.complete_get_output(letter))

    letter_recostructed = np.array(letter_recostructed)
    error_trained = np.mean(npsum((data - letter_recostructed) ** 2, axis=1) / 2)
    print("Train error: " + str(error_trained))

    #---------------- item c ----------------------------

    # x = y = []
    
    



if __name__ == "__main__":
    __main__()