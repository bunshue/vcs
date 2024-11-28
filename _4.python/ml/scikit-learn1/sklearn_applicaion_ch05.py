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
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

# 載入迴歸常見的評估指標
from sklearn.metrics import mean_squared_error  # 均方誤差 Mean Squared Error (MSE)
from sklearn.metrics import mean_absolute_error  # 平均絕對誤差 Mean Absolute Error (MAE)
from sklearn.metrics import r2_score  # R-Squared擬合度
from sklearn.metrics import accuracy_score  # 沒用到

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

# 存檔
import joblib

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

# 載入資料集

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

# 5. 選擇演算法
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

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
plt.show()

print("使用全部特徵")

# 載入資料集
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

# 模型訓練
from sklearn.linear_model import LogisticRegression

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

# 載入資料集

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

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
plt.show()

print("使用全部特徵")

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

plt.show()

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

plt.show()

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
plt.show()

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

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
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

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
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

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
plt.show()

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

# 5. 選擇演算法
from sklearn.linear_model import LogisticRegression

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
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

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

# 5. 選擇演算法
from sklearn.linear_model import LogisticRegression

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
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_lda, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

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
plt.show()

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
plt.show()

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
plt.show()

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
plt.show()

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
plt.show()

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

plt.show()

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

plt.show()

# t-SNE

perplexity = 25
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()

# PCA

