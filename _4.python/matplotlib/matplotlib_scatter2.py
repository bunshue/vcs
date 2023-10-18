# scatter 集合
# 散布圖 Scatter Chart

import sys
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

"""
額外設定 s、c 和 cmap，就能根據資料點的數據，對應出指定的顏色，
假設資料的範圍是 0～100，顏色地圖是紅橙黃綠藍，
則 0～20 對應紅色，21～40 對應橙色，
41～60 對應黃色，61～80 對應綠色，81～100 對應藍色。
"""


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,8,26,16,9,17,23,4,14,10]
size = [i * 100 for i in y]         # 放大資料點數據 100 倍，比較容易觀察尺寸
plt.scatter(x, y, s = size, c = size, cmap = 'Set1')  # 使用 Set1 的 colormap
plt.show()



print('------------------------------------------------------------')	#60個

#加上 vmin 和 vmax 的設定，能設定顏色的最大值與最小值
#當數值小於 1000 時，只會顯示紅色，當數值大於 2000 時，只會顯示灰色。

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,8,26,16,9,17,23,4,14,10]
size = [i*100 for i in y]
plt.scatter(x,y,s=size,c=size,cmap='Set1',vmin=1000,vmax=2000)
plt.show()



print('------------------------------------------------------------')	#60個

#多組數據的散布圖
#如果有多組數據需要同時呈現，可以獨立繪製每組散布圖，完成後再使用 show() 的方式顯示散布圖。

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y1 = [11,8,26,16,9,17,23,4,14,10]   # 第一組的 Y 軸數據
s1 = [i*100 for i in y1]            # 將第一組的 Y 軸數據放大 100 倍作為園點尺寸
y2 = [19,29,15,12,21,6,7,8,18,2]    # 第二組的 Y 軸數據
s2 = [i*100 for i in y2]            # 將第二組的 Y 軸數據放大 100 倍作為園點尺寸
plt.scatter(x,y1,s=s1,c='b',alpha=0.5)   # 設定透明度為 0.5
plt.scatter(x,y2,s=s2,c='r',alpha=0.5)   # 設定透明度為 0.5
plt.show()




print('------------------------------------------------------------')	#60個
"""
搭配 NumPy 繪製散布圖

由於 matplotlib 能完美的和 NumPy 整合，
所以能透過 NumPy 強大的處理或產生數據能力，快速產生許多繪圖用的數據，
下方的例子，使用 NumPy 產生每組 10 個共三組 100～2000 隨機數字 y 和 size，
使用 matplotlib 繪製出散布圖 ( 如果不指定顏色，每組數據會自動套用不同的顏色 )。
"""

import matplotlib.pyplot as plt
from numpy import random

x = range(0,10)
y = random.randint(100,2000,size=(3,10))    # 產生 3x10 陣列，內容為 100～2000 隨機數字
size = random.randint(100,2000,size=(3,10)) # 產生 3x10 陣列，內容為 100～2000 隨機數字
for i in range(0,3):
  plt.scatter(x,y[i],s=size[i],alpha=0.5)
plt.show()



print('------------------------------------------------------------')	#60個

#使用 NumPy 隨機數的「常態分佈」產生 500 個數據點，再透過 matplotlib 畫出散布圖。

from numpy import random
import matplotlib.pyplot as plt

x = random.normal(5,50,500)
y = random.normal(5,50,500)
plt.scatter(x,y,alpha=0.5,s=100)
plt.show()




print('------------------------------------------------------------')	#60個




