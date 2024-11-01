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

df = pd.read_csv("data/200811-201811b.csv")
"""
cc = df.head(20)
print(cc)

cc = df.info()
print(cc)

cc = df.describe()
print(cc)
"""

# 用圖表探索資料
# 利用distplot來看PM2.5主要集中的區間

sns.distplot(df["PM25"])
plt.show()

# 利用df.corr()先做出各變數間的關係係數，再用heatmap作圖
sns.heatmap(df.corr())
plt.show()

# 訓練線性模型

cc = df.columns
print(cc)

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
    X, y, test_size=0.4, random_state=101
)

# 載入線性迴歸，並訓練模型

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""

y_pred = lm.predict(X_test)

# 取得截距。如果公式是y=ax+b，b即是截距

print("截距b:", lm.intercept_)

# 截距b: 4.194703731759336

# 取得迴歸係數，並用Data Frame顯示
print(lm.coef_)

# 列出訓練的變數
print(X_train.columns)

# 預測
# 使用測試組資料來預測結果
predictions = lm.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(df)

df1 = df.head(20)
print(df1)

# 比較實際PM2.5及預測PM2.5的關係

plt.scatter(y_test, predictions)
plt.show()


df1.plot(kind="bar", figsize=(10, 8))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

# 看實際值及預測值之間的殘差分佈圖
sns.distplot((y_test - predictions))

plt.show()


# 載入迴歸常見的評估指標
from sklearn import metrics
print("評估 測試資料 與 預測結果 的差異")

# Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
cc = metrics.mean_absolute_error(y_test, predictions)
print("MAE : Mean Absolute Error :", cc)

# Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
cc = metrics.mean_squared_error(y_test, predictions)
print("MSE : Mean Squared Error :", cc)

# Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
cc = np.sqrt(metrics.mean_squared_error(y_test, predictions))
print("RMS : Root Mean Squared Error :", cc)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
