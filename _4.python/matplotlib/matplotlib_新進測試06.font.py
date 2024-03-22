"""
另法顯示中文
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

listCity = [
    "高雄市",
    "屏東縣",
    "臺東縣",
    "新北市",
    "臺中市",
    "臺北市",
    "臺南市",
    "新竹縣",
    "彰化縣",
    "嘉義縣",
    "雲林縣",
    "桃園市",
    "宜蘭縣",
    "苗栗縣",
    "南投縣",
    "基隆市",
    "花蓮縣",
]

listCount = [12, 24, 11, 11, 18, 8, 16, 11, 18, 8, 11, 9, 54, 40, 31, 10, 9]

# 繪製柱狀圖
font = {"family": "DFKai-SB"}  # 設定柱狀圖可以顯示中文
plt.rc("font", **font)
plt.barh(listCity, listCount, label="農業區")  # 橫向柱狀圖串列數據設定
plt.title("各縣市農場數量")  # 柱狀圖名稱
plt.xlim(0, 60)  # X軸範圍0~60
plt.xlabel("數量")  # X軸名稱
plt.ylabel("縣市")  # Y軸名稱
for y, x in enumerate(listCount):  # 使用迴圈讓柱狀末端顯示各縣市農業區總數
    plt.text(x, y, "%s" % x, ha="center")
plt.legend()  # 圖例(柱狀圖)說明
plt.grid(True)  # 顯示格線

plt.show()  # 顯示繪圖結果


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
