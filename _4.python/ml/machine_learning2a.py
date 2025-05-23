"""




"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import datetime
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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

import warnings

warnings.filterwarnings("once")

print("------------------------------------------------------------")  # 60個

from common1 import *

import tensorflow as tf
import joblib
import pickle
import matplotlib
import matplotlib as mpl

import sklearn
import sklearn.linear_model
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import f1_score  # F値
from sklearn.metrics import r2_score  # R-Squared擬合度, 決定係數
from sklearn.metrics import accuracy_score  # 正解率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve  # ROC曲線, AUC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score  # 適合率
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import recall_score  # 再現率
from sklearn.metrics import balanced_accuracy_score

from sklearn.datasets import make_blobs  # 生成分類資料
from sklearn.datasets import make_moons  # 生成非線性資料 上/下弦月資料
from sklearn.datasets import make_circles
from sklearn.datasets import make_classification
from sklearn.datasets import make_hastie_10_2

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import PolynomialFeatures

# from sklearn.preprocessing import Imputer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import f_classif
from sklearn.model_selection import GridSearchCV  # 網格搜索
from sklearn.model_selection import KFold
from sklearn.model_selection import PredefinedSplit
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer

import scipy

from sklearn import svm
from sklearn import cluster
from sklearn import decomposition
from sklearn import model_selection

from sklearn.decomposition import PCA


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Sklearn verion is {}".format(sklearn.__version__))

print("房價, 共 1460 筆資料 81欄位")

import scipy.stats as stats

train = pd.read_csv("data/houseprice.csv")  # 共 1460 筆資料 81欄位
print(len(train))
print(train.shape)
print(train.head(3))

y = train["SalePrice"]

sns.histplot(y)
plt.xlabel("售價區間")
plt.ylabel("賣出件數")
plt.title("統計 售價區間 / 賣出件數")
show()

# 另一種查看是否服從正態分布的可視化方法
import scipy.stats as st

res = st.probplot(y, plot=plt)
plt.ylabel("售價區間")
plt.xlabel("賣出件數")
plt.title("統計 售價區間 / 賣出件數")
show()

sns.histplot(y, kde=False)
plt.xlabel("售價區間")
plt.ylabel("賣出件數")
plt.title("統計 售價區間 / 賣出件數")
show()

""" 不能使用參數fit
sns.histplot(y, kde=True, fit=st.johnsonsu)
plt.title("使用 Johnson SU")
show()

sns.histplot(y, kde=False, fit=st.norm)
plt.title("使用 Normal")
show()

sns.histplot(y, kde=False, fit=st.lognorm)
plt.title("使用 Log Normal")
show()

# 另一種查看是否服從正態分布的可視化方法

sns.histplot(y, fit=st.norm)
plt.title("使用 Normal")
show()
"""

res = st.probplot(y, plot=plt)
plt.title("SalePrice")
show()

print("------------------------------")  # 30個

# 把房價做對數變換後再看
SalePrice_log = np.log(y)

"""
# transformed histogram and normal probability plot
sns.histplot(SalePrice_log, fit=st.norm)
plt.title("使用 Normal")
# plt.title('SalePrice log')
show()
"""
# 另一種查看是否服從正態分布的可視化方法
res = st.probplot(SalePrice_log, plot=plt)
print(res)
plt.title("SalePrice log")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy.stats import norm


def norm_prob(x, mu, sigma):
    p = norm(mu, sigma).cdf(x + 0.0001) - norm(mu, sigma).cdf(x - 0.0001)
    return p


def loglikelihood(data, mu, sigma):
    l = 0.0
    for x in data:
        l -= np.log(norm_prob(x, mu, sigma))
    return l


N = 1000
mu, sigma = 1.6, 0.2

h = 1.8

# rvs: 隨機變量
data = norm.rvs(loc=mu, scale=sigma, size=N)
# print(data)

bins = 50  # 束
plt.hist(data, bins=bins)
plt.title("normal distribution")
show()

# pdf: 概率密度函數
cc = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(cc)

cc = norm_prob(h, mu, sigma)
print(cc)

cc = loglikelihood(data, mu, sigma)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立空的df
df = pd.DataFrame()

# 增加 Gender 欄位 目標欄位
df["Gender"] = [
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "female",
    "female",
]

# 增加 4欄位 為 feature variables
df["Height"] = [6, 5.92, 5.58, 5.92, 5, 5.5, 5.42, 5.75]
df["Weight"] = [180, 190, 170, 165, 100, 150, 130, 150]
df["Size"] = [12, 11, 12, 10, 6, 8, 7, 9]
df["Team"] = ["i100", "i100", "i500", "i100", "i500", "i100", "i500", "i100"]

print("df:\n", df)

print("------------------------------")  # 30個

df1 = (
    df.groupby(["Team", "Gender"]).size().rename("cnt").reset_index().set_index("Team")
)
print("df1:\n", df1)

df2 = pd.DataFrame(df.groupby(["Team"]).size().rename("total"))
print("df2:\n", df2)

df3 = df1.merge(df2, left_index=True, right_index=True)
df3["p"] = df3["cnt"] * 1.0 / df3["total"]
df3 = df3.reset_index()
print("df3:\n", df3)

print("------------------------------")  # 30個


def p_x_given_y_1(team, gender):
    return df3["p"][df3["Team"] == team][df3["Gender"] == gender].values[0]


print("p_x_given_y_1")
print(p_x_given_y_1("i100", "female"))
# 0.4

print("------------------------------")  # 30個

# 計算先驗
# Number of i100
n_i100 = df["Team"][df["Team"] == "i100"].count()
print("n_i100 的個數 :", n_i100)

# Number of i500
n_i500 = df["Team"][df["Team"] == "i500"].count()
print("n_i500 的個數 :", n_i500)

# Total rows
total_ppl = df["Team"].count()
print("全部列數 :", n_i100)

# Number of males divided by the total rows
P_i100 = n_i100 * 1.0 / total_ppl

# Number of females divided by the total rows
P_i500 = n_i500 * 1.0 / total_ppl

print("P_i100 :", P_i100)
print("P_i500 :", P_i500)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 計算高斯分布的概率

# 建立空的df
df = pd.DataFrame()

# Create some feature values for this single row
# 增加 Gender 欄位 目標欄位 ??
# 增加 4欄位 為 feature variables ??
df["Height"] = [6]
df["Weight"] = [130]
df["Size"] = [8]
df["Gender"] = ["female"]

print("df:\n", df)


def p_x_given_y_2(x, mean_y, variance_y):
    # Input the arguments into a probability density function
    p = (
        1
        / (np.sqrt(2 * np.pi * variance_y))
        * np.exp((-((x - mean_y) ** 2)) / (2 * variance_y))
    )
    return p


cc = df["Gender"][0]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 安裝 auto-sklearn fail
print('Auto-Sklearn')

#pip install auto-sklearn

import autosklearn.classification
import statsmodels.api as sm
  
data = sm.datasets.anes96.load_pandas().data
label = 'vote'
features = [i for i in data.columns if i != label]
X_train = data[features]
y_train = data[label]
automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120, per_run_time_limit=120, # 兩分鐘
    include_estimators=["random_forest"])
automl.fit(X_train, y_train)  # 學習訓練.fit
print(automl.score(X_train, y_train))
"""

