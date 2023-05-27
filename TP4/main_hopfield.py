import numpy as np

from src.hopfield import train_hopfield
from src.hopfield import print_letter
from src.hopfield import mutate
from src.hopfield import mutate_pattern



# def parse_file():
#     file = open('docs/alphabet_letters.txt', 'r')
#     lines = file.readlines()
    
#     letters = []
#     letter = []
    
#     for line in lines:
#         if line[0] != "-" and line[0] != "1":
#             letters.append(letter)
#             letter = []
#         else:
#             i = 0
#             while i < len(line):
#                 if line[i] == "1":
#                     letter.append(1.)
#                     i += 1
#                 elif line[i] == "-":
#                     letter.append(-1.)
#                     i += 2
#                 else:
#                     i += 1
#     return letters

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

    train_letters = np.array([letters[0], letters[11], letters[19], letters[21]]) #A,L,T,V.

    # train_letters = np.array([letters[5], letters[12], letters[21], letters[25]]) #A,L,T,V. fmvz y ajlx
    # train_letters = np.array([letters[0], letters[9], letters[11], letters[23]]) #A,L,T,V. fmvz y ajlx (mejor)


    print("\nInput letters: \n")
    for input in train_letters:
        print_letter(input)
        print()

    print("\n ------------------------- \n")

    # letter_with_noise = mutate(letters[0], 0.1)
    letter_with_noise = mutate_pattern(letters[0], 3)
    # predict_letter = letters[0]

    print("Letter to predict with noise in iteration 0: \n")
    print_letter(letter_with_noise)
    
    letter_solved, iterations = train_hopfield(np.array(letter_with_noise), train_letters)
    # letter_solved, iterations = train_hopfield(predict_letter, train_letters)

    # print("Letter to predict: \n")
    # print_letter(predict_letter)
    # print("Letter to predict with noise: \n")
    # print_letter(letter_with_noise)
    print("\nLetter predicted in " + str(iterations) + " iteration/s \n" )
    print_letter(letter_solved)
    print("\n")


if __name__ == "__main__":
    main()