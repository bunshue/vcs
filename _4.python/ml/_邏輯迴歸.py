"""
監督式學習 : 邏輯迴歸 (logistic regression)

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

import joblib
import itertools
import sklearn.linear_model
import sklearn.metrics as metrics
from common1 import *
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_circles  # 圓形分佈的資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler  # 特徵縮放
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay  # 混淆矩陣圖
from sklearn.metrics import classification_report  # 分類報告
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn import tree
from sklearn import metrics
from sklearn import linear_model


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
N = 500  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 10.0  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

scaler = StandardScaler()
XX = scaler.fit_transform(X)  # STD特徵縮放

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(XX, y, test_size=0.4)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict

# 輸出準確性
score_train = logistic_regression.score(X_train, y_train)
score_test = logistic_regression.score(X_test, y_test)

print(f"訓練資料 的 準確性 = {score_train}")
print(f"測試資料 的 準確性 = {score_test}")

y_pred_train = logistic_regression.predict(X_train)  # 預測.predict
y_pred_test = logistic_regression.predict(X_test)  # 預測.predict

print("------------------------------")  # 30個
plt.subplot(221)

# 真實資料 空心圓
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i, 0], X[i, 1], c="none", marker="o", edgecolors="r")
    elif y[i] == 1:
        plt.scatter(X[i, 0], X[i, 1], c="none", marker="o", edgecolors="g")
    elif y[i] == 2:
        plt.scatter(X[i, 0], X[i, 1], c="none", marker="o", edgecolors="b")

# 真實資料 實心點
for i in range(len(X)):
    if y[i] == 0:
        plt.scatter(X[i, 0], X[i, 1], c="r", s=5)
    elif y[i] == 1:
        plt.scatter(X[i, 0], X[i, 1], c="g", s=5)
    elif y[i] == 2:
        plt.scatter(X[i, 0], X[i, 1], c="b", s=5)

plt.title("原始資料, 分成3群")

print("------------------------------")  # 30個
plt.subplot(222)

# 真實資料 空心圓
for i in range(len(XX)):
    if y[i] == 0:
        plt.scatter(XX[i, 0], XX[i, 1], c="none", marker="o", edgecolors="r")
    elif y[i] == 1:
        plt.scatter(XX[i, 0], XX[i, 1], c="none", marker="o", edgecolors="g")
    elif y[i] == 2:
        plt.scatter(XX[i, 0], XX[i, 1], c="none", marker="o", edgecolors="b")

# 真實資料 實心點
for i in range(len(XX)):
    if y[i] == 0:
        plt.scatter(XX[i, 0], XX[i, 1], c="r", s=5)
    elif y[i] == 1:
        plt.scatter(XX[i, 0], XX[i, 1], c="g", s=5)
    elif y[i] == 2:
        plt.scatter(XX[i, 0], XX[i, 1], c="b", s=5)

plt.title("特徵縮放後")

print("------------------------------")  # 30個
plt.subplot(223)

# 真實訓練資料 空心圓
for i in range(len(X_train)):
    if y_train[i] == 0:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="none", marker="o", edgecolors="r")
    elif y_train[i] == 1:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="none", marker="o", edgecolors="g")
    elif y_train[i] == 2:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="none", marker="o", edgecolors="b")

# 預測訓練資料 實心點
for i in range(len(X_train)):
    if y_pred_train[i] == 0:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="r", s=5)
    elif y_pred_train[i] == 1:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="g", s=5)
    elif y_pred_train[i] == 2:
        plt.scatter(X_train[i, 0], X_train[i, 1], c="b", s=5)

plt.title(f"預測 訓練資料 準確性 = {score_train}")

print("------------------------------")  # 30個
plt.subplot(224)

# 真實測試資料 空心圓
for i in range(len(X_test)):
    if y_test[i] == 0:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="none", marker="o", edgecolors="r")
    elif y_test[i] == 1:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="none", marker="o", edgecolors="g")
    elif y_test[i] == 2:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="none", marker="o", edgecolors="b")

# 預測測試資料 空心圓
for i in range(len(X_test)):
    if y_pred_test[i] == 0:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="r", s=5)
    elif y_pred_test[i] == 1:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="g", s=5)
    elif y_pred_test[i] == 2:
        plt.scatter(X_test[i, 0], X_test[i, 1], c="b", s=5)

# plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_test, s=5)
plt.title(f"預測 測試資料 準確性 = {score_test}")

plt.suptitle("監督式學習 : 邏輯迴歸 (logistic regression)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_regression_with_nonlinear_data

N = 1000  # n_samples, 樣本數
M = 4  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
print("make_circles,", N, "個樣本")

X, y = make_circles(n_samples=N, factor=0.3, noise=0.05, random_state=9487)

# 資料分割 多了一個 stratify=y
# X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=9487)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9487)

# 繪製訓練及測試資料

plt.figure(figsize=(8, 4))

plt.subplot(121)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.title("訓練資料")

plt.subplot(122)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
plt.title("測試資料")

show()

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict
print("y_pred :\n", y_pred, sep="")

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 48.80%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 30
group0 = np.random.normal(-1, 1, size=N)  # 第0群 30個, 範圍-1~1, 對應到0
group1 = np.random.normal(3, 1, size=N)  # 第1群 30個, 範圍1~3, 對應到1

x = np.r_[group0, group1]
print(x)
print(x.shape)

X = x.reshape((N * 2, -1))
print(X)
print(X.shape)

y = np.r_[np.zeros(N), np.ones(N)]  # 目標,前半0, 後半1
print(y)
print(y.shape)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict
print("全預測 :")
print(y_pred)
print(y_pred.shape)

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

length = len(y_pred)
print(len(y_pred))
print(len(y_pred_prob))

plt.subplot(211)
plt.hist(group0, alpha=0.3, label="第0群, 對應到0")
plt.hist(group1, alpha=0.3, label="第1群, 對應到1")
plt.title("原始資料")
plt.legend()

plt.subplot(212)
plt.plot(range(length), y_pred, color="lime", marker="o", markersize=10, label="預測結果")
plt.plot(range(length), y_pred_prob[:, 0], "ro-", label="對應到第0群的機率")
plt.plot(range(length), y_pred_prob[:, 1], "go-", label="對應到第1群的機率")
plt.legend()
show()

print(logistic_regression.predict_proba([[0]])[:, 1])  # 預測機率.predict_proba
print(logistic_regression.predict_proba([[0], [1], [2]])[:, 1])  # 預測機率.predict_proba

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

feature_names = ["萼長", "萼寬", "瓣長", "瓣寬"]
df = pd.DataFrame(iris.data, columns=feature_names)

y = iris.target  # 資料集目標

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("特徵縮放")
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(logistic_regression, "tmp_my_model_clf1.joblib")
joblib.dump(scaler, "tmp_my_model_scaler1.joblib")

print("------------------------------")  # 30個

print("讀取模型")
# 載入模型與標準化轉換模型
logistic_regression2 = joblib.load("tmp_my_model_clf1.joblib")
scaler = joblib.load("tmp_my_model_scaler1.joblib")

# 測試資料 萼長 萼寬 瓣長 瓣寬
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]  # 山鳶尾 變色鳶尾 維吉尼亞鳶尾
print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

feature_names = ["萼長", "萼寬", "瓣長", "瓣寬"]
df = pd.DataFrame(iris.data, columns=feature_names)

y = iris.target  # 資料集目標

# 集中
cc = (
    df["萼長"].mean(),
    df["萼長"].median(),
    df["萼長"].mode(),
)
print(cc)

# 計算變異數(variance)、標準差(standard deviation)、IQR
cc = (
    df["萼長"].var(),
    df["萼長"].std(),
    df["萼長"].quantile(0.75) - df["萼長"].quantile(0.25),
)
print(cc)
# (0.6856935123042505, 0.8280661279778629, 1.3000000000000007)

# 計算偏態(skewness)及峰度(kurtosis)
cc = df["萼長"].skew(), df["萼長"].kurt()
print(cc)

# 自行計算偏態
mean1 = df["萼長"].mean()
std1 = df["萼長"].std()
n = len(df["萼長"])
skew1 = (((df["萼長"] - mean1) / std1) ** 3).sum() * n / ((n - 1) * (n - 2))
print(skew1)

# 0.31491095663697277

# 自行計算峰度
M2 = (((df["萼長"] - mean1) / std1) ** 2).mean()
M4 = (((df["萼長"] - mean1) / std1) ** 4).mean()
K = M4 / (M2**2)
print(K - 3)

# -0.5735679489249756

from scipy.stats import kurtosis

print(kurtosis(df["萼長"], axis=0, bias=True))

# -0.5735679489249765

# 直方圖
sns.histplot(x="萼長", data=df)
show()

# 直方圖平滑化
sns.kdeplot(x="萼長", data=df)
show()

# 右偏

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(5, 1, 100)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
show()

# 右偏

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 500)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
show()

# 關聯度

df["y"] = y
cc = df.corr()
print(cc)

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("特徵縮放")
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(logistic_regression, "tmp_my_model_clf2.joblib")
joblib.dump(scaler, "tmp_my_model_scaler2.joblib")

print("------------------------------")  # 30個

print("讀取模型")
# 載入模型與標準化轉換模型
logistic_regression2 = joblib.load("tmp_my_model_clf2.joblib")
scaler = joblib.load("tmp_my_model_scaler2.joblib")

# 測試資料 萼長 萼寬 瓣長 瓣寬
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]

""" NG
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]  # 山鳶尾 變色鳶尾 維吉尼亞鳶尾
print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict
"""

""" 使用 streamlit 與人互動

