# ch25_8.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-3, 3.5, 0.5) 
y = np.arange(-3, 3.5, 0.5) 
X, Y = np.meshgrid(x, y)
U = np.sin(X) * Y
V = np.cos(X) * X
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V) 
ax.set_title('箭袋 Quiver',fontsize=14,color='b')
ax.set_aspect('equal')
plt.show()

      
