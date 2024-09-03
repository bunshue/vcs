"""
Matplotlib 多圖顯示(subplot()/subplot2grid()/subplots())

plt.subplots()

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

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

print("用plt畫圖")
plt.plot(x, y)
plt.title("用plt畫圖, 一張子圖")

plt.show()

print("------------------------------")  # 60個

print("fig, ax = plt.subplots() 一張子圖, 可以直接換回 plt.plot()")

print("用fig ax畫圖, 一張子圖")
fig, ax = plt.subplots()  # 一張子圖

ax.plot(x, y, label="sin")

ax.set_title("用fig ax畫圖, 一張子圖")
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()

print("------------------------------------------------------------")  # 60個

print("用fig ax畫圖, 一張子圖")
fig, ax = plt.subplots(1, 1)  # 一張子圖

ax.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

print("1 X 2 子圖")

# 兩張子圖，大小為 15x4 inch，dpi 分辨率 為 100 px/inch，故圖大小為 1500x400 px
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4), dpi=100)

fig.suptitle("兩張子圖, ncols = 2")

# ax0 左圖
ax0.plot(x, y)
ax0.set_title("用fig ax畫圖, 兩張子圖")

# ax1 右圖
ax1.plot(x, y)
ax1.set_title("用fig ax畫圖, 兩張子圖")

plt.show()

print("------------------------------------------------------------")  # 60個

print("1 X 2 子圖")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))  # 建立2個子圖
#fig, ax = plt.subplots(1, 2)  # 建立2個子圖 same
#fig, ax = plt.subplots(2)  # 建立2個子圖 same

ax[0].plot(x, y)  # 子圖索引 0
ax[1].plot(x, y)  # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

print("1 X 3 子圖")

fig, ax = plt.subplots(1, 3, figsize=(8, 4))

ax[0].plot(x,y0, label="sin")
ax[1].plot(x,y1, label="cos")
ax[2].plot(x,y2, label="tan")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個

print("3 X 1 子圖")

fig, ax = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle("共享 x 和 y 軸")

ax[0].plot(x, y)
ax[1].plot(x, y)
ax[2].plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

print("2 X 2 子圖")

fig, ax = plt.subplots(nrows=2, ncols=2)  # 建立 2 X 2 子圖
#fig, ax = plt.subplots(2, 2)  # 建立 2 X 2 子圖 #same
fig.suptitle("用fig ax畫圖, 四張子圖")

ax[0, 0].plot(x, y, "r")  # 子圖索引 0,0
ax[0, 1].plot(x, y, "g")  # 子圖索引 0,1
ax[1, 0].plot(x, y, "b")  # 子圖索引 1,0
ax[1, 1].plot(x, y, "y")  # 子圖索引 1,1
ax[0, 0].set_title("子圖[0, 0]")
ax[0, 1].set_title("子圖[0, 1]")
ax[1, 0].set_title("子圖[1, 0]")
ax[1, 1].set_title("子圖[1, 1]")

for a in ax.flat:
    a.set(xlabel="x 軸資料", ylabel="y 軸資料")

# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()

plt.show()

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 繪圖
    Matplotlib有很多種畫法，不同指令也可以達到相同效果 但較好也較全面的姿勢應該是先釐清fig,ax的關係
    step1:設定好fig,ax和subplots數目及figsize
    step2:個別指定每個ax的畫圖種類，例如line plot, bar chart or hist chart…
    step3:個別指定每個ax的屬性，例如label, xlabel, ylabel,xlim,ylim, legend, xticklabels等等
"""

fig, ax = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)

ax[0][0].plot(x, y0, label="Sin(x)")
ax[0][1].plot(x, y0, label="Sin(x)", linewidth=4, color="black")
ax[1][0].plot(x, y0, label="Sin(x)")
ax[1][1].plot(x, y0, label="Sin(x)")

# ax[1][0].set_xticklabels(labels = x, rotation = 45)
# ax[1][1].set_xticklabels(labels = x, rotation = 45)
ax[0][0].grid(True)
# ax[0][0].legend(['legend'], loc = 2)
ax[0][0].plot(x, y1, label="Cos(x)", marker="x", markersize=5, color="r")
ax[0][0].legend(loc=3)
ax[0][0].set_ylim(-1.2, 1.2)

ax[0][0].set_title("(0, 0)")
ax[0][1].set_title("(0, 1)")
ax[1][0].set_title("(1, 0)")
ax[1][1].set_title("(1, 1)")

ax[0][0].set_xlabel("x")
ax[0][1].set_xlabel("x")
ax[1][0].set_xlabel("x")
ax[1][1].set_xlabel("x")

ax[0][0].set_ylabel("y")
ax[0][1].set_ylabel("y")
ax[1][0].set_ylabel("y")
ax[1][1].set_ylabel("y")

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
fig.suptitle("共享 x 和 y 軸")

ax11.plot(x, y)
ax12.plot(x, y)
ax13.plot(x, y)
ax14.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

print("3 X 3 子圖")

fig, ax = plt.subplots(figsize=(12, 8), nrows=3, ncols=3, sharex=True, sharey=True)
fig.suptitle("共享 x 和 y 軸")

ax[0, 0].plot(x, y)
ax[0, 1].plot(x, y)
ax[0, 2].plot(x, y)
ax[1, 0].plot(x, y)
ax[1, 1].plot(x, y)
ax[1, 2].plot(x, y)
ax[2, 0].plot(x, y)
ax[2, 1].plot(x, y)
ax[2, 2].plot(x, y)

