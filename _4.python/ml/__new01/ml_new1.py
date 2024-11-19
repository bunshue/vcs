"""

機器學習

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 數據預處理（Data Preprocessing）

import sklearn
print("Sklearn verion is {}".format(sklearn.__version__))

from sklearn.impute import SimpleImputer

#This block is an example used to learn SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])
X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
print(imp_mean.transform(X))

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
X = [['Male', 1], ['Female', 3], ['Female', 2]]

enc.fit(X)

cc = enc.categories_
print(cc)

cc = enc.transform([['Female', 1], ['Male', 4]]).toarray()
print(cc)

cc = enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
print(cc)

cc = enc.get_feature_names_out(['gender', 'group'])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Data.csv")
# 不包括最后一列的所有列
X = dataset.iloc[:, :-1].values  # //.iloc[行，列]

# 取最后一列
Y = dataset.iloc[:, 3].values  # : 全部行 or 列；[a]第a行 or 列
# [a,b,c]第 a,b,c 行 or 列

print("X")
print(X)
print("Y")
print(Y)
print(X[:, 1:3])

# 第三步：處理丟失數據

# 我們得到的數據很少是完整的。
# 數據可能因為各種原因丟失，為了不降低機器學習模型的性能，需要處理數據。
# 我們可以用整列的平均值或中間值替換丟失的數據。
# 我們用sklearn.preprocessing庫中的Imputer類完成這項任務。

# Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# from sklearn.preprocessing import Imputer
# axis=0表示按列進行
# imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# print(imputer)
# print(X[ : , 1:3])
imputer = imputer.fit(X[:, 1:3])  # put the data we want to process in to this imputer
X[:, 1:3] = imputer.transform(X[:, 1:3])  # replace the np.nan with mean
# print(X[ : , 1:3])
print("---------------------")
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)

""" another
第3步：處理丟失數據

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
"""

# Step 4: Encoding categorical data
# 第四步：解析分類數據
# 分類數據指的是含有標簽值而不是數字值的變量。取值范圍通常是固定的。
# 例如"Yes"和"No"不能用于模型的數學計算，所以需要解析成數字。
# 為實現這一功能，我們從sklearn.preprocessing庫導入LabelEncoder類。

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

""" another
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
"""

# labelencoder_X = LabelEncoder()
# X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
# Creating a dummy variable
# print(X)
ct = ColumnTransformer([("", OneHotEncoder(), [0])], remainder="passthrough")
X = ct.fit_transform(X)
# onehotencoder = OneHotEncoder(categorical_features = [0])
# X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
print("---------------------")
print("Step 4: Encoding categorical data")
print("X")
print(X)
print("Y")
print(Y)

""" another
創建虛擬變量

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
"""

# Step 5: Splitting the datasets into training sets and Test sets
# 第五步：拆分數據集為測試集合和訓練集合
# 把數據集拆分成兩個：一個是用來訓練模型的訓練集合，另一個是用來驗證模型的測試集合。
# 兩者比例一般是80:20。
# 我們導入sklearn.model_selection庫中的train_test_split()方法。

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成
print("X_train")
print(X_train)
print("X_test")
print(X_test)
print("Y_train")
print(Y_train)
print("Y_test")
print(Y_test)

# 第六步：特征縮放
# 第6步：特征量化
# Step 6: Feature Scaling
# 大部分模型算法使用兩點間的歐氏距離表示，
# 但此特征在幅度、單位和范圍姿態問題上變化很大。
# 在距離計算中，高幅度的特征比低幅度特征權重更大。
# 可用特征標準化或Z值歸一化解決。
# 導入sklearn.preprocessing庫的StandardScalar類。

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print("---------------------")
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 逻辑回归（Logistic Regression）

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
Y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

# 特征缩放

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 第二步：逻辑回归模型

# 该项工作的库将会是一个线性模型库，之所以被称为线性是因为逻辑回归是一个线性分类器，
# 这意味着我们在二维空间中，我们两类用户（购买和不购买）将被一条直线分割。
# 然后导入逻辑回归类。下一步我们将创建该类的对象，它将作为我们训练集的分类器。

# 将逻辑回归应用于训练集
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
# 第3步：预测
# 预测测试集结果

y_pred = classifier.predict(X_test)

# 第4步：评估预测

# 我们预测了测试集。 现在我们将评估逻辑回归模型是否正确的学习和理解。
# 因此这个混淆矩阵将包含我们模型的正确和错误的预测。

# Making the Confusion Matrix
# 生成混淆矩阵
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test, y_pred)

print(cm)  # print confusion_matrix
print(classification_report(y_test, y_pred))  # print classification report

# 可视化

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.show()

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# K近邻法（K-NN）

dataset = pd.read_csv("data/Social_Network_Ads.csv")
print(dataset)

# 为了方便理解，这里我们只取Age年龄和EstimatedSalary估计工资作为特征

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 第四步：特征缩放
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 第五步：使用K-NN对训练集数据进行训练
# Fitting K-NN to the Training set
# 从sklearn的neighbors类中导入KNeighborsClassifier学习器

from sklearn.neighbors import KNeighborsClassifier

# 设置好相关的参数 n_neighbors = 5(K值的选择，默认选择5)、
# metric = 'minkowski'(距离度量的选择，这里选择的是闵氏距离(默认参数))、
# p = 2 (距离度量metric的附属参数，只用于闵氏距离和带权重闵氏距离中p值的选择，
# p=1为曼哈顿距离， p=2为欧式距离。默认为2)

classifier = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2)

classifier.fit(X_train, y_train)  # 學習訓練.fit

KNeighborsClassifier(
    algorithm="auto",
    leaf_size=30,
    metric="minkowski",
    metric_params=None,
    n_jobs=1,
    n_neighbors=5,
    p=2,
    weights="uniform",
)

# 第六步：对测试集进行预测
# Predicting the Test set results

y_pred = classifier.predict(X_test)
print(y_pred)


# 第七步：生成混淆矩阵
# Making the Confusion Matrix
# 混淆矩阵可以对一个分类器性能进行分析，由此可以计算出许多指标，例如：ROC曲线、正确率等

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

"""
[[64  4]
 [ 3 29]]
    预测值
    0   1
