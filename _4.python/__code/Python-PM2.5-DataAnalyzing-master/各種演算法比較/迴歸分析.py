"""
迴歸分析

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

df = pd.read_excel("20160101-20190101(Daily)迴歸分析.xlsx")
# print(df)

cc = df.set_index("Date")
print(cc)

"""
df.dtypes
df.isnull().sum()
df.isnull().any()
"""

X = df[
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

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)# 訓練組8成, 測試組2成

# 載入線性迴歸，並訓練模型
from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

"""
sns.heatmap(df.corr())
plt.show()

cc = df.corr()
print(cc)
"""
y_pred = linear_regression.predict(X_test)


df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})
df1 = df.head(25)
# print(df1)

df1.plot(kind="bar", figsize=(10, 8))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
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

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
