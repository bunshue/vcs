# matplotlib_新進測試13_前pie後scatter

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import os
import time
import random

print("------------------------------------------------------------")  # 60個

# OK 但搬遷有問題

# 構造數據
edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ["中專", "大專", "本科", "碩士", "其他"]

# 添加修飾的餅圖
explode = [0, 0.1, 0, 0, 0]  # 生成數據，用于突出顯示大專學歷人群
colors = ["#9999ff", "#ff9999", "#7777aa", "#2442aa", "#dd5555"]  # 自定義顏色

# 繪制餅圖

plt.pie(
    x=edu,  # 繪圖數據
    explode=explode,  # 突出顯示大專人群
    labels=labels,  # 添加教育水平標簽
    colors=colors,  # 設置餅圖的自定義填充色
    autopct="%.1f%%",  # 設置百分比的格式，這里保留一位小數
    pctdistance=0.8,  # 設置百分比標簽與圓心的距離
    labeldistance=1.1,  # 設置教育水平標簽與圓心的距離
    startangle=180,  # 設置餅圖的初始角度
    radius=1.2,  # 設置餅圖的半徑
    counterclock=False,  # 是否逆時針，這里設置為順時針方向
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)

plt.show()


print("------------------------------------------------------------")  # 60個

# 構建序列
data1 = pd.Series(
    {"中專": 0.2515, "大專": 0.3724, "本科": 0.3336, "碩士": 0.0368, "其他": 0.0057}
)
print(data1)
data1.name = ""
# 控制餅圖為正圓
plt.axes(aspect="equal")
# plot方法對序列進行繪圖
data1.plot(
    kind="pie",  # 選擇圖形類型
    autopct="%.1f%%",  # 餅圖中添加數值標簽
    radius=1,  # 設置餅圖的半徑
    startangle=180,  # 設置餅圖的初始角度
    counterclock=False,  # 將餅圖的順序設置為順時針方向
    title="失信用戶的受教育水平分布",  # 為餅圖添加標題
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)

plt.show()


print("------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt
from pylab import mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

country = ["美國", "澳洲", "日本", "歐洲", "英國"]
pou = [10543, 2105, 1190, 3346, 980]

plt.pie(pou, labels=country, explode=(0, 0, 0.2, 0, 0), autopct="%1.2f%%")  # 繪製圓餅圖

plt.show()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 50  # 色彩數列的點數
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(N):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2 * np.pi, N)  # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x, y1, c=colors, marker="*")  # 繪製 sine
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker="s")  # 繪製 cos
plt.show()

print("------------------------------------------------------------")  # 60個

points = 30
colorused = ["b", "c", "g", "k", "m", "r", "y"]  # 定義顏色
colors = []  # 建立色彩數列
for i in range(points):  # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1, 11, points)  # 建立 x
y = np.random.randint(1, 11, points)  # 建立 y
size = (points * np.random.rand(points)) ** 2  # 散點大小數列
plt.scatter(x, y, s=size, c=colors)  # 繪製散點
plt.xticks(np.arange(0, 12, step=1.0))  # x 軸刻度
plt.yticks(np.arange(0, 12, step=1.0))  # y 軸刻度
plt.show()

print("------------------------------------------------------------")  # 60個


x = np.linspace(0, 5, 500)  # 含500個元素的陣列
y = 1 - 0.5 * np.abs(x - 2)  # y陣列的變化
plt.scatter(x, y, s=50, c=x, cmap="rainbow")  # 色彩隨 x 軸值變化
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 500)  # 含500個元素的陣列
y = 1 - 0.5 * np.abs(x - 2)  # y陣列的變化
plt.scatter(x, y, s=50, c=y, cmap="rainbow")  # 色彩隨 y 軸值變化
plt.colorbar()  # 色彩條
plt.show()

print("------------------------------------------------------------")  # 60個

num = 100
while True:
    x = np.random.random(100)  # 建立x軸100個隨機數字
    y = np.random.random(100)  # 建立y軸100個隨機數字
    plt.scatter(x, y, s=100, c=x, cmap="brg")  # 繪製散點圖
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")  # 詢問是否繼續
    if yORn == "n" or yORn == "N":  # 輸入n或N則程式結束
        break

print("------------------------------------------------------------")  # 60個


def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])  # 隨機x軸移動值
    xloc = x[index - 1] + x_mov  # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])  # 隨機y軸移動值
    yloc = y[index - 1] + y_mov  # 計算y軸新位置
    x.append(xloc)  # x軸新位置加入串列
    y.append(yloc)  # y軸新位置加入串列


num = 10000  # 設定隨機點的數量
x = [0]  # 設定第一次執行x座標
y = [0]  # 設定第一次執行y座標
while True:
    for i in range(1, num):  # 建立點的座標
        loc(i)
    t = x  # 色彩隨x軸變化
    plt.scatter(x, y, s=2, c=t, cmap="brg")
    plt.axis("off")  # 隱藏座標
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")  # 詢問是否繼續
    if yORn == "n" or yORn == "N":  # 輸入n或N則程式結束
        break
    else:
        x[0] = x[num - 1]  # 上次結束x座標成新的起點x座標
        y[0] = y[num - 1]  # 上次結束y座標成新的起點y座標
        del x[1:]  # 刪除舊串列x座標元素
        del y[1:]  # 刪除舊串列y座標元素

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" fail
#zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = list(zip(X, Y))
print(Z)

plt.scatter(X, Y, s = 50, c = Z)
plt.show()
"""


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""

edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
plt.pie(x = edu, # 繪圖數據
labels = labels, # 添加教育水平標簽
autopct = '%.1f%%' # 設置百分比的格式，這里保留一位小數


# 將橫、縱坐標軸標準化處理，確保餅圖是一個正圓，否則為橢圓
plt.axes(aspect = 'equal')

"""