实0 64  4   
际1 3   29
值
预测集中的0总共有68个，1总共有32个。
在这个混淆矩阵中，实际有68个0，但K-NN预测出有67(64+3)个0，其中有3个实际上是1。
同时K-NN预测出有33(4+29)个1，其中4个实际上是0。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 支持向量机 (SVM)

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 第四步：特征量化
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
# X_test = sc.transform(X_test) maybe
# 第五步：适配SVM到训练集合
# Fitting SVM to the Training set
from sklearn.svm import SVC

classifier = SVC(kernel="linear", random_state=0)

classifier.fit(X_train, y_train)  # 學習訓練.fit

SVC(
    C=1.0,
    cache_size=200,
    class_weight=None,
    coef0=0.0,
    decision_function_shape="ovr",
    degree=3,
    gamma="auto",
    kernel="linear",
    max_iter=-1,
    probability=False,
    random_state=0,
    shrinking=True,
    tol=0.001,
    verbose=False,
)

# 第六步：预测测试集合结果
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# 第七步：创建混淆矩阵
# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

# 第八步：训练集合结果可视化
# Visualising the Training set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("SVM (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()


# 第九步：测试集合结果可视化

from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("SVM (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion="entropy", random_state=0)

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Decision Tree Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Decision Tree Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling 特征缩放
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Random Forest to the Training set
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(
    n_estimators=10, criterion="entropy", random_state=0
)

classifier.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
# 生成混淆矩阵，也称作误差矩阵
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Random Forest Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Random Forest Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pip install tf-nightly

# import tensorflow.keras as keras

import tensorflow as tf
print(tf.__version__)


"""
下载mnist数据
keras默认从(https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz)下载，
但国内很难连上， 可以参考(http://www.cnblogs.com/shinny/p/9283372.html)。
手动下载mnist.npz，然后修改mnist.py中的引用路径。 如果找不到mnist.py，可以用everthing搜索。
mnist.npz已上传到datasets文件夹，可从这里下载。
"""

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train[0])

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()

print("答案")
print(y_train[0])


x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train[0])

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=3)  # 學習訓練.fit


val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)


predictions = model.predict(x_test)
print(predictions)