import streamlit as st

# 設定 st 標題
st.title('鳶尾花（Iris）預測')

# 製作4個 st slider
sepal_length = st.slider('花萼長度:', min_value=3.0, max_value=8.0, value=5.8)
sepal_width = st.slider('花萼寬度:', min_value=2.0, max_value=5.0, value=3.5)
petal_length = st.slider('花瓣長度:', min_value=1.0, max_value=7.0, value=4.4)
petal_width = st.slider('花瓣寬度:', min_value=0.1, max_value=2.5, value=1.3)

if st.button('預測'):  # 當按下 預測 按鈕
    X_new = [[sepal_length,sepal_width,petal_length,petal_width]]
    X_new = scaler.transform(X_new)
    st.write('### 預測品種是：', labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 尋找銀行行銷活動目標客戶

"""
banking.csv # 41188 筆資料 21 欄
age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed,y
44,blue-collar,married,basic.4y,unknown,yes,no,cellular,aug,thu,210,1,999,0,nonexistent,1.4,93.444,-36.1,4.963,5228.1,0
53,technician,married,unknown,no,no,no,cellular,nov,fri,138,1,999,0,nonexistent,-0.1,93.2,-42,4.021,5195.8,0
28,management,single,university.degree,no,yes,no,cellular,jun,thu,339,3,6,2,success,-1.7,94.055,-39.8,0.729,4991.6,1
39,services,married,high.school,no,no,no,cellular,apr,fri,185,2,999,0,nonexistent,-1.8,93.075,-47.1,1.405,5099.1,0
55,retired,married,basic.4y,no,yes,no,cellular,aug,fri,137,1,3,1,success,-2.9,92.201,-31.4,0.869,5076.2,1
30,management,divorced,basic.4y,no,yes,no,cellular,jul,tue,68,8,999,0,nonexistent,1.4,93.918,-42.7,4.961,5228.1,0
"""

df = pd.read_csv("./data/banking.csv")
print("df之大小 :", df.shape)

# 2. 資料清理、資料探索與分析

# y 各類別資料筆數統計

sns.countplot(x="y", data=df)
show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6, 6), autopct="%1.1f%%")
plt.legend()
show()

cat_vars = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome",
]
for var in cat_vars:
    cat_list = "var" + "_" + var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1 = df.join(cat_list)
    df = data1

data_vars = df.columns.values.tolist()
to_keep = [i for i in data_vars if i not in cat_vars]
data_final = df[to_keep]
cc = data_final.columns.values
print(cc)

df = data_final
print(df)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.drop("y", axis=1).values
y = df.y.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

cc = classification_report(y_test, y_pred)
print("分類報告 :\n", cc, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib

plt.style.use("bmh")
colors = ["#A60628", "#467821"]
plt.cmap = matplotlib.colors.ListedColormap(colors)

# Bivariate normal distribution mean [0, 0] [0.5, 4], with a covariance matrix

N = 10
subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], N)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], N)
print(subset1)
print()
print(subset2)
print()

X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(N), np.ones(N)))  # 目標,前半0, 後半1
print(X)
print()

# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cmap, marker="o", s=40)
plt.scatter(X[:N, 0], X[:N, 1], c="r", label="第0群, 對應到0")
plt.scatter(X[N : N * 2 - 1, 0], X[N : N * 2 - 1, 1], c="g", label="第1群, 對應到1")
plt.legend()
show()

print("------------------------------")  # 30個

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict
print("全預測 :")
print(y_pred)

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

print("混淆矩陣 :\n", confusion_matrix(y, y_pred), sep="")

print("繪製熱圖")
sns.heatmap(confusion_matrix(y, y_pred))
show()

print("繪制分類邊界")
plt.style.use("bmh")

# Set min and max values and give it some padding
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
h = 0.01

# Generate a grid of points with distance h between them
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict the function value for the whole grid (get class for each grid point)
Z = logistic_regression.predict(np.c_[xx.ravel(), yy.ravel()])  # 預測.predict
Z = Z.reshape(xx.shape)
# print(Z)

# Plot the contour and training examples
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8)
# plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8, cmap=plt.cmap)
plt.title("logistic regression prediction")

show()

print("------------------------------")  # 30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


l_rate, iterations = 1, 10
add_intercept = True

if add_intercept:
    intercept = np.ones((X.shape[0], 1))
    X = np.hstack((intercept, X))

theta = np.zeros(X.shape[1]).reshape(-1, 1)
y = y.reshape(-1, 1)
accu_history = [0] * iterations
ll_history = [0.0] * iterations

for epoch in range(iterations):
    x_theta = np.dot(X, theta)
    y_hat = sigmoid(x_theta)
    error = y - y_hat
    gradient = np.dot(X.T, error)
    theta = theta + l_rate * gradient
    y_pred = np.round(y_hat)

    accu = np.sum(y_pred == y) * 1.0 / len(y)
    accu_history[epoch] = accu
    print("迭代 {} 次, 準確率 : {}".format(epoch + 1, accu))

print("theta :\n", theta, sep="")

