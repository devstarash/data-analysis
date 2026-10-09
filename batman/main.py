import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
DATA_FILE_NAME = "buildings.dat.txt"
information_about_buildings = []
EPS = 300
MIN_SAMPLES = 2
with open(DATA_FILE_NAME, 'r') as file:
    next(file)
    for line in file:
        information_about_buildings.append([int(x) for x in line.split()])
model = DBSCAN(eps = EPS, min_samples = MIN_SAMPLES)
labels = model.fit_predict(information_about_buildings)
information_about_buildings = np.array(information_about_buildings)
plt.scatter(information_about_buildings[:, 0], information_about_buildings[:, 1], c = labels)
possible_coordinates_of_vo = information_about_buildings[labels == -1]
print('Возможные координаты Во')
print('x\ty\tH')
for coordinates in possible_coordinates_of_vo:
  print(f'{coordinates[0]}\t{coordinates[1]}\t{coordinates[2]}')
  plt.scatter(coordinates[0], coordinates[1], s=300, facecolors='none', edgecolors='red', linewidths=2)
  plt.annotate(f"({coordinates[0]}, {coordinates[1]}, {coordinates[2]})", (coordinates[0], coordinates[1]), textcoords="offset points", xytext=(15, -5))
plt.title("Где может находиться ВО?")
plt.xlabel("X, футы")
plt.ylabel("Y, футы")
plt.show()