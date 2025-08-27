"""
feature_extraction

from sklearn.feature_extraction.text import CountVectorizer

實際上TFIDF分成兩個部份，TF和IDF。
分別表示
詞頻（term frequency，tf）和逆向檔案頻率（inverse document frequency，idf）

和Word2Vec一樣，是種將文字轉換為向量的方式

接著簡單介紹TF和IDF這兩個部份，理解也有助於使用scikit-learn裡的TFIDF。

TFIDF最常被使用的一個目的是，找到文件當中的關鍵字。怎樣的關鍵字是重要的？
一個直覺的想法是出現最多次的字。
這可能可以，不過因為每個文件的字數不同，無法比較。
所以在用文件內的字數作為分母，將所有文件得到數值加以規範化。
這也就是TF，特定單字在文件出現次數/文件總次數

不過只是這樣，很有可能讓一些定冠詞，或是常用單字，像是a, an, the, and, or 等等，
得到很高的分數。一個簡單的作法是先把這些字詞去掉(stopword)，
不過還有一種方式是將低這些單字的分數。
IDF會去計算一個字出現在文件的逆向頻率，這表示出現頻率越高，出現在越多文件之中，
但是得分會越低。透過TF和IDF相乘：TFxIDF，得到的綜合分數就是TFIDF。
"""

