# plot 集合 subplot的另一種寫法 3

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

print('subplot的另一種寫法 3')

# plot 集合

#          編號                                     圖像大小[英吋]      解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '不使用subplot畫多圖', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

print("在圖表的指定地方畫圖, 不用subplot")

listx = [1, 2, 3, 4, 5]
listy = [15, 50, 80, 40, 70]

print("1左下開始(0.1, 0.1), w = 0.3, h = 0.3, 左下圖")
plt.axes([0.1, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'r-s')

print("2左下開始(0.6, 0.1), w = 0.3, h = 0.3, 右下圖")
plt.axes([0.6, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'g--o')

print("3左下開始(0.1, 0.6), w = 0.3, h = 0.3, 左上圖")
plt.axes([0.1, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'b-s')

print("4左下開始(0.6, 0.6), w = 0.3, h = 0.3, 右上圖")
plt.axes([0.6, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'y--o')

plt.show()

print('------------------------------------------------------------')	#60個



#subplot 搭配 gridspec

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
c,s,t = np.cos(x), np.sin(x), np.tan(x)

# 建立 3x3 的 GridSpec 
gs = gridspec.GridSpec(3, 3)

# 第0列 第0張
plt.subplot(gs[0, 0])
plt.plot(x, c)

# 第0列 第1張
plt.subplot(gs[0, 1])
plt.plot(x, c)

# 第0列 第2張
plt.subplot(gs[0, 2])
plt.plot(x, c)

# 第1列，index 從 0 開始，也可用 [1,0:3] 表示
plt.subplot(gs[1,:])
plt.plot(x, c)

# 第2列 第0張
plt.subplot(gs[2, 0])
plt.plot(x, c)

# 第2列 第1張
plt.subplot(gs[2, 1])
plt.plot(x, c)

# 第2列 第2張
plt.subplot(gs[2, 2])
plt.plot(x, s)

plt.show()

print('------------------------------------------------------------')	#60個

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
ax0.hist(x, 5, histtype='stepfilled', facecolor='g', alpha=0.75)

ax0.set_title('stepfilled\n' + r'$\mu = 200, \sigma=25$')

# 自定分組，縱軸執行正規化處理表示為機率，直條的寬度大小為 80%
bins = [100, 150, 180, 195, 205, 220, 250, 300]

ax1.hist(x, bins, histtype='bar', rwidth=0.8)

ax1.set_title('unequal bins\n' + r'$\mu = 200, \sigma=25$')

# 緊密排列，並填滿原圖大小
fig.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

