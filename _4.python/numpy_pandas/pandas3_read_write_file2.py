"""
使用pandas讀寫檔案

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

# use_pivot_sum

df = pd.read_csv("data\ordersList.csv", encoding="utf-8", header=0)

print(
    df.pivot_table(
        index="品名",
        columns="客戶名稱",
        values="金額",
        fill_value=0,
        margins=True,
        aggfunc="sum",
    )
)

print(
    df.pivot_table(index="品名", columns="客戶名稱", values="金額", fill_value=0, margins=True)
)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
