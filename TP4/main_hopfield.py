import numpy as np

from src.hopfield import train_hopfield
from src.hopfield import print_letter
from src.hopfield import mutate


def parse_file():
    file = open('docs/alphabet_letters.txt', 'r')
    lines = file.readlines()
    
    letters = []
    letter = []
    
    for line in lines:
        if line[0] != "-" and line[0] != "1":
            letters.append(letter)
            letter = []
        else:
            i = 0
            while i < len(line):
                if line[i] == "1":
                    letter.append(1.)
                    i += 1
                elif line[i] == "-":
                    letter.append(-1.)
                    i += 2
                else:
                    i += 1
    return letters


def main():
    alg_name = "hopfield"
    letters = parse_file()
    train_letters = np.array([letters[17], letters[19], letters[21], letters[22]]) #R,T,V,W

    print("\nInput letters: \n")
    for input in train_letters:
        print_letter(input)
        print()

    print("\n ------------------------- \n")

    letter_with_noise = mutate(letters[22], 0.4)
    # predict_letter = letters[6]
    
    letter_solved, iterations = train_hopfield(np.array(letter_with_noise), train_letters)
    # print("Letter to predict: \n")
    # print_letter(predict_letter)
    print("Letter to predict with noise: \n")
    print_letter(letter_with_noise)
    print("\nLetter predicted: \n")
    print_letter(letter_solved)


if __name__ == "__main__":
    main()