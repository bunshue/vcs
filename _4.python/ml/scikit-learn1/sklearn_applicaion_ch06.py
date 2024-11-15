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
print("------------------------------------------------------------")  # 60個

# 06_01_logistic_regression_validation

# 證明 Exp(log(x)) = x

import math

for i in range(1, 101):
    assert round(math.e ** math.log(i), 6) == i

# 證明 log(1/x) = - log(x)

for i in range(1, 101):
    assert round(math.log(i), 6) == -round(math.log(1 / i), 6)

cc = math.log(100), -math.log(1 / 100)
print(cc)

# 計算羅吉斯函數的上限與下限

from sympy import *
import numpy as np

x = symbols("x")
expr = 1 / (1 + np.e ** (-x))
limit(expr, x, -1000), limit(expr, x, np.inf)

# 不使用 limit

cc = 1 / (np.e**np.inf)
print(cc)

# 繪製羅吉斯函數

import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 101)
y = 1 / (1 + np.e ** (-x))
plt.plot(x, y)
plt.axhline(0, linestyle="-.", c="r")
plt.axhline(1, linestyle="-.", c="r")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_02_logistic_regression_SGD
# 以梯度下降法求解羅吉斯迴歸

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# 載入資料集

iris = datasets.load_iris()

# 只取前兩個特徵，方便繪圖
X = iris.data[:, :2]
# 只取前兩個類別
y = (iris.target != 0) * 1

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
plt.show()

# 建立羅吉斯迴歸類別


class LogisticRegression:
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


# 模型訓練

model = LogisticRegression(lr=0.1, num_iter=300000)
model.fit(X, y)

# 預測

preds = model.predict(X)
cc = (preds == y).mean()
print(cc)

print("羅吉斯迴歸係數")

print(model.theta)

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
probs = model.predict_prob(grid).reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")
plt.show()

# 以 Scikit-learn 驗證

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C=1e20)
model.fit(X, y)

preds = model.predict(X)
cc = (preds == y).mean()
print(cc)

cc = model.intercept_, model.coef_
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
probs = model.predict_proba(grid)[:, 1].reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors="black")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_03_logistic_regression_attrition

# 員工流失預測

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 載入資料集

df = pd.read_csv("./data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

cc = df.isna().sum()
print(cc)

# 觀察資料集彙總資訊
cc = df.info()
# print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 繪圖

# y 各類別資料筆數統計
import seaborn as sns

sns.countplot(x=df["Attrition"])
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = df["Attrition"].value_counts()
print(cc)

print("檢查與時間有關的特徵相關性")

import matplotlib.pyplot as plt
import numpy as np

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
plt.show()

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
plt.show()


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

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法、6. 模型訓練

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 7. 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 90.14%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model=sm.Logit(y_train,X_train)
result=model.fit()
print(result.summary())
"""

"""
8. 模型評估

9. 模型佈署

10.模型預測
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_04_logistic_regression_with_nonlinear_data

# 以二次迴歸預測世界人口數

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 載入資料集

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)

# 資料切割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# 繪製訓練及測試資料
_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
plt.show()

# 使用Scikit-Learn LinearRegression類別驗算

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)
# cc = clf.coef_, lr.intercept_
# print(cc)

# 計算準確率

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 48.80%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_05_knn_iris

# 鳶尾花(Iris)品種的辨識

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 載入資料集

ds = datasets.load_iris()

# 2. 資料清理、資料探索與分析

import pandas as pd

df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

y = ds.target
print(y)

print(ds.target_names)

# 箱型圖
import seaborn as sns

sns.boxplot(data=df)
plt.show()

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# y 各類別資料筆數統計
import seaborn as sns

sns.countplot(x=y)
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print(y_train)

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=5)

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 90.00%

# 最近鄰的距離與索引值

cc = clf.kneighbors(X_test[0:1])
print(cc)

# 設定距離為加權值

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=5, weights="distance")
clf.fit(X_train_std, y_train)

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 96.67%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.show()

