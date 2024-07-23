"""
第28章：表格製作

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

print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch28\ch28_1.py

# ch28_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots()
data = [[100, 300], [400, 600], [500, 700]]  # 定義儲存格資料
column_labels = ["2023年", "2024年"]  # 定義欄位標題
c_colors = ["lightyellow"] * 2  # 定義欄標題顏色
row_labels = ["亞洲", "歐洲", "美洲"]  # 定義列標題
r_colors = ["lightgreen"] * 3  # 定義列標題顏色
ax.table(
    cellText=data,  # 建立表格
    colLabels=column_labels,
    colColours=c_colors,
    rowLabels=row_labels,
    rowColours=r_colors,
    loc="upper left",
)  # 從左邊上方放置表格
ax.axis("off")
ax.set_title("深智軟件銷售表", fontsize=16, color="b")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch28\ch28_2.py

# ch28_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
data = [
    [100, 105, 110, 115],
    [58, 61, 66, 72],
    [69, 70, 79, 82],
    [50, 52, 35, 55],
    [12, 14, 20, 22],
]
columns = ("2022年", "2023年", "2024年", "2025年")
rows = ("海外", "聯合發行", "博客來", "天瓏", "Momo")
# 建立長條圖的漸層色彩值
colors = plt.cm.Greens(np.linspace(0, 0.6, len(data)))
n_rows = len(data)
# 最初化堆疊長條圖資料的垂直位置, [0, 0, 0, 0]
y_bottom = np.zeros(len(columns))
# 繪製堆疊長條圖
index = np.arange(len(columns)) + 0.3
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], width=0.5, bottom=y_bottom, color=colors[row])
    y_bottom = y_bottom + data[row]  # 計算堆疊位置
    cell_text.append(["%1.1f" % (x) for x in y_bottom])
# 反轉色彩和文字標籤, 下方資料在上方出現
colors = colors[::-1]
cell_text.reverse()
# 在長條圖下方建立表格
the_table = plt.table(
    cellText=cell_text,
    rowLabels=rows,
    rowColours=colors,
    colLabels=columns,
    loc="bottom",
)
plt.ylabel("各通路業績表")
plt.yticks(np.arange(0, 500, step=100))
plt.xticks([])  # 隱藏顯示 x 軸刻度
plt.title("深智業績表", fontsize=16, color="b")
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch28\ch28_3.py

# ch28_3.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
data = [
    [100, 105, 110, 115],
    [58, 61, 66, 72],
    [69, 70, 79, 82],
    [50, 52, 35, 55],
    [12, 14, 20, 22],
]

columns = ("2022年", "2023年", "2024年", "2025年")
rows = ("Momo", "天瓏", "博客來", "聯合發行", "海外")

colors = ["r", "g", "b", "m", "orange"]  # 建立色彩
index = np.arange(len(columns)) + 0.3
n_rows = len(data)
# 繪製折線圖圖
for row in range(n_rows):
    plt.plot(index, data[row], color=colors[row])
# 在折線圖下方建立表格
plt.table(
    cellText=data, rowLabels=rows, rowColours=colors, colLabels=columns, loc="bottom"
)
plt.ylabel("各通路業績表")
plt.yticks(np.arange(0, 130, step=10))
plt.xticks([])
plt.title("深智業績表", fontsize=16, color="b")
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
