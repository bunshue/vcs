"""
20190407-空氣盒子數據Keras深度學習實作


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

df = pd.read_excel("KH-1982-2018b.xlsx")

# df.dtypes

# 轉換資料型態成float
df["PM25"] = df["PM25"].astype(float)

# 查看資料狀態
cc = df.describe(include="all")
print(cc)

# 分割資料，X為前12項；Y為第13項，且為數值
X = df.iloc[:, 0:12]
y = df.iloc[:, 12].values

# 進行資料前處理，轉換資料尺度
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()
X = sc.fit_transform(X)
y = y.reshape(-1, 1)
y = sc.fit_transform(y)

# 分成測試與訓練集(80%:20%)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 進行Keras的深度學習
from keras import Sequential  # 使用順序模型
from keras.layers import Dense


def build_regressor():
    # 建立輸入層
    regressor = Sequential()
    regressor.add(
        Dense(128, kernel_initializer="normal", input_dim=12, activation="relu")
    )  # 增加神經層12層
    # 建立隱藏層
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    regressor.add(Dense(256, kernel_initializer="normal", activation="relu"))
    # 建立輸出層:1
    regressor.add(Dense(1, kernel_initializer="normal", activation="linear"))
    # 編譯神經網路
    regressor.compile(
        optimizer="adam", loss="mean_squared_error", metrics=["mae", "accuracy"]
    )
    return regressor


from keras.wrappers.scikit_learn import KerasRegressor

regressor = KerasRegressor(build_fn=build_regressor, batch_size=32, epochs=160)

results = regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

loss_and_metrics = model.evaluate(X_train, y_train, batch_size=128)
print(loss_and_metrics)

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "k--", lw=4)
ax.set_xlabel("Measured")
ax.set_ylabel("Predicted")
plt.show()


y_pred = model.predict(X_test)

range_x = range(1, len(y_pred) + 1)
plt.figure(figsize=(12, 6))
plt.plot(range_x, y_pred, "--o", alpha=0.5, label="Predictions")
plt.plot(range_x, y_test, "-o", alpha=0.8, label="Real")
plt.title("Predictions V.S. Real")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