"""
8. 模型評估

9. 模型佈署

10.模型預測
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_06_knn_book_recommender

# 以KNN演算法實作書籍推薦

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 載入資料集

# 書籍資料
books = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Books.csv",
    sep=";",
    on_bad_lines="skip",
    low_memory=False,
    encoding="latin-1",
)
books.columns = [
    "ISBN",
    "bookTitle",
    "bookAuthor",
    "yearOfPublication",
    "publisher",
    "imageUrlS",
    "imageUrlM",
    "imageUrlL",
]

# 讀者資料
users = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Users.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
users.columns = ["userID", "Location", "Age"]


# 評價資料
ratings = pd.read_csv(
    "C:/_git/vcs/_big_files/Scikit-learn_data/BX-Book-Ratings.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
ratings.columns = ["userID", "ISBN", "bookRating"]

# 資料探索與分析

# 評價資料筆數
print(ratings.shape)

cc = ratings.head(10)
print(cc)

# 評價筆數繪圖
import seaborn as sns

plt.rc("font", size=15)
sns.countplot(x="bookRating", data=ratings)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

print("大部份書籍都未被評價")

print("書籍資料筆數")
print(books.shape)

print("讀者資料筆數")
print(users.shape)

print("讀者年齡分析")

users.Age.hist(bins=[0, 10, 20, 30, 40, 50, 100])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("system2.png", bbox_inches="tight")
plt.show()

print("最多人評分的書籍")

rating_count = pd.DataFrame(ratings.groupby("ISBN")["bookRating"].count())
top_rating = rating_count.sort_values("bookRating", ascending=False).head()
print(top_rating)

print("最多人評分的書籍明細")

most_rated_books = pd.DataFrame(top_rating.index, index=np.arange(5), columns=["ISBN"])
most_rated_books_summary = pd.merge(most_rated_books, books, on="ISBN")
print(most_rated_books_summary)

print("書籍評價的平均得分")

average_rating = pd.DataFrame(ratings.groupby("ISBN")["bookRating"].mean())
average_rating["ratingCount"] = pd.DataFrame(
    ratings.groupby("ISBN")["bookRating"].count()
)
cc = average_rating.sort_values("ratingCount", ascending=False).head()
print(cc)


# 觀察: 最多人評分書籍的平均得分並沒有相對比較高
# 為確保統計顯著性，只保留讀者評分超過200次者，書籍評分超過100次者

counts1 = ratings["userID"].value_counts()
ratings = ratings[ratings["userID"].isin(counts1[counts1 >= 200].index)]
counts = ratings["bookRating"].value_counts()
ratings = ratings[ratings["bookRating"].isin(counts[counts >= 100].index)]

# User-Item matrix

ratings_pivot = ratings.pivot(index="userID", columns="ISBN").bookRating
userID = ratings_pivot.index
ISBN = ratings_pivot.columns
print(ratings_pivot.shape)
cc = ratings_pivot.head()
print(cc)

# 任選一本書 0316666343，計算與其他書籍的相關係數

test_book = "0316666343"
bones_ratings = ratings_pivot[test_book]
# 計算與其他書籍的相關係數
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=["pearsonR"])
corr_bones.dropna(inplace=True)

# 結合書籍評價的平均得分
corr_summary = corr_bones.join(average_rating["ratingCount"])

# 只保留評價的平均得分>=300
high_corr_book = (
    corr_summary[corr_summary["ratingCount"] >= 300]
    .sort_values("pearsonR", ascending=False)
    .head(10)
)
print(high_corr_book)

# 取得書名

# 取得書名，扣除自己，取前9名
books_corr_to_bones = pd.DataFrame(
    high_corr_book.index[1:], index=np.arange(9), columns=["ISBN"]
)
corr_books = pd.merge(books_corr_to_bones, books, on="ISBN")
print(corr_books)

# KNN

# 合併評價表及書籍基本資料
combine_book_rating = pd.merge(ratings, books, on="ISBN")
columns = [
    "yearOfPublication",
    "publisher",
    "bookAuthor",
    "imageUrlS",
    "imageUrlM",
    "imageUrlL",
]
combine_book_rating = combine_book_rating.drop(columns, axis=1)
cc = combine_book_rating.head()
print(cc)

# 去除未評價書籍
combine_book_rating = combine_book_rating.dropna(axis=0, subset=["bookTitle"])
# 統計書籍的評價次數
book_ratingCount = (
    combine_book_rating.groupby(by=["bookTitle"])["bookRating"]
    .count()
    .reset_index()
    .rename(columns={"bookRating": "totalRatingCount"})[
        ["bookTitle", "totalRatingCount"]
    ]
)
cc = book_ratingCount.head()
print(cc)

# 合併評價次數及書籍基本資料
rating_with_totalRatingCount = combine_book_rating.merge(
    book_ratingCount, left_on="bookTitle", right_on="bookTitle", how="left"
)
cc = rating_with_totalRatingCount.head()
print(cc)

# 顯示評價次數的統計量
pd.set_option("display.float_format", lambda x: "%.3f" % x)
print(book_ratingCount["totalRatingCount"].describe())

# 顯示百分位數
print(book_ratingCount["totalRatingCount"].quantile(np.arange(0.9, 1, 0.01)))

# 熱門書籍：只有1%的書籍有超過50次的評分

# 篩選有超過50次評分的書籍
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query(
    "totalRatingCount >= @popularity_threshold"
)
cc = rating_popular_book.head()
print(cc)

# 合併熱門書籍及讀者基本資料，使用美國及加拿大資料

# 合併熱門書籍及讀者基本資料
combined = rating_popular_book.merge(
    users, left_on="userID", right_on="userID", how="left"
)

# 只考慮美國及加拿大讀者
us_canada_user_rating = combined[combined["Location"].str.contains("usa|canada")]
us_canada_user_rating = us_canada_user_rating.drop("Age", axis=1)
cc = us_canada_user_rating.head()
print(cc)

print(us_canada_user_rating.shape)

# KNN模型訓練

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# 去除重複值
us_canada_user_rating = us_canada_user_rating.drop_duplicates(["userID", "bookTitle"])
# 產生商品與讀者的樞紐分析表，會有很多 null value，均以0替代
us_canada_user_rating_pivot = us_canada_user_rating.pivot(
    index="bookTitle", columns="userID", values="bookRating"
).fillna(0)
# csr_matrix：壓縮稀疏矩陣，加速矩陣計算
us_canada_user_rating_matrix = csr_matrix(us_canada_user_rating_pivot.values)

# 找出相似商品，X為每一個讀者的評分
model_knn = NearestNeighbors(metric="cosine", algorithm="brute")
model_knn.fit(us_canada_user_rating_matrix)

# 測試

# 隨機抽取一件商品作預測
query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(
    np.array(us_canada_user_rating_pivot.iloc[query_index, :]).reshape(1, -1),
    n_neighbors=6,
)

# 顯示最相似的前5名商品，並顯示距離(相似性)
for i in range(0, len(distances.flatten())):
    if i == 0:  # 第一筆是自己
        print(f"{us_canada_user_rating_pivot.index[query_index]} 的推薦:")
    else:
        print(
            f"{i}: {us_canada_user_rating_pivot.index[indices.flatten()[i]]}"
            + f", 距離: {distances.flatten()[i]:.2f}:"
        )

# SVD 矩陣分解(Matrix Factorization)

# User-Item Matrix
us_canada_user_rating_pivot2 = us_canada_user_rating.pivot(
    index="userID", columns="bookTitle", values="bookRating"
).fillna(0)
cc = us_canada_user_rating_pivot2.head()
print(cc)

cc = us_canada_user_rating_pivot2.shape
print(cc)

X = us_canada_user_rating_pivot2.values.T
print(X.shape)

# TruncatedSVD 降維至 12 個

# 萃取 12 個特徵
import sklearn
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)
print(matrix.shape)

# 依據 12 個特徵計算相關係數
corr = np.corrcoef(matrix)
print(corr.shape)

# 測試

# 取得 "The Green Mile" 書籍索引值
us_canada_book_list = list(us_canada_user_rating_pivot2.columns)
coffey_hands = us_canada_book_list.index("The Green Mile")
print("The Green Mile 書籍索引值:", coffey_hands)

# 依照索引值找出與其他書的相關係數
corr_coffey_hands = corr[coffey_hands]
print(corr_coffey_hands)

# 列出相關係數 > 80% 的書籍
us_canada_book_title = us_canada_user_rating_pivot2.columns
cc = list(us_canada_book_title[(corr_coffey_hands >= 0.8)])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_07_surprise_test

# Surprise 測試

from surprise import SVD, KNNBasic
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split

# 載入資料集

# 載入內建 movielens-100k 資料集
data = Dataset.load_builtin("ml-100k")
print("user id\titem id\trating\ttimestamp")
cc = data.raw_ratings[:10]
print(cc)

# 資料分割

# 切分為訓練及測試資料，測試資料佔 25%
trainset, testset = train_test_split(data, test_size=0.25)

# 模型訓練

# 使用 KNN 演算法
model = KNNBasic()

# 訓練
model.fit(trainset)

# 模型評分

# 測試
predictions = model.test(testset)

# 計算 RMSE
accuracy.rmse(predictions)

# RMSE: 0.9874

# SVD

model = SVD()
model.fit(trainset)
predictions = model.test(testset)
accuracy.rmse(predictions)

# RMSE: 0.9405

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_08_knn_from_scratch_iris

# 自行開發KNN

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

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


# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

scaler = StandardScaler()
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

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

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


# 載入資料集

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

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 載入資料集

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

# 06_11_naive_bayes_spam

# 垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re

# 讀取資料集

mails = pd.read_csv("./data/spam.csv", encoding="latin-1")
cc = mails.head()
print(cc)

# 資料整理

mails.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
cc = mails.head()
print(cc)

mails.rename(columns={"v1": "label", "v2": "message"}, inplace=True)
cc = mails.head()
print(cc)

cc = mails["label"].value_counts()
print(cc)

mails["label"] = mails["label"].map({"ham": 0, "spam": 1})
cc = mails.head()
print(cc)

# 設定停用詞
import string

stopword_list = set(stopwords.words("english") + list(string.punctuation))
# 詞形還原(Lemmatization)
lem = WordNetLemmatizer()


# 前置處理(Preprocessing)
def preprocess(text, is_lower_case=True):
    if is_lower_case:
        text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens if len(token) > 1 and token != "..."]
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_tokens = [lem.lemmatize(token) for token in filtered_tokens]
    filtered_text = " ".join(filtered_tokens)
    return filtered_text


mails["message"] = mails["message"].map(preprocess)
cc = mails.head()
print(cc)

# 文字雲

# 凸顯垃圾信的常用單字
spam_words = " ".join(list(mails[mails["label"] == 1]["message"]))
spam_wc = WordCloud(width=512, height=512).generate(spam_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(spam_wc)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8114)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no = 0
for i in tfidf_matrix.toarray()[0]:
    if i > 0.0:
        no += 1
print(no)

# 資料分割

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)
# 模型訓練

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
cc = accuracy_score(y_pred, y_test)
print(cc)
# 0.895067264573991

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, y_pred))

cc = confusion_matrix(y_test, y_pred)
print(cc)

# 測試

message_processed_list = (
    "I cant pick the phone right now. Pls send a message",
    "Congratulations ur awarded $500",
    "Thanks for your subscription to Ringtone UK your mobile will be charged",
    "Oops, I'll let you know when my roommate's done",
    "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, 憯1.50 to rcv",
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
)
X_new = tfidf_vectorizer.transform(message_processed_list)
cc = clf.predict(X_new.toarray())
print(cc)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_01_svm_from_scratch
# 自行開發支援向量機分類器，並進行鳶尾花(Iris)品種的辨識

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# SVM 演算法


class SVM:
    def __init__(self, learning_rate=1e-3, lambda_param=1e-2, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    # 初始化權重、偏差
    def _init_weights_bias(self, X):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0

    # 類別代碼：-1, 1
    def _get_cls_map(self, y):
        return np.where(y <= 0, -1, 1)

    # 限制條件：y(wx + b) >= 1
    def _satisfy_constraint(self, x, idx):
        linear_model = np.dot(x, self.w) + self.b
        return self.cls_map[idx] * linear_model >= 1

    # 反向傳導
    def _get_gradients(self, constrain, x, idx):
        if constrain:
            dw = self.lambda_param * self.w
            db = 0
            return dw, db

        dw = self.lambda_param * self.w - np.dot(self.cls_map[idx], x)
        db = -self.cls_map[idx]
        return dw, db

    # 更新權重、偏差
    def _update_weights_bias(self, dw, db):
        self.w -= self.lr * dw
        self.b -= self.lr * db

    # 訓練
    def fit(self, X, y):
        self._init_weights_bias(X)
        self.cls_map = self._get_cls_map(y)

        for _ in range(self.n_iters):
            for idx, x in enumerate(X):
                constrain = self._satisfy_constraint(x, idx)
                dw, db = self._get_gradients(constrain, x, idx)
                self._update_weights_bias(dw, db)

    # 預測
    def predict(self, X):
        estimate = np.dot(X, self.w) + self.b
        prediction = np.sign(estimate)
        return np.where(prediction == -1, 0, 1)


# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 選擇演算法

clf = SVM(learning_rate=1e-2, lambda_param=1e-3, n_iters=5000)

# 模型訓練

clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 73.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以Scikit-learn SVM進行鳶尾花(Iris)品種的辨識

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.svm import SVC

clf = SVC(probability=True)
clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

cc = clf.support_vectors_
print(cc)

cc = clf.support_
print(cc)

cc = clf.predict_proba(X_test)
print(cc)

cc = clf.predict_log_proba(X_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
SVM優點：

    切出來的線很漂亮，擁有最大margin的特性
    可以很容易透過更換Kernel，做出非線性的線（非線性的決策邊界）

SVM缺點：

    效能較不佳，由於時間複雜度為O(n²)當有超過一萬筆資料時，運算速度會慢上許多

"""

