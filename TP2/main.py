import json
import numpy as np
import sys
import matplotlib.pyplot as plt
from color import EachColor

from genetic_algorithm import genetic_algorithm


def read_file():
    f = open('./config.json')
    return json.load(f)
     

def set_data_from_file(conf_file):
    return conf_file['color_palette'], conf_file['selection_algorithm'], conf_file['max_generations'], conf_file['expected_fitness']


if __name__ == "__main__":
    colors_from_palette = []
    target_color : EachColor

    conf_file = read_file()
    color_palette, selection_algorithm, max_generations, expected_fitness = set_data_from_file(conf_file)
    
    with open(color_palette, 'r') as file:
        first_line_is_target_color = file.readline()
        
        red, green, blue = first_line_is_target_color.split()
        target_color = EachColor(int(red), int(green), int(blue))

        for line in file:
            red, green, blue = line.split()
            current_color = EachColor(int(red), int(green), int(blue))
            colors_from_palette.append(current_color)
    file.close()


    result = genetic_algorithm(colors_from_palette, target_color, selection_algorithm, max_generations, expected_fitness)

    print("El color que se obtuvo como resultado es (R G B): " + str(result))
    print("El fitness obtenido fue de: " + str(round(result.get_fitness(target_color), 4)))

    # Grafica el color deseado y el color aproximado
    plt.imshow([[(result.red / 255, result.green / 255, result.blue / 255)],
                [(target_color.red / 255, target_color.green / 255, target_color.blue / 255)]])
    plt.show()