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