print("------------------------------------------------------------")  # 60個

""" 安裝 auto-ml fail
print('Auto-ML')

#pip install auto-ml

from auto_ml import Predictor
import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas().data
column_descriptions = {
    'vote': 'output',
    'TVnews': 'categorical',
    'educ': 'categorical',
    'income': 'categorical',
}

ml_predictor = Predictor(type_of_estimator='classifier', 
                         column_descriptions=column_descriptions)
model = ml_predictor.train(data)
model.score(data, data.vote)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ShuffleSplit 随机排列交叉验证器

from sklearn.model_selection import ShuffleSplit

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [3, 4], [5, 6]])
y = np.array([1, 2, 1, 2, 1, 2])
rs = ShuffleSplit(n_splits=5, test_size=0.25, random_state=0)
cc = rs.get_n_splits(X)
print(cc)

print(rs)
ShuffleSplit(n_splits=5, random_state=0, test_size=0.25, train_size=None)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

rs = ShuffleSplit(n_splits=5, train_size=0.5, test_size=0.25, random_state=0)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    return pipeline


def plot_learning_curve(
    estimator,
    X,
    y,
    ylim=None,
    cv=None,
    n_jobs=1,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    if ylim is not None:
        plt.ylim(*ylim)
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    plt.plot(train_sizes, train_scores_mean, "o--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")
    return plt


# 測試資料
N = 200
X = np.linspace(0, 1, N)
y = np.sqrt(X) + 0.2 * np.random.rand(N) - 0.1
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)

plt.figure(figsize=(14, 5))

plt.subplot(131)
degree = 1
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves (Under Fitting)")

plt.subplot(132)
degree = 3
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves")

plt.subplot(133)
degree = 10
plot_learning_curve(polynomial_model(degree), X, y, ylim=(0.75, 1.01), cv=cv)
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curves (Over Fitting)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 各種 模型評估 方法")

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

print(label_true)
print(label_pred)

print("測試 Adjusted Rand-Index : adjusted_rand_score")

cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index : %0.3f" % cc)

label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]

cc = metrics.adjusted_rand_score(label_true, label_pred)
print("Adjusted Rand-Index : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]

print("測試 Homogeneity : homogeneity_score")

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

cc = metrics.homogeneity_score(label_true, label_pred)
print("Homogeneity score : %0.3f" % cc)

print("測試 Completeness : completeness_score")

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

cc = metrics.completeness_score(label_true, label_pred)
print("Completeness score : %0.3f" % cc)

print("測試 V-measure : v_measure_score")

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

cc = metrics.v_measure_score(label_pred, label_true)
print("V-measure score : %0.3f" % cc)

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
cc = metrics.v_measure_score(label_true, label_pred)
print("V-measure score : %0.3f" % cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 數據預處理（Data Preprocessing）

print("Imputer Imputation 插補法")

from sklearn.impute import SimpleImputer

# SimpleImputer 對於np.nan 採用mean
imp_mean = SimpleImputer(missing_values=np.nan, strategy="mean")

imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])

X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
XT = imp_mean.transform(X)

print("原陣列 :\n", X, sep="")
print("轉換後 :\n", XT, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OneHotEncoder 獨熱編碼")

onehotencoder = OneHotEncoder(handle_unknown="ignore")

X = [["Male", 1], ["Female", 3], ["Female", 2]]

print("原陣列 :\n", X, sep="")

onehotencoder.fit(X)

# 類別
cc = onehotencoder.categories_
print("類別")
print(cc)

cc = onehotencoder.transform([["Female", 1], ["Male", 4]]).toarray()
print("b")
print(cc)

cc = onehotencoder.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
print("c")
print(cc)

cc = onehotencoder.get_feature_names_out(["gender", "group"])
print("d")
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" Data.csv 10筆資料 4個欄位
Country,Age,Salary,Purchased
France,44,72000,No
Spain,27,48000,Yes
Germany,30,54000,No
Spain,38,61000,No
Germany,40,,Yes
France,35,58000,Yes
Spain,,52000,No
France,48,79000,Yes
Germany,50,83000,No
France,37,67000,Yes
"""

df = pd.read_csv("data/Data.csv")
# print(df) # 包含df之column與index
print("df之資料內容")
print(df.values)  # 不包含df之column與index 只有資料內容 10筆資料 4個欄位

# 不包括最後一欄的所有欄 前3欄
X = df.iloc[:, :-1].values

# 取出第4欄
Y = df.iloc[:, 3].values

print("X 前3欄 :\n", X, sep="")
print("Y 第4欄 :\n", Y, sep="")
print("X 第2 3欄 :\n", X[:, 1:3], sep="")

# 第三步：處理丟失數據

# 我們得到的數據很少是完整的。
# 數據可能因為各種原因丟失，為了不降低機器學習模型的性能，需要處理數據。
# 我們可以用整列的平均值或中間值替換丟失的數據。
# 我們用sklearn.preprocessing庫中的Imputer類完成這項任務。

# Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# axis=0表示按列進行
# imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# print(imputer)
# print(X[ : , 1:3])

imputer = imputer.fit(X[:, 1:3])  # put the data we want to process in to this imputer
X[:, 1:3] = imputer.transform(X[:, 1:3])  # replace the np.nan with mean

# print(X[ : , 1:3])
print("------------------------------")  # 30個
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)

""" another
第3步：處理丟失數據

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
"""

# Step 4: Encoding categorical data
# 第四步：解析分類數據
# 分類數據指的是含有標簽值而不是數字值的變量。取值范圍通常是固定的。
# 例如"Yes"和"No"不能用于模型的數學計算，所以需要解析成數字。
# 為實現這一功能，我們從sklearn.preprocessing庫導入LabelEncoder類。

