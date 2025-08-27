"""
cohort_analysis

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import datetime as dt

# For Machine Learning Algorithm
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"

df = pd.read_excel(filename)

cc = df.head(5)
print(cc)

cc = df.info()
print(cc)

# Check and Clean Missing Data

cc = df.isnull().sum()
print(cc)

df = df.dropna(subset=["CustomerID"])

cc = df.isnull().sum().sum()
print(cc)

# Check & Clean Duplicates Data

cc = df.duplicated().sum()
print(cc)

df = df.drop_duplicates()

cc = df.duplicated().sum()
print(cc)

cc = df.describe()
print(cc)

df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
cc = df.describe()
print(cc)

cc = df.shape
print(cc)

# Let's Make Cohort Analysis


def get_month(x):
    return dt.datetime(x.year, x.month, 1)


df["InvoiceMonth"] = df["InvoiceDate"].apply(get_month)
grouping = df.groupby("CustomerID")["InvoiceMonth"]
df["CohortMonth"] = grouping.transform("min")
cc = df.tail()
print(cc)


def get_month_int(dframe, column):
    year = dframe[column].dt.year
    month = dframe[column].dt.month
    day = dframe[column].dt.day
    return year, month, day


invoice_year, invoice_month, _ = get_month_int(df, "InvoiceMonth")
cohort_year, cohort_month, _ = get_month_int(df, "CohortMonth")

year_diff = invoice_year - cohort_year
month_diff = invoice_month - cohort_month

df["CohortIndex"] = year_diff * 12 + month_diff + 1

# Count monthly active customers from each cohort
grouping = df.groupby(["CohortMonth", "CohortIndex"])
cohort_data = grouping["CustomerID"].apply(pd.Series.nunique)
# Return number of unique elements in the object.
cohort_data = cohort_data.reset_index()
cohort_counts = cohort_data.pivot(
    index="CohortMonth", columns="CohortIndex", values="CustomerID"
)
cc = cohort_counts
print(cc)

# Retention table
cohort_size = cohort_counts.iloc[:, 0]
retention = cohort_counts.divide(
    cohort_size, axis=0
)  # axis=0 to ensure the divide along the row axis
cc = retention.round(3) * 100  # to show the number as percentage
print(cc)

# Build the heatmap
plt.figure(figsize=(15, 8))
plt.title("Retention rates")
sns.heatmap(data=retention, annot=True, fmt=".0%", vmin=0.0, vmax=0.5, cmap="BuPu_r")
plt.show()

# Average quantity for each cohort
grouping = df.groupby(["CohortMonth", "CohortIndex"])
cohort_data = grouping["Quantity"].mean()
cohort_data = cohort_data.reset_index()
average_quantity = cohort_data.pivot(
    index="CohortMonth", columns="CohortIndex", values="Quantity"
)
average_quantity.round(1)
average_quantity.index = average_quantity.index.date

# Build the heatmap
plt.figure(figsize=(15, 8))
plt.title("Average quantity for each cohort")
sns.heatmap(data=average_quantity, annot=True, vmin=0.0, vmax=20, cmap="BuGn_r")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------")  # 30個
