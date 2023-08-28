# ch29_3.py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.plot(x, y, z, color='m', lw=3)
plt.show()


