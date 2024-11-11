"""
pip install scikit-learn

"""

import sklearn

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

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

from sklearn import datasets, svm, metrics

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
""" no clf
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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import neighbors

X = pd.DataFrame({"耐酸性": [7, 7, 3, 1], "強度": [7, 4, 4, 4]})

y = np.array([0, 0, 1, 1])
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = pd.DataFrame(np.array([[3, 7]]), columns=["耐酸性", "強度"])
pred = knn.predict(new_tissue)
print(pred)

print("------------------------------------------------------------")  # 60個

from sklearn import cluster

df = pd.DataFrame(
    {
        "length": [51, 46, 51, 45, 51, 50, 33, 38, 37, 33, 33, 21, 23, 24],
        "weight": [
            10.2,
            8.8,
            8.1,
            7.7,
            9.8,
            7.2,
            4.8,
            4.6,
            3.5,
            3.3,
            4.3,
            2.0,
            1.0,
            2.0,
        ],
    }
)
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

# 1. Rescale Data
# 將資料比例縮放到0與1之間# Rescale data (between 0 and 1)

import scipy
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 2. Standardize Data
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 3. Normalize Data
# 最大值變為1，最小值變為0

from sklearn.preprocessing import Normalizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(normalizedX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 4. Binarize Data (Make Binary)
# 資料二元化(0或者1)

from sklearn.preprocessing import Binarizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(binaryX[0:5, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer


def similarity_tfidf(s1, s2):
    def add_space(s):
        return " ".join(list(s))

    s1, s2 = add_space(s1), add_space(s2)

    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()

    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


string1 = "漢堡蛋"
string2 = "我要一份漢堡蛋"
# string2 = '請給我來一份漢堡蛋'
# string2 = '你是一個漢堡蛋嗎?'

result = similarity_tfidf(string1, string2)

print("相似度 : ", result)
if result > 0.2:
    print("OK, 一個漢堡蛋")
else:
    print("Sorry, 無法接受訂餐")

print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
iris.head()

sns.set()
sns.pairplot(iris, hue="species", height=3)

print(iris)
print("cccc")

print("------------------------------------------------------------")  # 60個

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"

tips = sns.load_dataset("tips")
print(tips)

print("------------------------------------------------------------")  # 60個

# 怎麼選最好參數、model？
# 製造像真的一様的數據

# from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=500, centers=3, n_features=2, random_state=0)
plt.scatter(x[:, 0], x[:, 1], c=y)

# plt.show()

print("------------------------------------------------------------")  # 60個

# Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

clf = SVC()
# clf = SVC(gamma = 'scale')

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

# 試用 Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

# 試用 Random Forest

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

x, y = datasets.make_regression(n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
plt.legend()

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習")

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="*", color="red")
plt.title("無監督學習")

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=5)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=0)
print(data)
print(label)
print(f"分類 : {label}")

plt.scatter(data[:, 0], data[:, 1], c=label, cmap="bwr")
plt.grid(True)

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=0)

print(data)
print(label)
print(f"分類 : {label}")

plt.subplot(121)
plt.scatter(data[:, 0], data[:, 1], c=label, cmap="bwr")

d_sta = StandardScaler().fit_transform(data)  # 標準化
print(d_sta)

plt.subplot(122)
plt.scatter(d_sta[:, 0], d_sta[:, 1], c=label, cmap="bwr")
plt.grid(True)

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)

print(f"特徵數據外形 : {d_sta.shape}")
print(f"訓練數據外形 : {dx_train.shape}")
print(f"測試數據外形 : {dx_test.shape}")
print(f"標籤數據外形 : {label.shape}")
print(f"訓練數據外形 : {label_train.shape}")
print(f"測試數據外形 : {label_test.shape}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
k_model = KNeighborsClassifier(n_neighbors=5)  # k = 5
# 建立訓練數據模型
k_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = k_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {k_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {k_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
svm_model = LinearSVC()
# 建立訓練數據模型
svm_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = svm_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {svm_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

data, label = make_moons(n_samples=200, noise=0.2, random_state=0)

d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm_model = LinearSVC()
svm_model.fit(dx_train, label_train)
pred = svm_model.predict(dx_test)
# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print("=" * 50)
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)
# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

data, label = datasets.load_iris(return_X_y=True)
print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=0
)
# 建立分類模型
tree_model = DecisionTreeClassifier()
# 建立訓練數據模型
tree_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = tree_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {tree_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {tree_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=0
)
# 建立分類模型
forest_model = RandomForestClassifier()
# 建立訓練數據模型
forest_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = forest_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {forest_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {forest_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習", fontsize=16)

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="*", color="red")
plt.title("無監督學習", fontsize=16)

# plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

df = pd.read_csv("data/iris.csv")

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:4].astype(float)
Y = to_categorical(dataset[:, 4])

X = StandardScaler().fit_transform(X)  # 標準化

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

print(model.summary())

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=100, batch_size=5)

loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

# Y_pred = model.predict_classes(X_test)
Y_pred = model.predict_step(X_test)
print(Y_pred)

Y_target = dataset[:, 4][120:].astype(int)
print(Y_target)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("迴歸效果評估")

print("MSE均方誤差")

from sklearn.metrics import mean_squared_error

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_squared_error(y_true, y_pred))

print("MAE平均絕對誤差")
from sklearn.metrics import mean_absolute_error

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_absolute_error(y_true, y_pred))

print("R-Squared擬合度")
from sklearn.metrics import r2_score

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(r2_score(y_true, y_pred))

print("------------------------------------------------------------")  # 60個

print("分類效果評估")
print("FP/FN/TP/TN")

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)

print("準確率")
from sklearn.metrics import accuracy_score

print(accuracy_score(y_real, y_pred))

print("召回率")
from sklearn.metrics import recall_score

print(recall_score(y_real, y_pred))

print("精度")
from sklearn.metrics import precision_score

print(precision_score(y_real, y_pred))

print("F值")

from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2))  # 計算fn

print("Logloss")
from sklearn.metrics import log_loss

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real, y_score))

print("ROC曲線和AUC")
from sklearn.metrics import roc_auc_score, roc_curve

print(roc_auc_score(y_real, y_score))  # AUC值

fpr, tpr, thresholds = roc_curve(y_real, y_score)
plt.plot(fpr, tpr)  # 繪圖

# plt.show()

# P-R曲線
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_real, y_score)
plt.plot(recall, precision)

# plt.show()

print("------------------------------------------------------------")  # 60個

print("多指標評分")

from sklearn.metrics import classification_report

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print("------------------------------------------------------------")  # 60個

print("聚類算法")

from sklearn.datasets import make_blobs  # 數據支持
from sklearn.cluster import KMeans  # 聚類方法

X, y = make_blobs(n_samples=100, random_state=150)
y_pred = KMeans(n_clusters=3, random_state=5).fit_predict(X)  # 訓練
plt.scatter(X[:, 0], X[:, 1], c=y_pred)

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())

print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())

df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

# plt.show()

print("------------------------------")  # 30個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())

print("------------------------------")  # 30個

scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std, columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_std.head())

df_std.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())
print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())
df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

print("------------------------------")  # 30個

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax, columns=["最小最大值縮放FB追蹤數", "最小最大值縮放快樂程度"])
print(df_minmax.head())

df_minmax.plot(kind="scatter", x="最小最大值縮放FB追蹤數", y="最小最大值縮放快樂程度")

# plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

df = pd.read_csv("data/test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個

# How do I use pandas with scikit-learn to create Kaggle submissions? (video)

# 讀取[Kaggle's Titanic competition]資料集至df
# train = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
train = pd.read_csv(filename)

print("檢視前幾行")
cc = train.head()
print(cc)

# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ["Pclass", "Parch"]
X = train.loc[:, feature_cols]

print("X之大小")
cc = X.shape
print(cc)

# create a response vector 'y' by selecting a Series
y = train.Survived
print("y之大小")
cc = y.shape
print(cc)

# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, y)

# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv("http://bit.ly/kaggletest")
print("檢視前幾行")
cc = test.head()
print(cc)

# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
print("X_new之大小")
cc = X_new.shape
print(cc)

# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)

# create a DataFrame of passenger IDs and testing set predictions
print("檢視前幾行")
cc = pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).head()
print(cc)

# ensure that PassengerID is the first column by setting it as the index
print("檢視前幾行")
cc = (
    pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class})
    .set_index("PassengerId")
    .head()
)
print(cc)

print("df轉csv")
pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).set_index(
    "PassengerId"
).to_csv("tmp_sub.csv")

print("df轉pickle")
train.to_pickle("tmp_train.pkl")

print("pickle轉df")
print("檢視前幾行")
cc = pd.read_pickle("tmp_train.pkl").head()
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data[:, :2], iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

# Standardize the features using StandardScaler
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Create a K-Nearest Neighbors classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Predict the target values on the test data
y_pred = knn.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)

# Accuracy: 0.631578947368421

print("------------------------------------------------------------")  # 60個

# Loading The Data

from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data, iris.target

# Print the lengths of X and y
print("Size of X:", X.shape)  #  (150, 4)
print("Size of y:", y.shape)  #  (150, )

print("------------------------------------------------------------")  # 60個

# Training And Test Data

# Import train_test_split from sklearn
from sklearn.model_selection import train_test_split

# Split the data into training and test sets with test_size=0.2 (20% for test set)
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Print the sizes of the arrays
print("Size of X_train:", X_train.shape)
print("Size of X_test: ", X_test.shape)
print("Size of y_train:", y_train.shape)
print("Size of y_test: ", y_test.shape)

print("------------------------------------------------------------")  # 60個

# Create instances of the models

# Import necessary classes from sklearn libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Create instances of supervised learning models
# Logistic Regression classifier (max_iter=1000)
lr = LogisticRegression(max_iter=1000)

# k-Nearest Neighbors classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)

# Support Vector Machine classifier
svc = SVC()

# Create instances of unsupervised learning models
# k-Means clustering with 3 clusters and 10 initialization attempts
k_means = KMeans(n_clusters=3, n_init=10)

# Principal Component Analysis with 2 components
pca = PCA(n_components=2)

print("------------------------------------------------------------")  # 60個

# Model Fitting

# Fit models to the data
lr.fit(X_train, y_train)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
k_means.fit(X_train)
pca.fit_transform(X_train)

# Print the instances and models
print("lr:", lr)
print("knn:", knn)
print("svc:", svc)
print("k_means:", k_means)
print("pca:", pca)

print("------------------------------------------------------------")  # 60個

# Prediction

# Predict using different supervised estimators
y_pred_svc = svc.predict(X_test)
y_pred_lr = lr.predict(X_test)
y_pred_knn_proba = knn.predict_proba(X_test)

# Predict labels using KMeans in clustering algorithms
y_pred_kmeans = k_means.predict(X_test)

# Print the results
print("Supervised Estimators:")
print("SVC predictions:", y_pred_svc)
print("Logistic Regression predictions:", y_pred_lr)
print("KNeighborsClassifier probabilities:\n", y_pred_knn_proba[:5], "\n     ...")

print("\nUnsupervised Estimators:")
print("KMeans predictions:", y_pred_kmeans)

print("------------------------------------------------------------")  # 60個

# Preprocessing The Data
# Standardization

from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler and fit it to training data
scaler = StandardScaler().fit(X_train)

# Transform the training and test data using the scaler
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

# Print the variables
print("\nStandardized X_train:\n", standardized_X[:5], "\n     ...")
print("\nStandardized X_test:\n", standardized_X_test[:5], "\n     ...")

# Normalization

from sklearn.preprocessing import Normalizer

scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

# Print the variables
print("\nNormalized X_train:\n", normalized_X[:5], "\n     ...")
print("\nNormalized X_test:\n", normalized_X_test[:5], "\n     ...")

# Binarization

import numpy as np
from sklearn.preprocessing import Binarizer

# Create a sample data array
data = np.array([[1.5, 2.7, 0.8], [0.2, 3.9, 1.2], [4.1, 1.0, 2.5]])

# Create a Binarizer instance with a threshold of 2.0
binarizer = Binarizer(threshold=2.0)

# Apply binarization to the data
binarized_data = binarizer.transform(data)

print("Original data:")
print(data)
print("\nBinarized data:")
print(binarized_data)

# Encoding Categorical Features

from sklearn.preprocessing import LabelEncoder

# Sample data: categorical labels
labels = ["cat", "dog", "dog", "fish", "cat", "dog", "fish"]

# Create a LabelEncoder instance
label_encoder = LabelEncoder()

# Fit and transform the labels
encoded_labels = label_encoder.fit_transform(labels)

# Print the original labels and their encoded versions
print("Original labels:", labels)
print("Encoded labels:", encoded_labels)

# Decode the encoded labels back to the original labels
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("Decoded labels:", decoded_labels)

print("------------------------------------------------------------")  # 60個

# Imputing Missing Values

import numpy as np
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0], [7.0, 8.0, 9.0]])

# Create a SimpleImputer instance with strategy='mean'
imputer = SimpleImputer(strategy="mean")

# Fit and transform the imputer on the data
imputed_data = imputer.fit_transform(data)

print("Original data:")
print(data)
print("\nImputed data:")
print(imputed_data)

print("------------------------------------------------------------")  # 60個

# Generating Polynomial Features

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6]])

# Create a PolynomialFeatures instance of degree 2
poly = PolynomialFeatures(degree=2)

# Transform the data to include polynomial features
poly_data = poly.fit_transform(data)

print("Original data:")
print(data)
print("\nPolynomial features:")
print(poly_data)

print("------------------------------------------------------------")  # 60個

# Classification Metrics

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Accuracy Score
accuracy_knn = knn.score(X_test, y_test)
print("Accuracy Score (knn):", knn.score(X_test, y_test))

accuracy_y_pred = accuracy_score(y_test, y_pred_lr)
print("Accuracy Score (y_pred):", accuracy_y_pred)

# Classification Report
classification_rep_y_pred = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred):\n", classification_rep_y_pred)

classification_rep_y_pred_lr = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred_lr):\n", classification_rep_y_pred_lr)

# Confusion Matrix
conf_matrix_y_pred_lr = confusion_matrix(y_test, y_pred_lr)
print("Confusion Matrix (y_pred_lr):\n", conf_matrix_y_pred_lr)

print("------------------------------------------------------------")  # 60個

# Regression Metrics

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# True values (ground truth)
y_true = [3, -0.5, 2]

# Predicted values
y_pred = [2.8, -0.3, 1.8]

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)

# Calculate Mean Squared Error
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)

# Calculate R² Score
r2 = r2_score(y_true, y_pred)
print("R² Score:", r2)

print("------------------------------------------------------------")  # 60個

# Clustering Metrics

from sklearn.metrics import adjusted_rand_score, homogeneity_score, v_measure_score

# Adjusted Rand Index
adjusted_rand_index = adjusted_rand_score(y_test, y_pred_kmeans)
print("Adjusted Rand Index:", adjusted_rand_index)

# Homogeneity Score
homogeneity = homogeneity_score(y_test, y_pred_kmeans)
print("Homogeneity Score:", homogeneity)

# V-Measure Score
v_measure = v_measure_score(y_test, y_pred_kmeans)
print("V-Measure Score:", v_measure)

print("------------------------------------------------------------")  # 60個

# Cross-Validation

# Import necessary library
from sklearn.model_selection import cross_val_score

# Cross-validation with KNN estimator
knn_scores = cross_val_score(knn, X_train, y_train, cv=4)
print(knn_scores)

# Cross-validation with Linear Regression estimator
lr_scores = cross_val_score(lr, X, y, cv=2)
print(lr_scores)

# Grid Search

# Import necessary library
from sklearn.model_selection import GridSearchCV

# Define parameter grid
params = {"n_neighbors": np.arange(1, 3), "weights": ["uniform", "distance"]}

# Create GridSearchCV object
grid = GridSearchCV(estimator=knn, param_grid=params)

# Fit the grid to the data
grid.fit(X_train, y_train)

# Print the best parameters found
print("Best parameters:", grid.best_params_)

# Print the best cross-validation score
print("Best cross-validation score:", grid.best_score_)

# Print the accuracy on the test set using the best parameters
best_knn = grid.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)
print("Test set accuracy:", test_accuracy)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(0, 1, N)
y = np.sqrt(X) + 0.2 * np.random.rand(N) - 0.1

X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


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


print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    ylim=None,
    cv=None,
    n_jobs=1,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
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


# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
titles = [
    "Learning Curves (Under Fitting)",
    "Learning Curves",
    "Learning Curves (Over Fitting)",
]
degrees = [1, 3, 10]

plt.figure(figsize=(18, 4))
for i in range(len(degrees)):
    plt.subplot(1, 3, i + 1)
    plot_learning_curve(
        polynomial_model(degrees[i]), titles[i], X, y, ylim=(0.75, 1.01), cv=cv
    )

plt.show()

print("------------------------------------------------------------")  # 60個

# from sklearn.datasets.samples_generator import make_blobs    old
from sklearn.datasets import make_blobs

# 生成數據
centers = [[-2, 2], [2, 2], [0, 4]]
X, y = make_blobs(n_samples=60, centers=centers, random_state=0, cluster_std=0.60)

# 畫出數據
plt.figure(figsize=(12, 8))
c = np.array(centers)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 畫出樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="orange")  # 畫出中心點

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.neighbors import KNeighborsClassifier

# 模型訓練
k = 5
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X, y)

# 進行預測
X_sample = [0, 2]
X_sample = np.array(X_sample).reshape(1, -1)
y_sample = clf.predict(X_sample)
neighbors = clf.kneighbors(X_sample, return_distance=False)

# 畫出示意圖
plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="k")  # 中心點
plt.scatter(X_sample[0][0], X_sample[0][1], marker="x", s=100, cmap="cool")  # 待預測的點

for i in neighbors[0]:
    # 預測點與距離最近的 5 個樣本的連線
    plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], "k--", linewidth=0.6)

plt.show()

print("------------------------------------------------------------")  # 60個

# 生成訓練樣本
N = 40
X = 5 * np.random.rand(N, 1)
y = np.cos(X).ravel()

# 添加一些噪聲
y += 0.2 * np.random.rand(N) - 0.1

# 訓練模型
from sklearn.neighbors import KNeighborsRegressor

k = 5
knn = KNeighborsRegressor(k)
knn.fit(X, y)

# 生成足夠密集的點并進行預測
T = np.linspace(0, 5, 500)[:, np.newaxis]
y_pred = knn.predict(T)
print(knn.score(X, y))

# 畫出擬合曲線
plt.figure(figsize=(12, 8))
plt.scatter(X, y, c="g", label="data", s=100)  # 畫出訓練樣本
plt.plot(T, y_pred, c="k", label="prediction", lw=4)  # 畫出擬合曲線
plt.axis("tight")
plt.title("KNeighborsRegressor (k = %i)" % k)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 加載數據
data = pd.read_csv("datasets/pima-indians-diabetes/diabetes.csv")
print("dataset shape {}".format(data.shape))

print(data.head())

print(data.groupby("Outcome").size())

X = data.iloc[:, 0:8]
Y = data.iloc[:, 8]
print("shape of X {}; shape of Y {}".format(X.shape, Y.shape))

print("------------------------------")  # 30個

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier

models = []
models.append(("KNN", KNeighborsClassifier(n_neighbors=2)))
models.append(
    ("KNN with weights", KNeighborsClassifier(n_neighbors=2, weights="distance"))
)
models.append(
    (
        "Radius Neighbors",
        RadiusNeighborsClassifier(
            #    n_neighbors=2, radius=500.0)))
            radius=500.0
        ),
    )
)

results = []
for name, model in models:
    model.fit(X_train, Y_train)
    results.append((name, model.score(X_test, Y_test)))
for i in range(len(results)):
    print("name: {}; score: {}".format(results[i][0], results[i][1]))

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

print("------------------------------")  # 30個

# 模型訓練

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, Y_train)
train_score = knn.score(X_train, Y_train)
test_score = knn.score(X_test, Y_test)
print("train score: {}; test score: {}".format(train_score, test_score))

from sklearn.model_selection import ShuffleSplit
from common.utils import plot_learning_curve

knn = KNeighborsClassifier(n_neighbors=2)
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
plt.figure(figsize=(10, 6))
plot_learning_curve(
    plt, knn, "Learn Curve for KNN Diabetes", X, Y, ylim=(0.0, 1.01), cv=cv
)

plt.show()

print("------------------------------")  # 30個

# 數據可視化

from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=2)
X_new = selector.fit_transform(X, Y)
print(X_new[0:5])

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X_new, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

# 畫出數據
plt.figure(figsize=(10, 6))
plt.ylabel("BMI")
plt.xlabel("Glucose")
plt.scatter(X_new[Y == 0][:, 0], X_new[Y == 0][:, 1], c="r", s=20, marker="o")  # 畫出樣本
plt.scatter(X_new[Y == 1][:, 0], X_new[Y == 1][:, 1], c="g", s=20, marker="^")  # 畫出樣本

plt.show()

print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(-2 * np.pi, 2 * np.pi, N)
Y = np.sin(X) + 0.2 * np.random.rand(N) - 0.1
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


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


from sklearn.metrics import mean_squared_error

degrees = [2, 3, 5, 10]
results = []
for d in degrees:
    model = polynomial_model(degree=d)
    model.fit(X, Y)
    train_score = model.score(X, Y)
    mse = mean_squared_error(Y, model.predict(X))
    results.append({"model": model, "degree": d, "score": train_score, "mse": mse})
for r in results:
    print(
        "degree: {}; train score: {}; mean squared error: {}".format(
            r["degree"], r["score"], r["mse"]
        )
    )

print("------------------------------")  # 30個

from matplotlib.figure import SubplotParams

plt.figure(figsize=(12, 6), dpi=200, subplotpars=SubplotParams(hspace=0.3))
for i, r in enumerate(results):
    fig = plt.subplot(2, 2, i + 1)
    plt.xlim(-8, 8)
    plt.title("LinearRegression degree={}".format(r["degree"]))
    plt.scatter(X, Y, s=5, c="b", alpha=0.5)
    plt.plot(X, r["model"].predict(X), "r-")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("titanic")


def read_dataset(fname):
    # 指定第一列作為行索引
    data = pd.read_csv(fname, index_col=0)
    # 丟棄無用的數據
    data.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)
    # 處理性別數據
    data["Sex"] = (data["Sex"] == "male").astype("int")
    # 處理登船港口數據
    labels = data["Embarked"].unique().tolist()
    data["Embarked"] = data["Embarked"].apply(lambda n: labels.index(n))
    # 處理缺失數據
    data = data.fillna(0)
    return data


train = read_dataset("datasets/titanic/train.csv")
print(train.head())

from sklearn.model_selection import train_test_split

y = train["Survived"].values
X = train.drop(["Survived"], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("train dataset: {0}; test dataset: {1}".format(X_train.shape, X_test.shape))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

# sys.exit()

print("------------------------------------------------------------")  # 60個

from sklearn.tree import export_graphviz

with open("titanic.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png


# 參數選擇 max_depth
def cv_score(d):
    clf = DecisionTreeClassifier(max_depth=d)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


depths = range(2, 15)
scores = [cv_score(d) for d in depths]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = depths[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel("max depth of decision tree")
plt.ylabel("score")
plt.plot(depths, cv_scores, ".g-", label="cross-validation score")
plt.plot(depths, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


# 訓練模型，并計算評分
def cv_score(val):
    clf = DecisionTreeClassifier(criterion="gini", min_impurity_decrease=val)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


# 指定參數范圍，分別訓練模型，并計算評分
values = np.linspace(0, 0.005, 50)
scores = [cv_score(v) for v in values]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

# 找出評分最高的模型參數
best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = values[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

# 畫出模型參數與模型評分的關系
plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel("threshold of entropy")
plt.ylabel("score")
plt.plot(values, cv_scores, ".g-", label="cross-validation score")
plt.plot(values, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_curve(train_sizes, cv_results, xlabel):
    train_scores_mean = cv_results["mean_train_score"]
    train_scores_std = cv_results["std_train_score"]
    test_scores_mean = cv_results["mean_test_score"]
    test_scores_std = cv_results["std_test_score"]
    plt.figure(figsize=(10, 6), dpi=144)
    plt.title("parameters turning")
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel("score")
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
    plt.plot(train_sizes, train_scores_mean, ".--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, ".-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")


from sklearn.model_selection import GridSearchCV

thresholds = np.linspace(0, 0.005, 50)
# Set the parameters by cross-validation
param_grid = {"min_impurity_decrease": thresholds}

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

plot_curve(thresholds, clf.cv_results_, xlabel="gini thresholds")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import GridSearchCV

entropy_thresholds = np.linspace(0, 0.01, 50)
gini_thresholds = np.linspace(0, 0.005, 50)

# Set the parameters by cross-validation
param_grid = [
    {"criterion": ["entropy"], "min_impurity_decrease": entropy_thresholds},
    {"criterion": ["gini"], "min_impurity_decrease": gini_thresholds},
    {"max_depth": range(2, 10)},
    {"min_samples_split": range(2, 30, 2)},
]

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

print("------------------------------------------------------------")  # 60個

print("生成決策樹圖形")

clf = DecisionTreeClassifier(
    criterion="entropy", min_impurity_decrease=0.002857142857142857
)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

# 導出 titanic.dot 文件
with open("titanic.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png

print("------------------------------------------------------------")  # 60個

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4]])

plt.figure(figsize=(8, 6), dpi=144)

plt.title("Decision Boundary")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.arrow(4, 4, -1, -1, shape="full", color="r")
plt.plot([3, 3], [0.5, 6], "--b")
plt.arrow(4, 4, -1, 0, shape="full", color="b", linestyle="--")
plt.annotate(
    r"margin 1",
    xy=(3.5, 4),
    xycoords="data",
    xytext=(3.1, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"margin 2",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(4, 3.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"support vector",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"support vector",
    xy=(2, 2),
    xycoords="data",
    xytext=(0.5, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 6), dpi=144)

plt.title("Support Vector Machine")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")
plt.arrow(4, 4, -1, -1, shape="full", color="b")
plt.annotate(
    r"$w^T x + b = 0$",
    xy=(5, 1),
    xycoords="data",
    xytext=(6, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$w^T x + b = 1$",
    xy=(6, 2),
    xycoords="data",
    xytext=(7, 2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$w^T x + b = -1$",
    xy=(3.5, 0.5),
    xycoords="data",
    xytext=(4.5, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"d",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(2, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"A",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

plt.figure(figsize=(13, 6), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)

X, y = make_blobs(
    n_samples=100,
    n_features=2,
    centers=[(1, 1), (2, 2)],
    random_state=4,
    shuffle=False,
    cluster_std=0.4,
)

plt.title("Non-linear Separatable")

plt.xlim(0, 3)
plt.ylim(0, 3)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], marker="o")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], marker="s")
plt.plot([0.5, 2.5], [2.5, 0.5], "-r")

# sub plot 2
plt.subplot(1, 2, 2)

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2], [1.5, 1.5], [1.2, 1.7]])
class2 = np.array(
    [[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4], [5.5, 3.5], [4.5, 4.5], [2, 1.5]]
)

plt.title("Slack Variable")

plt.xlim(0, 7)
plt.ylim(0, 7)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")
plt.arrow(2, 1.5, 2.25, 2.25, shape="full", color="b")
plt.annotate(
    r"violate margin rule.",
    xy=(2, 1.5),
    xycoords="data",
    xytext=(0.2, 0.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"normal sample. $\epsilon = 0$",
    xy=(4, 5),
    xycoords="data",
    xytext=(4.5, 5.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$\epsilon > 0$",
    xy=(3, 2.5),
    xycoords="data",
    xytext=(3, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 4), dpi=144)

plt.title("Cost")

plt.xlim(0, 4)
plt.ylim(0, 2)
plt.xlabel("$y^{(i)} (w^T x^{(i)} + b)$")
plt.ylabel("Cost")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot([0, 1], [1.5, 0], "-r")
plt.plot([1, 3], [0.015, 0.015], "-r")
plt.annotate(
    r"$J_i = R \epsilon_i$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1 - \epsilon_i$",
    xy=(0.7, 0.5),
    xycoords="data",
    xytext=(1, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$J_i = 0$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1$",
    xy=(1.5, 0),
    xycoords="data",
    xytext=(1.8, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(13, 6), dpi=144)

class1 = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 2], [4, 1], [5, 1]])
class2 = np.array(
    [[2.2, 4], [1.5, 5], [1.8, 4.6], [2.4, 5], [3.2, 5], [3.7, 4], [4.5, 4.5], [5.4, 3]]
)

# sub plot 1
plt.subplot(1, 2, 1)

plt.title("Non-linear Separatable in Low Dimension")

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.yticks(())
plt.xlabel("X1")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")

plt.scatter(class1[:, 0], np.zeros(class1[:, 0].shape[0]) + 0.05, marker="o")
plt.scatter(class2[:, 0], np.zeros(class2[:, 0].shape[0]) + 0.05, marker="s")

# sub plot 2
plt.subplot(1, 2, 2)

plt.title("Linear Separatable in High Dimension")

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel("X1")
plt.ylabel("X2")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [3.8, 2], "-r")

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_hyperplane(clf, X, y, h=0.02, draw_sv=True, title="hyperplan"):
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap="hot", alpha=0.5)

    markers = ["o", "s", "^"]
    colors = ["b", "r", "c"]
    labels = np.unique(y)
    for label in labels:
        plt.scatter(
            X[y == label][:, 0],
            X[y == label][:, 1],
            c=colors[label],
            marker=markers[label],
        )
    if draw_sv:
        sv = clf.support_vectors_
        plt.scatter(sv[:, 0], sv[:, 1], c="y", marker="x")


from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.3)
clf = svm.SVC(C=1.0, kernel="linear")
clf.fit(X, y)

plt.figure(figsize=(12, 4), dpi=144)
plot_hyperplane(clf, X, y, h=0.01, title="Maximum Margin Hyperplan")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=3, random_state=0, cluster_std=0.8)
clf_linear = svm.SVC(C=1.0, kernel="linear")
clf_poly = svm.SVC(C=1.0, kernel="poly", degree=3)
clf_rbf = svm.SVC(C=1.0, kernel="rbf", gamma=0.5)
clf_rbf2 = svm.SVC(C=1.0, kernel="rbf", gamma=0.1)

plt.figure(figsize=(10, 10), dpi=144)

clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = [
    "Linear Kernel",
    "Polynomial Kernel with Degree=3",
    "Gaussian Kernel with $\gamma=0.5$",
    "Gaussian Kernel with $\gamma=0.1$",
]
for clf, i in zip(clfs, range(len(clfs))):
    clf.fit(X, y)
    plt.subplot(2, 2, i + 1)
    plot_hyperplane(clf, X, y, title=titles[i])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_files

""" 缺資料
print("loading train dataset ...")
t = time.time()
news_train = load_files('datasets/mlcomp/379/train')
print("summary: {0} documents in {1} categories.".format(
    len(news_train.data), len(news_train.target_names)))
