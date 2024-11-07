
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
print("------------------------------------------------------------")  # 60個

# 類別變數編碼
# 測試資料

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)

df.columns = ["color", "size", "price", "classlabel"]
print(df)

# LabelEncoder

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
cc = encoder.fit_transform(df["size"])
print(cc)

cc = encoder.inverse_transform([1, 0, 2])
print(cc)

# Pandas Map

size_mapping = {"XL": 3, "L": 2, "M": 1}

df["size"] = df["size"].map(size_mapping)
print(df)

# OrdinalEncoder

from sklearn.preprocessing import OrdinalEncoder

data = [["Male", 1], ["Female", 3], ["Female", 2]]
encoder = OrdinalEncoder()
cc = encoder.fit_transform(data)
print(cc)

# One Hot Encoding with Pandas

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

cc = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
print(cc)

# pandas v1.5 above
df2 = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
cc = pd.from_dummies(df2[["is_blue", "is_green", "is_red"]], sep="_")
print(cc)

# One-hot Encoding with Scikit-learn

from sklearn.preprocessing import OneHotEncoder

# 測試資料
X = [["Male", 1], ["Female", 3], ["Female", 2]]

# 轉換
encoder = OneHotEncoder(handle_unknown="ignore")
X_new = encoder.fit_transform(X)
cc = X_new.toarray()
print(cc)

# 類別
cc = encoder.categories_
print(cc)

# 還原
cc = encoder.inverse_transform(X_new)
print(cc)

# 指定欄位名稱
cc = encoder.get_feature_names_out(["gender", "group"])
print(cc)

# 完整的表格處理程序

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

# One-hot Encoding
encoder = OneHotEncoder(handle_unknown="ignore")
color_new = encoder.fit_transform(df[["color"]])

# 指定欄位名稱
column_names = encoder.get_feature_names_out(encoder.feature_names_in_)

# 轉換
df_new = pd.DataFrame(color_new.toarray(), columns=column_names)
print(df_new)

# 刪除原欄位 'color'
df.drop(["color"], axis=1, inplace=True)

# 合併表格
df2 = pd.concat([df, df_new], axis=1)
print(df2)

# 存檔
import joblib

joblib.dump(encoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

import yfinance as yf

# 下載每日股價

df_quote = yf.download("1101.TW", start="2020-01-01", end="2022-11-30")
df_quote.tail()

print("轉換為月頻率")

df_quote_new = df_quote.resample("ME").mean()
print(df_quote_new)

print("讀取月營收資料")

df_monthly_sales = pd.read_csv("./data/stock_monthly_sales.csv")
cc = df_monthly_sales.head()
print(cc)

print("轉換日期格式")

df_quote_new = df_quote.reset_index()
df_quote_new.Date = df_quote_new.Date
df_quote_new.Date = df_quote_new.Date.map(lambda x: str(x)[:4] + str(x)[5:7])
print(df_quote_new)

print("合併2個表格")

# 轉換日期資料型態，讓2個表格的日期資料型態一致
df_monthly_sales["年月"] = df_monthly_sales["年月"].astype("str")

# 合併2個表格
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]

# 欄位改名
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
print(df)

print("計算股價與月營收關聯度")

cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("營收公布日期晚一個月")

df_monthly_sales["單月營收"] = df_monthly_sales["單月營收"].shift(-1)
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
df.dropna(inplace=True)

cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RobustScaler

# 測試資料

data = np.array([[1.0, -2.0, 2.0], [-2.0, 1.0, 3.0], [4.0, 1.0, -2.0]])
print(data)

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
cc = scaler.fit_transform(data)
print(cc)

# 驗證

def get_box_plot_data(data, bp):
    rows_list = []

    for i in range(data.shape[1]):
        dict1 = {}
        dict1["label"] = i
        dict1["最小值"] = bp["whiskers"][i * 2].get_ydata()[1]
        dict1["箱子下緣"] = bp["boxes"][i].get_ydata()[1]
        dict1["中位數"] = bp["medians"][i].get_ydata()[1]
        dict1["箱子上緣"] = bp["boxes"][i].get_ydata()[2]
        dict1["最大值"] = bp["whiskers"][(i * 2) + 1].get_ydata()[1]
        print(dict1)
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)


bp = plt.boxplot(data)
get_box_plot_data(data, bp)
print(data)
plt.show()

"""
	label 	最小值 	箱子下緣 	中位數 	箱子上緣 	最大值
0 	0 	-2.0 	-0.5 	1.0 	2.5 	4.0
1 	1 	-2.0 	-0.5 	1.0 	1.0 	1.0
2 	2 	-2.0 	0.0 	2.0 	2.5 	3.0
"""

# 計算中位數、IQR
median1 = np.median(data, axis=0)
scale1 = np.quantile(data, 0.75, axis=0) - np.quantile(data, 0.25, axis=0)
print(median1, scale1)
# 計算 RobustScaler
cc = (data - median1) / scale1
print(cc)

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