"""
tfidf

sklearn: TfidfVectorizer 中文处理及一些使用参数

TfidfVectorizer可以把原始文本转化为tf-idf的特征矩阵，从而为后续的文本相似度计算，
主题模型(如LSI)，文本搜索排序等一系列应用奠定基础。
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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

import jieba
import sklearn.linear_model
from sklearn.metrics import accuracy_score  # 正解率
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 分類特徵(Categorical Features)

data = [
    {"price": 850000, "rooms": 4, "neighborhood": "Queen Anne"},
    {"price": 700000, "rooms": 3, "neighborhood": "Fremont"},
    {"price": 650000, "rooms": 3, "neighborhood": "Wallingford"},
    {"price": 600000, "rooms": 2, "neighborhood": "Fremont"},
]
print(data)

# 利用one-hot encoding編碼的方式，可以有效率的判斷所指示值為1或0代表存在或不存在。

# DictVectorizer 对使用字典储存的数据进行特征提取与向量化
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False, dtype=int)
dv.fit_transform(data)
print(data)

# 查看vec每列的含義，可以檢查功能名稱：
print("特徵名稱 :\n", dv.get_feature_names_out(), sep="")

# 將sparse更改為True，可以解決為稀疏矩陣的問題
dv = DictVectorizer(sparse=True, dtype=int)
dv.fit_transform(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DictVectorizer 对使用字典储存的数据进行特征提取与向量化

print("DictVectorizer, sparse=True")  # 可以解決為稀疏矩陣的問題
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=True)
X = dv.fit_transform(
    [{"膚色": "黃", "身高": 176}, {"膚色": "白", "身高": 183}, {"膚色": "黑", "身高": 158}]
)
print("sparse編碼：")
print(X)

print("特徵名稱 :\n", dv.get_feature_names_out(), sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DictVectorizer 对使用字典储存的数据进行特征提取与向量化

print("DictVectorizer, sparse=False")
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(
    [{"膚色": "黃", "身高": 176}, {"膚色": "白", "身高": 183}, {"膚色": "黑", "身高": 158}]
)
print("one-hot編碼：")
print(X)

print("特徵名稱 :\n", dv.get_feature_names_out(), sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
X = cv.fit_transform(
    ["code is is easy, i like python", "code is too hard, i dislike python"]
)
print("one-hot編碼 :", X.toarray())

print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

texts = ["dog and fish, dog and dog", "dog and dog", "dog and cat"]

cv = CountVectorizer(ngram_range=(1, 1), stop_words="english")
count_train = cv.fit_transform(texts)
print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")
print(cv.vocabulary_)
print(count_train)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "One of the confiscated drafts was a story about stoning women to death for adultery – never published, never presented to anyone, the article stated. The narrative followed the story of a protagonist that watched a movie about stoning of women under Islamic law for adultery."
]

cv = CountVectorizer(ngram_range=(1, 2), stop_words="english")
count_train = cv.fit_transform(texts)
print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")
print(cv.vocabulary_)
print(count_train)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from sklearn.feature_extraction.text import CountVectorizer
import joblib

cv = joblib.load("count_vectorizer.pkl")
classifier = joblib.load("classifier.pkl")


def classify(document):
    label = {0: "reliable", 1: "unreliable"}
    document_text = cv.transform([document])
    y = classifier.predict(document_text)[0]
    return label[y]


document = input("Please enter your news description:")
print("This news review is " + classify(document) + ".")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

tv = TfidfVectorizer()

X = tv.fit_transform(texts)  # fit+transform

""" 不等於??
tv.fit(texts)
X = tv.transform(texts)     # 得到tf-idf矩阵，稀疏矩阵表示法
"""
print("特徵名稱 :\n", tv.get_feature_names_out(), sep="")

print(X)

print(X.shape)
# (4, 9)

print(X.todense())  # 转化为更直观的一般矩阵

print(tv.vocabulary_)  # 词语与列的对应关系
# {'have': 2, 'pen': 3, 'an': 0, 'apple': 1}

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

texts = ["I have a pen.", "I have an apple."]

tv = TfidfVectorizer().fit(texts)

X = tv.transform(texts)  # 得到tf-idf矩阵，稀疏矩阵表示法
print(X)
print(X.shape)
# (0, 3)	0.814802474667   # 第0个字符串，对应词典序号为3的词的TFIDF为0.8148
# (0, 2)	0.579738671538
# (1, 2)	0.449436416524
# (1, 1)	0.631667201738
# (1, 0)	0.631667201738

print(X.todense())  # 转化为更直观的一般矩阵
# [[ 0.          0.          0.57973867  0.81480247]
#  [ 0.6316672   0.6316672   0.44943642  0.        ]]

print(tv.vocabulary_)  # 词语与列的对应关系
# {'have': 2, 'pen': 3, 'an': 0, 'apple': 1}

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


t1 = list(jieba.cut("今天台北天氣晴朗，風景區擠滿了人潮。"))
t2 = list(jieba.cut("台北的天氣常常下雨。"))
c1 = " ".join(t1)
c2 = " ".join(t2)
print("第一句分詞： {}".format(c1))
print("第二句分詞： {}".format(c2))

print("------------------------------")  # 30個

print("使用TV")
from sklearn.feature_extraction.text import TfidfVectorizer

tv = TfidfVectorizer()

X = tv.fit_transform([c1, c2])

print("one-hot編碼 :", X.toarray())

print("特徵名稱 :\n", tv.get_feature_names_out(), sep="")

print("------------------------------")  # 30個

print("使用CV")

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
X = cv.fit_transform([c1, c2])

print("one-hot編碼 :", X.toarray())

print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")

print("------------------------------------------------------------")  # 60個

print("TF-IDF逆文本頻率指數")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

arr = [
    "第一天我參觀了美術館",
    "第二天我參觀了博物館",
    "第三天我參觀了動物園",
]

arr = [" ".join(jieba.cut(i)) for i in arr]  # 分詞
print(arr)

cv = CountVectorizer()
X = cv.fit_transform(arr)
word = cv.get_feature_names_out()

df = pd.DataFrame(X.toarray(), columns=word)
print(df)

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
weight = tfidf.toarray()
for i in range(len(weight)):  # 訪問每一句
    print("第{}句：".format(i))
    for j in range(len(word)):  # 訪問每個詞
        if weight[i][j] > 0.05:  # 只顯示重要關鍵字
            print(word[j], round(weight[i][j], 2))  # 保留兩位小數

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("比較字串的距離")

from sklearn.feature_extraction.text import CountVectorizer

texts = ["I am a good student", "I am a good teacher", "This is a pencil"]

cv = CountVectorizer()
counts = cv.fit_transform(texts).todense()  # 得到 texts 的特征向量，並將其轉為密集矩陣
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

from sklearn.metrics.pairwise import euclidean_distances

# 計算任兩個向量間的歐幾里德距離
print("Euclidean distances:")
distances_similarity_metrix = euclidean_distances(feature_vectors)
print(distances_similarity_metrix)
print()

from sklearn.metrics.pairwise import cosine_similarity

# 計算任兩個向量間的餘弦相似度
print("Cosine similarity:")
cosine_similarity_metrix = cosine_similarity(feature_vectors)
print(cosine_similarity_metrix)
print()

print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

text = ["小貝來到北京清華大學", "小花來到了網易杭研大廈", "小明碩士畢業于中國科學院", "小明愛北京小明愛北京天安門"]

texts = [
    "小貝 來到 北京 清華大學",
    "小花 來到 了 網易 杭研 大廈",
    "小明 碩士 畢業 于 中國 科學院",
    "小明 愛 北京 小明 愛 北京 天安門",
]

print("二值化、詞頻")
cv = CountVectorizer(min_df=1, binary=True)  # Transformer
X = cv.fit_transform(texts)
features = cv.get_feature_names_out()
for word in features:
    print(word)
print(len(features))

print(X.todense())

doc_df = pd.DataFrame(X.toarray(), index=text, columns=cv.get_feature_names_out()).head(
    10
)

print(doc_df)
print(doc_df.columns)

print("------------------------------")  # 30個

from sklearn.metrics.pairwise import cosine_similarity

cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index=text, columns=text)
print(sims_df)

print("------------------------------")  # 30個

# tf-idf

tv = TfidfVectorizer(min_df=1)

X = tv.fit_transform(texts)

print("特徵名稱 :\n", tv.get_feature_names_out(), sep="")

pd.set_option("display.precision", 2)
doc_df = pd.DataFrame(X.toarray(), index=text, columns=tv.get_feature_names_out()).head(
    10
)
print(doc_df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用 BOW 猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 載入資料

with open("./data/news.txt", "r+", encoding="UTF-8") as f:
    text = f.read()
# print(text)

# BOW 轉換
cv = CountVectorizer()
X = cv.fit_transform([text])
# 生字表

print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")

print("單字對應的出現次數")
print("one-hot編碼 :", X.toarray())

print("找出較常出現的單字")

import collections

MAX_FEATURES = 20
word_freqs = collections.Counter()
for word, freq in zip(cv.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")

print("考慮停用詞(Stop words)")

MAX_FEATURES = 20

# 轉換為 BOW
cv = CountVectorizer(stop_words="english")
X = cv.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(cv.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")

print("詞形還原(Lemmatization)")

text = text.lower().replace("korean", "korea").replace("stores", "store")

MAX_FEATURES = 20

# 轉換為 BOW
cv = CountVectorizer(stop_words="english")
X = cv.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(cv.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用 BOW 猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 測試資料

texts = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# BOW 轉換
cv = CountVectorizer()

X = cv.fit_transform(texts)

# 生字表
print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")

print("使用表格呈現單字及對應出現的次數")

df = pd.DataFrame(X.toarray(), columns=cv.get_feature_names_out())
print(df)

print("相似性比較")
from sklearn.metrics.pairwise import cosine_similarity

cc = cosine_similarity(df.iloc[-1:].values, df.iloc[:-1].values)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

texts = [
    "Python is popular in machine learning",
    "Distributed system is important in big data analysis",
    "Machine learning is theoretical foundation of data mining",
    "Learning Python is fun",
    "Playing soccer is fun",
    "Many data scientists like playing soccer",
    "Chinese men's soccer team failed again",
    "Thirty two soccer teams enter World Cup finals",
]

cv = CountVectorizer(min_df=1, stop_words="english")

X = cv.fit_transform(texts)

print("特徵名稱 :\n", cv.get_feature_names_out(), sep="")

df = pd.DataFrame(X.toarray(), index=texts, columns=cv.get_feature_names_out()).head(10)
print(df)

print("------------------------------")  # 30個

# Singular value decomposition and LSA
model = TruncatedSVD(2)
data_n = model.fit_transform(X)
data_n = Normalizer(copy=False).fit_transform(data_n)
print(data_n)

df = pd.DataFrame(data_n, index=texts, columns=["component_1", "component_2"])
print(df)

xs = data_n[:, 0]
ys = data_n[:, 1]

plt.figure(figsize=(4, 4))

ax = plt.gca()
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])

plt.scatter(xs, ys)
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
plt.title("Plot of points agains LSA principal components")

show()

print("------------------------------")  # 30個

similarity = np.asarray(np.asmatrix(data_n) * np.asmatrix(data_n).T)
df = pd.DataFrame(similarity, index=texts, columns=texts).head(10)
print(df)

print(similarity)

sns.heatmap(similarity, cmap="Reds")

show()

df = pd.DataFrame(
    model.components_,
    index=["component_1", "component_2"],
    columns=cv.get_feature_names_out(),
)
print(df.T)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print("假新聞資料集, 要做很久")

from sklearn.feature_extraction.text import CountVectorizer
import joblib

# 檔案在
# https://www.kaggle.com/competitions/fake-news/data?select=train.csv

train_df = pd.read_csv("D:/_git/vcs/_big_files/fake-news/train.csv")

train_df.dropna()

train_text = train_df["text"].astype(str)
train_label = train_df["label"]

cv = CountVectorizer(ngram_range=(1, 2), stop_words="english")
count_train = cv.fit_transform(train_text)

# 資料分割
X_train, X_test, Y_train, Y_test = train_test_split(
    count_train, train_label, test_size=0.2
)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, Y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict

print(f"計算準確率 : {accuracy_score(Y_test, y_pred)*100:.2f}%")

print("將 模型存檔 使用 joblib")
joblib.dump(count_vectorizer, "tmp_count_vectorizer.pkl")
joblib.dump(logistic_regression, "tmp_logistic_regression.pkl")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_files

""" NG 無檔案
print("loading documents ...")
t = time.time()
docs = load_files('datasets/clustering/data')
print("summary: {0} documents in {1} categories.".format(
    len(docs.data), len(docs.target_names)))
print("done in {0} seconds".format(time.time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print("vectorizing documents ...")
t = time.time()
tv = TfidfVectorizer(max_df=0.4, 
                             min_df=2, 
                             max_features=max_features, 
                             encoding='latin-1')

X = tv.fit_transform((d for d in docs.data))

print("n_samples: %d, n_features: %d" % X.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    docs.filenames[0], X[0].getnnz()))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

print("clustering documents ...")
t = time.time()
n_clusters = 4
clf = KMeans(n_clusters=n_clusters, 
               max_iter=100,
               tol=0.01,
               verbose=1,
               n_init=3)
clf.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(clf.inertia_)))
print("done in {0} seconds".format(time.time() - t))

print(len(clf.labels_))

cc = clf.labels_[1000:1010]
print(cc)

cc = docs.filenames[1000:1010]
print(cc)

print('------------------------------')	#30個

print("Top terms per cluster:")

order_centroids = clf.cluster_centers_.argsort()[:, ::-1]

print("特徵名稱：")
terms = tv.get_feature_names_out()
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
