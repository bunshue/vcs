"""
海生, 自動把圖畫得比較好看

使用海生數據集 load_dataset

tips

"""

print("------------------------------------------------------------")  # 60個

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print("資料來源 : 內建資料 1 計程車小費資料集EDA")

"""
# 計程車小費資料集EDA
共244筆資料, 7個欄位
"""


df = sns.load_dataset("tips")
cc = df.head(30)
print(cc)


df["log_tip"] = np.log(df["tip"])

# 類別變數轉換為數值
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

# 對小費繪製直方圖
sns.histplot(x="tip", data=df)
plt.title("小費統計")
plt.show()

df["log_tip"] = np.log(df["tip"])
sns.kdeplot(x="log_tip", data=df)
plt.show()

# 散佈圖
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

# 三維散佈圖
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

# joint plot
sns.jointplot(data=df, x="total_bill", y="tip", hue="day")
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

cc = df.day.unique()
print(cc)

# ['Sun', 'Sat', 'Thur', 'Fri']
# Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']

# 觀察週間對小費的影響

sns.barplot(x="day", y="tip", data=df)
plt.xlabel("星期幾")
plt.ylabel("小費")
plt.show()

# 箱型圖
sns.boxplot(x="day", y="tip", data=df)
plt.xlabel("星期幾")
plt.ylabel("小費")
plt.show()

print("繪製pair plot")
sns.pairplot(data=df, height=1)
plt.title("繪製pair plot")
plt.show()

print("熱力圖")
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=0.5)
plt.title("熱力圖")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