print("結果 :\n", accu_history, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
200811-201811d.csv # 100 筆資料 14 欄
SO2,CO,O3,PM25,Nox,NO,NO2,THC,NMHC,CH4,WindSpeed,TEMP,Humidity,Danger
4.4,0.47,32.2,31,24,3.46,20.84,2.309,0.231,2.078,1.91,24.86,77.11,0
6.4,0.52,30.2,32,32,5.64,26.3,2.186,0.227,1.959,1.72,26.58,71.93,0
3.2,0.45,30.5,46,20,2.36,18.05,0,0,0,2.08,24.75,76.33,1
5.2,0.47,32.5,38,24,3.18,20.64,2.374,0.225,2.15,1.66,24.97,79.97,1
"""

df = pd.read_csv("data/200811-201811d.csv")

print("df之大小 :", df.shape)

cc = df[df.PM25 > 30]
print("cc之大小 :", cc.shape)

cc = df[df["PM25"] > 30]
print("cc之大小 :", cc.shape)

# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

# df資料14欄，取出13欄當X，取出1欄當y
X = df.drop("Danger", axis=1)
y = df["Danger"]  # 目標, 0 : 不危險, 1 : 危險

print("資料 X 之大小 :", X.shape)
print("目標 y 之大小 :", y.shape)
print(y)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression(
    solver="liblinear"
)  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict
print("y_pred :\n", y_pred, sep="")

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

cc = classification_report(y_test, y_pred)
print("分類報告 :\n", cc, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectKBest 單變數特徵選取(Univariate feature selection)
# SelectKBest 挑選出K個分數最高的特徵

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)
print(X.shape)  # 150 X 4

# SelectKBest 特徵選取

logistic_regression = SelectKBest(chi2, k=2)
X_new = logistic_regression.fit_transform(X, y)
print(X_new.shape)  # 150 X 2

print("顯示特徵分數")
cc = logistic_regression.scores_
print(cc)

print("顯示 p value")
cc = logistic_regression.pvalues_
print(cc)

# 顯示特徵名稱
print("鳶尾花資料集")
iris = datasets.load_iris()
cc = np.array(iris.feature_names)[logistic_regression.scores_.argsort()[-2:][::-1]]
print(cc)

X = pd.DataFrame(iris.data, columns=iris.feature_names)
logistic_regression = SelectKBest(chi2, k=2)
X_new = logistic_regression.fit_transform(X, y)
cc = logistic_regression.get_feature_names_out()
print(cc)

# 選擇2個特徵
X = X[logistic_regression.get_feature_names_out()].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print("y_pred :\n", y_pred, sep="")

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
show()

# 使用全部特徵
print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 遞迴特徵消去法(Recursive feature elimination, RFE)

from sklearn.feature_selection import RFE
from sklearn.svm import SVC

print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# RFE 特徵選取

svc = SVC(kernel="linear", C=1)

clf = RFE(estimator=svc, n_features_to_select=2, step=1)

X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 特徵重要性排名
print(clf.ranking_)

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print("y_pred :\n", y_pred, sep="")

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("自建 邏輯迴歸")

# logistic_regression_SGD
# 以梯度下降法求解羅吉斯迴歸

iris = datasets.load_iris()

# 只取前兩個特徵，方便繪圖
X = iris.data[:, :2]
# 只取前兩個類別
y = (iris.target != 0) * 1

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
show()

# 建立羅吉斯迴歸類別


class MyLogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    # 加入偏差項(1)至X
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    # 羅吉斯函數
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # 損失函數
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    # 以梯度下降法訓練模型
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        # 權重初始值給 0
        self.theta = np.zeros(X.shape[1])

        # 正向傳導與反向傳導
        for i in range(self.num_iter):
            # WX
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            # 梯度
            gradient = np.dot(X.T, (h - y)) / y.size
            # 更新權重
            self.theta -= self.lr * gradient

            # 依據更新的權重計算損失
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

            # 列印損失
            if self.verbose == True and i % 10000 == 0:
                print(f"loss: {loss} \t")

    # 預測機率
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    # 預測
    def predict(self, X):
        return self.predict_prob(X).round()


# 做邏輯迴歸, 自建模型
logistic_regression = MyLogisticRegression(lr=0.1, num_iter=300000)  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict
print("全預測 :")
print(y_pred)

cc = (y_pred == y).mean()
print(cc)

print("羅吉斯迴歸係數")
print(logistic_regression.theta)
# array([-25.89066442,  12.523156  , -13.40150447])

# 分類結果繪圖
plt.figure(figsize=(10, 6))

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
x1_min, x1_max = (
    X[:, 0].min(),
    X[:, 0].max(),
)
x2_min, x2_max = (
    X[:, 1].min(),
    X[:, 1].max(),
)
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]

y_pred = logistic_regression.predict_prob(grid).reshape(xx1.shape)

plt.contour(xx1, xx2, y_pred, [0.5], linewidths=1, colors="black")
show()

# 以 Scikit-learn 驗證

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression(C=1e20)  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict
print("全預測 :")
print(y_pred)

cc = (y_pred == y).mean()
print(cc)

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
x1_min, x1_max = (
    X[:, 0].min(),
    X[:, 0].max(),
)
x2_min, x2_max = (
    X[:, 1].min(),
    X[:, 1].max(),
)
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
y_pred_prob = logistic_regression.predict_proba(grid)[:, 1].reshape(
    xx1.shape
)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

plt.contour(xx1, xx2, y_pred_prob, [0.5], linewidths=1, colors="black")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("邏輯迴歸(Logistic Regression)")

"""
Social_Network_Ads.csv # 400 筆資料 5 欄
User ID,Gender,Age,EstimatedSalary,Purchased
15624510,Male,19,19000,0
15810944,Male,35,20000,0
15668575,Female,26,43000,0
15603246,Female,27,57000,0
15694829,Female,32,150000,1
"""

df = pd.read_csv("data/Social_Network_Ads.csv")

print("df之大小 :", df.shape)

X = df.iloc[:, [2, 3]].values
Y = df.iloc[:, 4].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# 特征縮放 Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# 第二步：邏輯回歸模型

# 該項工作的庫將會是一個線性模型庫，之所以被稱為線性是因為邏輯回歸是一個線性分類器，
# 這意味著我們在二維空間中，我們兩類用戶（購買和不購買）將被一條直線分割。
# 然后導入邏輯回歸類。下一步我們將創建該類的對象，它將作為我們訓練集的分類器。

# 將邏輯回歸應用于訓練集
# Fitting Logistic Regression to the Training set

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
# 第3步：預測
# 預測測試集結果

y_pred = logistic_regression.predict(X_test)  # 預測.predict

# 第4步：評估預測

# 我們預測了測試集。 現在我們將評估邏輯回歸模型是否正確的學習和理解。
# 因此這個混淆矩陣將包含我們模型的正確和錯誤的預測。

# 生成混淆矩陣(Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)

print(cm)  # print confusion_matrix
print(classification_report(y_test, y_pred))  # print classification report

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    logistic_regression.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )

plt.title(" LOGISTIC(Training set)")
plt.xlabel(" Age")
plt.ylabel(" Estimated Salary")
plt.legend()

show()

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.contourf(
    X1,
    X2,
    logistic_regression.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )

plt.title(" LOGISTIC(Test set)")
plt.xlabel(" Age")
plt.ylabel(" Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_01_logistic_regression_validation

# 證明 Exp(log(x)) = x

for i in range(1, 101):
    assert round(math.e ** math.log(i), 6) == i

# 證明 log(1/x) = - log(x)

for i in range(1, 101):
    assert round(math.log(i), 6) == -round(math.log(1 / i), 6)

cc = math.log(100), -math.log(1 / 100)
print(cc)

# 計算羅吉斯函數的上限與下限

from sympy import *

x = symbols("x")
expr = 1 / (1 + np.e ** (-x))
limit(expr, x, -1000), limit(expr, x, np.inf)

# 不使用 limit

cc = 1 / (np.e**np.inf)
print(cc)

# 繪製羅吉斯函數
x = np.linspace(-6, 6, 101)
y = 1 / (1 + np.e ** (-x))
plt.plot(x, y)
plt.axhline(0, linestyle="-.", c="r")
plt.axhline(1, linestyle="-.", c="r")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_03_logistic_regression_attrition

# 員工流失預測

"""
WA_Fn-UseC_-HR-Employee-Attrition.csv # 1470 筆資料 35 欄
Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager
41,Yes,Travel_Rarely,1102,Sales,1,2,Life Sciences,1,1,2,Female,94,3,2,Sales Executive,4,Single,5993,19479,8,Y,Yes,11,3,1,80,0,8,0,1,6,4,0,5
49,No,Travel_Frequently,279,Research & Development,8,1,Life Sciences,1,2,3,Male,61,2,2,Research Scientist,2,Married,5130,24907,1,Y,No,23,4,4,80,1,10,3,3,10,7,1,7
37,Yes,Travel_Rarely,1373,Research & Development,2,2,Other,1,4,4,Male,92,2,1,Laboratory Technician,3,Single,2090,2396,6,Y,Yes,15,3,2,80,0,7,3,3,0,0,0,0
33,No,Travel_Frequently,1392,Research & Development,3,4,Life Sciences,1,5,4,Female,56,3,1,Research Scientist,3,Married,2909,23159,1,Y,Yes,11,3,3,80,0,8,3,3,8,7,3,0
27,No,Travel_Rarely,591,Research & Development,2,1,Medical,1,7,1,Male,40,3,1,Laboratory Technician,2,Married,3468,16632,9,Y,No,12,3,4,80,1,6,3,3,2,2,2,2
32,No,Travel_Frequently,1005,Research & Development,2,2,Life Sciences,1,8,4,Male,79,3,1,Laboratory Technician,4,Single,3068,11864,0,Y,No,13,3,3,80,0,8,2,2,7,7,3,6
59,No,Travel_Rarely,1324,Research & Development,3,3,Medical,1,10,3,Female,81,4,1,Laboratory Technician,1,Married,2670,9964,4,Y,Yes,20,4,1,80,3,12,3,2,1,0,0,0
"""

df = pd.read_csv("./data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
print("df之大小 :", df.shape)

# 2. 資料清理、資料探索與分析

cc = df.isna().sum()
print(cc)

# 觀察資料集彙總資訊

df.info()  # 這樣就已經把資料集彙總資訊印出來

# 描述統計量
cc = df.describe()
print(cc)

# y 各類別資料筆數統計
sns.countplot(x=df["Attrition"])
show()

# 以Pandas函數統計各類別資料筆數
cc = df["Attrition"].value_counts()
print(cc)

print("檢查與時間有關的特徵相關性")

# 設定關聯度上限為 0.4
max_corr = 0.4
time_params = [
    "Age",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]
# 計算關聯度
corr_df = df[time_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8, 5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(
        corr_df, mask=mask, vmax=max_corr, square=True, annot=True, cmap="YlGnBu"
    )
show()

# 刪除欄位
df.drop(
    {
        "TotalWorkingYears",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager",
    },
    axis=1,
    inplace=True,
)

print("檢查與薪資(Salary)有關的特徵相關性")

salary_params = [
    "DailyRate",
    "HourlyRate",
    "MonthlyIncome",
    "MonthlyRate",
    "PercentSalaryHike",
    "StockOptionLevel",
]
# 計算關聯度
corr_df = df[salary_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8, 5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(
        corr_df, mask=mask, vmax=max_corr, square=True, annot=True, cmap="YlGnBu"
    )
show()

print("找出所有類別變數，並顯示其類別")

df.select_dtypes("object").head()
print("Levels of categories: ")
for key in df.select_dtypes("object").keys():
    print(key, ":", df[key].unique())

print("進行One-hot encoding")

df2 = pd.get_dummies(
    df,
    columns=df.select_dtypes("object").keys(),
    prefix=df.select_dtypes("object").keys(),
)
cc = df2.keys()
print(cc)

print("刪除One-hot encoding的第一個類別欄位(base category)")

df2.drop(
    {
        "Attrition_No",
        "BusinessTravel_Non-Travel",
        "Department_Human Resources",
        "EducationField_Human Resources",
        "Gender_Female",
        "MaritalStatus_Single",
        "OverTime_No",
    },
    axis=1,
    inplace=True,
)
cont_vars = df2.select_dtypes("int").keys()
""" NG
dummies= df2.select_dtypes('uint8').keys().drop('Attrition_Yes') # 刪除目標變數(Y) 
print(dummies)
"""
print("指定特徵(X)及目標變數(Y)")

X = df2.drop("Attrition_Yes", axis=1)
y = df2["Attrition_Yes"]

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法、6. 模型訓練

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)

# 7. 模型評分

# 計算準確率
y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 90.14%

# 混淆矩陣
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

""" NG
#statsmodels 作法

import statsmodels.api as sm

model=sm.Logit(y_train, X_train)
result=model.fit()
print(result.summary())

#顯示權重資訊

stat_df=pd.DataFrame({'coefficients':result.params, 'p-value': result.pvalues,
                      'odds_ratio': np.exp(result.params)})
print(stat_df)

print("篩選重要的特徵變數")

significant_params=stat_df[stat_df['p-value']<=0.05].index
print(significant_params)

print("勝負比(Odds)")

cc = stat_df.loc[significant_params].sort_values('odds_ratio', ascending=False)['odds_ratio']
print(cc)
      
print("最後底定的模型：只保留重要的特徵變數")

y=df2['Attrition_Yes']
X=df2[significant_params]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model=sm.Logit(y_train,X_train)

result=model.fit()

print(result.summary())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
date_data.csv # 100 筆資料 8 欄
income,attractive,assets,edueduclass,Dated,income_rank,attractive_rank,assets_rank
3000,9,5.145476376,1,0,0,0,0
3000,14.5,40.643781041,4,1,0,0,1
3000,6,5.145476376,1,0,0,0,0
3000,1,7.0674341855,1,0,0,0,0
3500,14.5,3.7284,2,0,0,0,0
3500,28,12.569146178,3,0,0,1,0
3500,65.5,40.643781041,4,0,0,2,1
"""

df = pd.read_csv("data/date_data.csv")
print("df之大小 :", df.shape)

X = df.loc[:, "income":"assets"]
Y = df["Dated"]

# 資料分割
train_data, test_data, train_target, test_target = train_test_split(X, Y, test_size=0.2)

# 建模
logistic_model = linear_model.LogisticRegression()
logistic_model.fit(train_data, train_target)

test_est = logistic_model.predict(test_data)  # 預測.predict
train_est = logistic_model.predict(train_data)  # 預測.predict

test_est_p = logistic_model.predict_proba(test_data)[:, 1]  # 預測機率.predict_proba
train_est_p = logistic_model.predict_proba(train_data)[:, 1]  # 預測機率.predict_proba

# 决策（Decisions）类检验

print(metrics.classification_report(test_target, test_est))

metrics.accuracy_score(test_target, test_est)

# 排序（Rankings）类检验
# ROC曲线

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color="red")
plt.plot(fpr_train, tpr_train, color="black")
plt.title("ROC curve")

test_AUC = metrics.roc_auc_score(test_target, test_est_p)
train_AUC = metrics.roc_auc_score(train_target, train_est_p)
print("test_AUC:", test_AUC, "train_AUC:", train_AUC)

# KS曲线

test_x_axis = np.arange(len(fpr_test)) / float(len(fpr_test))
train_x_axis = np.arange(len(fpr_train)) / float(len(fpr_train))
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, test_x_axis, color="blue")
plt.plot(tpr_test, test_x_axis, color="red")
# plt.plot(fpr_train, train_x_axis, color=red)
# plt.plot(tpr_train, train_x_axis, color=red)
plt.title("KS curve")

show()

from scipy.stats import ks_2samp

ks_2samp(fpr_test, tpr_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# # 逻辑回归
# 信用风险建模案例
##数据说明：本数据是一份汽车贷款违约数据
##名称---中文含义
##application_id---申请者ID
##account_number---帐户号
##bad_ind---是否违约
##vehicle_year---汽车购买时间
##vehicle_make---汽车制造商
##bankruptcy_ind---曾经破产标识
##tot_derog---五年内信用不良事件数量(比如手机欠费消号)
##tot_tr---全部帐户数量
##age_oldest_tr---最久账号存续时间(月)
##tot_open_tr---在使用帐户数量
##tot_rev_tr---在使用可循环贷款帐户数量(比如信用卡)
##tot_rev_debt---在使用可循环贷款帐户余额(比如信用卡欠款)
##tot_rev_line---可循环贷款帐户限额(信用卡授权额度)
##rev_util---可循环贷款帐户使用比例(余额/限额)
##fico_score---FICO打分
##purch_price---汽车购买金额(元)
##msrp---建议售价
##down_pyt---分期付款的首次交款
##loan_term---贷款期限(月)
##loan_amt---贷款金额
##ltv---贷款金额/建议售价*100
##tot_income---月均收入(元)
##veh_mileage---行使历程(Mile)
##used_ind---是否二手车
##weight---样本权重

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 导入数据和数据清洗

accepts = pd.read_csv("data/accepts.csv").dropna()
print(accepts.shape)


##衍生变量:
def divMy(x, y):
    if x == np.nan or y == np.nan:
        return np.nan
    elif y == 0:
        return -1
    else:
        return x / y


divMy(1, 2)

##历史负债收入比:tot_rev_line/tot_income
accepts["dti_hist"] = accepts[["tot_rev_line", "tot_income"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##本次新增负债收入比:loan_amt/tot_income
accepts["dti_mew"] = accepts[["loan_amt", "tot_income"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##本次贷款首付比例:down_pyt/loan_amt
accepts["fta"] = accepts[["down_pyt", "loan_amt"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##新增债务比:loan_amt/tot_rev_debt
accepts["nth"] = accepts[["loan_amt", "tot_rev_debt"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)
##新增债务额度比:loan_amt/tot_rev_line
accepts["nta"] = accepts[["loan_amt", "tot_rev_line"]].apply(
    lambda x: divMy(x[0], x[1]), axis=1
)

cc = accepts.head()
print("前5筆資料 :\n", cc, sep="")

# 轉換資料型態
accepts.used_ind = accepts.used_ind.astype(float)
accepts.bad_ind = accepts.bad_ind.astype(float)

# 分类变量的相关关系

# 交叉表

cross_table = pd.crosstab(accepts.used_ind, accepts.bad_ind, margins=True)
# cross_table = pd.crosstab(accepts.bankruptcy_ind,accepts.bad_ind, margins=True)

print("交叉表 :\n", cross_table, sep="")

# 列聯表


def percConvert(ser):
    return ser / float(ser[-1])


cross_table.apply(percConvert, axis=1)

print("列聯表 :\n", cross_table, sep="")

cc = stats.chi2_contingency(cross_table.iloc[:2, :2])
print("chisq = %6.4f\np-value = %6.4f\ndof = %i\nexpected_freq = %s" % cc, sep="")

# 逻辑回归

accepts.plot(kind="scatter", x="age_oldest_tr", y="bad_ind")
plt.title("最久账号存续时间(月) 與 是否违约 的關係")
show()

# 随机抽样，建立训练集与测试集

train = accepts.sample(frac=0.7, random_state=1234).copy()
test = accepts[~accepts.index.isin(train.index)].copy()
print(" 训练集样本量: %i \n 测试集样本量: %i" % (len(train), len(test)))

lg = smf.glm(
    "bad_ind ~ age_oldest_tr",
    data=train,
    family=sm.families.Binomial(sm.families.links.logit()),
).fit()
lg.summary()

# 预测
train["proba"] = lg.predict(train)  # 預測.predict
test["proba"] = lg.predict(test)  # 預測.predict

test["proba"].head(10)

# 模型评估
# 设定阈值

test["prediction"] = (test["proba"] > 0.3).astype("int")

# 混淆矩阵
pd.crosstab(test.bad_ind, test.prediction, margins=True)

# 计算准确率
acc = sum(test["prediction"] == test["bad_ind"]) / np.float(len(test))
print("The accurancy is %.2f" % acc)

for i in np.arange(0.02, 0.3, 0.02):
    prediction = (test["proba"] > i).astype("int")
    confusion_matrix = pd.crosstab(prediction, test.bad_ind, margins=True)
    precision = confusion_matrix.loc[0, 0] / confusion_matrix.loc["All", 0]
    recall = confusion_matrix.loc[0, 0] / confusion_matrix.loc[0, "All"]
    Specificity = confusion_matrix.loc[1, 1] / confusion_matrix.loc[1, "All"]
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(
        "threshold: %s, precision: %.2f, recall:%.2f ,Specificity:%.2f , f1_score:%.2f"
        % (i, precision, recall, Specificity, f1_score)
    )

# 绘制ROC曲线
fpr_test, tpr_test, th_test = metrics.roc_curve(test.bad_ind, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.bad_ind, train.proba)

plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC 曲線")
show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 包含分类预测变量的逻辑回归
formula = """bad_ind ~ C(used_ind)"""

lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit())
).fit()
lg_m.summary()


# 多元逻辑回归
# 向前法
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = (
                smf.glm(
                    formula=formula,
                    data=data,
                    family=sm.families.Binomial(sm.families.links.logit()),
                )
                .fit()
                .aic
            )
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print("aic is {},continuing!".format(current_score))
        else:
            print("forward selection over!")
            break

    formula = "{} ~ {} ".format(response, " + ".join(selected))
    print("final formula is {}".format(formula))
    model = smf.glm(
        formula=formula,
        data=data,
        family=sm.families.Binomial(sm.families.links.logit()),
    ).fit()
    return model


# 只有连续变量可以进行变量筛选，分类变量需要进行WOE转换才可以进行变量筛选
candidates = [
    "bad_ind",
    "tot_derog",
    "age_oldest_tr",
    "tot_open_tr",
    "rev_util",
    "fico_score",
    "loan_term",
    "ltv",
    "veh_mileage",
    "dti_hist",
    "dti_mew",
    "fta",
    "nth",
    "nta",
]
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response="bad_ind")
lg_m1.summary()


# Seemingly wrong when using 'statsmmodels.stats.outliers_influence.variance_inflation_factor'


def vif(df, col_i):
    from statsmodels.formula.api import ols

    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


candidates = [
    "bad_ind",
    "fico_score",
    "ltv",
    "age_oldest_tr",
    "tot_derog",
    "nth",
    "tot_open_tr",
    "veh_mileage",
    "rev_util",
]
exog = train[candidates].drop(["bad_ind"], axis=1)

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))

train["proba"] = lg_m1.predict(train)  # 預測.predict
test["proba"] = lg_m1.predict(test)  # 預測.predict

fpr_test, tpr_test, th_test = metrics.roc_curve(test.bad_ind, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.bad_ind, train.proba)

plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC 曲線")
show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 目前vehicle_year、vehicle_make、bankruptcy_ind、used_ind这些分类变量无法通过逐步变量筛选法
# 解决方案：
# 1、逐一根据显著性测试
# 2、使用决策树等方法筛选变量，但是多分类变量需要事先进行变量概化
# 3、使用WOE转换，多分类变量也需要事先进行概化，使用scorecardpy包中的woe算法可以自动进行概化
# 使用第一种方法
# formula = """bad_ind ~ fico_score+ltv+age_oldest_tr+tot_derog+nth+tot_open_tr+veh_mileage+rev_util+C(used_ind)+C(vehicle_year)+C(bankruptcy_ind)"""
formula = """bad_ind ~ fico_score+ltv+age_oldest_tr+tot_derog+nth+tot_open_tr+veh_mileage+rev_util+C(bankruptcy_ind)"""
lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit())
).fit()
lg_m.summary()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


class WoE:
    """
    Basic functionality for WoE bucketing of continuous and discrete variables
    :param self.bins: DataFrame WoE transformed variable and all related statistics
    :param self.iv: Information Value of the transformed variable
    """

    def __init__(
        self,
        qnt_num=16,
        min_block_size=16,
        spec_values=None,
        v_type="c",
        bins=None,
        t_type="b",
    ):
        """
        :param qnt_num: Number of buckets (quartiles) for continuous variable split
        :param min_block_size: minimum number of observation in each bucket (continuous variables)
        :param spec_values: List or Dictionary {'label': value} of special values (frequent items etc.)
        :param v_type: 'c' for continuous variable, 'd' - for discrete
        :param bins: Predefined bucket borders for continuous variable split
        :t_type : Binary 'b' or continous 'c' target variable
        :return: initialized class
        """
        self.__qnt_num = qnt_num  # Num of buckets/quartiles
        self._predefined_bins = (
            None if bins is None else np.array(bins)
        )  # user bins for continuous variables
        self.type = v_type  # if 'c' variable should be continuous, if 'd' - discrete
        self._min_block_size = min_block_size  # Min num of observation in bucket
        self._gb_ratio = None  # Ratio of good and bad in the sample
        self.bins = None  # WoE Buckets (bins) and related statistics
        self.df = None  # Training sample DataFrame with initial data and assigned woe
        self.qnt_num = (
            None  # Number of quartiles used for continuous part of variable binning
        )
        self.t_type = t_type  # Type of target variable
        if (
            type(spec_values) == dict
        ):  # Parsing special values to dict for cont variables
            self.spec_values = {}
            for k, v in spec_values.items():
                if v.startswith("d_"):
                    self.spec_values[k] = v
                else:
                    self.spec_values[k] = "d_" + v
        else:
            if spec_values is None:
                self.spec_values = {}
            else:
                self.spec_values = {i: "d_" + str(i) for i in spec_values}

    def fit(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE class
        """
        # Data quality checks
        if not isinstance(x, pd.Series) or not isinstance(y, pd.Series):
            raise TypeError("pandas.Series type expected")
        if not x.size == y.size:
            raise Exception("Y size don't match Y size")
        # Calc total good bad ratio in the sample
        t_bad = np.sum(y)
        if t_bad == 0 or t_bad == y.size:
            raise ValueError("There should be BAD and GOOD observations in the sample")
        if np.max(y) > 1 or np.min(y) < 0:
            raise ValueError("Y range should be between 0 and 1")
        # setting discrete values as special values
        if self.type == "d":
            sp_values = {i: "d_" + str(i) for i in x.unique()}
            if len(sp_values) > 100:
                raise type(
                    "DiscreteVarOverFlowError",
                    (Exception,),
                    {
                        "args": (
                            "Discrete variable with too many unique values (more than 100)",
                        )
                    },
                )
            else:
                if self.spec_values:
                    sp_values.update(self.spec_values)
                self.spec_values = sp_values
        # Make data frame for calculations
        df = pd.DataFrame({"X": x, "Y": y, "order": np.arange(x.size)})
        # Separating NaN and Special values
        df_sp_values, df_cont = self._split_sample(df)
        # # labeling data
        df_cont, c_bins = self._cont_labels(df_cont)
        df_sp_values, d_bins = self._disc_labels(df_sp_values)
        # getting continuous and discrete values together
        self.df = df_sp_values.append(df_cont)
        self.bins = d_bins.append(c_bins)
        # calculating woe and other statistics
        self._calc_stat()
        # sorting appropriately for further cutting in transform method
        self.bins.sort_values("bins", inplace=True)
        # returning to original observation order
        self.df.sort_values("order", inplace=True)
        self.df.set_index(x.index, inplace=True)
        return self

    def fit_transform(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE transformed variable
        """
        self.fit(x, y)
        return self.df["woe"]

    def _split_sample(self, df):
        if self.type == "d":
            return df, None
        sp_values_flag = (
            df["X"].isin(self.spec_values.keys()).values | df["X"].isnull().values
        )
        df_sp_values = df[sp_values_flag].copy()
        df_cont = df[np.logical_not(sp_values_flag)].copy()
        return df_sp_values, df_cont

    def _disc_labels(self, df):
        df["labels"] = df["X"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        d_bins = pd.DataFrame({"bins": df["X"].unique()})
        d_bins["labels"] = d_bins["bins"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        return df, d_bins

    def _cont_labels(self, df):
        # check whether there is a continuous part
        if df is None:
            return None, None
        # Max buckets num calc
        self.qnt_num = (
            int(
                np.minimum(df["X"].unique().size / self._min_block_size, self.__qnt_num)
            )
            + 1
        )
        # cuts - label num for each observation, bins - quartile thresholds
        bins = None
        cuts = None
        if self._predefined_bins is None:
            try:
                cuts, bins = pd.qcut(df["X"], self.qnt_num, retbins=True, labels=False)
            except ValueError as ex:
                if ex.args[0].startswith("Bin edges must be unique"):
                    ex.args = (
                        "Please reduce number of bins or encode frequent items as special values",
                    ) + ex.args
                    raise
            bins = np.append((-float("inf"),), bins[1:-1])
        else:
            bins = self._predefined_bins
            if bins[0] != float("-Inf"):
                bins = np.append((-float("inf"),), bins)
            cuts = pd.cut(
                df["X"],
                bins=np.append(bins, (float("inf"),)),
                labels=np.arange(len(bins)).astype(str),
            )
        df["labels"] = cuts.astype(str)
        c_bins = pd.DataFrame(
            {"bins": bins, "labels": np.arange(len(bins)).astype(str)}
        )
        return df, c_bins

    def _calc_stat(self):
        # calculating WoE
        stat = (
            self.df.groupby("labels")["Y"]
            .agg({"mean": np.mean, "bad": np.count_nonzero, "obs": np.size})
            .copy()
        )
        if self.t_type != "b":
            stat["bad"] = stat["mean"] * stat["obs"]
        stat["good"] = stat["obs"] - stat["bad"]
        t_good = np.maximum(stat["good"].sum(), 0.5)
        t_bad = np.maximum(stat["bad"].sum(), 0.5)
        stat["woe"] = stat.apply(self._bucket_woe, axis=1) + np.log(t_good / t_bad)
        iv_stat = (stat["bad"] / t_bad - stat["good"] / t_good) * stat["woe"]
        self.iv = iv_stat.sum()
        # adding stat data to bins
        self.bins = pd.merge(stat, self.bins, left_index=True, right_on=["labels"])
        label_woe = self.bins[["woe", "labels"]].drop_duplicates()
        self.df = pd.merge(self.df, label_woe, left_on=["labels"], right_on=["labels"])

    def transform(self, x):
        """
        Transforms input variable according to previously fitted rule
        :param x: input variable
        :return: DataFrame with transformed with original and transformed variables
        """
        if not isinstance(x, pd.Series):
            raise TypeError("pandas.Series type expected")
        if self.bins is None:
            raise Exception("Fit the model first, please")
        df = pd.DataFrame({"X": x, "order": np.arange(x.size)})
        # splitting to discrete and continous pars
        df_sp_values, df_cont = self._split_sample(df)

        # function checks existence of special values, raises error if sp do not exist in training set
        def get_sp_label(x_):
            if x_ in self.spec_values.keys():
                return self.spec_values[x_]
            else:
                str_x = "d_" + str(x_)
                if str_x in list(self.bins["labels"]):
                    return str_x
                else:
                    raise ValueError(
                        "Value " + str_x + " does not exist in the training set"
                    )

        # assigning labels to discrete part
        df_sp_values["labels"] = df_sp_values["X"].apply(get_sp_label)
        # assigning labels to continuous part
        c_bins = self.bins[self.bins["labels"].apply(lambda z: not z.startswith("d_"))]
        if not self.type == "d":
            cuts = pd.cut(
                df_cont["X"],
                bins=np.append(c_bins["bins"], (float("inf"),)),
                labels=c_bins["labels"],
            )
            df_cont["labels"] = cuts.astype(str)
        # Joining continuous and discrete parts
        df = df_sp_values.append(df_cont)
        # assigning woe
        df = pd.merge(
            df, self.bins[["woe", "labels"]], left_on=["labels"], right_on=["labels"]
        )
        # returning to original observation order
        df.sort_values("order", inplace=True)
        return df.set_index(x.index)

    def merge(self, label1, label2=None):
        """
        Merge of buckets with given labels
        In case of discrete variable, both labels should be provided. As the result labels will be marget to one bucket.
        In case of continous variable, only label1 should be provided. It will be merged with the next label.
        :param label1: first label to merge
        :param label2: second label to merge
        :return:
        """
        spec_values = self.spec_values.copy()
        c_bins = self.bins[
            self.bins["labels"].apply(lambda x: not x.startswith("d_"))
        ].copy()
        if label2 is None and not label1.startswith(
            "d_"
        ):  # removing bucket for continuous variable
            c_bins = c_bins[c_bins["labels"] != label1]
        else:
            if not (label1.startswith("d_") and label2.startswith("d_")):
                raise Exception("Labels should be discrete simultaneously")
            bin1 = self.bins[self.bins["labels"] == label1]["bins"].iloc[0]
            bin2 = self.bins[self.bins["labels"] == label2]["bins"].iloc[0]
            spec_values[bin1] = label1 + "_" + label2
            spec_values[bin2] = label1 + "_" + label2
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            spec_values,
            self.type,
            c_bins["bins"],
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    def plot(self, figsize):
        """
        Plot WoE transformation and default rates
        :return: plotting object
        """
        index = np.arange(self.bins.shape[0])
        bar_width = 0.8
        woe_fig = plt.figure(figsize=figsize)
        plt.title("Number of Observations and WoE per bucket")
        ax = woe_fig.add_subplot(111)
        ax.set_ylabel("Observations")
        plt.xticks(index + bar_width / 2, self.bins["labels"])
        plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
        ax2 = ax.twinx()
        ax2.set_ylabel("Weight of Evidence")
        ax2.plot(
            index + bar_width / 2,
            self.bins["woe"],
            "bo-",
            linewidth=4.0,
            color="r",
            label="WoE",
        )
        handles1, labels1 = ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles = handles1 + handles2
        labels = labels1 + labels2
        plt.legend(handles, labels)
        woe_fig.autofmt_xdate()
        return woe_fig

    def optimize(self, criterion=None, fix_depth=None, max_depth=None, cv=3):
        """
        WoE bucketing optimization (continuous variables only)
        :param criterion: binary tree split criteria
        :param fix_depth: use tree of a fixed depth (2^fix_depth buckets)
        :param max_depth: maximum tree depth for a optimum cross-validation search
        :param cv: number of cv buckets
        :return: WoE class with optimized continuous variable split
        """
        if self.t_type == "b":
            tree_type = tree.DecisionTreeClassifier
        else:
            tree_type = tree.DecisionTreeRegressor
        m_depth = int(np.log2(self.__qnt_num)) + 1 if max_depth is None else max_depth
        cont = self.df["labels"].apply(lambda z: not z.startswith("d_"))
        x_train = np.array(self.df[cont]["X"])
        y_train = np.array(self.df[cont]["Y"])
        x_train = x_train.reshape(x_train.shape[0], 1)
        start = 1
        cv_scores = []
        if fix_depth is None:
            for i in range(start, m_depth):
                if criterion is None:
                    d_tree = tree_type(max_depth=i)
                else:
                    d_tree = tree_type(criterion=criterion, max_depth=i)
                scores = cross_val_score(d_tree, x_train, y_train, cv=cv)
                cv_scores.append(scores.mean())
            best = np.argmax(cv_scores) + start
        else:
            best = fix_depth
        final_tree = tree_type(max_depth=best)
        final_tree.fit(x_train, y_train)
        opt_bins = final_tree.tree_.threshold[final_tree.tree_.threshold > 0]
        opt_bins = np.sort(opt_bins)
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            self.spec_values,
            self.type,
            opt_bins,
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    @staticmethod
    def _bucket_woe(x):
        t_bad = x["bad"]
        t_good = x["good"]
        t_bad = 0.5 if t_bad == 0 else t_bad
        t_good = 0.5 if t_good == 0 else t_good
        return np.log(t_bad / t_good)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#拒绝推断" data-toc-modified-id="拒绝推断-0.1"><span class="toc-item-num">0.1&nbsp;&nbsp;</span>拒绝推断</a></span><ul class="toc-item"><li><span><a href="#第一步准备数据集：把解释变量和被解释变量分开，这是KNN这个函数的要求" data-toc-modified-id="第一步准备数据集：把解释变量和被解释变量分开，这是KNN这个函数的要求-0.1.1"><span class="toc-item-num">0.1.1&nbsp;&nbsp;</span>第一步准备数据集：把解释变量和被解释变量分开，这是KNN这个函数的要求</a></span></li><li><span><a href="#第二步：进行缺失值填补和标准化，这也是knn这个函数的要求" data-toc-modified-id="第二步：进行缺失值填补和标准化，这也是knn这个函数的要求-0.1.2"><span class="toc-item-num">0.1.2&nbsp;&nbsp;</span>第二步：进行缺失值填补和标准化，这也是knn这个函数的要求</a></span></li><li><span><a href="#第三步：建模并预测" data-toc-modified-id="第三步：建模并预测-0.1.3"><span class="toc-item-num">0.1.3&nbsp;&nbsp;</span>第三步：建模并预测</a></span></li><li><span><a href="#第四步：将审核通过的申请者和未通过的申请者进行合并" data-toc-modified-id="第四步：将审核通过的申请者和未通过的申请者进行合并-0.1.4"><span class="toc-item-num">0.1.4&nbsp;&nbsp;</span>第四步：将审核通过的申请者和未通过的申请者进行合并</a></span></li></ul></li><li><span><a href="#建立违约预测模型" data-toc-modified-id="建立违约预测模型-0.2"><span class="toc-item-num">0.2&nbsp;&nbsp;</span>建立违约预测模型</a></span><ul class="toc-item"><li><span><a href="#粗筛变量" data-toc-modified-id="粗筛变量-0.2.1"><span class="toc-item-num">0.2.1&nbsp;&nbsp;</span>粗筛变量</a></span></li><li><span><a href="#变量细筛与数据清洗" data-toc-modified-id="变量细筛与数据清洗-0.2.2"><span class="toc-item-num">0.2.2&nbsp;&nbsp;</span>变量细筛与数据清洗</a></span></li><li><span><a href="#变量分箱WOE转换" data-toc-modified-id="变量分箱WOE转换-0.2.3"><span class="toc-item-num">0.2.3&nbsp;&nbsp;</span>变量分箱WOE转换</a></span></li><li><span><a href="#构造分类模型" data-toc-modified-id="构造分类模型-0.2.4"><span class="toc-item-num">0.2.4&nbsp;&nbsp;</span>构造分类模型</a></span></li><li><span><a href="#检验模型" data-toc-modified-id="检验模型-0.2.5"><span class="toc-item-num">0.2.5&nbsp;&nbsp;</span>检验模型</a></span></li><li><span><a href="#评分卡开发" data-toc-modified-id="评分卡开发-0.2.6"><span class="toc-item-num">0.2.6&nbsp;&nbsp;</span>评分卡开发</a></span></li></ul></li></ul></li></ul></div>

# get_ipython().magic('matplotlib inline')

accepts = pd.read_csv("data/accepts.csv")
rejects = pd.read_csv("data/rejects.csv")

"""
#信用风险建模案例
##数据说明：本数据是一份汽车贷款违约数据
##名称---中文含义
##application_id---申请者ID
##account_number---帐户号
##bad_ind---是否违约
##vehicle_year---汽车购买时间
##vehicle_make---汽车制造商
##bankruptcy_ind---曾经破产标识
##tot_derog---五年内信用不良事件数量(比如手机欠费消号)
##tot_tr---全部帐户数量
##age_oldest_tr---最久账号存续时间(月)
##tot_open_tr---在使用帐户数量
##tot_rev_tr---在使用可循环贷款帐户数量(比如信用卡)
##tot_rev_debt---在使用可循环贷款帐户余额(比如信用卡欠款)
##tot_rev_line---可循环贷款帐户限额(信用卡授权额度)
##rev_util---可循环贷款帐户使用比例(余额/限额)
##fico_score---FICO打分
##purch_price---汽车购买金额(元)
##msrp---建议售价
##down_pyt---分期付款的首次交款
##loan_term---贷款期限(月)
##loan_amt---贷款金额
##ltv---贷款金额/建议售价*100
##tot_income---月均收入(元)
##veh_mileage---行使历程(Mile)
##used_ind---是否使用
##weight---样本权重
"""

##################################################################################################################
# ## 一、拒绝推断

# ### 第一步准备数据集：把解释变量和被解释变量分开，这是KNN这个函数的要求

# 取出部分变量用于做KNN：由于KNN算法要求使用连续变量，因此仅选了部分重要的连续变量用于做KNN模型
accepts_x = accepts[["tot_derog", "age_oldest_tr", "rev_util", "fico_score", "ltv"]]

accepts_y = accepts["bad_ind"]

rejects_x = rejects[["tot_derog", "age_oldest_tr", "rev_util", "fico_score", "ltv"]]

# ### 第二步：进行缺失值填补和标准化，这也是knn这个函数的要求

# 查看一下数据集的信息
rejects_x.info()


## 定义缺失值替换函数
def Myfillna_median(df):
    for i in df.columns:
        median = df[i].median()
        df[i].fillna(value=median, inplace=True)
    return df


# 缺失值填补
accepts_x_filled = Myfillna_median(df=accepts_x)

rejects_x_filled = Myfillna_median(df=rejects_x)

# 标准化数据
accepts_x_norm = pd.DataFrame(Normalizer().fit_transform(accepts_x_filled))
accepts_x_norm.columns = accepts_x_filled.columns

rejects_x_norm = pd.DataFrame(Normalizer().fit_transform(rejects_x_filled))
rejects_x_norm.columns = rejects_x_filled.columns

# ### 第三步：建模并预测

# 利用knn模型进行预测，做拒绝推断
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=5, weights="distance")
neigh.fit(accepts_x_norm, accepts_y)

rejects["bad_ind"] = neigh.predict(rejects_x_norm)  # 預測.predict

# ### 第四步：将审核通过的申请者和未通过的申请者进行合并

# accepts的数据是针对于违约用户的过度抽样
# 因此，rejects也要进行同样比例的抽样

rejects_res = rejects[rejects["bad_ind"] == 0].sample(1340)
rejects_res = pd.concat([rejects_res, rejects[rejects["bad_ind"] == 1]], axis=0)

data = pd.concat([accepts.iloc[:, 2:-1], rejects_res.iloc[:, 1:]], axis=0)

##################################################################################################################
# ## 二、建立违约预测模型

# ### 粗筛变量

# 分类变量转换
bankruptcy_dict = {"N": 0, "Y": 1}
data.bankruptcy_ind = data.bankruptcy_ind.map(bankruptcy_dict)

# 盖帽法处理年份变量中的异常值，并将年份其转化为距现在多长时间
# 此处只是一个示例，所有连续变量都要按此方法进行处理
year_min = data.vehicle_year.quantile(0.1)
year_max = data.vehicle_year.quantile(0.99)
data.vehicle_year = data.vehicle_year.map(lambda x: year_min if x <= year_min else x)
data.vehicle_year = data.vehicle_year.map(lambda x: year_max if x >= year_max else x)

data.vehicle_year = data.vehicle_year.map(lambda x: 2018 - x)

data.drop(["vehicle_make"], axis=1, inplace=True)

data_filled = Myfillna_median(df=data)

X = data_filled[
    [
        "age_oldest_tr",
        "bankruptcy_ind",
        "down_pyt",
        "fico_score",
        "loan_amt",
        "loan_term",
        "ltv",
        "msrp",
        "purch_price",
        "rev_util",
        "tot_derog",
        "tot_income",
        "tot_open_tr",
        "tot_rev_debt",
        "tot_rev_line",
        "tot_rev_tr",
        "tot_tr",
        "used_ind",
        "veh_mileage",
        "vehicle_year",
    ]
]
y = data_filled["bad_ind"]

# 利用随机森林填补变量
clf = RandomForestClassifier(max_depth=5, random_state=0)
clf.fit(X, y)

importances = list(clf.feature_importances_)
importances_order = importances.copy()
importances_order.sort(reverse=True)

cols = list(X.columns)
col_top = []
for i in importances_order[:9]:
    col_top.append((i, cols[importances.index(i)]))
col_top

col = [i[1] for i in col_top]

# ### 变量细筛与数据清洗

data_filled.head()

iv_c = {}
for i in col:
    try:
        iv_c[i] = (
            WoE(v_type="c").fit(data_filled[i], data_filled["bad_ind"]).optimize().iv
        )
    except:
        print(i)

pd.Series(iv_c).sort_values(ascending=False)

""" NG
# ### 变量分箱WOE转换

WOE_c = data_filled[col].apply(lambda col:WoE(v_type='c',qnt_num=5).fit(col,data_filled['bad_ind']).optimize().fit_transform(col,data_filled['bad_ind']))

WOE_c.head()

# ### 构造分类模型

# 資料分割

X = WOE_c
y = data_filled['bad_ind']

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)


def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    #This function prints and plots the confusion matrix.
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


# 构建逻辑回归模型，进行违约概率预测
lr = LogisticRegression(C = 1, penalty = 'l1')
lr.fit(X_train,y_train.values.ravel())
y_pred = lr.predict(X_test.values)  # 預測.predict

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test,y_pred)
np.set_printoptions(precision=2)

