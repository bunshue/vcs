"""
Iris 鳶尾花
Iris 鳶尾花數據庫 150筆資料 4個欄位 3種品種 每種50筆資料

以Iris dataset為例，鳶尾花資料集是非常著名的生物資訊資料集之一，
取自美國加州大學歐文分校的機器學習資料庫http://archive.ics.uci.edu/ml/datasets/Iris
資料的筆數為150筆，共有五個欄位：

# sepal_length,sepal_width,petal_length,petal_width,species

4個欄位 #sepal_length, sepal_width, petal_length, petal_width, species
萼長 花萼長度(Sepal.Length)(cm)
萼寬 花萼寬度(Sepal.Width)(cm)
瓣長 花瓣長度(Petal.Length)(cm)
瓣寬 花瓣寬度(Petal.Width)(cm)

# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 有四個 features: 花萼長度、花萼寬度 和 花瓣長度、花瓣寬度
# sepal 花萼
# petal  花瓣


3種品種 類別(Class)
['setosa' 'versicolor' 'virginica']

#鳶尾花(Iris)品種的辨識

標準的分類問題: 這是哪種鳶尾花

鳶尾花 (Iris)  數據庫是很有名的資料,
就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。
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
import sklearn.linear_model
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# 不要顯示一些警告
import warnings

# warnings.filterwarnings("ignore")

print("------------------------------------------------------------")  # 60個


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("鳶尾花數據庫 基本數據")

iris = datasets.load_iris()

print("所有資料 :", iris)
print("data :", iris.data)
print("target :", iris.target)

# 資料集目標名稱
print("target_names :", iris.target_names)

print("DESCR :", iris.DESCR)
print("feature_names :", iris.feature_names)
print("filename :", iris.filename)
print("data_module :", iris.data_module)

print("原始_特徵：{}, 原始_目標：{}".format(iris.data.shape, iris.target.shape))

print(iris.keys())
print("---------------------------")
print(iris.data.shape)
print("---------------------------")

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

print("觀察資料集彙總資訊")

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


# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
# 訓練組8成, 測試組2成

print("訓練_特徵：{}, 訓練_目標：{}".format(x_train.shape, y_train.shape))
print("測試_特徵：{}, 測試_目標：{}".format(x_test.shape, y_test.shape))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iris 轉 df, 再看iris資料")

df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("觀察資料集彙總資訊")
# 了解行資料的標題與資料型別(整數、浮點數、字串等)
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data, label = datasets.load_iris(return_X_y=True)

print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")

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
#plt.legend()
# 显示图形

plt.show()
show()
"""

iris = pd.read_csv("data/iris.csv")
print(iris.shape)
print(iris)

# 绘制散点图
plt.scatter(
    x=iris.petal_width,  # 指定散点图的x轴数据
    y=iris.petal_length,  # 指定散点图的y轴数据
    color="steelblue",  # 指定散点图中点的颜色
)
# 添加x轴和y轴标签
plt.xlabel("花瓣宽度")
plt.ylabel("花瓣长度")
# 添加标题
plt.title("鸢尾花的花瓣宽度与长度关系")
# 显示图形
show()

# Pandas模块绘制散点图
# 绘制散点图Virginica
iris.plot(x="petal_width", y="petal_length", kind="scatter", title="鸢尾花的花瓣宽度与长度关系")
# 修改x轴和y轴标签
plt.xlabel("花瓣宽度")
plt.ylabel("花瓣长度")
# 显示图形
show()

# seaborn模块绘制分组散点图
sns.lmplot(
    x="petal_width",  # 指定x轴变量
    y="petal_length",  # 指定y轴变量
    hue="target",  # 指定分组变量
    data=iris,  # 指定绘图数据集
    legend_out=False,  # 将图例呈现在图框内
    truncate=True,  # 根据实际的数据范围，对拟合线作截断操作
)
# 修改x轴和y轴标签
plt.xlabel("花瓣宽度")
plt.ylabel("花瓣长度")
# 添加标题
plt.title("鸢尾花的花瓣宽度与长度关系")
# 显示图形

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df)

# 資料集目標
y = iris.target
# print(y)

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

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)

# 模型評估
y_pred = logistic_regression.predict(X_test_std)
print("預測目標")
print(y_pred)

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

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]
# 山鳶尾 變色鳶尾 維吉尼亞鳶尾

print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df)

# 資料集目標
y = iris.target
# print(y)

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

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)

y_pred = logistic_regression.predict(X_test_std)
print("預測目標")
print(y_pred)

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

print("------------------------------")  # 60個

