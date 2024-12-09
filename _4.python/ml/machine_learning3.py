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
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度
from sklearn.metrics import accuracy_score


def show():
    return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個


# 迴歸效果評估
def evaluate_result(y_test, y_pred):
    print("真實資料(y_test) :", y_test)
    print("預測資料(y_pred) :", y_pred)

    print("計算 真實測試資料(y_test) 和 預測資料(y_pred)的 MSE")
    mse = np.sum((y_test - y_pred) ** 2) / len(y_test)
    print("MSE =", mse)

    # 平均絕對誤差 Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
    cc = mean_absolute_error(y_test, y_pred)
    print("MAE : Mean Absolute Error :", cc)

    # 均方誤差 Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
    mse = mean_squared_error(y_test, y_pred)
    print("MSE : Mean Squared Error :", mse)

    # Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
    cc = np.sqrt(mean_squared_error(y_test, y_pred))
    print("RMS : Root Mean Squared Error :", cc)

    print("計算 真實測試資料(y_test) 和 預測資料(y_pred) 的 決定係數r2 r2_score")
    r2 = r2_score(y_test, y_pred)
    print(f"決定係數R2 = {r2:.4f}")


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

joblib.dump(encoder, "tmp_color.joblib")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

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

# RobustScaler

# 測試資料

data = np.array([[1.0, -2.0, 2.0], [-2.0, 1.0, 3.0], [4.0, 1.0, -2.0]])
print(data)

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
cc = scaler.fit_transform(data)
print(cc)

# 驗證


def get_box_plot_data(data, bp):
    rows_list = []

    for i in range(data.shape[1]):
        dict1 = {}
        dict1["label"] = i
        dict1["最小值"] = bp["whiskers"][i * 2].get_ydata()[1]
        dict1["箱子下緣"] = bp["boxes"][i].get_ydata()[1]
        dict1["中位數"] = bp["medians"][i].get_ydata()[1]
        dict1["箱子上緣"] = bp["boxes"][i].get_ydata()[2]
        dict1["最大值"] = bp["whiskers"][(i * 2) + 1].get_ydata()[1]
        print(dict1)
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)


