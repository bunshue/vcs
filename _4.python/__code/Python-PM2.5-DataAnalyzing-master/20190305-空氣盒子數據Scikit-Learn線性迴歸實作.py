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

df = pd.read_csv("data/200811-201811a.csv")  # 共有 1447 筆資料
"""
cc = df.head(10)
print(cc)

#資料長度
print(len(df))
print(len(df["PM25"]))

cc = df.info()
print(cc)

cc = df.describe()
print(cc)
"""
plt.scatter(df["PM25"], df["CO"], c='yellow')
plt.scatter(df["PM25"][:100], df["CO"][:100], c='r')
plt.scatter(df["PM25"][100:200], df["CO"][100:200], c='g')
plt.scatter(df["PM25"][200:300], df["CO"][200:300], c='b')

plt.xlabel("PM25")
plt.ylabel("CO")
plt.title("PM25 對比 CO")

plt.show()

print("------------------------------------------------------------")  # 60個

# 使用 distplot() / histplot() 來看PM2.5主要集中的區間
# sns.distplot(df["PM25"])  # deprecated
sns.histplot(df["PM25"])

plt.title("PM25濃度統計")
plt.show()

print("------------------------------------------------------------")  # 60個

X = df["PM25"].values.reshape(-1, 1) # 轉成 1447 X 1
y = df["CO"].values.reshape(-1, 1)  # 轉成 1447 X 1

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

# test_size代表測試組比例。random_state代表設定隨機種子，讓測試結果可被重複

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=101
)  # 訓練組6成, 測試組4成

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 載入線性迴歸，並訓練模型
from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

# 取得截距。如果公式是y=ax+b，b即是截距
print("截距b :", linear_regression.intercept_)

# 取得迴歸係數，並用Data Frame顯示
print("迴歸係數 :", linear_regression.coef_)

# 預測, 使用測試組資料來預測結果
y_pred = linear_regression.predict(X_test)

df = pd.DataFrame({"測試資料": y_test.flatten(), "預測結果": y_pred.flatten()})
#print(df)

print("畫出前 N 筆, 比較實際PM2.5及預測PM2.5的關係")
N = 20
df1 = df.head(N)

plt.figure(figsize=(10, 5))

#df1.plot(kind="bar", figsize=(10, 5)) # 直接把整個df畫出來

x1 = np.arange(len(df1["測試資料"])) - 0.2
x2 = np.arange(len(df1["預測結果"])) + 0.2
plt.bar(x1, df1["測試資料"], width=0.4, ec="none", fc="#e63946")
plt.bar(x2, df1["預測結果"], width=0.4, ec="none", fc="#7fb069")

plt.plot(df1["測試資料"], 'r', label="測試資料")
plt.plot(df1["預測結果"], 'g', label="預測結果")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

#測試組資料來預測結果

plt.scatter(X_test, y_test, color="gray", label="測試資料")
plt.plot(X_test, y_pred, color="red", linewidth=5, label="預測結果")
plt.title("測試資料(灰) 對比 預測結果(紅)")
plt.show()

# 載入迴歸常見的評估指標
from sklearn import metrics
print("評估 測試資料 與 預測結果 的差異")

# Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
cc = metrics.mean_absolute_error(y_test, y_pred)
print("MAE : Mean Absolute Error :", cc)

# Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
cc = metrics.mean_squared_error(y_test, y_pred)
print("MSE : Mean Squared Error :", cc)

# Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
cc = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print("RMS : Root Mean Squared Error :", cc)

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/200811-201811a.csv")
"""
print(df)

cc = df.describe()
print(cc)

cc = df.isnull().any()
print(cc)
"""
df = df.fillna(method="ffill") # 將空值填入, ffill()拿前一個值往下填, 承上
print(df)

y = df["PM25"].values

#sns.distplot(df["PM25"])  # old
sns.histplot(df["PM25"])

plt.title("PM25濃度統計")
plt.show()

print("------------------------------------------------------------")  # 60個

X = df[
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# 訓練組8成, 測試組2成

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 載入線性迴歸，並訓練模型
from sklearn.linear_model import LinearRegression
  
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

""" NG
coeff_df = pd.DataFrame(linear_regression.coef_,X.columns,columns=['Coefficient'])  
print(coeff_df)
"""

y_pred = linear_regression.predict(X_test)

df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})

df1 = df.head(25)
print(df1)

df1.plot(kind="bar", figsize=(10, 8))

plt.show()

# 載入迴歸常見的評估指標
from sklearn import metrics
print("評估 測試資料 與 預測結果 的差異")

# Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
cc = metrics.mean_absolute_error(y_test, y_pred)
print("MAE : Mean Absolute Error :", cc)

# Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
cc = metrics.mean_squared_error(y_test, y_pred)
print("MSE : Mean Squared Error :", cc)

# Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
cc = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print("RMS : Root Mean Squared Error :", cc)

print("------------------------------------------------------------")  # 60個

# 2008年11月至2018年11月資料清洗

df = pd.read_csv("data/200811-201811a.csv")

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
# df.to_csv("tmp_200811-201811a.csv", encoding="utf8")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
plt.figure(figsize=(10, 5))
plt.tight_layout()


plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

"""



pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

