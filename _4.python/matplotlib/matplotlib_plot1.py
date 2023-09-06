# plot 集合

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

# 2D random walk
#fig2, ax2 = plt.subplots(num="Figure_2")

prng = np.random.RandomState(123)

x = np.linspace(0, 10, 101)

def random_walk(xy0=(0.0, 0.0), nsteps=100, std=1.0):
    xy = np.zeros((nsteps + 1, 2))
    xy[0,:] = xy0
    deltas = prng.normal(loc=0.0, scale=std, size=(nsteps, 2))
    xy[1:, :] = xy[0, :] + np.cumsum(deltas, axis=0)
    return xy

for cnt in range(3):
    traj = random_walk()
    plt.plot(traj[:, 0], traj[:, 1], label="Traj. {c}".format(c=cnt))

#ax2.legend(loc='best')

#第二張圖
plt.subplot(232)

x = np.linspace(0, 6.4, 200)    # x是numpy.ndarray格式

A = 0.8 #雜訊的振幅
y = np.cos(x) + np.random.rand(1, len(x)) * A - A / 2 #加入雜訊的點集    # y是numpy.ndarray格式

y = y.tolist()[0]   # y 由 numpy.ndarray格式 轉成list格式, 畫圖要用list格式

plt.plot(x, np.cos(x))
plt.plot(x, y)

plt.title('畫雜訊範例')

#第三張圖
plt.subplot(233)

plt.plot(np.random.randn(100))
plt.title('畫雜訊範例')

#第四張圖
plt.subplot(234)

#描點畫圓
# 角度
th = np.arange(0, 360)

# 圓周上的點P座標 
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x, y)
plt.axis('equal')       #軸比例

#第五張圖
plt.subplot(235)

#繪製半徑300的圓（y >= 0）

# 圓的方程式
r = 300  # 半徑
x = np.arange(-r, r + 1)    # x: -300～300
y = np.sqrt(r ** 2 - x ** 2)  # y

plt.plot(x, y)
plt.axis('equal')       #軸比例

#第六張圖
plt.subplot(236)

print('繪製移動平均圖')

import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_temperature.csv'

# 讀入氣溫資料
dat= pd.read_csv(filename, encoding='UTF-8')

n = len(dat)       # 資料筆數
x = range(1, n+1)  #  x軸的值（1～資料筆數）

# 氣溫
y = dat['平均氣溫']  # y軸的值（平均氣溫）
plt.plot(x, y)       # 繪圖

# 區間大小:9 的移動平均
v = np.ones(9)/9.0
y2 = np.convolve(y, v, mode='same')  # 計算移動平均
plt.plot(x[4:n-4], y2[4:n-4])        # 繪圖

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 2 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線


#第二張圖
plt.subplot(232)

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線

#第三張圖
plt.subplot(233)

plt.plot(np.random.randn(20))
plt.plot(range(20), np.random.randn(20))

#第四張圖
plt.subplot(234)

x = np.linspace(-5, 5, 1000)
y = np.sin(x) / (x**2+1)

plt.plot(x,y,lw=5)
plt.plot(x,np.cos(x))
#plt.xticks(np.arange(-5,6))

#第五張圖
plt.subplot(235)

#把這個函數大於 0 的地方標示出來。
y = np.sinc(x)
plt.plot(x,y)
plt.plot(x[y>0], y[y>0], 'o')

#第六張圖
plt.subplot(236)

x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

