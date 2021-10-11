import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(-np.pi, np.pi, 0.1)
Y = np.arange(-np.pi, np.pi, 0.1)
X, Y = np.meshgrid(X, Y)
# Z = (np.sin(X) * np.sin(Y) / (X * Y))
# Z = 1 / 9 * (2 * np.cos(X) * np.cos(Y) + np.cos(X) + np.cos(Y) + 1)
Z = abs(-1 * 2j * np.sin(X))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

