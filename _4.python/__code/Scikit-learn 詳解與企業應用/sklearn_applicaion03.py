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
print("作業完成")
print("------------------------------------------------------------")  # 60個
