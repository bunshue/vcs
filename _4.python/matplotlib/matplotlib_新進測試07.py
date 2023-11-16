# 新進測試07

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

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

#自訂座標軸的刻度及標籤–xticks()、yticks()

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.title('y = sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)

ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]
labels = ['0°', '90°', '180°', '270°', '360°']
plt.xticks(ticks, labels)

plt.plot(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

#在畫布切出子圖區 , 並繪製內容–add_subplot()

x = np.linspace(0, 2 * np.pi)
y1 = np.sin(x)
y5 = np.cos(x)
y6 = np.tan(x)

fig = plt.figure(figsize=(8, 6))        #整個圖表大小為 8 x 6 英吋
ax1 = fig.add_subplot(2, 3, 1)      #←編號 1 的子圖
ax1.plot(x, y1)

ax5 = fig.add_subplot(2, 3, 5)      #←編號 5 的子圖
ax5.plot(x, y5)

ax6 = fig.add_subplot(2, 3, 6)      #←編號 6 的子圖
ax6.plot(x, y6)

ax3 = fig.add_subplot(2, 3, 3)      #← 編號 3 的子圖

plt.show()

print('------------------------------------------------------------')	#60個

#調整子圖間距

x = np.linspace(0, 2 * np.pi)
y1 = np.sin(x)
y5 = np.cos(x)
y6 = np.tan(x)
fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.75)

for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    if i == 0:  
        ax.plot(x, y1)
    elif i == 4:
        ax.plot(x, y5)
    elif i == 5:    
        ax.plot(x, y6)

plt.show()

print('------------------------------------------------------------')	#60個

#設定子圖的座標範圍、座標說明文字與子圖標題

x = np.linspace(0, 2 * np.pi)
y1 = np.sin(x)
y5 = np.cos(x)
y6 = np.tan(x)

fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.75)
for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    if i == 0:
        ax.set_title('y=sin(x)')
        ax.plot(x, y1)
    elif i == 4:
        ax.set_title('y=cos(x)')
        ax.plot(x, y5)
    elif i == 5:
        ax.set_title('y=tan(x)')
        ax.plot(x, y6)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#設定長條圖橫軸標籤
x = [1, 2, 3, 4, 5, 6]
y = [12, 41, 32, 36, 21, 17]
labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
plt.bar(x, y, tick_label=labels)
plt.show()

print('------------------------------------------------------------')	#60個​

#繪製堆疊長條圖

x = [1, 2, 3, 4, 5, 6]
y1 = [12, 41, 32, 36, 21, 17]
y2 = [43, 1, 6, 17, 17, 9]

labels = ['Apple', 'Orange', 'Banana', 'Pineapple', 'Kiwifruit', 'Strawberry']
plt.bar(x, y1, tick_label=labels)				#繪製 y1 長條圖
plt.bar(x, y2, tick_label=labels, bottom=y1)	#繪製 y2 長條圖

plt.legend(('y1', 'y2'))			#顯示圖例來識別 y1 與 y2
plt.show()

print('------------------------------------------------------------')	#60個

#繪製直方圖

np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins='auto')

plt.show()


np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins='auto', density=True)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個