"""
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

print("------------------------------")  # 30個
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

# 第六步：特征縮放
# 第6步：特征量化
# Step 6: Feature Scaling
# 大部分模型算法使用兩點間的歐氏距離表示，
# 但此特征在幅度、單位和范圍姿態問題上變化很大。
# 在距離計算中，高幅度的特征比低幅度特征權重更大。
# 可用特征標準化或Z值歸一化解決。
# 導入sklearn.preprocessing庫的StandardScalar類。

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

print("------------------------------")  # 30個
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 類別變數編碼
# 測試資料

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)

df.columns = ["color", "size", "price", "classlabel"]
print("原df :\n", df, sep="")

print("使用 LabelEncoder")

labelencoder = LabelEncoder()

print("LabelEncoder size 字串 轉換 成 數字")
print('轉換前 df["size"] :\n', df["size"], sep="")

cc = labelencoder.fit_transform(df["size"])
print('轉換後 df["size"] :\n', cc, sep="")

cc = labelencoder.inverse_transform([1, 0, 2])
print("逆轉換 :\n", cc, sep="")

print("------------------------------")  # 30個
print("使用 Pandas Map, 對映")

size_mapping = {"XL": 3, "L": 2, "M": 1}

df["size"] = df["size"].map(size_mapping)
print("轉換後df :\n", df, sep="")

print("------------------------------")  # 30個
print("使用 獨熱編碼 OrdinalEncoder")

data = [["Male", 1], ["Female", 3], ["Female", 2]]
ordinalencoder = OrdinalEncoder()
cc = ordinalencoder.fit_transform(data)
print(cc)

print("使用 Pandas 之 獨熱編碼 OrdinalEncoder")

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

cc = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
print(cc)

# pandas v1.5 above
df2 = pd.get_dummies(df, columns=["color"], prefix="is", prefix_sep="_")
cc = pd.from_dummies(df2[["is_blue", "is_green", "is_red"]], sep="_")
print(cc)

print("使用 獨熱編碼 OrdinalEncoder")

# 測試資料
X = [["Male", 1], ["Female", 3], ["Female", 2]]

# 轉換
onehotencoder = OneHotEncoder(handle_unknown="ignore")
X_new = onehotencoder.fit_transform(X)
cc = X_new.toarray()
print(cc)

# 類別
cc = onehotencoder.categories_
print(cc)

# 還原
cc = onehotencoder.inverse_transform(X_new)
print(cc)

# 指定欄位名稱
cc = onehotencoder.get_feature_names_out(["gender", "group"])
print(cc)

# 完整的表格處理程序

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)
df.columns = ["color", "size", "price", "classlabel"]

# One-hot Encoding
onehotencoder = OneHotEncoder(handle_unknown="ignore")
color_new = onehotencoder.fit_transform(df[["color"]])

# 指定欄位名稱
column_names = onehotencoder.get_feature_names_out(onehotencoder.feature_names_in_)

# 轉換
df_new = pd.DataFrame(color_new.toarray(), columns=column_names)
print(df_new)

# 刪除原欄位 'color'
df.drop(["color"], axis=1, inplace=True)

# 合併表格
df2 = pd.concat([df, df_new], axis=1)
print(df2)

# 儲存模型 joblib.dump(onehotencoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
ROC曲線
Receiver operating characteristic curve
接收者操作特徵曲線
"""
# 繪製ROC曲線

# 載入資料

df = pd.read_csv("./data/roc_test_data.csv")
print(df)

"""
繪製ROC曲線
    計算第二欄的真(1)與假(0)的個數，假設分別為P及N，Y軸切成P格，X軸切成N格，如下圖。
    以第一欄降冪排序，從大排到小。
    依序掃描第二欄，若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格，直到最後一列，如下圖。
"""

# 計算P及N個數

# 計算第二欄的真(1)與假(0)的個數，假設分別為P及N
P = df[df["actual"] == 1].shape[0]
N = df[df["actual"] == 0].shape[0]
print(f"P={P}, N={N}")

# X、Y軸每一格的大小
cc = y_unit = 1 / P
print(cc)
cc = X_unit = 1 / N
print(cc)

# P=11, N=7

# 根據第1欄降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 掃描表格每一列，第二欄若是1，就往『上』畫一格，反之，若是0，就往『右』畫一格

X, y = [], []
current_X, current_y = 0, 0
for row in df2.itertuples():
    # 若是1，Y加1
    if row[2] == 1:
        current_y += y_unit
    else:  # 若是0，X加1
        current_X += X_unit
    # 儲存每一點X/Y座標
    X.append(current_X)
    y.append(current_y)

X = np.array(X)
y = np.array(y)
print(X, y)

# 繪製ROC曲線

plt.title("ROC 曲線")
plt.plot(X, y, color="orange")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

# Scikit-Learn 作法

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
print(f"偽陽率:\n{fpr}\n\n真陽率:\n{tpr}\n\n決策門檻:{threshold}")

"""
偽陽率:
[0.         0.         0.         0.14285714 0.14285714 0.28571429
 0.28571429 0.57142857 0.57142857 0.71428571 0.71428571 1.        ]

真陽率:
[0.         0.09090909 0.27272727 0.27272727 0.63636364 0.63636364
 0.81818182 0.81818182 0.90909091 0.90909091 1.         1.        ]

決策門檻:[1.99 0.99 0.8  0.73 0.56 0.48 0.42 0.32 0.22 0.11 0.1  0.03]
"""

# 繪製ROC曲線

auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 整體學習的錯誤率計算

from scipy.special import comb

# 計算整體學習的錯誤率


def ensemble_error(n_classifier, error):
    k_start = int(math.ceil(n_classifier / 2.0))
    probs = [
        comb(n_classifier, k) * error**k * (1 - error) ** (n_classifier - k)
        for k in range(k_start, n_classifier + 1)
    ]
    return sum(probs)


cc = ensemble_error(n_classifier=11, error=0.25)
print(cc)
# 0.03432750701904297

# 測試各種錯誤率，並繪圖

error_range = np.arange(0.0, 1.01, 0.01)
ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]

plt.plot(error_range, ens_errors, label="整體學習", linewidth=2)

plt.plot(error_range, error_range, linestyle="--", label="個別模型", linewidth=2)

