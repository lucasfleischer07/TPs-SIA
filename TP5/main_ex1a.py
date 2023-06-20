from src.plots import plot_one_letter_patterns
from src.utils import adapt_pattern
import numpy as np
from numpy import mean, sum as npsum
import matplotlib.pyplot as plt

from src.plots import plot_points_latent_space
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
    letters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL']
    for letter in font:
        aux = hexa_to_bin_array(letter)
        data.append(np.concatenate(aux))
        letters_patterns.append(aux)

    # Hago un diccionario con clave valor para la letra que me dan, el vector que le voy a asignar
    letters_dict = dict(zip(letters, letters_patterns))

    autoencoder = Autoencoder(config, config.layers, len(data[0]))
    #chequear xq ahora esta todo en un array (?)
    autoencoder.train(data, data)



    # ----------------- item a    -----------------------

    # Datos
    valores_x = ['25x20x15x10x2x10x15x20x25', '35x10x5x2x5x10x35', '35x10x2x10x35']
    valores_y = [0.3426486939323965, 1.2562263415389, 1.546197772768]

    colors = ['green', 'red', 'red']
    # Crear el gráfico de barras
    plt.bar(valores_x, valores_y, color = colors)

    # Personalizar el gráfico
    plt.title('Evaluacion de error para distintas arquitecturas')
    plt.xlabel('Arquitecturas')
    plt.ylabel('Error obtenido')

    # Mostrar el gráfico
    plt.show()


    # -----------------  item b   -----------------------

    #Verificamos el error obtenido al evaluar las letras
    letter_recostructed = []
    for letter in data:
        letter_recostructed.append(autoencoder.complete_get_output(letter))

    letter_recostructed = np.array(letter_recostructed)
    error_trained = np.mean(npsum((data - letter_recostructed) ** 2, axis=1) / 2)
    print("Train error: " + str(error_trained))

    #---------------- item c, grafico en 2d----------------------------

    x = []
    y = []
    for key, value in letters_dict.items():
        res = autoencoder.encode(np.concatenate(value))
        x.append(res[0])
        y.append(res[1])
    plot_points_latent_space(x, y, list(letters_dict.keys()), title="Espacio Latente")
    

    #---------------- item d ----------------------------
    # Generate 5 new letters from trained Autoencoder
    for i in range(5):
        random_latent_vector = np.array([np.random.uniform(low=0, high=1), np.random.uniform(low=-1, high=1)])
        new_letter = autoencoder.decode( random_latent_vector)
        #print(str(new_letter))
        adapt_pattern(new_letter)
        #print(str(new_letter))
        plot_one_letter_patterns(new_letter.reshape(7, 5))



if __name__ == "__main__":
    __main__()