print("讀取模型")
# 載入模型與標準化轉換模型
logistic_regression2 = joblib.load("tmp_my_model_clf2.joblib")
scaler = joblib.load("tmp_my_model_scaler2.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
""" NG
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]
# 山鳶尾 變色鳶尾 維吉尼亞鳶尾

print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])
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
    st.write('### 預測品種是：', labels[logistic_regression2.predict(X_new)[0]])
"""

print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

colmap = np.array(["r", "g", "y"])

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.subplots_adjust(hspace=0.5)
plt.scatter(X["sepal_length"], X["sepal_width"], color=colmap[y])
plt.xlabel("花萼長度(Sepal Length)")
plt.ylabel("花萼寬度(Sepal Width)")

plt.subplot(122)
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
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/iris.csv")

print(df.shape)
print(df.head(5))

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
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=["Species"])
df = pd.concat([X, y], axis=1)

print(df.head())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA

iris = datasets.load_iris()

n_components = 2  # 削減後の次元を2に設定
clf = PCA(n_components=n_components)
clf = clf.fit(iris.data)
print(clf.transform(iris.data))  # 変換したデータ

print("------------------------------------------------------------")  # 60個

from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()

n_components = 3  # ガウス分布の数
clf = GaussianMixture(n_components=n_components)
clf.fit(iris.data)
print(clf.predict(iris.data))  # クラスを予測
print(clf.means_)  # 各ガウス分布の平均
print(clf.covariances_)  # 各ガウス分布の分散

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

iris = datasets.load_iris()

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

clf = SVC()

clf.fit(x_train, y_train)

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

iris = datasets.load_iris()

# 資料內容 iris.data
# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 答案 iris.target

x = iris.data[:, :2]
y = iris.target

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("原圖")
show()

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

clf = SVC()

clf.fit(x_train, y_train)

SVC()

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

iris = datasets.load_iris()

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

iris = datasets.load_iris()

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

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print(y_pred - y_test)

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

df = pd.read_csv("data/iris.csv")

df.shape

df.head()

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

iris = datasets.load_iris()

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

iris = datasets.load_iris()

X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = SVC(C=0.8, kernel="rbf", gamma=1)  # 高斯核，鬆弛度0.8
# clf = SVC(C=0.5, kernel='linear') # 線性核，鬆弛度0.5

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

iris = datasets.load_iris()

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

iris = datasets.load_iris()

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

iris = datasets.load_iris()

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

iris = datasets.load_iris()

clf = SVC(random_state=1)

param_grid = {
    "kernel": ("linear", "rbf"),
    "C": [1, 2, 4],  # 制定參數範圍
    "gamma": [0.125, 0.25, 0.5, 1, 2, 4],
}
gs = GridSearchCV(
    estimator=clf, param_grid=param_grid, scoring="accuracy", cv=10, n_jobs=-1
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

iris = datasets.load_iris()

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


# 6-2 探索性資料分析──以 Iris 的花種分類為例
# 資料科學0. 感興趣的問題

# 資料科學1. 資料取得
# 資料科學1.1 自建資料或從網路下載資料後上傳到雲端硬碟

# Iris.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
print(df)

df = df.drop("Id", axis=1)
print(df.head())

# 資料科學2. 資料處理
# 資料科學2.1 由列資料了解資料集

print(df.head())

# 資料科學2.3 資料清理

# 缺失值的補值或刪除

# 刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True)  # 將列索引重新編號

# 資料轉換

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)
print(df.head())

# 資料科學3.2 資料視覺化

c = {0: "r", 1: "g", 2: "b"}
df["colors"] = df["Species"].map(c)
print(df)

