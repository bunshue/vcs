"""
葡萄酒品種分類資料集

紅酒資料集

#範例16-1:邏輯斯模型(logistic regression model，羅吉斯):分類，二分法類器
# 題目：預測3種意大利紅酒，將資料集分成train,test，先學習再預測，用3種指標來評估預測績效（決定係數R2，MAE，殘差圖）

#重點1：邏輯斯模型的應用性：
#羅吉斯迴歸現在已經被大量使用，因為它非常有效率，也不需要大量運算資源，所以受到廣泛利用。
它很容易解讀，不需要調整輸入特徵，也易於正規化，而且它所提供的輸出結果是經過良好校正的預測機率。
#應用1：衛生保健：例如預測受傷患者的死亡率。預測糖尿病和心臟病等疾病的發病率。
#應用2：政治:可用於預測選舉。這些預測是根據年齡、性別、居住地、社會地位、過往投票模式等變數，產生投票結果預測。
#應用3：產品測試：預測測試中系統或產品的成敗。
#應用4：行銷：可用於預測客戶詢價轉化為銷售的機率、訂閱開始或終止的機率，甚至是客戶對新產品系列的潛在興趣。
#應用5：金融業：可預測客戶未來遲繳的可能性，可以看出某位客戶是否會「違約」或「不違約」
#應用6：電子商務：電子商務公司大量投資於跨媒體廣告和促銷活動，很希望了解哪些活動最有效，以及最可能獲得潛在目標受眾響應的選項。
此模型集將客戶分類為「反應者」或「非反應者」，所以此模型稱為「反應傾向模型」。

#重點2：邏輯斯模型的預測數字：
#結果：0～1
#判別：0為否，1為是

#重點3：讀取sklearn的dataset，有2種做法：

#（1）方法1：
X, y = datasets.load_wine(return_X_y=True)
import sklearn.model_selection as ms
train_x, test_x, train_y, test_y = ms.train_test_split(X, y, test_size=0.2)

#（2）方法2：
wine = datasets.load_wine()
import sklearn.model_selection as ms
train_x, test_x, train_y, test_y = ms.train_test_split(wine.data, wine.target, test_size=0.2)

葡萄酒數據集/紅酒資料庫
Classes          3
Sample per class 59/71/48(共178筆資料)
Samples total    178
Dimensionality    13
Features         real, positive
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
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("葡萄酒品種分類資料集 基本數據 load_wine()")

wine = datasets.load_wine()

X = wine.data
y = wine.target  # 目標

print("目標 :", y)
print("目標名稱 :", wine.target_names)

print("幾個目標 :")
cc = wine.target[[10, 80, 140]]
print(cc)

print("wine.data.shape, 數據集資料 形狀")
print(wine.data.shape)

print("wine.frame")
print(wine.frame)
""" many
print("wine.DESCR, 數據集的完整描述, 資料集說明")
print(wine.DESCR)

print("wine")
print(wine)
"""

"""
看看各種影響酒品質的各種因素（欄位名稱）
data特徵資料的13個欄位名稱 = feature_names特徵名稱
data特徵資料的13個欄位數據 = data
"""
print("wine.feature_names, 數據集 欄位 的名稱, 特徵名稱")
print(wine.feature_names)

# wine.feature_names, 數據集 列 的名稱
cc = wine.data[:, [0]]  # alcohol
cc = wine.data[:, [1]]  # malic_acid
cc = wine.data[:, [2]]  # ash
cc = wine.data[:, [3]]  # alcalinity_of_ash
cc = wine.data[:, [4]]  # magnesium
cc = wine.data[:, [5]]  # total_phenols
cc = wine.data[:, [6]]  # flavanoids
cc = wine.data[:, [7]]  # nonflavanoid_phenols
cc = wine.data[:, [8]]  # proanthocyanins
cc = wine.data[:, [9]]  # color_intensity
cc = wine.data[:, [10]]  # hue
cc = wine.data[:, [11]]  # od280/od315_of_diluted_wines
cc = wine.data[:, [12]]  # proline

"""
先看資料集的keys:
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

