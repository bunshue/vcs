"""
opencv 集合 新進2

"""

import cv2

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def show():
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


print("------------------------------------------------------------")  # 60個

# 把照片转换成圆形马赛克效果

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# 首先使用cvtColor()将图像转换为灰度图像，然后使用Canny()找出图像的边缘。

img = cv2.imread("beauty05.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = 255 - cv2.Canny(img_gray, 50, 200)
Image.fromarray(np.hstack((img, edges[:, :, None].repeat(3, axis=2))))

# 非边缘部分可以用大圆填充。用distanceTransform()找到每个白色像素到最近的黑色像素的距离。

from matplotlib.pyplot import get_cmap

dist = cv2.distanceTransform(edges, cv2.DIST_L2, 3)
cmap = get_cmap("viridis")
Image.fromarray(cmap(dist / dist.max(), bytes=True))

# 所有距离中的最大值就是能填充的最大的圆。找到这个最大可填充圆的圆心(cx, cy)和半径radius。

idx = np.argmax(dist)
cy, cx = np.unravel_index(idx, dist.shape)
radius = dist[cy, cx]
cv2.circle(edges, (cx, cy), int(radius), (0, 0, 0, 0), thickness=-1)
Image.fromarray(edges)

"""
下面的find_circiles(filename, n)将图像文件filename转换为n个圆形填充图案。

❶当找到n//2个圆形之后，将开始找到的边缘图案edges_original设置为白色，这样可以继续让圆形填充边缘部分。
❷为了找到每个圆形对应的颜色，需要找到圆形中每个像素的坐标，然后计算原始图像中这些坐标的像素的颜色平均值。
这里通过比较cv2.circle()绘制圆形前后的像素值的差别，找到这些坐标。
"""


def find_circles(filename, n):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = 255 - cv2.Canny(img_gray, 50, 200)
    edges_original = edges.copy()
    circles = []
    for i in range(n):
        if i == n // 2:
            edges[edges_original == 0] = 255  # ❶
        dist = cv2.distanceTransform(edges, cv2.DIST_L2, 3)
        idx = np.argmax(dist)
        cy, cx = map(int, np.unravel_index(idx, dist.shape))
        radius = int(round(dist[cy, cx]))
        edges_old = edges.copy()
        cv2.circle(edges, (cx, cy), radius, (0, 0, 0, 0), thickness=-1)
        color = img[edges_old != edges].mean(0).astype(np.uint8)  # ❷
        circles.append([cx, cy, radius] + color.tolist())
    return dict(width=img.shape[1], height=img.shape[0], circles=circles)


circles = find_circles("beauty05.jpg", 1500)


# 变形动画

# 先将所有的图片的圆形信息保存到JSON文件之中。

from glob import glob
import json

for fn in glob("beauty*.jpg"):
    circles = find_circles(fn, 1500)
    with open(fn.replace(".jpg", ".json"), "w") as f:
        json.dump(circles, f)

data = []
for fn in glob("*.json"):
    with open(fn) as f:
        data.append(json.load(f))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
