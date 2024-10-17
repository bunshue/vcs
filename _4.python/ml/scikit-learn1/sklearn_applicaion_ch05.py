"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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
print("------------------------------------------------------------")  # 60個

# 簡單線性迴歸
# linear_regression

# OLS 公式
# y = wx + b

# 使用 OLS 公式計算 w、b

# 載入資料集
df = pd.read_csv("./data/population.csv")
print(df)

w = ((df["pop"] - df["pop"].mean()) * df["year"]).sum() / (
    (df["year"] - df["year"].mean()) ** 2
).sum()
b = df["pop"].mean() - w * df["year"].mean()

print(f"w={w}, b={b}")

# 使用NumPy函數polyfit驗算

coef = np.polyfit(df["year"], df["pop"], deg=1)
print(f"w={coef[0]}, b={coef[1]}")

# w=0.061159358661554586, b=-116.35631056117121

# 使用Scikit-Learn LinearRegression類別驗算

from sklearn.linear_model import LinearRegression

X, y = df[["year"]].values, df["pop"].values

lr = LinearRegression()
lr.fit(X, y)
cc = lr.coef_, lr.intercept_
print(cc)

# (array([0.06115936]), -116.3563105611711)

print("使用公式預測2050年人口數")

print(2050 * coef[0] + coef[1])

# 9.02037469501569

print("使用矩陣計算")

import numpy as np

X = df[["year"]].values

# b = b * 1
one = np.ones((len(df), 1))

# 將 x 與 one 合併
X = np.concatenate((X, one), axis=1)

y = df[["pop"]].values

# 求解
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"w={w[0, 0]}, b={w[1, 0]}")

# w=0.06115935866154644, b=-116.35631056115507

print("以Scikit-Learn的房價資料集為例，求解線性迴歸")

# 載入 Boston 房價資料集
with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

print("使用矩陣計算")

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values

# b = b * 1
one = np.ones((X.shape[0], 1))

# 將 x 與 one 合併
X2 = np.concatenate((X, one), axis=1)

# 求解
w = np.linalg.inv(X2.T @ X2) @ X2.T @ y
print(w)

print("以Scikit-Learn的線性迴歸驗證")

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)

