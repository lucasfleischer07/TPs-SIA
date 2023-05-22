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


def biplot_graph(principal_df, countries_principal_components, pca, categories, countries):
    x_country = principal_df.values[:, 0]
    y_country = principal_df.values[:, 1]
    x_scale = 1.0 / (x_country.max() - x_country.min())
    y_scale = 1.0 / (y_country.max() - y_country.min())
    plt.scatter(countries_principal_components[:, 0:2][:,0] * x_scale, countries_principal_components[:, 0:2][:,1] * y_scale, s=3)

    for i in range(np.transpose(pca.components_[0:2, :]).shape[0]):
        plt.arrow(0, 0, np.transpose(pca.components_[0:2, :])[i, 0], np.transpose(pca.components_[0:2, :])[i, 1], color='r', alpha=0.5)
        plt.text(np.transpose(pca.components_[0:2, :])[i, 0] * 1.15, np.transpose(pca.components_[0:2, :])[i, 1] * 1.15, categories[i], color='g', ha='center', va='center')
    for i in range(len(countries_principal_components[:, 0:2][:,0])):
        plt.text(countries_principal_components[:, 0:2][:,0][i] * x_scale, countries_principal_components[:, 0:2][:,1][i] * (y_scale + 0.015), countries[i], color='b', ha='center', va='center', fontsize=8)

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title('Valores de las Componentes Principales 1 y 2')

    plt.grid()
    plt.show()


def bar_graph(countries_principal_components, countries, title): 
    countries_principal_components_value = []
    for country in countries_principal_components:
        value = np.sum(country)
        countries_principal_components_value.append(value)

    x = countries
    y = countries_principal_components_value

    plt.ylim(np.amin(countries_principal_components_value), np.amax(countries_principal_components_value))

    # Plot
    plt.bar(x, y)

    # Etiquetas y título
    plt.ylabel('PCA1')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')

    plt.show()

def plot_pca(vec, labels, descr):
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

    principal_df = pd.DataFrame(data=countries_principal_components, columns=['principal component ' + str(i) for i in range(7)])
    print(principal_df)
    np.set_printoptions(precision=6,suppress=True)
    print(pca.components_)


    boxplot_graph(data, categories, 'Diagrama de las características de los países estandarizadas')
    biplot_graph(principal_df, countries_principal_components, pca, categories, countries)
   
    bar_graph(countries_principal_components[:, 0], countries, 'PCA1 per country')
    #este tiene colores en rojo negativos, azules positivos.
    # plot_pca(countries_principal_components[:, 0], countries, "PCA1 per country")
    
    
    



if __name__ == "__main__":
    main()