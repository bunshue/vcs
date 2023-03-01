
##########
## Code for the 3D surface plot and the 2D random walk tajectories
##########
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import viridis as colormap

"""
Figure 1: a 3D surface plot (from matplotlib gallery)
"""
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

"""
Figure 2: a few examples of 2D random walk
"""
fig2, ax2 = plt.subplots(num="Figure_2")

prng = np.random.RandomState(123)

x = np.linspace(0, 10, 101)

def random_walk(xy0=(0.0, 0.0), nsteps=100, std=1.0):
    xy = np.zeros((nsteps + 1, 2))
    xy[0,:] = xy0
    deltas = prng.normal(loc=0.0, scale=std, size=(nsteps, 2))
    xy[1:, :] = xy[0, :] + np.cumsum(deltas, axis=0)
    return xy

for cnt in range(3):
    traj = random_walk()
    ax2.plot(traj[:, 0], traj[:, 1], label="Traj. {c}".format(c=cnt))

ax2.legend(loc='best')

plt.show()
####################
