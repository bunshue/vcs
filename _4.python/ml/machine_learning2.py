"""




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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

import sklearn
import sklearn.linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.datasets import make_blobs

import matplotlib
import matplotlib as mpl

print("------------------------------------------------------------")  # 60個

"""
計算相似度
#sklearn sklearn向量距離計算

通過 euclidean_distances 計算多個向量間的歐氏距離。

歐幾里得距離 (Euclidean distance)
    0, r1*r2, r1*r3, r1*r4
-----,     0, r2*r3, r2*r4
-----, -----,     0, r3*r4
-----, -----, -----,     0
"""

from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity

print("測試 euclidean_distances 歐幾里得距離 (Euclidean distance)")

X = np.array(
    [
        [4, 3, 0, 0, 5, 0],  # r1
        [5, 0, 4, 0, 4, 0],  # r2
        [4, 0, 5, 3, 4, 0],  # r3
        [0, 3, 0, 0, 0, 5],  # r4
    ]
)

"""
X = np.array(
    [
        [4, 3, 0, 0, 5, 0, 4, 3, 0, 0, 5, 0],  # r1
        [5, 0, 4, 0, 4, 0, 5, 0, 4, 0, 4, 0],  # r2
    ]
)
"""

dist = euclidean_distances(X)
print(dist)

print("測試 cosine_similarity")
sim = cosine_similarity(X)
print(sim)

print("兩列之間的距離")
X = [[0, 1], [1, 1]]
cc = euclidean_distances(X, X)
print(cc)

print("與原點之間的距離")
cc = euclidean_distances(X, [[0, 0]])
print(cc)

print("比較字串的距離")

from sklearn.feature_extraction.text import CountVectorizer

corpus = ["I am a good student", "I am a good teacher", "This is a pencil"]  # 文集

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(corpus).todense()  # 得到文集corpus的特征向量，並將其轉為密集矩陣
print(counts)

""" kilo OK, 但是 sugar不OK
for x,y in [[0,1],[0,2],[1,2]]:
    dist = euclidean_distances(counts[x],counts[y])
    print('文檔{}與文檔{}的距離{}'.format(x,y,dist))
"""

print("比較幾個向量的距離")

# 每個人的特徵向量
vector1 = [1.0, 1.0, 1.0]  # 嫌犯 1 的特徵
vector2 = [0.2, 0.7, 0.2]  # 嫌犯 2 的特徵
vector3 = [0.4, 0.8, 0.9]  # 嫌犯 3 的特徵
vector4 = [0.8, 0.8, 0.3]  # 嫌犯 4 的特徵

# 把特徵向量集合成一個串列，好讓 sklearn 方便直接計算任兩個向量間的相似度
feature_vectors = [vector1, vector2, vector3, vector4]
print("Feature vectors:")
print(feature_vectors)
print()

# 計算任兩個向量間的歐幾里德距離
print("Euclidean distances:")
distances_similarity_metrix = euclidean_distances(feature_vectors)
print(distances_similarity_metrix)
print()

# 計算任兩個向量間的餘弦相似度
print("Cosine similarity:")
cosine_similarity_metrix = cosine_similarity(feature_vectors)
print(cosine_similarity_metrix)
print()

print("------------------------------------------------------------")  # 60個
"""
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

text = ["小貝來到北京清華大學",
        "小花來到了網易杭研大廈",
        "小明碩士畢業于中國科學院",
        "小明愛北京小明愛北京天安門"
        ]
               
corpus = ["小貝 來到 北京 清華大學",
          "小花 來到 了 網易 杭研 大廈",
          "小明 碩士 畢業 于 中國 科學院",
          "小明 愛 北京 小明 愛 北京 天安門"
          ]

print('二值化、詞頻')
vectorizer = CountVectorizer(min_df = 1, binary = True) #Transformer
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)
print(len(features))

print(data.todense())

doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)

print(doc_df)
print(doc_df.columns)

print('------------------------------')	#30個

from sklearn.metrics.pairwise import cosine_similarity

cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index = text, columns = text)
print(sims_df)

print('------------------------------')	#30個

#tf-idf

vectorizer = TfidfVectorizer(min_df = 1)
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)

print('------------------------------')	#30個

pd.set_option('display.precision', 2)
doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)
print(doc_df)

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
x = np.array([i * np.pi / 180 for i in range(0, 370, 10)])
#y = np.sin(x) + np.random.normal(0, 0.15, len(x))
y = np.sin(x)

data = pd.DataFrame(np.column_stack([x, y]), columns = ['x', 'y'])
#data.head(10)
print(data)
plt.scatter(data['x'], data['y'], s = 30)

plt.show()

for i in range(2, 16):
    colname = 'x_%d'%i      
    data[colname] = data['x'] ** i

tt = data.head()
print(tt)

print('------------------------------')	#30個


def linear_regression(data, power, models_to_plot):
    print('power =', power)
    #initialize predictors:
    predictors = ['x']
    if power >= 2:
        predictors.extend(['x_%d'%i for i in range(2, power + 1)])
    
    # 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
    
    linear_regression.fit(data[predictors],data['y'])  # 學習訓練.fit
    
    y_pred = linear_regression.predict(data[predictors])  # 預測.predict
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y']) ** 2)
    ret = [rss]
    ret.extend([linear_regression.intercept_])
    ret.extend(linear_regression.coef_)
    
    #Check if a plot is to be made for the entered power
    if power in models_to_plot:
        print(power)
        print(models_to_plot[power])
        plt.subplot(models_to_plot[power])
        plt.tight_layout()
        plt.plot(data['x'], y_pred, lw = 3)
        plt.plot(data['x'], data['y'], '.')
        plt.title('Plot for power: %d , RSS: %.2f' % (power, rss))
    
    return ret

#Initialize a dataframe to store the results:
col = ['rss','intercept'] + ['coef_x_%d' % i for i in range(1, 16)]
ind = ['model_pow_%d' % i for i in range(1, 16)]

coef_matrix_simple = pd.DataFrame(index = ind, columns = col)
print('1111')
print(coef_matrix_simple)

#Define the powers for which a plot is required:
models_to_plot = {1:231,3:232,6:233,9:234,12:235,15:236}

#Iterate through all powers and assimilate results
for i in range(1,16):
    print("i =", i)
    coef_matrix_simple.iloc[i-1,0:i+2] = linear_regression(data, power=i, models_to_plot=models_to_plot)

plt.show()

print('------------------------------')	#30個

#Set the display format to be scientific for ease of analysis
pd.options.display.float_format = '{:,.2g}'.format

print('2222')
print(coef_matrix_simple)

print('------------------------------')	#30個

# Ridge Regression 嶺迴歸

#L2 Normalization Ridge Regression

from sklearn.linear_model import Ridge

def ridge_regression(data, predictors, alpha, models_to_plot={}):
    #ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg = Ridge(alpha=alpha)
    ridgereg.fit(data[predictors],data['y'])  # 學習訓練.fit
    y_pred = ridgereg.predict(data[predictors])  # 預測.predict
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)


    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred,lw=3)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g ,RSS : %.2f'%(alpha,rss))
    return ret


#Initialize predictors to be set of 15 powers of x
predictors=['x']
predictors.extend(['x_%d'%i for i in range(2,16)])

#Set the different values of alpha to be tested
alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]

#Initialize the dataframe for storing coefficients.
col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
ind = ['alpha_%.2g'%alpha_ridge[i] for i in range(0,10)]
coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
for i in range(10):
    coef_matrix_ridge.iloc[i,] = ridge_regression(data, predictors, alpha_ridge[i], models_to_plot)

plt.show()        

print('------------------------------')	#30個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_ridge

print(tt)

print('------------------------------')	#30個

#有多少個系數為0

coef_matrix_ridge.apply(lambda x: sum(x.values==0),axis=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import TruncatedSVD

corpus = ["Python is popular in machine learning",
         "Distributed system is important in big data analysis",
        "Machine learning is theoretical foundation of data mining",
        "Learning Python is fun",
        "Playing soccer is fun",
        "Many data scientists like playing soccer",
        "Chinese men's soccer team failed again",
        "Thirty two soccer teams enter World Cup finals"]

vectorizer = CountVectorizer(min_df=1, stop_words="english")
data = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()

tt = pd.DataFrame(data.toarray(), index=corpus, columns=vectorizer.get_feature_names_out()).head(10)
print(tt)

print('------------------------------')	#30個

#Singular value decomposition and LSA
model = TruncatedSVD(2)
data_n = model.fit_transform(data)
data_n = Normalizer(copy=False).fit_transform(data_n)
print(data_n)

tt = pd.DataFrame(data_n, index = corpus, columns = ["component_1", "component_2"])
print(tt)

xs = data_n[:,0]
ys = data_n[:,1]

plt.figure(figsize=(4,4))

ax = plt.gca()
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])

