import json
import numpy as np
import sys
import matplotlib.pyplot as plt
import random

from src.each_color import EachColor
from src.generic_algorithm import genetic_algorithm


def read_file():
    f = open('./config.json')
    return json.load(f)
     

def set_data_from_file(conf_file):
    return conf_file['colors_palette'], conf_file['selection_algorithm'], conf_file['mutation_rate'], conf_file['max_generations'], conf_file['expected_fitness'], conf_file['population_number'], conf_file['fitness_cut']


if __name__ == "__main__":
    colors_from_palette = []
    target_color : EachColor

    conf_file = read_file()
    colors_palette, selection_algorithm, mutation_rate, max_generations, expected_fitness, population_number, fitness_cut = set_data_from_file(conf_file)
    if not fitness_cut:
        expected_fitness = 1.1


    with open(colors_palette, 'r') as file:
        first_line_is_target_color = file.readline()
        
        red, green, blue = first_line_is_target_color.split()
        target_color = EachColor(int(red), int(green), int(blue))

        n = population_number
        random_lines = random.sample(file.readlines(), n)        

        for line in random_lines :
            red, green, blue = line.split()
            current_color = EachColor(int(red), int(green), int(blue))
            colors_from_palette.append(current_color)
    file.close()


    result, generation_fitnesses, populations = genetic_algorithm(colors_from_palette, target_color, selection_algorithm, mutation_rate, max_generations, expected_fitness, population_number)

    print("El color que se obtuvo como resultado es (R G B): " + str(result))
    print("El fitness obtenido fue de: " + str(round(result.get_fitness(target_color), 4)))
    print("Numero de poblacion: " + str(population_number))

    complemento_encontrado = (1 - result.red/255, 1 - result.green/255, 1 - result.blue/255)
    complemento_objetivo = (1 - target_color.red/255, 1 - target_color.green/255, 1 - target_color.blue/255)

    plt.imshow([[(result.red / 255, result.green / 255, result.blue / 255)],
                [(target_color.red / 255, target_color.green / 255, target_color.blue / 255)]])
    plt.text(0, 0, 'Color Encontrado', color=complemento_encontrado, ha='center', va='center')
    plt.text(0, 1, 'Color Objetivo', color=complemento_objetivo, ha='center', va='center')
    plt.show()