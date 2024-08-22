"""
# plot 集合
第06章：繪製多個圖表
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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

plt.subplot(1,2,1)      # 建立子圖表 1,2,1
plt.text(0.15,0.5,'subplot(1,2,1)',fontsize='16',c='b')

plt.subplot(2,2,2)      # 建立子圖表 2,2,2
plt.text(0.15,0.5,'subplot(2,2,2)',fontsize='16',c='m')

plt.subplot(2,2,4)      # 建立子圖表 2,2,4
plt.text(0.15,0.5,'subplot(2,2,4)',fontsize='16',c='m')

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)

plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')

plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')

plt.subplot(2,1,2)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.suptitle('主標題 : 衰減函數',fontsize=16,c='b')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure()    # 地理投影圖表 Aitoff
plt.subplot(projection="aitoff")
plt.title("地理投影 = Aitoff",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Hammer
plt.subplot(projection="hammer")
plt.title("地理投影 = Hammer",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Lambert
plt.subplot(projection="lambert")
plt.title("地理投影 = Lambert",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Mollweide
plt.subplot(projection="mollweide")
plt.title("地理投影 = Mollweide",c='b')
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x**2)
ax = plt.subplot()      # 回傳子圖物件
ax.plot(x, y)           # 使用子圖物件調用plot()函數

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
ax = plt.subplot()
ax.plot(x, y1, lw = 2)              # 線條寬度是 2
ax.plot(x, y2, linewidth = 5)       # 線條寬度是 5                

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x**2)
ax = plt.subplot()      # 回傳子圖物件
ax.plot(x, y)           # 使用子圖物件調用plot()函數
ax.set_title("Sin function")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
ax = plt.subplot()
ax.plot(squares)
ax.set_aspect('equal')

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(211)              
ax1.plot(x1, np.sin(2*np.pi*x1))

# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(212)  
ax2.plot(x2, np.sin(4*np.pi*x2))

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(211)              
ax1.plot(x1, np.sin(2*np.pi*x1))

# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(212, sharex=ax1)  # 共享 x 軸
ax2.plot(x2, np.sin(4*np.pi*x2))

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(211)              
ax1.plot(x1, np.sin(2*np.pi*x1))
ax1.tick_params('x',labelbottom=False)  # 取消顯示刻度標籤

# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(212, sharex=ax1)      # 共享 x 軸
ax2.plot(x2, np.sin(4*np.pi*x2))
plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(121)          
ax1.plot(x, np.sin(x**2),'b')
# 建立子圖 2
ax2 = plt.subplot(122)      
ax2.plot(x, 1+np.sin(x**2),'g--')

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(121)          
ax1.plot(x, np.sin(x**2),'b')
# 建立子圖 2
ax2 = plt.subplot(122,sharey=ax1)   # 共享 y 軸    
ax2.plot(x, 1+np.sin(x**2),'g--')

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(121)          
ax1.plot(x, np.sin(x**2),'b')
# 建立子圖 2
ax2 = plt.subplot(122,sharey=ax1)       # 共享 y 軸    
ax2.plot(x, 1+np.sin(x**2),'g--')
ax2.tick_params('y',labelleft=False)    # 取消顯示刻度標籤
plt.suptitle("共享 y 軸")

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(221)              
ax1.plot(x1, np.sin(2*np.pi*x1))
# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax2.plot(x2, np.sin(4*np.pi*x2))
# 建立子圖 3
x3 = np.linspace(0, 2*np.pi, 300)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)  # 共享x和y軸        
ax3.plot(x3, np.sin(x3**2),'b')
# 建立子圖 4
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)  # 共享x和y軸    
ax4.plot(x3, 1+np.sin(x3**2),'g--')
plt.suptitle("共享 x 和 y 軸")

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(221)              
ax1.plot(x1, np.sin(2*np.pi*x1))
ax1.tick_params('x',labelbottom=False)          # 取消顯示x軸刻度標籤
# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax2.plot(x2, np.sin(4*np.pi*x2))
ax2.tick_params('x', labelbottom=False)         # 取消顯示x軸刻度標籤
ax2.tick_params('y', labelleft=False)           # 取消顯示y軸刻度標籤
# 建立子圖 3
x3 = np.linspace(0, 2*np.pi, 300)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)  # 共享x和y軸        
ax3.plot(x3, np.sin(x3**2),'b')
# 建立子圖 4
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)  # 共享x和y軸    
ax4.plot(x3, 1+np.sin(x3**2),'g--')
ax4.tick_params('y',labelleft=False)            # 取消顯示y軸刻度標籤
plt.suptitle("共享 x 和 y 軸")

plt.show()

print("------------------------------------------------------------")  # 60個

fsize = 24                  # 字型大小                           
ax = plt.subplot()          # 建立圖表
ax.plot([1, 3])             # 繪製圖表
ax.set_xlabel('x 座標', fontsize=fsize)
ax.set_ylabel('y 座標', fontsize=fsize)
ax.set_title('資料布局', fontsize=fsize)

plt.show()

print("------------------------------------------------------------")  # 60個

fsize = 24                  # 字型大小                           
ax = plt.subplot()          # 建立圖表
ax.plot([1, 3])             # 繪製圖表
ax.set_xlabel('x 座標', fontsize=fsize)
ax.set_ylabel('y 座標', fontsize=fsize)
ax.set_title('資料布局', fontsize=fsize)

plt.show()

print("------------------------------------------------------------")  # 60個


def my_plot(ax, size):
    ax.plot([1, 3])             # 繪製圖表
    ax.set_xlabel('x 座標', fontsize=size)
    ax.set_ylabel('y 座標', fontsize=size)
    ax.set_title('資料布局', fontsize=size)    

fsize = 24                  # 字型大小                           
ax1 = plt.subplot(2,2,1)    # 建立圖表
my_plot(ax1,fsize)
ax2 = plt.subplot(2,2,2)    # 建立圖表
my_plot(ax2,fsize)
ax3 = plt.subplot(2,2,3)    # 建立圖表
my_plot(ax3,fsize)
ax4 = plt.subplot(2,2,4)    # 建立圖表
my_plot(ax4,fsize)

plt.show()

print("------------------------------------------------------------")  # 60個


def my_plot(ax, size):
    ax.plot([1, 3])             # 繪製圖表
    ax.set_xlabel('x 座標', fontsize=size)
    ax.set_ylabel('y 座標', fontsize=size)
    ax.set_title('資料布局', fontsize=size)    

fsize = 24                  # 字型大小                           
ax1 = plt.subplot(2,2,1)    # 建立圖表
my_plot(ax1,fsize)
ax2 = plt.subplot(2,2,2)    # 建立圖表
my_plot(ax2,fsize)
ax3 = plt.subplot(2,2,3)    # 建立圖表
my_plot(ax3,fsize)
ax4 = plt.subplot(2,2,4)    # 建立圖表
my_plot(ax4,fsize)

plt.show()

print("------------------------------------------------------------")  # 60個


def my_plot(ax, size):
    ax.plot([1, 3])             # 繪製圖表
    ax.set_xlabel('x 座標', fontsize=size)
    ax.set_ylabel('y 座標', fontsize=size)
    ax.set_title('資料布局', fontsize=size)    

fsize = 24                  # 字型大小                           
ax1 = plt.subplot(2,2,1)    # 建立圖表
my_plot(ax1,fsize)
ax2 = plt.subplot(2,2,3)    # 建立圖表
my_plot(ax2,fsize)
ax3 = plt.subplot(1,2,2)    # 建立圖表
my_plot(ax3,fsize)

plt.show()

print("------------------------------------------------------------")  # 60個


def my_plot(ax, size):
    ax.plot([1, 3])             # 繪製圖表
    ax.set_xlabel('x 座標', fontsize=size)
    ax.set_ylabel('y 座標', fontsize=size)
    ax.set_title('資料布局', fontsize=size)    

fsize = 24                  # 字型大小                           
ax1 = plt.subplot(2,2,1)    # 建立圖表
my_plot(ax1,fsize)
ax2 = plt.subplot(2,2,3)    # 建立圖表
my_plot(ax2,fsize)
ax3 = plt.subplot(1,2,2)    # 建立圖表
my_plot(ax3,fsize)

plt.show()

print("------------------------------------------------------------")  # 60個


fig, ax = plt.subplots(nrows=1,ncols=2) # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(1, 2)            # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2)               # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')
for a in ax.flat:
    a.set(xlabel='x 軸資料', ylabel='y 軸資料')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')
for a in ax.flat:
    a.set(xlabel='x 軸資料', ylabel='y 軸資料')
# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig, ax = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('共享 x 和 y 軸', fontsize=18)
ax[0].plot(x, y ** 2, 'b--')
ax[1].plot(x, 0.5 * y, 'go')
ax[2].plot(x, y, 'm+')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
x = np.arange(1,11)                         
ax1 = fig.add_subplot(2,2,1)        # 建立子圖表 1
ax1.plot(x, x)
ax1.set_title("子圖 221")
ax1 = fig.add_subplot(2,2,3)        # 建立子圖表 3
ax1.plot(x, x, 'g')
ax1.set_title("子圖 223")
ax1 = fig.add_subplot(1,2,2)        # 建立子圖表 2
ax1.plot(x, x, 'm')
ax1.set_title("子圖 122")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[1,0])
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0,0])
ax1.set_title('gs[0,0]')
ax2 = fig.add_subplot(gs[0,1])
ax2.set_title('gs[0,1]')
ax3 = fig.add_subplot(gs[1,0])
ax3.set_title('gs[1,0]')
ax4 = fig.add_subplot(gs[1,1])
ax4.set_title('gs[1,1]')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0,0])
ax1.set_title('gs[0,0]')
ax2 = fig.add_subplot(gs[0,1])
ax2.set_title('gs[0,1]')
ax3 = fig.add_subplot(gs[1,:])
ax3.set_title('gs[1,:]')

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0)
ax = gs.subplots(sharex=True, sharey=True)
fig.suptitle('共享 x 和 y 軸', fontsize=18)
ax[0].plot(x, y ** 2, 'b--')
ax[1].plot(x, 0.5 * y, 'go')
ax[2].plot(x, y, 'm+')
# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
fig.suptitle('共享 x(column) 和 y(row) 軸', fontsize=18)
ax1.plot(x, y, 'b')
ax2.plot(x, y ** 2, 'g')
ax3.plot(x+1, y, 'm')
ax4.plot(x+2, y ** 2, 'r')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
y2 = np.cos(x)
# 繪圖
ax.plot(x, y1)
ax.plot(x, y2, 'g', lw='3')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax1 = plt.subplots(1, 1)
ax2 = ax1.twinx()               # 使用相同的 x 軸
# y1 = sin(x)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
# y2 = cos(x)
y2 = np.cos(x)
# 繪圖
ax1.plot(x, y1)
ax2.plot(x, y2, 'g', lw='3')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
gs = fig.add_gridspec(2,2)          # 建立 2 x 2 網格

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
gs_ax1 = fig.add_subplot(gs[0,0])   # 用網格物件索引0,0指定子圖
gs_ax1.plot(x, y,'b')               
gs_ax1.set_title('子圖[0, 0]')
gs_ax2 = fig.add_subplot(gs[0,1])   # 用網格物件索引0,1指定子圖
gs_ax2.plot(x, y,'g')               
gs_ax2.set_title('子圖[0, 1]')
gs_ax3 = fig.add_subplot(gs[1,0])   # 用網格物件索引1,0指定子圖
gs_ax3.plot(x, y,'m')               
gs_ax3.set_title('子圖[1, 0]')
gs_ax4 = fig.add_subplot(gs[1,1])   # 用網格物件索引1,1指定子圖
gs_ax4.plot(x, y,'r')               
gs_ax4.set_title('子圖[1, 1]')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
gs = fig.add_gridspec(3, 3)         # 建立 3 x 3 子圖
x = np.arange(1,11) 
gs_ax1 = fig.add_subplot(gs[0,:])   # 使用切片觀念
gs_ax1.plot(x, x)
gs_ax1.set_title('gs[0,:]')
gs_ax2 = fig.add_subplot(gs[1,:-1]) # 使用切片觀念
gs_ax2.plot(x, x)
gs_ax2.set_title('gs[1,:-1]')
gs_ax3 = fig.add_subplot(gs[1:,-1]) # 使用切片觀念
gs_ax3.plot(x, x)
gs_ax3.set_title('gs[1:,-1]')
gs_ax4 = fig.add_subplot(gs[-1,0])  # 使用切片觀念
gs_ax4.plot(x, x)
gs_ax4.set_title('gs[-1,0]')
gs_ax5 = fig.add_subplot(gs[-1,-2]) # 使用切片觀念
gs_ax5.plot(x, x)
gs_ax5.set_title('gs[-1,-2]')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
# 子圖 0 列和 1 列的高度比是 2:1
# 子圖 0 列和 1 列的寬度比是 2:1
gs = fig.add_gridspec(nrows=2, ncols=2, height_ratios=[2,1],
                      width_ratios=[2,1])
# 建立子圖物件
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,:])
# x 軸資料
x = np.linspace(0, 2*np.pi, 500)
# 繪製子圖
ax1.plot(x, np.sin(x))
ax2.plot(x, np.sin(x)**2,'g')
ax3.plot(x, np.sin(x) + np.cos(x),'m')
# 建立軸標籤
ax1.set_ylabel("y")
ax3.set_xlabel("x")
ax3.set_ylabel("y")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1,0.1,0.8,0.8])

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1,0.1,0.5,0.8])
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1,0.1,0.8,0.8])
x = np.linspace(0, 2*np.pi, 500)
ax.plot(x, np.sin(x)**2,'g')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()

x = np.arange(1,11)
plt.plot(x, x)
plt.title('外圖表')
#新增子區域位置和大小
left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
# 設定子座標物件
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x,x, 'g')
ax2.set_title('內圖表')

plt.show() 

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(2 * np.pi * x) + 1
fig = plt.figure()
ax = plt.axes()
#ax.set_xlim([1, 5])
#ax.set_ylim([-0.5, 2.5])
plt.plot(x, y)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(2 * np.pi * x) + 1
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([1, 5])
ax.set_ylim([-0.5, 2.5])
plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


