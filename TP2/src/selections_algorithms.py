from src.each_color import EachColor
import numpy as np
import math

PROBABILISTIC_TOURNAMENT_VALUE = 0.75

def selection_method(population, target, selection_algorithm):
        match selection_algorithm: 
            case "elite":
                elite_selection(population, target)
            case "roulette":
                roulette_selection(population, target)
            case "rank":
                rank_selection(population, target)
            # case "probabilistic_tournament":
            #     probabilistic_tournament_selection(population, target)


def elite_selection(population, target):
    population.sort(key=lambda x: x.get_fitness(target), reverse=True)
    population = population[0:math.ceil(len(population)/2)]


def roulette_selection(population, target):
    max = sum(individual.get_fitness(target) for individual in population) 
    probabilities = [individual.get_fitness(target) / max for individual in population]
    np_array = np.random.choice(list(population), size=len(population)//2, replace=True, p=probabilities)
    population = np_array


def rank_selection(population, target):
    population_size = len(population)
    population.sort(key=lambda x: x.get_fitness(target), reverse=True)
    f_1 = [(population_size-i)/i for i in range(1, population_size+1)]
    sum_f_1 = sum(f_1)

    if sum_f_1 == 0:
        probabilities = [1.0]
    else:
        probabilities = [(f_1[i] / sum_f_1) for i in range(0, population_size)]

    np_array = np.random.choice(list(population), size=population_size//2, replace=False, p=probabilities)
    population = np_array


# TODO AJUSTAR
# def probabilistic_tournament_selection(population,fitness_values):
#     newPopulation=np.array([])
#     while(population.size>0):
#         if population.size==1:
#             newPopulation.append(population[0])
#             population=np.delete(population,0)
#             fitness_values=np.delete(fitness_values,0)
#         else:
#             random_numbers = random.sample(range(0, population.size), 2)
#             if(random.random()<PROBABILISTIC_TOURNAMENT_VALUE):
#                 if(fitness_values[random_numbers[0]] > fitness_values[random_numbers[1]]):
#                     newPopulation.append[population[random_numbers[0]]]
#                 else: newPopulation.append[population[random_numbers[1]]]
#             else: 
#                 if(fitness_values[random_numbers[0]] > fitness_values[random_numbers[1]]):
#                     newPopulation.append[population[random_numbers[1]]]
#                 else: newPopulation.append[population[random_numbers[0]]]
#             population=np.delete(population,max(random_numbers))
#             fitness_values=np.delete(fitness_values,max(random_numbers))
#             population=np.delete(population,min(random_numbers))
#             fitness_values=np.delete(fitness_values,min(random_numbers))
#     return population