"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
"""
#鳶尾花(Iris)品種的辨識
ds = datasets.load_iris()

#乳癌診斷預測
ds = datasets.load_breast_cancer()
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. 載入資料集

ds = datasets.load_iris()
"""
print("資料集說明")
print(ds.DESCR)

print("資料集欄位")
print(ds.feature_names)

print("資料集資料")
print(ds.data)

print("資料集目標名稱")
print(ds.target_names)

print("資料集目標")
print(ds.target)
"""

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(ds.data, columns=ds.feature_names)
# print(df)

# 資料集目標
y = ds.target
# print(y)
# 資料集目標名稱
# print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

print("描述統計量")
cc = df.describe()
print(cc)

# 箱型圖
import seaborn as sns

sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
plt.show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
import seaborn as sns
sns.countplot(x=y)
plt.title('y 各類別資料筆數統計')
plt.show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
# print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
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
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
plt.show()

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_model.joblib")
joblib.dump(scaler, "tmp_scaler.joblib")

print("------------------------------------------------------------")  # 60個

import joblib

# 10.模型預測

# 載入模型與標準化轉換模型
clf = joblib.load("tmp_model.joblib")
scaler = joblib.load("tmp_scaler.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]

print("### 預測品種是：", labels[clf.predict(X_new)[0]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
"""
#Scikit-learn_Toy datasets

#載入酒類資料集

"""

from sklearn import datasets

ds = datasets.load_wine()

print("資料集說明")

print(ds.DESCR)

print("資料集的特徵(X)")

import pandas as pd

df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

print("資料集的目標(Y)")
print(ds.target)

print("目標(Y)的名稱，即標註(Label)")
print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

print("描述統計量")
cc = df.describe()
print(cc)

print("另一種載入資料集的方法")

X, y = datasets.load_wine(return_X_y=True)
print(X)

print(y)

print("------------------------------------------------------------")  # 60個

# 人臉辨識資料集(Labeled Faces in the Wild, LFW)

from sklearn.datasets import fetch_lfw_people

# 載入資料集

ds = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# 2. 資料清理、資料探索與分析

# 資料集說明
print(ds.DESCR)

# 資料維度
n_samples, h, w = ds.images.shape

X = ds.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = ds.target
target_names = ds.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

print(ds.target_names)

# 是否有含遺失值(Missing value)
import numpy as np

cc = np.isnan(X).sum()
print(cc)


print("# y 各類別資料筆數統計")
import pandas as pd

df_y = pd.DataFrame({"code": y})
df_y["name"] = df_y["code"].map(dict(enumerate(ds.target_names)))

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="name", data=df_y)
plt.xticks(rotation=30)

plt.show()

print("以Pandas函數統計各類別資料筆數")
pd.Series(y).value_counts()

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=500)

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
from sklearn.metrics import accuracy_score

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.xticks(rotation=30)
plt.show()

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 10.模型預測，暫不進行

print("------------------------------------------------------------")  # 60個

# 新聞資料集

from sklearn.datasets import fetch_20newsgroups

# 載入資料集

# 篩選新聞類別
categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

data_train = fetch_20newsgroups(
    subset="train",
    categories=categories,
    shuffle=True,
)

print("------------------------------------------------------------")  # 60個

# Generated datasets

from sklearn.datasets import (
    make_classification,
    make_blobs,
    make_regression,
    make_circles,
    make_moons,
)

# 載入分類資料集

X, y = make_classification(
    n_samples=100,
    n_classes=3,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=5,
)
print(X.shape)

# 繪圖

import matplotlib.pyplot as plt

# 樣本點的形狀
markers = ["x", "o", "^"]

# 針對類別各畫一個散佈圖
for k in range(3):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, marker=markers[k], s=50)
plt.show()

# 載入集群資料集

X, y, centers = make_blobs(
    n_samples=100, centers=3, cluster_std=1, n_features=2, return_centers=True
)
print(X.shape)

print(centers)

import matplotlib.pyplot as plt

# 樣本點的形狀
markers = ["x", "o", "^"]

# 針對類別各畫一個散佈圖
for k in range(3):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, marker=markers[k], s=50)

# 繪製集群中心點
X_0 = []
X_1 = []
for i in range(len(centers)):
    X_0.append(centers[i, 0])
    X_1.append(centers[i, 1])
plt.scatter(X_0, X_1, marker="s", s=200, alpha=0.5)

plt.show()

# 載入迴歸資料集

X, y, coef = make_regression(
    n_samples=100, n_features=1, noise=20, coef=True, random_state=123
)
print(X.shape)

print(coef)

plt.scatter(X[:, 0], y)
plt.plot([min(X), max(X)], [min(X) * coef, max(X) * coef], "r")
plt.show()

# 載入非線性的資料集

X, y = make_moons(n_samples=100, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])
plt.show()

# 載入圓形分佈的資料集

X, y = make_circles(n_samples=100, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])
plt.show()

print("------------------------------------------------------------")  # 60個

# 鐵達尼號資料清理

import seaborn as sns
import pandas as pd

# 載入鐵達尼號資料集

df = sns.load_dataset("titanic")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

cc = df.describe(include="O")
print(cc)

cc = df.describe(include="all")
print(cc)

# 遺失值(Missing value)處理

cc = df.isnull().sum()
print(cc)

# 年齡(age)遺失值(Missing value)以中位數取代

df.age.fillna(df.age.median(), inplace=True)
cc = df.isnull().sum()
print(cc)

# 上船港口(embark_town)遺失值(Missing value)以前一筆取代

# 取得遺失值的列數
cc = df[pd.isna(df.embark_town)]
print(cc)

# 以前一筆取代
df.embark_town.fillna(method="ffill", inplace=True)
cc = df.loc[[61, 829]]
print(cc)

# 驗證
cc = df.loc[[61 - 1, 829 - 1]]
print(cc)

# 上船港口(embarked)遺失值(Missing value)以後一筆取代

# 取得遺失值的列數
cc = df[pd.isna(df.embarked)]
print(cc)

# 以後一筆取代
df.embarked.fillna(method="bfill", inplace=True)
cc = df.loc[[61, 829]]
print(cc)

# 驗證
cc = df.loc[[61 + 1, 829 + 1]]
print(cc)

# 甲板(deck)遺失值過多，刪除該欄位

df.drop("deck", axis=1, inplace=True)
cc = df.info()
print(cc)

# 離群值(Outlier) 處理

import matplotlib.pyplot as plt

plt.boxplot(df.age)
plt.show()


def get_box_plot_data(labels, bp):
    rows_list = []

    for i in range(len(labels)):
        dict1 = {}
        dict1["label"] = labels[i]
        dict1["最小值"] = bp["whiskers"][i * 2].get_ydata()[1]
        dict1["箱子下緣"] = bp["boxes"][i].get_ydata()[1]
        dict1["中位數"] = bp["medians"][i].get_ydata()[1]
        dict1["箱子上緣"] = bp["boxes"][i].get_ydata()[2]
        dict1["最大值"] = bp["whiskers"][(i * 2) + 1].get_ydata()[1]
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)


bp = plt.boxplot(df.age)
get_box_plot_data(["age"], bp)
plt.show()

"""
	label 	最小值 	箱子下緣 	中位數 	箱子上緣 	最大值