from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 載入Iris資料集
iris = datasets.load_iris()

x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
print("target_names: " + str(iris["target_names"]))
y = pd.DataFrame(iris["target"], columns=["target"])
iris_data = pd.concat([x, y], axis=1)
iris_data = iris_data[["sepal length (cm)", "petal length (cm)", "target"]]
iris_data = iris_data[iris_data["target"].isin([0, 1])]
cc = iris_data.head(3)
print(cc)

# 將資料分為Train以及Test並將特徵標準化

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    iris_data[["sepal length (cm)", "petal length (cm)"]],
    iris_data[["target"]],
    test_size=0.3,
    random_state=0,
)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 載入SVM中的SVC，並將kernel設為線性（SVM的Kernel可以換成非線性），並將Probability設為True

from sklearn.svm import SVC

svm = SVC(kernel="linear", probability=True)

svm.fit(X_train_std, y_train["target"].values)

""" Out
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=True, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

SVC是SVM用C++語言實作的版本，背後是libsvm

"""

cc = svm.predict(X_test_std)
print(cc)

cc = y_test["target"].values
print(cc)

error = 0
for i, v in enumerate(svm.predict(X_test_std)):
    if v != y_test["target"].values[i]:
        error += 1
print(error)

cc = svm.predict_proba(X_test_std)
print(cc)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            c=cmap(idx),
            edgecolor="black",
            marker=markers[idx],
            label=cl,
        )

    # highlight test samples
    if test_idx:
        # plot all samples
        if not versiontuple(np.__version__) >= versiontuple("1.9.0"):
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            warnings.warn("Please update to NumPy 1.9.0 or newer")
        else:
            X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c="",
            alpha=1.0,
            edgecolor="black",
            linewidths=1,
            marker="o",
            s=55,
            label="test set",
        )


