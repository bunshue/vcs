"""

使用 fig, ax = plt.subplots()

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
#import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)

print('------------------------------------------------------------')	#60個

print('用plt畫圖')
plt.plot(x, np.sin(x), 'r-o')
plt.plot(x, np.cos(x), 'g-o')
plt.title('用plt畫圖, 一張子圖')

plt.show()

print('------------------------------------------------------------')	#60個

print('fig, ax = plt.subplots() 一張子圖, 可以直接換回 plt.plot()')

print('------------------------------------------------------------')	#60個

print('用fig ax畫圖, 一張子圖')
fig, ax = plt.subplots()    #一張子圖
ax.plot(x, np.sin(x), 'r-o')
ax.plot(x, np.cos(x), 'g-o')
ax.set_title('用fig ax畫圖, 一張子圖')

plt.show()

print('------------------------------------------------------------')	#60個

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), 'r-o')
ax.set_title('用fig ax畫圖, 一張子圖')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()

print('------------------------------------------------------------')	#60個

# 兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols = 2, figsize = (15, 4), dpi = 100)
fig.suptitle('兩張子圖, ncols = 2', fontsize = 16) # 圖表主標題
      
#ax0 左圖
ax0.plot(x, np.sin(x), 'r-o')
ax0.set_title('用fig ax畫圖, 兩張子圖')
      
#ax1 右圖
ax1.plot(x, np.cos(x), 'g-o')
ax1.set_title('用fig ax畫圖, 兩張子圖')

plt.show()

print('------------------------------------------------------------')	#60個

#直方圖

np.random.seed(0)

# 平均 200，標準差為 25 的分佈
mu = 200
sigma = 25
x = np.random.normal(mu, sigma, size=100)

# 擁有兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols = 2, figsize = (15, 4), dpi = 100)

#ax0 左圖
# 分成 5 組，背景為透明度為 0.75 的綠色，並且縱軸不做正規化處理為數量，直條的間距填滿
ax0.hist(x, 5, histtype = 'stepfilled', facecolor = 'g', alpha = 0.75)
ax0.set_title('stepfilled\n' + r'$\mu = 200, \sigma=25$')

#ax1 右圖
# 自定分組，縱軸執行正規化處理表示為機率，直條的寬度大小為 80%
bins = [100, 150, 180, 195, 205, 220, 250, 300]

ax1.hist(x, bins, histtype = 'bar', rwidth = 0.8)
ax1.set_title('unequal bins\n' + r'$\mu = 200, \sigma=25$')

# 緊密排列，並填滿原圖大小
fig.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

print('用fig ax畫圖, 四張子圖')

x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)

fig, ax = plt.subplots(2, 2)        # 建立4個子圖
fig.suptitle("用fig ax畫圖, 四張子圖", fontsize = 16) # 圖表主標題

ax[0, 0].plot(x, y, 'r')            # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')

ax[0, 1].plot(x, y, 'g')            # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')

ax[1, 0].plot(x, y, 'b')            # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')

ax[1, 1].plot(x, y, 'y')            # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]') 

plt.tight_layout()                  # 緊縮佈局

plt.show()

print('------------------------------------------------------------')	#60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')

ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')

ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')

ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect(2)
ax[1, 1].set_title('設定寬高比是2')

fig.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')

ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')

ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')

ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect('equal', 'box')
ax[1, 1].set_title('設定寬高比相同')

fig.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

print('兩Y軸不同刻度, plot + plot')

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()

ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel('弧度', color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")

ax2 = ax.twinx()

ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")

ax.set_title('兩Y軸不同刻度 plot + plot', size=20)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


# 2D random walk
#fig2, ax2 = plt.subplots(num="Figure_2")
#ax2.legend(loc='best')

"""
plt.xlabel('弧度')

ax.set_xlabel('弧度')
"""


