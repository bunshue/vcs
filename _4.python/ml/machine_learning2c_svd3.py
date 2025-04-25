"""
machine_learning2c_svd3

SVD

Stochastic_grad_descent

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

# from common1 import *
import pickle
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from sklearn.decomposition import TruncatedSVD

data = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]
n_components = 2  # 潛在変數の數

model = TruncatedSVD(n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data))  # 変換したデータ
print(model.explained_variance_ratio_)  # 寄與率
print(sum(model.explained_variance_ratio_))  # 累積寄與率

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# knn_book_recommender

# 以KNN演算法實作書籍推薦

# 書籍資料
books = pd.read_csv(
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Books.csv",
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
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Users.csv",
    sep=";",
    on_bad_lines="skip",
    encoding="latin-1",
)
users.columns = ["userID", "Location", "Age"]


# 評價資料
ratings = pd.read_csv(
    "D:/_git/vcs/_big_files/Scikit-learn_data/BX-Book-Ratings.csv",
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
plt.rc("font", size=15)
sns.countplot(x="bookRating", data=ratings)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

show()

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
# 存圖 plt.savefig("tmp_system2.png", bbox_inches="tight")

show()

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
pd.set_option("display.float_format", lambda x: "%0.3f" % x)
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
model_knn.fit(us_canada_user_rating_matrix)  # 學習訓練.fit

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
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)
print(matrix.shape)

# 依據 12 個特徵計算 相關係數
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

# Surprise 測試

from surprise import SVD
from surprise import KNNBasic
from surprise import Dataset
from surprise import accuracy

# 載入內建 movielens-100k 資料集
data = Dataset.load_builtin("ml-100k")
print("user id\titem id\trating\ttimestamp")
cc = data.raw_ratings[:10]
print(cc)

# 資料分割, 使用特殊的資料分割函數
from surprise.model_selection import train_test_split

# 切分為訓練及測試資料，測試資料佔 20%
trainset, testset = train_test_split(data, test_size=0.2)

# 恢復原本的函數
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# 模型訓練

# 使用 KNN 演算法
model = KNNBasic()

# 訓練
model.fit(trainset)  # 學習訓練.fit

# 模型評分

# 測試
predictions = model.test(testset)

# 計算 RMSE
accuracy.rmse(predictions)

# RMSE: 0.9874

# SVD

model = SVD()

model.fit(trainset)  # 學習訓練.fit

predictions = model.test(testset)

accuracy.rmse(predictions)

# RMSE: 0.9405

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
Python如何分解SVD(奇異值分解)

在这个示例中，我们首先创建了一个矩阵 ( A )，然後使用numpy.linalg.svd函数对其进行SVD分解。
函数返回三个矩阵：( U )、( Sigma ) 和 ( V^T )。
需要注意的是，numpy.linalg.svd返回的 ( Sigma ) 是一个向量，而不是一个对角矩阵。

#一、使用NumPy库的linalg.svd函数
#二、使用Scipy库的linalg.svd函数
"""

A = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 4, 0, 0, 0]])
print("A矩陣 :")
print(A)
print(A.shape)

# 使用NumPy进行SVD分解
U, Sigma, VT = np.linalg.svd(A)

# 使用Scipy进行SVD分解
U, Sigma, VT = scipy.linalg.svd(A)

print("U矩阵 :")
print(U)
print(U.shape)

print("Sigma对角矩阵 :")
print(Sigma)
print(Sigma.shape)

print("VT矩阵 :")
print(VT)
print(VT.shape)

"""
#五、SVD分解的应用
5.1 数据降维
SVD在数据降维中有广泛的应用。
通过SVD分解，我们可以将高维数据映射到低维空间，从而减少计算复杂度和存储空间。
以下是一个使用SVD进行数据降维的示例：
"""
from sklearn.decomposition import TruncatedSVD

X = np.random.rand(100, 50)

# 使用TruncatedSVD进行数据降维
svd = TruncatedSVD(n_components=10)

X_reduced = svd.fit_transform(X)

print("原始数据形状：", X.shape)
print("降维後数据形状：", X_reduced.shape)

