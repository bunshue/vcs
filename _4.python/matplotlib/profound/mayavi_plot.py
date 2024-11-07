"""

使用 mayavi


# pip install mayavi


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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#mlab_plot將Mayavi的場景抓圖內嵌到Notebook中：

from numpy import pi, sin, cos, mgrid

dphi, dtheta = pi/250.0, pi/250.0
[phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)

# View it.
from mayavi import mlab
s = mlab.mesh(x, y, z)
mlab.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 繪制心形隱函數曲面

from mayavi import mlab

x, y, z = np.mgrid[-3:3:100j, -1:1:100j, -3:3:100j]
f = (x**2 + 9.0/4*y**2 + z**2 - 1)**3 - x**2 * z**3 - 9.0/80 * y**2 * z**3
contour = mlab.contour3d(x, y, z, f, contours=[0], color=(1, 0, 0))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
使用Mayavi绘制多为数组下标存取的演示图像。
"""
import numpy as np
from mayavi import mlab

x, y, z = np.mgrid[:6,:7,:8]
c = np.zeros((6, 7, 8), dtype=np.int)
c.fill(1)
k = np.random.randint(2,5,size=(6, 7))

idx_i, idx_j, _ = np.ogrid[:6, :7, :8]
idx_k = k[:,:, np.newaxis] + np.arange(3)
c[idx_i, idx_j, idx_k] = np.random.randint(2,6, size=(6,7,3))

mlab.points3d(x[c>1], y[c>1], z[c>1], c[c>1], mode="cube", scale_factor=0.8, 
    scale_mode="none", transparent=True, vmin=0, vmax=8, colormap="Greys")

mlab.points3d(x[c==1], y[c==1], z[c==1], c[c==1], mode="cube", scale_factor=0.8,
    scale_mode="none", transparent=True, vmin=0, vmax=8, colormap="Greys", opacity = 0.2)
mlab.gcf().scene.background = (1,1,1)

mlab.figure()
x, y, z = np.mgrid[:6,:7,:3]
mlab.points3d(x, y, z, c[idx_i, idx_j, idx_k], mode="cube", scale_factor=0.8, 
    scale_mode="none", transparent=True, vmin=0, vmax=8, colormap="Greys", opacity = 1)
mlab.gcf().scene.background = (1,1,1)
mlab.show()





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



