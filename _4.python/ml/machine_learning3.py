"""
機器學習入門


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

"""
01.讀入基本套件

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數
f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk), 我們想知道這
f(x)=y,其中的 y 就是某一個類別。

這種學函數的方法, 又可以分為:

    supervised learning
    unsupervised learning

其中的 supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。而 unsupervised learning 就神了, 我們不知道答案, 卻要電腦自己去學!

做數據分析, 幾乎每一次都要讀入這些套件!
"""

# 02. 關於 overfitting

plt.figure(figsize=(12, 8))

x = np.linspace(0, 1, 20)
y = -((x - 1) ** 2) + 1

plt.subplot(211)
X = np.linspace(0, 1, 20)
Y = -((X - 1) ** 2) + 1 + 0.08 * np.random.randn(20)
plt.scatter(X, Y, c="r", s=50)
plt.plot(x, y)
plt.grid()
plt.title("aaaa")

plt.subplot(212)
z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x), "r")
plt.scatter(X, Y, c="r", s=50)
plt.plot(x, y)
plt.ylim(0, 2)
plt.grid()
plt.title("這叫很低的 bias, 很高的 variance")

plt.show()

print("------------------------------------------------------------")  # 60個

"""
03. 迴歸法預測函數
03-1. 假的數據真的迴歸
做一條直線

我們來一條線, 比如說 f(x) = 1.2x + 0.8 + noise
"""

N = 50
x = np.linspace(0, 1, N)
y = 1.2 * x + 0.8 + 0.2 * np.random.randn(N)

plt.scatter(x, y)

plt.grid()
plt.title("aaaa")

plt.show()


"""
分訓練資料、測試資料

一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」,
就是不讓電腦在計算時「看到」這些測試資料。
等函數學成了以後, 再來測試準不準確。這是我們可以用

sklearn.model_selection 裡的 train_test_split

來亂數選一定百分比的資料來用。
"""
from sklearn.model_selection import train_test_split

# 把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=9487
)

# len(x_train)    #80%
# len(x_test)     #20%

"""
【重點】注意輸入格式
只有一個 feature 時, 我們要小心的是, 很多機器學習、深度學習的套件, 都不希望我們用
x=[x1,x2,…,xn]
這樣子去做, 而是希望變成
x=[[x1],[x2],…,[xn]]
這種形式!
"""

xx = np.array([3, 9, 8, 1, 2])
yy = np.array([1, 3, 9, 2, 4])

"""
xx.shape
xx.reshape(5,1)
xx = xx.reshape(len(xx),1)
"""

# 正式轉我們的訓練資料

x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# step 1. 開一台「線性迴歸機」

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

# step 2. fit 學習、訓練

regr.fit(x_train, y_train)

# step 3. predict 預測

Ypred = regr.predict(x_test)

# x: x_test
# y: Ypred
# x_test.ravel()

plt.plot(x_test.ravel(), Ypred, "r")

plt.scatter(x_test.ravel(), y_test)

plt.grid()
plt.title("aaaa")
plt.show()


# 計算分數
from sklearn.metrics import mean_squared_error, r2_score

mse_t = mean_squared_error(y_train, regr.predict(x_train))
r2_t = r2_score(y_train, regr.predict(x_train))
print("訓練資料")
print("MSE =", mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, Ypred)
r2 = r2_score(y_test, Ypred)
print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
在金融預測上的應用

神經網路
連 SVM 都沒辦法, 那一定是方法還不夠高級, 所以我們用更高級的神經網路來做做看!
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

# [2] 打造我們的神經網路函數學習機

model = Sequential()
model.add(Dense(20, input_dim=5))
model.add(Activation("relu"))
model.add(Dense(20))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 看一下我們神經網路長什麼樣子, 有沒有做錯。

model.summary()

""" TBD
#[3] 訓練

model.fit(x_train, yb_train, batch_size=100, epochs=20)


#[4] 預測

#看起來不太妙, 我們來試試預測...

NN_pred = model.predict_classes(x_test)

YP_NN = yb_test[(NN_pred==1).ravel()]

len(YP_NN)

458

len(YP_NN[YP_NN == 1])

246

246/458

0.537117903930131

