import numpy as np
from copy import deepcopy


def train_hopfield(query, initial_letters): #le pasa la letra q quiere llegar, y las 4 letras de input
        # Estimating weights
        n, columns = initial_letters.shape #devuelve filas y columnas de inputs
        k = np.zeros((n, columns))
        for i in range(len(initial_letters)): #crea una matriz con las letras iniciales en las filas
            k[i, :] = initial_letters[i]
        
        weights = (1 / n) * (np.matmul(k.T, k))
        np.fill_diagonal(weights, 0)

        iterations = 0
        S = query #patron de consulta, S es el vector de estados
        old_S = None

        while not np.array_equal(S, old_S):
            if(iterations != 0):
                print("\nIteration: " + str(iterations) + "\n") 
                print_letter(S)
            old_S = S
            S = np.sign(np.dot(weights, S)) 
            iterations += 1 #iteraciones

        return S, iterations


def print_letter(letter):
    edited = []
    if letter is False:
        return False
    for i in range(len(letter)):
        if letter[i] == -1:
            edited.append(" ")
        else:
            edited.append("*")
    for i in range(5):
        print(edited[i*5], edited[(i*5)+1], edited[(i*5)+2], edited[(i*5)+3], edited[(i*5)+4])


def mutate(letter, prob): #funciona como que 0.1 es menor que 0.9.
    mutated_letter = np.copy(letter)
    for i in range(mutated_letter.size):
        if np.random.random() < prob:
            mutated_letter[i] *= -1
    return mutated_letter


def mutate_pattern(pattern, bytes_to_change):
    indexs = np.random.choice(len(pattern), bytes_to_change, replace=False)
    p = deepcopy(pattern)
    for i in indexs:
        p[i] = 1 if p[i] == -1 else -1

    return p