plt.scatter(xs, ys)
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.title('Plot of points agains LSA principal components')

plt.show()

print('------------------------------')	#30個

similarity = np.asarray(np.asmatrix(data_n) * np.asmatrix(data_n).T)
tt = pd.DataFrame(similarity, index = corpus, columns = corpus).head(10)
print(tt)

print(similarity)
 
sns.heatmap(similarity, cmap = 'Reds')

plt.show()

print(pd.DataFrame(model.components_,index=['component_1','component_2'],columns=vectorizer.get_feature_names_out()).T)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print('房價, 共 1460 筆資料 81欄位')

import scipy.stats as stats

train = pd.read_csv(u'data/houseprice.csv') # 共 1460 筆資料 81欄位
print(len(train))
print(train.shape)
print(train.head(3))

y = train['SalePrice']

sns.histplot(y)
plt.xlabel('售價區間')
plt.ylabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
plt.show()

#另一種查看是否服從正態分布的可視化方法
import scipy.stats as st

res = st.probplot(y, plot=plt)
plt.ylabel('售價區間')
plt.xlabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
plt.show()

sns.distplot(y,kde=False)
plt.xlabel('售價區間')
plt.ylabel('賣出件數')
plt.title('統計 售價區間 / 賣出件數')
plt.show()

sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.title('使用 Johnson SU')
plt.show()

sns.distplot(y, kde=False, fit=st.norm)
plt.title('使用 Normal')
plt.show()

sns.distplot(y, kde=False, fit=st.lognorm)
plt.title('使用 Log Normal')
plt.show()

#另一種查看是否服從正態分布的可視化方法

sns.distplot(y, fit=st.norm)
plt.title('使用 Normal')
plt.show()

res = st.probplot(y, plot=plt)
plt.title('SalePrice')
plt.show()

print('------------------------------')	#30個

#把房價做對數變換后再看
SalePrice_log = np.log(y)
 
#transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm);
plt.title('SalePrice log')
plt.show()

#另一種查看是否服從正態分布的可視化方法
res = st.probplot(SalePrice_log, plot=plt)
print(res)
plt.title('SalePrice log')
plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from scipy.stats import norm


def norm_prob(x, mu, sigma):
    p = norm(mu, sigma).cdf(x + 0.0001) - norm(mu, sigma).cdf(x - 0.0001)
    return p


def loglikelihood(data, mu, sigma):
    l = 0.0
    for x in data:
        l -= np.log(norm_prob(x, mu, sigma))
    return l


N = 1000
mu, sigma = 1.6, 0.2

h = 1.8

#rvs: 隨機變量
data = norm.rvs(loc=mu, scale=sigma, size=N)
#print(data)

bins = 50  # 束
plt.hist(data, bins=bins)
plt.title('normal distribution')
plt.show()

#pdf: 概率密度函數
tt = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(tt)

tt = norm_prob(h, mu, sigma)
print(tt)

