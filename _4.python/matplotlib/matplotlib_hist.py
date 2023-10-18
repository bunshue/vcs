# hist 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)

print('以直方圖顯示常態分佈')
x = np.random.randn(N)  #常態分佈數字

n, bins, patches = plt.hist(x, num_bins, facecolor = 'yellow', edgecolor = 'yellow')
print(n)
print(bins)

#第二張圖
plt.subplot(232)

normal_samples = np.random.normal(size = N) # 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples, bins = num_bins)

#第三張圖
plt.subplot(233)

uniform_samples = np.random.uniform(size = N) # 生成 N 組介於 0 與 1 之間均勻分配隨機變數
plt.hist(uniform_samples, bins = num_bins)

#第四張圖
plt.subplot(234)

print('描繪頻率分布圖')

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_onigiri.csv'
dat = pd.read_csv(filename, encoding = 'UTF-8')

# 頻率分布圖
plt.hist(dat['店長'], bins = range(0, 200, 10), alpha = 0.5)
plt.hist(dat['太郎'], bins = range(0, 200, 10), alpha = 0.5)

print('計算平均數、變異數、標準差')

print('店長---------')
print('平均:', np.mean(dat['店長']))
print('變異數:', np.var(dat['店長']))
print('標準差:', np.std(dat['店長']))

print('太郎---------')
print('平均:', np.mean(dat['太郎']))
print('變異數:', np.var(dat['太郎']))
print('標準差:', np.std(dat['太郎']))

#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個


