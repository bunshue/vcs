"""

使用 fig, ax = plt.subplots()

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

# import matplotlib

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)

print("------------------------------------------------------------")  # 60個

print("用plt畫圖")
plt.plot(x, np.sin(x), "r-o", label = "sin")
plt.plot(x, np.cos(x), "g-o", label = "cos")
plt.title("用plt畫圖, 一張子圖")
plt.legend()

plt.show()

print("fig, ax = plt.subplots() 一張子圖, 可以直接換回 plt.plot()")

print("用fig ax畫圖, 一張子圖")
fig, ax = plt.subplots()  # 一張子圖
ax.plot(x, np.sin(x), "r-o", label = "sin")
ax.plot(x, np.cos(x), "g-o", label = "cos")
ax.set_title("用fig ax畫圖, 一張子圖")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()

print("------------------------------------------------------------")  # 60個

# 兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(15, 4), dpi=100)
fig.suptitle("兩張子圖, ncols = 2", fontsize=16)  # 圖表主標題

# ax0 左圖
ax0.plot(x, np.sin(x), "r-o")
ax0.set_title("用fig ax畫圖, 兩張子圖")

# ax1 右圖
ax1.plot(x, np.cos(x), "g-o")
ax1.set_title("用fig ax畫圖, 兩張子圖")

plt.show()

print("------------------------------------------------------------")  # 60個

print("用fig ax畫圖, 四張子圖")

x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)

fig, ax = plt.subplots(2, 2)  # 建立4個子圖
fig.suptitle("用fig ax畫圖, 四張子圖", fontsize=16)  # 圖表主標題

ax[0, 0].plot(x, y, "r")  # 子圖索引 0,0
ax[0, 0].set_title("子圖[0, 0]")

ax[0, 1].plot(x, y, "g")  # 子圖索引 0,1
ax[0, 1].set_title("子圖[0, 1]")

ax[1, 0].plot(x, y, "b")  # 子圖索引 1,0
ax[1, 0].set_title("子圖[1, 0]")

ax[1, 1].plot(x, y, "y")  # 子圖索引 1,1
ax[1, 1].set_title("子圖[1, 1]")

plt.tight_layout()  # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots(2, 2)  # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title("繪圓形, 看起來像橢圓")

ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis("equal")
ax[0, 1].set_title("寬高比相同, 是圓形")

ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis("equal")
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title("設定寬和高相同區間")

ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
#ax[1, 1].set_aspect(2)
#ax[1, 1].set_title("設定寬高比是2")
ax[1, 1].set_aspect("equal", "box")
ax[1, 1].set_title("設定寬高比相同")

fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# 2D random walk
# fig2, ax2 = plt.subplots(num="Figure_2")
# ax2.legend(loc='best')

"""
plt.xlabel('弧度')

ax.set_xlabel('弧度')
"""


print("------------------------------------------------------------")  # 60個

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