tt = loglikelihood(data, mu, sigma)
print(tt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

neg_data = "data/neg.csv"
pos_data = "data/pos.csv"

import codecs
import jieba

corpus = []
with codecs.open(neg_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus.append(" ".join(words))

neg_df = pd.DataFrame()
neg_df["content"] = corpus
neg_df["label"] = 0

corpus2 = []
with codecs.open(pos_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus2.append(" ".join(words))

pos_df = pd.DataFrame()
pos_df["content"] = corpus2
pos_df["label"] = 1

tt = neg_df.head(5)
print(tt)

tt = pos_df.head(5)
print(tt)

corpus_df = pd.concat((neg_df, pos_df))

tt = corpus_df.head(5)
print(tt)

print('------------------------------')	#30個

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
counts = cv.fit_transform(corpus_df["content"].values)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
targets = corpus_df["label"].values
classifier.fit(counts, targets)  # 學習訓練.fit

examples = ["這 本 書 真差", "這個 電影 還 可 以"]
example_counts = cv.transform(examples)
predictions = classifier.predict(example_counts)  # 預測.predict

print('預測結果 :', predictions)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. 建立空的df
df = pd.DataFrame()

# 2. 增加 Gender 欄位 目標欄位
df["Gender"] = [
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "female",
    "female",
]

# 3. 增加 4欄位 為 feature variables
df["Height"] = [6, 5.92, 5.58, 5.92, 5, 5.5, 5.42, 5.75]
df["Weight"] = [180, 190, 170, 165, 100, 150, 130, 150]
df["Size"] = [12, 11, 12, 10, 6, 8, 7, 9]
df["Team"] = ["i100", "i100", "i500", "i100", "i500", "i100", "i500", "i100"]

print("df:\n", df)

print("------------------------------")  # 30個

df1 = (
    df.groupby(["Team", "Gender"]).size().rename("cnt").reset_index().set_index("Team")
)
print("df1:\n", df1)

df2 = pd.DataFrame(df.groupby(["Team"]).size().rename("total"))
print("df2:\n", df2)

df3 = df1.merge(df2, left_index=True, right_index=True)
df3["p"] = df3["cnt"] * 1.0 / df3["total"]
df3 = df3.reset_index()
print("df3:\n", df3)

print("------------------------------")  # 30個


def p_x_given_y_1(team, gender):
    return df3["p"][df3["Team"] == team][df3["Gender"] == gender].values[0]


print("p_x_given_y_1")
print(p_x_given_y_1("i100", "female"))
# 0.4

print("------------------------------")  # 30個

# 計算先驗
# Number of i100
n_i100 = df["Team"][df["Team"] == "i100"].count()
print("n_i100 的個數 :", n_i100)

# Number of i500
n_i500 = df["Team"][df["Team"] == "i500"].count()
print("n_i500 的個數 :", n_i500)

# Total rows
total_ppl = df["Team"].count()
print("全部列數 :", n_i100)

# Number of males divided by the total rows
P_i100 = n_i100 * 1.0 / total_ppl

# Number of females divided by the total rows
P_i500 = n_i500 * 1.0 / total_ppl

print("P_i100 :", P_i100)
print("P_i500 :", P_i500)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 計算高斯分布的概率

# 1. 建立空的df
df = pd.DataFrame()

# Create some feature values for this single row
# 2. 增加 Gender 欄位 目標欄位 ??
# 3. 增加 4欄位 為 feature variables ??
df["Height"] = [6]
df["Weight"] = [130]
df["Size"] = [8]
df["Gender"] = ["female"]

print("df:\n", df)


def p_x_given_y_2(x, mean_y, variance_y):
    # Input the arguments into a probability density function
    p = (
        1
        / (np.sqrt(2 * np.pi * variance_y))
        * np.exp((-((x - mean_y) ** 2)) / (2 * variance_y))
    )
    return p


tt = df["Gender"][0]
print(tt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""

"""
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

train_size = 20
test_size = 12
train_X = np.random.uniform(low=0, high=1.2, size=train_size)
test_X = np.random.uniform(low=0.1, high=1.3, size=test_size)
train_y = np.sin(train_X * 2 * np.pi) + np.random.normal(0, 0.2, train_size)
test_y = np.sin(test_X * 2 * np.pi) + np.random.normal(0, 0.2, test_size)

poly = PolynomialFeatures(6)  # 次數は6

train_poly_X = poly.fit_transform(train_X.reshape(train_size, 1))
test_poly_X = poly.fit_transform(test_X.reshape(test_size, 1))

model = Ridge(alpha=1.0)

model.fit(train_poly_X, train_y)  # 學習訓練.fit

train_pred_y = model.predict(train_poly_X)  # 預測.predict
test_pred_y = model.predict(test_poly_X)  # 預測.predict
print(mean_squared_error(train_pred_y, train_y))
print(mean_squared_error(test_pred_y, test_y))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# データ生成
centers = [(-1, -0.125), (0.5, 0.5)]

N = 50
print("產生", N, "筆資料 2維 2群")
X, y = make_blobs(n_samples=N, n_features=2, centers=centers, cluster_std=0.3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LinearSVC()

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))  # 評価
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
from sklearn.naive_bayes import MultinomialNB

# データ生成
X_train = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
]
y_train = [1, 1, 1, 0, 0, 0]

model = MultinomialNB()

model.fit(X_train, y_train)  # 學習訓練.fit

print(model.predict([[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]))  # 預測.predict
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
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
n_components = 2  # 潜在変数の数

model = TruncatedSVD(n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data))  # 変換したデータ
print(model.explained_variance_ratio_)  # 寄与率
print(sum(model.explained_variance_ratio_))  # 累積寄与率
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import NMF

centers = [[5, 10, 5], [10, 4, 10], [6, 8, 8]]
X, _ = make_blobs(centers=centers)  # centersを中心としたデータを生成
n_components = 2  # 潜在変数の数

model = NMF(n_components=n_components)

model.fit(X)  # 學習訓練.fit

W = model.transform(X)  # 分解後の行列
H = model.components_
print(W)
print(H)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# removeで本文以外の情報を取り除く
data = fetch_20newsgroups(remove=("headers", "footers", "quotes"))
max_features = 1000
# 文書 データをベクトルに変換
tf_vectorizer = CountVectorizer(max_features=max_features, stop_words="english")
tf = tf_vectorizer.fit_transform(data.data)
n_topics = 20

model = LatentDirichletAllocation(n_components=n_topics)

model.fit(tf)  # 學習訓練.fit

print(model.components_)  # 各トピックが持つ単語分布
print(model.transform(tf))  # トピックで表現された文書

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" import fail
from sklearn.datasets import samples_generator
from sklearn.manifold import LocallyLinearEmbedding

data, color = samples_generator.make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍点の数 
n_components = 2 # 削減後の次元数

model = LocallyLinearEmbedding(n_neighbors=n_neighbors,

n_components=n_components)

model.fit(data)  # 學習訓練.fit

print(model.transform(data)) # 変換したデータ
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------")  # 30個
''' NG
print("混同行列")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y, y_pred)
print(cm)

print("------------------------------")  # 30個

print("正解率")
from sklearn.metrics import accuracy_score

accuracy_score(y, y_pred)

print("------------------------------")  # 30個

print("適合率")
from sklearn.metrics import precision_score

precision_score(y, y_pred)

print("------------------------------")  # 30個

print("再現率")
from sklearn.metrics import recall_score

recall_score(y, y_pred)

print("------------------------------")  # 30個

print("F値")
from sklearn.metrics import f1_score

f1_score(y, y_pred)

print("------------------------------")  # 30個

print("予測確率")
logistic_regression.predict_proba(X)

print("------------------------------")  # 30個

y_pred2 = (logistic_regression.predict_proba(X)[:, 1] > 0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print("------------------------------")  # 30個

print("ROC曲線・AUC")
from sklearn.metrics import roc_curve

probas = logistic_regression.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print("------------------------------")  # 30個

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, "gray")
ax.fill_between(fpr, tpr, 0, color="skyblue", alpha=0.8)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_facecolor("xkcd:white")
plt.show()

print("------------------------------")  # 30個

from sklearn.metrics import roc_auc_score

roc_auc_score(y, probas[:, 1])

print("------------------------------")  # 30個

print("平均二乗誤差")

from sklearn.metrics import mean_squared_error

mean_squared_error(y, y_pred)

print("------------------------------")  # 30個

print("決定係数")

from sklearn.metrics import r2_score

print(r2_score(y, y_pred))

print("------------------------------")  # 30個

print("異なるアルゴリズムを利用した場合との比較")

from sklearn.svm import SVR

model_svr_linear = SVR(C=0.01, kernel="linear")

model_svr_linear.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_linear.predict(X)  # 預測.predict
print(y_svr_pred)

"""
fig, ax = plt.subplots()
ax.scatter(X, y, color='pink', marker='s', label='data set')
ax.plot(X, y_pred, color='blue', label='regression curve')
ax.plot(X, y_svr_pred, color='red', label='SVR')
ax.legend()
plt.show()
"""

print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数
print(model_svr_linear.coef_)  # 傾き
print(model_svr_linear.intercept_)  # 切片

print("------------------------------")  # 30個

print("ハイパーパラメータの設定")

model_svr_rbf = SVR(C=1.0, kernel="rbf")

model_svr_rbf.fit(X, y)  # 學習訓練.fit

y_svr_pred = model_svr_rbf.predict(X)  # 預測.predict
print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]

model_svr_rbf_1 = SVR(C=1.0, kernel="rbf")

model_svr_rbf_1.fit(train_X, train_y)  # 學習訓練.fit

test_y_pred = model_svr_rbf_1.predict(test_X)  # 預測.predict
print(mean_squared_error(test_y, test_y_pred))  # 平均二乗誤差
print(r2_score(test_y, test_y_pred))  # 決定係数

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("機械学習モデルへの適用")

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups

categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]
remove = ("headers", "footers", "quotes")
twenty_train = fetch_20newsgroups(
    subset="train", remove=remove, categories=categories
)  # 学習データ
twenty_test = fetch_20newsgroups(
    subset="test", remove=remove, categories=categories
)  # 検証データ

count_vect = CountVectorizer()  # 単語カウント
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_test_count = count_vect.transform(twenty_test.data)

model = LinearSVC()

model.fit(X_train_counts, twenty_train.target)  # 學習訓練.fit

predicted = model.predict(X_test_count)  # 預測.predict
np.mean(predicted == twenty_test.target)

tf_vec = TfidfVectorizer()  # tf-idf
X_train_tfidf = tf_vec.fit_transform(twenty_train.data)
X_test_tfidf = tf_vec.transform(twenty_test.data)

model = LinearSVC()

model.fit(X_train_tfidf, twenty_train.target)  # 學習訓練.fit

predicted = model.predict(X_test_tfidf)  # 預測.predict
np.mean(predicted == twenty_test.target)

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6-1 探索性資料分析──以Titanic(鐵達尼號)之生還預測為例
# 資料科學 0. 問個感興趣的問題

# 資料科學 1. 資料取得
# 資料科學1.1 自建資料或下載資料後上傳到雲端硬碟

# train.csv行資料說明.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/titanic.csv"
df = pd.read_csv(filename)
"""
print(df)
print(df.info())
print(df.describe())
"""

# 資料科學2.3 資料清理
# 缺失值的補值或刪除

print(df.isnull())

print(df.isnull().sum())

print(df.isnull().count())

print(df.isnull().sum() / df.isnull().count() * 100)

df[df["Age"].isnull() == True]

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

df[df["Embarked"].isnull()]

df["Embarked"].value_counts()

df["Embarked"] = df["Embarked"].fillna("S")

df.loc[[61, 829], :]  # 顯示列索引61,829的資料

print(df.info())

df = df.drop("Cabin", axis=1)

print(df.info())

# 刪除重複值或異常值
df[df.duplicated()]

# 資料轉換
print(df.head())

s = {"female": 0, "male": 1}
df["Sex"] = df["Sex"].map(s)
e = {"S": 0, "C": 1, "Q": 2}
df["Embarked"] = df["Embarked"].map(e)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)

print(df.head())

# 資料科學3.2 資料視覺化
# 1.全體乘客生還、死亡的比例

print(df["Survived"].value_counts())

df["Survived"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 2.男性、女性乘客的比例

print(df["Sex"].value_counts())

df["Sex"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 3.搭1等艙、2等艙、3等艙的乘客比例

print(df["Pclass"].value_counts())

df["Pclass"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 4.進一步探討性別與生還的關係

# 女、男乘客的人數

print(df.groupby(["Sex"])["PassengerId"].count())

# 不同性別的生還和死亡人數

print(df.groupby(["Sex", "Survived"])["PassengerId"].count())

df.groupby(["Sex", "Survived"])["PassengerId"].count().plot(kind="bar", rot=1)
plt.show()

print("------------------------------")  # 30個

# 不同性別生還人數/不同性別人數

ss = (
    df.groupby(["Sex", "Survived"])["PassengerId"].count()
    / df.groupby(["Sex"])["PassengerId"].count()
    * 100
)
print(ss)

ss.plot(kind="bar", color=["r", "g"], rot=0)
plt.show()

print("------------------------------")  # 30個

# 5.進一步探討艙等與生還的關係

# 三種艙等的生還和死亡人數

print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())

df.groupby(["Pclass", "Survived"])["PassengerId"].count().plot(kind="bar", rot=0)
plt.show()

print("------------------------------")  # 30個

# 不同艙等生還人數/不同艙等人數

ps = (
    df.groupby(["Pclass", "Survived"])["PassengerId"].count()
    / df.groupby(["Pclass"])["PassengerId"].count()
    * 100
)
print(ps)

ps.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6-2 探索性資料分析──以 Iris 的花種分類為例
# 資料科學0. 感興趣的問題

# 資料科學1. 資料取得
# 資料科學1.1 自建資料或從網路下載資料後上傳到雲端硬碟

# Iris.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
print(df)

df = df.drop("Id", axis=1)
print(df.head())

# 資料科學2. 資料處理
# 資料科學2.1 由列資料了解資料集

print(df.head())

# 資料科學2.2 了解行資料的標題與資料型別(整數、浮點數、字串等)

print(df.info())

# 資料科學2.3 資料清理

# 缺失值的補值或刪除

print(df.info())

# 刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True)  # 將列索引重新編號

# 資料轉換

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)
print(df.head())

# 資料科學3.2 資料視覺化

c = {0: "r", 1: "g", 2: "b"}
df["colors"] = df["Species"].map(c)
print(df)

df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (圖)-不同欄位和「類別(Species)」所繪製的散佈圖
# (a)花萼長度
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (b)花萼寬度
df.plot(kind="scatter", x="SepalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (c)花瓣長度
df.plot(kind="scatter", x="PetalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (d)花瓣寬度
df.plot(kind="scatter", x="PetalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (圖)-2個欄位組合所繪製的散佈圖
# (a)花萼長度 vs. 花萼寬度
df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (b)花瓣長度 vs. 花瓣寬度
df.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (c)花萼長度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (d)花瓣長度 vs. 花萼寬度
df.plot(kind="scatter", x="PetalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (e)花萼長度 vs. 花瓣長度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalLengthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (f)花萼寬度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalWidthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Iris為例

# 1. 資料取得

filename = "data/Iris2.csv"

df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

df.info()

df = df.drop_duplicates()  # 刪除重複列
df.reset_index(drop=True)  # 將列索引重新編號
s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
df.info()

# 3. 探索性資料分析
print(df.head())
"""
#4. 機器學習做資料分析
9-2 機器學習實作──以Iris為例
9-2-1 提出具體的假設
9-2-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
df_y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)  # 建立新模型 knn

knn.fit(X_train, y_train)  # 學習訓練.fit

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的正確率計算-------")

print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 學習訓練.fit
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 8
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)  # 學習訓練.fit

# 加廣知識：視覺化圖表來顯示準確率

df_knn = pd.DataFrame()
df_knn["s"] = s
df_knn.index = [3, 4, 5, 6, 7, 8, 9, 10]
df_knn.plot(grid=True)

plt.show()

print("分類的預測結果：")
pred = knn.predict(X_test)  # 預測.predict
print(pred)

print(y_test.values)  # 觀察Test data真實數據

# 加廣知識：利用values屬性做橫式顯示

print(y_test)

print(y_test.values)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 1.0

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

# 加深知識：交叉驗證概念

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("交叉驗證每次的準確率：", s)
print("交叉驗證得到的平均準確率：", s.mean())

# 決定模型
# 進行分類預測

new = [[6.6, 3.1, 5.2, 2.4]]
v = knn.predict(new)  # 預測.predict
if v == 0:
    s = "Iris-Setosa"
elif v == 1:
    s = "Iris-Versicolour"
elif v == 2:
    s = "Iris-Virginica"
else:
    s = "錯誤"
print("預測結果為：", s)

# 預測結果為： 錯誤

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Titanic為例

# 1. 資料取得

filename = "data/titanic.csv"
df = pd.read_csv(filename)
print(df.head())

# 2. 資料處理
df.info()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna("S")
df = df.drop("Cabin", axis=1)
print("重複值：", df[df.duplicated()])  # 檢查有無重複值

df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print(df.head())

# 重複值： Empty DataFrame

# 3. 探索性資料分析

print(df.head())

"""
4. 機器學習做資料分析
9-4 機器學習實作─以Titanic為例
9-4-1 提出具體的假設
9-4-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["Sex", "Pclass"]]
df_y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)  # 學習訓練.fit

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的準確率計算-------")
print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 學習訓練.fit
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 4
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)  # 學習訓練.fit

print("分類的預測結果：")
pred = knn.predict(X_test)  # 預測.predict
print(pred)  # 觀察預測結果

print("真實數據：")
print(y_test.values)  # 觀察真實數據(Test data)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 0.7541899441340782

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("準確率：", s)
print("平均準確率：", s.mean())
print("最高：", s.max())
print("最差：", s.min())

# 決定模型
# 進行分類預測

print("-----------(1)電影中兩位主角的生還推測-------------")

Rose = [[0, 1]]  # 女性 頭等艙 蘿絲（Rose DeWitt Bukater）
Jack = [[1, 3]]  # 男性 三等艙 傑克（Jack Dawson）
v = knn.predict(Rose)  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Rose能生還嗎 ? ", s)  # Rose為女性,及坐頭等艙

v = knn.predict(Jack)  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"

print("Jack能生還嗎 ? ", s)  # Jack為男性,及坐三等艙

# 真實的伊西多和伊達·斯特勞斯（Isidor and Ida Straus）夫婦 (You stay, I stay)
# http://www.epochtimes.com/b5/17/12/6/n9931745.htm
# Isidor 美國梅西百貨創辦人之一

print("-----(2)真實的伊西多和伊達·斯特勞斯夫婦的生還推測-------")
Mrs = [[0, 1]]  # 女性 頭等艙 Straus, Mrs. Isidor (Rosalie Ida Blun)
Mr = [[1, 1]]  # 男性 頭等艙 Straus, Mr. Isidor
v = knn.predict(Mrs)  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Straus能生還嗎 ? ", s)  # Ida為女性,及坐頭等艙，可優先搭乘救生艇存活

v = knn.predict(Mr)  # Isidor的生存率有多高呢？  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mr. Straus能生還嗎 ? ", s)

# 真實的 Mrs. Brown
# https://hokkfabrica.com/her-story-margaret-brown-from-titanic/
#

print("-----------(3)真實的Mrs. Brown的生還推測-------------")

# 女性 頭等艙 Brown, Mrs. James Joseph (Margaret Tobin) 故事中的暴發戶 對Jack很友善
Brown = [[0, 1]]
v = knn.predict(Brown)  # Mrs. Brown呢？  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Brown能生還嗎 ? ", s)

print("-------------- (5)若你也搭上了鐵達尼號呢？ ----------------")

# s=input('您的性別（0：女，1：男），請輸入代碼？ ')
s = 1
# c=input('搭乘的船艙艙等（1：S艙，2：C艙，3：Q艙），請輸入代碼？ ')
c = 3
you = [[int(s), int(c)]]
v = knn.predict(you)  # 預測.predict
if v == 1:
    print("預測為:幸運生還")
else:
    print("預測為:無法生還")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10-1 機器學習前準備
# 1. 資料取得

filename = "data/Iris2.csv"
df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

print(df.info())

df = df.drop_duplicates()  # 刪除重複列

df.reset_index(drop=True)  # 將列索引重新編號

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

df["Species"] = df["Species"].map(s)

print(df.info())

# 3. 探索性資料分析
print(df.head())

# 4. 機器學習做資料分析
# 10-2 機器學習實作
# 挑選模型：匯入 K- 平均法模型

from sklearn.cluster import KMeans

# 學習訓練：建立並訓練 K-平均法模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
k = 1

km = KMeans(n_clusters=k)

km.fit(df_X)  # 學習訓練.fit

# 測試評估

print("分群準確性:", km.inertia_)

# 分群準確性: 663.895238095238

s = []
for k in range(1, 15):
    km = KMeans(n_clusters=k)
    km.fit(df_X)  # 學習訓練.fit
    s.append(km.inertia_)

print(s)

# [663.895238095238, 151.77145833333336, 77.91989035087718, 56.64237065018315, 45.816421929824564, 38.380978808131445, 34.1150969785575, 29.771330051212402, 27.730401211361738, 25.771261585636587, 24.236889472455648, 22.68941452991453, 21.258278047116285, 19.7686452991453]

# 看視覺化圖表決定參數K值
df_kmeans = pd.DataFrame()
df_kmeans["inertia_"] = s
df_kmeans.index = list(range(1, 15))
df_kmeans.plot(grid=True)
plt.show()

k = 3
km = KMeans(n_clusters=k)

km.fit(df_X)  # 學習訓練.fit

print("分群的預測結果：")
pred = km.fit_predict(df_X)
print(pred)

# 決定模型
# 進行分群預測

df1 = df_X.copy()
df1["pred"] = pred

c = {0: "r", 1: "g", 2: "b"}

df1["colors"] = df1["pred"].map(c)
df1.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df1["colors"])

plt.show()

# 給一朵鳶尾花的4個特徵值：「花萼長度 6.6公分、花萼寬度 3.1公分、花瓣長度 5.2公分、花寬度 2.4公分」

new = [[6.6, 3.1, 5.2, 2.4]]

v = km.predict(new)  # 預測.predict

print("預測結果為：", v)

# 預測結果為： [0]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

''' 一個很大的範例
"""
探索性數據分析（EDA）

EDA指對已有的數據用可視化等手段探索數據的結構和規律的一種數據分析方法，
其目的是最大化對數據的直覺，完成這個事情的方法是結合統計學的圖形以各種形式展現出來。
在深入機器學習或統計建模之前，EDA是一個重要的步驟，
這是因為它提供了為現有問題開發適當模型并正確解釋其結果所需的來龍去脈。
EDA通常涉及以下幾種方法的組合：
.原始數據集中每個字段的單變量可視化和匯總統計
.數據集中每個變量與感興趣目標變量之間的關系的雙變量可視化和匯總統計
.多元可視化以了解數據中不同字段之間的交互作用
.降維以了解數據,通過將數據折疊成幾個小數據點讓觀察值聚類成有區別的小組，
可以更容易地識別行為模式
"""

import scipy.stats as stats
import sklearn.linear_model as linear_model

# import xgboost as xgb
# from sklearn.cross_validation import KFold
# from IPython.display import HTML, display
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 20

train = pd.read_csv("data/houseprice.csv")
print(train.head(3))

print("訓練數據集基本信息")

# print(train.info())

print(train.shape)

# 訓練數據集基本信息
# (1460, 81)

# 1.1 首先，區分出數據中的數值型變量和類別型變量
# 數值型變量

quantitative = [f for f in train.columns if train.dtypes[f] != "object"]
quantitative.remove("SalePrice")
quantitative.remove("Id")

# 類別型變量

qualitative = [f for f in train.columns if train.dtypes[f] == "object"]

ccs = [
    "FullBath",
    "HalfBath",
    "TotRmsAbvGrd",
    "Fireplaces",
    "GarageYrBlt",
    "GarageCars",
    "OverallQual",
]
for col in ccs:
    if col in quantitative:
        quantitative.remove(col)
    if not col in qualitative:
        qualitative.append(col)

print("訓練集樣本數量：{}".format(train.shape[0]))
print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
訓練集樣本數量：1460
數值型變量共有：29
類別型變量共有：50
"""
# 1.2查看缺失值的分布情況

missing = train.isnull().sum() / train.shape[0]
print(missing.head(3))

missing = missing[missing > 0]
print("有缺失值的變量共有：{}".format(len(missing)))

missing.sort_values(inplace=True)
print("缺失率超過50%的有{}個".format(len(missing[missing >= 0.5])))

print(missing[missing >= 0.5])

missing.plot.bar(figsize=(6, 4))

plt.show()
"""
Id            0.0
MSSubClass    0.0
MSZoning      0.0
dtype: float64
有缺失值的變量共有：19
缺失率超過50%的有4個
Fence          0.807534
Alley          0.937671
MiscFeature    0.963014
PoolQC         0.995205
dtype: float64
"""

# 可以直接刪除這幾個變量

missing_cols = missing[missing >= 0.5].index.tolist()

for col in missing_cols:
    if col in quantitative:
        quantitative.remove(col)
    if col in qualitative:
        qualitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

# 數值型變量共有：29
# 類別型變量共有：46

# 2 數值型變量
# 2.1 查看目標變量saleprice是否服從正態分布

import scipy.stats as st

y = train["SalePrice"]

plt.figure(1)
sns.distplot(y, kde=False)
plt.show()

plt.figure(2)
plt.title("Johnson SU")
sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.show()

plt.figure(3)
plt.title("Normal")
sns.distplot(y, kde=False, fit=st.norm)
plt.show()

plt.figure(4)
plt.title("Log Normal")
sns.distplot(y, kde=False, fit=st.lognorm)
plt.show()

# 另一種查看是否服從正態分布的可視化方法
sns.distplot(train["SalePrice"], fit=st.norm)
plt.show()

res = st.probplot(train["SalePrice"], plot=plt)
plt.show()

# 把房價做對數變換后再看
SalePrice_log = np.log(train["SalePrice"])
# transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm)
plt.show()


res = st.probplot(SalePrice_log, plot=plt)
print(res)

plt.show()


"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))

顯然，房價本身不服從正態分布，是不能直接用來做回歸建模的。但是經過對數轉換之后，就好了很多。
對于其它的數值型變量，也同樣要做分布的正態性檢驗.
檢驗方法就用：夏皮羅-威爾克(Shapiro-Wilk)法檢驗數據正態性,即W檢驗。
"""

check_normality = lambda x: stats.shapiro(x.fillna(0))[1] < 0.01

normal = pd.DataFrame(train[quantitative])
normal = normal.apply(check_normality)
print(normal.sort_values(ascending=False).head(4))

normal = normal < 0.01
print(not normal.any())

"""
YrSold          True
LowQualFinSF    True
LotFrontage     True
LotArea         True
dtype: bool
True

可以發現所有的數值型變量都沒能通過正態性分布檢驗，都需要做轉換。
我們可以把所有的數值型變量的分布曲線都畫出來，從可視化角度進一步驗證這個判斷
"""

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")
plt.show()

df = pd.DataFrame(
    {"A": {0: "a", 1: "b", 2: "c"}, "B": {0: 1, 1: 3, 2: 5}, "C": {0: 2, 1: 4, 2: 6}}
)
print(df)

pd.melt(df, id_vars=["A"], value_vars=["B", "C"])
print(df)

# 看起來TotalBsmtSF, KitchenAbvGr, LotFrontage, LotArea這幾個變量似乎更適合做些變型，以使其服從正態分布。
# 2.2 異常值分析
# 對saleprice做標準化后再看

"""
# NG
saleprice_scaled = StandardScaler().fit_transform(train["SalePrice"][:, np.newaxis])
low_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][:10]
high_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][-10:]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)
"""


"""
outer range (low) of the distribution:
[[-1.83870376]
 [-1.83352844]
 [-1.80092766]
 [-1.78329881]
 [-1.77448439]
 [-1.62337999]
 [-1.61708398]
 [-1.58560389]
 [-1.58560389]
 [-1.5731    ]]

