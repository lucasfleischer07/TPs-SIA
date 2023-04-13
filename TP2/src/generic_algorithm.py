from audioop import reverse
from hashlib import new
from operator import ge, ne
from src.each_color import EachColor
from src.crossbreed import *
from src.selections_algorithms import selection_method
from src.mutation import *
import math
import random
import copy
import numpy

red_coordinates = []
green_coordinates = []
blue_coordinates = []

color_fit_coordinates = []
closest_color = EachColor(0, 0, 0)

def validation_fitness(expected_fitness):
    if (not expected_fitness == "default") and (0 <= expected_fitness <= 1):
        return expected_fitness
    return 0.95

# Se generan dos hijos por pareja, de ellos se toma uno random
# De la poblacion vieja se toma la mitad tambien
def genetic_algorithm(population, target, selection_algorithm, max_generations, expected_fitness):
    expected_fitness = validation_fitness(expected_fitness)
    closest_fit = 0
    
    gen = 0
    max : float
    
    while gen < (max_generations):
        new_pop = []

        # crossbreed
        n_iterations = math.floor(len(population) / 2)
        j=0
        for c in range(n_iterations):
            parent1 = population[j]
            parent2 = population[j+1]
            j = j+2
            first_child, sec_child = uniform_crossbreed(parent1, parent2)
            
            if numpy.random.uniform() > 0.5:
                new_pop.append(first_child)
            else:
                new_pop.append(sec_child)

        #de los hijos agregados a la nueva poblacion, mutamos los que tengan bajo fitness   
        i = 0
        while i < len(new_pop) :
            if new_pop[i].get_fitness(target) < 0.15:
                candidate =  copy.deepcopy(new_pop[i])
                if not in_population(new_pop, candidate.mutate()):
                    new_pop[i] = candidate
            i = i + 1

        # nos quedamos con los mejores de la vieja poblacion 
        # Mutamos de forma uniforme a la antigua generacion 
        uniform_mutation(new_pop, population, target)

        # De la antigua generacion nos quedamos con la mitad, los que estan en indice par por ejemplo
        # De esta forma tomamos mitad de la poblacion vieja y mitad de la nueva
        for c in range(n_iterations):
            new_pop.append(population[c * 2])

        
        selection_method(new_pop, target, selection_algorithm)

        max = new_pop[0]

        for individual in new_pop:
            if individual.get_fitness(target) > max.get_fitness(target):
                max = EachColor(individual.red, individual.green, individual.blue)

        if(max.get_fitness(target) >= expected_fitness):
            print("Encontrado en la generacion numero: " + str(gen))
            return max

        if(max.get_fitness(target) > closest_fit):
            closest_color = EachColor(max.red, max.green, max.blue)
            closest_fit = closest_color.get_fitness(target)
            print("ACTUALIZADO")
            print(gen)
            print(closest_color)
            print("fitness")
            print(closest_color.get_fitness(target))
            
    
        color_fit_coordinates.append(closest_color.get_fitness(target))

        if(not in_population(new_pop, closest_color)):
            new_pop.append(EachColor(closest_color.red, closest_color.green, closest_color.blue))

        print(closest_color.get_fitness(target))
        population = new_pop
        gen += 1
        

    print("No se pudo completar el algoritmo en " + str(gen) + " generaciones")
    return closest_color