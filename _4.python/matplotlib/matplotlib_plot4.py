'''
[Python] Matplotlib 基本教學 

'''


import numpy as np
import matplotlib.pyplot as plt


selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


'''
#線圖


# 建立 x，從 -pi 到 pi，共 100 點，且需包含終點 pi
x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
c,s,t = np.cos(x), np.sin(x), np.tan(x)

# 第一次呼叫 plt.plot 會自動建立合適的 figure
# 之後若有使用到 plt.method 皆以此 figure 為主
# 可以使用 latex 語法，需用 $ ... $ 包住
plt.plot(x, c, label=r'cos$\theta$')

# 之後呼叫 plt.plot 會使用先前建立的 figure
# 畫出紅色向下三角形
plt.plot(x, s, 'rv', label=r'sin$\theta$')
# 畫出綠虛線，並在各點位置標上綠線青圓點
plt.plot(x, t, color='g', linestyle='dashed', marker='o', markerfacecolor='c', markersize=5)

# 設定 x軸 label
plt.xlabel('X軸')
# 設定 x軸對應的刻度，並替換為文字
plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# 設定 x軸左右範圍
xmin ,xmax = x.min(), x.max()
dx = (xmax - xmin) * 0.2
plt.xlim(xmin - dx, xmax + dx)

# 設定 y軸 label
plt.ylabel('Y軸')
# 設定 x軸對應的刻度
plt.yticks([-1, 0, +1])
# 設定 y軸上下範圍
ymin ,ymax = c.min(), c.max()
dy = (ymax - ymin) * 0.2
plt.ylim(ymin - dy, ymax + dy)

plt.title('標題')

# 放置文字
plt.text(0, 1.2, '我在這', color='red')

# 需有 label 才會顯示，所以 tanθ 並無顯示
plt.legend()

# 建立中心坐標軸
# 回傳目前的坐標軸 get current axes
ax = plt.gca()
# 將上跟右的線，設成隱藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 設定 x軸刻度顯示在下方
ax.xaxis.set_ticks_position('bottom')
# 設定下方的線，移動至 data 為 -1 的地方
ax.spines['bottom'].set_position(('data',-1))
# 設定 y軸刻度顯示在左方
ax.yaxis.set_ticks_position('left')
# 設定左方的線，移動至坐標軸中心
ax.spines['left'].set_position(('axes', 0.5))
# ---------------------------------------------

# 顯示圖
plt.show()


#分隔圖


import matplotlib.pyplot as plt

# 建立第一張圖，若直接 plt.plot 隱含自動建立 figure 並建立 subplot(111)
plt.figure(1)
# 第一張圖的第一張子圖，231 表示大小為 row:2 col:3 的第一張，index 從 1 開始
plt.subplot(231)
plt.plot([1,2,3])

# 第一張圖的第五張子圖，等同235，index 從 1 開始
# plt.subplot(nrows, ncols, plot_number)
# 但 plot_number 不是參數名，所以無法寫成 plt.subplot(nrows=2, ncols=3, plot_number=5)
plt.subplot(2, 3, 5)
plt.plot([4,5,6])

# 建立第二張圖，若無建立，以下行為會覆蓋之前的圖
plt.figure(2)
# 默認建立子圖 subplot(111)
plt.plot([4,5,6])
# 切換到 figure 1 ; 子圖 subplot(235) 仍是當前圖
plt.figure(1)
# 加入 subplot 235 的標题
plt.title('fifth', color='r') 

# 顯示圖
plt.show()


#subplot 搭配 gridspec

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 建立 3x3 的 GridSpec 
gs = gridspec.GridSpec(2, 3)

# 建立第一張圖，若直接 plt.plot 隱含自動建立 figure 並建立 subplot(111)
plt.figure(1)
# 第一張圖的 (0,-1) 子圖，index 從 0 開始
plt.subplot(gs[0,-1])
plt.plot([1,2,3])
# 第一張圖的第二欄，index 從 0 開始，也可用 [1,0:3] 表示
plt.subplot(gs[1,:])
plt.plot([4,5,6])

# 建立第二張圖，若無建立，以下行為會覆蓋之前的圖
plt.figure(2)
# 默認建立子圖 subplot(111)
plt.plot([4,5,6])
# 切換到 figure 1 ; 子圖 (1,:) 仍是當前圖
plt.figure(1)
# 切換到 (0,-1) 成為 figure1 的當前圖
plt.subplot(gs[0,-1])
# 加入 subplot (0,-1) 的標题
plt.title('(0,-1)', color='r') 

# 顯示圖
plt.show()

'''

''' fail
#直方圖

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

# 平均 200，標準差為 25 的分佈
mu = 200
sigma = 25
x = np.random.normal(mu, sigma, size=100)

# 擁有兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(15, 4), dpi=100)

# 分成 5 組，背景為透明度為 0.75 的綠色，並且縱軸不做正規化處理為數量，直條的間距填滿
ax0.hist(x, 5, normed=0, histtype='stepfilled', facecolor='g', alpha=0.75)
ax0.set_title('stepfilled\n' + r'$\mu = 200, \sigma=25$')

# 自定分組，縱軸執行正規化處理表示為機率，直條的寬度大小為 80%
bins = [100, 150, 180, 195, 205, 220, 250, 300]
ax1.hist(x, bins, normed=1, histtype='bar', rwidth=0.8)
ax1.set_title('unequal bins\n' + r'$\mu = 200, \sigma=25$')

# 緊密排列，並填滿原圖大小
fig.tight_layout()

# 顯示圖
plt.show()
'''

#散點圖

import numpy as np
import matplotlib.pyplot as plt


N = 150
# 產生 150 個 0~2 之間的隨機半徑
r = 2 * np.random.rand(N)
# 產生 150 個 0~2pi 之間的隨機弧度
theta = 2 * np.pi * np.random.rand(N)
# 區域大小與半徑成正比
area = 50 * r**2
# 顏色由弧度決定
colors = theta

ax = plt.subplot(211)
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

# 畫出極座標圖，此時的 x 為弧度，y 為半徑
ax = plt.subplot(212, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

plt.show()

#圓餅圖

import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
# 分離係數，所以只有 'Hogs' 會分離
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
# 從 90° 開始，逆時針排列，並加上陰影，並加上每塊的比例，格式為 '%1.2f%%'
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
# 調整比例，確認顯示為圓形
ax1.axis('equal')

plt.show()