plt.title("錯誤率比較")
plt.xlabel("個別模型錯誤率")
plt.ylabel("整體學習錯誤率")
plt.grid(alpha=0.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Area Under Curve (AUC) of Receiver operating characteristic (ROC)

score_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
thres = 0.9
y_pred = (score_pred > thres).astype(int)

print("With a threshold of %.2f, the rule always predict 0. Predictions:" % thres)
print(y_pred)

accuracy_score(y_true, y_pred)

# The overall precision an recall on each individual class
r = recall_score(y_true, y_pred, average=None)
print(
    "Recalls on individual classes are:",
    r,
    "ie, 100% of specificity, 0% of sensitivity",
)

# However AUC=1 indicating a perfect separation of the two classes
auc = roc_auc_score(y_true, score_pred)
print("But the AUC of %.2f demonstrate a good classes separation." % auc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

bv = np.array([10, 20, 30, 40, 50])  # business volume(營業額)
tax = 0.2 * bv  # Tax
bp = 0.1 * bv + np.array([-0.1, 0.2, 0.1, -0.2, 0.1])  # business potential(商機)

X = np.column_stack([bv, tax])
beta_star = np.array([0.1, 0])  # true solution

# Since tax and bv are correlated, there is an infinite number of linear combinations
# leading to the same prediction.

# 10 times the bv then subtract it 9 times using the tax variable:
beta_medium = np.array([0.1 * 10, -0.1 * 9 * (1 / 0.2)])

# 100 times the bv then subtract it 99 times using the tax variable:
beta_large = np.array([0.1 * 100, -0.1 * 99 * (1 / 0.2)])

print("L2 norm of coefficients:")
print("small : %.2f" % (np.sum(beta_star**2)))
print("medium :%.2f" % (np.sum(beta_medium**2)))
print("large : %.2f." % (np.sum(beta_large**2)))

print("However all models provide the exact same predictions.")
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_medium))
assert np.all(np.dot(X, beta_star) == np.dot(X, beta_large))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# **Regression**

N = 50  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
T = 1  # n_targets, 標籤類別
NOISE = 10  # noise, 分散程度

print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y, coef = datasets.make_regression(
    n_samples=N,
    n_features=M,
    noise=NOISE,
    n_informative=2,
    random_state=9487,
    coef=True,
)

print("== Ridge (L2 penalty) ==")
model = sklearn.linear_model.RidgeCV(cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== Lasso (L1 penalty) ==")
model = sklearn.linear_model.LassoCV(n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

print("== ElasticNet (L1 penalty) ==")
model = sklearn.linear_model.ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], n_jobs=-1, cv=3)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

# Regression dataset where first 2 features are predictives
n_features = 5
n_features_info = 2
n_samples = 100
X = np.random.randn(100, 5)
beta = np.zeros(n_features)
beta[:n_features_info] = 1
Xbeta = np.dot(X, beta)
eps = np.random.randn(n_samples)
y = Xbeta + eps

# Random permutations

# Fit model on all data (!! risk of overfit)
model = sklearn.linear_model.RidgeCV()

model.fit(X, y)  # 學習訓練.fit

print("Coefficients on all data:")
print(model.coef_)

# Random permutation loop
nperm = 1000  # !! Should be at least 1000 (to assess a p-value at 1%)
scores_names = ["r2"]
scores_perm = np.zeros((nperm + 1, len(scores_names)))
coefs_perm = np.zeros((nperm + 1, X.shape[1]))

scores_perm[0, :] = r2_score(y, model.predict(X))
coefs_perm[0, :] = model.coef_

orig_all = np.arange(X.shape[0])
for perm_i in range(1, nperm + 1):
    model.fit(X, np.random.permutation(y))  # 學習訓練.fit
    y_pred = model.predict(X).ravel()  # 預測.predict
    scores_perm[perm_i, :] = r2_score(y, y_pred)
    coefs_perm[perm_i, :] = model.coef_

# One-tailed empirical p-value
pval_pred_perm = np.sum(scores_perm >= scores_perm[0]) / scores_perm.shape[0]
pval_coef_perm = np.sum(coefs_perm >= coefs_perm[0, :], axis=0) / coefs_perm.shape[0]

print("R2 p-value: %0.3f" % pval_pred_perm)
print("Coeficients p-values:", np.round(pval_coef_perm, 3))

# Compute p-values corrected for multiple comparisons using FWER max-T
# (Westfall and Young, 1993) procedure.

pval_coef_perm_tmax = (
    np.array(
        [
            np.sum(coefs_perm.max(axis=1) >= coefs_perm[0, j])
            for j in range(coefs_perm.shape[1])
        ]
    )
    / coefs_perm.shape[0]
)
print("P-values with FWER (Westfall and Young) correction")
print(pval_coef_perm_tmax)

# Plot distribution of third coefficient under null-hypothesis
# Coeffitients 0 and 1 are significantly different from 0.


def hist_pvalue(perms, ax, name):
    """Plot statistic distribution as histogram.
    Paramters
    ---------
    perms: 1d array, statistics under the null hypothesis.
           perms[0] is the true statistic .
    """
    # Re-weight to obtain distribution
    pval = np.sum(perms >= perms[0]) / perms.shape[0]
    weights = np.ones(perms.shape[0]) / perms.shape[0]
    ax.hist(
        [perms[perms >= perms[0]], perms],
        histtype="stepfilled",
        bins=100,
        label="p-val<%0.3f" % pval,
        weights=[weights[perms >= perms[0]], weights],
    )
    ax.axvline(x=perms[0], color="k", linewidth=2)  # , label="observed statistic")
    ax.set_ylabel(name)
    ax.legend()
    return ax


n_coef = coefs_perm.shape[1]
fig, axes = plt.subplots(n_coef, 1, figsize=(12, 9))
for i in range(n_coef):
    hist_pvalue(coefs_perm[:, i], axes[i], str(i))

_ = axes[-1].set_xlabel("Coefficient distribution under null hypothesis")

# Bootstrap loop
nboot = 100  # !! Should be at least 1000
scores_names = ["r2"]
scores_boot = np.zeros((nboot, len(scores_names)))
coefs_boot = np.zeros((nboot, X.shape[1]))

orig_all = np.arange(X.shape[0])
for boot_i in range(nboot):
    boot_tr = np.random.choice(orig_all, size=len(orig_all), replace=True)
    boot_te = np.setdiff1d(orig_all, boot_tr, assume_unique=False)
    Xtr, ytr = X[boot_tr, :], y[boot_tr]
    Xte, yte = X[boot_te, :], y[boot_te]
    model.fit(Xtr, ytr)  # 學習訓練.fit
    y_pred = model.predict(Xte).ravel()  # 預測.predict
    scores_boot[boot_i, :] = r2_score(yte, y_pred)
    coefs_boot[boot_i, :] = model.coef_

# Compute Mean, SE, CI
# Coeffitients 0 and 1 are significantly different from 0.

scores_boot = pd.DataFrame(scores_boot, columns=scores_names)
scores_stat = scores_boot.describe(percentiles=[0.975, 0.5, 0.025])