0 	age 	3.0 	22.0 	28.0 	35.0 	54.0
"""

df = df[(3.0 <= df.age) & (df.age <= 54.0)]
plt.hist(df.age)
plt.show()


# 類別變數轉換為數值

df.sex = df.sex.map({"male": 1, "female": 0})
cc = df.head()
print(cc)

df.embark_town = df.embark_town.map({"Southampton": 0, "Cherbourg": 1, "Queenstown": 2})
cc = df.head()
print(cc)

# 欄位分組(bin)

bins = [0, 12, 18, 25, 35, 60, 100]
cats = pd.cut(df.age, bins)
print(cats)

print(cats.cat.categories)

cc = cats.cat.categories.to_list()[1].left, cats.cat.categories.to_list()[1].right
print(cc)

df.age = pd.cut(df.age, bins, labels=range(len(bins) - 1))
cc = df.head()
print(cc)

# 移除重複資料

# 增加一筆重複資料
print(df.shape)

df.drop_duplicates()

y = df.survived
X = df.drop(["survived", "alive", "embarked", "who", "alone", "class"], axis=1)
cc = X.head()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test_std)
# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 82.42%

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_titanic_model.joblib")
joblib.dump(scaler, "tmp_titanic_scaler.joblib")

print("------------------------------------------------------------")  # 60個

# Scikit-learn 前置處理
# 遺失值(Missing value)處理

import numpy as np
from sklearn.impute import SimpleImputer

# 以平均數填補
imp = SimpleImputer(missing_values=np.nan, strategy="mean")
# 訓練
imp.fit([[1, 2], [np.nan, 3], [7, 6]])

# 轉換
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))

import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

imp = SimpleImputer(missing_values=pd.NA, strategy="median")
# 訓練並轉換，SimpleImputer 輸入必須是二維
imp.fit_transform(df.age.values.reshape(-1, 1))

# 多變數(Multivariate)

import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 訓練
imp = IterativeImputer(max_iter=10, random_state=0)
imp.fit([[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]])

# 轉換
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
print(np.round(imp.transform(X_test)))

# 必須為數值欄位
df = sns.load_dataset("titanic")
df.sex = df.sex.map({"male": 1, "female": 0})
df2 = df[["pclass", "sex", "age", "sibsp", "parch", "fare"]]

imp = IterativeImputer(max_iter=10, random_state=0)

# 訓練並轉換
df2 = imp.fit_transform(df2.values)
df_new = pd.DataFrame(df2, columns=["pclass", "sex", "age", "sibsp", "parch", "fare"])
print(df_new)

cc = df_new.isnull().sum()
print(cc)

print("------------------------------------------------------------")  # 60個

# 類別變數編碼
# 測試資料

import pandas as pd

df = pd.DataFrame(
    [
        ["green", "M", 10.1, "class1"],
        ["red", "L", 13.5, "class2"],
        ["blue", "XL", 15.3, "class1"],
    ]
)

df.columns = ["color", "size", "price", "classlabel"]
print(df)

# LabelEncoder

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
cc = encoder.fit_transform(df["size"])
print(cc)

cc = encoder.inverse_transform([1, 0, 2])
print(cc)

# Pandas Map

size_mapping = {"XL": 3, "L": 2, "M": 1}

df["size"] = df["size"].map(size_mapping)
print(df)

# OrdinalEncoder

from sklearn.preprocessing import OrdinalEncoder

data = [["Male", 1], ["Female", 3], ["Female", 2]]
encoder = OrdinalEncoder()
cc = encoder.fit_transform(data)
print(cc)

# One Hot Encoding with Pandas

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

# One-hot Encoding with Scikit-learn

from sklearn.preprocessing import OneHotEncoder

# 測試資料
X = [["Male", 1], ["Female", 3], ["Female", 2]]

# 轉換
encoder = OneHotEncoder(handle_unknown="ignore")
X_new = encoder.fit_transform(X)
cc = X_new.toarray()
print(cc)

# 類別
cc = encoder.categories_
print(cc)

# 還原
cc = encoder.inverse_transform(X_new)
print(cc)

# 指定欄位名稱
cc = encoder.get_feature_names_out(["gender", "group"])
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
encoder = OneHotEncoder(handle_unknown="ignore")
color_new = encoder.fit_transform(df[["color"]])

# 指定欄位名稱
column_names = encoder.get_feature_names_out(encoder.feature_names_in_)

# 轉換
df_new = pd.DataFrame(color_new.toarray(), columns=column_names)
print(df_new)

# 刪除原欄位 'color'
df.drop(["color"], axis=1, inplace=True)

# 合併表格
df2 = pd.concat([df, df_new], axis=1)
print(df2)

# 存檔
import joblib

joblib.dump(encoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

import pandas as pd
import yfinance as yf

# 下載每日股價

df_quote = yf.download("1101.TW", start="2020-01-01", end="2022-11-30")
df_quote.tail()

print("轉換為月頻率")

df_quote_new = df_quote.resample("ME").mean()
print(df_quote_new)

print("讀取月營收資料")

df_monthly_sales = pd.read_csv("./data/stock_monthly_sales.csv")
cc = df_monthly_sales.head()
print(cc)

print("轉換日期格式")

df_quote_new = df_quote.reset_index()
df_quote_new.Date = df_quote_new.Date
df_quote_new.Date = df_quote_new.Date.map(lambda x: str(x)[:4] + str(x)[5:7])
print(df_quote_new)

print("合併2個表格")

# 轉換日期資料型態，讓2個表格的日期資料型態一致
df_monthly_sales["年月"] = df_monthly_sales["年月"].astype("str")

# 合併2個表格
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]

# 欄位改名
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
print(df)

print("計算股價與月營收關聯度")

cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("營收公布日期晚一個月")

df_monthly_sales["單月營收"] = df_monthly_sales["單月營收"].shift(-1)
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
df.dropna(inplace=True)

cc = df[["sales", "Adj Close"]].corr()
print(cc)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# descriptive_statistics

# 鳶尾花(Iris)品種的辨識

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. 載入資料集

ds = datasets.load_iris()
"""
print("資料集說明")
print(ds.DESCR)