# 看wine資料集的keys：
cc = wine.keys()
print(cc)

print(wine.data.shape)
print(wine.target.shape)

# data(特徵資料)的內容
print(wine.data)

# data(特徵資料（各種變數x1,x2,x3....）)總共幾筆
print(wine.data.shape)
# (178, 13)

# target：葡萄酒品種，總共幾筆
print(wine.target.shape)

"""
wine的數據有13種特徵欄位，而每個特徵變數有的意義分別為：
1.alcohol: 酒精濃度
2.malic acid：蘋果酸
3.ash：灰
4.alcalinity of ash：灰的鹼度
5.magnesium：鎂
6.total phenols：總酚
7.flavanoids：黃酮類化合物
8.nonflavanoid phenols：非黃烷類酚類
9.proanthocyanins：原花青素
10.color intensity：色彩強度
11.hue：色調
12.OD280/OD315 of diluted wines：稀釋酒
13.proline：脯氨酸
"""

print("------------------------------")  # 30個

print("wine轉df")
print("資料集的特徵(X)")

df = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df)

print("觀察資料集彙總資訊")
df.info()  # 這樣就已經把資料集彙總資訊印出來

print("描述統計量")
cc = df.describe()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

wine = datasets.load_wine()

x3 = wine.data[:, [0]]  # alcohol
y3 = wine.data[:, [9]]  # color_intensity

plt.subplot(121)
plt.scatter(x3, y3)

plt.subplot(122)
plt.hist(y3, bins=50)

plt.suptitle("wine")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

wine = datasets.load_wine()

df_X = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df_X.head())

df_y = pd.DataFrame(wine.target, columns=["kind(target)"])
print(df_y.head())

df = pd.concat([df_X, df_y], axis=1)
print(df.head())

plt.subplot(121)
plt.hist(df.loc[:, "alcohol"])

plt.subplot(122)
plt.boxplot(df.loc[:, "alcohol"])

show()

print(df.corr())
print(df.describe())

print("------------------------------")  # 30個

print("使用 scatter_matrix")
from pandas.plotting import scatter_matrix

_ = scatter_matrix(df, figsize=(15, 15))
show()

_ = scatter_matrix(df.iloc[:, [0, 9, -1]])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 支持向量機

wine = datasets.load_wine()

X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = SVC(gamma=0.001, decision_function_shape="ovo")
clf.fit(X_train, y_train)

dec = clf.decision_function(X_test)
cc = dec.shape[1]  # n_class * (n_class - 1) / 2 =  3*2/2 = 3
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.ensemble import RandomForestClassifier

wine = datasets.load_wine()

X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.3
)
model = RandomForestClassifier()
model.fit(X_train, y_train)  # 學習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("k-fold 交叉驗證法")

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

X, y = datasets.load_wine(return_X_y=True)

dx_std = StandardScaler().fit_transform(X)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, y, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

val_score = cross_val_score(forest, dx_train, dy_train, cv=5)

predictions = forest.predict(dx_test)

print("準確率:", forest.score(dx_train, dy_train))

print(val_score.mean().round(3))

print("準確率:", forest.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 產生預測結果報告

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X, y = datasets.load_wine(return_X_y=True)

dx_std = StandardScaler().fit_transform(X)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, y, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print("準確率:", forest.score(dx_train, dy_train))
print("準確率:", forest.score(dx_test, dy_test))

print(classification_report(dy_test, predictions))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("邏輯迴歸")

wine = datasets.load_wine()

# 5.練習5：把data資料轉成pandas的dataframe數據格式（變數df_x）

df_x = pd.DataFrame(wine.data, columns=wine.feature_names)

c1 = [
    "酒精濃度",
    "蘋果酸",
    "灰",
    "灰的鹼度",
    "鎂",
    "總酚",
    "黃酮類化合物",
    "非黃烷類酚類",
    "原花青素",
    "色彩強度",
    "色調",
    "稀釋酒",
    "脯氨酸",
]

# 設定英文欄位

df_x = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df_x)


