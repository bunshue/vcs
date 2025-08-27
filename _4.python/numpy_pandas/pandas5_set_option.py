"""
Pandas 之 set_option

"""
print("------------------------------------------------------------")  # 60個

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

print("打印目前的顯示設定")
# pd.describe_option("display")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(np.random.rand(4, 6))

print("顯示資料, 多位小數")
print(df)
# print(df.max())#axis=0 軸0方向取值 垂直
print(df.max(axis=0))  # axis=0 軸0方向取值 垂直
# print(df.max(axis=1))#axis=1 軸1方向取值 水平

print("設定顯示格式, 2位小數, 真實資料不變")

pd.set_option("display.float_format", "{:.2f}".format)
# pd.set_option("display.float_format", "{:4.2g}".format)#設定顯示格式

print("顯示資料, 只顯示2位小數")
print(df)
print(df.max(axis=0))  # axis=0 軸0方向取值 垂直

print("------------------------------------------------------------")  # 60個

print("一個很大的df 100X100")
df = pd.DataFrame(np.random.rand(100, 100))
print("在IDLE上的顯示, 預設最多 10 rows 及 6 columns")
print(df)

print("在IDLE上的顯示, 改成最多 5 rows 及 4 columns")
# 廢棄 pd.set_option("max_columns", 5)
# 廢棄 pd.set_option("max_rows", 4)
pd.options.display.max_rows = 5
pd.options.display.max_columns = 4

print(df)

print("------------------------------------------------------------")  # 60個

print("一個很大的df 100X100")
df = pd.DataFrame(np.random.rand(100, 100))
print("在IDLE上的顯示, 預設最多 10 rows 及 6 columns")
print(df)

print("在IDLE上的顯示, 改成最多 5 rows 及 4 columns")
pd.set_option("display.max_rows", 5)  # 設定最大能顯示 5 rows
pd.set_option("display.max_columns", 4)  # 設定最大能顯示 4 columns

print(df)

print("在IDLE上的顯示, 顯示全部 rows 和 columns")
pd.set_option("display.max_rows", None)  # 设置显示所有列
pd.set_option("display.max_columns", None)  # 设置显示所有列
# many print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# pd.set_option("precision", 2) 此寫法廢棄

pd.set_option("display.width", 4)  # 沒效, 不知何義
pd.set_option("display.show_dimensions", False)