print(lr.coef_, lr.intercept_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_02_ linear_regression_boston

# 房價預測

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 載入 Boston 房價資料集

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 觀察資料集彙總資訊
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 直方圖
import seaborn as sns

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
plt.show()

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# 6. 模型訓練

model.fit(X_train_std, y_train)

# 7. 模型評分

# R2、MSE、MAE
y_pred = model.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("權重")
print(model.coef_)

print("偏差(Bias)")
print(model.intercept_)

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(model, "tmp_lr_model.joblib")
joblib.dump(scaler, "tmp_lr_scaler.joblib")

# 10.模型預測

import joblib

# 載入模型與標準化轉換模型
model = joblib.load("tmp_lr_model.joblib")
scaler = joblib.load("tmp_lr_scaler.joblib")

list1 = [0 for _ in range(13)]

list1[0] = 1.7  # 犯罪率
list1[1] = 11.0  # 大坪數房屋比例
list1[2] = 11.0  # 非零售業的營業面積比例
list1[3] = 0  # 是否靠近河岸, 0: "否", 1: "是"
list1[4] = 0.5  # 一氧化氮濃度
list1[5] = 6.0  # 平均房間數
list1[6] = 0.0  # 屋齡(1940年前建造比例)
list1[7] = 3.8  # 與商業區距離
list1[8] = 10.0  # 與高速公路距離
list1[9] = 408.0  # 地價稅
list1[10] = 18.0  # 師生比例
list1[11] = 356.0  # 黑人比例(Bk — 0.63)²
list1[12] = 12.0  # 低下階級的比例

X_new = [list1]
X_new = scaler.transform(X_new)

print(f"### 預測房價：{model.predict(X_new)[0]:.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_04_nonlinear_regression.ipynb

# 以二次迴歸預測世界人口數

import numpy as np
import pandas as pd

# 載入資料集

df = pd.read_csv("./data/population.csv")
X, y = df[["year"]].values, df["pop"].values

# 使用 NumPy polyfit 計算

coef = np.polyfit(X.reshape(-1), y, deg=2)
print(f"y={coef[0]} X^2 + {coef[1]} X + {coef[2]}")

# y=-0.0002668845596210234 X^2 + 1.1420418251266993 X + -1210.2427271938489

# 繪圖

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.scatter(df["year"], y, c="blue", marker="o", s=2, label="實際")

plt.plot(
    df["year"].values,
    (df["year"] ** 2) * coef[0] + df["year"] * coef[1] + coef[2],
    c="red",
    label="預測",
)
plt.legend()
plt.show()


# 使用公式預測2050年人口數

print((2050**2) * coef[0] + 2050 * coef[1] + coef[2])

# 9.360652508533576

# 產生 X 平方項，並與X合併

X_2 = X**2
X_new = np.concatenate((X_2, X), axis=1)
cc = X_new.shape
print(cc)

# (151, 2)

# 使用Scikit-Learn LinearRegression類別驗算

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_new, y)
cc = lr.coef_, lr.intercept_
print(cc)

# (array([-2.66884560e-04,  1.14204183e+00]), -1210.242727194026)

print("使用公式預測2050年人口數")

print((2050**2) * lr.coef_[0] + 2050 * lr.coef_[1] + lr.intercept_)

# 9.36065250853244

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_05_multi_variables_nonlinear_regression

# 多元非線性迴歸

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=300, n_features=2, noise=50)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
plt.rcParams["legend.fontsize"] = 10
ax.plot(X[:, 0], X[:, 1], y, "o", markersize=8, color="blue", alpha=0.5)
plt.title("測試資料")
plt.show()

# 使用 PolynomialFeatures 產生多項式

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)  # 2 次方
X_new = poly.fit_transform(X)  # 轉換
cc = X_new.shape
print(cc)

cc = poly.get_feature_names_out(["x1", "x2"])
print(cc)

print("資料分割")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train_std, y_train)
cc = lr.coef_, lr.intercept_
print(cc)

# 模型評分

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# R2、MSE、MAE
y_pred = lr.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

# R2 = 52.87
# MSE = 3155.4231199414303
# MAE = 45.322099168462366

# 使用原始特徵的模型評分

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

lr = LinearRegression()
lr.fit(X_train_std, y_train)

y_pred = lr.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_06_regression_outlier_effect

# 迴歸缺點

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=20, n_features=1, noise=50)

# 繪圖

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(8, 8))
plt.scatter(X, y, color="blue", alpha=0.5)
plt.title("測試資料")
plt.show()

# 模型訓練

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)
cc = lr.coef_, lr.intercept_
print(cc)

print("製造離群值")

print(y[0])

# 製造離群值
y[0] += 2000

# 模型訓練

from sklearn.linear_model import LinearRegression

lr2 = LinearRegression()
lr2.fit(X, y)
cc = lr2.coef_, lr2.intercept_
print(cc)

# 繪圖比較

from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
plt.scatter(X, y, color="blue", alpha=0.5)

line_X = np.array([-3, 3])
plt.plot(line_X, line_X * lr.coef_ + lr.intercept_, c="green", label="原迴歸線")
plt.plot(line_X, line_X * lr2.coef_ + lr2.intercept_, c="red", label="新迴歸線")
plt.title("測試資料")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_07_regression_vs_time_series

# 迴歸(Regression)與時間序列(Time Series) 比較

import os
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# 載入資料集

df = pd.read_csv("./data/monthly-airline-passengers.csv")
print(df)

# 資料轉換

# 設定為日期的資料型態
df["Date"] = pd.to_datetime(df["Month"])

