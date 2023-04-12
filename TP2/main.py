import csv
from src.generic_algorithm import generate_population, calculate_fitness, roulette_selection, uniform_crossover, mutation

if __name__ == "__main__":
    # Leer colores de archivo csv
    with open('colors.csv', 'r') as file:
        reader = csv.reader(file)
        palette = [list(map(int, row)) for row in reader]
        
    palette_size = len(palette)
    print(palette)

    # Obtener parámetros de input
    target_color = list(map(int, input("Ingrese el color objetivo (R,G,B): ").split(",")))
    population_size = int(input("Ingrese el tamaño de la población: "))
    mutation_probability = float(input("Ingrese la probabilidad de mutación (entre 0 y 1): "))
    max_generations = int(input("Ingrese el número máximo de generaciones: "))
    
    # Generar población inicial
    population = generate_population(population_size, palette_size)

    # Ejecutar algoritmo genético
    generation = 0
    while generation < max_generations:
        
        fitness_values = [calculate_fitness(chromosome, palette, target_color) for chromosome in population]
        

        # Seleccionar padres por ruleta
        parent1 = roulette_selection(population, fitness_values)
        parent2 = roulette_selection(population, fitness_values)

        # Realizar cruzamiento
        child = uniform_crossover(parent1, parent2)

        # Realizar mutación
        mutated_child = mutation(child, palette_size, mutation_probability)

        # Reemplazar peor cromosoma en población con el hijo mutado
        worst_index = fitness_values.index(max(fitness_values))
        population[worst_index] = mutated_child

        generation += 1

    # Obtener mejor cromosoma y su aptitud
    fitness_values = [calculate_fitness(chromosome,palette, target_color) for chromosome in population]
    best_index = fitness_values.index(min(fitness_values))
    best_chromosome = population[best_index]
    best_fitness = fitness_values[best_index]

    # Imprimir resultado
    print("El mejor cromosoma encontrado es:", best_chromosome)
    print("Su aptitud es:", best_fitness)



# import csv
# from src.generic_algorithm import genetic_algorithm

# if __name__ == "__main__":
#     # Leer colores de archivo csv
#     with open('colors.csv', 'r') as file:
#         reader = csv.reader(file)
#         palette = [list(map(int, row)) for row in reader]

#     palette_size = len(palette)
#     print(palette)

#     # Obtener parámetros de input
#     target_color = list(map(int, input("Ingrese el color objetivo (R,G,B): ").split(",")))
#     population_size = int(input("Ingrese el tamaño de la población: "))
#     mutation_probability = float(input("Ingrese la probabilidad de mutación (entre 0 y 1): "))
#     max_generations = int(input("Ingrese el número máximo de generaciones: "))

#     # Ejecutar algoritmo genético
#     best_chromosome, best_fitness = genetic_algorithm(palette, target_color, population_size, mutation_probability, max_generations)

#     # Imprimir resultado
#     print("El mejor cromosoma encontrado es:", best_chromosome)
#     print("Su aptitud es:", best_fitness)
