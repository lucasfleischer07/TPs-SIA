import random
import math

# Función para generar un cromosoma aleatorio
def generate_chromosome(palette_size):
    return [random.randint(0, palette_size-1) for i in range(palette_size)]


# Función para calcular la aptitud de un cromosoma
def calculate_fitness(chromosome, palette, target_color):
    r, g, b = 0, 0, 0
    for chromosome_index in chromosome:
        r += palette[chromosome_index][0]
        g += palette[chromosome_index][1]
        b += palette[chromosome_index][2]
    r /= len(chromosome)
    g /= len(chromosome)
    b /= len(chromosome)
    return math.sqrt((target_color[0]-r)**2 + (target_color[1]-g)**2 + (target_color[2]-b)**2)



# Función para realizar la selección de padres por ruleta
def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probabilities = [fitness/total_fitness for fitness in fitness_values]
    selected_index = random.choices(range(len(population)), weights=selection_probabilities, k=1)[0]
    return population[selected_index]


# Función para realizar la cruza uniforme de dos padres
def uniform_crossover(parent1, parent2):
    child = [None] * len(parent1)
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child[i] = parent1[i]
        else:
            child[i] = parent2[i]
    return child


# Función para realizar la mutación de un cromosoma
def mutation(chromosome, palette_size, mutation_probability):
    for i in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[i] = random.randint(0, palette_size-1)
    return chromosome


# Función para generar la población inicial
def generate_population(population_size, palette_size):
    population = [generate_chromosome(palette_size) for i in range(population_size)]
    return population


# import random
# import math
# import numpy as np

# def generate_chromosome(palette_size):
#     return [random.randint(0, palette_size-1) for i in range(palette_size)]

# def calculate_fitness(chromosome, palette, target_color):
#     # Se calculan todas las componentes R, G, B a la vez en una sola iteración
#     r, g, b = 0, 0, 0
#     for index in chromosome:
#         r += palette[index][0]
#         g += palette[index][1]
#         b += palette[index][2]
#     r /= len(chromosome)
#     g /= len(chromosome)
#     b /= len(chromosome)
#     return math.sqrt((target_color[0]-r)**2 + (target_color[1]-g)**2 + (target_color[2]-b)**2)

# def roulette_selection(population, fitness_values):
#     # Se utiliza la función de numpy para normalizar la lista de aptitudes
#     selection_probabilities = np.array(fitness_values) / np.sum(fitness_values)
#     selected_index = np.random.choice(range(len(population)), p=selection_probabilities)
#     return population[selected_index]

# def uniform_crossover(parent1, parent2):
#     # Se utiliza la función de numpy para hacer el muestreo aleatorio de los bits
#     mask = np.random.randint(0, 2, len(parent1), dtype=bool)
#     child = parent1.copy()
#     child[mask] = parent2[mask]
#     return child

# def mutation(chromosome, palette_size, mutation_probability):
#     # Se utiliza la función de numpy para hacer el muestreo aleatorio de los bits
#     mask = np.random.random(size=len(chromosome)) < mutation_probability
#     chromosome[mask] = np.random.randint(0, palette_size, size=np.sum(mask))
#     return chromosome

# def generate_population(population_size, palette_size):
#     # Se utiliza la función de numpy para generar toda la población de una vez
#     return np.random.randint(0, palette_size, size=(population_size, palette_size))


# def genetic_algorithm(palette, target_color, population_size=100, num_generations=100, mutation_probability=0.01):
#     palette_size = len(palette)
#     population = generate_population(population_size, palette_size)
#     fitness_values = [calculate_fitness(chromosome, palette, target_color) for chromosome in population]

#     for i in range(num_generations):
#         new_population = []

#         while len(new_population) < population_size:
#             parent1 = roulette_selection(population, fitness_values)
#             parent2 = roulette_selection(population, fitness_values)
#             child = uniform_crossover(parent1, parent2)
#             child = mutation(child, palette_size, mutation_probability)
#             new_population.append(child)

#         population = new_population
#         fitness_values = [calculate_fitness(chromosome, palette, target_color) for chromosome in population]

#         best_fitness = min(fitness_values)
#         best_index = fitness_values.index(best_fitness)
#         best_chromosome = population[best_index]

#         if i % 10 == 0:
#             print(f"Generation {i}: Best fitness = {best_fitness:.3f}, Best chromosome = {best_chromosome}")
    
#     return best_chromosome