print("資料集欄位")
print(ds.feature_names)

print("資料集資料")
print(ds.data)

print("資料集目標名稱")
print(ds.target_names)

print("資料集目標")
print(ds.target)
"""

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(ds.data, columns=ds.feature_names)
# print(df)

# 資料集目標
y = ds.target
# print(y)
# 資料集目標名稱
# print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

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
import seaborn as sns

sns.histplot(x="sepal length (cm)", data=df)
plt.show()

# 直方圖平滑化
sns.kdeplot(x="sepal length (cm)", data=df)
plt.show()

# 右偏
import numpy as np

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(5, 1, 100)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

# 右偏
import numpy as np

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 500)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

# 關聯度

df["y"] = y
cc = df.corr()
print(cc)

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
plt.show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
import seaborn as sns

sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
plt.show()

print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

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
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
plt.show()

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_model.joblib")
joblib.dump(scaler, "tmp_scaler.joblib")

print("------------------------------------------------------------")  # 60個

import joblib

# 10.模型預測

# 載入模型與標準化轉換模型
clf = joblib.load("tmp_model.joblib")
scaler = joblib.load("tmp_scaler.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]

print("### 預測品種是：", labels[clf.predict(X_new)[0]])


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
print("------------------------------------------------------------")  # 60個


# 尋找銀行行銷活動目標客戶

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 載入資料集

df = pd.read_csv("./data/banking.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# y 各類別資料筆數統計
import seaborn as sns

sns.countplot(x="y", data=df)
plt.show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

from matplotlib import pyplot as plt

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6, 6), autopct="%1.1f%%")
plt.legend()
plt.show()

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

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop("y", axis=1).values
y = df.y.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# ((32950, 63), (8238, 63), (32950,), (8238,))

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 91.53%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# 8. 模型評估，暫不進行

# 9. 模型佈署，暫不進行



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 計程車小費資料集EDA

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import seaborn as sns
import numpy as np

# 載入資料集

df = sns.load_dataset("tips")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 對小費繪製直方圖
sns.histplot(x="tip", data=df)
plt.show()

df["log_tip"] = np.log(df["tip"])
sns.kdeplot(x="log_tip", data=df)
plt.show()

# 散佈圖
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# 三維散佈圖
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.show()

# joint plot
sns.jointplot(data=df, x="total_bill", y="tip", hue="day")
plt.show()

df.day.unique()

# ['Sun', 'Sat', 'Thur', 'Fri']
# Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']

# 觀察週間對小費的影響

sns.barplot(x="day", y="tip", data=df)
plt.show()

# 箱型圖
sns.boxplot(x="day", y="tip", data=df)
plt.show()

# 類別變數轉換為數值
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

cc = df.info()
print(cc)

# 繪製pair plot
sns.pairplot(data=df, height=1)
plt.show()

# 熱力圖
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=0.5)
plt.show()

cc = df.isna().sum()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop("tip", axis=1).values
y = df.tip.values
print(y)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# ((195, 7), (49, 7), (195,), (49,))

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

# 6. 模型訓練

lr.fit(X_train_std, y_train)

"""
LinearRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = lr.predict(X_test_std)