print(
    "r-squared: Mean=%.2f, SE=%.2f, CI=(%.2f %.2f)"
    % tuple(scores_stat.loc[["mean", "std", "2.5%", "97.5%"], "r2"])
)

coefs_boot = pd.DataFrame(coefs_boot)
coefs_stat = coefs_boot.describe(percentiles=[0.975, 0.5, 0.025])
print("Coefficients distribution")
print(coefs_stat)

# Plot coefficient distribution

df = pd.DataFrame(coefs_boot)
staked = pd.melt(df, var_name="Variable", value_name="Coef. distribution")
sns.set_theme(style="whitegrid")
ax = sns.violinplot(x="Variable", y="Coef. distribution", data=staked)
_ = ax.axhline(0, ls="--", lw=2, color="black")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一個很大的範例 ST")
"""
探索性數據分析（EDA）

EDA指對已有的數據用可視化等手段探索數據的結構和規律的一種數據分析方法，
其目的是最大化對數據的直覺，完成這個事情的方法是結合統計學的圖形以各種形式展現出來。
在深入機器學習或統計建模之前，EDA是一個重要的步驟，
這是因為它提供了為現有問題開發適當模型并正確解釋其結果所需的來龍去脈。
EDA通常涉及以下幾種方法的組合：
.原始數據集中每個字段的單變量可視化和匯總統計
.數據集中每個變量與感興趣目標變量之間的關系的雙變量可視化和匯總統計
.多元可視化以了解數據中不同字段之間的交互作用
.降維以了解數據,通過將數據折疊成幾個小數據點讓觀察值聚類成有區別的小組，
可以更容易地識別行為模式
"""

import scipy.stats as stats
import sklearn.linear_model as linear_model

# 共 1460 筆資料, 81 欄位
train = pd.read_csv("data/houseprice.csv")

print("訓練數據集基本信息")
# many print(train.info())
print("train.shape :", train.shape)  # 1460 X 81

# 前幾筆資料 print(train.head())

# 1.1 首先，區分出數據中的數值型變量和類別型變量
# 數值型變量

quantitative = [f for f in train.columns if train.dtypes[f] != "object"]
quantitative.remove("SalePrice")
quantitative.remove("Id")

print("quantitative len :", len(quantitative))

# 類別型變量
qualitative = [f for f in train.columns if train.dtypes[f] == "object"]

ccs = [
    "FullBath",
    "HalfBath",
    "TotRmsAbvGrd",
    "Fireplaces",
    "GarageYrBlt",
    "GarageCars",
    "OverallQual",
]
for col in ccs:
    if col in quantitative:
        quantitative.remove(col)
    if not col in qualitative:
        qualitative.append(col)

print("訓練集樣本數量：{}".format(train.shape[0]))  # 1460
print("數值型變量共有：{}".format(len(quantitative)))  # 29
print("類別型變量共有：{}".format(len(qualitative)))  # 50

# 1.2查看缺失值的分布情況

missing = train.isnull().sum() / train.shape[0]

print("missing資料")
print(missing.head())

missing = missing[missing > 0]
print("有缺失值的變量共有 : {}".format(len(missing)))  # 19

missing.sort_values(inplace=True)
print("缺失率超過50%的有 {} 個".format(len(missing[missing >= 0.5])))  # 5

print(missing[missing >= 0.5])

missing.plot.bar()
plt.title("有缺失值的變量")
show()

print("可以直接刪除這幾個變量")

missing_cols = missing[missing >= 0.5].index.tolist()

for col in missing_cols:
    if col in quantitative:
        quantitative.remove(col)
    if col in qualitative:
        qualitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))  # 29
print("類別型變量共有：{}".format(len(qualitative)))  # 45

# 2 數值型變量
# 2.1 查看目標變量saleprice是否服從正態分布

import scipy.stats as st

y = train["SalePrice"]

sns.histplot(y, kde=False)
plt.title("預設方法")
show()
""" 不能使用參數fit
sns.histplot(y, kde=True, fit=st.johnsonsu)
plt.title("使用 Johnson SU")
show()

sns.histplot(y, kde=False, fit=st.norm)
plt.title("使用 Normal")
show()

sns.histplot(y, kde=False, fit=st.lognorm)
plt.title("使用 Log Normal")
show()

# 另一種查看是否服從正態分布的可視化方法
sns.histplot(train["SalePrice"], fit=st.norm)
plt.title("使用 Normal")
show()
"""
res = st.probplot(train["SalePrice"], plot=plt)
show()

# 把房價做對數變換後再看
SalePrice_log = np.log(train["SalePrice"])

# transformed histogram and normal probability plot
# 不能使用參數fit
# sns.histplot(SalePrice_log, fit=st.norm)
# show()

res = st.probplot(SalePrice_log, plot=plt)
print(res)

show()

"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))
顯然，房價本身不服從正態分布，是不能直接用來做回歸建模的。但是經過對數轉換之後，就好了很多。
對于其它的數值型變量，也同樣要做分布的正態性檢驗.
檢驗方法就用：夏皮羅-威爾克(Shapiro-Wilk)法檢驗數據正態性,即W檢驗。
"""

check_normality = lambda x: stats.shapiro(x.fillna(0))[1] < 0.01

normal = pd.DataFrame(train[quantitative])
normal = normal.apply(check_normality)

print(normal.sort_values(ascending=False).head(4))

normal = normal < 0.01
print(not normal.any())

"""
YrSold          True
LowQualFinSF    True
LotFrontage     True
LotArea         True
dtype: bool     True
可以發現所有的數值型變量都沒能通過正態性分布檢驗，都需要做轉換。
我們可以把所有的數值型變量的分布曲線都畫出來，從可視化角度進一步驗證這個判斷
"""

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")
show()

df = pd.DataFrame(
    {"A": {0: "a", 1: "b", 2: "c"}, "B": {0: 1, 1: 3, 2: 5}, "C": {0: 2, 1: 4, 2: 6}}
)
print(df)

pd.melt(df, id_vars=["A"], value_vars=["B", "C"])
print(df)

# 看起來TotalBsmtSF, KitchenAbvGr, LotFrontage, LotArea這幾個變量似乎更適合做些變型，以使其服從正態分布。
# 2.2 異常值分析
# 對saleprice做標準化後再看

"""
# NG
saleprice_scaled = StandardScaler().fit_transform(train["SalePrice"][:, np.newaxis])
low_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][:10]
high_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][-10:]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)
"""

"""
outer range (low) of the distribution:
[[-1.83870376]
 [-1.83352844]
 [-1.80092766]
 [-1.78329881]
 [-1.77448439]
 [-1.62337999]
 [-1.61708398]
 [-1.58560389]
 [-1.58560389]
 [-1.5731    ]]

