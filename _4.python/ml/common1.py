"""
共用函數

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


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度
from sklearn.metrics import accuracy_score  # 沒用到

print("------------------------------------------------------------")  # 60個


# 迴歸效果評估
def evaluate_result(y_test, y_pred):
    # print("真實資料(y_test) :", y_test)
    # print("預測資料(y_pred) :", y_pred)

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


def print_y_data(y):
    N = 30  # 最多的個數
    R = 10  # 每R個換行
    length = len(y)
    if length > N:
        length = N
    if length <= 30:
        R = 31
    for i in range(length):
        print(y[i], end="")
        if i % R == (R - 1):
            print()
        else:
            print(end=" ")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