outer range (high) of the distribution:
[[ 3.82897043]
 [ 4.04098249]
 [ 4.49634819]
 [ 4.71041276]
 [ 4.73032076]
 [ 5.06214602]
 [ 5.42383959]
 [ 5.59185509]
 [ 7.10289909]
 [ 7.22881942]]

"""

# 低房價并沒有太多異常，但是高房價有兩個超過了7，雖然不一定是異常值，但是要小心
# 2.3 查看數值型變量和待預測變量之間的相關性
# 常用pearson相關系數，它是用有前提條件，并且是有局限的——判斷線性相關，非線性相關它是無能為力的。
# Spearman相關系數 vs pearson相關系數的優點：對于數據分布沒有要求。也叫秩和。


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")
    return spr


features = quantitative

spr = spearman(train, features)
plt.show()


# 刪除相關系數小于0.3的變量

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

for col in spr[abs(spr["spearman"]) < 0.3].feature:
    if col in quantitative:
        quantitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
數值型變量共有：29
類別型變量共有：46
數值型變量共有：12
類別型變量共有：46
"""

# 2.4 用散點圖觀察數值型變量之間的關系

# scatterplot

from copy import copy

sns.set(font_scale=2)
cols1 = copy(quantitative)
cols1.append("SalePrice")
# plt.figure('a')
sns.pairplot(train[cols1].fillna(0.0), height=2.5)
plt.show()

