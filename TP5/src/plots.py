import numpy as np
import matplotlib.pyplot as plt

def plot_letters_patterns_with_noise(letters_patterns_with_noise):
    num_letters = len(letters_patterns_with_noise)
    num_rows = (num_letters) // 5  # Calcular el número de filas necesario
    fig, axs = plt.subplots(num_rows, 6, figsize=(10, num_rows * 1.5))
    axs = axs.flat

    for i, ax in enumerate(axs):
        if i < num_letters:
            letter_vector = letters_patterns_with_noise[i]
            matrix = np.array(letter_vector).reshape(7, 5)

            # Crear el gráfico de la matriz con divisiones entre celdas
            num_rows, num_columns = matrix.shape
            colors = [['violet' if val == 1 else 'white' for val in row] for row in matrix]

            if num_columns > 0:
                ax.axis('off')
                table = ax.table(cellText=None, cellColours=colors, cellLoc='center', loc='center')
                table.scale(1, 1.5)
                table.auto_set_font_size(False)
                table.set_fontsize(14)
                ax.axis('off')

    # Ajustar los espacios entre las subtramas y mostrar el gráfico
    plt.tight_layout()
    plt.show()


def plot_letters_patterns(letters_patterns):
    num_letters = len(letters_patterns)
    num_rows = (num_letters) // 5  # Calcular el número de filas necesario
    fig, axs = plt.subplots(num_rows, 6, figsize=(10, num_rows * 1.5))
    axs = axs.flat

    for i, ax in enumerate(axs):
        if i < num_letters:
            matrix = letters_patterns[i]

            # Crear el gráfico de la matriz con divisiones entre celdas
            num_rows, num_columns = matrix.shape
            colors = [['violet' if val == 1 else 'white' for val in row] for row in matrix]

            if num_columns > 0:
                ax.axis('off')
                table = ax.table(cellText=None, cellColours=colors, cellLoc='center', loc='center')
                table.scale(1, 1.5)
                table.auto_set_font_size(False)
                table.set_fontsize(14)
                ax.axis('off')

    # Ajustar los espacios entre las subtramas y mostrar el gráfico
    plt.tight_layout()
    plt.show()

    
def plot_one_letter_patterns(letter_patterns):
    fig, ax = plt.subplots(1, figsize=(2, 3))

    # Create the color map for the pattern
    colors = [['violet' if val == 1 else 'white' for val in row] for row in letter_patterns]

    # Create the table with cell colors
    num_rows, num_columns = letter_patterns.shape
    if num_columns > 0:
        ax.axis('off')
        table = ax.table(cellText=None, cellColours=colors, cellLoc='center', loc='center')
        table.scale(1, 1.5)
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        ax.axis('off')

    # Show the plot
    plt.tight_layout()


def plot_points_latent_space(x, y, labels, title = ''):
    plt.clf()
    plt.plot(x, y, color='blue', marker='o', linestyle='none', markersize=4)
    for i in range(len(labels)):
        plt.text(x[i], y[i] + 0.04, labels[i], color='black', ha='center',
                va='center', fontsize=10)
    plt.title(title)

    plt.show()