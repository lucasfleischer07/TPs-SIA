import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def calculate_energy(weights, states):
    energy = -0.5 * np.dot(states.T, np.dot(weights, states))
    return energy

def train_hopfield(query, initial_letters):
    # Estimating weights
    n, columns = initial_letters.shape
    k = np.zeros((n, columns))
    for i in range(len(initial_letters)):
        k[i, :] = initial_letters[i]

    weights = (1 / n) * (np.matmul(k.T, k))
    np.fill_diagonal(weights, 0)

    iterations = 0
    S = np.where(query >= 0, 1, -1)  # Cambiar -1 por 1 en la inicialización de S
    results = []
    energy_list = []
    results.append(S)


    while True:
        if iterations != 0:
            print("\nIteration: " + str(iterations) + "\n") 
            print_letter(S)
        prev_state = np.sign(np.dot(weights, S))
        prev_state = np.where(prev_state == 0, -1, prev_state)
        results.append(prev_state)
        energy = calculate_energy(weights, prev_state)
        energy_list.append(energy)

        if np.array_equal(prev_state, S) and iterations != 0:
            break

        S = prev_state
        iterations += 1

    return S, iterations, energy_list


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


# def mutate(letter, prob): #funciona como que 0.1 es menor que 0.9.
#     mutated_letter = np.copy(letter)
#     for i in range(mutated_letter.size):
#         if np.random.random() < prob:
#             mutated_letter[i] *= -1
#     return mutated_letter


def mutate_pattern(pattern, bytes_to_change):
    indexs = np.random.choice(len(pattern), bytes_to_change, replace=False)
    p = deepcopy(pattern)
    for i in indexs:
        p[i] = 1 if p[i] == -1 else -1

    return p


def energy_plot(energy_list):
    plt.plot(range(1, len(energy_list[:-1]) + 1), energy_list[:-1], 'o-', color='green')
    plt.ylabel('Energía')
    plt.xlabel('Iteraciones')
    plt.title('Función de energía')
    plt.show()