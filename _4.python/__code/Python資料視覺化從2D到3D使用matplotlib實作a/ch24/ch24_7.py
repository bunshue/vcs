# ch24_7.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1.2-x**2+y**5)*np.exp(-x**2-y**2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-2.5, 2.5, 100)
y = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X,Y,Z,12,cmap='Greens')        # 填充輪廓圖
plt.colorbar()                              # 色彩條
oval = plt.contour(X,Y,Z,12,colors='b')     # 輪廓圖
plt.clabel(oval,colors='b')                 # 增加高度標記
plt.title('指數函數的輪廓圖,levels=12',fontsize=16,color='b')
plt.show()


      
