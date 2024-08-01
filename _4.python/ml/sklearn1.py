"""
pip install scikit-learn

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print('------------------------------------------------------------')	#60個

import sklearn as skl
print(skl.__version__)

from sklearn import datasets, svm, metrics
print(dir(datasets))

import sklearn
print(sklearn)

print('------------------------------------------------------------')	#60個

print('線性回歸的範例 1')

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [88, 72, 90, 76, 92]
lm.fit(X, y)
print('第6次考試分數：', lm.predict([[6]]))

print('線性回歸的範例 2')

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [1, 4, 9, 16, 25]
lm.fit(X, y)

xx = np.linspace(0,10,11)
yy = np.linspace(0,10,11)
for i in range(11):
    print(i)
    print('第',i,'項', lm.predict([[i]]))
    xx[i] = i
    yy[i] = lm.predict([[i]])

plt.plot(X,y,'ro-')
plt.plot(xx,yy,'go:')


plt.show()

print('------------------------------------------------------------')	#60個

from scipy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

def similarity_tfidf(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    s1, s2 = add_space(s1), add_space(s2)

    cv = TfidfVectorizer(tokenizer = lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()

    return np.dot(vectors[0], vectors[1])/(norm(vectors[0]) * norm(vectors[1]))

string1 = '漢堡蛋'
string2 = '我要一份漢堡蛋'
#string2 = '請給我來一份漢堡蛋'
#string2 = '你是一個漢堡蛋嗎?'

result = similarity_tfidf(string1, string2)

print('相似度 : ', result)
if result > 0.2:
    print('OK, 一個漢堡蛋')
else:
    print('Sorry, 無法接受訂餐')


print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看

iris = sns.load_dataset('iris')
iris.head()

sns.set()
sns.pairplot(iris, hue='species', height=3);

print(iris)
print('cccc')

print('------------------------------------------------------------')	#60個

# seaborn

import seaborn as sns #海生, 自動把圖畫得比較好看

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

plt.rcParams["font.sans-serif"]='Microsoft JhengHei'

tips = sns.load_dataset("tips")
print(tips)

print('------------------------------------------------------------')	#60個

#怎麼選最好參數、model？
#製造像真的一様的數據

#from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples = 500,
                  centers = 3,
                  n_features = 2,
                  random_state = 0)
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.show()

print('------------------------------------------------------------')	#60個

#Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

clf = SVC()
#clf = SVC(gamma = 'scale')

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

#試用 Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

#試用 Random Forest

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators = 100)

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

from sklearn import datasets

np.random.seed(3)                           # 設計隨機數種子
x, y = datasets.make_regression(n_features = 1, noise = 20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features = 1, noise = 20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label = "訓練數據")
plt.scatter(x_test, y_test, label = "測試數據")
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features = 1, noise = 20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

regression = linear_model.LinearRegression()               # 建立線性模組物件
regression.fit(x_train, y_train)
print(f'斜率  = {regression.coef_[0].round(2)}')
print(f'截距  = {regression.intercept_.round(2)}')

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features = 1, noise = 20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

regression = linear_model.LinearRegression()               # 建立線性模組物件
regression.fit(x_train, y_train)
print(f'斜率  = {regression.coef_[0].round(2)}')
print(f'截距  = {regression.intercept_.round(2)}')

y_pred = regression.predict(x_test)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train,y_train,label = "訓練數據")
plt.scatter(x_test,y_test,label = "測試數據")
# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color = "red")

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)                           
print(f'決定係數 = {r2.round(2)}')

plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets

np.random.seed(3)                                       # 設定隨機數種子值

#np.random.seed(5)                                       # 設定隨機數種子值

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples = 300, n_features = 2)                                

# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:, 0], data[:, 1], marker = "o", edgecolor = "black")

plt.title("無監督學習")

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples = 300, n_features = 2)
                                  
e = cluster.KMeans(n_clusters = 3)      # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples = 300, n_features = 2)
                                  
e = cluster.KMeans(n_clusters = 3)      # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(data[:, 0], data[:, 1], marker = "o", c = e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker = "*", color = "red")
plt.title("無監督學習")
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples = 1000,
                         n_features = 2,
                         centers = 2,
                         random_state = 5)
d_sta = StandardScaler().fit_transform(data)    # 標準化

# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta, label,
                                                              test_size = 0.2,
                                                              random_state = 0)
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

print('------------------------------------------------------------')	#60個



