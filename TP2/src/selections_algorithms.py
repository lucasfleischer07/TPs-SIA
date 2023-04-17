from src.each_color import EachColor
import numpy as np
import math
import copy
import random

PROBABILISTIC_TOURNAMENT_VALUE = 0.75

def selection_method(population, target, selection_algorithm):
    if selection_algorithm == "elite":
        elite_selection(population, target)
    elif selection_algorithm == "roulette":
        roulette_selection(population, target)
    elif selection_algorithm == "rank":
        rank_selection(population, target)
    elif selection_algorithm=="probabilistic_tournament":
         probabilistic_tournament_selection(population, target)


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


def probabilistic_tournament_selection(population,target):
    random.shuffle(population)
    n=len(population)
    newPopulation=[]
    if n % 2 == 1:
        population.append(copy.deepcopy(population[0]))
    for i in range(0, n, 2):
        if population[i].get_fitness(target) > population[i+1].get_fitness(target):
            best_color=population[i]
            worst_color=population[i+1]
        else:
            best_color=population[i+1]
            worst_color=population[i]
        if(random.random()<PROBABILISTIC_TOURNAMENT_VALUE):
            newPopulation.append(best_color)
        else:
            newPopulation.append(worst_color)
    population=newPopulation