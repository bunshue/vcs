"""
violinplot 集合 小提琴圖


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

# 小提琴圖
data = np.random.rand(20, 5)
plt.violinplot(data, showmeans=False, showmedians=True)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35, 38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].set_title("小提琴圖")
ax[0].violinplot(x)
ax[1].set_title("箱線圖")
ax[1].boxplot(x)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35, 38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True)
ax[0].set_title("小提琴圖")
ax[0].violinplot(x, showmedians=True)
ax[1].set_title("箱線圖")
ax[1].boxplot(x)

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
# 建立 200 個均勻分佈的隨機數
uniform = np.arange(-100, 100)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharey=True)
ax[0].set_title("均勻分佈")
ax[0].set_ylabel("觀察值")
ax[0].violinplot(uniform, showmedians=True)
# 建立 200 個常態分佈的隨機數
normal = np.random.normal(size=200) * 35
ax[1].set_title("常態分佈")
ax[1].violinplot(normal, showmedians=True)

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
# 建立 3 組隨機數
data1 = np.random.randint(1, 100, size=100)
data2 = np.random.randint(1, 100, size=100)
data3 = np.random.randint(1, 100, size=100)
dataset = [data1, data2, data3]  # 3 組數據組成 dataset
# 建立圖表物件
fig = plt.figure()
ax = fig.gca()  # 獲得目前圖表物件
vio = plt.violinplot(dataset)  # 建立小提琴圖
for body in vio["bodies"]:  # 小提琴圖區塊
    body.set_facecolor("cyan")  # 內部顏色是 cyan
    body.set_edgecolor("m")  # 邊線顏色是 magenta
    body.set_alpha(0.8)  # 透明度 0.8
ax.set_title("3 組均勻分布的小提琴圖", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
# 建立 1 組隨機數
data = np.random.normal(size=1000)
fig, ax = plt.subplots(nrows=2, ncols=4)
# 建立小提琴圖
ax[0, 0].violinplot(data)
ax[0, 0].set_title("預設小提琴圖", color="m")
ax[0, 1].violinplot(data, widths=[0.2])
ax[0, 1].set_title("重新定義寬度", color="m")
ax[0, 2].violinplot(data, vert=False)
ax[0, 2].set_title("水平小提琴圖", color="m")
ax[0, 3].violinplot(data, positions=[3])
ax[0, 3].set_title("重新定義位置", color="m")
ax[1, 0].violinplot(data, showextrema=False)
ax[1, 0].set_title("隱藏極值", color="m")
ax[1, 1].violinplot(data, showmeans=True)
ax[1, 1].set_title("顯示均值", color="m")
ax[1, 2].violinplot(data, showmedians=True)
ax[1, 2].set_title("顯示中位數", color="m")
ax[1, 3].violinplot(data, quantiles=[0.25, 0.5, 0.75])
ax[1, 3].set_title("顯示分位數", color="m")
plt.suptitle("8 組均勻分布的小提琴圖", fontsize=16, color="b")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# 建立測試資料
np.random.seed(10)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
# 建立子圖
fig, axes = plt.subplots()
axes.set_title("設計小提琴圖", fontsize=16, color="b")
parts = axes.violinplot(data, showmeans=False, showmedians=False)
# 建立小提琴圖
for p in parts["bodies"]:
    p.set_facecolor("red")
    p.set_edgecolor("black")
    p.set_alpha(1)
# 獲得小提琴圖最大值
wseg = parts["cmaxes"].get_segments()  # 小提琴圖最大值線段
w_max = []  # 設定最大值串列
for i in range(len(wseg)):
    upper_array = wseg[i]
    for j in range(0, len(upper_array), 2):
        w_max.append(upper_array[j][1])  # 取得最大值 y 軸值
# 獲得小提琴圖最小值
wseg = parts["cmins"].get_segments()  # 小提琴圖最大值線段
c_min = []  # 設定最大值串列
for i in range(len(wseg)):
    lower_array = wseg[i]
    for j in range(0, len(lower_array), 2):
        c_min.append(lower_array[j][1])  # 取得最小值 y 軸值
# 繪製小提琴內部
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
inds = np.arange(1, len(medians) + 1)
axes.scatter(inds, medians, marker="*", color="white", s=30, zorder=3)
axes.vlines(inds, quartile1, quartile3, color="b", linestyle="-", lw=5)
axes.vlines(inds, c_min, w_max, color="b", linestyle="-", lw=1)
# 設定 x 軸
labels = ["A", "B", "C", "D"]
axes.set_xticks(np.arange(1, len(labels) + 1))
axes.set_xticklabels(labels=labels)
axes.set_xlim(0.25, len(labels) + 0.75)
axes.set_xlabel("數據樣本", fontsize=12, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