bp = plt.boxplot(data)
get_box_plot_data(data, bp)
print(data)
show()

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import nltk
nltk.download('wordnet')
"""
print("------------------------------------------------------------")  # 60個

# SelectFromModel

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import SVC

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print("X.shape")
print(cc)

# SelectFromModel特徵選取

svc = SVC(kernel="linear", C=1)
clf = SelectFromModel(estimator=svc, threshold="mean")
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print("X_new.shape")
print(cc)

print("特徵是否被選取")
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

print("選擇2個特徵")
X = X_new

print("資料分割")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
# ((120, 2), (30, 2), (120,), (30,))

print("特徵縮放")
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 7. 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(y_pred)

print("計算準確率")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.67%

from sklearn.metrics import confusion_matrix

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import ConfusionMatrixDisplay

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

print("使用全部特徵")

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# (120, 4) (30, 4) (120,) (30,)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

print("模型計分")
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 順序特徵選取(Sequential Feature Selection)

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.svm import SVC

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print(cc)

# SFS 特徵選取
svc = SVC(kernel="linear", C=1)
clf = SequentialFeatureSelector(estimator=svc, n_features_to_select=2)
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print(cc)

# 特徵是否被選取
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 7. 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 86.67%

from sklearn.metrics import confusion_matrix

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import ConfusionMatrixDisplay

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

print("使用全部特徵")

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 實現PCA演算法

# 建立測試資料

# 固定隨機種子
np.random.seed(2342347)

# 第一個類別
mu_vec1 = np.array([0, 0, 0])  # 平均數
cov_mat1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

# 第二個類別
mu_vec2 = np.array([1, 1, 1])  # 平均數
cov_mat2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T

cc = class1_sample.shape, class2_sample.shape
print(cc)

# 繪圖

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot(
    class1_sample[0, :],
    class1_sample[1, :],
    class1_sample[2, :],
    "o",
    markersize=8,
    color="blue",
    alpha=0.5,
    label="類別1",
)
ax.plot(
    class2_sample[0, :],
    class2_sample[1, :],
    class2_sample[2, :],
    "^",
    markersize=8,
    alpha=0.5,
    color="red",
    label="類別2",
)

plt.title("測試資料")
ax.legend(loc="upper right")

show()

# 合併資料

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
cc = all_samples.shape
print(cc)

# 計算共變異數矩陣(covariance matrix)

cov_mat = np.cov([all_samples[0, :], all_samples[1, :], all_samples[2, :]])
print("共變異數矩陣:\n", cov_mat)

# 計算特徵向量(eigenvector)及對應的特徵值(eigenvalue, λ)

# 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
eig_val_sc, eig_vec_sc = np.linalg.eig(cov_mat)
print("特徵向量:\n", eig_vec_sc)
print("特徵值:\n", eig_val_sc)

# 繪製特徵向量

from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch


# 繪製箭頭
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


# 設定 3D 繪圖
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# 繪製特徵向量
ax.plot(
    all_samples[0, :],
    all_samples[1, :],
    all_samples[2, :],
    "o",
    markersize=8,
    color="green",
    alpha=0.2,
)
[mean_x, mean_y, mean_z] = np.mean(all_samples, axis=1)
ax.plot([mean_x], [mean_y], [mean_z], "o", markersize=10, color="red", alpha=0.5)
for v in eig_vec_sc.T:
    a = Arrow3D(
        [mean_x, v[0]],
        [mean_y, v[1]],
        [mean_z, v[2]],
        mutation_scale=20,
        lw=3,
        arrowstyle="-|>",
        color="r",
    )
    ax.add_artist(a)
ax.set_xlabel("x_values")
ax.set_ylabel("y_values")
ax.set_zlabel("z_values")

show()

# 合併特徵向量及特徵值，針對特徵值降冪排序，挑出前2名。

# 合併特徵向量及特徵值
eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:, i]) for i in range(len(eig_val_sc))]

# 針對特徵值降冪排序
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# 挑出前2名
for i in eig_pairs[:2]:
    print(i[1])

# 座標轉換矩陣

matrix_w = np.hstack((eig_pairs[0][1].reshape(3, 1), eig_pairs[1][1].reshape(3, 1)))
print("Matrix W:\n", matrix_w)

# 原始資料乘以轉換矩陣，得到主成分

transformed = matrix_w.T.dot(all_samples)
cc = transformed.shape
print(cc)

# 繪製轉換後的資料

plt.plot(
    transformed[0, 0:20],
    transformed[1, 0:20],
    "o",
    markersize=7,
    color="blue",
    alpha=0.5,
    label="class1",
)
plt.plot(
    transformed[0, 20:40],
    transformed[1, 20:40],
    "^",
    markersize=7,
    color="red",
    alpha=0.5,
    label="class2",
)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel("x_values")
plt.ylabel("y_values")
plt.legend()
plt.title("Transformed samples with class labels")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PCA 個案實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析
# 資料集說明
# print(ds.DESCR)

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 進行特徵萃取(PCA)


# PCA 函數實作
def PCA_numpy(X, X_test, no):
    cov_mat = np.cov(X.T)
    # 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
    eigen_val, eigen_vecs = np.linalg.eig(cov_mat)
    # 合併特徵向量及特徵值
    eigen_pairs = [
        (np.abs(eigen_val[i]), eigen_vecs[:, i]) for i in range(len(eigen_vecs))
    ]

    # 針對特徵值降冪排序
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)

    w = eigen_pairs[0][1][:, np.newaxis]
    for i in range(1, no):
        w = np.hstack((w, eigen_pairs[i][1][:, np.newaxis]))

    # 轉換：矩陣相乘 (n, m) x (m, 2) = (n, 2)
    return X.dot(w), X_test.dot(w)


X_train_pca, X_test_pca = PCA_numpy(X_train_std, X_test_std, 2)  # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_pca, y_train)  # 學習訓練.fit

# 7. 模型計分
# 計算準確率
y_pred = clf.predict(X_test_pca)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

# 繪製決策邊界(Decision regions)
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  # 預測.predict
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    """ NG
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )
    """


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
show()

# 使用全部特徵

X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn PCA 實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 特徵萃取(PCA)
from sklearn.decomposition import PCA

pca1 = PCA(n_components=2)
X_train_pca = pca1.fit_transform(X_train_std)
X_test_pca = pca1.transform(X_test_std)
cc = X_train_pca.shape, X_test_pca.shape, pca1.explained_variance_ratio_
print(cc)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_pca, y_train)  # 學習訓練.fit

# 7. 模型計分
# 計算準確率
y_pred = clf.predict(X_test_pca)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 97.22%

# 繪製決策邊界(Decision regions)
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  # 預測.predict
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    """ NG
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )
    """


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
show()

# 使用全部特徵

X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 94.44%

# 測試Scikit-learn 的PCA函數其他用法

# 不設定參數
pca1 = PCA()
X_train_pca = pca1.fit_transform(X_train_std)
pca1.explained_variance_ratio_

# 加總可解釋變異
np.sum(pca1.explained_variance_ratio_)

# 1.0

# 對可解釋變異繪製柏拉圖(Pareto)
plt.bar(range(1, 14), pca1.explained_variance_ratio_, alpha=0.5, align="center")
plt.step(range(1, 14), np.cumsum(pca1.explained_variance_ratio_), where="mid")
plt.ylabel("Explained variance ratio")
plt.xlabel("Principal components")
plt.axhline(0.8, color="r", linestyle="--")
show()

# 設定可解釋變異下限
pca2 = PCA(0.8)
X_train_pca = pca2.fit_transform(X_train_std)
cc = X_train_pca.shape
print(cc)

print("------------------------------------------------------------")  # 60個

# LDA 個案實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 進行特徵萃取


# 計算 S_W, S_B 散佈矩陣
def calculate_SW_SB(X, y, label_count):
    mean_vecs = []
    for label in range(label_count):
        mean_vecs.append(np.mean(X[y == label], axis=0))
        print(f"Class {label} Mean = {mean_vecs[label]}")

    d = X.shape[1]  # number of features
    S_W = np.zeros((d, d))
    for label, mv in zip(range(label_count), mean_vecs):
        class_scatter = np.cov(X[y == label].T)
        S_W += class_scatter
    print(f"Sw shape:{S_W.shape}")

    mean_overall = np.mean(X, axis=0)
    S_B = np.zeros((d, d))
    for i, mean_vec in enumerate(mean_vecs):
        n = X[y == i + 1, :].shape[0]
        mean_vec = mean_vec.reshape(d, 1)  # make column vector
        mean_overall = mean_overall.reshape(d, 1)  # make column vector
        S_B += n * (mean_vec - mean_overall).dot((mean_vec - mean_overall).T)
    print(f"Sb shape:{S_B.shape}")
    return S_W, S_B


# LDA 函數實作
def LDA_numpy(X, X_test, y, label_count, no):
    S_W, S_B = calculate_SW_SB(X, y, label_count)
    # 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
    eigen_val, eigen_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
    # 合併特徵向量及特徵值
    eigen_pairs = [
        (np.abs(eigen_val[i]), eigen_vecs[:, i]) for i in range(len(eigen_vecs))
    ]
    print("Eigenvalues in descending order:\n")
    for eigen_val in eigen_pairs:
        print(eigen_val[0])

    # 針對特徵值降冪排序
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)

    w = eigen_pairs[0][1][:, np.newaxis].real
    for i in range(1, no):
        w = np.hstack((w, eigen_pairs[i][1][:, np.newaxis].real))

    # 轉換：矩陣相乘 (n, m) x (m, 2) = (n, 2)
    return X.dot(w), X_test.dot(w)


X_train_pca, X_test_pca = LDA_numpy(
    X_train_std, X_test_std, y_train, len(ds.target_names), 2
)  # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

# 6. 模型訓練
clf.fit(X_train_pca, y_train)  # 學習訓練.fit

# 7. 模型計分
# 計算準確率
y_pred = clf.predict(X_test_pca)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  # 預測.predict
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    """ NG
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )
    """


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
show()

# 使用全部特徵

X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn LDA實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 特徵萃取(LDA)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std, y_train)
X_test_lda = lda.transform(X_test_std)
cc = X_train_lda.shape, X_test_lda.shape, lda.explained_variance_ratio_
print(cc)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

# 6. 模型訓練
clf.fit(X_train_lda, y_train)  # 學習訓練.fit

# 7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_lda)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

# 繪製決策邊界(Decision regions)
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  # 預測.predict
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    """
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )
    """


plot_decision_regions(X_test_lda, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
show()

# 使用全部特徵

X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn LDA實作

# 載入資料
from sklearn.datasets import make_circles

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
show()

# PCA 萃取特徵

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=2)
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = pca.fit(X_train).transform(X_test)  # 學習訓練.fit

# 繪製原始測試資料及經PCA轉換後的新資料

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
show()

# KernelPCA 萃取特徵

from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")
show()

# 載入上/下弦月資料

from sklearn.datasets import make_moons

# X, y = make_moons(n_samples=1_000, noise=0.05, random_state=0)
X, y = make_moons(n_samples=1000, random_state=123)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
show()

# PCA 萃取特徵

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=2)
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = pca.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
show()

# KernelPCA 萃取特徵

from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(n_components=None, kernel="rbf", gamma=15)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)  # 學習訓練.fit

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# t-SNE測試

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# 生成3個集群資料

np.random.seed(10)
num_points_per_class = 50

# Class 1
mean1 = [0, 0]
cov = [[0.1, 0], [0, 0.1]]
X1 = np.random.multivariate_normal(mean1, cov, num_points_per_class)

# Class 2
mean2 = [10, 0]
X2 = np.random.multivariate_normal(mean2, cov, num_points_per_class)

# Class 3
mean3 = [5, 6]
X3 = np.random.multivariate_normal(mean3, cov, num_points_per_class)

X = np.concatenate([X1, X2, X3], axis=0)
cc = X.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# 繪圖

colors = ["red", "green", "blue"]
for i in range(3):
    plt.scatter(X[i * 50 : (i + 1) * 50, 0], X[i * 50 : (i + 1) * 50, 1], c=colors[i])

show()

# t-SNE

perplexity = 25
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()

# PCA

X_pca = PCA(n_components=1).fit_transform(X)
for i in range(3):
    plt.scatter(X_pca[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


# 困惑度(perplexity)測試

perplexity = 2
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


perplexity = 130
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
show()


# 非線性分離
# 生成S曲線資料

from matplotlib import ticker
from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
cc = S_points.shape, S_color.shape
print(cc)

# ((1500, 3), (1500,))

# 定義繪圖函數


def plot_2d(points, points_color, title):
    fig, ax = plt.subplots(figsize=(3, 3), facecolor="white", constrained_layout=True)
    fig.suptitle(title, size=16)
    add_2d_scatter(ax, points, points_color)
    show()


def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


def plot_3d(points, points_color, title):
    x, y, z = points.T

    fig, ax = plt.subplots(
        figsize=(6, 6),
        facecolor="white",
        tight_layout=True,
        subplot_kw={"projection": "3d"},
    )
    fig.suptitle(title, size=16)
    col = ax.scatter(x, y, z, c=points_color, s=50, alpha=0.8)
    ax.view_init(azim=-60, elev=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(1))

    fig.colorbar(col, ax=ax, orientation="horizontal", shrink=0.6, aspect=60, pad=0.01)
    show()


# 繪製原始資料

plot_3d(S_points, S_color, "Original S-curve samples")

# 繪製降維後資料

t_sne = manifold.TSNE(
    n_components=2,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)

plot_2d(S_t_sne, S_color, "T-distributed Stochastic  \n Neighbor Embedding")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04_19_BOW

# 使用BOW猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 載入資料

with open("./data/news.txt", "r+", encoding="UTF-8") as f:
    text = f.read()
# print(text)

# BOW 轉換
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([text])
# 生字表
cc = vectorizer.get_feature_names_out()
print(cc)


print("單字對應的出現次數")
cc = X.toarray()
print(cc)


print("找出較常出現的單字")

import collections

MAX_FEATURES = 20
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")


print("考慮停用詞(Stop words)")

MAX_FEATURES = 20

# 轉換為 BOW
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")


print("詞形還原(Lemmatization)")

text = text.lower().replace("korean", "korea").replace("stores", "store")

MAX_FEATURES = 20

# 轉換為 BOW
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用BOW猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 測試資料

corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# BOW 轉換
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
# 生字表
cc = vectorizer.get_feature_names_out()
print(cc)

print("使用表格呈現單字及對應出現的次數")

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)

print("相似性比較")

from sklearn.metrics.pairwise import cosine_similarity

cc = cosine_similarity(df.iloc[-1:].values, df.iloc[:-1].values)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# spam_classification_with_tfidf
# 垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
import re

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
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8111)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no = 0
for i in tfidf_matrix.toarray()[0]:
    if i > 0.0:
        no += 1
print(no)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = LogisticRegression()

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict
cc = accuracy_score(y_pred, y_test)
print(cc)

# 0.9668161434977578

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print(classification_report(y_test, y_pred))

print("混淆矩陣")
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
cc = clf.predict(X_new.toarray())  # 預測.predict
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性迴歸

# OLS 公式
# y = wx + b

# 使用 OLS 公式計算 w、b

df = pd.read_csv("./data/population.csv")
print(df)

w = ((df["pop"] - df["pop"].mean()) * df["year"]).sum() / (
    (df["year"] - df["year"].mean()) ** 2
).sum()
b = df["pop"].mean() - w * df["year"].mean()

print(f"w={w}, b={b}")

# 使用NumPy函數polyfit驗算

coef = np.polyfit(df["year"], df["pop"], deg=1)
print(f"w={coef[0]}, b={coef[1]}")

# w=0.061159358661554586, b=-116.35631056117121

print("使用sklearn的 線性迴歸 LinearRegression()")

X, y = df[["year"]].values, df["pop"].values

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

cc = linear_regression.coef_, linear_regression.intercept_
print(cc)

# (array([0.06115936]), -116.3563105611711)

print("使用公式預測2050年人口數")

print(2050 * coef[0] + coef[1])

# 9.02037469501569

print("使用矩陣計算")

X = df[["year"]].values

# b = b * 1
one = np.ones((len(df), 1))

# 將 x 與 one 合併
X = np.concatenate((X, one), axis=1)

y = df[["pop"]].values

# 求解
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"w={w[0, 0]}, b={w[1, 0]}")

# w=0.06115935866154644, b=-116.35631056115507

print("以Scikit-Learn的房價資料集為例，求解線性迴歸")

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

print("使用矩陣計算")

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values

# b = b * 1
one = np.ones((X.shape[0], 1))

# 將 x 與 one 合併
X2 = np.concatenate((X, one), axis=1)

# 求解
w = np.linalg.inv(X2.T @ X2) @ X2.T @ y
print(w)

print("使用sklearn的 線性迴歸 LinearRegression()")

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

print(linear_regression.coef_, linear_regression.intercept_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_02_ linear_regression_boston

# 房價預測

from sklearn.preprocessing import StandardScaler

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

df.info()  # 這樣就已經把資料集彙總資訊印出來

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 直方圖
X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
show()

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

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

# 7. 模型評分

# R2、MSE、MAE
y_pred = linear_regression.predict(X_test_std)  # 預測.predict
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("權重")
print(linear_regression.coef_)

print("偏差(Bias)")
print(linear_regression.intercept_)

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
joblib.dump(linear_regression, "tmp_linear_regression_model.joblib")
joblib.dump(scaler, "tmp_linear_regression_scaler.joblib")

# 10.模型預測
# 載入模型與標準化轉換模型
linear_regression2 = joblib.load("tmp_linear_regression_model.joblib")
scaler = joblib.load("tmp_linear_regression_scaler.joblib")

list1 = [0 for _ in range(13)]

list1[0] = 1.7  # 犯罪率
list1[1] = 11.0  # 大坪數房屋比例
list1[2] = 11.0  # 非零售業的營業面積比例
list1[3] = 0  # 是否靠近河岸, 0: "否", 1: "是"
list1[4] = 0.5  # 一氧化氮濃度
list1[5] = 6.0  # 平均房間數
list1[6] = 0.0  # 屋齡(1940年前建造比例)
list1[7] = 3.8  # 與商業區距離
list1[8] = 10.0  # 與高速公路距離
list1[9] = 408.0  # 地價稅
list1[10] = 18.0  # 師生比例
list1[11] = 356.0  # 黑人比例(Bk — 0.63)²
list1[12] = 12.0  # 低下階級的比例

X_new = [list1]
X_new = scaler.transform(X_new)

print(f"### 預測房價：{linear_regression2.predict(X_new)[0]:.2f}")  # 預測.predict

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_04_nonlinear_regression.ipynb

# 以二次迴歸預測世界人口數

df = pd.read_csv("./data/population.csv")
X, y = df[["year"]].values, df["pop"].values

# 使用 NumPy polyfit 計算

coef = np.polyfit(X.reshape(-1), y, deg=2)
print(f"y={coef[0]} X^2 + {coef[1]} X + {coef[2]}")
# y=-0.0002668845596210234 X^2 + 1.1420418251266993 X + -1210.2427271938489

plt.figure(figsize=(8, 6))
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.scatter(df["year"], y, c="blue", marker="o", s=2, label="實際")

plt.plot(
    df["year"].values,
    (df["year"] ** 2) * coef[0] + df["year"] * coef[1] + coef[2],
    c="red",
    label="預測",
)
plt.legend()
show()


# 使用公式預測2050年人口數

print((2050**2) * coef[0] + 2050 * coef[1] + coef[2])

# 9.360652508533576

# 產生 X 平方項，並與X合併

X_2 = X**2
X_new = np.concatenate((X_2, X), axis=1)
cc = X_new.shape
print(cc)

# (151, 2)

print("使用sklearn的 線性迴歸 LinearRegression()")

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_new, y)  # 學習訓練.fit

cc = linear_regression.coef_, linear_regression.intercept_
print(cc)

# (array([-2.66884560e-04,  1.14204183e+00]), -1210.242727194026)

print("使用公式預測2050年人口數")

print(
    (2050**2) * linear_regression.coef_[0]
    + 2050 * linear_regression.coef_[1]
    + linear_regression.intercept_
)

# 9.36065250853244

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_05_multi_variables_nonlinear_regression

# 多元非線性迴歸

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=300, n_features=2, noise=50)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
plt.rcParams["legend.fontsize"] = 10
ax.plot(X[:, 0], X[:, 1], y, "o", markersize=8, color="blue", alpha=0.5)
plt.title("測試資料")
show()

# 使用 PolynomialFeatures 產生多項式

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)  # 2 次方
X_new = poly.fit_transform(X)  # 轉換
cc = X_new.shape
print(cc)

cc = poly.get_feature_names_out(["x1", "x2"])
print(cc)

X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

cc = linear_regression.coef_, linear_regression.intercept_
print(cc)

# R2、MSE、MAE
y_pred = linear_regression.predict(X_test_std)  # 預測.predict
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

# R2 = 52.87
# MSE = 3155.4231199414303
# MAE = 45.322099168462366

# 使用原始特徵的模型評分

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test_std)  # 預測.predict
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_06_regression_outlier_effect

# 迴歸缺點

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=20, n_features=1, noise=50)

# 繪圖

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(8, 8))
plt.scatter(X, y, color="blue", alpha=0.5)
plt.title("測試資料")
show()

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

cc = linear_regression.coef_, linear_regression.intercept_
print(cc)

print("製造離群值")

print(y[0])

# 製造離群值
y[0] += 2000

linear_regression2 = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression2.fit(X, y)  # 學習訓練.fit

cc = linear_regression2.coef_, linear_regression2.intercept_
print(cc)

fig = plt.figure(figsize=(8, 8))
plt.scatter(X, y, color="blue", alpha=0.5)

line_X = np.array([-3, 3])
plt.plot(
    line_X,
    line_X * linear_regression.coef_ + linear_regression.intercept_,
    c="green",
    label="原迴歸線",
)
plt.plot(
    line_X,
    line_X * linear_regression2.coef_ + linear_regression2.intercept_,
    c="red",
    label="新迴歸線",
)
plt.title("測試資料")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_07_regression_vs_time_series

# 迴歸(Regression)與時間序列(Time Series) 比較

df = pd.read_csv("./data/monthly-airline-passengers.csv")
print(df)

# 資料轉換

# 設定為日期的資料型態
df["Date"] = pd.to_datetime(df["Month"])

# 設定日期為 DataFrame 的索引值
df = df.set_index("Date")

# 依照資料內容設定日期的頻率
df.index = pd.DatetimeIndex(df.index.values, freq=df.index.inferred_freq)
# 將原有欄位刪除
df.drop("Month", axis=1, inplace=True)

# 繪圖

plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
show()

# 迴歸(Regression)
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# X = df.index.astype(str).map(lambda x:x[:4]+x[5:7]).values.reshape(df.shape[0], -1)
X = np.arange(df.shape[0]).reshape(-1, 1)
y = df["Passengers"]

linear_regression.fit(X, y)  # 學習訓練.fit

pred = linear_regression.predict(X)  # 預測.predict
print("MSE =", mean_squared_error(y, pred))

# MSE = 2091.7994339346533

# 實際樣本點
plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
# show()

# 預測迴歸線
plt.plot(df.index, pred)
show()

# 殘差線圖
plt.plot(df.index, np.abs(df["Passengers"] - pred))
show()

# 定態測試(Augmented Dickey–Fuller Test for Stationarity)

from statsmodels.tsa.stattools import adfuller

result = adfuller(df["Passengers"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: 0.8153688792060482
p value: 0.991880243437641
滯後期數(Lags): 13
資料筆數: 130
"""