print("done in {0} seconds".format(time.time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

print("vectorizing train dataset ...")
t = time.time()
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in news_train.data))
print("n_samples: %d, n_features: %d" % X_train.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_train.filenames[0], X_train[0].getnnz()))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

from sklearn.naive_bayes import MultinomialNB

print("traning models ...".format(time.time() - t))
t = time.time()
y_train = news_train.target
clf = MultinomialNB(alpha=0.0001)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
print("train score: {0}".format(train_score))
print("done in {0} seconds".format(time.time() - t))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 缺資料
print("loading test dataset ...")
t = time.time()
news_test = load_files('datasets/mlcomp/379/test')
print("summary: {0} documents in {1} categories.".format(
    len(news_test.data), len(news_test.target_names)))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

print("vectorizing test dataset ...")
t = time.time()
X_test = vectorizer.transform((d for d in news_test.data))
y_test = news_test.target
print("n_samples: %d, n_features: %d" % X_test.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_test.filenames[0], X_test[0].getnnz()))
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

pred = clf.predict(X_test[0])
print("predict: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[pred[0]]))
print("actually: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[news_test.target[0]]))

print("------------------------------")  # 30個

print("predicting test dataset ...")
t = time.time()
pred = clf.predict(X_test)
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

from sklearn.metrics import classification_report

print("classification report on test set for classifier:")
print(clf)
print(classification_report(y_test, pred,
                            target_names=news_test.target_names))

print("------------------------------")  # 30個

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, pred)
print("confusion matrix:")
print(cm)

print("------------------------------")  # 30個

# Show confusion matrix
plt.figure(figsize=(8, 8), dpi=144)
plt.title('Confusion matrix of the classifier')
ax = plt.gca()                                  
ax.spines['right'].set_color('none')            
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.matshow(cm, fignum=1, cmap='gray')
plt.colorbar()

plt.show()
"""
print("------------------------------------------------------------")  # 60個

print("PCA 算法模擬")

A = np.array([[3, 2000], [2, 3000], [4, 5000], [5, 8000], [1, 2000]], dtype="float")

# 數據歸一化
mean = np.mean(A, axis=0)
norm = A - mean
# 數據縮放
scope = np.max(norm, axis=0) - np.min(norm, axis=0)
norm = norm / scope
print(norm)

U, S, V = np.linalg.svd(np.dot(norm.T, norm))
print(U)

U_reduce = U[:, 0].reshape(2, 1)
print(U_reduce)

R = np.dot(norm, U_reduce)
print(R)

Z = np.dot(R, U_reduce.T)
print(Z)

print(np.multiply(Z, scope) + mean)

print("------------------------------")  # 30個

print("使用 sklearn 包實現")

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def std_PCA(**argv):
    scaler = MinMaxScaler()
    pca = PCA(**argv)
    pipeline = Pipeline([("scaler", scaler), ("pca", pca)])
    return pipeline


pca = std_PCA(n_components=1)
R2 = pca.fit_transform(A)
print(R2)

print(pca.inverse_transform(R2))

print("------------------------------------------------------------")  # 60個

print("降維及恢復示意圖")

plt.figure(figsize=(8, 8), dpi=144)

plt.title("Physcial meanings of PCA")

ymin = xmin = -1
ymax = xmax = 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(norm[:, 0], norm[:, 1], marker="s", c="b")
plt.scatter(Z[:, 0], Z[:, 1], marker="o", c="r")
plt.arrow(0, 0, U[0][0], U[1][0], color="r", linestyle="-")
plt.arrow(0, 0, U[0][1], U[1][1], color="r", linestyle="--")
plt.annotate(
    r"$U_{reduce} = u^{(1)}$",
    xy=(U[0][0], U[1][0]),
    xycoords="data",
    xytext=(U_reduce[0][0] + 0.2, U_reduce[1][0] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$u^{(2)}$",
    xy=(U[0][1], U[1][1]),
    xycoords="data",
    xytext=(U[0][1] + 0.2, U[1][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"raw data",
    xy=(norm[0][0], norm[0][1]),
    xycoords="data",
    xytext=(norm[0][0] + 0.2, norm[0][1] - 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"projected data",
    xy=(Z[0][0], Z[0][1]),
    xycoords="data",
    xytext=(Z[0][0] + 0.2, Z[0][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=200,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)

plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker="o")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.score(X))))

labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ["o", "^", "*"]
colors = ["r", "b", "y"]

plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())

# 畫樣本
for c in range(n_clusters):
    cluster = X[labels == c]
    plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
# 畫出中心點
plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])

plt.show()

print("------------------------------------------------------------")  # 60個


def fit_plot_kmean_model(n_clusters, X):
    plt.xticks(())
    plt.yticks(())

    # 使用 k-均值算法進行擬合
    kmean = KMeans(n_clusters=n_clusters)
    kmean.fit_predict(X)

    labels = kmean.labels_
    centers = kmean.cluster_centers_
    markers = ["o", "^", "*", "s"]
    colors = ["r", "b", "y", "k"]

    # 計算成本
    score = kmean.score(X)
    plt.title("k={}, score={}".format(n_clusters, (int)(score)))

    # 畫樣本
    for c in range(n_clusters):
        cluster = X[labels == c]
        plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
    # 畫出中心點
    plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])


from sklearn.cluster import KMeans

n_clusters = [2, 3, 4]

plt.figure(figsize=(10, 3), dpi=144)
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from time import time
from sklearn.datasets import load_files

""" 無檔案
print("loading documents ...")
t = time()
docs = load_files('datasets/clustering/data')
print("summary: {0} documents in {1} categories.".format(
    len(docs.data), len(docs.target_names)))
print("done in {0} seconds".format(time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print("vectorizing documents ...")
t = time()
vectorizer = TfidfVectorizer(max_df=0.4, 
                             min_df=2, 
                             max_features=max_features, 
                             encoding='latin-1')
X = vectorizer.fit_transform((d for d in docs.data))
print("n_samples: %d, n_features: %d" % X.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    docs.filenames[0], X[0].getnnz()))
print("done in {0} seconds".format(time() - t))

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

print("clustering documents ...")
t = time()
n_clusters = 4
kmean = KMeans(n_clusters=n_clusters, 
               max_iter=100,
               tol=0.01,
               verbose=1,
               n_init=3)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.inertia_)))
