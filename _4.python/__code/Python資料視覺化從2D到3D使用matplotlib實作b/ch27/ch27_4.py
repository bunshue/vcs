# ch27_4.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig,ax = plt.subplots(2,2)
# 建立 ax[0,0] 內容
circle = Circle((2.5,2.5),radius=2,facecolor="w",edgecolor="r")
ax[0,0].add_patch(circle)               # 將circle物件加入ax[0,1]軸物件
ax[0,0].set_xlim(0,5)
ax[0,0].set_ylim(0,5)
ax[0,0].set_title('繪製圓')
# 建立 ax[0,1] 內容
rect = ax[0,1].patch                    # 建立patch物件
rect.set_facecolor("m")                 # 設定patch物件內部顏色是品紅色
circle = Circle((2.5,2.5),radius=2,facecolor="lightyellow",edgecolor="r")
ax[0,1].add_patch(circle)               # 將circle物件加入ax[0,1]軸物件
ax[0,1].set_xlim(0,5)
ax[0,1].set_ylim(0,5)
ax[0,1].set_aspect("equal")
ax[0,1].set_title('繪製圓 + 矩形框, 軸長度單位相同\n自定義軸長度')
# 建立 ax[1,0] 內容
rect = ax[1,0].patch                    # 建立patch物件
rect.set_facecolor("g")                 # 設定patch物件內部顏色是綠色
circle = Circle((2.5,2.5),radius=2,facecolor="lightyellow",edgecolor="r")
ax[1,0].add_patch(circle)               # 將circle物件加入ax[0,1]軸物件
ax[1,0].axis("equal")
ax[1,0].set_title('繪製圓 + 矩形框, 軸長度單位相同\n矩形框內部是綠色')
# 建立 ax[1,1] 內容
rect = ax[1,1].patch                    # 建立patch物件
rect.set_facecolor("b")                 # 設定patch物件內部顏色是藍色
circle = Circle((2.5,2.5),radius=2,facecolor="lightyellow",edgecolor="r")
ax[1,1].add_patch(circle)               # 將circle物件加入ax[0,1]軸物件
ax[1,1].axis("equal")
ax[1,1].set_title('繪製圓 + 矩形框, 軸長度單位相同\n矩形框內部是藍色')
plt.tight_layout()
plt.show()





