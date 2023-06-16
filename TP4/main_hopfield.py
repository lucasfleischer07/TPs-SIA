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

    # train_letters = np.array([letters[0], letters[11], letters[19], letters[21]]) #ALTV
    train_letters = np.array([letters[5], letters[12], letters[21], letters[25]]) #FMVZ. 

    # train_letters = np.array([letters[0], letters[9], letters[11], letters[23]]) #A,j,l,x 

    print("\nInput letters: \n")
    for input in train_letters:
        print_letter(input)
        print()

    print("\n ------------------------- \n")

    # letter_with_noise = mutate(letters[0], 0.1)

    noise = 8
    letter_with_noise = mutate_pattern(letters[25], noise)

    # predict_letter = letters[12]

    # print("Letter to predict: \n")
    # print_letter(predict_letter)
    print("Letter to predict with noise: " + str(noise) + "\n")
    print_letter(letter_with_noise)
    

    #forma 2 con energia
    result, iterations, energy_list = train_hopfield(np.array(letter_with_noise), train_letters)
    # result, iterations, energy_list = train_hopfield(predict_letter, train_letters)

    
 
    print("\nLetter predicted in " + str(iterations)  + " iteration/s \n" )
    print_letter(result)
    print("\n")

    energy_plot(energy_list)


if __name__ == "__main__":
    main()