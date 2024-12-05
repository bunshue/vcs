"""
Iris 鳶尾花
Iris 鳶尾花數據庫 150筆資料 4個欄位 3種品種 每種50筆資料

花萼長度(Sepal.Length)
花萼寬度(Sepal.Width)
花瓣長度(Petal.Length)
花瓣寬度(Petal.Width)。
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
['setosa' 'versicolor' 'virginica']

#鳶尾花(Iris)品種的辨識

標準的分類問題: 這是哪種鳶尾花

鳶尾花 (Iris)  數據庫是很有名的資料,
就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。

我們現在來看看, 可不可以讓電腦辨識, 這是哪個亞種的鳶尾花?

在 sklearn.datasets 有幾個數據庫可以提供給大家玩玩。

以Iris dataset為例，鳶尾花資料集是非常著名的生物資訊資料集之一，
取自美國加州大學歐文分校的機器學習資料庫http://archive.ics.uci.edu/ml/datasets/Iris
資料的筆數為150筆，共有五個欄位：
#sepal_length, sepal_width, petal_length, petal_width, species
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
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
from common1 import *
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

print("所有資料 :", iris)
print("data :", iris.data)
print("target :", iris.target)
print("target_names :", iris.target_names)
print("DESCR :", iris.DESCR)
print("feature_names :", iris.feature_names)
print("filename :", iris.filename)
print("data_module :", iris.data_module)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/iris_sample.csv"

iris = pd.read_csv(filename)

print("資料")
print(iris)

print("資料shape")
print(iris.shape)

print("資料.type")
print(type(iris))

print("size")
print(np.unique(iris["花萼長度"].values).size)
print()

cccc = np.where(iris["類別"] == "versicolor", 1, 0)
print("抓出versicolor :", cccc)
print()

color = ["r", "y", "b"]
species = ["Setosa", "Versicolour", "Virginica"]
Setosa = []
Versicolour = []
Virginica = []

print(type(iris))
print(len(iris))
print(iris.shape)

# sepal_length,sepal_width,petal_length,petal_width,species
print(iris["花萼長度"])

print(len(iris["花萼長度"]))

print(iris["花萼長度"][0])

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == "setosa":
        Setosa.append(1)
        Versicolour.append(0)
        Virginica.append(0)
    elif iris["類別"][i] == "versicolor":
        Setosa.append(0)
        Versicolour.append(1)
        Virginica.append(0)
    elif iris["類別"][i] == "virginica":
        Setosa.append(0)
        Versicolour.append(0)
        Virginica.append(1)

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/iris_sample.csv"

iris = pd.read_csv(filename)
# print('全部資料')
# print(iris)

print("資料.shape :", iris.shape)
print("資料.type :", type(iris))
print("資料.長度 :", len(iris))
print("資料.head()")
print(iris.head())

print("花萼長度資料 :")
print(iris["花萼長度"])
print()
print("花萼長度資料長度 :", len(iris["花萼長度"]))
print("花萼長度資料之第 0 筆資料 :", iris["花萼長度"][0])

print("花萼長度 不同的數字 size :", np.unique(iris["花萼長度"].values).size)
print("花萼寬度 不同的數字 size :", np.unique(iris["花萼寬度"].values).size)
print("花瓣長度 不同的數字 size :", np.unique(iris["花瓣長度"].values).size)
print("花瓣寬度 不同的數字 size :", np.unique(iris["花瓣寬度"].values).size)
print("花萼長度 :")
print(iris["花萼長度"].values)
print("花萼寬度 :")
print(iris["花萼寬度"].values)
print("花瓣長度 :")
print(iris["花瓣長度"].values)
print("花瓣寬度 :")
print(iris["花瓣寬度"].values)

class1 = np.where(iris["類別"] == "setosa", 1, 0)
print("抓出versicolor :", class1)
class2 = np.where(iris["類別"] == "versicolor", 1, 0)
print("抓出versicolor :", class2)
class3 = np.where(iris["類別"] == "virginica", 1, 0)
print("抓出versicolor :", class3)

Setosa = []
Versicolour = []
Virginica = []

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == "setosa":
        Setosa.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )
    elif iris["類別"][i] == "versicolor":
        Versicolour.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )
    elif iris["類別"][i] == "virginica":
        Virginica.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

plt.scatter(
    x=np.array(Setosa)[:, 0],  # Setosa种类的花瓣的长度
    y=np.array(Setosa)[:, 1],  # Setosa种类的花瓣的宽度
    s=80,
    c="red",
    label="Setosa",
)

plt.scatter(
    x=np.array(Versicolour)[:, 0],  # Versicolour种类的花瓣的长度
    y=np.array(Versicolour)[:, 1],  # Versicolour种类的花瓣的宽度
    s=50,
    c="green",
    label="Versicolour",
)

plt.scatter(
    x=np.array(Virginica)[:, 0],  # Virginica种类的花瓣的长度
    y=np.array(Virginica)[:, 1],  # Virginica种类的花瓣的宽度
    s=20,
    c="blue",
    label="Virginica",
)

# 添加轴标签和标题
plt.title("花瓣长度与宽度的关系", fontsize=20)
plt.xlabel("花瓣的长度", fontsize=15)
plt.ylabel("花瓣的宽度", fontsize=15)
plt.legend(loc="best")  # 添加图例

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import matplotlib as mpl

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_format)
# 设置x轴显示多少个日期刻度
# xlocator = mpl.ticker.LinearLocator(10)
# 设置x轴每个刻度的间隔天数
xlocator = mpl.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)
# 为了避免x轴刻度标签的紧凑，将刻度标签旋转45度
plt.xticks(rotation = 45)

# 添加y轴标签
plt.ylabel('人数')
# 添加图形标题
plt.title('每天微信文章阅读人数与人次趋势')
# 添加图例Virginica
plt.legend()
# 显示图形
show()
"""


