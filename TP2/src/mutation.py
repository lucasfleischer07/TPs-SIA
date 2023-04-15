from src.each_color import EachColor
import numpy as np

#TODO IAN SEGUIR HAY PARAMETROS Q NO USAMOS


def in_population(pop, candidate):
    for individual in pop:
        if individual.equals(candidate):
            return True
    return False


def uniform_mutation(new_population, mutation_rate):
    for individual in new_population:
        individual: EachColor
        if np.random.uniform() < mutation_rate:
            individual.mutate()
            