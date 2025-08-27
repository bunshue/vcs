"""
skimage : scikit-image SciKit (toolkit for SciPy)


"""

import skimage

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


"""
基本圖形的繪制

圖形包括線條、圓形、橢圓形、多邊形等。

1、畫線條

skimage.draw.line(r1,c1,r2,c2)

返回當前繪制圖形上所有點的坐標，如：
rr, cc =skimage.draw.line(1, 5, 8, 2)
表示從（1，5）到（8，2）連一條線，返回線上所有的像素點坐標[rr,cc]
"""

"""
設定線條顏色:
skimage.draw.set_color(img, coords, color)
skimage.draw.set_color(img, [rr, cc], [255, 0, 0]) # 紅色
"""

img = skimage.data.chelsea()
x_st, y_st, x_sp, y_sp = 100, 0, 300, 250
rr, cc = skimage.draw.line(y_st, x_st, y_sp, x_sp)
# img[rr, cc] = 255
skimage.draw.set_color(img, [rr, cc], [0, 0, 255])  # 藍色
plt.imshow(img, plt.cm.gray)
plt.title("draw.line 直線")
plt.show()

"""
3、多邊形
函數格式：skimage.draw.polygon(Y,X)
Y為多邊形頂點的行集合，X為各頂點的列值集合。
"""

img = skimage.data.chelsea()
Y = np.array([0, 100, 200, 200, 100])
X = np.array([50, 100, 100, 0, 0])
rr, cc = skimage.draw.polygon(Y, X)
skimage.draw.set_color(img, [rr, cc], [255, 0, 0])
plt.imshow(img, plt.cm.gray)
plt.title("draw.polygon 多邊形")
plt.show()

"""
我在此處只設置了四個頂點，因此是個四邊形。
4、橢圓
格式：skimage.draw.ellipse(cy, cx, yradius, xradius）
cy和cx為中心點坐標，yradius和xradius代表長短軸。
"""

img = skimage.data.chelsea()
rr, cc = skimage.draw.ellipse(250, 350, 50, 100)
skimage.draw.set_color(img, [rr, cc], [255, 0, 0])
plt.imshow(img, plt.cm.gray)
plt.title("draw.ellipse 橢圓")
plt.show()

"""
5、貝塞兒曲線
格式：skimage.draw.bezier_curve(y1,x1,y2,x2,y3,x3,weight)
y1,x1表示第一個控制點坐標
y2,x2表示第二個控制點坐標
y3,x3表示第三個控制點坐標
weight表示中間控制點的權重，用于控制曲線的彎曲度。
"""

img = skimage.data.chelsea()
rr, cc = skimage.draw.bezier_curve(150, 50, 50, 280, 260, 400, 2)
skimage.draw.set_color(img, [rr, cc], [255, 0, 0])
plt.imshow(img, plt.cm.gray)
plt.title("draw.bezier_curve 貝塞兒曲線")
plt.show()

"""
6、空心圓
和前面的畫圓是一樣的，只是前面是實心圓，而此處畫空心圓，只有邊框線。
格式：skimage.draw.circle_perimeter(yx,yc,radius)
yx,yc是圓心坐標，radius是半徑
"""

img = skimage.data.chelsea()
rr, cc = skimage.draw.circle_perimeter(150, 150, 50)
skimage.draw.set_color(img, [rr, cc], [0, 255, 0])
plt.imshow(img, plt.cm.gray)
plt.title("draw.circle_perimeter 空心圓")
plt.show()

"""
7、空心橢圓
格式：skimage.draw.ellipse_perimeter(cy, cx, yradius, xradius）
cy,cx表示圓心
yradius,xradius表示長短軸
"""

img = skimage.data.chelsea()
rr, cc = skimage.draw.ellipse_perimeter(250, 350, 50, 100)
skimage.draw.set_color(img, [rr, cc], [255, 0, 0])
plt.imshow(img, plt.cm.gray)
plt.title("draw.ellipse_perimeter 空心橢圓")
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
