"""
機器學習：建立線性迴歸資料與預測

線性迴歸（linear regression)
    Finding the curve that best fits your data is called regression, and when that curve is a straight line, it's called linear regression.
    找出符合資料規律的直線，就叫線性迴歸。

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

建立迴歸資料 make_regression
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

from sklearn import linear_model

import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度
from sklearn.metrics import accuracy_score  # 沒用到

print("------------------------------------------------------------")  # 60個


# 迴歸效果評估
def evaluate_result(y_test, y_pred):
    print("真實資料(y_test) :", y_test)
    print("預測資料(y_pred) :", y_pred)

    print("計算 真實測試資料(y_test) 和 預測資料(y_pred)的 MSE")
    mse = np.sum((y_test - y_pred) ** 2) / len(y_test)
    print("MSE =", mse)

    # 平均絕對誤差 Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
    cc = mean_absolute_error(y_test, y_pred)
    print("MAE : Mean Absolute Error :", cc)

    # 均方誤差 Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
    mse = mean_squared_error(y_test, y_pred)
    print("MSE : Mean Squared Error :", mse)

    # Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
    cc = np.sqrt(mean_squared_error(y_test, y_pred))
    print("RMS : Root Mean Squared Error :", cc)

    print("計算 真實測試資料(y_test) 和 預測資料(y_pred) 的 決定係數r2 r2_score")
    r2 = r2_score(y_test, y_pred)
    print(f"決定係數R2 = {r2:.4f}")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 簡單資料 y = x
xx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yy0 = xx  # 理想資料, y = x
yy1 = np.array([0, 1, 4, 3, 4, 5, 6, 3, 8, 9, 10])  # 真實資料

"""
# 複雜資料 f(x) = sin(3.2x) + 0.8x
N = 50
xx = np.linspace(0, 5, N)
yy0 = np.sin(3.2 * x) + 0.8 * x
yy1 = np.sin(3.2 * x) + 0.8 * x + 0.3 * np.random.randn(N)
"""
print("------------------------------------------------------------")  # 60個
"""
print("資料來源 : 建立迴歸資料 make_regression 1 無 / 有 資料分割")