plot_decision_regions(X_train_std, y_train["target"].values, classifier=svm)
plt.xlabel("sepal length [standardized]")
plt.ylabel("petal width [standardized]")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_03_svm _sample_weight

# 不平衡的資料集利用sample_weight矯正

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 生成隨機資料

np.random.seed(0)
# 20筆資料，前10筆+1
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
# y 前10筆為1，後10筆為-1
y = [1] * 10 + [-1] * 10
print(X)
print(y)

# 指定不同權重

# 初始權重為隨機亂數
modified_weight = abs(np.random.randn(len(X)))

# 後5筆權重乘以 5
modified_weight[15:] *= 5
# 第10筆權重乘以 15
modified_weight[9] *= 15
print(modified_weight)

# 無加權的模型訓練

clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

"""
SVC(gamma=1)
"""

# 加權的模型訓練

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=modified_weight)

"""
SVC(gamma=1)
"""

# 決策邊界函數


def plot_decision_function(classifier, sample_weight, axis, title):
    # plot the decision function
    xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))

    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plot the line, the points, and the nearest vectors to the plane
    axis.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
    axis.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        s=100 * sample_weight,
        alpha=0.9,
        cmap=plt.cm.bone,
        edgecolors="black",
    )

    axis.axis("off")
    axis.set_title(title)


