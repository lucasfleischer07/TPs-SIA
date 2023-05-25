import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import csv

from src.kohonen import estandarize_data_func  

def read_and_load_csv_data():
    with open('docs/europe.csv', 'r') as csv_file:
        plots = csv.reader(csv_file, delimiter=',')
        next(plots)   # Para skipear la linea de Contry, Area y eso

        data = []
        countries=[]

        for row in plots:
            countries.append(str(row[0]))
            data.append([int(row[1]), int(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])])

        csv_file.close()

    return data, countries


def boxplot_graph(data, categories, title_name):
    # plt.figure(figsize=(8, 6))  # Creo el plt con un tamaio determinado
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan'] # Defino los colores que uso para cada categoria

    bp = plt.boxplot(data, patch_artist=True) # Datos NO Estandarizados

    # Personalizar el color de cada caja
    for box, flier, color in zip(bp['boxes'], bp['fliers'], colors):
        box.set(facecolor=color)  # Asignar el color a cada caja
        flier.set(markerfacecolor=color, marker='o', markersize=5)  # Asignar el color a los puntos atípicos

    # Etiquetas para los ejes y Título del gráfico
    plt.xlabel('Componentes Principales')
    plt.ylabel('Valores')
    plt.title(title_name)
    
    # Pongo en el eje x el nombre de las categorias
    plt.xticks(range(1, len(categories) + 1), categories, rotation=45, ha='right')
    
    plt.show()


#ESTE NOS DA ESCALA DE PAISES MAS CHICOS
# def biplot_graph(principal_df, countries_principal_components, pca, categories, countries):
#     x_country = principal_df.values[:, 0]
#     y_country = principal_df.values[:, 1]
#     x_scale = 1.0 / (x_country.max() - x_country.min())
#     y_scale = 1.0 / (y_country.max() - y_country.min())
#     plt.scatter(countries_principal_components[:, 0:2][:,0] * x_scale, countries_principal_components[:, 0:2][:,1] * y_scale, s=1)

#     for i in range(np.transpose(pca.components_[0:2, :]).shape[0]):
#         plt.arrow(0, 0, np.transpose(pca.components_[0:2, :])[i, 0], np.transpose(pca.components_[0:2, :])[i, 1], color='r', alpha=0.5, head_width=0.05, head_length=0.05)
#         plt.text(np.transpose(pca.components_[0:2, :])[i, 0] * 1.15, np.transpose(pca.components_[0:2, :])[i, 1] * 1.15, categories[i], color='g', ha='center', va='center')
#     for i in range(len(countries_principal_components[:, 0:2][:,0])):
#         plt.text(countries_principal_components[:, 0:2][:,0][i] * x_scale, countries_principal_components[:, 0:2][:,1][i] * (y_scale + 0.015), countries[i], color='b', ha='center', va='center', fontsize=8)

#     plt.xlabel("PC1")
#     plt.ylabel("PC2")
#     plt.title('Valores de las Componentes Principales 1 y 2')

#     plt.grid()
#     plt.show()


