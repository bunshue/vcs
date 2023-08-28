# ch24_5.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return -(x**2 + y**2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z)               # 填充輪廓圖
plt.colorbar()                      # 色彩條
oval = plt.contour(X, Y, Z)         # 輪廓圖
plt.clabel(oval,colors='b')         # 增加高度標記
plt.title('有高度標記的輪廓圖',fontsize=16,color='b')
plt.show()


      