# 繪圖比較兩個模型

# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 權重全部為 1
constant_weight = np.ones(len(X))
plot_decision_function(clf_no_weights, constant_weight, axes[0], "無加權的模型")

# 權重全部為 1
plot_decision_function(clf_weights, modified_weight, axes[1], "加權的模型")
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_04_svm_kernels

# 非線性分割SVM測試

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 生成隨機資料

# 16筆資料，分兩類
X = np.c_[
    (0.4, -0.7),
    (-1.5, -1),
    (-1.4, -0.9),
    (-1.3, -1.2),
    (-1.1, -0.2),
    (-1.2, -0.4),
    (-0.5, 1.2),
    (-1.5, 2.1),
    (1, 1),
    (1.3, 0.8),
    (1.2, 0.5),
    (0.2, -2),
    (0.5, -2.4),
    (0.2, -2.3),
    (0, -2.7),
    (1.3, 2.1),
].T
Y = [0] * 8 + [1] * 8

print(X)
print(Y)

# 繪圖比較三種 kernels 模型

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
for fignum, kernel in enumerate(["linear", "poly", "rbf"]):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)

    plt.subplot(1, 3, fignum + 1)
    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="r",
    )
    colors = np.array(["yellow", "lightgreen"])
    plt.scatter(X[:, 0], X[:, 1], c=colors[Y], zorder=10, cmap=plt.cm.Paired)

    x_min, x_max, y_min, y_max = -3, 3, -3, 3
    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_05_svr_kernels

