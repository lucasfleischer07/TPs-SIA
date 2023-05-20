import json
import csv
import numpy as np

from src.kohonen import train_kohonen
from src.kohonen import plot_heatmap_kohonen


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
        initial_radius = int(config["initial_radius"])
        final_radius = int(config["final_radius"])
        max_iterations = int(config["max_iterations"])
        k = int(config["k"])

    return learning_rate, initial_radius, final_radius, max_iterations, k


def main():
    alg_name = "kohonen"
    data, countries = read_and_load_csv_data()
    data = np.array(data)
    learning_rate, initial_radius, final_radius, max_iterations, k = read_and_load_json_data(alg_name)
    weights,choices,results = train_kohonen(data, k, max_iterations, learning_rate, initial_radius, final_radius,countries)
    print("\n\n")
    print(weights)
    print("\n\n")
    print(choices)
    print("\n\n")
    print(results)
    plot_heatmap_kohonen(results, k, learning_rate)


if __name__ == "__main__":
    main()