# 設定中文欄位
c1 = [
    "酒精濃度",
    "蘋果酸",
    "灰",
    "灰的鹼度",
    "鎂",
    "總酚",
    "黃酮類化合物",
    "非黃烷類酚類",
    "原花青素",
    "色彩強度",
    "色調",
    "稀釋酒",
    "脯氨酸",
]
df_x = pd.DataFrame(wine.data, columns=c1)
print(df_x)


"""
#6.練習6：把target資料轉換成pandas數據dataframe格式（種類df_y）

df_y = pd.DataFrame(boston.target, columns=['種類'])
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

df_y = pd.DataFrame(wine.target, columns=["種類"])
print(df_y)

"""
#7.練習7：建立線性迴歸的模型sklearn model方法：（3步驟）
#1.步驟1：先建立數學模型(邏輯斯模型logistic regression model)

import sklearn.linear_model as lm

model = lm.LinearRegression())

#2.步驟2：讓模型model學習歷史數據

學習指令：model.fit(dataframeX, dataframeY)

3.步驟3：讓模型model進行預測

使用test_x進行預測=pred_y

然後比較實際數值test_y, 與pred_y的差異

指令：model.predict(test_X)

注意：t1,t2必須要是dataframe

t1 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

t2 =[[13.53, 4.10, 2.74, 24.5, 96.0, 2.05, 0.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

# 1.步驟1：先建立數學模型(邏輯斯模型logistic regression model)
import sklearn.linear_model as lm

model = lm.LogisticRegression()

# 2.步驟2：讓模型model學習歷史數據
model.fit(df_x, df_y)

# 3.步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[6]==>黃酮類化合物==>3.76
print("預測這個紅酒A的酒種：")
t1 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
model.predict(t1)

# 數據差別在[6]==>黃酮類化合物==>0.76
print("預測這個紅酒B的酒種：")
t2 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 0.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
# t1 =[[13.53,   3.10,   2.74,   24.5,   96.0,   2.05,   3.76,   0.56,   1.35,   9.20,   0.61,   1.60,   560.0]]
model.predict(t2)

"""
8.練習8：畫圖，黃酮類化合物 vs 酒種
畫圖的方式有2種
方法（1）使用df.plot(x="欄位", y="欄位", kind="scatter")
方法（2）使用plt.scatter(x=df[欄位], y=df[欄位])
數據點

t1 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

預測：t1-->model.predict(t1)

但是畫圖（黃酮類化合物 vs 酒種)

所以畫點（x = t1[0][6] ==> 黃酮類化合物 ==> 3.76)

但是預測值，還是（y = model.predict(t1))

plt.scatter(t1[0][6], model.predict(t1), label="預測紅酒A",color="red")
"""

plt.scatter(df_x["黃酮類化合物"], df_y, label="實際數據")
plt.scatter(t1[0][6], model.predict(t1), label="預測紅酒A", color="red")
plt.scatter(t2[0][6], model.predict(t2), label="預測紅酒B", color="orange")

plt.legend()
plt.xlabel("黃酮類化合物")
plt.ylabel("酒種")
plt.title("畫圖，黃酮類化合物 vs 酒種")
show()

"""
9.結論(1)：黃酮類化合物，不是影響酒種的關鍵因素
10.練習10：測試，不同『脯氨酸』是否是影響酒種的關鍵因素
步驟3：讓模型model進行預測:model.predict(dataframe())
數據差別在[12]==>脯氨酸==>1560.0

預測這個紅酒C的酒種：

t3 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 1560.0]]
數據差別在[12]==>脯氨酸==>560.0

預測這個紅酒D的酒種：

t4 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

model.predict(t1)
"""

from pickle import TUPLE3

# (1).步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[12]==>脯氨酸==>1560.0
print("預測這個紅酒C的酒種：")
t3 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 1560.0]]
model.predict(t3)

