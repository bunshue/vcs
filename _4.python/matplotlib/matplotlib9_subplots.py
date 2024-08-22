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
'''
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)

print("------------------------------------------------------------")  # 60個

print("用plt畫圖")
plt.plot(x, np.sin(x), "r-o", label="sin")
plt.plot(x, np.cos(x), "g-o", label="cos")
plt.title("用plt畫圖, 一張子圖")
plt.legend()

plt.show()

print("fig, ax = plt.subplots() 一張子圖, 可以直接換回 plt.plot()")

print("用fig ax畫圖, 一張子圖")
fig, ax = plt.subplots()  # 一張子圖
ax.plot(x, np.sin(x), "r-o", label="sin")
ax.plot(x, np.cos(x), "g-o", label="cos")
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
# ax[1, 1].set_aspect(2)
# ax[1, 1].set_title("設定寬高比是2")
ax[1, 1].set_aspect("equal", "box")
ax[1, 1].set_title("設定寬高比相同")

fig.tight_layout()

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
fig, axs = plt.subplots(2, 3, figsize=(6.4, 4.8), dpi=160, sharex=True, sharey=True)

axs[0][0].bar(names, values, color="red")
axs[0][1].scatter(names, values, color="green")
axs[0][2].plot(names, values, color="cyan")
axs[1][0].bar(names, values, color="magenta")
axs[1][1].scatter(names, values, color="yellow")
axs[1][2].plot(names, values, color="blue")
axs[0][0].set(xlabel="水果", ylabel="數量")
axs[0][1].set(xlabel="水果", ylabel="數量")
axs[0][2].set(xlabel="水果", ylabel="數量")
axs[1][0].set(xlabel="水果", ylabel="數量")
axs[1][1].set(xlabel="水果", ylabel="數量")
axs[1][2].set(xlabel="水果", ylabel="數量")
axs[0][0].set_title("圖1")
axs[0][1].set_title("圖2")
axs[0][2].set_title("圖3")
axs[1][0].set_title("圖4")
axs[1][1].set_title("圖5")
axs[1][2].set_title("圖6")
axs[0][0].grid(True)
axs[0][1].grid(True)
axs[0][2].grid(True)
axs[1][0].grid(True)
axs[1][1].grid(True)
axs[1][2].grid(True)
fig.suptitle("分類繪圖", fontsize=20)
plt.show()

print("------------------------------------------------------------")  # 60個

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

print("3圖比較")

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, ax = plt.subplots(1, 3, figsize=(12, 8))

ax[0].plot(x,y0, label="sin")
ax[1].plot(x,y1, label="cos")
ax[2].plot(x,y2, label="tan")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個

f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

"""
Matplotlib 繪圖
    Matplotlib有很多種畫法，不同指令也可以達到相同效果 但較好也較全面的姿勢應該是先釐清fig,ax的關係
    step1:設定好fig,ax和subplots數目及figsize
    step2:個別指定每個ax的畫圖種類，例如line plot, bar chart or hist chart…
    step3:個別指定每個ax的屬性，例如label, xlabel, ylabel,xlim,ylim, legend, xticklabels等等
"""

x = np.linspace(0, 6.28, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)

axs[0][0].plot(x, y1, label="Sin(x)")
axs[0][1].plot(x, y1, label="Sin(x)", linewidth=4, color="black")
axs[1][0].plot(x, y1, label="Sin(x)")
axs[1][1].plot(x, y1, label="Sin(x)")
axs[0][0].set_title("(0, 0)")
axs[0][1].set_title("(0, 1)")
axs[1][0].set_title("(1, 0)")
axs[1][1].set_title("(1, 1)")
axs[0][0].set_xlabel("x_label0")
axs[0][1].set_xlabel("x_label1")
axs[1][0].set_xlabel("x_label2")
axs[1][1].set_xlabel("x_label3")
axs[0][0].set_ylabel("y_label0")
axs[0][1].set_ylabel("y_label1")
axs[1][0].set_ylabel("y_label2")
axs[1][1].set_ylabel("y_label3")
# axs[1][0].set_xticklabels(labels = x, rotation = 45)
# axs[1][1].set_xticklabels(labels = x, rotation = 45)
axs[0][0].grid(True)
# axs[0][0].legend(['legend'], loc = 2)
axs[0][0].plot(x, y2, label="Cos(x)", marker="x", markersize=5, color="r")
axs[0][0].legend(loc=3)
axs[0][0].set_ylim(-1.2, 1.2)

fig.suptitle("Suptitle")

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)  # 建立4個子圖
x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y, "b")  # 子圖索引 0,0
ax[0, 0].set_title("子圖[0, 0]")
ax[0, 1].plot(x, y, "g")  # 子圖索引 0,1
ax[0, 1].set_title("子圖[0, 1]")
ax[1, 0].plot(x, y, "m")  # 子圖索引 1,0
ax[1, 0].set_title("子圖[1, 0]")
ax[1, 1].plot(x, y, "r")  # 子圖索引 1,1
ax[1, 1].set_title("子圖[1, 1]")
fig.suptitle("4個子圖的實作", fontsize=16)  # 圖表主標題

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
ax[1, 1].set_aspect("equal", "box")
ax[1, 1].set_title("設定寬高比相同")

fig.tight_layout()
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
ax[1, 1].set_aspect(2)
ax[1, 1].set_title("設定寬高比是2")

fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, num=100, endpoint=True)
y = np.sin(x)

# 建立 3 x 3 的子圖
fig, axs = plt.subplots(figsize=(12, 8),nrows=3, ncols=3, sharex=True, sharey=True)

axs[0, 0].plot(x,y)
axs[0, 1].plot(x,y)
axs[0, 2].plot(x,y)
axs[1, 0].plot(x,y)
axs[1, 1].plot(x,y)
axs[1, 2].plot(x,y)
axs[2, 0].plot(x,y)
axs[2, 1].plot(x,y)
axs[2, 2].plot(x,y)
axs[2, 2].set_title("subplots", c="b")
axs[2, 2].axis("square")  # 建立矩形子圖

plt.tight_layout()
plt.show()
'''
print("------------------------------------------------------------")  # 60個



fig, ax = plt.subplots(nrows=1,ncols=2) # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(1, 2)            # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2)               # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')
for a in ax.flat:
    a.set(xlabel='x 軸資料', ylabel='y 軸資料')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]')
for a in ax.flat:
    a.set(xlabel='x 軸資料', ylabel='y 軸資料')
# 隱藏內側的刻度標記與標籤
for a in ax.flat:
    a.label_outer()

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
fig, ax = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('共享 x 和 y 軸', fontsize=18)
ax[0].plot(x, y ** 2, 'b--')
ax[1].plot(x, 0.5 * y, 'go')
ax[2].plot(x, y, 'm+')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
y2 = np.cos(x)
# 繪圖
ax.plot(x, y1)
ax.plot(x, y2, 'g', lw='3')

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax1 = plt.subplots(1, 1)
ax2 = ax1.twinx()               # 使用相同的 x 軸
# y1 = sin(x)
x = np.linspace(0, 2*np.pi, 300)
y1 = np.sin(x)
# y2 = cos(x)
y2 = np.cos(x)
# 繪圖
ax1.plot(x, y1)
ax2.plot(x, y2, 'g', lw='3')

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