# 房價預測

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 載入 Boston 房價資料集

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 觀察資料集彙總資訊
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 繪圖

# 直方圖
import seaborn as sns

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
plt.show()

# 3. 不須進行特徵工程

# 4. 資料分割

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

from sklearn.svm import SVR

model = SVR(kernel="linear")

# 6. 模型訓練

model.fit(X_train_std, y_train)

"""
SVR(kernel='linear')
"""

# 7. 模型評分

# R2、MSE、MAE
y_pred = model.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

"""
R2 = 69.56
MSE = 19.12608965301932
MAE = 3.198509245210469
"""

# 取得偏差項及權重
cc = model.intercept_, model.coef_
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition

# SVM人臉辨識

from time import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.decomposition import PCA

# 載入資料集

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print(f"n_samples: {n_samples}")
print(f"n_features: {n_features}")
print(f"n_classes: {n_classes}")

"""
Total dataset size:
n_samples: 1288
n_features: 1850
n_classes: 7
"""

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 使用 PCA 萃取 150 個特徵

n_components = 150

t0 = time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print(f"轉換耗時: {(time() - t0):.3f}s")

# 轉換耗時: 0.183s

# 模型訓練

from sklearn.svm import SVC

clf = SVC(kernel="rbf", class_weight="balanced")
clf.fit(X_train_pca, y_train)

"""
SVC(class_weight='balanced')
"""

# 模型評分

# 計算準確率
from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 分類報告

y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))

# 混淆矩陣圖

ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation=30
)
plt.show()

# 結合圖像與預測結果驗證


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    return f"predicted: {pred_name}\ntrue:         {true_name}"


prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w, n_row=6, n_col=4)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition_org

# Faces recognition example using eigenfaces and SVMs

# The dataset used in this example is a preprocessed excerpt of the "Labeled Faces in the Wild", aka LFW_:

# http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

from time import time
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from scipy.stats import loguniform

# Download the data, if not already on disk and load it as numpy arrays

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

# Split into a training set and a test and keep 25% of the data for testing.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled dataset): unsupervised feature extraction / dimensionality reduction

n_components = 150

print(
    "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
)
t0 = time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))

# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}
clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)

# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
plt.tight_layout()
plt.show()

# Predicting people's names on the test set

# Qualitative evaluation of the predictions using matplotlib


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


# plot the result of the prediction on a portion of the test set


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    return "predicted: %s\ntrue:      %s" % (pred_name, true_name)


prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_07_decision_tree_from_scratch

# 自行開發決策樹

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 計算熵(entropy)


# 熵公式
def entropy_func(c, n):
    return -(c * 1.0 / n) * math.log(c * 1.0 / n, 2)
    # gini
    # return 1-(c*1.0/n)**2


"""
# 熵公式
def entropy_func(c, n):
    # return -(c*1.0/n)*math.log(c*1.0/n, 2)
    # gini
    return 1 - (c * 1.0 / n) ** 2
"""


# 依特徵值切割成兩類，分別計算熵，再加總
# 計算同一節點內的熵，只有兩個類別
def entropy_cal(c1, c2):
    if c1 == 0 or c2 == 0:
        return 0
    return entropy_func(c1, c1 + c2) + entropy_func(c2, c1 + c2)


# 視每個特徵都是類別變數，依每個類別切割，分別計算熵
# 計算同一節點內的熵，多個類別
def entropy_of_one_division(division):
    s = 0
    n = len(division)
    classes = set(division)
    # 計算每一類別的熵，再加總
    for c in classes:
        n_c = sum(division == c)
        e = n_c * 1.0 / n * entropy_cal(sum(division == c), sum(division != c))
        s += e
    return s, n


# 依分割條件計算熵
def get_entropy(y_predict, y_real):
    if len(y_predict) != len(y_real):
        print("They have to be the same length")
        return None
    n = len(y_real)
    # 左節點
    s_true, n_true = entropy_of_one_division(y_real[y_predict])
    # 右節點
    s_false, n_false = entropy_of_one_division(y_real[~y_predict])
    # 左、右節點加權總和
    s = n_true * 1.0 / n * s_true + n_false * 1.0 / n * s_false
    return s


# 決策樹演算法類別


