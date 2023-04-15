from audioop import reverse
from hashlib import new
from operator import ge, ne
from src.each_color import EachColor
from src.crossbreed import uniform_crossbreed
from src.selections_algorithms import selection_method
from src.mutation import uniform_mutation
import math
import random
import copy
import numpy



limit_generation = 1000

def validation_fitness(expected_fitness):
    if (not expected_fitness == "default") and (0 <= expected_fitness <= 1):
        return expected_fitness
    return 0.95

# Se generan dos hijos por pareja, de ellos se toma uno random
# De la poblacion vieja se toma la mitad tambien
def genetic_algorithm(population, target, selection_algorithm, mutation_rate, max_generations, expected_fitness,population_size,fitness_cut):
    expected_fitness = validation_fitness(expected_fitness)
    closest_fit = 0
    generation_maxes = []
    gen = 0
    populations=[]
    while gen < (limit_generation):
        max=None
        populations.append(copy.deepcopy(population))
        parents = copy.deepcopy(population)
        selection_method(parents, target, selection_algorithm)
        n = len(parents)
        random.shuffle(parents)
        if n % 2 == 1:
            parents.append(copy.deepcopy(parents[0]))
        child_pop=[]
        for i in range(0, n, 2):
            child1,child2 = uniform_crossbreed(parents[i],parents[i+1])
            child_pop.append(child1)
            child_pop.append(child2)

        # nos quedamos con los mejores de la vieja poblacion 
        # Mutamos de forma uniforme a la antigua generacion 
        uniform_mutation(child_pop,mutation_rate)

        new_pop = []
        new_pop.extend(child_pop)
        
        i = 0
        while len(new_pop) < population_size and i < len(parents):
           new_pop.append(parents[i])

        max = new_pop[0]
        for individual in new_pop:
            if individual.get_fitness(target) > max.get_fitness(target):
                max = EachColor(individual.red, individual.green, individual.blue,mutation_rate)
        generation_maxes.append(max.get_fitness(target))

        if(fitness_cut and max.get_fitness(target) >= expected_fitness):
            print("Encontrado en la generacion numero: " + str(gen))
            return max,generation_maxes,populations


        
        population = new_pop
        gen += 1
        if not fitness_cut and gen >= max_generations:
            return max, generation_maxes, populations
        
    return max, generation_maxes, populations