outer range (high) of the distribution:
[[ 3.82897043]
 [ 4.04098249]
 [ 4.49634819]
 [ 4.71041276]
 [ 4.73032076]
 [ 5.06214602]
 [ 5.42383959]
 [ 5.59185509]
 [ 7.10289909]
 [ 7.22881942]]

"""

# 低房價并沒有太多異常，但是高房價有兩個超過了7，雖然不一定是異常值，但是要小心
# 2.3 查看數值型變量和待預測變量之間的相關性
# 常用pearson相關系數，它是用有前提條件，并且是有局限的——判斷線性相關，非線性相關它是無能為力的。
# Spearman相關系數 vs pearson相關系數的優點：對于數據分布沒有要求。也叫秩和。


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")
    return spr


features = quantitative

spr = spearman(train, features)
show()

# 刪除相關系數小于0.3的變量

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

for col in spr[abs(spr["spearman"]) < 0.3].feature:
    if col in quantitative:
        quantitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
數值型變量共有：29
類別型變量共有：46
數值型變量共有：12
類別型變量共有：46
"""

# 用散點圖觀察數值型變量之間的關系
# scatterplot

from copy import copy

sns.set(font_scale=2)
cols1 = copy(quantitative)
cols1.append("SalePrice")
sns.pairplot(train[cols1].fillna(0.0), height=2.5)
show()

# scatterplot

sns.set(font_scale=2)

cols1 = copy(quantitative[:6])

cols1.append("SalePrice")

sns.pairplot(train[cols1].fillna(0.0), height=2.5)

cols2 = copy(quantitative[6:])

cols2.append("SalePrice")

sns.pairplot(train[cols2].fillna(0.0), height=2.5)

show()

"""
3.類別型變量
對于類別型的變量，要觀察目標變量（sale_price）在類別的各個取值上的分布情況；用分組箱線圖
對于類別型變量的缺失值，不再用0填充，而是用一個特殊的值'Missing'填充。
"""

for c in qualitative:
    train[c] = train[c].astype("category")
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(["MISSING"])
        train[c] = train[c].fillna("MISSING")


def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x = plt.xticks(rotation=90)


f = pd.melt(train, id_vars=["SalePrice"], value_vars=qualitative)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(boxplot, "value", "SalePrice")

show()

"""
看起來像LotConfig、LandSlope這樣的變量，對于房價的影響似乎不大。
Neighborhood對房價有影響。然後每個類別的不同子類之間看起來似乎也有差別。
overallQual的值太多。

具體到一個分類指標和數值型變量之間的相關關系，我們可以用方差分析進行檢查。
3.2 方差分析
"""


def anova(frame):
    anv = pd.DataFrame()
    anv["feature"] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]["SalePrice"].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")


a = anova(train)
a["disparity"] = np.log(1.0 / a["pval"].values)
sns.barplot(data=a, x="feature", y="disparity")
x = plt.xticks(rotation=90)
show()

"""
這里我們用了方差分析，來看每一個類別變量和預測變量Sale_price之間是否有相關關系。
因為我們最後得到了個p值，p>0.05說明樣本的分組之間沒有顯著性差異，
p值越小說明差異越顯著。
因為我們想用一個類似于“變異度”的指標——“差異度”，
我們希望這個指標越大，說明差異越明顯。也就是想要一個同向變化的指標，所以對p值取了個倒數。
僅此而已。

對于這些分類變量的每個值做正確編碼
另一種編碼方式是OneHotEncoding或者dummy
"""


def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering["val"] = frame[feature].unique()
    ordering.index = ordering.val
    ordering["spmean"] = (
        frame[[feature, "SalePrice"]].groupby(feature).mean()["SalePrice"]
    )
    ordering = ordering.sort_values("spmean")
    ordering["ordering"] = range(1, ordering.shape[0] + 1)
    ordering = ordering["ordering"].to_dict()

    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature + "_E"] = o


qual_encoded = []
for q in qualitative:
    encode(train, q)
    qual_encoded.append(q + "_E")

print(qual_encoded)

"""
['MSZoning_E', 'Street_E', 'LotShape_E', 'LandContour_E', 'Utilities_E', 'LotConfig_E', 'LandSlope_E', 'Neighborhood_E', 'Condition1_E', 'Condition2_E', 'BldgType_E', 'HouseStyle_E', 'RoofStyle_E', 'RoofMatl_E', 'Exterior1st_E', 'Exterior2nd_E', 'MasVnrType_E', 'ExterQual_E', 'ExterCond_E', 'Foundation_E', 'BsmtQual_E', 'BsmtCond_E', 'BsmtExposure_E', 'BsmtFinType1_E', 'BsmtFinType2_E', 'Heating_E', 'HeatingQC_E', 'CentralAir_E', 'Electrical_E', 'KitchenQual_E', 'Functional_E', 'FireplaceQu_E', 'GarageType_E', 'GarageFinish_E', 'GarageQual_E', 'GarageCond_E', 'PavedDrive_E', 'SaleType_E', 'SaleCondition_E', 'FullBath_E', 'HalfBath_E', 'TotRmsAbvGrd_E', 'Fireplaces_E', 'GarageYrBlt_E', 'GarageCars_E', 'OverallQual_E']
"""
print(train.head(3))

"""
	Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PavedDrive_E	SaleType_E	SaleCondition_E	FullBath_E	HalfBath_E	TotRmsAbvGrd_E	Fireplaces_E	GarageYrBlt_E	GarageCars_E	OverallQual_E
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	8.0	1.0	86.0	3.0	7.0
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	2.0	5.0	2.0	57.0	3.0	6.0
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	5.0	2.0	91.0	3.0	7.0
3 rows × 127 columns
"""

print(train["GarageQual_E"].value_counts())

"""
4.0    1311
,2.0      81
,3.0      48
,5.0      14
,6.0       3
,1.0       3
,Name: GarageQual_E, dtype: int64
3.4.查看衍生變量和房價的Spearman相關性
對于相關性的檢測我們使用的是Spearman correlation，
這種檢驗方法的好處是即使是非線性相關也能檢測出來。
"""

sns.set(font_scale=1.2)


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")


features = qual_encoded
spearman(train, features)
show()

"""
顯然，OverallQual和房價的關系最明顯。房子的鄰居和位置看起來也是有影響的。

觀察變量之間的相關性
回歸模型對于變量共線的容忍度差，所以，我們需要考慮變量之間的相關性。
用相關系數矩陣的熱力圖即可。
"""