import numpy as np

print(np.argmax(predictions[0]))


plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.show()


# 保存模型
model.save("tmp_epic_num_reader.model")

# 加载保存的模型
new_model = tf.keras.models.load_model("tmp_epic_num_reader.model")

# 测试保存的模型
predictions = new_model.predict(x_test)
print(np.argmax(predictions[0]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 要先对数据集中的图片进行处理，可能需要进行的任务有图像尺寸统一、颜色处理等

import cv2
from tqdm import tqdm

# 数据集的路径
DATADIR = "C:/_git/vcs/_big_files/kagglecatsanddogs_5340_1000/PetImages/"
DATADIR = "C:/_git/vcs/_big_files/kagglecatsanddogs_5340_800/PetImages/"

CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  # 创建路径
    for img in os.listdir(path):  # 迭代遍历每个图片
        img_array = cv2.imread(
            os.path.join(path, img), cv2.IMREAD_GRAYSCALE
        )  # 转化成array
        plt.imshow(img_array, cmap="gray")  # 转换成图像展示
        plt.show()  # display!

        break  # 我们作为演示只展示一张，所以直接break了
    break  # 同上


# 看下array中存储的图像数据：
# print(img_array)

print("看下array的形状")
print(img_array.shape)

# 我们可以看到这是一张很大的图片，并且拥有RGB3个通道，这并不是我们想要的，
# 所以接下来我们将要进行的操作会使图像变小，并且只剩下灰度：

print("resize")
IMG_SIZE = 100

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap="gray")
plt.show()

# 接下来，我们将要创建所有这些培训数据，但是，首先，我们应该留出一些图像进行最终测试。
# 我将手动创建一个名为Testing的目录，然后在其中创建2个目录，一个用于Dog，一个用于Cat。
# 从这里开始，我将把Dog和Cat的前15张图像移到训练版本中。确保移动它们，而不是复制。我们将使用它进行最终测试。

print("訓練資料")
training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)  # 得到分类，其中 0=dog 1=cat

        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # 大小转换
                training_data.append([new_array, class_num])  # 加入训练数据中
            except Exception as e:  # 为了保证输出是整洁的
                pass
            # except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            # except Exception as e:
            #    print("general exception", e, os.path.join(path,img))


create_training_data()

print(len(training_data))

# 我们有大约25,000张图片。
# 我们要做的一件事是确保我们的数据是平衡的。在这个数据集的情况下，
# 我可以看到数据集开始时是平衡的。平衡，我的意思是每个班级都有相同数量的例子（相同数量的狗和猫）。
# 如果不平衡，您要么将类权重传递给模型，以便它可以适当地测量误差，或者通过将较大的集修剪为与较小集相同的大小来平衡样本。
# 现在数据集中要么全是dog要么全是cat，因此接下来要引入随机：

import random

random.shuffle(training_data)

# 我们的training_data是一个列表，这意味着它是可变的，所以它现在很好地改组了。
# 我们可以通过迭代几个初始样本并打印出类来确认这一点：

for sample in training_data[:10]:
    print(sample[1])

# 现在可以看到已经是0、1交替了，我们可以开始我们的模型了：

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# 让我们保存这些数据，这样我们就不需要每次想要使用神经网络模型时继续计算它：

import pickle

pickle_out = open("tmp_X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("tmp_y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
# We can always load it in to our current script, or a totally new one by doing:

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

# 现在我们已经拿出了数据集，我们已经准备好覆盖卷积神经网络，并用我们的数据进行分类。
# 以上就是这次的关于数据集操作的全部任务。

"""
基础知识
基本的CNN结构如下： Convolution(卷积) -> Pooling(池化) -> Convolution -> Pooling -> Fully Connected Layer(全连接层) -> Output
Convolution（卷积）是获取原始数据并从中创建特征映射的行为。
Pooling(池化)是下采样，通常以“max-pooling”的形式，我们选择一个区域，然后在该区域中取最大值，这将成为整个区域的新值。
Fully Connected Layers(全连接层)是典型的神经网络，其中所有节点都“完全连接”。卷积层不像传统的神经网络那样完全连接。
卷积：我们将采用某个窗口，并在该窗口中查找要素,该窗口的功能现在只是新功能图中的一个像素大小的功能，但实际上我们将有多层功能图。
接下来，我们将该窗口滑过并继续该过程,继续此过程，直到覆盖整个图像。
池化：最常见的池化形式是“最大池化”，其中我们简单地获取窗口中的最大值，并且该值成为该区域的新值。
全连接层：每个卷积和池化步骤都是隐藏层。在此之后，我们有一个完全连接的层，然后是输出层。
完全连接的层是典型的神经网络（多层感知器）类型的层，与输出层相同。
注意
本次代码中所需的X.pickle和y.pickle为上一篇的输出，路径请根据自己的情况更改！
"""

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

import pickle

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3)  # 學習訓練.fit


