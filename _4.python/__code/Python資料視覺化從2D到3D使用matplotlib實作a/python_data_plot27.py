"""

第27章：繪製幾何圖形

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_1.py

# ch27_1.py
import matplotlib.pyplot as plt

figure, axes = plt.subplots()  # 建立子圖物件
circle = plt.Circle((0.5, 0.5), 0.4)  # 繪製圓
axes.set_aspect("equal")  # 設定座標單位長度相同
axes.add_artist(circle)  # 將物件加入圖表物件
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_2.py

# ch27_2.py
import matplotlib.pyplot as plt

figure, axes = plt.subplots()  # 建立子圖物件
circle = plt.Circle((0.5, 0.5), 0.4, fill=False, linewidth=3, edgecolor="m")  # 繪製圓
axes.set_aspect("equal")  # 設定座標單位長度相同
plt.gcf().gca().add_artist(circle)  # 將物件加入圖表物件
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_3.py

# ch27_3.py
import matplotlib.pyplot as plt

figure, axes = plt.subplots()  # 建立子圖物件
circle = plt.Circle((0.5, 0.5), 0.4, fill=False, linewidth=3, edgecolor="m")  # 繪製圓
axes.set_aspect("equal")  # 設定座標單位長度相同
plt.gca().add_artist(circle)  # 將物件加入圖表物件
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_4.py

# ch27_4.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig, ax = plt.subplots(2, 2)
# 建立 ax[0,0] 內容
circle = Circle((2.5, 2.5), radius=2, facecolor="w", edgecolor="r")
ax[0, 0].add_patch(circle)  # 將circle物件加入ax[0,1]軸物件
ax[0, 0].set_xlim(0, 5)
ax[0, 0].set_ylim(0, 5)
ax[0, 0].set_title("繪製圓")
# 建立 ax[0,1] 內容
rect = ax[0, 1].patch  # 建立patch物件
rect.set_facecolor("m")  # 設定patch物件內部顏色是品紅色
circle = Circle((2.5, 2.5), radius=2, facecolor="lightyellow", edgecolor="r")
ax[0, 1].add_patch(circle)  # 將circle物件加入ax[0,1]軸物件
ax[0, 1].set_xlim(0, 5)
ax[0, 1].set_ylim(0, 5)
ax[0, 1].set_aspect("equal")
ax[0, 1].set_title("繪製圓 + 矩形框, 軸長度單位相同\n自定義軸長度")
# 建立 ax[1,0] 內容
rect = ax[1, 0].patch  # 建立patch物件
rect.set_facecolor("g")  # 設定patch物件內部顏色是綠色
circle = Circle((2.5, 2.5), radius=2, facecolor="lightyellow", edgecolor="r")
ax[1, 0].add_patch(circle)  # 將circle物件加入ax[0,1]軸物件
ax[1, 0].axis("equal")
ax[1, 0].set_title("繪製圓 + 矩形框, 軸長度單位相同\n矩形框內部是綠色")
# 建立 ax[1,1] 內容
rect = ax[1, 1].patch  # 建立patch物件
rect.set_facecolor("b")  # 設定patch物件內部顏色是藍色
circle = Circle((2.5, 2.5), radius=2, facecolor="lightyellow", edgecolor="r")
ax[1, 1].add_patch(circle)  # 將circle物件加入ax[0,1]軸物件
ax[1, 1].axis("equal")
ax[1, 1].set_title("繪製圓 + 矩形框, 軸長度單位相同\n矩形框內部是藍色")
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_5.py

# ch27_5.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.image as img

jk = img.imread("jk.jpg")  # 讀取原始圖像
fig, ax = plt.subplots()  # 建立 axes 軸物件
im = ax.imshow(jk)  # 顯示 jk 影像物件
# 建立剪輯模式
patch = Circle((160, 160), radius=150, transform=ax.transData)
im.set_clip_path(patch)  # 建立剪輯結果
ax.axis("off")  # 關閉軸標記與刻度
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_6.py

# ch27_6.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 建立軸單位長度相同的 axes 軸物件
figure, axes = plt.subplots(subplot_kw={"aspect": "equal"})
center = (0, 0)  # 橢圓中心
width = 4  # 橢圓水平軸直徑
height = 2  # 橢圓垂直軸直徑
ellip = Ellipse(xy=center, width=width, height=height)  # 繪製橢圓
axes.add_artist(ellip)  # 將物件加入軸物件
axes.set_xlim(-3, 3)
axes.set_ylim(-2, 2)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_7.py

# ch27_7.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

angle = 30  # 炫轉角度
angles = np.arange(0, 180, angle)  # 建立角度陣列
# 建立軸單位長度相同的 axes 軸物件
fig, axes = plt.subplots(subplot_kw={"aspect": "equal"})
center = (0, 0)  # 橢圓中心
width = 4  # 橢圓水平軸直徑
height = 2  # 橢圓垂直軸直徑
for angle in angles:  # 繪製系列橢圓
    ellip = Ellipse(center, width, height, angle, facecolor="g", alpha=0.2)
    axes.add_artist(ellip)  # 加入ellip物件
axes.set_xlim(-2.2, 2.2)
axes.set_ylim(-2.2, 2.2)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_8.py

# ch27_8.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

np.random.seed(10)  # 隨機數種子
num = 100  # 建立 100 個橢圓
ells = [
    Ellipse(
        xy=np.random.rand(2) * 10,  # 隨機數產生橢圓中心xy
        width=np.random.rand(),  # 隨機數產生水平軸直徑
        height=np.random.rand(),  # 隨機數產生垂直軸直徑
        angle=np.random.rand() * 360,
    )  # 隨機數產生炫轉角度
    for i in range(num)
]  # 執行 num 次

fig, axes = plt.subplots(subplot_kw={"aspect": "equal"})
# 將橢圓物件加入軸物件, 同時格式化所有橢圓物件
for e in ells:
    axes.add_artist(e)  # 將橢圓物件加入軸物件
    e.set_clip_box(axes.bbox)  # 擷取橢圓
    e.set_alpha(np.random.rand())  # 隨機數產生透明度
    e.set_facecolor(np.random.rand(3))  # 建立隨機數顏色
# 設定顯示空間
axes.set_xlim(0, 10)
axes.set_ylim(0, 10)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_9.py

# ch27_9.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 建立軸單位長度相同的 ax 軸物件
figure, ax = plt.subplots(subplot_kw={"aspect": "equal"})
center = (1, 1)  # 橢圓中心
width = 4  # 橢圓水平軸直徑
height = 2  # 橢圓垂直軸直徑
rect = Rectangle(
    xy=center, width=width, height=height, facecolor="lightyellow", edgecolor="b"
)  # 繪製矩形
ax.add_artist(rect)  # 將物件加入軸物件
ax.set_xlim(0, 6)
ax.set_ylim(0, 4)
plt.show()


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_10.py

# ch27_10.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
img = np.arange(25).reshape(5, 5)  # 建立影像
ax.imshow(img, cmap="Blues")
ax.add_patch(
    Rectangle(
        (0.5, 0.5),  # 矩形 xy
        3,
        3,  # 寬與高
        fc="none",  # 內部顏色
        ec="g",  # 矩形框的顏色
        linestyle="--",  # 線條樣式
        lw=8,
    )
)  # 矩形線寬
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_11.py

# ch27_11.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.image as img

jk = img.imread("jk.jpg")  # 讀取原始圖像
fig, ax = plt.subplots()  # 建立 axes 軸物件
im = ax.imshow(jk)  # 顯示 jk 影像物件
ax.add_patch(
    Rectangle(
        (60, 30), 200, 200, fc="none", ec="g", lw=5  # 矩形 xy  # 寬與高  # 內部顏色  # 矩形框的顏色
    )
)  # 矩形線寬
ax.axis("off")  # 關閉軸標記與刻度
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_12.py

# ch27_12.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch

fig = plt.figure()
ax = fig.add_subplot(111)

rect1 = patch.Rectangle(
    (-150, -200), 400, 150, color="g"  # 矩形 xy  # width, height
)  # 矩形是綠色
rect2 = patch.Rectangle(
    (-100, 10), 400, 200, color="m"  # 矩形 xy  # width, height
)  # 矩形是品紅色
rect3 = patch.Rectangle(
    (-300, -50), 100, 200, color="y"  # 矩形 xy  # width, height
)  # 矩形是淺黃色
ax.add_patch(rect1)  # 將 rect1 加入軸物件
ax.add_patch(rect2)  # 將 rect2 加入軸物件
ax.add_patch(rect3)  # 將 rect3 加入軸物件
plt.xlim([-400, 400])
plt.ylim([-300, 300])
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_13.py

# ch27_13.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch

fig = plt.figure()
ax = fig.subplots()
# 繪製橢圓
xy = (2, 1.5)  # 定義 xy
arc0 = patch.Arc(xy, 2, 1)  # 使用 Arc 繪製橢圓
# 繪製圓弧
arc1 = patch.Arc(
    xy,
    3,
    1.5,  # xy, width, height
    theta1=0,  # 圓弧起始角度
    theta2=120,  # 圓弧結束角度
    ec="g",  # 綠色線
    lw=10,
)  # 線寬是 10
arc2 = patch.Arc(
    xy,
    3,
    1.5,  # xy, width, height
    theta1=120,  # 圓弧起始角度
    theta2=180,  # 圓弧結束角度
    ec="r",  # 紅色線
    linestyle="--",  # 虛線
    lw=5,
)  # 線寬是 5
arc3 = patch.Arc(
    xy,
    3,
    1.5,  # xy, width, height
    theta1=180,  # 圓弧起始角度
    theta2=300,  # 圓弧結束角度
    color="b",  # 藍色線
    lw=10,
)  # 線寬是 10
arc4 = patch.Arc(
    xy,
    3,
    1.5,  # xy, width, height
    theta1=300,  # 圓弧起始角度
    theta2=360,  # 圓弧結束角度
    ec="m",  # 品紅色
    linestyle="-.",  # 虛點線
    lw=5,
)  # 線寬是 5
for arc in (arc0, arc1, arc2, arc3, arc4):
    ax.add_patch(arc)
ax.axis([0, 4, 0, 3])
ax.set_aspect(1)  # 1與'equal'效果相同
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_14.py

# ch27_14.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch

fig = plt.figure()
ax = fig.subplots()
# 繪製楔形, wedge1 使用預設顏色
wedge1 = patch.Wedge(
    (1, 3), 0.6, theta1=0, theta2=270  # center, r  # 楔形第 1 掃描角
)  # 楔形第 2 掃描角

wedge2 = patch.Wedge(
    (1, 1), 0.6, theta1=90, theta2=360, color="r"  # center, r  # 楔形第 1 掃描角  # 楔形第 2 掃描角
)  # 紅色


wedge3 = patch.Wedge(
    (3, 1), 0.6, theta1=180, theta2=90, color="g"  # center, r  # 楔形第 1 掃描角  # 楔形第 2 掃描角
)  # 藍色

wedge4 = patch.Wedge(
    (3, 3),
    0.6,  # center, r
    theta1=270,  # 楔形第 1 掃描角
    theta2=180,  # 楔形第 2 掃描角
    color="m",
)  # 品紅色
ax.add_patch(wedge1)
ax.add_patch(wedge2)
ax.add_patch(wedge3)
ax.add_patch(wedge4)
ax.axis([0, 4, 0, 4])
ax.set_aspect("equal")  #
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_15.py

# ch27_15.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch

fig = plt.figure()
ax = fig.subplots()
# 繪製楔形, wedge1 使用預設顏色
wedge1 = patch.Wedge(
    (1, 3), 0.6, theta1=0, theta2=270  # center, r  # 楔形第 1 掃描角
)  # 楔形第 2 掃描角

wedge2 = patch.Wedge(
    (1, 1), 0.6, theta1=90, theta2=360, color="r"  # center, r  # 楔形第 1 掃描角  # 楔形第 2 掃描角
)  # 紅色


wedge3 = patch.Wedge(
    (3, 1), 0.6, theta1=180, theta2=90, color="g"  # center, r  # 楔形第 1 掃描角  # 楔形第 2 掃描角
)  # 藍色

wedge4 = patch.Wedge(
    (3, 3),
    0.6,  # center, r
    theta1=270,  # 楔形第 1 掃描角
    theta2=180,  # 楔形第 2 掃描角
    color="m",
)  # 品紅色
ax.add_patch(wedge1)
ax.add_patch(wedge2)
ax.add_patch(wedge3)
ax.add_patch(wedge4)
ax.axis([0, 4, 0, 4])
ax.set_aspect("equal")  #
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_16.py

# ch27_16.py
from matplotlib import pyplot as plt
from matplotlib.patches import Arrow

fig = plt.figure()
ax = fig.subplots()

arr1 = Arrow(3, 3, 2, 0)
arr2 = Arrow(3, 3, 0, 1.75, color="g", width=0.6)
arr3 = Arrow(3, 3, -1.5, 0, color="m", width=0.4)
arr4 = Arrow(3, 3, 0, -1, color="r", width=0.2)
ax.add_patch(arr1)
ax.add_patch(arr2)
ax.add_patch(arr3)
ax.add_patch(arr4)
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
ax.grid(True)
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_17.py

# ch27_17.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np

ax = plt.subplot()
xy = np.array([[5, 5], [8, 3], [8, 1], [2, 1], [2, 3]])
poly = patch.Polygon(xy, closed=True, fc="g")
ax.add_patch(poly)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch27\ch27_18.py

# ch27_18.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

circle = patch.Circle((2, 8), 1.5, fc="r")
square = patch.Rectangle((7, 6.5), 2.5, 3, fc="b")
triangle = patch.Polygon(((0.5, 1), (4, 1), (2.2, 3.8)), fc="m")
diamond = patch.Polygon(((5, 2), (7, 5.3), (5, 8.5), (3, 5.3)), fc="g")

fig = plt.figure()
ax = fig.add_subplot(fc="lightyellow", aspect="equal")
# for 迴圈加入外形物件
for shape in (square, circle, triangle, diamond):
    ax.add_artist(shape)  # 加入物件
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set(xlim=(0, 10), ylim=(0, 10))  # 設定顯示區間
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