# 計算 r2、MSE
print(
    f"R2:{r2_score(y_test, y_pred):.2f}, MSE:{mean_squared_error(y_test, y_pred):.2f}"
)

# R2:0.91, MSE:0.26

# 8. 模型評估，暫不進行

# 9. 模型佈署，暫不進行

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Min-max scaling

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 測試資料
data = np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18]])
print(data)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
cc = scaler.fit_transform(data)
print(cc)

#驗證

# 計算最大值、最小值
max1 = np.max(data, axis=0)
min1 = np.min(data, axis=0)
print(max1, min1)

# Min-max scaling 計算
cc = (data - min1) / (max1 - min1)
print(cc)

#載入資料集

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#((455, 30), (114, 30), (455,), (114,))

#特徵縮放

scaler = MinMaxScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#98.25%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%')

#96.49%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#標準化(Standardization)

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 測試資料
data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
print(data)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cc = scaler.fit_transform(data)
print(cc)

cc = scaler.mean_
print(cc)

# 驗證

# 計算平均數、標準差
mean1 = np.mean(data, axis=0)
std1 = np.std(data, axis=0)
print(mean1, std1)

# 標準化計算
cc = (data - mean1) / std1
print(cc)
    
# 載入資料集

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

#不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%')

#92.98%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#MaxAbsScaler
#簡單測試

