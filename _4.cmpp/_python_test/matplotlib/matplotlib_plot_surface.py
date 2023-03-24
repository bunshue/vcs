# 3D surface plot

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import viridis as colormap

step = 0.04
maxval = 1.0
fig1 = plt.figure("Figure_1")
ax1 = fig1.add_subplot(111, projection='3d')

# Create supporting points in polar coordinates
r = np.linspace(0, 1.2, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
# Transform them to cartesian system
X, Y = R*np.cos(P), R*np.sin(P)

Z = ((R**2 - 1)**2)
ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=colormap)
ax1.set_zlim3d(0, 1)
ax1.set_xlabel(r'$\phi_\mathrm{real}$')
ax1.set_ylabel(r'$\phi_\mathrm{im}$')
ax1.set_zlabel(r'$V(\phi)$')

plt.show()