"""
在仅仅三个epoches之后，我们的验证准确率为71％。
如果我们继续进行更多的epoches，我们可能会做得更好，但我们应该讨论我们如何知道我们如何做。
为了解决这个问题，我们可以使用TensorFlow附带的TensorBoard，它可以帮助您在训练模型时可视化模型。
我们将在下一个教程中讨论TensorBoard以及对我们模型的各种调整！
"""

# 这是Python，TensorFlow和Keras教程系列的深度学习基础知识的第4部分。
# 在这一部分，我们将讨论的是TensorBoard。
# TensorBoard是一个方便的应用程序，允许您在浏览器中查看模型或模型的各个方面。
# 我们将TensorBoard与Keras一起使用的方式是通过Keras回调。实际上有很多Keras回调，你可以自己制作。
from tensorflow.keras.callbacks import TensorBoard
# Using TensorFlow backend.
# 创建TensorBoard回调对象
NAME = "Cats-vs-dogs-CNN"

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

"""
最终，你会希望获得更多的自定义NAME，但现在这样做。
因此，这将保存模型的训练数据logs/NAME，然后由TensorBoard读取。
最后，我们可以通过将它添加到.fit方法中来将此回调添加到我们的模型中，
例如：
model.fit(X, y,
          batch_size=32,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])  # 學習訓練.fit
请注意，这callbacks是一个列表。您也可以将其他回调传递到此列表中。
我们的模型还没有定义，所以现在让我们把它们放在一起：
"""
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
import pickle
import time

NAME = "Cats-vs-dogs-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

"""
运行此之后，您应该有一个名为的新目录logs。我们现在可以使用tensorboard从这个目录中可视化初始结果。
打开控制台，切换到工作目录，然后键入：tensorboard --logdir=logs/。
您应该看到一个通知：TensorBoard 1.10.0 at http://H-PC:6006 (Press CTRL+C to quit)“h-pc”是您机器的名称。
打开浏览器并前往此地址。你应该看到类似的东西：
"""

# 现在我们可以看到我们的模型随着时间的推移。让我们改变模型中的一些东西。
# 首先，我们从未在密集层中添加激活。另外，让我们尝试整体较小的模型：

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
import pickle
import time

NAME = "Cats-vs-dogs-64x2-CNN"

pickle_in = open("tmp_X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("tmp_y.pickle", "rb")
y = pickle.load(pickle_in)

X = X / 255.0

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))
model.add(Activation("sigmoid"))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"],
)

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3, callbacks=[tensorboard])  # 學習訓練.fit

# 除此之外，我还改名为NAME = "Cats-vs-dogs-64x2-CNN"。
# 不要忘记这样做，否则你会偶然附加到你以前的型号的日志，它看起来不太好。我们现在检查TensorBoard：

"""
看起来更好！但是，您可能会立即注意到验证丢失的形状。
损失是衡量错误的标准，看起来很明显，在我们的第四个时代之后，事情开始变得糟糕。
有趣的是，我们的验证准确性仍然持续，但我想它最终会开始下降。
更可能的是，第一件遭受的事情确实是你的验证损失。这应该提醒你，你几乎肯定会开始过度适应。
这种情况发生的原因是该模型不断尝试减少样本损失。
在某些时候，模型不是学习关于实际数据的一般事物，而是开始只记忆输入数据。
如果你继续这样做，是的，样本中的“准确性”会上升，但你的样本，以及你试图为模型提供的任何新数据可能会表现得很差。
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