df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (圖)-不同欄位和「類別(Species)」所繪製的散佈圖
# (a)花萼長度
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (b)花萼寬度
df.plot(kind="scatter", x="SepalWidthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (c)花瓣長度
df.plot(kind="scatter", x="PetalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (d)花瓣寬度
df.plot(kind="scatter", x="PetalWidthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (圖)-2個欄位組合所繪製的散佈圖
# (a)花萼長度 vs. 花萼寬度
df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (b)花瓣長度 vs. 花瓣寬度
df.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (c)花萼長度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (d)花瓣長度 vs. 花萼寬度
df.plot(kind="scatter", x="PetalLengthCm", y="SepalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (e)花萼長度 vs. 花瓣長度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalLengthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (f)花萼寬度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalWidthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


""" no clf
# 02 [練習] 圖形化我們的成果

# 1. 上次的成果拿回來使用

# 記得上次我們做了個鳶尾花分類器。
# 1.1 找回我們的分類器

from sklearn.externals import joblib

clf = joblib.load("iris_clf_01.pkl")

# 真的可以用了嗎?

print(clf.predict([[2, 3]]))

# 可以! 太棒了!
# 1.2 看看我們分類的全貌

# 我們用一下之前的方式, 畫出我們想要看到我們可愛的 SVM 是怎麼以花萼長度、花萼寬度來分類的。
# 上次我們用了 Python 所謂 "list comprehension" 的作法 (本質上是 for 迴圈), 現在我們換個方式看來比較「高級」的方式。

xt, yt = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-1, 1, 0.5))

print(xt)
print(yt)

# 看得出來 meshgrid 做了什麼呢? 基本上它就是說我們在 x, y 兩個指定範圍的長方型當中, 依我們指定的間隔找出格點。
# 這些格點的座標分成 x 座標一個 array, y 座標一個。x 或 y 座標的 array, 的座標是一列一列標記的。
# 要是你覺得這樣的表示法很討厭, 我們也可以讓它變一長串的向量。

print(xt.ravel())

# 注意這其實原來的 xt 並沒有變哦。

print(xt)

# 我們可以把 (x,y) 一點一點的座標收集起來嗎?

print(np.c_[xt.ravel(), yt.ravel()])


# 把資料的型式這樣變來變去會是數據分析非常非常常做的事情。
# 我們經這麼多廢話後終於可以來做正事。

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.2), np.arange(1.5, 5.0, 0.2))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z)
show()

# 雖然看來我們用了比較多白痴的方法做出一樣的事, 不過一些技巧之後也可以常常使用。
# 1.3 快速換個配色

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.coolwarm, alpha=0.8)
show()


plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.prism, alpha=0.8)
show()

# 1.4 取回鳶尾花訓練資料

iris = datasets.load_iris()

x = iris.data[:, :2]

y = iris.target

# 我們來畫畫比較。

plt.subplot(121)

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.subplot(122)

plt.scatter(x[:, 0], x[:, 1], s=50, c=clf.predict(x))

show()

# 左邊的是訓練資料, 右邊是用我們 SVM 分類器分出來的。你有看出差異嗎? 是不是很難看出? 我們來用用另一個方式。

# 1.5 畫圖的另一個方式

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.02), np.arange(1.5, 5.0, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
show()

Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap=plt.cm.coolwarm)
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_02_logistic_regression_SGD
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

logistic_regression.fit(X, y)

# 預測
preds = logistic_regression.predict(X)
cc = (preds == y).mean()
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
probs = logistic_regression.predict_prob(grid).reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")
show()

# 以 Scikit-learn 驗證

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression(C=1e20)  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)

preds = logistic_regression.predict(X)
cc = (preds == y).mean()
print(cc)

cc = logistic_regression.intercept_, logistic_regression.coef_
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
probs = logistic_regression.predict_proba(grid)[:, 1].reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_08_knn_from_scratch_iris

# 自行開發KNN

# 公用函數


# 依筆數找出最大類別
def most_common(lst):
    return max(set(lst), key=lst.count)


# 歐幾里得距離(Euclidean distance)
def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


# KNN 演算法


class KNN:
    def __init__(self, k=5, dist_metric=euclidean):
        self.k = k
        self.dist_metric = dist_metric

    # 指定訓練資料
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # 預測
    def predict(self, X_test):
        neighbors = []
        for x in X_test:
            # 計算距離
            distances = self.dist_metric(x, self.X_train)
            # 距離排序
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            # K個最近鄰
            neighbors.append(y_sorted[: self.k])

        # 找出最大類別
        return list(map(most_common, neighbors))

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = sum(y_pred == y_test) / len(y_test)
        return accuracy


X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 選擇演算法
clf = KNN()

# 模型訓練
clf.fit(X_train_std, y_train)

# 模型評估

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_09_naive_bayes_from_scratch

# 自行開發高斯單純貝氏分類器

# NaiveBayes 演算法


# 貝氏定理 P(y|X) = P(X|y) * P(y) / P(X)
class NaiveBayesClassifier:
    # 計算常態分配的機率(pdf)：P(X)
    def gaussian_density(self, class_idx, x):
        """
        常態分配 pdf 公式:
        (1/√2pi*σ) * exp((-1/2)*((x-μ)^2)/(2*σ²))
        """
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp((-1 / 2) * ((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        prob = numerator / denominator
        return prob

    # 計算後驗機率 P(y|X)
    def calc_posterior(self, x):
        posteriors = []

        # 計算每一類的後驗機率 P(y|X)
        for i in range(self.count):
            # 使用 log 比較穩定
            prior = np.log(self.prior[i])
            conditional = np.sum(np.log(self.gaussian_density(i, x)))
            posterior = prior + conditional
            posteriors.append(posterior)

        # 傳回最大機率的類別
        return self.classes[np.argmax(posteriors)]

    # 訓練
    def fit(self, features, target):
        self.classes = np.unique(target)
        self.count = len(self.classes)
        self.feature_nums = features.shape[1]
        self.rows = features.shape[0]

        # 計算每個特徵的平均數、變異數
        data = np.concatenate((target.reshape(-1, 1), features), axis=1)
        self.mean = np.array(
            [np.mean(data[data[:, 0] == i, 1:], axis=0) for i in self.classes]
        )
        self.var = np.array(
            [np.var(data[data[:, 0] == i, 1:], axis=0) for i in self.classes]
        )
        # 計算先驗機率 P(y)
        self.prior = (
            np.array([target[target == i].shape[0] for i in self.classes]) / self.rows
        )

    # 預測
    def predict(self, features):
        preds = [self.calc_posterior(f) for f in features]
        return preds


X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 選擇演算法
clf = NaiveBayesClassifier()

# 模型訓練
clf.fit(X_train, y_train)

# 模型評估

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_10_Scikit-learn_naive_bayes

# 以單純貝氏分類器進行鳶尾花(Iris)品種的辨識

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 使用伯努利單純貝氏分類器

from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 20.00%

# 使用多項單純貝氏分類器

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 80.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 09_02_kmeans_from_scratch

# 自行開發K-Means

# 歐幾里得距離函數


def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


# K-Means演算法類別


class KMeans:
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters  # 組數
        self.max_iter = max_iter  # EM 最大次數

    # 訓練
    def fit(self, X_train):
        # 生成1個質心
        self.centroids = [random.choice(X_train)]
        # 生成其他 n-1 個質心
        for _ in range(self.n_clusters - 1):
            # Calculate distances from points to the centroids
            dists = np.sum(
                [euclidean(centroid, X_train) for centroid in self.centroids], axis=0
            )
            # 正規化
            dists /= np.sum(dists)
            # 依據距離作為機率，隨機產生質心
            new_centroid_idx = np.random.choice(range(len(X_train)), size=1, p=dists)[0]
            self.centroids += [X_train[new_centroid_idx]]

        iteration = 0
        prev_centroids = [np.zeros(X_train.shape[1])] * self.n_clusters
        while (
            np.not_equal(self.centroids, prev_centroids).any()
            and iteration < self.max_iter
        ):
            # 找到最近的質心
            sorted_points = [[] for _ in range(self.n_clusters)]
            for x in X_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)

            # 尋找新質心
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                # 如果組內沒有任何樣本點，沿用上次的質心
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            iteration += 1
        # print(iteration)

    # 模型評估
    def evaluate(self, X):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)

        return centroids, centroid_idxs


from sklearn.datasets import make_blobs  # 集群資料集

X_train, true_labels = make_blobs(n_samples=100, centers=5, random_state=42)
plt.scatter(X_train[:, 0], X_train[:, 1])
show()

# 標準化
X_train = preprocessing.StandardScaler().fit_transform(X_train)

# 訓練
CLUSTERS = 5  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  # 學習訓練.fit

# 模型評估

class_centers, classification = clf.evaluate(X_train)

sns.scatterplot(
    x=[X[0] for X in X_train],
    y=[X[1] for X in X_train],
    hue=true_labels,
    style=classification,
    palette="deep",
    legend=None,
)
plt.plot(
    [x for x, _ in clf.centroids],
    [y for _, y in clf.centroids],
    "*",
    markersize=20,
    color="r",
)
plt.title("k-means")
show()

# 鳶尾花資料集測試

X, y = datasets.load_iris(return_X_y=True)

# 標準化
X_train = preprocessing.StandardScaler().fit_transform(X)

# 訓練
CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

clf.fit(X_train)  # 學習訓練.fit

# 7

# 模型評估
_, y_pred = clf.evaluate(X_train)

print(accuracy_score(y, y_pred))
# 0.22

# 驗證

# 實際值
cc = ",".join([str(i) for i in y])
print(cc)

# 預測值
cc = ",".join([str(i) for i in y_pred])
print(cc)

p = pd.Series(y_pred)
print(p[p == 1].index)

p = pd.Series(y)
print(p[p == 0].index)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 凝聚階層集群(Agglomerative Hierarchical Clustering, AHC)

# 生成資料
variables = ["X", "Y", "Z"]
labels = ["ID_0", "ID_1", "ID_2", "ID_3", "ID_4"]

X = np.random.random_sample([5, 3]) * 10
df = pd.DataFrame(X, columns=variables, index=labels)
print(df)

# 計算集群彼此間的距離

from scipy.spatial.distance import pdist, squareform

row_dist = pd.DataFrame(
    squareform(pdist(df, metric="euclidean")), columns=labels, index=labels
)
print(row_dist)

# 計算平均連結距離

from scipy.cluster.hierarchy import linkage

row_clusters = linkage(pdist(df, metric="euclidean"), method="average")
pd.DataFrame(
    row_clusters,
    columns=["row label 1", "row label 2", "distance", "no. of items in clust."],
    index=["cluster %d" % (i + 1) for i in range(row_clusters.shape[0])],
)

# 繪製樹狀圖(dendrogram)

from scipy.cluster.hierarchy import dendrogram

row_dendr = dendrogram(row_clusters, labels=labels)
plt.ylabel("歐幾里德距離", fontsize=14)
show()

# 繪製熱力圖

fig = plt.figure(figsize=(8, 8), facecolor="white")
axd = fig.add_axes([0.09, 0.1, 0.2, 0.6])  # x-pos, y-pos, width, height

# 樹狀圖顯示在左邊
row_dendr = dendrogram(row_clusters, orientation="left")

# 降冪排序
df_rowclust = df.iloc[row_dendr["leaves"][::-1]]

# 不顯示刻度
axd.set_xticks([])
axd.set_yticks([])

# 不顯示座標軸
for i in axd.spines.values():
    i.set_visible(False)

# 繪製熱力圖
axm = fig.add_axes([0.23, 0.1, 0.6, 0.6])  # x-pos, y-pos, width, height
cax = axm.matshow(df_rowclust, interpolation="nearest", cmap="hot_r")
fig.colorbar(cax)
axm.set_xticklabels([""] + list(df_rowclust.columns))
axm.set_yticklabels([""] + list(df_rowclust.index))
show()

# Scikit-learn AgglomerativeClustering

from sklearn.cluster import AgglomerativeClustering

# 分 3 類
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)
# Cluster labels: [1 0 0 2 1]

# 分 2 類
ac = AgglomerativeClustering(n_clusters=2, metric="euclidean", linkage="complete")
labels = ac.fit_predict(X)
print("Cluster labels: %s" % labels)
# Cluster labels: [0 1 1 0 0]

# 使用鳶尾花資料集測試


# 繪製樹狀圖
def plot_dendrogram(model, **kwargs):
    # 計算每個集群的筆數
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # 繪製樹狀圖
    dendrogram(linkage_matrix, **kwargs)


# 載入資料集
X, _ = datasets.load_iris(return_X_y=True)

# distance_threshold=0 表示會建立完整的樹狀圖(dendrogram)
clf = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

clf = clf.fit(X)  # 學習訓練.fit

plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(clf, truncate_mode="level", p=3)  # 限制 3 層
plt.ylabel("歐幾里德距離", fontsize=14)
plt.xlabel("每個集群的筆數", fontsize=14)
show()

# 各種距離衡量方式的比較

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

# Generate sample data
n_samples = 1500
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)


X = np.concatenate((x, y))
X += 0.7 * np.random.randn(2, n_samples)
X = X.T

# Create a graph capturing local connectivity. Larger number of neighbors
# will give more homogeneous clusters to the cost of computation
# time. A very large number of neighbors gives more evenly distributed
# cluster sizes, but may not impose the local manifold structure of
# the data
knn_graph = kneighbors_graph(X, 30, include_self=False)

for connectivity in (None, knn_graph):
    for n_clusters in (30, 3):
        plt.figure(figsize=(10, 4))
        for index, linkage in enumerate(("average", "complete", "ward", "single")):
            plt.subplot(1, 4, index + 1)
            clf = AgglomerativeClustering(
                linkage=linkage, connectivity=connectivity, n_clusters=n_clusters
            )
            t0 = time.time()
            clf.fit(X)  # 學習訓練.fit
            elapsed_time = time.time() - t0
            plt.scatter(X[:, 0], X[:, 1], c=clf.labels_, cmap=plt.cm.nipy_spectral)
            plt.title(
                "linkage=%s\n(time %.2fs)" % (linkage, elapsed_time),
                fontdict=dict(verticalalignment="top"),
            )
            plt.axis("equal")
            plt.axis("off")

            plt.subplots_adjust(bottom=0, top=0.89, wspace=0, left=0, right=1)
            plt.suptitle(
                "n_cluster=%i, connectivity=%r"
                % (n_clusters, connectivity is not None),
                size=17,
            )
            plt.tight_layout()

show()

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

iris = datasets.load_iris()

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
