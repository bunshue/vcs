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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics


# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度
from sklearn.metrics import accuracy_score  # 計算分類模型的準確率


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個


# 迴歸效果評估
def evaluate_result(y_test, y_pred):
    # print("真實資料(y_test) :", y_test)
    # print("預測資料(y_pred) :", y_pred)

    # 自己算
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
    # print(f"決定係數R2 = {r2_score(y_test, y_pred)*100:.2f}")


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
    print()


"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('測試 evaluate_result')

xx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yy = np.array([0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 10])

print_y_data(xx)
print_y_data(yy)

evaluate_result(xx, yy)

print("------------------------------------------------------------")  # 60個

#accuracy_score(y_true, y_pred) 用于计算分类模型的准确率，即分类正确的样本数除以总样本数
#y_true：真实的分类标签，可以是列表、数组、Pandas Series或其他可迭代对象
#y_pred：模型预测的分类标签，需要与y_true格式相同
#accuracy_score()函数将返回一个0到1之间的单精度浮点数，表示分类模型的准确率

y_true = [0, 1, 2, 1, 3]
y_pred = [0, 1, 2, 2, 3]
cc = accuracy_score(y_true, y_pred)
print("計算分類模型的準確率 accuracy_score :")
print(cc)

print("------------------------------------------------------------")  # 60個
"""
"""
sklearn.metrics中的评估方法介绍
（accuracy_score, recall_score, roc_curve, roc_auc_score, confusion_matrix）
"""

'''
from sklearn.metrics import accuracy_score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
cc = accuracy_score(y_true, y_pred)
print(cc)

cc = accuracy_score(y_true, y_pred, normalize=False)
print(cc)

# normalize：默认值为True，返回正确分类的比例；如果为False，返回正确分类的样本数

from sklearn.metrics import recall_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
cc = recall_score(y_true, y_pred, average="macro")
print(cc)
cc = recall_score(y_true, y_pred, average="micro")
print(cc)

cc = recall_score(y_true, y_pred, average="weighted")
print(cc)

cc = recall_score(y_true, y_pred, average=None)
print(cc)

"""
ROC曲线指受试者工作特征曲线/接收器操作特性(receiver operating characteristic，ROC)曲线,是反映灵敏性和特效性连续变量的综合指标,是用构图法揭示敏感性和特异性的相互关系，它通过将连续变量设定出多个不同的临界值，从而计算出一系列敏感性和特异性。ROC曲线是根据一系列不同的二分类方式（分界值或决定阈），以真正例率（也就是灵敏度）（True Positive Rate,TPR）为纵坐标，假正例率（1-特效性）（False Positive Rate,FPR）为横坐标绘制的曲线。
ROC观察模型正确地识别正例的比例与模型错误地把负例数据识别成正例的比例之间的权衡。TPR的增加以FPR的增加为代价。ROC曲线下的面积是模型准确率的度量，AUC（Area under roccurve）。
"""

from sklearn import metrics

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr)
print(tpr)
print(thresholds)

from sklearn.metrics import auc

cc = metrics.auc(fpr, tpr)
print(cc)

from sklearn.metrics import roc_auc_score

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
cc = roc_auc_score(y_true, y_scores)
print(cc)

from sklearn.metrics import confusion_matrix

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
cc = confusion_matrix(y_true, y_pred)
print(cc)

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
cc = confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
print(cc)

'''
