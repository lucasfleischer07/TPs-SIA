import numpy as np
from src.each_color import EachColor

# TODO: No esta testeado
def uniform_crossbreed(parent1, parent2):
    child1_components = []
    child2_components = []

    for component1, component2 in zip(parent1.components, parent2.components):
        binary1 = format(component1, '08b')
        binary2 = format(component2, '08b')

        child1_binary = ''
        child2_binary = ''

        for i in range(len(binary1)):
            if np.random.uniform() > 0.5:
                child1_binary += binary1[i]
                child2_binary += binary2[i]
            else:
                child1_binary += binary2[i]
                child2_binary += binary1[i]

        child1_components.append(int(child1_binary, 2))
        child2_components.append(int(child2_binary, 2))

    child1 = EachColor(child1_components[0], child1_components[1], child1_components[2])
    child2 = EachColor(child2_components[0], child2_components[1], child2_components[2])

    return child1, child2


# def crossbreed(one, two):

BITS_NUM = 8
getbinary = lambda x, n: format(x, 'b').zfill(n)

def uniform_crossbreed(parent1, parent2):
    child_red1, child_red2 = uniform_crossbreed_per_color(parent1.red, parent2.red)
    child_green1, child_green2 = uniform_crossbreed_per_color(parent1.green, parent2.green)
    child_blue1, child_blue2 = uniform_crossbreed_per_color(parent1.blue, parent2.blue)

    child1 = EachColor(child_red1, child_green1, child_blue1)
    child2 = EachColor(child_red2, child_green2, child_blue2)

    return child1, child2

def uniform_crossbreed_per_color(component1, component2):
    child_bin1 = getbinary(component1, 8)
    child_bin2 = getbinary(component2, 8)

    for i in range(8):
        if np.random.uniform() > 0.5:
            aux = child_bin1[i]
            child_bin1 = child_bin1[:i] + child_bin2[i] + child_bin1[i + 1:]
            child_bin2 = child_bin2[:i] + aux + child_bin2[i + 1:]

    return int(child_bin1, 2), int(child_bin2, 2)

