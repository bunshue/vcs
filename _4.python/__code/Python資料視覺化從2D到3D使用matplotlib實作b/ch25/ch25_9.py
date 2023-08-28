# ch25_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-2, 2.2, 0.2) 
y = np.arange(-2, 2.2, 0.2) 
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
U, V = np.gradient(Z)
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V) 
ax.set_title('箭袋 Quiver',fontsize=14,color='b')
ax.set_aspect('equal')
plt.show()

      
