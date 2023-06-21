import numpy as np
from copy import deepcopy

def hexa_to_bin_array(hexa_character):
    bin_array = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        current_row = hexa_character[row]
        for col in range(0, 5):
            bin_array[row][4-col] = current_row & 1
            current_row >>= 1
    return bin_array


def add_noise(letters, num_of_bytes_to_change):
    letters = deepcopy(letters)
    for l in letters:
        indexs = np.random.choice(len(l), num_of_bytes_to_change, replace=False)
        r = np.random.uniform(low=-0.5, high=0.5, size=len(indexs))
        l[indexs] = (l[indexs].astype(float) + r).astype(int)
    return letters


def mutate_pattern(pattern, bytes_to_change):
    mutated_pattern = []
    for sub_pattern in pattern:
        indexs = np.random.choice(len(sub_pattern), bytes_to_change, replace=False)
        mutated_sub_pattern = deepcopy(sub_pattern)
        for i in indexs:
            mutated_sub_pattern[i] = 1 if mutated_sub_pattern[i] == 0 else 0
        mutated_pattern.append(mutated_sub_pattern)
    return mutated_pattern


def mutate_pattern2(patterns, bytes_to_change):
    patterns = deepcopy(patterns)
    for p in patterns:
        indexs = np.random.choice(len(p), bytes_to_change, replace=False)
        r = np.random.uniform(low=-0.5, high=0.5, size=len(indexs))
        p[indexs] += r
    return patterns

def resize_letter(x):
    return np.array(np.split(x, 7))

def adapt_pattern(pattern):
    for i in range(len(pattern)):
        if pattern[i] < 0:
            pattern[i] = 0
        else:
            pattern[i] = 1

def adapt_pattern2(pattern):
    adapted_pattern = np.where(pattern < 0, 0, 1)
    return adapted_pattern

def dividir_array(array):
    matriz = []
    for i in range(0, len(array), 5):
        matriz.append(array[i:i+5])
    return matriz

def generate_new_letter(letter1,letter2,letter3,letter4):
    new_letter = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        random_number = np.random.uniform(low=-0, high=1)
        for col in range(0, 5):
            if random_number < 0.25:
                new_letter[row][4-col] = letter1[row][4-col]
            elif random_number >= 0.25 and random_number < 0.5:
                new_letter[row][4-col] = letter2[row][4-col]
            elif random_number >= 0.5 and random_number < 0.75:
                new_letter[row][4-col] = letter3[row][4-col]
            else:
                new_letter[row][4-col] = letter4[row][4-col]
    return new_letter