# scatterplot

sns.set(font_scale=2)

cols1 = copy(quantitative[:6])

cols1.append("SalePrice")

# plt.figure('b')

sns.pairplot(train[cols1].fillna(0.0), height=2.5)

cols2 = copy(quantitative[6:])

cols2.append("SalePrice")

# plt.figure('c')

sns.pairplot(train[cols2].fillna(0.0), height=2.5)

plt.show()

"""
3.類別型變量

對于類別型的變量，要觀察目標變量（sale_price）在類別的各個取值上的分布情況；用分組箱線圖

對于類別型變量的缺失值，不再用0填充，而是用一個特殊的值'Missing'填充。
"""

for c in qualitative:
    train[c] = train[c].astype("category")
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(["MISSING"])
        train[c] = train[c].fillna("MISSING")


def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x = plt.xticks(rotation=90)


f = pd.melt(train, id_vars=["SalePrice"], value_vars=qualitative)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(boxplot, "value", "SalePrice")

plt.show()

"""
看起來像LotConfig、LandSlope這樣的變量，對于房價的影響似乎不大。 Neighborhood對房價有影響。 然后每個類別的不同子類之間看起來似乎也有差別。 overallQual的值太多。

具體到一個分類指標和數值型變量之間的相關關系，我們可以用方差分析進行檢查。
3.2 方差分析
"""


