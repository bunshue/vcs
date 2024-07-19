
from matplotlib.animation import FuncAnimation

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# 建立最初化的 line 資料 (x, y)  
def init():  
    line.set_data([], [])  
    return line,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):        
    x = np.linspace(0, 2*np.pi, 500)        # 建立 sin 的 x 值 
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 建立 sin 的 y 值  
    line.set_data(x, y)                     # 更新波形的資料
    return line,

# 建立動畫需要的 Figure 物件
fig = plt.figure()   
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-2, 2))    
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = ax.plot([], [], lw=3, color='g')  
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫  
ani = FuncAnimation(fig, animate,
                    frames = 200,          
                    init_func = init,                        
                    interval = 20)          # interval是控制速度
ani.save('tmp_sin.gif', writer='pillow')        # 儲存 tmp_sin.gif 檔案

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立最初化的 line 資料 (x, y)  
def init():  
    line.set_data([], [])  
    return line,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):        
    x = np.linspace(0, 2*np.pi, 10)         # 建立 sin 的 x 值 
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 建立 sin 的 y 值  
    line.set_data(x, y)                     # 更新波形的資料
    return line,

# 建立動畫需要的 Figure 物件
fig = plt.figure()   
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-2, 2))    
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = ax.plot([], [], lw=3, color='g')  
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫  
ani = FuncAnimation(fig, animate,
                    frames = 200,          
                    init_func = init,                        
                    interval = 20)          # interval是控制速度
ani.save('tmp_sin2.gif', writer='pillow')       # 儲存 tmp_sin2.gif 檔案

plt.show()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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
#line, = ax.plot(x, y, color='g',linestyle='-',linewidth=3)
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

print('------------------------------------------------------------')	#60個

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

   

print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
(line,) = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # update the data
    return (line,)


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return (line,)


# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
ani = animation.FuncAnimation(
    fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False
)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




