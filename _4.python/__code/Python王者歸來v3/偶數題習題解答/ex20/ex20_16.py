# ex20_16.py
import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return (np.power(x,2) + np.power(y, 2))
def f2(x, y):                                # 右邊曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X,Y), cmap='hsv')   # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X,Y), cmap='hsv')   # 繪製 3D 圖
plt.show()



      
