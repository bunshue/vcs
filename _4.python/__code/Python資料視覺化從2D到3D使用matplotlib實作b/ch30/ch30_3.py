# ch30_3.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D             
import numpy as np

def f(x, y):                                # 曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

fig = plt.figure()                  
ax = Axes3D(fig)                            # 建立 3D 軸物件

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
plt.show()
















