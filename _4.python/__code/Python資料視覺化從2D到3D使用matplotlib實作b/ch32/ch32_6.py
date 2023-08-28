# ch32_6.py
from matplotlib.animation import FuncAnimation  
import matplotlib.pyplot as plt  
import numpy as np  

# 建立最初化的 line 資料 (x, y) 
def init():  
    line.set_data([], [])  
    return line, 
# 建立逆時鐘的螺紋線 
def animate(i):      
    r = 0.1 * i 
    x = r * np.sin(-r)      # 建立 x 點資料
    y = r * np.cos(-r)      # 建立 y 點資料      
    xlist.append(x)         # 將新的點資料 x 加入 xlist
    ylist.append(y)         # 將新的點資料 y 加入 ylist
    line.set_data(xlist, ylist)    # 更新線條     
    return line,
# 建立動畫需要的 Figure 物件  
fig = plt.figure()
# 建立軸物件與設定大小
axes = plt.axes(xlim=(-25, 25), ylim=(-25, 25))  
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = axes.plot([], [], lw=3, color='g')
# 最初化線條的 x, y 資料, xlist, ylist
xlist, ylist = [], []    
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫     
anim = FuncAnimation(fig, animate,  
                     init_func = init,  
                     frames = 200, 
                     interval = 10)  
plt.show()

