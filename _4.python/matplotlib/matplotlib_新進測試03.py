# 新進測試03

"""

特殊語法

"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd
import random

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 2 * np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
sin_line, = plt.plot(x, y1, label = "Sin", linestyle = '--')                         
cos_line, = plt.plot(x, y2, label = "Cos", lw = 3)

sin_legend = plt.legend(handles = [sin_line], loc = 1)  # 建立sin圖表物件

plt.gca().add_artist(sin_legend)    # 手動將sin圖例加入圖表

plt.legend(handles = [cos_line], loc = 4)               # 建立cos圖表

plt.show()

print('------------------------------------------------------------')	#60個

data1 = [1, 2, 3, 4, 5, 6, 7, 8]            # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]       # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.figure(1)                               # 建立圖表1              
plt.plot(seq, data1, '-*')                  # 繪製圖表1

plt.figure(2)                               # 建立圖表2
plt.plot(seq, data2, '-o')                  # 以下皆是繪製圖表2

plt.show()

print('------------------------------------------------------------')	#60個

# 新增圖表區
plt.figure()
plt.plot([1,2,3])
# 新增圖表區並設定屬性
plt.figure(figsize=[8,4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(figsize=[8,4])
plt.axes([0,0,0.4,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.5,0,0.4,1])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(figsize=[8,4])
plt.axes([0,0,0.8,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.55,0.1,0.2,0.2])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



