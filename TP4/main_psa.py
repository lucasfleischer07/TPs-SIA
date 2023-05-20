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



def main():
    categories =  ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    data, countries = read_and_load_csv_data()
    data = np.array(data)
    standarized_data = estandarize_data_func(data,len(data),len(data[0]))
    pca = PCA()
    countries_principal_components = pca.fit_transform(standarized_data)
    #print('Los componentes principales son: ' + str(countries_principal_components))



    principal_df = pd.DataFrame(data=countries_principal_components, columns=['principal component ' + str(i) for i in range(7)])
    print(principal_df)
    np.set_printoptions(precision=6,suppress=True)
    print(pca.components_)

    # BIPLOT
    x_country = principal_df.values[:, 0]
    y_country = principal_df.values[:, 1]
    x_scale = 1.0 / (x_country.max() - x_country.min())
    y_scale = 1.0 / (y_country.max() - y_country.min())
    plt.scatter(countries_principal_components[:, 0:2][:,0] * x_scale, countries_principal_components[:, 0:2][:,1] * y_scale, s=3)

    for i in range(np.transpose(pca.components_[0:2, :]).shape[0]):
        plt.arrow(0, 0, np.transpose(pca.components_[0:2, :])[i, 0], np.transpose(pca.components_[0:2, :])[i, 1], color='r', alpha=0.5)
        plt.text(np.transpose(pca.components_[0:2, :])[i, 0] * 1.15, np.transpose(pca.components_[0:2, :])[i, 1] * 1.15, categories[i], color='g', ha='center', va='center')
    for i in range(len(countries_principal_components[:, 0:2][:,0])):
        plt.text(countries_principal_components[:, 0:2][:,0][i] * x_scale, countries_principal_components[:, 0:2][:,1][i] * (y_scale + 0.015), countries[i], color='b', ha='center', va='center', fontsize=4)

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()