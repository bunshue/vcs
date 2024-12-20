"""
加州房價
20640筆資料, 8個欄位

用線性迴歸預測加州房價


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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.linear_model import LinearRegression


def show():
    # return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

print("加州房價數據庫 基本數據")

housing = datasets.fetch_california_housing()
print("housing資料型態 :", type(housing))

X = housing.data
y = housing.target

print("所有資料 :")
# many print(housing)

print("看一下資料集的描述")
# many print(housing.DESCR)

print("加州房價資料庫說明資料 :")
# many print(housing["DESCR"])

print("資料集資料 :")
# many print(housing.data)

print("資料集目標/答案/target/y")
print(housing.target)

print("共有 :", len(housing.data), "筆資料")
print("len :", len(housing))  # ??

print("特徵的名稱 :", housing.feature_names)
print("特徵的個數 :", len(housing.feature_names))

print("data shape :", housing.data.shape)
print("target shape :", housing.target.shape)

# 看各個 feature 和房價的闗係圖。

plt.figure(figsize=(8, 8))

for i, feature in enumerate(housing.feature_names):
    print(i, feature)
    plt.subplot(3, 3, i + 1)
    plt.scatter(X[:, i], y, s=1)
    plt.xlabel(feature)
    plt.ylabel("price")
    plt.tight_layout()

show()

print("------------------------------")  # 30個

X = housing.data
y = housing.target

# 特徵的數據是在 .data 中, 現在來建一個 Data Frame。
cal = pd.DataFrame(X, columns=housing.feature_names)
print(cal.head())

print("------------------------------")  # 30個

# 把要預測的房價也放進來。
cal["MEDV"] = y
print(cal.head())

print("------------------------------")  # 30個

# 可以用 seaborn 畫個美美的房價分佈圖。

sns.distplot(cal.MEDV, bins=30)
show()

# 再來可以做一個相關係數矩陣 (Correlation Matrix), 並且畫出 "heat map"。
correlation_matrix = cal.corr().round(2)

sns.set(rc={"figure.figsize": (11.7, 8.27)})

sns.heatmap(correlation_matrix, annot=True)
show()

# 接下來我們把輸入輸出分好
XX = cal.loc[:, "MedInc":"Longitude"].values
yy = cal.MEDV

x_train, x_test, y_train, y_test = train_test_split(XX, yy, test_size=0.2)

linear_regression = LinearRegression()

linear_regression.fit(x_train, y_train)

y_predict = linear_regression.predict(x_test)

# 現在來計算我們預測的成績。
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print("MSE =", mse)
print("R2 =", r2)

# 用很有創意的方法, 把圖給畫出來。

plt.scatter(y_test, y_predict)
plt.xlim(0, 5.5)
plt.ylim(0, 5.5)
plt.plot([0, 5.5], [0, 5.5], "r")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("加州房價數據庫")

housing = datasets.fetch_california_housing()
X = housing.data
y = housing.target

# 為了怕模型 overfit，我們需要把資料分成訓練資料跟測試資料

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

linear_regression = LinearRegression()

linear_regression.fit(x_train, y_train)

y_predict = linear_regression.predict(x_test)

# 為了看看模型是不是學的好棒棒，把「真實的結果」當作 x 座標， 「預測的結果」當作 y 座標描點在圖上
# 為了方便比較，再畫一條對角線當作比較基準！
# (學得好的話，所有的點應該都會在對角線上，表示結果一樣)

plt.scatter(y_test, y_predict)
plt.plot([0, 5], [0, 5], "r")
plt.xlabel("True Price")
plt.ylabel("Predicted Price")
show()

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
