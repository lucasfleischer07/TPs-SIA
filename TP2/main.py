import csv
import copy
import random
import numpy as np
from src.generic_algorithm import generate_population, calculate_fitness, roulette_selection, uniform_crossover, mutation,elite_selection,rank_selection,probabilistic_tournament_selection,generate_couples
from src.chromosome_to_rgb import chromosome_to_rgb


if __name__ == "__main__":

    # Leer colores de archivo csv
    with open('colors.csv', 'r') as file:
        reader = csv.reader(file)
        palette = [list(map(int, row)) for row in reader]
        
    palette_size = len(palette)

    # Obtengo el color objetivo
    TARGET_COLOR = list(map(int, input("Ingrese el color objetivo (R,G,B): ").split(",")))
    while len(TARGET_COLOR) != 3 or all(color > 255 or color < 0 for color in TARGET_COLOR):
        TARGET_COLOR = list(map(int, input("Por favor ingrese 3 numero separados por "," para el color objetivo y que los valores no sean menores a 0 ni mayores a 255 (R,G,B): ").split(",")))

    # Obtengo el tamaño de la poblacion
    POPULATION_SIZE = int(input("Ingrese el tamaño de la población: "))
    while POPULATION_SIZE < 0:
        POPULATION_SIZE = int(input("Por favor ingrese un numeor positivo para el tamaño de la población: "))
    
    # Obtengo la porbabilidad de mutacion
    MUTATION_PROBABILITY = float(input("Ingrese la probabilidad de mutación (entre 0 y 1): "))
    while (MUTATION_PROBABILITY > 1.0 or MUTATION_PROBABILITY < 0.0):
        MUTATION_PROBABILITY = float(input("Por favor, ingrese la probabilidad de mutación (entre 0 y 1): "))

    # Obtengo el número máximo de generaciones
    MAX_GENERATIONS = int(input("Ingrese el número máximo de generaciones: "))
    while MAX_GENERATIONS < 0:
        MAX_GENERATIONS = int(input("Por favor ingrese un numeor positivo para el máximo de generaciones: "))

    # Obtengo el algoritmo de seleccion
    GENERIC_ALGORITHM = int(input("Seleccione que algoritmo de seleccion que quieres que te lo resuelva\n\t1. Roulette.\n\t2. Elite.\n\t3. Probabilistic Tournament.\n\t4. Rank.\n"))
    while GENERIC_ALGORITHM != 1 and GENERIC_ALGORITHM != 2 and GENERIC_ALGORITHM != 3 and GENERIC_ALGORITHM != 4:
            GENERIC_ALGORITHM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero del 1 al 4: "))
    
    # Generar población inicial
    population = generate_population(POPULATION_SIZE, palette_size)


    # Ejecutar algoritmo genético
    generation = 0
    while generation < MAX_GENERATIONS:
        
        fitness_values = np.array([calculate_fitness(chromosome, palette, TARGET_COLOR) for chromosome in population])
        
        parents = roulette_selection(copy.deepcopy(population),fitness_values)
        result = generate_couples(parents)
        couples = result[0]
        childs = []
        
        for couple in couples:
            childs.append(uniform_crossover(couple[0],couple[1]))    

        # Realizar mutación
        for child in childs:
            child = mutation(child, palette_size, MUTATION_PROBABILITY)

        # Reemplazar peor cromosoma en población con el hijo mutado
        newPopultaion=childs
        if(len(newPopultaion)<len(population)):
            random_numbers = random.sample(range(0, len(population)), len(population)-len(newPopultaion))
            for number in random_numbers:
                newPopultaion.append(population[number])
        population=np.array(newPopultaion)
        print(population)

        generation += 1

    # Obtener mejor cromosoma y su aptitud
    fitness_values = [calculate_fitness(chromosome,palette, TARGET_COLOR) for chromosome in population]
    best_index = fitness_values.index(min(fitness_values))
    best_chromosome = population[best_index]
    best_fitness = fitness_values[best_index]

    # Obtengo el color RGB del cromosoma
    best_rgb_color = chromosome_to_rgb(best_chromosome, 'colors.csv')

    # Imprimir resultado
    print("El mejor cromosoma encontrado es:", best_chromosome)
    print("El mejor color encontrado es: ", best_rgb_color)
    print("Su aptitud es:", best_fitness)
