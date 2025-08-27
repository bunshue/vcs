"""
熱力圖 heatmap 集合

一般 畫 熱力圖
海生 畫 熱力圖

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import seaborn as sns  # 海生, 自動把圖畫得比較好看

print("------------------------------------------------------------")  # 60個

# 熱圖

df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ],
    index=["王小明", "李小美", "陳大同", "林小玉"],
    columns=["國文", "英文", "數學", "自然", "社會"],
)
print("原資料 :\n", df, "\n")

print(type(df))
# sns.set(font="meiryo")
sns.heatmap(df)
# sns.heatmap(df, linewidths=.1, annot=True, fmt="d")
# sns.heatmap(df, linewidths=.5, cmap="coolwarm", fmt="d", annot=True)

plt.show()

print("------------------------------------------------------------")  # 60個

# 熱圖 差別在 index 與 columns

df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ]
)
print("原資料 :\n", df, "\n")

print(type(df))
# sns.set(font="meiryo")
sns.heatmap(df)
# sns.heatmap(df, linewidths=.1, annot=True, fmt="d")
# sns.heatmap(df, linewidths=.5, cmap="coolwarm", fmt="d", annot=True)

plt.show()

print("------------------------------------------------------------")  # 60個

listdata = [
    [15, 13, 10, 13, 15],
    [12, 8, 5, 8, 12],
    [10, 5, 0, 5, 10],
    [12, 8, 5, 8, 12],
    [15, 13, 10, 13, 15],
]

"""
listdata = [[ 1.,          0.91141626,  0.99267261,  0.99020915,  0.12721213,  0.328172,       -0.1305195,  -0.23568907],
            [ 0.91141626,  1.,          0.95445981,  0.9599327,   0.52408571,  0.687798,       0.28900806,  0.18508259],
            [ 0.99267261,  0.95445981,  1.,          0.99982106,  0.24613326,  0.43991025,       -0.00976181, -0.11653121],
            [ 0.99020915,  0.9599327,   0.99982106,  1.,          0.26442422,  0.45681976,       0.009156,   -0.09772227],
            [ 0.12721213,  0.52408571,  0.24613326,  0.26442422,  1.,          0.97869093,       0.96678711,  0.93395042],
            [ 0.328172,    0.687798,    0.43991025,  0.45681976,  0.97869093,  1.,       0.89370463,  0.84066014],
            [-0.1305195,   0.28900806, -0.00976181,  0.009156,    0.96678711,  0.89370463,    1.,          0.99427726],
            [-0.23568907,  0.18508259, -0.11653121, -0.09772227,  0.93395042,  0.84066014, 0.99427726,  1.        ]]
"""

ndarray2d = np.array(listdata)
print(type(ndarray2d))
print(ndarray2d)
print("維度", ndarray2d.ndim)
print("形狀", ndarray2d.shape)
print("數量", ndarray2d.size)

sns.heatmap(ndarray2d, cmap="Reds")
# sns.heatmap(ndarray2d, cmap="coolwarm")
# sns.heatmap(ndarray2d, annot = True)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
