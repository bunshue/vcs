"""
Lasso
Ridge

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

import tensorflow as tf
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料 上/下弦月資料


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)

train_size = 20
test_size = 12
train_X = np.random.uniform(low=0, high=1.2, size=train_size)
test_X = np.random.uniform(low=0.1, high=1.3, size=test_size)
train_y = np.sin(train_X * 2 * np.pi) + np.random.normal(0, 0.2, train_size)
test_y = np.sin(test_X * 2 * np.pi) + np.random.normal(0, 0.2, test_size)

poly = PolynomialFeatures(6)  # 次數は6

train_poly_X = poly.fit_transform(train_X.reshape(train_size, 1))

test_poly_X = poly.fit_transform(test_X.reshape(test_size, 1))

model = Ridge(alpha=1.0)

model.fit(train_poly_X, train_y)  # 學習訓練.fit

train_pred_y = model.predict(train_poly_X)  # 預測.predict
test_pred_y = model.predict(test_poly_X)  # 預測.predict

print("訓練資料之 MSE :", mean_squared_error(train_pred_y, train_y))
print("測試資料之 MSE :", mean_squared_error(test_pred_y, test_y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Lasso回归(也称套索回归),是一种正则化的线性回归。
与岭回归相同，使用Lasso也是约束系数，使其接近于0，但使用的是L1正则化。
lasso惩罚系数是向量的L1范数，换句话说，系数的绝对值之和。
L1正则化的结果是，使用lasso时，某些系数刚好为0。
这说明某些特征被模型完全忽略。这可以看做是一种自动化的特征选择。
"""

# 将lasso应用在波士顿房价预测上面

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import mglearn

# 读取数据，并划分训练集和测试集
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# 通过设置不同的alpha值建立三个lasso实例
lasso = Lasso().fit(X_train, y_train)
lasso001 = Lasso(alpha=0.01).fit(X_train, y_train)
lasso00001 = Lasso(alpha=0.0001).fit(X_train, y_train)

# 输出三个lasso实例的信息
print("**********************************")
print("Lasso alpha=1")
print("training set score:{:.2f}".format(lasso.score(X_train, y_train)))
print("test set score:{:.2f}".format(lasso.score(X_test, y_test)))
print("Number of features used:{}".format(np.sum(lasso.coef_ != 0)))

print("**********************************")
print("Lasso alpha=0.01")
print("training set score:{:.2f}".format(lasso001.score(X_train, y_train)))
print("test set score:{:.2f}".format(lasso001.score(X_test, y_test)))
print("Number of features used:{}".format(np.sum(lasso001.coef_ != 0)))

print("**********************************")
print("Lasso alpha=0.0001")
print("training set score:{:.2f}".format(lasso00001.score(X_train, y_train)))
print("test set score:{:.2f}".format(lasso00001.score(X_test, y_test)))
print("Number of features used:{}".format(np.sum(lasso00001.coef_ != 0)))
# 建立岭回归实例
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)

# 绘制三个lasso和一个岭回归的系数分布结果
plt.figure(figsize=(7, 7))
plt.plot(lasso.coef_, "s", label="Lasso alpha=1")
plt.plot(lasso001.coef_, "^", label="Lasso alpha=0.01")
plt.plot(lasso00001.coef_, "v", label="Lasso alpha=0.0001")
plt.plot(ridge01.coef_, "o", label="ridge alpha=0.1")
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")
plt.ylim(-25, 25)
plt.legend(ncol=2, loc=(0, 1.05))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import linear_model

clf = linear_model.Lasso(alpha=0.1)
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# Lasso(alpha=0.1)
print(clf.coef_)

# [0.85 0.  ]
print(clf.intercept_)
# 0.15...

print("------------------------------------------------------------")  # 60個

print("使用 Lasso 類來擬合數據")

from sklearn.linear_model import Lasso

X = np.random.rand(100, 10)
y = np.random.rand(100)

lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

print("模型係數")
print(lasso.coef_)

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
