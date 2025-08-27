"""
LineCollection_曲線集合

"""

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

def show():
    plt.tight_layout()
    plt.show()

print("------------------------------------------------------------")  # 60個

lines = [
    [[100, 0], [195, 70], [158, 180], [42, 180], [5, 70], [100, 0]],
    [[300, 0], [395, 70], [358, 180], [242, 180], [205, 70], [300, 0]],
    [[200, 200], [295, 270], [258, 380], [142, 380], [105, 270], [200, 200]],
]

# print(lines)

# 使用matplotlib.collections顯示大量曲線
from matplotlib import collections as mc

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))  # 1X2 子圖

print("------------------------------")  # 30個

line_collection = mc.LineCollection(lines, colors="r", linewidths=1, alpha=0.8)
ax1.add_collection(line_collection)  # add_collection 只能用 ax

ax1.set_aspect("equal")
ax1.autoscale()
# ax1.axis("off")

print("曲線數 :", len(line_collection.get_paths()))
print("曲線顏色數 :", len(line_collection.get_edgecolors()))

print("------------------------------")  # 30個

polys = mc.PolyCollection(lines, color='r', facecolors="none")
ax2.add_collection(polys)
ax2.set_aspect("equal")
ax2.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Matplotlib 多邊形繪製

對於繪圖而言，多邊形繪製是個常見需求，
想在 Matplotlib 繪製多邊形，
可以透過 matplotlib.collections 的 PolyCollection 收集多邊形頂點
"""

from matplotlib.collections import PolyCollection

ax = plt.gca()

ax.add_collection(
    PolyCollection(
        [
            [[0, 0], [10, 0], [0, 10]],  # 三角形
            [[0, 20], [20, 20], [20, 40], [0, 40]],  # 長方形
        ]
    )
)

ax.add_collection(
    PolyCollection(
        [[[25, 15], [45, 20], [45, 40], [40, 45], [30, 40]]],  # 五邊形
        linewidth=0.1,
        facecolor="red",
        edgecolor="black",
    )
)

ax.set_xlim([0, 50])
ax.set_ylim([0, 50])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Matplotlib 多邊形繪製

來運用多邊形繪製來產生〈NumPy 陣列資料型態〉中的謝爾賓斯基三角形：
"""

from matplotlib.collections import PolyCollection


def sierpinski(n):
    def quotientAndRemainderZero(elem, n):
        quotient = elem // n
        remainder = elem % n
        return quotient & remainder == 0

    quotientAndRemainderZero = np.frompyfunc(quotientAndRemainderZero, 2, 1)

    nums = np.arange(n**2)
    nums = nums[np.where(quotientAndRemainderZero(nums, n))]
    return (nums % n, nums // n)


# 在每個 x, y 建立一個三角形
def tri(x, y):
    return [[x, y], [x + 1, y], [x, y + 1]]


tri = np.frompyfunc(tri, 2, 1)

n = 32
x, y = sierpinski(n)

ax = plt.gca()
ax.add_collection(PolyCollection(tri(x, y)))
ax.set_xlim([0, n])
ax.set_ylim([0, n])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
Matplotlib 多邊形繪製

若要在三維空間繪製多邊形，
可以透過 mpl_toolkits.mplot3d.art3d 的 Poly3DCollection，
例如在〈Matplotlib 三角曲面〉透過六次呼叫 plot_surface 來繪製立方體的範例
"""

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

width = 30
depth = 40
height = 50


def box(width, depth, height):
    faces = Poly3DCollection(
        [
            [[0, 0, 0], [width, 0, 0], [width, depth, 0], [0, depth, 0]],
            [
                [0, 0, height],
                [width, 0, height],
                [width, depth, height],
                [0, depth, height],
            ],
            [[0, 0, 0], [width, 0, 0], [width, 0, height], [0, 0, height]],
            [
                [0, depth, 0],
                [width, depth, 0],
                [width, depth, height],
                [0, depth, height],
            ],
            [[0, 0, 0], [0, depth, 0], [0, depth, height], [0, 0, height]],
            [
                [width, 0, 0],
                [width, depth, 0],
                [width, depth, height],
                [width, 0, height],
            ],
        ]
    )
    faces.set_edgecolor("black")

    ax = plt.axes(projection="3d")
    ax.add_collection3d(faces)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    lim = max(width, depth, height)
    ax.set_xlim([0, lim])
    ax.set_ylim([0, lim])
    ax.set_zlim([0, lim])

    show()


box(width, depth, height)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
Matplotlib 多邊形繪製
既然如此，要用 Poly3DCollection 來繪製正四面體也是可以的：
"""

from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def tetrahedron(width):
    n = width / (2**0.5) * 0.5

    xs = np.array([n, -n, n, -n])
    ys = np.array([n, n, -n, -n])
    zs = np.array([n, -n, -n, n])

    coord = np.dstack((xs, ys, zs))[0]

    faces = Poly3DCollection(
        [coord[[0, 1, 2]], coord[[1, 2, 3]], coord[[2, 3, 0]], coord[[3, 0, 1]]]
    )
    faces.set_edgecolor("black")

    ax = plt.axes(projection="3d")
    ax.add_collection3d(faces)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_xlim([-n, n])
    ax.set_ylim([-n, n])
    ax.set_zlim([-n, n])

    show()


width = 30
tetrahedron(width)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#橢圓集合(EllipseCollection)

from matplotlib import collections as mc

# `EllipseColletion`的`unit`參數：`unit='x'`（左圖）、`unit='xy'`（右圖）
angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
offsets = np.c_[3*np.cos(angles), 2*np.sin(angles)]
angles_deg = np.rad2deg(angles)
widths = np.full_like(angles, 2)
heights = np.full_like(angles, 1)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))  # 1X2 子圖

ellipse_collection0 = mc.EllipseCollection(widths, heights, angles_deg, units="x", array=angles,
                          offsets=offsets, transOffset=axes[0].transData)
axes[0].add_collection(ellipse_collection0)# add_collection 只能用 ax
axes[0].axis((-5, 5, -5, 5))

ellipse_collection1 = mc.EllipseCollection(widths, heights, angles_deg, units="xy", array=angles,
                          offsets=offsets, transOffset=axes[1].transData)
axes[1].add_collection(ellipse_collection1)# add_collection 只能用 ax
axes[1].axis((-5, 5, -5, 5))
#axes[1].set_aspect("equal")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個