N = 100
X, y = datasets.make_regression(n_samples=N, n_features=1, n_targets=1, noise=10)
# X, y = datasets.make_regression(n_samples=N, n_features=1, noise=10)
# N個樣本, 1種特徵(features), 1種標籤類別(target), noise為分散程度

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# 全部資料, 訓練預測畫圖
linear_regression.fit(X, y)  # 學習訓練.fit
y_pred = linear_regression.predict(X)  # 預測.predict
plt.scatter(X, y, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(X, y_pred, c="r", label="線性迴歸")
plt.legend()
plt.show()

print("資料分割")
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 分割資料, 訓練預測畫圖
linear_regression.fit(x_train, y_train)  # 學習訓練.fit
y_pred = linear_regression.predict(x_test)  # 預測.predict
plt.scatter(X, y, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(x_test, y_pred, c="r", label="線性迴歸")
plt.legend()
plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print("資料來源 : 自建資料 2 做成df")

xxx = xx
yyy = yy1

X = pd.DataFrame(xxx, columns=["XXX"])  # DataFrame

target = pd.DataFrame(yyy, columns=["YYY"])
y = target["YYY"]  # Series

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測 或 部分預測
x_test = pd.DataFrame(np.array([1, 3, 5, 7, 9]), columns=["XXX"])  # DataFrame

y_pred = linear_regression.predict(x_test)  # 預測.predict, 傳入df

plt.scatter(xxx, yyy, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(x_test, y_pred, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 4 做成df, 一維資料 線性迴歸")

datas = np.array([147.9, 163.5, 159.8, 155.1, 163.3, 158.7, 172.0, 161.2, 153.9, 161.6])
targets = np.array([41.7, 60.2, 47.0, 53.2, 48.3, 55.2, 58.5, 49.0, 46.7, 52.5])

X = pd.DataFrame(datas, columns=["第一欄"])

target = pd.DataFrame(targets, columns=["目標"])
y = target["目標"]

print(X, y)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict
print(y_pred)

plt.scatter(datas, targets, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(X["第一欄"], y_pred, color="r", marker="o", markersize=8, label="線性迴歸")

plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 5 做成df, 二維資料 線性迴歸")

datas = np.array(
    [
        [67, 160],
        [68, 165],
        [70, 167],
        [65, 170],
        [80, 165],
        [85, 167],
        [78, 178],
        [79, 182],
        [95, 175],
        [89, 172],
    ]
)
targets = np.array([50, 60, 65, 65, 70, 75, 80, 85, 90, 81])

X = pd.DataFrame(datas, columns=["第一欄", "第二欄"])
target = pd.DataFrame(targets, columns=["目標"])
y = target["目標"]
print(X, y)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

# 預測 第一欄 和 第二欄 [66,164],[82,172] 的 目標
# new_df = pd.DataFrame(np.array([[66, 164], [82, 172]]), columns=["第一欄", "第二欄"])
# y_pred = linear_regression.predict(new_df)  # 預測.predict

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict
print(y_pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7a")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列
# y1 = y1.reshape(len(y1), 1) 可以不用

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y1)  # 學習訓練.fit

y_pred = linear_regression.predict(X)  # 預測.predict

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線

plt.title("線性迴歸 無 資料分割")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7b 資料分割")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料


# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    x, y1, test_size=0.2, random_state=9487
)  # 訓練組8成, 測試組2成


X_train = x_train.reshape(len(x_train), 1)  # x訓練資料要轉為 NX1 陣列
X_test = x_test.reshape(len(x_test), 1)  # x測試資料要轉為 NX1 陣列

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test)  # 預測.predict

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.scatter(x_train, y_train, s=100, c="b", label="真實資料(訓練組)")  # 真實資料
plt.scatter(x_test, y_test, s=300, c="m", label="真實資料(測試組)")  # 真實資料
plt.plot(x_test, y_pred, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線

plt.title("線性迴歸 + 資料分割")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------")  # 30個

# 有x測試資料預測到的結果和真實y測試資料比對

X_test = x_test.reshape(len(x_test), 1)  # x測試資料要轉為 NX1 陣列

y_pred = linear_regression.predict(X_test)  # 預測.predict

print("評估 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7c SVR(linear) 迴歸")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料
X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列

# 迴歸, 用 sklearn 裡的 SVR 的 linear 來做迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

svr_lin.fit(X, y1)  # 學習訓練.fit, SVR(linear) 迴歸

y_pred_lin = svr_lin.predict(X)  # 預測.predict, SVR(linear)

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred_lin, color="r", marker="o", markersize=8, label="SVR線性迴歸")  # SVR線性迴歸

plt.title("SVR(linear) 迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7c SVR(rbf/linear/poly) 迴歸")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料
X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列

# 迴歸, 用 sklearn 裡的 SVR 的 rbf 來做迴歸
svr_rbf = sklearn.svm.SVR(kernel="rbf", C=1e3, gamma=0.3)  # SVR 函數學習機, rbf

# 迴歸, 用 sklearn 裡的 SVR 的 linear 來做迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

# 迴歸, 用 sklearn 裡的 SVR 的 poly 來做迴歸
svr_poly = sklearn.svm.SVR(kernel="poly", C=1e3, degree=4)  # SVR 函數學習機, poly

svr_rbf.fit(X, y1)  # 學習訓練.fit, SVR(rbf) 迴歸
svr_lin.fit(X, y1)  # 學習訓練.fit, SVR(linear) 迴歸
svr_poly.fit(X, y1)  # 學習訓練.fit, SVR(poly) 迴歸

y_pred_rbf = svr_rbf.predict(X)  # 預測.predict, SVR(rbf)
y_pred_lin = svr_lin.predict(X)  # 預測.predict, SVR(linear)
y_pred_poly = svr_poly.predict(X)  # 預測.predict, SVR(poly)

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred_rbf, color="m", marker="o", markersize=8, label="rbf")  # SVR(rbf)
plt.plot(
    x, y_pred_lin, color="r", marker="o", markersize=8, label="linear"
)  # SVR(linear)
plt.plot(x, y_pred_poly, color="y", marker="o", markersize=8, label="poly")  # SVR(poly)
plt.title("SVR(rbf/linear/poly) 迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用 Radial Basis Function (RBF)
# （高斯）徑向基函數核（英語：Radial basis function kernel），或稱為RBF核
def RBF(x, center, sigma):
    k = np.exp(-((x - center) ** 2) / (2 * sigma**2))
    return k


print("資料來源 : 自建資料 7d 線性/多項式/RBF")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

# 使用 線性學習機 學習
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
X = x.reshape(len(x), 1)
linear_regression.fit(X, y1)  # 學習訓練.fit

# 使用 6 次多項式 學習
X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])
regression_poly = sklearn.linear_model.LinearRegression()  # 函數學習機
regression_poly.fit(X_poly, y1)  # 學習訓練.fit

# 使用 RBF
sigma = 0.3
X_rbf = np.array(
    [
        [
            RBF(k, 0.5, sigma),
            RBF(k, 1.5, sigma),
            RBF(k, 2.5, sigma),
            RBF(k, 3.5, sigma),
            RBF(k, 4.5, sigma),
        ]
        for k in x
    ]
)
regression_rbf = sklearn.linear_model.LinearRegression()  # 函數學習機
regression_rbf.fit(X_rbf, y1)  # 學習訓練.fit

y_pred_lin = linear_regression.predict(X)  # 預測.predict
y_pred_poly = regression_poly.predict(X_poly)  # 預測.predict
y_pred_rbf = regression_rbf.predict(X_rbf)  # 預測.predict

plt.plot(x, y0, color="lime", label="理想資料")  # 理想資料
plt.plot(x, y1, color="m", marker="o", markersize=8, label="真實資料")  # 線性迴歸曲線
plt.plot(x, y_pred_lin, "r", label="線性學習機 預測結果")
plt.plot(x, y_pred_poly, "g", label="6次多項式 預測結果")
plt.plot(x, y_pred_rbf, "b", label="RBF 預測結果")

plt.title("各種方法比較")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 內建資料 1 計程車小費資料集EDA")

# 計程車小費資料集EDA  共244筆資料, 7個欄位

from sklearn import preprocessing

df = sns.load_dataset("tips")
cc = df.head(30)
# print(cc)
cc = df.info()
# print(cc)

# 資料清理、資料探索與分析

# 類別變數轉換為數值
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

cc = df.isna().sum()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.drop("tip", axis=1).values
y = df.tip.values
print(y)

# 真正開始分析資料

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = preprocessing.StandardScaler()
print("特徵縮放")
print(X_train)
X_train_std = scaler.fit_transform(X_train)  # 特徵縮放
print(X_train_std)

X_test_std = scaler.transform(X_test)  # 特徵縮放

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test_std)  # 預測.predict

