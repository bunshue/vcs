# ch20_52.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(x, y):                                # 左邊曲面函數
    return (4 - x**2 - y**2)
def animate(i):
    ax.view_init(60,i)

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖
ax.set_axis_off()

ani = FuncAnimation(fig,func=animate,frames=np.arange(0,360,3),
                    interval=60)
plt.show()


      
