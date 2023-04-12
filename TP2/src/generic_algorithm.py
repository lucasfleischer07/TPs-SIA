import random
import math
import numpy as np
import pdb


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
    return distance

# Función para realizar la selección de padres por ruleta pero devuelve solo 1 individuo
# def roulette_selection(population, fitness_values):
#     total_fitness = sum(fitness_values)
#     selection_probabilities = np.array([fitness/total_fitness for fitness in fitness_values])
#     selected_index = random.choices(range(len(population)), weights=selection_probabilities, k=1)[0]
#     return population[selected_index]


# Función para realizar la selección de padres por ruleta
def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probabilities = np.array([fitness/total_fitness for fitness in fitness_values])
    selected_indices = random.choices(range(len(population)), weights=selection_probabilities, k=len(population)//2)
    selected_population = [population[i] for i in selected_indices]
    return selected_population


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
            
    
# Asigno un rango dependiendo del fitness value de cada individuo, y a partir de ese rango calculo la probabilidad de seleccion (es una alternativa a ruleta)
def rank_selection(population, fitness_values):

    n = len(population)
    # Ordeno dependiendo del fitness value a la population de mayor a menor
    sorted_pairs = sorted(zip(fitness_values, population), reverse=True)
    # sorted_fitness=[pair[0] for pair in sorted_pairs]
    sorted_population = [pair[1] for pair in sorted_pairs]
   
    ranks = np.array([n - i for i in range(n)])

    # Divido cada valor sobre la suma total
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
    # Permutar aleatoriamente los índices del array
    null_element = None
    permutation = random.sample(range(len(array)), len(array))
    random.shuffle(permutation)

    # Verificar si la longitud del array es impar
    if len(array) % 2 != 0:
        null_element = array[-1]
        array = array[:-1]

    # Dividir el array permutado en parejas consecutivas de elementos
    pairs = []
    for i in range(0, len(pairs), 2):
        if i+1 < len(array):
            pair = (array[permutation[i]], array[permutation[i+1]])
            pairs.append(pair)

    # Devolver las parejas y el elemento nulo
    return pairs, null_element






# def generate_couples(array):
#     # Permutar aleatoriamente los índices del array
#     null_element=None
#     permutation = np.random.permutation(array.shape[0])
#     #if len(array) % 2 != 0:
#     #    null_element=array[permutation[len(array)-1]]
#     #    array=np.delete(array,array[permutation[len(array)-1]])
#     #    permutation=np.delete(permutation,permutation[len(array)-1])
#     #    print(null_element)
                
#     # Dividir el array permutado en parejas consecutivas de elementos
#     pairs = np.array(list(zip(array[permutation[::2]], array[permutation[1::2]])))
    
    
#     # Devolver las parejas y el elemento nulo
#     return pairs, np.array(null_element)