print("評估 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 檔案資料")

# 共 15188 筆資料, 16欄位
df = pd.read_excel(
    "C:/_git/vcs/_4.python/__code/Python-PM2.5-DataAnalyzing-master/各種演算法比較/20160101-20190101(Daily)迴歸分析.xlsx"
)

print("df 111")
print(df.columns)
print(df.shape)
print(df)
cc = df.head(10)
print(cc)

# 資料長度
print(len(df))
print(len(df["PM25"]))

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

print(df.columns)
cc = df.set_index("Date")  # 將Date欄位設定為索引欄位
print("df 222")
print(df.columns)
print(df.shape)
print(cc)

print(df.dtypes)
print(df.isnull().sum())
print(df.isnull().any())


x = df[
    [
        "SO2",
        "CO",
        "O3",
        "PM10",
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

y = df["PM25"].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

"""
sns.heatmap(df.corr())
plt.show()
cc = df.corr()
print(cc)
"""

y_pred = linear_regression.predict(x_test)  # 預測.predict

df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})
df1 = df.head(25)
# print(df1)

df1.plot(kind="bar", figsize=(10, 8))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

print("評估 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 內建 糖尿病")

"""
Multiple Regression多元回歸糖尿病案例
diabetes dataset 資料集是一個糖尿病的資料集
主要包括442筆資料,10個屬性值,分別是:
Age(年齡)、Sex(性別)、Body mass index(體質指數)、
Average Blood Pressure(平均血壓)、S1-S6一年後疾病級數指標,
Target為一年後患疾病的定量指標。
題目1
建立線性多元回歸的預測模型,繪製散佈圖來比較一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。
題目2
建立線性多元回歸的預測模型,只取Age(年齡)、Sex(性別)、Body mass index(體質指數)、Average Blood Pressure(平均血壓)作為解釋變數,產生模型,並匯出散佈圖來比較預測一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。
"""

