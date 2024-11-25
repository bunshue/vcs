"""

fetch_20newsgroups



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

from sklearn.datasets import fetch_20newsgroups  # 新聞資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個

news = fetch_20newsgroups(subset="all")

print("目標值：")
print(news.target)
print("目標名稱：")
print(news.target_names)
print("第一篇新聞內容：")
print(news.data[0])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
單純貝氏分類器 naive Bayes classifier
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

news = fetch_20newsgroups(subset="all")

x_train, x_test, y_train, y_test = train_test_split(
    news.data, news.target, test_size=0.20
)

tf = TfidfVectorizer()
x_train = tf.fit_transform(x_train)
x_test = tf.transform(x_test)

mlt = MultinomialNB(alpha=1.0)
mlt.fit(x_train, y_train)
score = mlt.score(x_test, y_test)
print(score)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 篩選新聞類別
categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

data_train = fetch_20newsgroups(
    subset="train",
    categories=categories,
    shuffle=True,
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = fetch_20newsgroups()
print(data.target_names)

"""
Downloading 20news dataset. This may take a few minutes.
Downloading dataset from https://ndownloader.figshare.com/files/5975967 (14 MB)
"""

# ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']


categories = [
    "talk.religion.misc",
    "soc.religion.christian",
    "sci.space",
    "comp.graphics",
]
train = fetch_20newsgroups(subset="train", categories=categories)
test = fetch_20newsgroups(subset="test", categories=categories)

print(train.data[5])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)


from sklearn.metrics import confusion_matrix

mat = confusion_matrix(test.target, labels)
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(
    mat.T,
    square=True,
    annot=True,
    fmt="d",
    cbar=False,
    xticklabels=train.target_names,
    yticklabels=train.target_names,
)
plt.xlabel("True Label")
plt.ylabel("Predicted Label")
plt.show()

"""
/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
  import pandas.util.testing as tm
"""


def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    print(train.target_names[pred[0]])


predict_category("sending a payload to the ISS")


# sci.space


predict_category("discussing islam vs atheism")


# soc.religion.christian


predict_category("determining the screen resolution")


# comp.graphics


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("機械学習モデルへの適用")

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
