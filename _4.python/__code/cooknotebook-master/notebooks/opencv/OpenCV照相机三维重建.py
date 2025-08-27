"""
OpenCV照相机三维重建

"""

import cv2

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"

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

# OpenCV的照相机三维重建

import pylab as pl
from mpl_toolkits import mplot3d
from itertools import product
from itertools import combinations
from plotlyhelp import init_plotly_online_mode

init_plotly_online_mode()

points = []
vertexs = list(product([-1, 1], [-1, 1], [-1, 1]))
for v1, v2 in combinations(vertexs, 2):
    dist = np.sum(np.subtract(v1, v2) ** 2) ** 0.5
    if dist > 2.1:
        continue
    points.append(np.column_stack([np.linspace(v1[i], v2[i], 10) for i in range(3)]))
points = np.vstack(points)
points = np.array(list(set(tuple(p) for p in points.tolist())))
points = points.T
points *= 100
points[2] += 300


def plot_points(points):
    from plotly.offline import iplot
    import plotly.graph_objs as go

    x, y, z = points[:3]

    trace1 = go.Scatter3d(x=x, y=y, z=z, mode="markers", marker=dict(size=3))

    data = [trace1]
    layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


plot_points(points)

"""
下面是一些帮助函数:
    homogeneous(x)：将坐标转换为齐次坐标
    camera_matrix()：计算照相机的旋转矩阵
    rot_matrix()：使用下面的公式计算旋转矩阵
"""


def homogeneous(x):
    x = np.asarray(x)
    if x.ndim == 1:
        return np.r_[x, 1]
    else:
        return np.vstack([x, np.ones(x.shape[1])])


def camera_matrix(f, cx, cy):
    return np.array([[f, 0, cx], [0, f, cy], [0, 0, 1]], dtype=float)


def plot_pixels(pixels, width=640, height=480):
    fig, ax = pl.subplots()
    ax.set_aspect("equal")
    rect = pl.Rectangle((0, 0), 640, 480, fill=False, ls="--")
    ax.add_patch(rect)
    ax.axis("off")
    ax.plot(pixels[0], pixels[1], "s", ms=1)
    return fig, ax


def rot_matrix(theta, axis):
    c = np.cos(theta)
    s = np.sin(theta)
    m = np.array([[c, -s], [s, c]])
    m2 = np.insert(np.insert(m, axis, 0, axis=0), axis, 0, axis=1)
    m2[axis, axis] = 1
    if axis == 1:
        m2 = m2.T
    return m2


# 下面将点云映射到照相机的照片上。第一个照相机的的旋转偏移矩阵为标准矩阵：

Rt1 = np.column_stack([np.eye(3), np.zeros(3)])
A1 = camera_matrix(300, 320, 240)
A1_inv = np.linalg.inv(A1)
pixels1 = A1 @ Rt1 @ homogeneous(points)
pixels1 /= pixels1[2]
plot_pixels(pixels1)

# 第二个照相机绕Y轴旋转20度，并且在X-Y平面上偏移(-30, -10)。两个照相机的照相机矩阵相同。

Rt2 = np.column_stack([rot_matrix(np.deg2rad(20), 1), [-30, -10, 0]])
print(Rt2)
A2 = A1
A2_inv = np.linalg.inv(A2)
pixels2 = A2 @ Rt2 @ homogeneous(points)
pixels2 /= pixels2[2]
pixels_normal2 = A2_inv @ pixels2
plot_pixels(pixels2)

pixels_normal1 = A1_inv @ pixels1
pixels_normal2 = A2_inv @ pixels2
points4d = cv2.triangulatePoints(Rt1, Rt2, pixels_normal1[:2], pixels_normal2[:2])
points4d /= points4d[-1]
cc = np.allclose(points, points4d[:3])
print(cc)

# Fundamental矩阵和Essential矩阵

F, Fmask = cv2.findFundamentalMat(pixels1[:2].T, pixels2[:2].T, cv2.FM_LMEDS)
cc = np.allclose((pixels2 * (F @ pixels1)).sum(0), 0, atol=1e-3)
print(cc)

E = A2.T @ F @ A1
cc = np.allclose((pixels_normal2 * (E @ pixels_normal1)).sum(0), 0, atol=1e-3)
print(cc)

E2, _ = cv2.findEssentialMat(
    pixels1[:2].T, pixels2[:2].T, 300, (320.0, 240.0), cv2.FM_LMEDS
)
cc = np.allclose((pixels_normal2 * (E @ pixels_normal1)).sum(0), 0, atol=1e-3)
print(cc)

U, S, Vt = np.linalg.svd(E)
W = np.array([0.0, -1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]).reshape(3, 3)
Z = np.array([0, 1, 0, -1, 0, 0, 0, 0, 0]).reshape(3, 3)
R1 = U @ W.T @ Vt
R2 = U @ W @ Vt
tx = U @ Z @ U.T
t1 = tx[[2, 0, 1], [1, 2, 0]]
t2 = -t1

# OpenCV中提供了decomposeEssentialMat(E)实现上述对Essential矩阵的分解运算，它返回两个旋转矩阵和一个偏移向量。

cc = cv2.decomposeEssentialMat(E)
print(cc)

points4d = cv2.triangulatePoints(
    Rt1, np.column_stack([R1, t1]), pixels_normal1[:2], pixels_normal2[:2]
)
points4d /= points4d[-1]
plot_points(points4d)

points4d = cv2.triangulatePoints(
    Rt1, np.column_stack([R1, t2]), pixels_normal1[:2], pixels_normal2[:2]
)
points4d /= points4d[-1]
plot_points(points4d)

points4d = cv2.triangulatePoints(
    Rt1, np.column_stack([R2, t1]), pixels_normal1[:2], pixels_normal2[:2]
)
points4d /= points4d[-1]
plot_points(points4d)

points4d = cv2.triangulatePoints(
    Rt1, np.column_stack([R2, t2]), pixels_normal1[:2], pixels_normal2[:2]
)
points4d /= points4d[-1]
plot_points(points4d)

# recoverPose()可以通过Essential矩阵、两组像素坐标以及照相机矩阵找到正确的旋转矩阵和偏移向量。

ret, R, t, mask = cv2.recoverPose(E, pixels1[:2].T, pixels2[:2].T, A1)
print(R, t)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