#ESTE NOS DA ESCALA DE PAISES MAS GRANDE
def biplot_graph(pca, principal_components, loadings, countries, labels):
    fig, ax = plt.subplots()
    ax.scatter(principal_components[:, 0], principal_components[:, 1])
    
    for i in range(len(principal_components[0])):
        ax.arrow(0, 0, loadings[i, 0], loadings[i, 1], head_width=0.05, head_length=0.05, fc='red', ec='red')
        ax.text(loadings[i, 0]*1.2, loadings[i, 1]*1.2, f'{labels[i]}', color='purple')

    colors = [
    'blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'gray',
    'olive', 'cyan', 'magenta', 'lime', 'teal', 'lavender', 'maroon',
    'navy', 'yellow', 'aqua', 'salmon', 'gold', 'indigo', 'tan', 'coral',
    'peru', 'plum', 'slategray', 'darkgreen', 'sienna'
    ]

    country_colors = dict(zip(countries, colors))  # Diccionario de país-color

    for i in range(len(principal_components)):
        # ax.text(principal_components[i, 0], principal_components[i, 1], f'{countries[i]}', color='blue')
        ax.scatter(principal_components[i, 0], principal_components[i, 1], color=colors[i])

    print("colors" + str(country_colors))


    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    ax.set_xlabel(f'PCA 1')
    ax.set_ylabel(f'PCA 2')
    ax.set_title('Biplot con valores de componentes principales 1 y 2')

    plt.show()


    data = {
        '  Austria': 'blue', '  Belgium': 'green', '  Bulgaria': 'red', '  Croatia': 'orange',
        '  Czech Republic': 'purple', '  Denmark': 'brown', '  Estonia': 'pink', '  Finland': 'gray',
        '  Germany': 'olive', '  Greece': 'cyan', '  Hungary': 'magenta', '  Iceland': 'lime',
        '  Ireland': 'teal', '  Italy': 'lavender', '  Latvia': 'maroon', '  Lithuania': 'navy',
        '  Luxembourg': 'yellow', '  Netherlands': 'aqua', '  Norway': 'salmon', '  Poland': 'gold',
        '  Portugal': 'indigo', '  Slovakia': 'tan', '  Slovenia': 'coral', '  Spain': 'peru',
        '  Sweden': 'plum', '  Switzerland': 'slategray', '  Ukraine': 'darkgreen',
        '  United Kingdom': 'sienna'
    }

    # Crear listas separadas para los nombres de los países y los colores
    countries = list(data.keys())
    colors = list(data.values())

    for i in range(len(countries)):
        x = 1      # Coordenada x del punto
        y = i + 1  # Coordenada y del punto
        color = colors[i]   # Color del punto
        country = countries[i]   # Nombre del país
        
        plt.scatter(x, y, color=color)   # Graficar el punto

        plt.text(x, y, country, color='black', fontsize=8, ha='left', va='center')   # Agregar el nombre del país

    # Ajustar los límites del gráfico
    plt.xlim(0, 2)
    plt.ylim(0, len(countries) + 1)

    # Mostrar el gráfico
    plt.show()


def bar_graph(vec, labels, descr):
    x = list(labels)
    y = list(vec)
    plt.rc('font', size=10)

    fig, ax = plt.subplots(figsize=(10, 8))
    width = 0.5
    ind = np.arange(len(y))  

    cc = ['colors'] * len(y)
    for n, val in enumerate(y):
        if val < 0:
            cc[n] = 'red'
        elif val >= 0:
            cc[n] = 'blue'

    ax.bar(ind, y, width, color=cc)
    ax.set_xticks(ind + width / 100)
    ax.set_xticklabels(x, minor=False)
    plt.xticks(rotation=90)
    ax.set_ylabel('PCA1')
    ax.set_xlabel('Paises')
    plt.title(descr)
    plt.show()



def main():
    categories =  ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    data, countries = read_and_load_csv_data()
    data = np.array(data)
    # boxplot_graph(data, categories, 'Diagrama de las características de los países sin estandarizadas')
    
    standarized_data = estandarize_data_func(data,len(data),len(data[0]))
    pca = PCA()
    
    countries_principal_components = pca.fit_transform(standarized_data)
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)


    principal_df = pd.DataFrame(data=countries_principal_components, columns=['principal component ' + str(i) for i in range(7)])
    print(principal_df)
    np.set_printoptions(precision=6,suppress=True)
    print(pca.components_)

    boxplot_graph(data, categories, 'Diagrama de las características de los países estandarizadas')

    biplot_graph(pca, countries_principal_components, loadings, countries, categories)

    #este tiene colores en rojo negativos, azules positivos.
    bar_graph(countries_principal_components[:, 0], countries, "PCA1 per country")
    
    
    



if __name__ == "__main__":
    main()