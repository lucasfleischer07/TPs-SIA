import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import math
from src.hopfield import train_hopfield, energy_plot, print_letter, mutate_pattern


def parse_file():
    file = open('docs/letters.txt', 'r')
    lines = file.readlines()

    letters = []

    for i in range(26):
        letter = []
        for j in range(5):
            current_line = list(map(lambda v: int(v), lines[j + i * 5].split()))
            for n in current_line:
                letter.append(n)
        letters.append(letter)

    letters = np.array(letters)
    letters = np.where(letters == 0, -1, letters)

    return letters


def main():
    alg_name = "hopfield"
    letters = parse_file() 
    print(len(letters))

    train_letters = np.array([letters[0], letters[5], letters[15], letters[17]]) #A,L,T,V.
    # train_letters = np.array([letters[5], letters[12], letters[21], letters[25]]) #A,L,T,V. fmvz y ajlx
    # train_letters = np.array([letters[0], letters[9], letters[11], letters[23]]) #A,L,T,V. fmvz y ajlx (mejor)

    print("\nInput letters: \n")
    for input in train_letters:
        print_letter(input)
        print()

    print("\n ------------------------- \n")

    # letter_with_noise = mutate(letters[0], 0.1)

    noise = 6
    letter_with_noise = mutate_pattern(letters[0], noise)

    # predict_letter = letters[0]

    # print("Letter to predict with noise in iteration 0: \n")
    # print_letter(letter_with_noise)

    # print("Letter to predict: \n")
    # print_letter(predict_letter)
    print("Letter to predict with noise: " + str(noise) + "\n")
    print_letter(letter_with_noise)
    
    #forma 1 sin energia q anda
    # letter_solved, iterations = train_hopfield(np.array(letter_with_noise), train_letters)
    # letter_solved, iterations = train_hopfield(predict_letter, train_letters)

    #forma 2 con energia
    result, iterations, energy_list = train_hopfield(np.array(letter_with_noise), train_letters)
    # result, iterations, energy_list = train_hopfield(predict_letter, train_letters)

    
 
    print("\nLetter predicted in " + str(iterations)  + " iteration/s \n" )
    print_letter(result)
    print("\n")

    # energy_plot(energy_list)


if __name__ == "__main__":
    main()