def anova(frame):
    anv = pd.DataFrame()
    anv["feature"] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]["SalePrice"].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")


a = anova(train)
a["disparity"] = np.log(1.0 / a["pval"].values)
sns.barplot(data=a, x="feature", y="disparity")
x = plt.xticks(rotation=90)
plt.show()


"""
這里我們用了方差分析，來看每一個類別變量和預測變量Sale_price之間是否有相關關系。

因為我們最后得到了個p值，p>0.05說明樣本的分組之間沒有顯著性差異，

p值越小說明差異越顯著。

因為我們想用一個類似于“變異度”的指標——“差異度”，我們希望這個指標越大，說明差異越明顯。也就是想要一個同向變化的指標，所以對p值取了個倒數。僅此而已。
3.3 對于這些分類變量的每個值做正確編碼

另一種編碼方式是OneHotEncoding或者dummy
"""


def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering["val"] = frame[feature].unique()
    ordering.index = ordering.val
    ordering["spmean"] = (
        frame[[feature, "SalePrice"]].groupby(feature).mean()["SalePrice"]
    )
    ordering = ordering.sort_values("spmean")
    ordering["ordering"] = range(1, ordering.shape[0] + 1)
    ordering = ordering["ordering"].to_dict()

    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature + "_E"] = o


qual_encoded = []
for q in qualitative:
    encode(train, q)
    qual_encoded.append(q + "_E")

print(qual_encoded)

"""
['MSZoning_E', 'Street_E', 'LotShape_E', 'LandContour_E', 'Utilities_E', 'LotConfig_E', 'LandSlope_E', 'Neighborhood_E', 'Condition1_E', 'Condition2_E', 'BldgType_E', 'HouseStyle_E', 'RoofStyle_E', 'RoofMatl_E', 'Exterior1st_E', 'Exterior2nd_E', 'MasVnrType_E', 'ExterQual_E', 'ExterCond_E', 'Foundation_E', 'BsmtQual_E', 'BsmtCond_E', 'BsmtExposure_E', 'BsmtFinType1_E', 'BsmtFinType2_E', 'Heating_E', 'HeatingQC_E', 'CentralAir_E', 'Electrical_E', 'KitchenQual_E', 'Functional_E', 'FireplaceQu_E', 'GarageType_E', 'GarageFinish_E', 'GarageQual_E', 'GarageCond_E', 'PavedDrive_E', 'SaleType_E', 'SaleCondition_E', 'FullBath_E', 'HalfBath_E', 'TotRmsAbvGrd_E', 'Fireplaces_E', 'GarageYrBlt_E', 'GarageCars_E', 'OverallQual_E']
"""
print(train.head(3))

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PavedDrive_E	SaleType_E	SaleCondition_E	FullBath_E	HalfBath_E	TotRmsAbvGrd_E	Fireplaces_E	GarageYrBlt_E	GarageCars_E	OverallQual_E
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	8.0	1.0	86.0	3.0	7.0
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	2.0	5.0	2.0	57.0	3.0	6.0
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	5.0	2.0	91.0	3.0	7.0
,

3 rows × 127 columns
,

"""

print(train["GarageQual_E"].value_counts())

"""
4.0    1311
,2.0      81
,3.0      48
,5.0      14
,6.0       3
,1.0       3
,Name: GarageQual_E, dtype: int64

3.4.查看衍生變量和房價的Spearman相關性

對于相關性的檢測我們使用的是Spearman correlation，這種檢驗方法的好處是即使是非線性相關也能檢測出來。
"""

sns.set(font_scale=1.2)


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")


features = qual_encoded
spearman(train, features)
plt.show()

"""
顯然，OverallQual和房價的關系最明顯。房子的鄰居和位置看起來也是有影響的。
3.5 觀察變量之間的相關性

回歸模型對于變量共線的容忍度差，所以，我們需要考慮變量之間的相關性。用相關系數矩陣的熱力圖即可。
"""

sns.set(font_scale=1)

plt.figure(1)

corr = train[quantitative + ["SalePrice"]].corr("spearman")

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

# from functools import partial
# # my_heatmap=partial(sns.heatmap,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

plt.figure(2)
corr = train[qual_encoded + ["SalePrice"]].corr()
sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

plt.figure(3)
corr = pd.DataFrame(
    np.zeros([len(quantitative) + 1, len(qual_encoded) + 1]),
    index=quantitative + ["SalePrice"],
    columns=qual_encoded + ["SalePrice"],
)
for q1 in quantitative + ["SalePrice"]:
    for q2 in qual_encoded + ["SalePrice"]:
        corr.loc[q1, q2] = train[q1].corr(train[q2])

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

"""
3.6 觀察所有變量（包括衍生變量）和目標變量之間的關系

現在所有類別型變量也做了重新編碼，編碼成數值型。所有所有的特征都可以看作是數值型的了。于是，我們可以再次全景式觀察變量和目標變量之間的關系。
"""


def pairplot(x, y, **kwargs):
    ax = plt.gca()
    ts = pd.DataFrame({"time": x, "val": y})
    ts = ts.groupby("time").mean()
    ts.plot(ax=ax)
    plt.xticks(rotation=90)


# 畫散點圖
sns.set(style="ticks", color_codes=True)

f = pd.melt(train, id_vars=["SalePrice"], value_vars=quantitative + qual_encoded)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(pairplot, "value", "SalePrice")

plt.show()

"""
看起來，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E There are lots of nonlinearities this may be the cause why some variables wont be selected by Lasso/Lars. Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E look like they would benefit from adding quadratic term to regression. But on the other hand this will most probably provoke overfit.

觀察的結果提示我們，有些變量可以嘗試做些變換，比如平方變換。
4.高級內容

考慮數據本身是否分群，如果分群，就可以用分段回歸。

接下來，考慮是否可以分段進行回歸。

我們把房價200000作為分界點，之下的作為普通住宅，之上的作為豪宅，然后看看在這樣分開后，那些數值型變量的均值有多大差異。
"""

features = quantitative
standard = train[train["SalePrice"] < 200000]
pricey = train[train["SalePrice"] >= 200000]

diff = pd.DataFrame()
diff["feature"] = features
diff["difference"] = [
    (pricey[f].fillna(0.0).mean() - standard[f].fillna(0.0).mean())
    / (standard[f].fillna(0.0).mean())
    for f in features
]

sns.barplot(data=diff, x="feature", y="difference")
x = plt.xticks(rotation=90)

print(diff)

plt.show()

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	feature	difference
0	MSSubClass	-0.150366
1	LotFrontage	0.238321
2	LotArea	0.536645
3	OverallQual	0.361440
4	OverallCond	-0.047635
5	YearBuilt	0.015026
6	YearRemodAdd	0.010197
7	MasVnrArea	2.029480
8	BsmtFinSF1	0.729316
9	BsmtFinSF2	-0.023328
10	BsmtUnfSF	0.410808
11	TotalBsmtSF	0.515235
12	1stFlrSF	0.396664
13	2ndFlrSF	0.978444
14	LowQualFinSF	-0.298300
15	GrLivArea	0.512153
16	BsmtFullBath	0.577215
17	BsmtHalfBath	-0.487756
18	FullBath	0.424714
19	HalfBath	0.684120
20	BedroomAbvGr	0.092859
21	KitchenAbvGr	-0.050115
22	TotRmsAbvGrd	0.257338
23	Fireplaces	1.102258
24	GarageYrBlt	0.090733
25	GarageCars	0.550690
26	GarageArea	0.596397
27	WoodDeckSF	0.950341
28	OpenPorchSF	1.314906
29	EnclosedPorch	-0.479096
30	3SsnPorch	0.881312
31	ScreenPorch	0.623489
32	PoolArea	2.213669
33	MiscVal	-0.559517
34	MoSold	0.052589
35	YrSold	-0.000021
,

我們用tnse方法，把每個高維樣本映射到二維平面上的點。

然后我們對樣本做標準化處理，處理之后做PCA，提取前30個主成分。也就是把樣本的特征降維到30個特征。

對這30個特征的樣本聚類，聚成5類。

在把這5類用可視化的方法會出來，看看是否有聚集趨勢。
"""