ax[2, 2].set_title("subplots", c="b")
ax[2, 2].axis("square")  # 建立矩形子圖

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

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
# ax[1, 1].set_aspect(2)
# ax[1, 1].set_title("設定寬高比是2")
ax[1, 1].set_aspect("equal", "box")
ax[1, 1].set_title("設定寬高比相同")

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()

ax.plot(x, y)

# 設定刻度大小
ax.tick_params(axis="both", labelsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=100)

# 設定刻度大小
ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis([0, 6, -1, 1])

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立字典data
data = {"蘋果": 10, "橘子": 15, "檸檬": 5, "萊姆": 20}
# 取出keys為串列list
names = list(data.keys())
# 取出values為串列list
values = list(data.values())
# 預設字體大小
plt.rc("font", size=6)
# 軸標題字體大小
plt.rc("axes", titlesize=8)
# 軸標籤字體大小
plt.rc("axes", labelsize=6)
# X軸刻度字體大小
plt.rc("xtick", labelsize=6)
# Y軸刻度字體大小
plt.rc("ytick", labelsize=6)

# sharex, sharey 共用X軸, Y軸 刻度
# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
# 將圖分成2列3欄共6個子圖
fig, ax = plt.subplots(2, 3, figsize=(6.4, 4.8), dpi=160, sharex=True, sharey=True)

ax[0][0].bar(names, values, color="red")
ax[0][1].scatter(names, values, color="green")
ax[0][2].plot(names, values, color="cyan")
ax[1][0].bar(names, values, color="magenta")
ax[1][1].scatter(names, values, color="yellow")
ax[1][2].plot(names, values, color="blue")
ax[0][0].set(xlabel="水果", ylabel="數量")
ax[0][1].set(xlabel="水果", ylabel="數量")
ax[0][2].set(xlabel="水果", ylabel="數量")
ax[1][0].set(xlabel="水果", ylabel="數量")
ax[1][1].set(xlabel="水果", ylabel="數量")
ax[1][2].set(xlabel="水果", ylabel="數量")
ax[0][0].set_title("圖1")
ax[0][1].set_title("圖2")
ax[0][2].set_title("圖3")
ax[1][0].set_title("圖4")
ax[1][1].set_title("圖5")
ax[1][2].set_title("圖6")
ax[0][0].grid(True)
ax[0][1].grid(True)
ax[0][2].grid(True)
ax[1][0].grid(True)
ax[1][1].grid(True)
ax[1][2].grid(True)

fig.suptitle("分類繪圖")
plt.show()

print("------------------------------------------------------------")  # 60個

# 準備描點x,y資料
x = np.arange(-10, 10, 0.1)
y1 = x**3
y2 = x**2

# 指定 寬6.4inches, 高4.8inches, 160dpi
# 將圖分成一個子圖
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)

# 畫出y=x**3曲線
ax.plot(x, y1)

# 畫出y=x**2曲線
ax.plot(x, y2)

# 加上X軸刻度範圍-10~10(如果大小顛倒，圖形會左右鏡射)
ax.set_xlim(-10, 10)

# 加上Y軸刻度範圍-1000~1000(如果大小顛倒，圖形會左右鏡射)
ax.set_ylim(-1000, 1000)

# 加上X軸刻度標示 -10,-9,-8,...,10(只有整數),字體大小為預設
ax.set_xticks(np.arange(-10, 11, 1))

# 加上Y軸刻度標示 -1000,-900,...,1000(只有100的倍數),字體大小為預設
ax.set_yticks(np.arange(-1000, 1000, 100))

# 加上X軸標題(靠右對齊x=1.0為X軸最右)
ax.set_xlabel("X軸", horizontalalignment="right", verticalalignment="top", x=1.0)

# 加上Y軸標題(靠上對齊y=1.0為Y軸最上)
ax.set_ylabel("Y軸", horizontalalignment="right", verticalalignment="bottom", y=1.0)
# ax.set(xlabel='X軸', ylabel='Y軸')

ax.grid()  # 加上格線

# 子圖標題
ax.set_title("子圖標題", loc="right")

# figure標題
fig.suptitle("y=x**3&y=x**2")

# 儲存檔案名為test.png
# fig.savefig("tmp_test.png")

# 圖例說明
ax.legend(["y=x**3", "y=x**2"])

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

# pandas plot

"""
    使用plt.subplot2s()做圖
    (2,2): 表示把窗口分成2行2列
    ax1, ax2 代表第一行由左至右的兩個位置(座標(1,1), (1,2))
    ax3, ax4 代表第二行由左至右的兩個位置(座標(2,1), (2,2))
    sharex: 是否共享座標軸X (使用相同座標軸)
    sharey: 是否共享座標軸 (使用相同座標軸)
"""
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
    2, 2, sharex=False, sharey=False, figsize=(12, 8)
)
data = np.arange(1, 10, 0.5)

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data**2)
df3 = pd.DataFrame(data**3)
df4 = pd.DataFrame(data**4)

ax1.plot(df1)
ax2.plot(df2)
ax3.plot(df3)
ax4.plot(df4)

plt.show()

print("------------------------------------------------------------")  # 60個




# 2D random walk
# fig2, ax2 = plt.subplots(num="Figure_2")
# ax2.legend(loc='best')

"""
plt.xlabel('弧度')

ax.set_xlabel('弧度')
"""

print("------------------------------------------------------------")  # 60個

