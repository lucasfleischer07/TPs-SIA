import random
import math
import numpy as np

PROBABILISTIC_TOURNAMENT_VALUE = 0.75

# Función para generar un cromosoma aleatorio
def generate_chromosome(palette_size):
    return np.array([random.randint(0, palette_size-1) for i in range(palette_size)])


# Función para calcular la aptitud de un cromosoma (a major valor mejor aptitud)
def calculate_fitness(chromosome, palette, target_color):
    r, g, b = 0, 0, 0
    for chromosome_index in chromosome:
        r += palette[chromosome_index][0]
        g += palette[chromosome_index][1]
        b += palette[chromosome_index][2]
    r /= len(chromosome)
    g /= len(chromosome)
    b /= len(chromosome)
    distance = math.sqrt((target_color[0]-r)**2 + (target_color[1]-g)**2 + (target_color[2]-b)**2)
    return 1 / (1 + distance)


# Función para realizar la selección de padres por ruleta
def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probabilities = np.array([fitness/total_fitness for fitness in fitness_values])
    selected_index = random.choices(range(len(population)), weights=selection_probabilities, k=1)[0]
    return population[selected_index]


def elite_selection(population,fitness_values):
    fitness_values_list=fitness_values.tolist()
    population_list=population.tolist()
    
    sorted_pairs = sorted(zip(fitness_values_list, population_list), reverse=True)
    sorted_population = [pair[1] for pair in sorted_pairs]
    return np.array(sorted_population[0:math.ceil(len(population)/2)])


def probabilistic_tournament_selection(population,fitness_values):
    newPopulation=np.array([])
    while(population.size>0):
        if population.size==1:
            newPopulation.append(population[0])
            population=np.delete(population,0)
            fitness_values=np.delete(fitness_values,0)
        else:
            random_numbers = random.sample(range(0, population.size), 2)
            if(random.random()<PROBABILISTIC_TOURNAMENT_VALUE):
                if(fitness_values[random_numbers[0]] > fitness_values[random_numbers[1]]):
                    newPopulation.append[population[random_numbers[0]]]
                else: newPopulation.append[population[random_numbers[1]]]
            else: 
                if(fitness_values[random_numbers[0]] > fitness_values[random_numbers[1]]):
                    newPopulation.append[population[random_numbers[1]]]
                else: newPopulation.append[population[random_numbers[0]]]
            population=np.delete(population,max(random_numbers))
            fitness_values=np.delete(fitness_values,max(random_numbers))
            population=np.delete(population,min(random_numbers))
            fitness_values=np.delete(fitness_values,min(random_numbers))
    return population
            
    
#asigno un rango dependiendo del fitness value de cada individuo, y a partir de ese rango calculo la probabilidad de seleccion (es una alternativa a ruleta)
def rank_selection(population, fitness_values):

    n = len(population)
    #ordeno dependiendo del fitness value a la population de mayor a menor
    sorted_pairs = sorted(zip(fitness_values, population), reverse=True)
    # sorted_fitness=[pair[0] for pair in sorted_pairs]
    sorted_population = [pair[1] for pair in sorted_pairs]
   
    ranks = np.array([n - i for i in range(n)])

    #divido cada valor sobre la suma total
    selection_probs = ranks / np.sum(ranks)
    selected_individuals = np.random.choice(sorted_population, size=n//2, replace=True, p=selection_probs)
    return list(selected_individuals)
     

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
    population = np.array([generate_chromosome(palette_size) for i in range(population_size)])
    return population

def generate_couples(array):
    # permutar aleatoriamente los índices del array
    null_element=None
    permutation = np.random.permutation(array.shape[0])
    #if len(array) % 2 != 0:
    #    null_element=array[permutation[len(array)-1]]
    #    array=np.delete(array,array[permutation[len(array)-1]])
    #    permutation=np.delete(permutation,permutation[len(array)-1])
    #    print(null_element)
                
    # dividir el array permutado en parejas consecutivas de elementos
    pairs = np.array(list(zip(array[permutation[::2]], array[permutation[1::2]])))
    
    
    # devolver las parejas y el elemento nulo
    return pairs, np.array(null_element)


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

