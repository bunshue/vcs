"""
20190313-空氣盒子數據Scikit-Learn線性迴歸實作-註解版

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

import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/200811-201811b.csv")  # 共有 1447 筆資料

plt.scatter(df["PM25"], df["CO"], c='yellow')
plt.scatter(df["PM25"][:100], df["CO"][:100], c='r')
plt.scatter(df["PM25"][100:200], df["CO"][100:200], c='g')
plt.scatter(df["PM25"][200:300], df["CO"][200:300], c='b')

plt.xlabel("PM25")
plt.ylabel("CO")
plt.title("PM25 對比 CO")

plt.show()

print("------------------------------")  # 30個

# 用 histplot() 看PM2.5主要集中的區間
sns.histplot(df["PM25"])
plt.title("PM25濃度統計")
plt.show()

print("------------------------------")  # 30個

# 使用 df.corr() 先做出各變數間的關係係數，再用heatmap作圖
sns.heatmap(df.corr())
plt.title("關係係數")
plt.show()

print("------------------------------")  # 30個

# 訓練線性模型

# X是想探索的自變數，Y是依變數。

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
]

y = df["PM25"]

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

# test_size代表測試組比例。random_state代表設定隨機種子，讓測試結果可被重複

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=9487
)  # 訓練組6成, 測試組4成

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train, y_train)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

# 取得截距。如果公式是y=ax+b，b即是截距
print("截距b:", linear_regression.intercept_)
# 截距b: 4.194703731759336

# 取得迴歸係數，並用Data Frame顯示
print("迴歸係數 :", linear_regression.coef_)

# 列出訓練的變數
print(X_train.columns)

# 預測, 使用測試組資料來預測結果
y_pred = linear_regression.predict(X_test)  # 預測.predict

df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})
#print(df)

print("畫出前 N 筆, 比較實際PM2.5及預測PM2.5的關係")
N = 20
df1 = df.head(N)

plt.figure(figsize=(10, 5))

plt.scatter(y_test, y_pred)

plt.show()

df1.plot(kind="bar", figsize=(10, 8))
plt.show()

# 看實際值及預測值之間的殘差分佈圖
sns.distplot((y_test - y_pred))

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

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


