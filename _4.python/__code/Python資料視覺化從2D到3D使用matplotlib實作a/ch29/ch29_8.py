# ch29_8.py
import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z, c=c, cmap='hsv')
plt.show()