print("Recall metric in the testing dataset: ", cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

# Plot non-normalized confusion matrix
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix
                      , classes=class_names
                      , title='Confusion matrix')
show()


## 加入代价敏感参数，重新计算
lr = LogisticRegression(C = 1, penalty = 'l1', class_weight='balanced')
lr.fit(X_train,y_train.values.ravel())
y_pred = lr.predict(X_test.values)  # 預測.predict

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test,y_pred)
np.set_printoptions(precision=2)

print("Recall metric in the testing dataset: ", cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

# Plot non-normalized confusion matrix
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix
                      , classes=class_names
                      , title='Confusion matrix')
show()

# ### 检验模型

fpr,tpr,threshold = roc_curve(y_test,y_pred, drop_intermediate=False) ###计算真正率和假正率  
roc_auc = auc(fpr,tpr) ###计算auc的值  
  
plt.figure()  
lw = 2  
plt.figure(figsize=(10,10))  
plt.plot(fpr, tpr, color='darkorange',  
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc) ###假正率为横坐标，真正率为纵坐标做曲线  
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')  
plt.xlim([0.0, 1.0])  
plt.ylim([0.0, 1.05])  
plt.xlabel('False Positive Rate')  
plt.ylabel('True Positive Rate')  
plt.title('Receiver operating characteristic example')  
plt.legend(loc="lower right")  
show()