features = quantitative + qual_encoded
model = TSNE(n_components=2, random_state=0, perplexity=50)
X = train[features].fillna(0.0).values
tsne = model.fit_transform(X)

std = StandardScaler()
s = std.fit_transform(X)

pca = PCA(n_components=40)

pca.fit(s)  # 學習訓練.fit

pc = pca.transform(s)

kmeans = KMeans(n_clusters=5)

kmeans.fit(pc)  # 學習訓練.fit

fr = pd.DataFrame({"tsne1": tsne[:, 0], "tsne2": tsne[:, 1], "cluster": kmeans.labels_})
sns.lmplot(data=fr, x="tsne1", y="tsne2", hue="cluster", fit_reg=False)

plt.show()

print(np.sum(pca.explained_variance_ratio_))

"""
0.846903058622
看起來聚集趨勢并不明顯，所以分段回歸的意義似乎不大。
另外40個主成分能解釋84%的方差。
"""

y = train["SalePrice"].values


def johnson(y):
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)
    yt = gamma + eta * np.arcsinh((y - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon


yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

plt.figure(1)
sns.distplot(yt)

plt.figure(2)
sns.distplot(yt2)

plt.show()

# 5.最后建模


def error(actual, predicted):
    actual = np.log(actual)
    predicted = np.log(predicted)
    return np.sqrt(np.sum(np.square(actual - predicted)) / len(actual))


def log_transform(feature):
    train[feature] = np.log1p(train[feature].values)


def quadratic(feature):
    train[feature + "2"] = train[feature] ** 2


# 下面這些特征做log轉化
log_transform("GrLivArea")
log_transform("1stFlrSF")
log_transform("2ndFlrSF")
log_transform("TotalBsmtSF")
log_transform("LotArea")
log_transform("LotFrontage")
log_transform("KitchenAbvGr")
log_transform("GarageArea")

# 下面這些特征取平方轉換
# quadratic('OverallQual') fail
quadratic("YearBuilt")
quadratic("YearRemodAdd")
quadratic("TotalBsmtSF")
quadratic("2ndFlrSF")
quadratic("Neighborhood_E")
quadratic("RoofMatl_E")
quadratic("GrLivArea")

qdr = [
    "OverallQual2",
    "YearBuilt2",
    "YearRemodAdd2",
    "TotalBsmtSF2",
    "2ndFlrSF2",
    "Neighborhood_E2",
    "RoofMatl_E2",
    "GrLivArea2",
]

# 下面這些特征做二值化
train["HasBasement"] = train["TotalBsmtSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasGarage"] = train["GarageArea"].apply(lambda x: 1 if x > 0 else 0)
train["Has2ndFloor"] = train["2ndFlrSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasMasVnr"] = train["MasVnrArea"].apply(lambda x: 1 if x > 0 else 0)
train["HasWoodDeck"] = train["WoodDeckSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPorch"] = train["OpenPorchSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPool"] = train["PoolArea"].apply(lambda x: 1 if x > 0 else 0)
train["IsNew"] = train["YearBuilt"].apply(lambda x: 1 if x > 2000 else 0)

boolean = [
    "HasBasement",
    "HasGarage",
    "Has2ndFloor",
    "HasMasVnr",
    "HasWoodDeck",
    "HasPorch",
    "HasPool",
    "IsNew",
]

features = quantitative + qual_encoded + boolean + qdr
lasso = linear_model.LassoLarsCV(max_iter=10000)

""" NG
# sklearn中要求X，y都是矩陣形式，而不是數據框
X = train[features].fillna(0.).values
Y = train['SalePrice'].values

lasso.fit(X, np.log(Y))  # 學習訓練.fit

#反log1p變換
Ypred = np.exp(lasso.predict(X))  # 預測.predict
print(error(Y, Ypred))

"""
# 一個很大的範例
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

"""
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

kmeans = cluster.KMeans(n_clusters=k, random_state=9487)

kmeans.fit(df)  # 學習訓練.fit

print(kmeans.labels_)

colmap = np.array(["r", "g", "y"])
plt.scatter(df["length"], df["weight"], color=colmap[kmeans.labels_])

plt.show()
"""
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
automl.fit(X_train, y_train)  # 學習訓練.fit
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
print("------------------------------------------------------------")  # 60個
"""
# titanic ST

# 數據集和數據處理

from pandas import Series, DataFrame

# 繪圖分析
sns.set_style("whitegrid")

# 機器學習
from sklearn.linear_model import LogisticRegression  # 邏輯迴歸
from sklearn.svm import SVC, LinearSVC  # 支持向量機
from sklearn.ensemble import RandomForestClassifier  # 隨機森林

# from sklearn.neighbors import KneighborsClassifier # K近鄰演算法（K Nearest Neighbor）
from sklearn.naive_bayes import GaussianNB  # 數據集和數據處理

print("------------------------------")	#30個

titanic_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.describe())

facet = sns.FacetGrid(titanic_df, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, titanic_df["Age"].max()))
facet.add_legend()
plt.show()

fig, axis1 = plt.subplots(1, 1, figsize=(18, 4))
average_age = titanic_df[["Age", "Survived"]].groupby(["Age"], as_index=False).mean()
sns.barplot(x="Age", y="Survived", data=average_age)
plt.show()

print("------------------------------")	#30個


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

print("------------------------------")	#30個

# 生成模型所需的訓練集和測試集
X_train = titanic_df.drop("Survived", axis=1)
Y_train = titanic_df["Survived"]
X_test = test_df.copy()

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()  # 初始化模型

logreg.fit(X_train, Y_train)  # 學習訓練.fit

print(logreg.score(X_train, Y_train))  # 模型評分

Y_pred = logreg.predict(X_test)  # 預測
"""
print("------------------------------------------------------------")  # 60個
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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

x_train = x_train.fillna(x.mean()) # 空值填充訓練集
x_val = x_val.fillna(x.mean()) # 空值填充驗證集
x_test = test.fillna(x.mean()) # 空值填充測試集
x = x.fillna(x.mean()) # 空值填充全集

print('------------------------------------------------------------')	#60個

# 訓練模型生成提交數據

#clf = RandomForestRegressor(criterion='mse', random_state=9487) # 隨機森林迴歸
#clf = GradientBoostingClassifier(criterion='mse',random_state=9487) # GBDT分類
clf = GradientBoostingRegressor(criterion='mse', random_state=9487) # GBDT迴歸

if True: # 用於本地測試
    clf.fit(x_train, y_train)  # 學習訓練.fit
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val)])
    print("MSE: %.4f" % mse)
else: # 用於遠程提交
    clf.fit(x, y) # 全量數據訓練  # 學習訓練.fit
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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

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
kf = KFold(len(data), n_folds = 5, shuffle=True, random_state=9487) # 5折交叉驗證
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
    clf = GradientBoostingRegressor(criterion='mse', random_state=9487)
    clf.fit(x_train[features_new], y_train)  # 學習訓練.fit
    mse = mean_squared_error(y_val, [round(i) for i in clf.predict(x_val[features_new])])
    if mse < baseline:
        print("remove", i, "MSE: %.4f" % mse)

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
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
scaler = StandardScaler().fit(X)  # 學習訓練.fit
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
scaler = Normalizer().fit(X)  # 學習訓練.fit
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
binarizer = Binarizer(threshold=0.0).fit(X)  # 學習訓練.fit
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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 製造像真的一様的數據
N = 500
GROUPS = 3
x, y = make_blobs(n_samples=N, centers=GROUPS, n_features=2, random_state=9487)
plt.scatter(x[:, 0], x[:, 1], c=y)

plt.show()

print("------------------------------")  # 30個

# Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

print("使用 SVC")
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
clf = SVC()
# clf = SVC(gamma = 'scale')

scores = cross_val_score(clf, x, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------")  # 30個

print("使用 Decision Tree")
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

scores = cross_val_score(clf, x, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------")  # 30個

print("使用 Random Forest")

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)

scores = cross_val_score(clf, x, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x, y = datasets.make_regression(n_features=1, noise=20)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

plt.show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 訓練組8成, 測試組2成

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析  # 學習訓練.fit
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析  # 學習訓練.fit
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="*", color="red")
plt.title("無監督學習")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=9487)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
lo_model = LogisticRegression()

# 建立訓練數據模型
lo_model.fit(dx_train, label_train)  # 學習訓練.fit

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
print("------------------------------------------------------------")  # 60個

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=9487)
print(data)
print(label)
print(f"分類 : {label}")

