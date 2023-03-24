# plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

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

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from numpy import sin

plt.plot(np.random.randn(100))


#第三張圖
plt.subplot(233)

x1 = [1, 5, 9, 13, 17]
y1 = [5, 30, 15, 35, 5]

#連線
#plt.plot(x1, y1, color='red')

#linestyle 虛線樣式
#plt.plot(x1, y1, color='red', linestyle="--")

#linestyle 虛點樣式
#plt.plot(x1, y1, color='red', linestyle="-.")

#linestyle 虛點樣式「:」
#plt.plot(x1, y1, color='red', linestyle=":")

#marker 點「.」標記
#因為需要展示出效果，因此把 linestyle 設為實線，linewidth 為 2.0，markersize 設為 16
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".")

#marker 圓「o」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="o")

#marker 星「*」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="*")

#marker 矩形「s」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="s")

#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".", label="Test")

# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 1")

x2 = [3, 8, 12, 16, 20]
y2 = [8, 33, 18, 38, 8]
# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(x2, y2, color='blue', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 2")

plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題內容及大小
plt.title('Plot title', fontsize="18") # 設定圖表標題內容及大小

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍

plt.legend()




#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()