"""
5.2 图像压缩
SVD在图像压缩中也有重要应用。
通过SVD分解，我们可以将图像数据表示为低秩矩阵，从而减少存储空间和传输带宽。
以下是一个使用SVD进行图像压缩的示例：
"""

from skimage import io

# 读取图像
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = "data/circle.bmp"
image = io.imread(filename, as_gray=True)

# 使用NumPy进行SVD分解
U, Sigma, VT = np.linalg.svd(image)

# 选择前k个奇异值进行图像压缩
k = 50

compressed_image = np.dot(U[:, :k], np.dot(np.diag(Sigma[:k]), VT[:k, :]))

# 显示原图和压缩後的图像
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Compressed Image")
plt.imshow(compressed_image, cmap="gray")

show()

# 在这个示例中，我们首先读取了一张灰度图像，
# 然後使用NumPy的numpy.linalg.svd函数对其进行SVD分解。
# 通过选择前 ( k ) 个奇异值，我们可以重构出压缩後的图像。

"""
1. 什么是SVD分解？
SVD分解是奇异值分解（Singular Value Decomposition）的缩写，
是一种矩阵分解的方法。它将一个矩阵分解为三个矩阵的乘积，
分别是左奇异矩阵、奇异值矩阵和右奇异矩阵。

2. 如何在Python中进行SVD分解？
在Python中，可以使用NumPy库来进行SVD分解。首先，需要导入NumPy库，
然後使用numpy.linalg.svd()函数进行分解。
例如，如果有一个矩阵A，可以使用以下代码进行SVD分解：
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, V = np.linalg.svd(A)

3. SVD分解有什么应用场景？
SVD分解在数据分析和机器学习中有广泛的应用。
它可以用于降维，帮助去除数据中的噪声和冗余信息，从而提取出数据的主要特征。
此外，SVD分解还可以用于图像压缩、推荐系统、文本挖掘等领域。
通过SVD分解，我们可以对复杂的数据进行简化和分析，从而得到更有用的信息。
"""
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Classification using Stochastic Gradient Descent

# Stochastic gradient descent (SGD)

from sklearn.datasets import make_classification
from time import time
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Train using various classifiers with increasing training set size

# SGDClassifier: Using hinge loss (support vector machine loss)

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
hinge_acc = []
hinge_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    hinge_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    hinge_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# SGDClassifier: Using log loss (logistic regression)

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
log_acc = []
log_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    log_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    log_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# SGDClassifier: Using perceptron loss/algorithm

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
perceptron_acc = []
perceptron_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    perceptron_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    perceptron_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# Random Forest classifier

rf = RandomForestClassifier(
    n_estimators=20, max_depth=5, min_samples_leaf=5, min_samples_split=10, n_jobs=-1
)
rf_acc = []
rf_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    rf.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    rf_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, rf.predict(X_test))
    rf_acc.append(acc)
    print("Accuracy:", round(acc, 3))
    print()

# Plot


def plot_var(var, var_name):
    size = np.array([int(10 ** (0.2 * i)) for i in range(15, 31)])
    plt.figure(figsize=(8, 5))
    plt.title(f"{var_name} with training set size", fontsize=18)
    plt.semilogx(size * 0.7, var, marker="o", color="k", lw=3, markersize=12)
    plt.grid(True)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Training set size", fontsize=15)
    plt.ylabel("Training time (milliseconds)", fontsize=15)
    # show()


plot_var(hinge_time, "Hinge loss time")
plot_var(log_time, "Logistic loss time")
plot_var(perceptron_time, "Perceptron algorithm time")
plot_var(rf_time, "Random Forest time")
show()

plot_var(hinge_acc, "Hinge loss accuracy")
plot_var(log_acc, "Logistic loss accuracy")
plot_var(perceptron_acc, "Perceptron algorithm accuracy")
plot_var(rf_acc, "Random Forest accuracy")
show()

# Observation
# While achieving similar accuracy level, the SGDClassifier estimator variants demonstrate faster training time as compared to the Random Forest classifier. The difference is not that significant at the low end of the training set size (< 100,000). But the difference becomes prominent for larger training set size.

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 60個