class DecisionTreeClassifier(object):
    def __init__(self, max_depth=3):
        self.depth = 0
        self.max_depth = max_depth

    # 訓練
    def fit(self, x, y, par_node={}, depth=0):
        if par_node is None:
            return None
        elif len(y) == 0:
            return None
        elif self.all_same(y):
            return {"val": float(y[0])}
        elif depth >= self.max_depth:
            return None
        else:
            # 計算資訊增益
            col, cutoff, entropy = self.find_best_split_of_all(x, y)
            if cutoff is not None:
                y_left = y[x[:, col] < cutoff]
                y_right = y[x[:, col] >= cutoff]
                par_node = {
                    "col": feature_names[col],
                    "index_col": int(col),
                    "cutoff": float(cutoff),
                    "val": float(np.round(np.mean(y))),
                }
                par_node["left"] = self.fit(
                    x[x[:, col] < cutoff], y_left, {}, depth + 1
                )
                par_node["right"] = self.fit(
                    x[x[:, col] >= cutoff], y_right, {}, depth + 1
                )
                self.depth += 1
            self.trees = par_node
            return par_node

    # 比較所有特徵找到最佳切割條件
    def find_best_split_of_all(self, x, y):
        col = None
        min_entropy = 1
        cutoff = None
        for i, c in enumerate(x.T):
            entropy, cur_cutoff = self.find_best_split(c, y)
            if entropy == 0:  # 找到最佳切割條件
                return i, cur_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                col = i
                cutoff = cur_cutoff
        return col, cutoff, min_entropy

    # 根據一個特徵找到最佳切割條件
    def find_best_split(self, col, y):
        min_entropy = 10
        n = len(y)
        for value in set(col):
            y_predict = col < value
            my_entropy = get_entropy(y_predict, y)
            if my_entropy <= min_entropy:
                min_entropy = my_entropy
                cutoff = value
        return min_entropy, cutoff

    # 檢查是否節點中所有樣本均屬同一類
    def all_same(self, items):
        return all(x == items[0] for x in items)

    # 預測
    def predict(self, x):
        tree = self.trees
        results = np.array([0] * len(x))
        for i, c in enumerate(x):
            try:
                results[i] = self._get_prediction(c)
            except:
                pass
        return results

    # 預測一筆
    def _get_prediction(self, row):
        cur_layer = self.trees
        while cur_layer is not None and cur_layer.get("cutoff"):
            if row[cur_layer["index_col"]] < cur_layer["cutoff"]:
                cur_layer = cur_layer["left"]
            else:
                cur_layer = cur_layer["right"]
        else:
            return cur_layer.get("val") if cur_layer is not None else None


# 載入資料集

# ds = datasets.load_iris()

ds = datasets.load_wine()

feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 選擇演算法

# 模型訓練

import json

clf = DecisionTreeClassifier()
output = clf.fit(X_train, y_train)
# output
print(json.dumps(output, indent=4))

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 30.56%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_08_scikit-learn_decision_tree

# Scikit-learn決策樹演算法

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 載入資料集

ds = datasets.load_wine()
feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()  # criterion='entropy')
clf.fit(X_train, y_train)

# DecisionTreeClassifier()

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 繪製樹狀圖

import matplotlib.pyplot as plt

from sklearn.tree import plot_tree

plt.figure(figsize=(14, 10))
plot_tree(clf, feature_names=feature_names)
plt.show()


# 使用 graphviz 繪製圖形
"""
安裝
    安裝 graphviz (https://graphviz.org/download/)
    將安裝路徑的bin加入環境變數Path中(C:\Program Files (x86)\Graphviz2.XX\bin)
    pip install graphviz pydotplus
"""
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=ds.target_names,
    feature_names=ds.feature_names,
    out_file=None,
)
graph = graph_from_dot_data(dot_data)
# graph.write_png('tmp_wine_tree.png')  NG

# dot 格式存檔

dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=ds.target_names,
    feature_names=ds.feature_names,
    out_file="tmp_wine_tree.dot",
)

# 取得樹狀圖的相關資訊

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, -1)]  # seed is the root node id and its parent depth
while len(stack) > 0:
    node_id, parent_depth = stack.pop()
    node_depth[node_id] = parent_depth + 1

    # If we have a test node
    if children_left[node_id] != children_right[node_id]:
        stack.append((children_left[node_id], parent_depth + 1))
        stack.append((children_right[node_id], parent_depth + 1))
    else:
        is_leaves[node_id] = True

print(f"樹狀圖共有{n_nodes}個節點:")
for i in range(n_nodes):
    depth = node_depth[i] * "\t"
    if is_leaves[i]:
        print(f"{depth}node={i} leaf node.")
    else:
        print(
            f"{depth}node={i} child node: go to node {children_left[i]} if X[:, "
            + f"{feature[i]}] <= {threshold[i]} else to node {children_right[i]}."
        )
