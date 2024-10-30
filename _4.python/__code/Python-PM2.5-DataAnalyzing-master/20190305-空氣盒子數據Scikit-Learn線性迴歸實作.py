"""
20190305-空氣盒子數據Scikit-Learn線性迴歸實作

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

import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("data//200811-201811a.csv")

cc = dataset.describe()
print(cc)

dataset.plot(x="PM25", y="CO", style="o")
plt.title("PM25 vs CO")
plt.xlabel("PM25")
plt.ylabel("CO")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(10, 5))
plt.tight_layout()

seabornInstance.distplot(dataset["PM25"])

plt.show()

print("------------------------------------------------------------")  # 60個

X = dataset["PM25"].values.reshape(-1, 1)
y = dataset["CO"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=101
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)  # training the algorithm

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""

# To retrieve the intercept:
print(regressor.intercept_)

# For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test.flatten(), "Predicted": y_pred.flatten()})
print(df)

print("------------------------------------------------------------")  # 60個

df1 = df.head(25)
df1.plot(kind="bar", figsize=(10, 5))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.scatter(X_test, y_test, color="gray")
plt.plot(X_test, y_pred, color="red", linewidth=2)
plt.show()

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("------------------------------------------------------------")  # 60個

import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("data/200811-201811a.csv")

cc = dataset.describe()
print(cc)

dataset.isnull().any()

dataset = dataset.fillna(method="ffill")

X = dataset[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
].values

y = dataset["PM25"].values

plt.figure(figsize=(10, 5))
plt.tight_layout()
seabornInstance.distplot(dataset["PM25"])
plt.show()

print("------------------------------------------------------------")  # 60個

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""

""" NG
coeff_df = pd.DataFrame(regressor.coef_,X.columns,columns=['Coefficient'])  
print(coeff_df)
"""

y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

df1 = df.head(25)

print(df1)

df1.plot(kind="bar", figsize=(10, 8))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("------------------------------------------------------------")  # 60個

# 2008年11月至2018年11月資料清洗

df = pd.read_csv("data/200811-201811a.csv")

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

# df.dtypes

df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
# df["CO2"] = pd.to_numeric(df.CO2, errors='coerce')
df["O3"] = pd.to_numeric(df.O3, errors="coerce")
df["PM25"] = pd.to_numeric(df.PM25, errors="coerce")
df["Nox"] = pd.to_numeric(df.Nox, errors="coerce")
df["NO"] = pd.to_numeric(df.NO, errors="coerce")
df["NO2"] = pd.to_numeric(df.NO2, errors="coerce")
df["THC"] = pd.to_numeric(df.THC, errors="coerce")
df["NMHC"] = pd.to_numeric(df.NMHC, errors="coerce")
df["CH4"] = pd.to_numeric(df.CH4, errors="coerce")
df["WindSpeed"] = pd.to_numeric(df.WindSpeed, errors="coerce")
df["TEMP"] = pd.to_numeric(df.TEMP, errors="coerce")
df["Humidity"] = pd.to_numeric(df.Humidity, errors="coerce")

# 處理缺失值
df = df.fillna(0)

# 檢查屬性是否已經改變
# df.dtypes

# 存檔至新的CSV
df.to_csv("tmp_200811-201811a.csv", encoding="utf8")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
