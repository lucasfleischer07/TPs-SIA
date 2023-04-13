from src.each_color import EachColor
import numpy as np

#TODO IAN SEGUIR HAY PARAMETROS Q NO USAMOS

def mutate(color):
    return np.random.randint(0,255)

def in_population(pop, candidate):
    for individual in pop:
        if individual.equals(candidate):
            return True
    return False


def uniform_mutation(new_population, population, target):
    old_color : EachColor
    for individual in population:
        if np.random.uniform() < 0.5:
            individual.mutate()
            