print("done in {0} seconds".format(time() - t))

print(len(kmean.labels_))

cc = kmean.labels_[1000:1010]
print(cc)

cc = docs.filenames[1000:1010]
print(cc)

print('------------------------------')	#30個

#from __future__ import print_function

print("Top terms per cluster:")

order_centroids = kmean.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(n_clusters):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

a = np.array([[20, 10, 30, 40], [100, 300, 200, 400], [1, 5, 3, 2]])
cc = a.argsort()[:, ::-1]
print(cc)

a = np.array([10, 30, 20, 40])
cc = a.argsort()[::-1]
print(cc)
"""
print("------------------------------------------------------------")  # 60個

from sklearn import metrics

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Adjusted Rand-Index for random sample: %.3f"
    % metrics.adjusted_rand_score(label_true, label_pred)
)
label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]
print(
    "Adjusted Rand-Index for same structure sample: %.3f"
    % metrics.adjusted_rand_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "Homogeneity score for same structure sample: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]
print(
    "Homogeneity score for each cluster come from only one class: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "Homogeneity score for each cluster come from two class: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Homogeneity score for random sample: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "Completeness score for same structure sample: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print(
    "Completeness score for each class assign to only one cluster: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "Completeness score for each class assign to two class: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Completeness score for random sample: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "V-measure score for same structure sample: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print(
    "V-measure score for each class assign to only one cluster: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
print(
    "V-measure score for each class assign to only one cluster: %.3f"
    % metrics.v_measure_score(label_pred, label_true)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "V-measure score for each class assign to two class: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
"""
from sklearn import metrics

labels = docs.target
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, kmean.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, kmean.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, kmean.labels_))
print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, kmean.labels_))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, kmean.labels_, sample_size=1000))
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


print("------------------------------------------------------------")  # 60個