plt.scatter(data[:, 0], data[:, 1], c=label, cmap="bwr")
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=9487)

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

print(f"特徵數據外形 : {d_sta.shape}")
print(f"訓練數據外形 : {dx_train.shape}")
print(f"測試數據外形 : {dx_test.shape}")
print(f"標籤數據外形 : {label.shape}")
print(f"訓練數據外形 : {label_train.shape}")
print(f"測試數據外形 : {label_test.shape}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor）

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
k_model = KNeighborsClassifier(n_neighbors=5)  # k = 5  # K近鄰演算法（K Nearest Neighbor）

# 建立訓練數據模型
k_model.fit(dx_train, label_train)  # 學習訓練.fit

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
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
lo_model = LogisticRegression()

# 建立訓練數據模型
lo_model.fit(dx_train, label_train)  # 學習訓練.fit

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
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
svm_model = LinearSVC()

# 建立訓練數據模型
svm_model.fit(dx_train, label_train)  # 學習訓練.fit

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
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC

data, label = make_moons(n_samples=200, noise=0.2, random_state=9487)

d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm_model = LinearSVC()

svm_model.fit(dx_train, label_train)  # 學習訓練.fit

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

data, label = datasets.load_iris(return_X_y=True)

print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")

print("------------------------------------------------------------")  # 60個

from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

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
print("------------------------------------------------------------")  # 60個

from sklearn.ensemble import RandomForestClassifier

data, label = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

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

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=9487
)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=9487
)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=9487
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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
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

plt.show()

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

plt.show()
"""
print("------------------------------------------------------------")  # 60個
"""
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

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

df = pd.read_csv("data/test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# titanic

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

# titanic SP
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import neighbors, datasets, preprocessing
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data[:, :2], iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

# Standardize the features using StandardScaler
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Create a K-Nearest Neighbors classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=5)  # K近鄰演算法（K Nearest Neighbor）

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

iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data, iris.target

# Print the lengths of X and y
print("Size of X:", X.shape)  #  (150, 4)
print("Size of y:", y.shape)  #  (150, )

# Split the data into training and test sets with test_size=0.2 (20% for test set)
X, y = iris.data, iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

# Print the sizes of the arrays
print("Size of X_train:", X_train.shape)
print("Size of X_test: ", X_test.shape)
print("Size of y_train:", y_train.shape)
print("Size of y_test: ", y_test.shape)

print("------------------------------------------------------------")  # 60個

# Create instances of the models

# Import necessary classes from sklearn libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor）
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Create instances of supervised learning models
# Logistic Regression classifier (max_iter=1000)
lr = LogisticRegression(max_iter=1000)

# k-Nearest Neighbors classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)  # K近鄰演算法（K Nearest Neighbor）

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
"""
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
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)
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
print("------------------------------------------------------------")  # 60個

# 加載數據
data = pd.read_csv("datasets/pima-indians-diabetes/diabetes.csv")
print("dataset shape {}".format(data.shape))

print(data.head())

print(data.groupby("Outcome").size())

X = data.iloc[:, 0:8]
Y = data.iloc[:, 8]
print("shape of X {}; shape of Y {}".format(X.shape, Y.shape))


# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier

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

knn = KNeighborsClassifier(n_neighbors=2)  # K近鄰演算法（K Nearest Neighbor）
knn.fit(X_train, Y_train)
train_score = knn.score(X_train, Y_train)
test_score = knn.score(X_test, Y_test)
print("train score: {}; test score: {}".format(train_score, test_score))

from sklearn.model_selection import ShuffleSplit
from common.utils import plot_learning_curve

knn = KNeighborsClassifier(n_neighbors=2)  # K近鄰演算法（K Nearest Neighbor）
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)
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
print("------------------------------------------------------------")  # 60個
"""
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

plt.figure(figsize=(12, 8), subplotpars=SubplotParams(hspace=0.3))
for i, r in enumerate(results):
    fig = plt.subplot(2, 2, i + 1)
    plt.xlim(-8, 8)
    plt.title("LinearRegression degree={}".format(r["degree"]))
    plt.scatter(X, Y, s=5, c="b", alpha=0.5)
    plt.plot(X, r["model"].predict(X), "r-")

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print("titanic ST")


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


train = read_dataset("datasets/titanic/train.csv") # 共891筆資料, 8欄位
print(train.head())

# 把 "Survived"欄位拿出來當訓練目標 => y
y = train["Survived"].values

# 把 "Survived"欄位從原訓練資料移除 => X
X = train.drop(["Survived"], axis=1).values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)

print("train_score :", train_score)
print("test_score :", test_score)

print("------------------------------")  # 30個

from sklearn.tree import export_graphviz

with open("tmp_titanic1.dot", "w") as f:
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

plt.figure(figsize=(10, 6))
plt.grid()
plt.xlabel("max depth of decision tree")
plt.ylabel("score")
plt.plot(depths, cv_scores, ".g-", label="cross-validation score")
plt.plot(depths, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------")  # 30個

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
plt.figure(figsize=(10, 6))
plt.grid()
plt.xlabel("threshold of entropy")
plt.ylabel("score")
plt.plot(values, cv_scores, ".g-", label="cross-validation score")
plt.plot(values, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------")  # 30個


def plot_curve(train_sizes, cv_results, xlabel):
    train_scores_mean = cv_results["mean_train_score"]
    train_scores_std = cv_results["std_train_score"]
    test_scores_mean = cv_results["mean_test_score"]
    test_scores_std = cv_results["std_test_score"]
    plt.figure(figsize=(10, 6))
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

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

print("生成決策樹圖形")

clf = DecisionTreeClassifier(
    criterion="entropy", min_impurity_decrease=0.002857142857142857
)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

# 導出 titanic.dot 文件
with open("tmp_titanic2.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png
"""

print("titanic SP")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4]])

plt.figure(figsize=(8, 6))

plt.title("Decision Boundary")

plt.xlim(0, 8)
plt.ylim(0, 6)

ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")

plt.plot([1, 5], [5, 1], "r-")
plt.arrow(4, 4, -1, -1, shape="full", color="r")

plt.plot([3, 3], [0.5, 6], "b--")
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

print("------------------------------")  # 30個

plt.figure(figsize=(8, 6))

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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
plt.figure(figsize=(13, 6))

# sub plot 1
plt.subplot(1, 2, 1)

X, y = make_blobs(
    n_samples=100,
    n_features=2,
    centers=[(1, 1), (2, 2)],
    random_state=9487,
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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
plt.figure(figsize=(8, 4))

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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
plt.figure(figsize=(13, 6))

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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
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


X, y = make_blobs(n_samples=100, centers=2, random_state=9487, cluster_std=0.3)
clf = sklearn.svm.SVC(C=1.0, kernel="linear")
clf.fit(X, y)

plt.figure(figsize=(12, 4))
plot_hyperplane(clf, X, y, h=0.01, title="Maximum Margin Hyperplan")

plt.show()

print("------------------------------")  # 30個

X, y = make_blobs(n_samples=100, centers=3, random_state=9487, cluster_std=0.8)
clf_linear = sklearn.svm.SVC(C=1.0, kernel="linear")
clf_poly = sklearn.svm.SVC(C=1.0, kernel="poly", degree=3)
clf_rbf = sklearn.svm.SVC(C=1.0, kernel="rbf", gamma=0.5)
clf_rbf2 = sklearn.svm.SVC(C=1.0, kernel="rbf", gamma=0.1)

plt.figure(figsize=(10, 10))

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
"""
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
plt.figure(figsize=(8, 8))
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
print("------------------------------------------------------------")  # 60個
"""
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

print("------------------------------")  # 30個

print("降維及恢復示意圖")

plt.figure(figsize=(8, 8))

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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
X, y = make_blobs(
    n_samples=200,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=9487,
)

plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker="o")

plt.show()

print("------------------------------")  # 30個

from sklearn.cluster import KMeans

n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.score(X))))

labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ["o", "^", "*"]
colors = ["r", "b", "y"]

plt.figure(figsize=(6, 4))
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

print("------------------------------")  # 30個


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

plt.figure(figsize=(10, 3))
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from time import time
from sklearn.datasets import load_files

""" NG 無檔案
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

terms = vectorizer.get_feature_names_out()
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# plt.rcParams['figure.figsize'] = 12, 8

np.random.seed(3)
np.random.seed(10)  # Setting seed for reproducability
np.random.seed(3)