結果真是慘慘慘, 怎麼會這樣呢?

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
13.畫我們練習成果的討論
"""

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
plt.show()

# 雖然看來我們用了比較多白痴的方法做出一樣的事, 不過一些技巧之後也可以常常使用。
# 1.3 快速換個配色

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.show()


plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.prism, alpha=0.8)
plt.show()


# 1.4 取回鳶尾花訓練資料

from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data[:, :2]

y = iris.target

# 我們來畫畫比較。

plt.subplot(121)

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.subplot(122)

plt.scatter(x[:, 0], x[:, 1], s=50, c=clf.predict(x))

plt.show()

# 左邊的是訓練資料, 右邊是用我們 SVM 分類器分出來的。你有看出差異嗎? 是不是很難看出? 我們來用用另一個方式。

# 1.5 畫圖的另一個方式

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.02), np.arange(1.5, 5.0, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.show()


Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap=plt.cm.coolwarm)
plt.show()

print("------------------------------------------------------------")  # 60個

# 打開一個線性迴歸的函數學習機

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

# 造資料, 調整成 sklearn 會接受的形狀

x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

X = x.reshape(len(x), 1)

# 把資料放進函數學習機，開始它的訓練

regr.fit(X, y)

# 用 predict 看一下訓練的成果，順便畫個圖

Y = regr.predict(X)

plt.scatter(x, y)
plt.plot(x, Y, "r")
plt.show()

# 結果看起來不錯，會有微小誤差的原因，則是因為真實世界的資料有不可避免的雜訊

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 均勻地在 0 到 5 之間取一百個點，再隨便決定一個函數，叫做 y = f(x) = 1.9x + 0.8 好了
# 為了增加真實感，加上一點雜訊

x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

# 開開心心地讓 sklearn 幫我們分離出訓練資料跟測試資料，測試資料的比例是 0.3 的話，
# 訓練資料就會自動是 0.7 了呢，真是方便！
# random_state 可以是耍寶用的 87 ，要選其他數字也當然可以

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=87
)
x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# 一樣叫出一個線性迴歸的函數學習機，再放進「訓練資料」讓它開始訓練

regr = LinearRegression()
regr.fit(x_train, y_train)

# 用 plot 把「訓練資料」的正確答案畫成一條線，再把模型 predict 出來的結果描點畫在同一張圖上
# 可以清楚的看到結果

plt.scatter(x_train, y_train)
plt.plot(x_train, regr.predict(x_train), "r")
plt.show()


# 跟上面一樣的做法，只是這次對象換成「測試資料」

plt.scatter(x_test, y_test)
plt.plot(x_test, regr.predict(x_test), "r")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import neighbors

X = pd.DataFrame({
   "耐酸性": [7, 7, 3, 1],
   "強度":   [7, 4, 4, 4]
})

y = np.array([0, 0, 1, 1])
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = pd.DataFrame(np.array([[3, 7]]),
                          columns=["耐酸性", "強度"])
pred = knn.predict(new_tissue)
print(pred)

print("------------------------------------------------------------")  # 60個

from sklearn import cluster

df = pd.DataFrame({
   "length": [51, 46, 51, 45, 51, 50, 33,
              38, 37, 33, 33, 21, 23, 24],
   "weight": [10.2, 8.8, 8.1, 7.7, 9.8, 7.2, 4.8,
              4.6, 3.5, 3.3, 4.3, 2.0, 1.0, 2.0]
})
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(df)
print(kmeans.labels_)

colmap = np.array(["r", "g", "y"])
plt.scatter(df["length"], df["weight"], color=colmap[kmeans.labels_])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 安裝 auto-sklearn fail
print('Auto-Sklearn')

#pip install auto-sklearn
import autosklearn.classification
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')
  
data = sm.datasets.anes96.load_pandas().data
label = 'vote'
features = [i for i in data.columns if i != label]
X_train = data[features]
y_train = data[label]
automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120, per_run_time_limit=120, # 兩分鐘
    include_estimators=["random_forest"])
automl.fit(X_train, y_train)
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

""" 一些 fail
print('Auto-Keras')

