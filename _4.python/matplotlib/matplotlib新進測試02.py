"""
新進測試

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

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

#柱狀圖參數調整

# 數據
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# 設定圖形大小和分辨率
plt.figure(figsize=(10, 5), dpi=100)

# 繪製柱狀圖並自定義參數
plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.5, hatch='/', width=0.5, label='數據1')

# 設定標題和標籤
plt.title('22柱狀圖示例')
plt.xlabel('類別')
plt.ylabel('值')

# 設定刻度標籤
plt.xticks(categories)
plt.yticks([0, 5, 10, 15, 20, 25])

# 顯示網格線
plt.grid(True)

# 顯示圖例
plt.legend()

# 顯示圖形
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色和樣式
color：設定柱子的顏色，可以是一個顏色或一個顏色列表。
edgecolor：設定柱子邊框的顏色。
linewidth：設定柱子邊框的寬度。
hatch：設定柱子的圖案填充，例如 '/'（斜線），'\\'（反斜線），'|'（垂直線），'-'（水平線）。
柱子的寬度
width：設定柱子的寬度。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
"""

print("------------------------------------------------------------")  # 60個

#散點圖參數調整

# 數據
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [50, 100, 150, 200, 250]
colors = [1, 2, 3, 4, 5]

# 設定圖形大小和分辨率
plt.figure(figsize=(10, 5), dpi=100)

# 繪製散點圖並自定義參數
plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, edgecolor='black', linewidth=1.5, label='數據1')

# 設定標題和標籤
plt.title('44散點圖示例')
plt.xlabel('X軸')
plt.ylabel('Y軸')

# 設定刻度標籤
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 3, 5, 7, 11])

# 顯示網格線
plt.grid(True)

# 顯示圖例
plt.legend()

# 顯示圖形
plt.colorbar()  # 顯示顏色條
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色和樣式
color：設定點的顏色，可以是一個顏色或一個顏色列表。
c：設定點的顏色，可以使用單一顏色或一個數值序列來根據數值著色。
marker：設定標記樣式，例如 'o'（圓點），'s'（正方形），'^'（三角形）。
大小
s：設定點的大小，可以是一個數值或一個數值列表。
透明度
alpha：設定點的透明度，範圍從0（完全透明）到1（完全不透明）。
邊框
edgecolor：設定點的邊框顏色。
linewidth：設定點的邊框寬度。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
"""

print("------------------------------------------------------------")  # 60個

# 繪製餅圖
#plt.pie(sizes, labels=labels, autopct='%1.1f%%')

print("------------------------------------------------------------")  # 60個

"""
autopct='%1.1f%%' 的解釋

autopct 參數用來控制餅圖上顯示的自動百分比標籤。這個參數接受一個字符串格式或一個函數，用來指定如何顯示每個餅圖部分的百分比。

%1.1f：這是一個格式化字符串，用來指定浮點數的格式。

%：這是格式化操作的開始標誌。用來指示如何格式化後面的數值。
1：這表示總共顯示至少1個字符（包括小數點和小數位）。
.1：這表示顯示1位小數。
f：這表示以浮點數格式顯示數值。
%%：這表示一個百分號。由於百分號在格式字符串中有特別的意義，所以需要用兩個百分號來表示一個實際的百分號。
"""
print("------------------------------------------------------------")  # 60個

#圓餅圖參數調整

# 數據
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # 將第二塊分離出來

# 繪製圓餅圖並自定義參數
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

# 設置標題
plt.title('66圓餅圖示例')

# 顯示圖形
plt.show()

print("------------------------------------------------------------")  # 60個

"""
參數說明
顏色
colors：設定各個部分的顏色，可以是一個顏色列表。
起始角度
startangle：設定第一塊的起始角度，以度數為單位。
比例顯示
autopct：設定每塊的比例顯示格式，例如 '%1.1f%%' 表示保留一位小數的百分比。
分離圓餅塊
explode：設定分離圓餅塊的距離，默認為0。如果要將某塊突出顯示，可以設置一個數值列表，其中需要分離的塊設置為大於0的值。
陰影
shadow：設置是否顯示陰影，取值為布林值。
圓餅比例
pctdistance：設定比例文字距離圓心的距離，默認為0.6。
圓形或扁平化
normalize：設置是否將數據標準化，使得總和為1。如果為 False，數據不會被標準化。
圓餅中心空白
wedgeprops：設置圓餅塊的屬性，例如邊框顏色、寬度等。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



# 繪製折線圖並自定義參數
plt.plot(x, y, color='b', linestyle='--', linewidth=2.0, marker='o', markersize=8, markerfacecolor='red', markeredgecolor='blue', label='數據1')

# 設定刻度標籤
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 3, 5, 7, 11])

"""
參數說明
顏色和樣式
color：設定折線的顏色，例如 'r'（紅色），'#00FF00'（綠色）。
linestyle：設定折線的樣式，例如 '-'（實線），'--'（虛線），'-.'（點劃線），':'（點線）。
linewidth：設定折線的寬度，例如 2.0。
標記
marker：設定數據點的標記樣式，例如 'o'（圓點），'s'（正方形），'^'（三角形）。
markersize：設定標記的大小，例如 8。
markerfacecolor：設定標記內部顏色。
markeredgecolor：設定標記邊緣顏色。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
"""

"""
儲存圖表
# 圖片繪製完後，使用? plt.savefig 來儲存圖片
plt.savefig('tmp_plot.png')
"""