# 利用sklearn.metrics中的roc_curve算出tpr，fpr作图

fig, ax = plt.subplots()
ax.plot(1 - threshold, tpr, label='tpr') # ks曲线要按照预测概率降序排列，所以需要1-threshold镜像
ax.plot(1 - threshold, fpr, label='fpr')
ax.plot(1 - threshold, tpr-fpr,label='KS')
plt.xlabel('score')
plt.title('KS Curve')
#plt.xticks(np.arange(0,1,0.2), np.arange(1,0,-0.2))
#plt.xticks(np.arange(0,1,0.2), np.arange(score.max(),score.min(),-0.2*(data['反欺诈评分卡总分'].max() - data['反欺诈评分卡总分'].min())))
plt.figure(figsize=(20,20))
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')

show()
"""

print("測試使用 WoE()")

# Set target type: 'b' for default/non-default, 'c' for continous pd values
t_type_ = "c"
# Set sample size
N = 20
# Random variables
x1 = np.random.rand(N)
x2 = np.random.rand(N)
if t_type_ == "b":
    y_ = np.where(
        np.random.rand(
            N,
        )
        + x1
        + x2
        > 2,
        1,
        0,
    )
else:
    y_ = np.random.rand(N) + x1 + x2
    y_ = (y_ - np.min(y_)) / (np.max(y_) - np.min(y_)) / 2
# Inserting special values
x1[0:20] = float("nan")
x1[30:50] = float(0)
x1[60:80] = float(1)
x2[0:20] = float("nan")
# Initialize WoE object
woe_def = WoE()
woe = WoE(7, 30, spec_values={0: "0", 1: "1"}, v_type="c", t_type=t_type_)
# Transform x1
""" NG
woe.fit(pd.Series(x1), pd.Series(y_))
# Transform x2 using x1 transformation rules
woe.transform(pd.Series(x2))
# Optimize x1 transformation using tree with maximal depth = 5 (optimal depth is chosen by cross-validation)
woe2 = woe.optimize(max_depth=5)
# Merge discrete buckets
woe3 = woe.merge('d_0', 'd_1')
# Merge 2 and 3 continuous buckets
woe4 = woe3.merge('2')
# Print Statistics
print(woe.bins)
# print(woe2.bins)
# print(woe3.bins)
print(woe4.bins)
# Plot and show WoE graph
fig = woe.plot()
plt.show(fig)
fig = woe2.plot()
plt.show(fig)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------")  # 30個

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit
# .fit之後, 取得迴歸係數

print(logistic_regression.coef_)
print(logistic_regression.intercept_)
print(logistic_regression.classes_)

# yy = np.array([-5, -4, -3, -2, -1, 0, 1, 2 ,3, 4, 5])  # 真實資料
# YY = yy.reshape(len(yy), 1)


# 用heatmap(.isnull())來找出缺失的資料在哪些欄位
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
show()