print()

node_indicator = clf.decision_path(X)
leave_id = clf.apply(X)
sample_id = 0
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print(f"Rules used to predict sample {sample_id}: ")
for node_id in node_index:
    if leave_id[sample_id] == node_id:
        continue

    if X[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "decision id node {} : (X[{}, {}] (= {}) {} {})".format(
            node_id,
            sample_id,
            feature[node_id],
            X[sample_id, feature[node_id]],
            threshold_sign,
            threshold[node_id],
        )
    )

# For a group of samples, we have the following common node.
sample_ids = [0, 1]
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)

common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nThe following samples %s share the node %s in the tree"
    % (sample_ids, common_node_id)
)
print("It is %s %% of all nodes." % (100 * len(common_node_id) / n_nodes,))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_09_scikit-learn_decision_tree_regression

# Scikit-learn迴歸樹測試

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# 生成隨機資料

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# 訓練兩個模型

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_1.fit(X, y)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_2.fit(X, y)

# DecisionTreeRegressor(max_depth=5)

# 預測

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# 模型繪圖

plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_10_decision_tree_regression_boston

# 房價預測

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 載入 Boston 房價資料集

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 繪圖

# 直方圖
import seaborn as sns

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
plt.show()

# 3. 不須進行特徵工程

# 4. 資料分割

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

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()

# 6. 模型訓練

model.fit(X_train_std, y_train)

# DecisionTreeRegressor()

# 7. 模型評分

# R2、MSE、MAE
y_pred = model.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_11_decision_tree_multioutput_face_completion

# 使用Scikit-learn各種迴歸演算法預測人臉下半部

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

# 載入資料集

data, targets = fetch_olivetti_faces(return_X_y=True)

# 資料分割

train = data[targets < 30]
test = data[targets >= 30]

# 模型訓練

n_pixels = data.shape[1]
# 人臉上半部為 X，人臉下半部為 Y
X_train = train[:, : (n_pixels + 1) // 2]
y_train = train[:, n_pixels // 2 :]

# 使用各種迴歸演算法
ESTIMATORS = {
    "迴歸樹": DecisionTreeRegressor(),
    "KNN": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

# 訓練
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)

# 測試 5 筆資料

n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]

# 預測
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    y_test_predict[name] = estimator.predict(X_test)

# 依照各種迴歸演算法測試結果繪製人臉

# 設定圖片寬/高
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("預測人臉下半部", size=16)

# 繪圖
for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i > 0:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1, title="true faces")

    sub.axis("off")
    sub.imshow(
        true_face.reshape(image_shape), cmap=plt.cm.gray, interpolation="nearest"
    )

    # 依照各種迴歸演算法繪製人臉
    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j, title=est)

        sub.axis("off")
        sub.imshow(
            completed_face.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation="nearest",
        )
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_12_scikit-learn_random_forest
# Scikit-learn決策樹演算法

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 載入資料集

ds = datasets.load_wine()
feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)

# RandomForestClassifier(n_estimators=50)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 97.22%

# 特徵重要性

cc = clf.feature_importances_
print(cc)

print(feature_names)

# 繪圖

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.figure(figsize=(10, 6))
df = pd.DataFrame(
    {"feature_names": feature_names, "feature_importance": clf.feature_importances_}
)
df.sort_values(by=["feature_importance"], ascending=False, inplace=True)
sns.barplot(x=df["feature_importance"], y=df["feature_names"])
plt.show()

# 使用Permutation importance評估特徵重要性

from sklearn.inspection import permutation_importance

result = permutation_importance(
    clf, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)

sorted_importances_idx = result.importances_mean.argsort()
importances = pd.DataFrame(
    result.importances[sorted_importances_idx].T,
    columns=np.array(feature_names)[sorted_importances_idx],
)

ax = importances.plot.box(vert=False, whis=10, figsize=(10, 6))
ax.set_title("Permutation Importances (test set)")
ax.axvline(x=0, color="k", linestyle="--")
ax.set_xlabel("Decrease in accuracy score")
ax.figure.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_13_chaid_three_cat

from seaborn import load_dataset

df = load_dataset("titanic")
cc = df.head()
print(cc)

df.embarked = df.embarked.fillna(method="ffill")
cc = df.head()
print(cc)

from CHAID import Tree

independent_variable_columns = ["sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

from CHAID import Tree

independent_variable_columns = ["fare", "sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["ordinal"] + ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
