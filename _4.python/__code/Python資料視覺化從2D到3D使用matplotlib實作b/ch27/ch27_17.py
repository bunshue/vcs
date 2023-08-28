# ch27_17.py  
import matplotlib.pyplot as plt
import  matplotlib.patches as patch
import numpy as np

ax = plt.subplot()
xy = np.array([[5,5],[8,3],[8,1],[2,1],[2,3]])
poly = patch.Polygon(xy, closed=True, fc='g')
ax.add_patch(poly)
ax.set_xlim(0,10)
ax.set_ylim(0,6)
ax.set_aspect('equal')
plt.show()