"""
# 读入数据
iris = pd.read_csv(r'F:\\python_Data_analysis_and_mining\\06\\iris.csv')
print(iris.shape)Virginica
# 绘制散点图
plt.scatter(x = iris.Petal_Width, # 指定散点图的x轴数据
y = iris.Petal_Length, # 指定散点图的y轴数据
color = 'steelblue' # 指定散点图中点的颜色
)
# 添加x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
show()

# Pandas模块绘制散点图
# 绘制散点图Virginica
iris.plot(x = 'Petal_Width', y = 'Petal_Length', kind = 'scatter', title = '鸢尾花的花瓣宽度与长度关系')
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 显示图形
show()

# seaborn模块绘制分组散点图
sns.lmplot(x = 'Petal_Width', # 指定x轴变量
y = 'Petal_Length', # 指定y轴变量
hue = 'Species', # 指定分组变量
data = iris, # 指定绘图数据集
legend_out = False, # 将图例呈现在图框内
truncate = True # 根据实际的数据范围，对拟合线作截断操作
)
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

print(iris.keys())
print("---------------------------")
print(iris.data.shape)
print("---------------------------")

iris = load_iris()
print("特徵值：")
print(iris.data[0:3])
print("目標值：")
print(iris.target)
print("特徵名稱(資料集欄位)：")
print(iris.feature_names)
print("目標名稱：")
print(iris.target_names)
print("鳶尾花資料集描述")
print(iris.DESCR)
print("資料集資料")
print(iris.data)
print("資料集目標名稱")
print(iris.target_names)
print("資料集目標")
print(iris.target)
print("看鳶尾花數據庫的features")
print(iris.feature_names)

# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 有四個 features: 花萼長度、花萼寬度 和 花瓣長度、花瓣寬度
# sepal 花萼
# petal  花瓣

print(iris.data)
print(type(iris.data))
print(len(iris.data))
print(iris.data.shape)
print(iris.data[5])  # 第5筆資料
print(iris.data[:5])  # 前5筆資料
print("答案")
print(iris.target)

"""
#debug 10筆資料
iris.data = iris.data[45:55]
iris.target = iris.target[45:55]
"""
"""
#debug 10筆資料
irisdata = [[5.1, 3.5, 1.4, 0.2],
            [4.9, 3.0, 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            [7.0, 3.2, 4.7, 1.4],
            [6.4, 3.2, 4.5, 1.5],
            [6.9, 3.1, 4.9, 1.5],
            [6.3, 2.5, 5.0, 1.9],
            [6.5, 3.0, 5.2, 2.0],
            [6.2, 3.4, 5.4, 2.3],
            [5.9, 3.0, 5.1, 1.8]]
iris.data = np.array(irisdata)
iristarget = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
iris.target = np.array(iristarget)
"""

"""
print('data')
print(iris.data)
print('target')
print(iris.target)
"""

print("共有 :", len(iris.data), "筆資料")

# 資料內容
# 這些數據中, data 就是我們的 x (輸入), target 是 y (輸出)。
# 輸入的數據四個 features 是: 花萼長度、花萼寬度、花瓣長度、花瓣寬度。
# print(iris.data)   many

# 輸出就是某筆數據是哪種 (事實上是哪個亞屬) 的鳶尾花, 共分為 0, 1, 2 三種。
# print(iris.target)

# 只用部份 features
# 我們只選用花萼長度、花萼寬度 (當然只是例子, 事實上四個參數很少, 全部一起來也可以) 當輸入資料。
# 準備輸入及輸出數據, 注意 4 個特徵我們只用了兩個。


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df)

# 資料集目標
y = iris.target
# print(y)
# 資料集目標名稱
# print(iris.target_names)

print("觀察資料集彙總資訊")

df.info()  # 這樣就已經把資料集彙總資訊印出來

print("描述統計量")
cc = df.describe()
print(cc)

print("df之大小")
M, N = df.shape
print(df.shape)
print("df之大小", M, "X", N)

print("iris 資料集欄名columns")
cc = df.columns
print(cc)

print("花萼長度")
print(df["sepal length (cm)"].head())
print("花萼寬度")
print(df["sepal width (cm)"].head())
print("花瓣長度")
print(df["petal length (cm)"].head())
print("花瓣寬度")
print(df["petal width (cm)"].head())

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

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 訓練資料, 測試資料, 訓練目標, 測試目標
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
# print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練
clf.fit(X_train_std, y_train)

# 7. 模型評估
y_pred = clf.predict(X_test_std)
print("預測目標")
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(clf, "tmp_my_model_clf1.joblib")
joblib.dump(scaler, "tmp_my_model_scaler1.joblib")

print("------------------------------")  # 30個

print("讀取模型")
# 載入模型與標準化轉換模型
clf = joblib.load("tmp_my_model_clf1.joblib")
scaler = joblib.load("tmp_my_model_scaler1.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]
# 山鳶尾 變色鳶尾 維吉尼亞鳶尾

print("### 預測品種是：", labels[clf.predict(X_new)[0]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df)

# 資料集目標
y = iris.target
# print(y)
# 資料集目標名稱
# print(iris.target_names)

print("觀察資料集彙總資訊")

df.info()  # 這樣就已經把資料集彙總資訊印出來

print("描述統計量")
cc = df.describe()
print(cc)

# 集中
cc = (
    df["sepal length (cm)"].mean(),
    df["sepal length (cm)"].median(),
    df["sepal length (cm)"].mode(),
)
print(cc)

# 計算變異數(variance)、標準差(standard deviation)、IQR
cc = (
    df["sepal length (cm)"].var(),
    df["sepal length (cm)"].std(),
    df["sepal length (cm)"].quantile(0.75) - df["sepal length (cm)"].quantile(0.25),
)

print(cc)

# (0.6856935123042505, 0.8280661279778629, 1.3000000000000007)

# 計算偏態(skewness)及峰度(kurtosis)
cc = df["sepal length (cm)"].skew(), df["sepal length (cm)"].kurt()
print(cc)

# 自行計算偏態
mean1 = df["sepal length (cm)"].mean()
std1 = df["sepal length (cm)"].std()
n = len(df["sepal length (cm)"])
skew1 = (
    (((df["sepal length (cm)"] - mean1) / std1) ** 3).sum() * n / ((n - 1) * (n - 2))
)
print(skew1)

# 0.31491095663697277

# 自行計算峰度
M2 = (((df["sepal length (cm)"] - mean1) / std1) ** 2).mean()
M4 = (((df["sepal length (cm)"] - mean1) / std1) ** 4).mean()
K = M4 / (M2**2)
print(K - 3)

# -0.5735679489249756

from scipy.stats import kurtosis

print(kurtosis(df["sepal length (cm)"], axis=0, bias=True))

# -0.5735679489249765

# 直方圖
sns.histplot(x="sepal length (cm)", data=df)
show()

# 直方圖平滑化
sns.kdeplot(x="sepal length (cm)", data=df)
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

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 訓練資料, 測試資料, 訓練目標, 測試目標
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
# print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練
clf.fit(X_train_std, y_train)

# 7. 模型評估
y_pred = clf.predict(X_test_std)
print("預測目標")
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(clf, "tmp_my_model_clf2.joblib")
joblib.dump(scaler, "tmp_my_model_scaler2.joblib")

print("------------------------------")  # 60個

print("讀取模型")
# 載入模型與標準化轉換模型
clf = joblib.load("tmp_my_model_clf2.joblib")
scaler = joblib.load("tmp_my_model_scaler2.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
""" NG
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]
# 山鳶尾 變色鳶尾 維吉尼亞鳶尾

