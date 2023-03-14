import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import inferno as colormap
from matplotlib.colors import LogNorm

fig = plt.figure()
fig.clf()
ax = Axes3D(fig, azim=-128.0, elev=43.0)

s = 0.05
x = np.arange(-2.0, 2.0 + s, s)
y = np.arange(-1.0, 3.0 + s, s)
X, Y = np.meshgrid(x, y)
Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2

# Without using `` linewidth=0, edgecolor='none' '', the code may produce a
# graph with wide black edges, which will make the surface look much darker.
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(),
                cmap=colormap, linewidth=0, edgecolor='none')

ax.set_xlim([-2, 2])
ax.set_ylim([-1, 3])
ax.set_zlim([0, 2500])

ax.set_xlabel("x")
ax.set_ylabel("y")

#存圖命令
filename = '__temp/Rosenbrock function.png'
fig.savefig(filename)

plt.show()