# 結論：p > 0.05 ==> 非定態

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df["Passengers"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df["Passengers"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# 時間序列(Time Series)

from statsmodels.tsa.arima.model import ARIMA

# 建立時間序列資料
series = df.copy()

# AR(1) 模型訓練
ar = ARIMA(df, order=(1, 0, 0))

model = ar.fit()  # 學習訓練.fit

print("檢視神經網路")
model.summary()  # 檢視神經網路

cc = model.params
print(cc)

cc = df["Passengers"].mean()
print(cc)

# 繪圖比較實際值與預測值

cc = model.fittedvalues
print(cc)

series["Passengers"].plot(figsize=(12, 6), color="black", linestyle="-", label="實際值")
model.fittedvalues.plot(
    figsize=(12, 6), color="green", linestyle=":", lw=2, label="預測值"
)
plt.legend()
show()

print(f"AR MSE = {(np.sum(model.resid**2) / len(model.resid)):.2f}")

# AR MSE = 1301.63

# 使用迴歸驗證
linear_regression2 = sklearn.linear_model.LinearRegression()  # 函數學習機

# 複製資料
series2 = series.copy()

# 將前一期 y 當作 x
series2["Passengers_1"] = series2["Passengers"].shift(-1)
series2.dropna(inplace=True)
X = series2["Passengers"].values.reshape(series2.shape[0], -1)

linear_regression2.fit(X, series2["Passengers_1"])  # 學習訓練.fit

cc = linear_regression2.coef_, linear_regression2.intercept_
print(cc)

# (array([0.95893198]), 13.705504997522155)

series2["TS"] = model.fittedvalues
series2["LR"] = (
    linear_regression2.coef_ * series["Passengers"] + linear_regression2.intercept_
)
series2["LR"].plot(color="green", linestyle="-.", lw=2, legend="LR")
series2["TS"].plot(figsize=(12, 6), color="red", linestyle=":", lw=2, legend="TS")
show()

cc = series2[["TS", "LR"]]
print(cc)

# AR(1) 殘差(residual)繪圖

residuals = pd.DataFrame(model.resid)
residuals.plot()
show()

# 資料分割
X_train, X_test = train_test_split(series, test_size=0.2, shuffle=False)

# 查看陣列維度
cc = X_train.shape, X_test.shape
print(cc)

# 模型訓練、預測與繪圖

# AR(1) 模型訓練
ar_1 = ARIMA(X_train[["Passengers"]], order=(1, 0, 0))

model_1 = ar_1.fit()  # 學習訓練.fit

# 預測 12 個月
pred = model_1.predict(X_train.shape[0], X_train.shape[0] + 12 - 1)  # 預測.predict

# 繪圖
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

series["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_1.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
show()

# 改用 SARIMAX (Seasonal ARIMA) 演算法
# 一次差分(First-order Differencing)

df_diff = df.copy()
df_diff["Passengers_diff"] = df_diff["Passengers"] - df_diff["Passengers"].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff"].plot()
show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: -2.8292668241699994
p value: 0.0542132902838255
滯後期數(Lags): 12
資料筆數: 130
"""

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df_diff["Passengers_diff"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df_diff["Passengers_diff"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# 二次差分(Second-order Differencing)

df_diff["Passengers_diff_2"] = df_diff["Passengers_diff"] - df_diff[
    "Passengers_diff"
].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff_2"].plot()
show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff_2"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)
"""
Test Stat: -16.384231542468505
p value: 2.7328918500142407e-29
Lags: 11
Num observations: 130
"""
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig = plot_acf(df_diff["Passengers_diff_2"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df_diff["Passengers_diff_2"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# SARIMAX

# 資料分割
X_train, X_test = train_test_split(df_diff, test_size=0.2, shuffle=False)

# SARIMAX
import statsmodels.api as sm

ar_diff = sm.tsa.statespace.SARIMAX(
    X_train[["Passengers"]], order=(1, 2, 1), seasonal_order=(1, 2, 1, 12)
)

print("到這邊會脫離程式......................")

"""
# 這個 .fit 有問題 會脫離程式
model_diff = ar_diff.fit()  # 學習訓練.fit

# 預測 12 個月
pred = model_diff.predict(X_train.shape[0], X_train.shape[0] + 12 - 1, dynamic=True)  # 預測.predict
print(pred)

df_diff["pred"] = np.concatenate((model_diff.fittedvalues.values, pred.values))
cc = df_diff["pred"]
print(cc)

# 繪圖

df_diff["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_diff.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
show()

print(f"SARIMAX MSE = {(np.sum(model_diff.resid**2) / len(model_diff.resid)):.2f}")

# SARIMAX MSE = 427.67

# 結論：SARIMAX 準確率比迴歸高
# 時間序列 MSE： 427， 迴歸 MSE： 2091

from statsmodels.tsa.seasonal import seasonal_decompose

decomp = pd.read_csv("./data/monthly-airline-passengers.csv")
decomp["Date"] = pd.to_datetime(decomp["Month"])
decomp = decomp.set_index("Date")
decomp.index = pd.DatetimeIndex(df.index.values, freq=decomp.index.inferred_freq)
decomp.drop("Month", axis=1, inplace=True)

s_dc = seasonal_decompose(decomp["Passengers"], model="additive")
decomp["SDC_Seasonal"] = s_dc.seasonal
decomp["SDC_Trend"] = s_dc.trend
decomp["SDC_Error"] = s_dc.resid
decomp["SDC_TS"] = s_dc.trend + s_dc.seasonal

print("ddddd")

plt.title("Trend components")
decomp["Passengers"].plot(
    figsize=(12, 6), color="black", linestyle="-", legend="Passengers"
)
decomp["SDC_Trend"].plot(
    figsize=(12, 6), color="blue", linestyle="-.", lw=2, legend="SDC_Trend"
)
decomp["SDC_TS"].plot(figsize=(12, 6), color="green", linestyle=":", lw=2, legend="TS")

show()

# 效應分解(Decomposition)

# Plot the original time series, trend, seasonal and random components
fig, axarr = plt.subplots(4, sharex=True)
fig.set_size_inches(5.5, 5.5)

decomp["Passengers"].plot(ax=axarr[0], color="b", linestyle="-")
axarr[0].set_title("Monthly Passengers")

pd.Series(data=decomp["SDC_Trend"], index=decomp.index).plot(
    color="r", linestyle="-", ax=axarr[1]
)
axarr[1].set_title("Trend component in monthly employment")

pd.Series(data=decomp["SDC_Seasonal"], index=decomp.index).plot(
    color="g", linestyle="-", ax=axarr[2]
)
axarr[2].set_title("Seasonal component in monthly employment")

pd.Series(data=decomp["SDC_Error"], index=decomp.index).plot(
    color="k", linestyle="-", ax=axarr[3]
)
axarr[3].set_title("Irregular variations in monthly employment")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)
fig = plt.xticks(rotation=10)

show()

MSE = (decomp["SDC_Error"] ** 2).sum() / decomp["SDC_Error"].shape[0]
print("MSE=", MSE)

"""
# ('MSE=', 340.80467800107556)

"""
結論：時間序列預測準確率比迴歸高
時間序列 MSE： 340， 迴歸 MSE： 2091
"""

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
show()

# 以 Scikit-learn 驗證

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_03_logistic_regression_attrition

# 員工流失預測

from sklearn import preprocessing

df = pd.read_csv("./data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
cc = df.head()
print(cc)

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

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法、6. 模型訓練

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model=sm.Logit(y_train,X_train)
result=model.fit()
print(result.summary())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_06_knn_book_recommender

# 以KNN演算法實作書籍推薦

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
plt.savefig("tmp_system2.png", bbox_inches="tight")
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

# 載入內建 movielens-100k 資料集
data = Dataset.load_builtin("ml-100k")
print("user id\titem id\trating\ttimestamp")
cc = data.raw_ratings[:10]
print(cc)

# 資料分割

# 切分為訓練及測試資料，測試資料佔 20%
trainset, testset = train_test_split(data, test_size=0.2)

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

from sklearn import preprocessing

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
from wordcloud import WordCloud
import re

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
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

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
X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)
# 模型訓練

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

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

X_train, X_test, y_train, y_test = train_test_split(
    iris_data[["sepal length (cm)", "petal length (cm)"]],
    iris_data[["target"]],
    test_size=0.2,
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_03_svm _sample_weight

# 不平衡的資料集利用sample_weight矯正

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_04_svm_kernels

# 非線性分割SVM測試

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_05_svr_kernels

# 房價預測

from sklearn.preprocessing import StandardScaler

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

df.info()  # 這樣就已經把資料集彙總資訊印出來

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 繪圖

# 直方圖
X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
show()

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
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.decomposition import PCA

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
y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 分類報告

y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))

# 混淆矩陣圖

ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation=30
)
show()

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition_org

# Faces recognition example using eigenfaces and SVMs

# The dataset used in this example is a preprocessed excerpt of the "Labeled Faces in the Wild", aka LFW_:

# http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

from time import time
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
    X, y, test_size=0.2, random_state=42
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
show()

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_07_decision_tree_from_scratch

# 自行開發決策樹

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
from sklearn.tree import plot_tree

plt.figure(figsize=(14, 10))
plot_tree(clf, feature_names=feature_names)
show()

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

from sklearn.tree import DecisionTreeRegressor

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_10_decision_tree_regression_boston

# 房價預測

from sklearn.preprocessing import StandardScaler

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
X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
show()

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

from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_12_scikit-learn_random_forest
# Scikit-learn決策樹演算法

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

plt.figure(figsize=(10, 6))
df = pd.DataFrame(
    {"feature_names": feature_names, "feature_importance": clf.feature_importances_}
)
df.sort_values(by=["feature_importance"], ascending=False, inplace=True)
sns.barplot(x=df["feature_importance"], y=df["feature_names"])
show()

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
show()

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