print("### 預測品種是：", labels[clf.predict(X_new)[0]])
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
    st.write('### 預測品種是：', labels[clf.predict(X_new)[0]])
"""

print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace=0.5)
plt.scatter(X["sepal_length"], X["sepal_width"], color=colmap[y])
plt.xlabel("花萼長度(Sepal Length)")
plt.ylabel("花萼寬度(Sepal Width)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

dtree = tree.DecisionTreeClassifier(max_depth=8)
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
print(dtree.predict(XTest))
print("---------------------------")
print(yTest.values)

print("------------------------------------------------------------")  # 60個

from sklearn import tree

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

dtree = tree.DecisionTreeClassifier(max_depth=8)
dtree.fit(XTrain, yTrain)

with open("tmp_tree2.dot", "w") as f:
    f = tree.export_graphviz(dtree, feature_names=iris.feature_names, out_file=f)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/iris.csv")

print(df.shape)
print(df.head(5))
print(df.describe())

target_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.subplots_adjust(hspace=0.5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length 花萼長")
plt.ylabel("Sepal Width 花萼寬")

plt.subplot(122)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length 花瓣長")
plt.ylabel("Petal Width 花瓣寬")

show()

print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=["Species"])
df = pd.concat([X, y], axis=1)

print(df.head())

print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA

iris = datasets.load_iris()

n_components = 2  # 削減後の次元を2に設定
model = PCA(n_components=n_components)
model = model.fit(iris.data)
print(model.transform(iris.data))  # 変換したデータ

print("------------------------------------------------------------")  # 60個

from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()

n_components = 3  # ガウス分布の数
model = GaussianMixture(n_components=n_components)
model.fit(iris.data)
print(model.predict(iris.data))  # クラスを予測
print(model.means_)  # 各ガウス分布の平均
print(model.covariances_)  # 各ガウス分布の分散

print("------------------------------------------------------------")  # 60個

# 決策樹 (decision tree)

from sklearn.tree import DecisionTreeClassifier

dx, dy = datasets.load_iris(return_X_y=True)

print(dx[0])
print(dy[0])

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size=0.2)
# 訓練組8成, 測試組2成

tree = DecisionTreeClassifier()

tree.fit(dx_train, dy_train)

predictions = tree.predict(dx_test)

print(tree.score(dx_train, dy_train))

print(tree.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個

# 隨機森林 (random forest)

from sklearn.ensemble import RandomForestClassifier

dx, dy = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size=0.2)
# 訓練組8成, 測試組2成

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train))

print(forest.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = load_iris()

"""
print("另存新檔");
filename = 'tmp_aaaa.csv'
np.savetxt(filename, iris.data, delimiter=',')
print("寫入完成")
"""

# :2 是 前兩個 => 花萼
# 2: 是 第2個(含)以後 => 花瓣

# 準備 inputs 和 outputs
x = iris.data
y = iris.target

# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 只選兩個 features 原因之一是好畫 :)

plt.scatter(X[:, 0], X[:, 1], c="pink", s=150)
plt.scatter(X[:, 0], X[:, 1], s=50, c=Y, alpha=0.6)
plt.title("花瓣 原始資料")
show()

# 試著用我們學過的方式, 看能不能做出一個分類器函數, 來把鳶尾花正確分類!

# 準備 inputs 和 outputs
x = iris.data
y = iris.target

# 為了表示我們很神 (事實上只是好畫圖), 我們只用兩個 features (花瓣長度、寬度)。
# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

# 看一下整筆數據的分佈。
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("花瓣 原始資料")
show()

# 看訓練結果
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.title("花瓣 訓練資料")
show()

# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 開個分類機、訓練
# 再一次, 三部曲打造函數學習機。
# 第一部曲：打開一台函數學習機

from sklearn.svm import SVC

clf = SVC()

# 第二部曲：訓練
clf.fit(x_train, y_train)

# 第三部曲：預測
y_predict = clf.predict(x_test)

print("看看我們模型預測和真實狀況差多少?")
print(y_predict - y_test)

# 看看有沒有不準的?
y_predict = clf.predict(x_test)

# 這時因為如果答對了, 我們和正確答案相減就是 0。學得不錯就會大部份是 0, 錯的不是 0 畫出來就會不同色。我們來試試看。
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)
plt.title("看差值")
show()

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)
plt.title("看最後預測結果")
show()

# 現在我們做的是讓平面上密密麻麻的點都去看它會是哪種鳶尾花的數據。

x1, y1 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))

# 記得 x1, y1 是什麼樣子的, 我們要拉平之後 (x1_ravel(), y1_ravel()), 再用 np.c_ 合成一點一點的, 才可以送進去預測。

Z = clf.predict(np.c_[x1.ravel(), y1.ravel()])

# 好奇的話可以看看我們到底送了多少點進去?

print(len(x1.ravel()))

# 52500

# 等一下我們要用 contourf 做填充型的等高線, 每一點的「高度」就是我們的 SVC 學習機判斷鳶尾花的亞種。但用 contourf 輸入的格點是前面 meshgrid 後的 x1, y1, 而高度 Z 也是要用同樣的型式。

Z = Z.reshape(x1.shape)

# 於是我們終於可以畫圖了...

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
plt.contourf(x1, y1, Z, alpha=0.3)
show()

# 這是測試資料, 之前我們已經知道我們全對!
# 不如就來看看所有鳶尾花資料我們 SVC 的表現。

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.contourf(x1, y1, Z, alpha=0.3)
show()

# 在測試資料中是全對!! 我們畫圖來看看整體表現如何?
# 畫出結果
x0 = np.linspace(0, 7.5, 500)
y0 = np.linspace(0, 2.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:, 0], X[:, 1], c=Y)

show()

x0 = np.linspace(3, 8, 500)
y0 = np.linspace(1.5, 4.5, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:, 0], X[:, 1], c=Y)
show()

# 畫出結果
x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)
show()

x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
np.c_[xx, yy]
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.title("更炫的畫圖法")
show()


"""
X, Y = np.meshgrid(np.arange(4, 8, 0.02), np.arange(2, 4.5, 0.02))

