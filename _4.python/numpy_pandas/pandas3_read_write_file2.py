"""
使用pandas讀寫檔案

"""

print("------------------------------------------------------------")  # 60個

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print("------------------------------------------------------------")  # 60個

# use_pivot_sum

import pandas as pd

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
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
