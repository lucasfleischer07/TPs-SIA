import json
import csv
import numpy as np
from sklearn.decomposition import PCA

from src.kohonen import estandarize_data_func
from src.oja import train_oja
from main_pca import bar_graph

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


def read_and_load_json_data(alg_name):
    with open('./config.json', 'r') as config_file:
        data_from_json = json.load(config_file)
        config_file.close()

    if(alg_name in data_from_json):
        config = data_from_json[alg_name]
        learning_rate = float(config["learning_rate"])
        max_epochs = int(config["max_epochs"])

    return learning_rate, max_epochs



def main(): 
    alg_name = "oja"
    labels = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    
    data, countries = read_and_load_csv_data()
    learning_rate, max_epochs = read_and_load_json_data(alg_name)
    
    data = np.array(data)
    data_standarized = estandarize_data_func(data, len(data), len(data[0]))
    
    initial_weights = 2 * np.random.default_rng().random(len(data_standarized[0])) - 1

    weights = train_oja(data_standarized, learning_rate, initial_weights, max_epochs)
    

    # Realiza una multiplicación de matriz entre data_standarized y weights utilizando la función np.matmul de NumPy.
    # Esta operación de multiplicación de matriz np.matmul(data_standarized, weights) aplica 
    # la transformación lineal definida por los pesos aprendidos a los datos estandarizados, lo que permite obtener
    # la representación de los datos en el espacio de las componentes principales.
    pca = np.matmul(data_standarized, weights)
    
    # print("Approximated Eigenvector - First Component")
    # print(weights)
    # print("Approximated PCA1")
    # print(pca)

    bar_graph(weights, labels, 'PCA1 con Oja')
    bar_graph(pca, countries, 'PCA1 por pais con Oja')

    pca = PCA()
    principal_components = pca.fit_transform(data_standarized)

    # print("Eigenvector - First Component")
    # print(pca.components_.T[:, 0])
    # print("PCA 1")
    # print(principal_components[:, 0])

    bar_graph(pca.components_[0], labels, "PCA1 con Sklearn")
    bar_graph(principal_components[:, 0], countries, "PCA1 por pais con Sklearn")

    error = 0
    for i in range(len(weights)):
        error = np.abs(weights[i] - principal_components[0][i])
    print("\nError: " + str(error))


if __name__ == "__main__":
    main()