from keras.datasets import mnist
from autokeras import ImageClassifier
from autokeras.constant import Constant
import autokeras
from keras.utils import plot_model
    
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))
clf = ImageClassifier(verbose=True, augment=False)
clf.fit(x_train, y_train, time_limit=500 * 60)
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
y = clf.evaluate(x_test, y_test)
print(y * 100)
clf.export_keras_model('model.h5')
plot_model(clf, to_file='model.png')
"""

print("------------------------------------------------------------")  # 60個

# 數據集和數據處理

from pandas import Series, DataFrame

# 繪圖分析
sns.set_style("whitegrid")

# 機器學習
from sklearn.linear_model import LogisticRegression  # 邏輯迴歸
from sklearn.svm import SVC, LinearSVC  # 支持向量機
from sklearn.ensemble import RandomForestClassifier  # 隨機森林

# from sklearn.neighbors import KneighborsClassifier # K近鄰
from sklearn.naive_bayes import GaussianNB  # 數據集和數據處理

print("------------------------------------------------------------")  # 60個

titanic_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.describe())

print("------------------------------------------------------------")  # 60個

facet = sns.FacetGrid(titanic_df, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, titanic_df["Age"].max()))
facet.add_legend()
plt.show()

fig, axis1 = plt.subplots(1, 1, figsize=(18, 4))
average_age = titanic_df[["Age", "Survived"]].groupby(["Age"], as_index=False).mean()
sns.barplot(x="Age", y="Survived", data=average_age)
plt.show()


print("------------------------------------------------------------")  # 60個


def get_person(passenger):  # 小於16歲的分類爲兒童
    age, sex = passenger
    return "child" if age < 16 else sex


def conv(df):
    df["Person"] = df[["Age", "Sex"]].apply(get_person, axis=1)  # 組合特徵
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())  # 缺失值填充爲均值
    df["Embarked"] = df["Embarked"].fillna("S")  # 缺失值填充爲S
    df["Fare"] = df["Fare"].astype(int)  # 類型轉換

    person_dummies = pd.get_dummies(df["Person"])  # onehot編碼
    person_dummies.columns = ["Child", "Female", "Male"]
    df = df.join(person_dummies)  # 連接原數據與onehot數據
    df = df.drop(
        ["PassengerId", "Name", "Ticket", "Person", "Sex", "Embarked", "Cabin", "Age"],
        axis=1,
    )  # 刪除非數據型特徵
    return df


titanic_df = conv(titanic_df)
test_df = conv(test_df)

print("------------------------------------------------------------")  # 60個

# 生成模型所需的訓練集和測試集
X_train = titanic_df.drop("Survived", axis=1)
Y_train = titanic_df["Survived"]
X_test = test_df.copy()

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()  # 初始化模型
logreg.fit(X_train, Y_train)  # 訓練模型
print(logreg.score(X_train, Y_train))  # 模型評分
Y_pred = logreg.predict(X_test)  # 預測

print("------------------------------------------------------------")  # 60個

"""
實際數據請從天池競賽平臺下載
https://tianchi.aliyun.com/competition/gameList/activeList
https://tianchi.aliyun.com/competition/activeList
"""

import datetime
from pandas.api.types import is_numeric_dtype  # 用於判斷特徵類型
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  # 分類模型
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor  # 迴歸模型
from sklearn.model_selection import cross_val_score, train_test_split  # 切分數據集
from sklearn.metrics import mean_squared_error  # 評價函數

"""
無csv資料
data = pd.read_csv('data/happiness_train_min.csv', encoding='gb2312')

test = pd.read_csv('data/happiness_test_min.csv', encoding='gb2312')

print(data.columns.tolist()) # 查看所有特徵
print(data.dtypes) # 查看各特徵類型

print('------------------------------------------------------------')	#60個

# 特徵工程

features = []
label = 'happiness' # 目標變量

for col in data.columns:
    if not is_numeric_dtype(data[col]): # 非數值型特徵
        print(col, data[col].dtype)
        print(data[col].unique()[:5])
    elif col != label and col != 'id': # 加入可直接代入模型的特徵
        features.append(col)
        
x = data[features] # 自變量
y = data[label] # 目標變量
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, random_state=0)
x_train = x_train.fillna(x.mean()) # 空值填充訓練集
x_val = x_val.fillna(x.mean()) # 空值填充驗證集
x_test = test.fillna(x.mean()) # 空值填充測試集
x = x.fillna(x.mean()) # 空值填充全集


print('------------------------------------------------------------')	#60個

# 訓練模型生成提交數據

#clf = RandomForestRegressor(criterion='mse', random_state=0) # 隨機森林迴歸
#clf = GradientBoostingClassifier(criterion='mse',random_state=0) # GBDT分類
clf = GradientBoostingRegressor(criterion='mse', random_state=0) # GBDT迴歸

if True: # 用於本地測試
    clf.fit(x_train, y_train)
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val)])
    print("MSE: %.4f" % mse)
