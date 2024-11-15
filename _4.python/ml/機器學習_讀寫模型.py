"""
機器學習_讀寫模型

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

import pickle
import joblib

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立模型, 並儲存模型")

print("線性迴歸")

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y0 = x  # 理想資料, y = x
y1 = np.array([0, 1, 4, 3, 4, 5, 6, 3, 8, 9, 10])  # 真實資料

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列
y1 = y1.reshape(len(y1), 1)

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

print("將 模型存檔 存成 pickle")

with open("tmp_my_model.pickle", "wb") as f:
    pickle.dump(linear_regression, f)

print("將 模型存檔 存成 joblib")
joblib.dump(linear_regression, "tmp_my_model.joblib")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之")

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y0 = x  # 理想資料, y = x
y1 = np.array([0, 1, 4, 3, 4, 5, 6, 3, 8, 9, 10])  # 真實資料

X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列


# 讀取模型 pickle
y_pred2 = []
with open("tmp_my_model.pickle", "rb") as f:
    linear_regression2 = pickle.load(f)
    y_pred2 = linear_regression2.predict(X)  # 預測.predict
print(y_pred2)

# 讀取模型 joblib
y_pred3 = []
linear_regression3 = joblib.load("tmp_my_model.joblib")
y_pred3 = linear_regression3.predict(X)  # 預測.predict
print(y_pred3)

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred2, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線
# plt.plot(x, y_pred3, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線

plt.title("線性迴歸 無 資料分割")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個