sns.set(font_scale=1)

corr = train[quantitative + ["SalePrice"]].corr("spearman")

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

# from functools import partial
# # my_heatmap=partial(sns.heatmap,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

# 相關係數
corr = train[qual_encoded + ["SalePrice"]].corr()
sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

corr = pd.DataFrame(
    np.zeros([len(quantitative) + 1, len(qual_encoded) + 1]),
    index=quantitative + ["SalePrice"],
    columns=qual_encoded + ["SalePrice"],
)
for q1 in quantitative + ["SalePrice"]:
    for q2 in qual_encoded + ["SalePrice"]:
        corr.loc[q1, q2] = train[q1].corr(train[q2])

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

show()

"""
觀察所有變量（包括衍生變量）和目標變量之間的關系

現在所有類別型變量也做了重新編碼，編碼成數值型。所有所有的特征都可以看作是數值型的了。
于是，我們可以再次全景式觀察變量和目標變量之間的關系。
"""


def pairplot(x, y, **kwargs):
    ax = plt.gca()
    ts = pd.DataFrame({"time": x, "val": y})
    ts = ts.groupby("time").mean()
    ts.plot(ax=ax)
    plt.xticks(rotation=90)


# 畫散點圖
sns.set(style="ticks", color_codes=True)

f = pd.melt(train, id_vars=["SalePrice"], value_vars=quantitative + qual_encoded)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(pairplot, "value", "SalePrice")

show()

"""
看起來，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E
There are lots of nonlinearities this may be the cause
why some variables wont be selected by Lasso/Lars.
Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E
look like they would benefit from adding quadratic term to regression.
But on the other hand this will most probably provoke overfit.

觀察的結果提示我們，有些變量可以嘗試做些變換，比如平方變換。

高級內容

考慮數據本身是否分群，如果分群，就可以用分段回歸。

接下來，考慮是否可以分段進行回歸。

我們把房價200000作為分界點，之下的作為普通住宅，之上的作為豪宅，
然後看看在這樣分開後，那些數值型變量的均值有多大差異。
"""

features = quantitative
standard = train[train["SalePrice"] < 200000]
pricey = train[train["SalePrice"] >= 200000]

diff = pd.DataFrame()
diff["feature"] = features
diff["difference"] = [
    (pricey[f].fillna(0.0).mean() - standard[f].fillna(0.0).mean())
    / (standard[f].fillna(0.0).mean())
    for f in features
]

sns.barplot(data=diff, x="feature", y="difference")
x = plt.xticks(rotation=90)

print(diff)

show()

"""
	feature	difference
0	MSSubClass	-0.150366
1	LotFrontage	0.238321
2	LotArea	0.536645
3	OverallQual	0.361440
4	OverallCond	-0.047635
5	YearBuilt	0.015026
6	YearRemodAdd	0.010197
7	MasVnrArea	2.029480
8	BsmtFinSF1	0.729316
9	BsmtFinSF2	-0.023328
10	BsmtUnfSF	0.410808
11	TotalBsmtSF	0.515235
12	1stFlrSF	0.396664
13	2ndFlrSF	0.978444
14	LowQualFinSF	-0.298300
15	GrLivArea	0.512153
16	BsmtFullBath	0.577215
17	BsmtHalfBath	-0.487756
18	FullBath	0.424714
19	HalfBath	0.684120
20	BedroomAbvGr	0.092859
21	KitchenAbvGr	-0.050115
22	TotRmsAbvGrd	0.257338
23	Fireplaces	1.102258
24	GarageYrBlt	0.090733
25	GarageCars	0.550690
26	GarageArea	0.596397
27	WoodDeckSF	0.950341
28	OpenPorchSF	1.314906
29	EnclosedPorch	-0.479096
30	3SsnPorch	0.881312
31	ScreenPorch	0.623489
32	PoolArea	2.213669
33	MiscVal	-0.559517
34	MoSold	0.052589
35	YrSold	-0.000021

我們用tnse方法，把每個高維樣本映射到二維平面上的點。
然後我們對樣本做標準化處理，處理之後做PCA，提取前30個主成分。也就是把樣本的特征降維到30個特征。
對這30個特征的樣本聚類，聚成5類。
在把這5類用可視化的方法會出來，看看是否有聚集趨勢。
"""

from sklearn.manifold import TSNE

features = quantitative + qual_encoded
model = TSNE(n_components=2, random_state=0, perplexity=50)
X = train[features].fillna(0.0).values
tsne = model.fit_transform(X)

std = StandardScaler()
s = std.fit_transform(X)

pca = PCA(n_components=40)

pca.fit(s)  # 學習訓練.fit

pc = pca.transform(s)

kmeans = KMeans(n_clusters=5)

kmeans.fit(pc)  # 學習訓練.fit

fr = pd.DataFrame({"tsne1": tsne[:, 0], "tsne2": tsne[:, 1], "cluster": kmeans.labels_})

sns.lmplot(data=fr, x="tsne1", y="tsne2", hue="cluster", fit_reg=False)

show()

print(np.sum(pca.explained_variance_ratio_))

"""
0.846903058622
看起來聚集趨勢并不明顯，所以分段回歸的意義似乎不大。
另外40個主成分能解釋84%的方差。
"""

y = train["SalePrice"].values


