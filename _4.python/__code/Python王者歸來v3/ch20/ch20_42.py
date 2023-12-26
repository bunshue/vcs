# ch20_42.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 建立最初化點的位置 
def init():
    dot.set_data(x[0], y[0])        # 更新紅色點的資料
    return dot,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):    
    dot.set_data(x[i], y[i])        # 更新紅色點的資料
    return dot,

# 建立動畫需要的 Figure 物件
fig = plt.figure()
N = 200
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))
# 建立和繪製 sin 波形
x = np.linspace(0, 2*np.pi, N)
y = np.sin(x)
line, = ax.plot(x, y, color='g',linestyle='-',linewidth=3)
# 建立和繪製紅點
dot, = ax.plot([],[],color='red',marker='o',
               markersize=15,linestyle='')
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫
ani = FuncAnimation(fig=fig, func=animate,
                    frames=N,
                    init_func=init,
                    interval=20,
                    blit=True,
                    repeat=True)
plt.show()