# 測試資料
import numpy as np
data = np.array([[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]])
print(data)

from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
cc = scaler.fit_transform(data)
print(cc)

#驗證

# 計算最大值
max1 = np.max(data, axis=0)

# MaxAbsScaler計算
cc = data / max1
print(cc)

#載入資料集

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

#3. 不須進行特徵工程

#4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#((455, 30), (114, 30), (455,), (114,))

#特徵縮放

scaler = MaxAbsScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""
#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#96.49%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

#不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#RobustScaler

# 測試資料
import numpy as np
data = np.array([[ 1., -2.,  2.],[ -2.,  1.,  3.],[ 4.,  1., -2.]])
print(data)

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
cc = scaler.fit_transform(data)
print(cc)

#驗證

import matplotlib.pyplot as plt
import pandas as pd

def get_box_plot_data(data, bp):
    rows_list = []

    for i in range(data.shape[1]):
        dict1 = {}
        dict1['label'] = i
        dict1['最小值'] = bp['whiskers'][i*2].get_ydata()[1]
        dict1['箱子下緣'] = bp['boxes'][i].get_ydata()[1]
        dict1['中位數'] = bp['medians'][i].get_ydata()[1]
        dict1['箱子上緣'] = bp['boxes'][i].get_ydata()[2]
        dict1['最大值'] = bp['whiskers'][(i*2)+1].get_ydata()[1]
        print(dict1)
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)

bp = plt.boxplot(data)
get_box_plot_data(data, bp)
print(data)
plt.show()

"""
	label 	最小值 	箱子下緣 	中位數 	箱子上緣 	最大值
0 	0 	-2.0 	-0.5 	1.0 	2.5 	4.0
1 	1 	-2.0 	-0.5 	1.0 	1.0 	1.0
2 	2 	-2.0 	0.0 	2.0 	2.5 	3.0
"""

# 計算中位數、IQR
median1 = np.median(data, axis=0)
scale1 = np.quantile(data, 0.75, axis=0) - np.quantile(data, 0.25, axis=0)
print(median1, scale1)
# 計算 RobustScaler
cc = (data - median1) / scale1
print(cc)

#載入資料集

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

#3. 不須進行特徵工程

#4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#特徵縮放

scaler = RobustScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#95.61%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

#不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%')

#94.74%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#SelectKBest 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#載入資料集

X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

#(150, 4)

#SelectKBest 特徵選取

clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

#(150, 2)

# 顯示特徵分數
cc = clf.scores_
print(cc)

# 顯示 p value
print(clf.pvalues_)

# 顯示特徵名稱
import numpy as np
ds = datasets.load_iris()
cc = np.array(ds.feature_names)[clf.scores_.argsort()[-2:][::-1]]
print(cc)

# 另一種寫法
import pandas as pd
X = pd.DataFrame(ds.data, columns=ds.feature_names)
clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
cc = clf.get_feature_names_out()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 選擇2個特徵
X = X[clf.get_feature_names_out()].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred)
                              , display_labels=ds.target_names)
disp.plot()
plt.show()

#使用全部特徵

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#(120, 4) (30, 4) (120,) (30,)
#96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectPercentile 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectPercentile, chi2

# 載入資料集

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# SelectPercentile 特徵選取

clf = SelectPercentile(chi2, percentile=10)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 71.94%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 98.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
GenericUnivariateSelect 單變數特徵選取(Univariate feature selection)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import GenericUnivariateSelect, chi2

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# GenericUnivariateSelect 特徵選取

# 使用 SelectKBest, 20 個特徵
clf = GenericUnivariateSelect(chi2, mode="k_best", param=20)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
遞迴特徵消去法(Recursive feature elimination)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# RFE 特徵選取

svc = SVC(kernel="linear", C=1)
clf = RFE(estimator=svc, n_features_to_select=2, step=1)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 特徵重要性排名
print(clf.ranking_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%


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