x_data = np.c_[X.ravel(), Y.ravel()]

data_pred = clf.predict(x_data)

Z = data_pred.reshape(X.shape)

plt.contourf(X, Y, Z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], c = y)

show()
"""

# 畫出結果

x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 全部訓練 SVM

iris = load_iris()
# 資料內容 iris.data
# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 答案 iris.target

x = iris.data[:, :2]
y = iris.target

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("原圖")
show()

from sklearn.svm import SVC

clf = SVC()
clf.fit(x, y)
clf.predict(x)
clf.predict(x) - y
gd = np.array([[i, j] for i in np.arange(4, 8, 0.2) for j in np.arange(1.8, 4.5, 0.2)])
gdc = clf.predict(gd)
plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
plt.title("SVM結果")
show()

# 呈現學習成果
# 學出來的用比較透明的顏色, 真實資料用 100% 不透明。

gd = np.array([[i, j] for i in np.arange(4, 8, 0.1) for j in np.arange(1.8, 4.5, 0.1)])
gdc = clf.predict(gd)
plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc, alpha=0.4)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.title("SVM結果2")
show()

print("------------------------------------------------------------")  # 60個

# PCA 可以救鳶尾花嗎？
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)
# 我們來看原來的樣子, 是一個 4 維的向量。
print(x.shape)
print(len(x))
print(x)
print(x[7])

# 經 PCA 之後, 濃縮成 2 維向量。
print(X.shape)
print(len(X))
print(X)
print(X[7])

# 看看 PCA 後, 來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
show()

# 看來好像真的會比較容易切開, 我們來試試是否真的這樣。先來分訓練和測試資料。

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 再來進入標準程序。
# step 1: 打造函數學習機

clf = SVC()

# step 2: 訓練

clf.fit(x_train, y_train)

SVC()

# step 3: 預測

# 這次我們直接畫出來。

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 把鳶尾花的資料集讀進來

iris = load_iris()

# 分好 features 跟 target
X = iris.data
Y = iris.target

# 照著題目的說明，只拿花萼的 features 來用
# 分好訓練跟測試資料，再把「正確答案」的分佈畫一下做個確認

X = X[:, :2]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
show()

# 設定一個 SVM 的函數學習機，把訓練資料放進去 train

from sklearn.svm import SVC

clf = SVC()
clf.fit(x_train, y_train)

"""
SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,    decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,    max_iter=-1, probability=False, random_state=None, shrinking=True,
,    tol=0.001, verbose=False)
"""

# 稍微瞄一下預測結果跟正確答案的差距，發現大致上做得還不錯！
# 而且好像比原本用花瓣的 features 還要好！
# 選擇 features 真的很重要！

y_predict = clf.predict(x_test)
print(y_predict - y_test)
y_predict - y_test

"""
array([ 0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,
,        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1])
"""

# 當然要畫個圖看一下，這樣還可以確認哪些特殊的情況下模型會分不好
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)
show()

# 也可以畫這種的

y_predict = clf.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)
show()

# 照著題目的說明，換另一種 SVM 來試試看

from sklearn.svm import NuSVC

clf1 = NuSVC()
clf1.fit(x_train, y_train)

"""
NuSVC(break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,      decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,      max_iter=-1, nu=0.5, probability=False, random_state=None, shrinking=True,
,      tol=0.001, verbose=False)
"""

"""
嗚，好像變差了
但這件事告訴我們，不同的模型在不同的參數情況下，
也會學出不同的結果跟好壞，
因此適時的做實驗調整模型跟參數也是很重要的！
"""

y_predict = clf1.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = load_iris()

x = iris.data
y = iris.target

X = x[:, :2]
Y = y

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("原始資料")
show()

from sklearn.svm import SVC

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

Ypred = clf.predict(x_test)

print(Ypred - y_test)

x0 = np.linspace(3.8, 8.2, 500)
y0 = np.linspace(1.8, 4.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)
show()


# PCA 可以救鳶尾花嗎？

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)

# 我們稍稍的「欣賞一下」 PCA 對我們的資料集做了什麼，來看看某朵鳶尾花的資料。
# pca.transform([[6.3, 2.3, 4.4, 1.3]])
# 真的變成平面上一個點！來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
show()


print(x[87])

print(y[87])

print(pca.transform([[6.3, 2.3, 4.4, 1.3]]))

print(clf.predict([[0.81509524, -0.37203706]]))

print(X.shape)

# print(Z.reshape(X.shape))


# 畫完整分類
# 和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
show()

x1, x2 = np.meshgrid(np.arange(-0.2, 1.2, 0.02), np.arange(-0.2, 1.2, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha=0.3)
# NG plt.scatter(x[:, 0], x[:, 1], s=100, c=clf.labels_)
show()

# 呈現出來
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
# NG plt.scatter(x[:, 0], x[:, 1], c=clf.labels_)
show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/iris.csv")
df.shape

df.head()

df.describe()


target_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace=0.5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.subplot(1, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

show()

print("------------------------------------------------------------")  # 60個

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn import preprocessing

df = pd.read_csv("data/iris.csv")

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:4].astype(float)
Y = to_categorical(dataset[:, 4])

scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

cc = model.summary()
print(cc)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=100, batch_size=5)

loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

Y_pred = np.argmax(model.predict(X_test), axis=-1)
print(Y_pred)

Y_target = dataset[:, 4][120:].astype(int)
print(Y_target)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("模型篩選特徵")

from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
print(clf.feature_importances_)

print("------------------------------------------------------------")  # 60個

print("數學方法降維")

from sklearn.decomposition import PCA

iris = datasets.load_iris()
data = pd.DataFrame(iris.data, columns=["SpealLen", "SpealWid", "PetalLen", "PetalWid"])
mat = data.corr()
sns.heatmap(
    mat,
    annot=True,
    vmax=1,
    vmin=-1,
    xticklabels=True,
    yticklabels=True,
    square=True,
    cmap="gray",
)

show()

print("------------------------------------------------------------")  # 60個

pca = PCA(n_components=2)
data1 = pca.fit_transform(data)
print(data1.shape)
print(pca.explained_variance_ratio_, pca.explained_variance_ratio_.sum())
plt.scatter(data1[:, 0], data1[:, 1], c=np.array(iris.target), cmap=plt.cm.copper)

show()

print("------------------------------------------------------------")  # 60個

from sklearn import svm

iris = load_iris()

X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = svm.SVC(C=0.8, kernel="rbf", gamma=1)  # 高斯核，鬆弛度0.8
# clf = svm.SVC(C=0.5, kernel='linear') # 線性核，鬆弛度0.5

clf.fit(X_train, y_train.ravel())

print("trian pred:%.3f" % (clf.score(X_train, y_train)))  # 對訓練集打分
print("test pred:%.3f" % (clf.score(X_test, y_test)))  # 對測試集打分
print(clf.support_vectors_)  # 支持向量列表，從中看到切分邊界
print(clf.n_support_)  # 每類別持向量個數

plt.plot(X_train[:, 0], X_train[:, 1], "o", color="#bbbbbb")
plt.plot(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], "o")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹")

from sklearn import tree  # 決策樹工具
import pydotplus  # 做圖工具
import io

iris = load_iris()
X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = tree.DecisionTreeClassifier(max_depth=5)

clf.fit(X_train, y_train)  # 訓練模型

print("score:", clf.score(X_test, y_test))  # 模型打分

# 生成決策樹圖片
dot_data = io.StringIO()
tree.export_graphviz(
    clf,
    out_file=dot_data,
    feature_names=iris.feature_names,
    filled=True,
    rounded=True,
    impurity=False,
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# fail
# open('a.jpg','wb').write(graph.create_jpg()) # 保存圖片

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("切分數據集與交叉驗證")

iris = load_iris()
X = iris.data
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# ????
X_train, X_test = train_test_split(X, test_size=0.3, random_state=10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" some fail
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

iris = load_iris()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
# 訓練組8成, 測試組2成

num = 5 # 5折交叉驗證
train_preds = np.zeros(X_train.shape[0]) # 用於保存預測結果
test_preds = np.zeros((X_test.shape[0], num))
kf = KFold(len(X_train), n_folds = num, shuffle=True, random_state=0)
for i, (train_index, eval_index) in enumerate(kf):
    clf = SVC(C=1, gamma=0.125, kernel='rbf')
    clf.fit(X_train[train_index], y_train[train_index])
    train_preds[eval_index] += clf.predict(X_train[eval_index])
    test_preds[:,i] = clf.predict(X_test)
print(accuracy_score(y_train, train_preds)) # 返回結果: 0.971428571429
print(test_preds.mean(axis=1))

from sklearn.model_selection import cross_val_score # python 3使用
print(cross_val_score(clf, iris.data, iris.target).mean())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("模型調參")

# 網格搜索
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

iris = load_iris()
model = SVC(random_state=1)
param_grid = {
    "kernel": ("linear", "rbf"),
    "C": [1, 2, 4],  # 制定參數範圍
    "gamma": [0.125, 0.25, 0.5, 1, 2, 4],
}
gs = GridSearchCV(
    estimator=model, param_grid=param_grid, scoring="accuracy", cv=10, n_jobs=-1
)
gs = gs.fit(iris.data, iris.target)
y_pred = gs.predict(iris.data)  # 預測
print(gs.best_score_)
print(gs.best_params_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" some fail
from sklearn.model_selection import cross_val_score
from hyperopt import hp,STATUS_OK,Trials,fmin,tpe
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def f(params): # 定義評價函數
    t = params['type']
    del params['type']
    if t == 'svm':
        clf = SVC(**params)
    elif t == 'randomforest':
        clf = RandomForestClassifier(**params)
    else:
        return 0
    acc = cross_val_score(clf, iris.data, iris.target).mean() 
    return {'loss': -acc, 'status': STATUS_OK} # 求最小值:準確率加負號

iris = load_iris()
space = hp.choice('classifier_type', [ # 定義可選參數
    {
        'type': 'svm',
        'C': hp.uniform('C', 0, 10.0),
        'kernel': hp.choice('kernel', ['linear', 'rbf']),
        'gamma': hp.uniform('gamma', 0, 20.0)
    },
    {
        'type': 'randomforest',
        'max_depth': hp.choice('max_depth', range(1,20)),
        'max_features': hp.choice('max_features', range(1,5)),
        'n_estimators': hp.choice('n_estimators', range(1,20)),
        'criterion': hp.choice('criterion', ["gini", "entropy"])
    }
])
best = fmin(f, space, algo=tpe.suggest, max_evals=100)
print('best:',best) 
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = load_iris()
print("原始_特徵：{}, 原始_目標：{}".format(iris.data.shape, iris.target.shape))

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
# 訓練組8成, 測試組2成

print("訓練_特徵：{}, 訓練_目標：{}".format(x_train.shape, y_train.shape))
print("測試_特徵：{}, 測試_目標：{}".format(x_test.shape, y_test.shape))

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


""" 測試 df
df.to_csv("tmp_iris1.csv")
df.to_csv("tmp_iris2.csv", encoding="utf8")
df.to_csv("tmp_iris3.csv", encoding="utf-8-sig")


df1 = pd.read_csv("tmp_iris1.csv")
print(df1)

df2 = pd.read_csv("tmp_iris2.csv")
print(df2)

df3 = pd.read_csv("tmp_iris3.csv")
print(df3)

print("比較df是否相同")
cc = df.equals(df1)
print(cc)
cc = df.equals(df2)
print(cc)
cc = df.equals(df3)
print(cc)
"""


print("------------------------------------------------------------")  # 60個
# new

iris = datasets.load_iris()
# print(iris.feature_names)

X = iris.data
y = iris.target

print("iris.data.shape=", iris.data.shape)
print("dir(iris)", dir(iris))
print("iris.target.shape=", iris.target.shape)
try:
    print("iris.feature_names=", iris.feature_names)
except:
    print("No iris.feature_names=")

import xlsxwriter

try:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
except:
    df = pd.DataFrame(
        iris.data,
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )

df["target"] = iris.target

print(df.head())
df.to_csv("tmp_iris.csv", sep="\t")

""" no save
writer = pd.ExcelWriter("tmp_iris.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer.save()
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
