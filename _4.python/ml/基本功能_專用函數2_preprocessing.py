"""
基本功能_專用函數2

特徵縮放

# StandardScaler
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似

print("資料前處理方式(4) 測試特徵縮放")

1. StandardScaler (平均值和標準差)
Standardization 平均&變異數標準化
將所有特徵標準化，也就是高斯分佈。使得數據的平均值為0，方差為1。
適合的使用時機於當有些特徵的方差過大時，使用標準化能夠有效地讓模型快速收斂。

2. MinMaxScaler(最小最大值標準化)
MinMaxScaler 最小最大值標準化
在MinMaxScaler中是給定了一個明確的最大值與最小值。
每個特徵中的最小值變成了0，最大值變成了1。數據會縮放到到[0,1]之間。

3. MaxAbsScaler（絕對值最大標準化）
MaxAbsScaler 絕對值最大標準化
MaxAbsScaler 與 MinMaxScaler 類似，所有數據都會除以該列絕對值後的最大值。
數據會縮放到到[-1,1]之間。

4. RobustScaler
RobustScaler 中位數和四分位數標準化
可以有效的縮放帶有outlier的數據，透過Robust如果數據中含有異常值在縮放中會捨去。
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

from sklearn.preprocessing import StandardScaler  # STD特徵縮放
from sklearn.preprocessing import MinMaxScaler  # MMS特徵縮放
from sklearn.preprocessing import MaxAbsScaler  # MAS特徵縮放
from sklearn.preprocessing import RobustScaler  # RS特徵縮放

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

print("常態分布資料1000點")

N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
X = mu + sigma * np.random.randn(N, 2)  # 隨機數
print("原始資料")
print("平均數:", round(np.mean(X), 3))
print("標準差:", round(np.std(X), 3))

print("------------------------------")  # 30個

scaler = StandardScaler()  # STD特徵縮放
X_std = scaler.fit_transform(X)
print("STD特徵縮放")
print("平均數:", round(np.mean(X_std), 3))
print("標準差:", round(np.std(X_std), 3))

print(f"STD特徵縮放 前, 資料的平均值與標準差 : {X.mean():.2f}, {X.std():.2f}")
print(f"STD特徵縮放 後, 資料的平均值與標準差 : {X_std.mean():.2f}, {X_std.std():.2f}")

plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c="r", cmap="bwr")
# plt.scatter(X.T[0], X.T[1], c='r', cmap="Dark2")
plt.grid(True)
plt.title("原始資料\n平均值100 標準差15")

plt.subplot(222)
plt.scatter(X_std[:, 0], X_std[:, 1], c="r", cmap="bwr")
# plt.scatter(X_std.T[0], X_std.T[1], c='r', cmap="Dark2")
plt.grid(True)
plt.title("特徵縮放 StandardScaler\n平均值0 標準差1")

plt.subplot(223)
n, bins, patches = plt.hist(
    X[:, 0], bins=num_bins, density=True, color="red", rwidth=0.5, alpha=0.5
)
n, bins, patches = plt.hist(
    X[:, 1], bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)
plt.grid(True)
plt.title("原始資料\n平均值100 標準差15")

plt.subplot(224)
n, bins, patches = plt.hist(
    X_std[:, 0], bins=num_bins, density=True, color="red", rwidth=0.5, alpha=0.5
)
n, bins, patches = plt.hist(
    X_std[:, 1], bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)
plt.grid(True)
plt.title("特徵縮放 StandardScaler\n平均值0 標準差1")

show()

print("------------------------------")  # 30個

scaler = MinMaxScaler()  # MMS特徵縮放
X_mms = scaler.fit_transform(X)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c="r", cmap="bwr")
plt.subplot(122)
plt.scatter(X_mms[:, 0], X_mms[:, 1], c="r", cmap="bwr")
plt.suptitle("MMS特徵縮放 => [0, 1]")
show()

print("------------------------------")  # 30個

scaler = MaxAbsScaler()  # MAS特徵縮放
X_mas = scaler.fit_transform(X)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], s=30, c="r")
plt.subplot(122)
plt.scatter(X_mas[:, 0], X_mas[:, 1], s=30, c="r")
plt.suptitle("MAS特徵縮放 => [-1, 1]")
show()

print("MAS特徵縮放")

data = np.array([[1.0, -1.0, 2.0], [2.0, 0.0, 0.0], [0.0, 1.0, -1.0]])
print(data)

scaler = MaxAbsScaler()  # MAS特徵縮放
cc = scaler.fit_transform(data)
print(cc)

# 驗證
# 計算最大值
max1 = np.max(data, axis=0)
# MaxAbsScaler計算
cc = data / max1
print(cc)

print("------------------------------")  # 30個

scaler = RobustScaler()  # RS特徵縮放
X_rs = scaler.fit_transform(X)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], s=30, c="r")
plt.subplot(122)
plt.scatter(X_rs[:, 0], X_rs[:, 1], s=30, c="r")
plt.suptitle("RS特徵縮放 中位數和四分位數標準化")
show()

print("RS特徵縮放")

data = np.array([[1.0, -2.0, 2.0], [-2.0, 1.0, 3.0], [4.0, 1.0, -2.0]])
print(data)

scaler = RobustScaler()  # RS特徵縮放
cc = scaler.fit_transform(data)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_selection import VarianceThreshold

scaler = MinMaxScaler()  # MMS特徵縮放
data = scaler.fit_transform(
    [[3, 2, 61, 10000], [3, 8, 54, 12000], [3, 4, 60, 10500], [3, 1, 58, 11000]]
)
print("原始特徵：")
print(data)
vari = VarianceThreshold(threshold=0.0)
# vari = VarianceThreshold(threshold=0.14)
data2 = vari.fit_transform(data)
print("特徵選擇後：")
print(data2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction import DictVectorizer

dict = DictVectorizer(sparse=True)
data = dict.fit_transform(
    [{"膚色": "黃", "身高": 176}, {"膚色": "白", "身高": 183}, {"膚色": "黑", "身高": 158}]
)
print("sparse編碼：")
print(data)
print("特徵名稱：")
print(dict.get_feature_names_out())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction import DictVectorizer

dict = DictVectorizer(sparse=False)
data = dict.fit_transform(
    [{"膚色": "黃", "身高": 176}, {"膚色": "白", "身高": 183}, {"膚色": "黑", "身高": 158}]
)
print("one-hot編碼：")
print(data)
print("特徵名稱：")
print(dict.get_feature_names_out())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
data = cv.fit_transform(
    ["code is is easy, i like python", "code is too hard, i dislike python"]
)
print("one-hot編碼：")
print(data.toarray())
print("特徵名稱：")
print(cv.get_feature_names_out())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

texts = ["dog and fish, dog and dog", "dog and dog", "dog and cat"]
count_vectorizer = CountVectorizer(ngram_range=(1, 1), stop_words="english")
count_train = count_vectorizer.fit_transform(texts)
print(count_vectorizer.get_feature_names_out())
print(count_vectorizer.vocabulary_)
print(count_train)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "One of the confiscated drafts was a story about stoning women to death for adultery – never published, never presented to anyone, the article stated. The narrative followed the story of a protagonist that watched a movie about stoning of women under Islamic law for adultery."
]

count_vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words="english")
count_train = count_vectorizer.fit_transform(texts)
print(count_vectorizer.get_feature_names_out())
print(count_vectorizer.vocabulary_)
print(count_train)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer
import joblib

count_vectorizer = joblib.load("count_vectorizer.pkl")
classifier = joblib.load("classifier.pkl")


def classify(document):
    label = {0: "reliable", 1: "unreliable"}
    document_text = count_vectorizer.transform([document])
    y = classifier.predict(document_text)[0]
    return label[y]


document = input("Please enter your news description:")
print("This news review is " + classify(document) + ".")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import TfidfVectorizer

t1 = list(jieba.cut("今天台北天氣晴朗，風景區擠滿了人潮。"))
t2 = list(jieba.cut("台北的天氣常常下雨。"))
c1 = " ".join(t1)
c2 = " ".join(t2)

tf = TfidfVectorizer()
data = tf.fit_transform([c1, c2])
print("one-hot編碼：")
print(data.toarray())
print("特徵名稱：")
print(tf.get_feature_names_out())

print("------------------------------------------------------------")  # 60個

from sklearn.feature_extraction.text import CountVectorizer

t1 = list(jieba.cut("今天台北天氣晴朗，風景區擠滿了人潮。"))
t2 = list(jieba.cut("台北的天氣常常下雨。"))
c1 = " ".join(t1)
print("第一句分詞： {}".format(c1))
c2 = " ".join(t2)
print("第二句分詞： {}".format(c2))

cv = CountVectorizer()
data = cv.fit_transform([c1, c2])
print("one-hot編碼：")
print(data.toarray())
print("特徵名稱：")
print(cv.get_feature_names_out())

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

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(arr)
word = vectorizer.get_feature_names_out()
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler


print("------------------------------------------------------------")  # 60個
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

show()

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

show()

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

show()

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
