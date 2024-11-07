print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
# 電影打分資料MovieLens中讀入使用者資料

import pandas as pd
columns = 'user_id', 'age', 'sex', 'occupation', 'zip_code'
df = pd.read_csv("data/ml-100k/u.user", 
                 delimiter="|", header=None, names=columns)
print(df.head())

""" fail
#%fig=使用Pandas統計電影打分使用者的職業
df.groupby("occupation").age.mean().order().plot(kind="bar", figsize=(12, 4));
"""

print("------------------------------------------------------------")  # 60個

"""
在下面的實例中，讀入圖形moon.jpg，並轉為二值圖形。
找到二值圖中黑白區域相交的邊線，並計算其周長和面積。
然後透過這兩個參數計算pi。

"""

import cv2

img = cv2.imread("data/moon.jpg", cv2.IMREAD_GRAYSCALE)
_, bimg = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
contour, _ = cv2.findContours(bimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
contour = cv2.approxPolyDP(contour[0], epsilon=2, closed=False)
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour, True)
cc = perimeter**2 / (4 * area)
print(cc)

print("------------------------------------------------------------")  # 60個

#%figonly=使用`ogrid`計算二元函數的曲面
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pylab as pl

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x**2 - y**2)

fig = pl.figure(figsize=(15, 5))
ax = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="coolwarm", linewidth=0.2)

plt.show()

print("------------------------------------------------------------")  # 60個

def normal_pdf(mean, var, x):
    return 1 / np.sqrt(2 * np.pi * var) * np.exp(-(x - mean) ** 2 / (2 * var))

np.random.seed(42)
data = np.random.normal(0, 2.0, size=10)
mean, var = np.mean(data), np.var(data)
var_range = np.linspace(max(var - 4, 0.1), var + 4, 100)

p = normal_pdf(mean, var_range[:, None], data)
p = np.product(p, axis=1) 

#%fig=偏樣本方差位於似然估計曲線的最大值處
import pylab as pl
pl.plot(var_range, p)
pl.axvline(var, 0, 1, c="r")
pl.show()

print("------------------------------------------------------------")  # 60個

foldername = 'C:/_git/vcs/_1.data/______test_files1/__pic//_scenery'

import glob
import numpy as np
from cv2 import imread, imwrite

imgs = []
for fn in glob.glob(foldername + "/*.jpg"):
    print(fn)
    imgs.append(imread(fn, -1))

length = len(imgs)
print(length)
"""
for i in range(length):
    print(imgs[i].shape)
"""



df = pd.DataFrame(np.random.randint(0, 100, (10, 4)), columns=["A", "B", "C", "D"])

"""
from scpy2.common import GraphvizMPLTransform
import pylab as pl
fig = pl.figure()

#%dot GraphvizMPLTransform.graphviz(fig.transFigure)
"""

from sympy import symbols, solve
a, b, c, x = symbols("a,b,c,x")

cc =  solve(a * x ** 2 + b * x + c, x)
print(cc)



'''
print("------------------------------------------------------------")  # 60個










print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



