# ch25_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-10, 11) 
y = np.arange(-10, 11) 
X, Y = np.meshgrid(x, y)
U, V = X, Y
plt.quiver(X, Y, U, V) 
plt.title('箭袋 Quiver',fontsize=14,color='b')
plt.show()

      