# 設定日期為 DataFrame 的索引值
df = df.set_index("Date")

# 依照資料內容設定日期的頻率
df.index = pd.DatetimeIndex(df.index.values, freq=df.index.inferred_freq)
# 將原有欄位刪除
df.drop("Month", axis=1, inplace=True)

# 繪圖

plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
plt.show()

# 迴歸(Regression)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

lr = LinearRegression()
# X = df.index.astype(str).map(lambda x:x[:4]+x[5:7]).values.reshape(df.shape[0], -1)
X = np.arange(df.shape[0]).reshape(-1, 1)
y = df["Passengers"]
lr.fit(X, y)
pred = lr.predict(X)
print("MSE =", mean_squared_error(y, pred))

# MSE = 2091.7994339346533

# 實際樣本點
plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
# plt.show()

# 預測迴歸線
plt.plot(df.index, pred)
plt.show()

# 殘差線圖
plt.plot(df.index, np.abs(df["Passengers"] - pred))
plt.show()

# 定態測試(Augmented Dickey–Fuller Test for Stationarity)

from statsmodels.tsa.stattools import adfuller

result = adfuller(df["Passengers"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: 0.8153688792060482
p value: 0.991880243437641
滯後期數(Lags): 13
資料筆數: 130
"""

# 結論：p > 0.05 ==> 非定態

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df["Passengers"], lags=20)
fig.set_size_inches(10, 5)
plt.show()

fig = plot_pacf(df["Passengers"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

# 時間序列(Time Series)

from statsmodels.tsa.arima.model import ARIMA

# 建立時間序列資料
series = df.copy()

# AR(1) 模型訓練
ar = ARIMA(df, order=(1, 0, 0))
model = ar.fit()

# 顯示模型訓練報告
print(model.summary())

cc = model.params
print(cc)

cc = df["Passengers"].mean()
print(cc)

# 繪圖比較實際值與預測值

cc = model.fittedvalues
print(cc)

series["Passengers"].plot(figsize=(12, 6), color="black", linestyle="-", label="實際值")
model.fittedvalues.plot(
    figsize=(12, 6), color="green", linestyle=":", lw=2, label="預測值"
)
plt.legend()
plt.show()

print(f"AR MSE = {(np.sum(model.resid**2) / len(model.resid)):.2f}")

# AR MSE = 1301.63

# 使用迴歸驗證

lr2 = LinearRegression()

# 複製資料
series2 = series.copy()

# 將前一期 y 當作 x
series2["Passengers_1"] = series2["Passengers"].shift(-1)
series2.dropna(inplace=True)
X = series2["Passengers"].values.reshape(series2.shape[0], -1)

# 模型訓練
lr2.fit(X, series2["Passengers_1"])
cc = lr2.coef_, lr2.intercept_
print(cc)

# (array([0.95893198]), 13.705504997522155)

series2["TS"] = model.fittedvalues
series2["LR"] = lr2.coef_ * series["Passengers"] + lr2.intercept_
series2["LR"].plot(color="green", linestyle="-.", lw=2, legend="LR")
series2["TS"].plot(figsize=(12, 6), color="red", linestyle=":", lw=2, legend="TS")
plt.show()

cc = series2[["TS", "LR"]]
print(cc)

# AR(1) 殘差(residual)繪圖

residuals = pd.DataFrame(model.resid)
residuals.plot()
plt.show()

# 資料分割

test_size = 12

from sklearn.model_selection import train_test_split

# 資料分割
X_train, X_test = train_test_split(series, test_size=test_size, shuffle=False)

# 查看陣列維度
cc = X_train.shape, X_test.shape
print(cc)

# 模型訓練、預測與繪圖

# AR(1) 模型訓練
ar_1 = ARIMA(X_train[["Passengers"]], order=(1, 0, 0))
model_1 = ar_1.fit()

# 預測 12 個月
pred = model_1.predict(X_train.shape[0], X_train.shape[0] + test_size - 1)

# 繪圖
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

series["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_1.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
plt.show()

# 改用 SARIMAX (Seasonal ARIMA) 演算法
# 一次差分(First-order Differencing)

df_diff = df.copy()
df_diff["Passengers_diff"] = df_diff["Passengers"] - df_diff["Passengers"].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff"].plot()
plt.show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: -2.8292668241699994
p value: 0.0542132902838255
滯後期數(Lags): 12
資料筆數: 130
"""

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df_diff["Passengers_diff"], lags=20)
fig.set_size_inches(10, 5)
plt.show()

fig = plot_pacf(df_diff["Passengers_diff"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

# 二次差分(Second-order Differencing)

df_diff["Passengers_diff_2"] = df_diff["Passengers_diff"] - df_diff[
    "Passengers_diff"
].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff_2"].plot()
plt.show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff_2"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)
"""
Test Stat: -16.384231542468505
p value: 2.7328918500142407e-29
Lags: 11
Num observations: 130
"""
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df_diff["Passengers_diff_2"], lags=20)
fig.set_size_inches(10, 5)
plt.show()

fig = plot_pacf(df_diff["Passengers_diff_2"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

# SARIMAX

print("到這邊會脫離程式......................")

# 資料分割
X_train, X_test = train_test_split(df_diff, test_size=12, shuffle=False)

# SARIMAX
import statsmodels.api as sm

ar_diff = sm.tsa.statespace.SARIMAX(
    X_train[["Passengers"]], order=(1, 2, 1), seasonal_order=(1, 2, 1, 12)
)
model_diff = ar_diff.fit()

# 預測 12 個月
pred = model_diff.predict(X_train.shape[0], X_train.shape[0] + 12 - 1, dynamic=True)
print(pred)

df_diff["pred"] = np.concatenate((model_diff.fittedvalues.values, pred.values))
cc = df_diff["pred"]
print(cc)

# 繪圖

df_diff["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_diff.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
plt.show()

print(f"SARIMAX MSE = {(np.sum(model_diff.resid**2) / len(model_diff.resid)):.2f}")

# SARIMAX MSE = 427.67

# 結論：SARIMAX 準確率比迴歸高
# 時間序列 MSE： 427， 迴歸 MSE： 2091

from statsmodels.tsa.seasonal import seasonal_decompose

decomp = pd.read_csv("./data/monthly-airline-passengers.csv")
decomp["Date"] = pd.to_datetime(decomp["Month"])
decomp = decomp.set_index("Date")
decomp.index = pd.DatetimeIndex(df.index.values, freq=decomp.index.inferred_freq)
decomp.drop("Month", axis=1, inplace=True)

s_dc = seasonal_decompose(decomp["Passengers"], model="additive")
decomp["SDC_Seasonal"] = s_dc.seasonal
decomp["SDC_Trend"] = s_dc.trend
decomp["SDC_Error"] = s_dc.resid
decomp["SDC_TS"] = s_dc.trend + s_dc.seasonal

print("ddddd")

plt.title("Trend components")
decomp["Passengers"].plot(
    figsize=(12, 6), color="black", linestyle="-", legend="Passengers"
)
decomp["SDC_Trend"].plot(
    figsize=(12, 6), color="blue", linestyle="-.", lw=2, legend="SDC_Trend"
)
decomp["SDC_TS"].plot(figsize=(12, 6), color="green", linestyle=":", lw=2, legend="TS")

plt.show()

# 效應分解(Decomposition)

# Plot the original time series, trend, seasonal and random components
fig, axarr = plt.subplots(4, sharex=True)
fig.set_size_inches(5.5, 5.5)

decomp["Passengers"].plot(ax=axarr[0], color="b", linestyle="-")
axarr[0].set_title("Monthly Passengers")

pd.Series(data=decomp["SDC_Trend"], index=decomp.index).plot(
    color="r", linestyle="-", ax=axarr[1]
)
axarr[1].set_title("Trend component in monthly employment")

pd.Series(data=decomp["SDC_Seasonal"], index=decomp.index).plot(
    color="g", linestyle="-", ax=axarr[2]
)
axarr[2].set_title("Seasonal component in monthly employment")

pd.Series(data=decomp["SDC_Error"], index=decomp.index).plot(
    color="k", linestyle="-", ax=axarr[3]
)
axarr[3].set_title("Irregular variations in monthly employment")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)
fig = plt.xticks(rotation=10)

plt.show()

MSE = (decomp["SDC_Error"] ** 2).sum() / decomp["SDC_Error"].shape[0]
print("MSE=", MSE)

# ('MSE=', 340.80467800107556)

"""
結論：時間序列預測準確率比迴歸高
時間序列 MSE： 340， 迴歸 MSE： 2091
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_08_regularization

# L1、L2 regularization的計算與強度比較

import pandas as pd
import numpy as np

# 權重
W = np.array([-1, 5, 3, -9]).reshape(2, 2)
print(W)

# L1

Lambda = 0.5
L1 = Lambda * np.sum(np.abs(W))
print(L1)

# L2

L2 = Lambda * np.sum(W**2)
print(L2)

# 58.0

print("結論：L2 強度較大")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_09_regularization_housing

# 過度擬合與regularization

import pandas as pd
import numpy as np

# 載入房價資料集

# 載入訓練資料
from sklearn.model_selection import train_test_split

train_df = pd.read_csv("./data/train.csv", index_col="ID")

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 模型訓練與評分

from sklearn.linear_model import LinearRegression, Ridge, Lasso

# 模型訓練
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

print(f"訓練判定係數: {lr_model.score(X_train, y_train)}")
print(f"測試判定係數: {lr_model.score(X_test, y_test)}")

# 模型評分
y_pred = lr_model.predict(X_test)

# 訓練判定係數: 0.7268827869293253
# 測試判定係數: 0.7254687959254533

# 生成新特徵，為舊特徵的平方

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 生成新特徵，為舊特徵的平方
X["crim_2"] = X["crim"] ** 2
X["zn_2"] = X["zn"] ** 2
X["indus_2"] = X["indus"] ** 2
X["chas_2"] = X["chas"] ** 2
X["nox_2"] = X["nox"] ** 2
X["rm_2"] = X["rm"] ** 2
X["age_2"] = X["age"] ** 2
X["dis_2"] = X["dis"] ** 2
X["rad_2"] = X["rad"] ** 2
X["tax_2"] = X["tax"] ** 2
X["ptratio_2"] = X["ptratio"] ** 2
X["black_2"] = X["black"] ** 2
X["lstat_2"] = X["lstat"] ** 2

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 模型訓練與評分

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline

# 建立管線
steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", LinearRegression()),
]
pipeline = Pipeline(steps)

# 模型訓練
pipeline.fit(X_train, y_train)

# 模型評分
print(f"訓練判定係數: {pipeline.score(X_train, y_train)}")
print(f"測試判定係數: {pipeline.score(X_test, y_test)}")

# 訓練判定係數: 1.0
# 測試判定係數: -60.45752231085903

# l2 Regularization or Ridge Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Ridge(alpha=10, fit_intercept=True)),
]

ridge_pipe = Pipeline(steps)
ridge_pipe.fit(X_train, y_train)

# 模型評分
print(f"訓練判定係數: {ridge_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {ridge_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.9411030494647765
# 測試判定係數: 0.8158674422432347

# l1 Regularization or Lasso Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Lasso(alpha=0.3, fit_intercept=True)),
]

lasso_pipe = Pipeline(steps)

lasso_pipe.fit(X_train, y_train)

# 模型評分
print(f"訓練判定係數: {lasso_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {lasso_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.8525646297860277
# 測試判定係數: 0.8367938135279831

print("結論：L1 test score 最高")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