# 題目1
diabetes = datasets.load_diabetes()

# print(diabetes.DESCR)
print("keys")
print(diabetes.keys())
print("feature_names")
print(diabetes.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=["Target"])

print("Target為一年後患疾病的定量指標")
y = target["Target"]  # Series
print()
print(y)
print()

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

y_pred_diabetes = linear_regression.predict(X)  # 預測.predict

plt.scatter(y, y_pred_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")

plt.show()

"""
#題目2
###################### 4 items ##############################
X1 = diabetes.data[:,:4]
X1 = pd.DataFrame(X1, columns=["age","sex","bmi", "bp"])
#print(X1)

target = pd.DataFrame(diabetes.target ,columns=["Target"])
y1 = target["Target"]

linear_regression_4items = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression_4items.fit(X1,y1)  # 學習訓練.fit

print("迴歸係數:", linear_regression_4items.coef_)
print("截距:", linear_regression_4items.intercept_)
y_pred_4items_diabetes = linear_regression_4items.predict(X1)# 預測.predict

plt.scatter(y1 ,y_pred_4items_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")
plt.show()

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 內建 糖尿病")

"""
糖尿病数据（适用于回归任务）

这是一个糖尿病的数据集，主要包括442行数据，10个属性值，分别是：
Age(年龄)、性别(Sex)、Body mass index(体质指数)、Average Blood Pressure(平均血压)、
S1~S6一年后疾病级数指标。

Target为一年后患疾病的定量指标，因此适合与回归任务
"""


def do_linear_regression():
    diabetes = datasets.load_diabetes()

    X = diabetes.data[:, np.newaxis, 2]
    print("Data shape: ", X.shape)

    x_train, x_test, y_train, y_test = train_test_split(
        X, diabetes.target, test_size=0.1, random_state=4
    )

    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

    linear_regression.fit(x_train, y_train)  # 學習訓練.fit

    y_pred = linear_regression.predict(x_test)  # 預測.predict

    plt.scatter(x_test, y_test, color="black")
    plt.plot(x_test, y_pred, color="blue", linewidth=3)
    plt.show()


print("線性迴歸")
do_linear_regression()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 ddddd")

print("線性迴歸, 輸入資料的寫法")
X = [[10.0], [8.0], [13.0], [9.0], [11.0], [14.0], [6.0], [4.0], [12.0], [7.0], [5.0]]
y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)

print("預測的寫法")
y_pred = linear_regression.predict([[0], [1]])  # 預測.predict
print(y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("簡單線性回歸")

dataset = pd.read_csv("data/studentscores.csv")
X = dataset.iloc[:, :1].values
Y = dataset.iloc[:, 1].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)
# 訓練組8成, 測試組2成

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

plt.scatter(X, Y, color="b", label="真實資料")

y_pred = linear_regression.predict(x_test)  # 預測.predict
plt.plot(x_test, y_pred, "mo-", label="線性迴歸2")

plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多元线性回归（Multiple Linear Regression）")

# 讀取資料
dataset = pd.read_csv("data/50_Startups.csv")
X = dataset.iloc[:, :-1].values  # 全部資料
Y = dataset.iloc[:, 4].values  # 第4欄的全部資料(收益)
Z = dataset.iloc[:, 0].values  # 第0欄的全部資料(R&D花費)
print("X:")
print(X)
print("Y:")
print(Y)
print("Z:")
print(Z)
print()

# 缺失資料之處理
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=0.0, strategy="mean")
imputer = imputer.fit(X[:, 0:3])
X[:, 0:3] = imputer.transform(X[:, 0:3])
print(X)

# 将类别数据数字化

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder = LabelEncoder()
print("original:")
print(X[:10])
# print(X[: , 3])
X[:, 3] = labelencoder.fit_transform(X[:, 3])
# print(X[: , 3])
print("labelencoder:")
print(X[:10])
ct = ColumnTransformer([("encoder", OneHotEncoder(), [3])], remainder="passthrough")
X = ct.fit_transform(X)
# onehotencoder = OneHotEncoder(categorical_features = [3])
# X = onehotencoder.fit_transform(X).toarray()
print("onehot:")
print(X[:10])

"""
躲避虚拟变量陷阱
在回归预测中我们需要所有的数据都是numeric的，但是会有一些非numeric的数据，
比如国家，省，部门，性别。这时候我们需要设置虚拟变量（Dummy variable）。
做法是将此变量中的每一个值，衍生成为新的变量，是设为1，否设为0.
举个例子，“性别”这个变量,我们可以虚拟出“男”和”女”两虚拟变量，
男性的话“男”值为1，”女”值为0；女性的话“男”值为0，”女”值为1。
但是要注意，这时候虚拟变量陷阱就出现了。
就拿性别来说，其实一个虚拟变量就够了，比如 1 的时候是“男”， 0 的时候是”非男”，即为女。
如果设置两个虚拟变量“男”和“女”，语义上来说没有问题，可以理解，
但是在回归预测中会多出一个变量，多出的这个变量将会对回归预测结果产生影响。
一般来说，如果虚拟变量要比实际变量的种类少一个。
在多重线性回归中，变量不是越多越好，而是选择适合的变量。这样才会对结果准确预测。
如果category类的特征都放进去，拟合的时候，所有权重的计算，都可以有两种方法实现，
一种是提高某个category的w，一种是降低其他category的w，这两种效果是等效的，
也就是发生了共线性,虚拟变量系数相加和为1，出现完全共线陷阱。
但是下面测试尽然和想法不一致。。。
"""

# Avoiding Dummy Variable Trap
X1 = X[:, 1:]

print(X1)
print(X)

# 拆分数据集为训练集和测试集
# Splitting the dataset into the Training set and Test set

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

x1_train, x1_test, y1_train, y1_test = train_test_split(X1, Y, test_size=0.2)

# 第2步：在训练集上训练多元线性回归模型
# Fitting Multiple Linear Regression to the Training set

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

linear_regression2 = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression2.fit(x1_train, y1_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict
y1_pred = linear_regression2.predict(x1_test)  # 預測.predict
print(y_pred)
print(y1_pred)

# regression evaluation
from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG OneHotEncoder
dataset = pd.read_csv("data/50_Startups.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

# 将类别数据数字化

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# 躲避虚拟变量陷阱

X = X[:, 1:]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict
print(y_pred)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some sample data
x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 3, 4, 5, 6])

# Create the model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Predict the outcome for a new data point
new_x = np.array([6]).reshape((-1, 1))
y_pred = model.predict(new_x)

# Print the coefficients and predicted outcome
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)
print("Predicted outcome: ", y_pred[0])


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np

# Generate some sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Calculate the slope and y-intercept of the regression line
slope, intercept = np.polyfit(x, y, 1)

# Use the slope and y-intercept to make predictions
new_x = 6
y_pred = slope * new_x + intercept

# Print the slope, y-intercept, and predicted outcome
print("Slope: ", slope)
print("Y-intercept: ", intercept)
print("Predicted outcome: ", y_pred)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np

# Generate some sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Calculate the coefficients of the regression line
X = np.vstack([x, np.ones(len(x))]).T
coeffs = np.linalg.inv(X.T @ X) @ X.T @ y

# Use the coefficients to make predictions
new_x = 6
y_pred = coeffs[0] * new_x + coeffs[1]

# Print the coefficients and predicted outcome
print("Coefficients: ", coeffs)
print("Predicted outcome: ", y_pred)


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

# 共同取出
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

print("迴歸係數:", linear_regression.coef_)
# 迴歸係數: [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163 476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]


# 測試資料型態
xxx = np.array([3, 9, 8, 1, 2])
yyy = np.array([1, 3, 9, 2, 4])

print("目前 xxx 是個 5 維向量")
print(xxx.shape)

# xxx訓練資料要轉為 NX1 陣列
xxx = xxx.reshape(len(xxx), 1)
print(xxx.shape)


print("打印一些結果")
print(linear_regression.predict([[1.3]]))  # 預測.predict
print(linear_regression.predict([[2.7], [1.5]]))  # 預測.predict


# 預測

print(svr_lin.predict([[6.2]]))  # 預測.predict
print(svr_lin.predict([[6.2], [7.4], [8]]))  # 預測.predict

temp = [[23]]  # 輸入特徵值(氣溫)
p = linear_regression.predict(temp)  # 輸出標籤(預測的銷售量)  # 預測.predict
print(p)

temp = [[23], [18], [36]]
p = linear_regression.predict(temp)  # 預測.predict
print(p)


# SVR 函數學習機, rbf / linear / poly


plt.axis([-3, 3, -150, 150])  # 設定各軸顯示範圍
plt.xlim(-3, 3)
plt.ylim(-150, 150)


# -------------------------

"""
# 決定模型：取出線性迴歸模型的 m、b 參數
print("線性迴歸的模型為 y = f(x) = mx + k")
print("m 為 ", linear_regression.coef_)
print("k 為 ", linear_regression.intercept_)

m = linear_regression.coef_[0][0]  # 取出斜率
k = linear_regression.intercept_[0]  # 取出截距
print(f"斜率  = {m.round(2)}")
print(f"截距  = {k.round(2)}")

y2 = m * xs + k
plt.plot(xs, ys, "b-o", lw=1, ms=10, label="實驗值")
plt.plot(xs, y2, "r", lw=2, label="迴歸直線")  # 繪製迴歸直線

xxx = 10
predicted = m * xxx + k
print(f"x = 10 的 預測值 = {predicted}")
plt.plot(xxx, predicted, "ro", lw=1, ms=12, label="預測值")


"""

# 預測
cc = linear_regression.predict([[6]])  # 預測.predict


plt.plot(xxx, yyy, "go:")


# 資料的寫法
X = [[1], [2], [3], [4], [5]]
y = [88, 72, 90, 76, 92]
linear_regression.fit(X, y)  # 學習訓練.fit


# 資料的寫法
# x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
# y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量
# x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
# y = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
xs = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]], dtype=float)
ys = np.array([[0.0], [1.0], [2.0], [5.0], [4.0], [5.0]], dtype=float)

linear_regression.fit(xs, ys)  # 學習訓練.fit


"""
因變數 x
應變數
y0 理想資料
y1 真實資料

1. 理想資料 lime
2. 真實資料 b
3. 線性迴歸 red
   其他迴歸

"""


print("評估 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)


plt.scatter(X, y, c="blue", marker="o", lw=0.1, label="真實資料")


# 標準
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.scatter(x, y1, s=100, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(x, Y, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線


print("評估 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)


# 自己算
print("計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE")
mse = np.sum((y_test - Y_test) ** 2) / len(y_test)
print("MSE =", mse)


print("計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE")
mse = np.sum((y_test - Y_test) ** 2) / len(y_test)
print("MSE =", mse)