X_pca = PCA(n_components=1).fit_transform(X)
for i in range(3):
    plt.scatter(X_pca[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


# 困惑度(perplexity)測試

perplexity = 2
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


perplexity = 130
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


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
    plt.show()


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
    plt.show()


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
from math import log, sqrt
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

from sklearn.linear_model import LogisticRegression

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

# 載入資料集
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
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 直方圖
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
import joblib

joblib.dump(linear_regression, "tmp_linear_regression_model.joblib")
joblib.dump(scaler, "tmp_linear_regression_scaler.joblib")

# 10.模型預測

import joblib

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

# 載入資料集

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
plt.show()


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

print((2050**2) * linear_regression.coef_[0] + 2050 * linear_regression.coef_[1] + linear_regression.intercept_)

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
plt.show()

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
plt.show()

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
plt.plot(line_X, line_X * linear_regression.coef_ + linear_regression.intercept_, c="green", label="原迴歸線")
plt.plot(line_X, line_X * linear_regression2.coef_ + linear_regression2.intercept_, c="red", label="新迴歸線")
plt.title("測試資料")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_07_regression_vs_time_series

# 迴歸(Regression)與時間序列(Time Series) 比較

# 載入資料集

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
plt.show()

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
# plt.show()

# 預測迴歸線
plt.plot(df.index, pred)
plt.show()

# 殘差線圖
plt.plot(df.index, np.abs(df["Passengers"] - pred))
plt.show()

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
plt.show()

fig = plot_pacf(df["Passengers"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

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
plt.show()

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
series2["LR"] = linear_regression2.coef_ * series["Passengers"] + linear_regression2.intercept_
series2["LR"].plot(color="green", linestyle="-.", lw=2, legend="LR")
series2["TS"].plot(figsize=(12, 6), color="red", linestyle=":", lw=2, legend="TS")
plt.show()

cc = series2[["TS", "LR"]]
print(cc)

# AR(1) 殘差(residual)繪圖

residuals = pd.DataFrame(model.resid)
residuals.plot()
plt.show()

test_size = 12 # ???

# 資料分割
X_train, X_test = train_test_split(series, test_size=test_size, shuffle=False)

# 查看陣列維度
cc = X_train.shape, X_test.shape
print(cc)

# 模型訓練、預測與繪圖

# AR(1) 模型訓練
ar_1 = ARIMA(X_train[["Passengers"]], order=(1, 0, 0))

model_1 = ar_1.fit()  # 學習訓練.fit

# 預測 12 個月
pred = model_1.predict(X_train.shape[0], X_train.shape[0] + test_size - 1)  # 預測.predict

# 繪圖
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

series["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_1.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
plt.show()

# 改用 SARIMAX (Seasonal ARIMA) 演算法
# 一次差分(First-order Differencing)

df_diff = df.copy()
df_diff["Passengers_diff"] = df_diff["Passengers"] - df_diff["Passengers"].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff"].plot()
plt.show()

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
plt.show()

fig = plot_pacf(df_diff["Passengers_diff"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

# 二次差分(Second-order Differencing)

df_diff["Passengers_diff_2"] = df_diff["Passengers_diff"] - df_diff[
    "Passengers_diff"
].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff_2"].plot()
plt.show()

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
plt.show()

fig = plot_pacf(df_diff["Passengers_diff_2"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
plt.show()

# SARIMAX

print("到這邊會脫離程式......................")

# 資料分割
X_train, X_test = train_test_split(df_diff, test_size=12, shuffle=False)

# SARIMAX
import statsmodels.api as sm

ar_diff = sm.tsa.statespace.SARIMAX(
    X_train[["Passengers"]], order=(1, 2, 1), seasonal_order=(1, 2, 1, 12)
)
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
plt.show()

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

plt.show()

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

plt.show()

MSE = (decomp["SDC_Error"] ** 2).sum() / decomp["SDC_Error"].shape[0]
print("MSE=", MSE)

# ('MSE=', 340.80467800107556)

"""
結論：時間序列預測準確率比迴歸高
時間序列 MSE： 340， 迴歸 MSE： 2091
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_08_regularization
# L1、L2 regularization的計算與強度比較

# 權重
W = np.array([-1, 5, 3, -9]).reshape(2, 2)
print(W)

# L1

Lambda = 0.5
L1 = Lambda * np.sum(np.abs(W))
print(L1)

# L2

L2 = Lambda * np.sum(W**2)
print(L2)

# 58.0

print("結論：L2 強度較大")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05_09_regularization_housing
# 過度擬合與regularization
# 載入房價資料集

train_df = pd.read_csv("./data/train.csv", index_col="ID")

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 模型訓練與評分

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

# 模型訓練
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train, y_train)  # 學習訓練.fit

print(f"訓練判定係數: {linear_regression.score(X_train, y_train)}")
print(f"測試判定係數: {linear_regression.score(X_test, y_test)}")

# 模型評分
y_pred = linear_regression.predict(X_test)  # 預測.predict

# 訓練判定係數: 0.7268827869293253
# 測試判定係數: 0.7254687959254533

# 生成新特徵，為舊特徵的平方

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 生成新特徵，為舊特徵的平方
X["crim_2"] = X["crim"] ** 2
X["zn_2"] = X["zn"] ** 2
X["indus_2"] = X["indus"] ** 2
X["chas_2"] = X["chas"] ** 2
X["nox_2"] = X["nox"] ** 2
X["rm_2"] = X["rm"] ** 2
X["age_2"] = X["age"] ** 2
X["dis_2"] = X["dis"] ** 2
X["rad_2"] = X["rad"] ** 2
X["tax_2"] = X["tax"] ** 2
X["ptratio_2"] = X["ptratio"] ** 2
X["black_2"] = X["black"] ** 2
X["lstat_2"] = X["lstat"] ** 2

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 模型訓練與評分

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline

# 建立管線
steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", LinearRegression()),
]
pipeline = Pipeline(steps)

pipeline.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {pipeline.score(X_train, y_train)}")
print(f"測試判定係數: {pipeline.score(X_test, y_test)}")

# 訓練判定係數: 1.0
# 測試判定係數: -60.45752231085903

# l2 Regularization or Ridge Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Ridge(alpha=10, fit_intercept=True)),
]

ridge_pipe = Pipeline(steps)

ridge_pipe.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {ridge_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {ridge_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.9411030494647765
# 測試判定係數: 0.8158674422432347

# l1 Regularization or Lasso Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Lasso(alpha=0.3, fit_intercept=True)),
]

lasso_pipe = Pipeline(steps)

lasso_pipe.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {lasso_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {lasso_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.8525646297860277
# 測試判定係數: 0.8367938135279831

print("結論：L1 test score 最高")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