else: # 用於遠程提交
    clf.fit(x, y) # 全量數據訓練
    df = pd.DataFrame()
    df['id'] = test.id
    df['happiness'] = clf.predict(x_test[features])
    df.to_csv('out/submit_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),index=False)

print('------------------------------------------------------------')	#60個

import datetime
from pandas.api.types import is_numeric_dtype # 用於判斷特徵類型
from sklearn.model_selection import cross_val_score, train_test_split # 切分數據集
from sklearn.metrics import mean_squared_error # 評價函數

data = pd.read_csv('data/happiness_train_min.csv', encoding='gb2312')
test = pd.read_csv('data/happiness_test_min.csv', encoding='gb2312')

print('------------------------------------------------------------')	#60個

# 特徵工程

def get_mean(fea, data, test): # 同時變換訓練集和測試集
    arr1 = data[fea].unique()
    arr2 = test[fea].unique()
    arr3 = list(arr1)
    arr3.extend(arr2) # 有的數據只出現在訓練集或測試集中
    arr4 = list(set(arr3))
    dic = {}
    for x in arr4:
        dic[x] = data[data[fea] == x][label].mean() # 取其因變量均值
    data[fea] = data[fea].apply(lambda x: dic[x]) # 數據替換
    test[fea] = test[fea].apply(lambda x: dic[x])
    return data,test

label = 'happiness' # 目標變量
features = []

data, test = get_mean('city', data, test)
data, test = get_mean('invest_other', data, test)
data, test = get_mean('province', data, test)

for col in data.columns:
    if not is_numeric_dtype(data[col]): # 非數值型特徵
        continue
    elif col != label and col != 'id' and col not in ['public_service_7']: # 去掉干擾特徵
        features.append(col)
        data[col] = data[col].apply(lambda x: np.nan if x < 0 else x) # 優化點一
        test[col] = test[col].apply(lambda x: np.nan if x < 0 else x)

data_all = pd.concat([data,test]) # 優化點二
data = data[data['happiness'] > 0] # 去掉因變量缺失的數據
x = data[features] # 自變量
y = data[label] # 目標變量
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, random_state=0)
x_train = x_train.fillna(data_all[features].mean()) # 空值填充訓練集
x_val = x_val.fillna(data_all[features].mean()) # 空值填充驗證集
x_test = test.fillna(data_all[features].mean()) # 空值填充測試集
x = x.fillna(data_all[features].mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型

import xgboost as xgb
from sklearn.cross_validation import KFold

def my_eval(preds, train): # 自定義評價函數
    score = mean_squared_error(train.get_label(), preds)
    return 'myeval', score

my_params = {"booster":'gbtree','eta': 0.005, 'max_depth': 6, 'subsample': 0.7, 
              'colsample_bytree': 0.8, 'objective': 'reg:linear', 'eval_metric': 'rmse', 
              'silent': True, 'nthread': 4} # 模型參數

train_preds = np.zeros(len(data)) # 用於保存預測結果
test_preds = np.zeros(len(test))
kf = KFold(len(data), n_folds = 5, shuffle=True, random_state=0) # 5折交叉驗證
for fold, (trn_idx, val_idx) in enumerate(kf):
    print("fold {}".format(fold+1))
    train_data = xgb.DMatrix(data[features].iloc[trn_idx], data[label].iloc[trn_idx]) # 訓練集
    val_data = xgb.DMatrix(data[features].iloc[val_idx], data[label].iloc[val_idx]) # 驗證集
    watchlist = [(train_data, 'train'), (val_data, 'valid_data')]
    clf = xgb.train(dtrain=train_data, num_boost_round=5000, evals=watchlist, 
               early_stopping_rounds=200, verbose_eval=100, 
               params=my_params,feval = my_eval)
    train_preds[val_idx] = clf.predict(xgb.DMatrix(data[features].iloc[val_idx]),
               ntree_limit=clf.best_ntree_limit)
    test_preds += clf.predict(xgb.DMatrix(test[features]), 
               ntree_limit=clf.best_ntree_limit) / kf.n_folds
print("CV score: {:<8.8f}".format(mean_squared_error(train_preds, data[label])))

df = pd.DataFrame() # 生成提交結果
df['id'] = test.id
df['happiness'] = test_preds
df.to_csv('out/submit_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),index=False)

print('------------------------------------------------------------')	#60個

fig,ax = plt.subplots()
fig.set_size_inches(40,6)
xgb.plot_tree(clf, ax=ax, num_trees=0) # 顯示模型中的第一棵樹
plt.savefig('tmp.png',dpi=300)

print('------------------------------------------------------------')	#60個

# 檢測干擾變量

from sklearn.ensemble import GradientBoostingRegressor

baseline = 0.4887 # 誤差baseline
for i in features:
    features_new = [x for x in features if x != i]
    clf = GradientBoostingRegressor(criterion='mse', random_state=0)
    clf.fit(x_train[features_new], y_train)
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val[features_new])])
    if mse < baseline:
        print("remove", i, "MSE: %.4f" % mse)

"""
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