def johnson(y):
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)  # 學習訓練.fit
    yt = gamma + eta * np.arcsinh((y - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon


yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

sns.histplot(yt)
show()

sns.histplot(yt2)
show()

# 5.最後建模


def error(actual, predicted):
    actual = np.log(actual)
    predicted = np.log(predicted)
    return np.sqrt(np.sum(np.square(actual - predicted)) / len(actual))


def log_transform(feature):
    train[feature] = np.log1p(train[feature].values)


def quadratic(feature):
    train[feature + "2"] = train[feature] ** 2


# 下面這些特征做log轉化
log_transform("GrLivArea")
log_transform("1stFlrSF")
log_transform("2ndFlrSF")
log_transform("TotalBsmtSF")
log_transform("LotArea")
log_transform("LotFrontage")
log_transform("KitchenAbvGr")
log_transform("GarageArea")

# 下面這些特征取平方轉換
# quadratic('OverallQual') fail
quadratic("YearBuilt")
quadratic("YearRemodAdd")
quadratic("TotalBsmtSF")
quadratic("2ndFlrSF")
quadratic("Neighborhood_E")
quadratic("RoofMatl_E")
quadratic("GrLivArea")

qdr = [
    "OverallQual2",
    "YearBuilt2",
    "YearRemodAdd2",
    "TotalBsmtSF2",
    "2ndFlrSF2",
    "Neighborhood_E2",
    "RoofMatl_E2",
    "GrLivArea2",
]

# 下面這些特征做二值化
train["HasBasement"] = train["TotalBsmtSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasGarage"] = train["GarageArea"].apply(lambda x: 1 if x > 0 else 0)
train["Has2ndFloor"] = train["2ndFlrSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasMasVnr"] = train["MasVnrArea"].apply(lambda x: 1 if x > 0 else 0)
train["HasWoodDeck"] = train["WoodDeckSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPorch"] = train["OpenPorchSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPool"] = train["PoolArea"].apply(lambda x: 1 if x > 0 else 0)
train["IsNew"] = train["YearBuilt"].apply(lambda x: 1 if x > 2000 else 0)

boolean = [
    "HasBasement",
    "HasGarage",
    "Has2ndFloor",
    "HasMasVnr",
    "HasWoodDeck",
    "HasPorch",
    "HasPool",
    "IsNew",
]

features = quantitative + qual_encoded + boolean + qdr
lasso = linear_model.LassoLarsCV(max_iter=10000)

""" NG
# sklearn中要求X，y都是矩陣形式，而不是數據框
X = train[features].fillna(0.).values
Y = train['SalePrice'].values

lasso.fit(X, np.log(Y))  # 學習訓練.fit

#反log1p變換
Ypred = np.exp(lasso.predict(X))  # 預測.predict

print(error(Y, Ypred))
"""
print("一個很大的範例 SP")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" tfnn引用錯誤
import tfnn

bank_data = pd.read_csv("data/bank-full.csv", sep=";")

data = tfnn.Data(bank_data.iloc[:, :-1], bank_data.iloc[:, -1])
data.encode_cat_y(inplace=True)
data.encode_cat_x(inplace=True)
network = tfnn.ClfNetwork(
    data.xs.shape[1],
    data.ys.shape[1],
)
data = network.normalizer.minmax_fit(data, -1, 1)
train_data, test_data = data.train_test_split()
network.add_hidden_layer(50, activator=tfnn.nn.relu)
network.add_output_layer(activator=None)
network.set_optimizer(tfnn.train.GradientDescentOptimizer(0.0001))
evaluator = tfnn.Evaluator(network)

for i in range(1000):
    b_xs, b_ys = train_data.next_batch(100, loop=True)
    network.run_step(b_xs, b_ys)
    if i % 50 == 0:
        print(evaluator.compute_accuracy(test_data.xs, test_data.ys))
# print(test_data.ys.iloc[:,0].value_counts())
print(network.predict(test_data.xs.iloc[20:30, :]))  # 預測.predict
print(test_data.ys.iloc[20:30, :])
"""
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

# X -= X.mean(axis=0)  # Centering is required

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 以下OK 可搬出

""" NG
print("混同行列")

cm = confusion_matrix(y, y_pred)
print(cm)

print("------------------------------")  # 30個

print("正解率")
accuracy_score(y, y_pred)

print("------------------------------")  # 30個

print("適合率")
precision_score(y, y_pred)

print("------------------------------")  # 30個

print("再現率")
recall_score(y, y_pred)

print("------------------------------")  # 30個

print("F値")
f1_score(y, y_pred)

print("------------------------------")  # 30個

print("予測確率")
logistic_regression.predict_proba(X)

print("------------------------------")  # 30個

y_pred2 = (logistic_regression.predict_proba(X)[:, 1] > 0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print("------------------------------")  # 30個

print("ROC曲線・AUC")
probas = logistic_regression.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print("------------------------------")  # 30個

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, "gray")
ax.fill_between(fpr, tpr, 0, color="skyblue", alpha=0.8)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_facecolor("xkcd:white")
show()

print("------------------------------")  # 30個

roc_auc_score(y, probas[:, 1])

print("------------------------------")  # 30個

print("平均二乗誤差")
mean_squared_error(y, y_pred)

print("------------------------------")  # 30個

print("決定係數")
print(r2_score(y, y_pred))

print("------------------------------")  # 30個

print("異なるアルゴリズムを利用した場合との比較")

from sklearn.svm import SVR

model_svr_linear = SVR(C=0.01, kernel="linear")

model_svr_linear.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_linear.predict(X)  # 預測.predict
print(y_svr_pred)

"""
fig, ax = plt.subplots()
ax.scatter(X, y, color="pink", marker="s", label="data set")
ax.plot(X, y_pred, color="blue", label="regression curve")
ax.plot(X, y_svr_pred, color="red", label="SVR")
ax.legend()
show()
"""

print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係數
print(model_svr_linear.coef_)  # 傾き
print(model_svr_linear.intercept_)  # 切片

print("------------------------------")  # 30個

print("ハイパーパラメータの設定")

model_svr_rbf = SVR(C=1.0, kernel="rbf")

model_svr_rbf.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_rbf.predict(X)  # 預測.predict
print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係數

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]

model_svr_rbf_1 = SVR(C=1.0, kernel="rbf")

model_svr_rbf_1.fit(train_X, train_y)  # 學習訓練.fit

test_y_pred = model_svr_rbf_1.predict(test_X)  # 預測.predict
print(mean_squared_error(test_y, test_y_pred))  # 平均二乗誤差
print(r2_score(test_y, test_y_pred))  # 決定係數

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個


# pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 20


missing.plot.bar(figsize=(6, 4))

plt.figure(1)


# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# 可搬出

"""
data/test3.csv
性別,尺寸,價格
male,XL,800
female,M,400
not specified,XXL,300
male,L,500
female,S,700
female,XS,850
"""

df = pd.read_csv("data/test3.csv")
print(df)

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Encoding categorical features

# get_dummies 是 利用pandas實現one-hot-encoding(獨熱編碼)的方式
print(pd.get_dummies(["A", "B", "C", "A", "B", "D"]))

df = pd.DataFrame([["green", "A"], ["red", "B"], ["blue", "A"]])

df.columns = ["color", "class"]

print("get_dummies前 :")
print(df)

print("get_dummies後 :")
df2 = pd.get_dummies(df)
print(df2)

print("可以对指定列进行get_dummies")

df3 = pd.get_dummies(df.color)
print(df3)

print("将指定列进行get_dummies 後合并到元数据中")

df4 = df.join(pd.get_dummies(df.color))
print(df4)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# [平均]輪廓係數 silhouette_score
print(
    "Silhouette Coefficient: %0.3f"
    % metrics.silhouette_score(X, kmean.labels_, sample_size=1000)
)


print("預測結果 :\n", y_pred, sep="")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
