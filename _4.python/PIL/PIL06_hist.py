"""

用直方圖分析一張圖片的顏色組成


"""

import os
import sys
import time
import random
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

from PIL import Image
from PIL import ImageDraw

print('------------------------------------------------------------')	#60個

"""
圖像直方圖

我們先來看兩個函數reshape和flatten:

假設我們先生成一個一維數組：

vec=np.arange(15)
print vec

顯示為：

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

如果我們要把這個一維數組，變成一個3*5二維矩陣，我們可以使用reshape來實現

mat= vec.reshape(3,5)
print mat

顯示為

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

現在如果我們返過來，知道一個二維矩陣，要變成一個一維數組，就不能用reshape了，只能用flatten. 我們來看兩者的區別

a1=mat.reshape(1,-1)  #-1表示為任意，讓系統自動計算
print a1
a2=mat.flatten()
print a2

顯示為：

a1:  [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
a2:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

可以看出，用reshape進行變換，實際上變換后還是二維數組，兩個方括號，因此只能用flatten.

我們要對圖像求直方圖，就需要先把圖像矩陣進行flatten操作，使之變為一維數組，然后再進行統計。

一、畫灰度圖直方圖

繪圖都可以調用matplotlib.pyplot庫來進行，其中的hist函數可以直接繪制直方圖。

調用方式：

n, bins, patches = plt.hist(arr, bins=50, density = True, facecolor='green', alpha=0.75)

hist的參數非常多，但常用的就這五個，只有第一個是必須的，后面四個可選

arr: 需要計算直方圖的一維數組

bins: 直方圖的柱數，可選項，默認為10

density: 是否將得到的直方圖向量歸一化。默認為False

facecolor: 直方圖顏色

alpha: 透明度

返回值 ：

n: 直方圖向量，是否歸一化由參數設定

bins: 返回各個bin的區間范圍

patches: 返回每個bin里面包含的數據，是一個list
"""

img=np.array(Image.open(filename).convert('L'))

plt.figure('Peony')
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density = True, facecolor='green', alpha=0.5)

plt.show()

"""
二、彩色圖片直方圖
實際上是和灰度直方圖一樣的，只是分別畫出三通道的直方圖，然后疊加在一起。
"""

src=Image.open(filename)
r, g, b=src.split()

plt.figure('Peony')
array_r = np.array(r).flatten()
plt.hist(array_r, bins=256, alpha=0.5, density = True,facecolor='r',edgecolor='r',stacked=1)
array_g = np.array(g).flatten()
plt.hist(array_g, bins=256, alpha=0.5, density = True, facecolor='g',edgecolor='g',stacked=1)
array_b = np.array(b).flatten()
plt.hist(array_b, bins=256, alpha=0.5, density = True, facecolor='b',edgecolor='b')
plt.show()


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