# (2).步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[12]==>脯氨酸==>560.0
print("預測這個紅酒D的酒種：")
t4 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
model.predict(t4)

plt.scatter(df_x["脯氨酸"], df_y, label="實際數據")
plt.scatter(t3[0][12], model.predict(t3), label="預測紅酒C", color="red")
plt.scatter(t4[0][12], model.predict(t4), label="預測紅酒D", color="orange")

plt.legend()
plt.xlabel("脯氨酸")
plt.ylabel("酒種")
plt.title("畫圖，脯氨酸 vs 酒種")
show()

# 11.結論(2)：脯氨酸，是影響酒種的關鍵因素

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("KMeans")

wine = datasets.load_wine()

X = wine.data[:, [0, 9]]

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

fig, ax = plt.subplots()
ax.scatter(X[pred == 0, 0], X[pred == 0, 1], color="red", marker="s", label="Label1")
ax.scatter(X[pred == 1, 0], X[pred == 1, 1], color="blue", marker="s", label="Label2")
ax.scatter(X[pred == 2, 0], X[pred == 2, 1], color="green", marker="s", label="Label3")
ax.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    s=200,
    color="yellow",
    marker="*",
    label="center",
)
ax.legend()
plt.title("wine")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PCA 個案實作

wine = datasets.load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
cc = df.head()
print(cc)

# 指定X、Y
X = df.values
y = wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
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

logistic_regression.fit(X_train_pca, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = logistic_regression.predict(X_test_pca)  # 預測.predict
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


plot_decision_regions(X_test_pca, y_test, classifier=logistic_regression)
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

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("PCA")

wine = datasets.load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
cc = df.head()
print(cc)

# 指定X、Y
X = df.values
y = wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
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

logistic_regression.fit(X_train_pca, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = logistic_regression.predict(X_test_pca)  # 預測.predict
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


plot_decision_regions(X_test_pca, y_test, classifier=logistic_regression)
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

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
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

wine = datasets.load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
cc = df.head()
print(cc)

# 指定X、Y
X = df.values
y = wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
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
    X_train_std, X_test_std, y_train, len(wine.target_names), 2
)  # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_pca, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = logistic_regression.predict(X_test_pca)  # 預測.predict
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


plot_decision_regions(X_test_pca, y_test, classifier=logistic_regression)
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

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("LDA")

wine = datasets.load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
cc = df.head()
print(cc)

# 指定X、Y
X = df.values
y = wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放
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

logistic_regression.fit(X_train_lda, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = logistic_regression.predict(X_test_lda)  # 預測.predict
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


plot_decision_regions(X_test_lda, y_test, classifier=logistic_regression)
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

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

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


wine = datasets.load_wine()

feature_names = wine.feature_names
X, y = wine.data, wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

import json

clf = DecisionTreeClassifier()
output = clf.fit(X_train, y_train)
print(json.dumps(output, indent=4))

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 30.56%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹")

wine = datasets.load_wine()

feature_names = wine.feature_names
X, y = wine.data, wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()  # criterion='entropy')
clf.fit(X_train, y_train)

# DecisionTreeClassifier()

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
    class_names=wine.target_names,
    feature_names=wine.feature_names,
    out_file=None,
)
graph = graph_from_dot_data(dot_data)
# graph.write_png('tmp_wine_tree.png')  NG

# dot 格式存檔

dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=wine.target_names,
    feature_names=wine.feature_names,
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

print("隨機森林")

wine = datasets.load_wine()

feature_names = wine.feature_names
X, y = wine.data, wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)

# RandomForestClassifier(n_estimators=50)

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
