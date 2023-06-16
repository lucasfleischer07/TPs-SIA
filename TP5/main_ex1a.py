import numpy as np


from src.utils import hexa_to_array
from src.include import font

def __main__():
    # TODO: HAcer lo de leer la configuracion y eso

    data = []
    letters_patterns = []
    letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']

    for letter in font:
        aux = hexa_to_array(letter)
        data.append(np.concatenate(aux))
        letters_patterns.append(aux)

    # Hago un diccionario con clave valor para la letra que me dan, el vector que le voy a asignar
    letters_dict = dict(zip(letters, letters_patterns))


    # TODO: Meter aca abajo el llamado del autoencoder y eso






if __name__ == "__main__":
    __main__()