"""
基本功能_專用函數2

特徵縮放

# StandardScaler
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似

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

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個

print("資料前處理方式(4) 測試特徵縮放")
"""
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

"""
dataset = pd.read_csv("data/studentscores.csv")
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values
"""

iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 指定X，並轉為 Numpy 陣列
X = df.values
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

print(x_train.shape)

# 特徵縮放
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_std = scaler.fit_transform(x_train)  # STD特徵縮放

print("全部欄")
print(f"特徵縮放 前, 資料的平均值與標準差 : {x_train.mean():.2f}, {x_train.std():.2f}")
print(f"特徵縮放 後, 資料的平均值與標準差 : {x_train_std.mean():.2f}, {x_train_std.std():.2f}")
print("第0欄")
print(f"特徵縮放 前, 資料的平均值與標準差 : {x_train[0].mean():.2f}, {x_train[0].std():.2f}")
print(f"特徵縮放 後, 資料的平均值與標準差 : {x_train_std[0].mean():.2f}, {x_train_std[0].std():.2f}")
print("第1欄")
print(f"特徵縮放 前, 資料的平均值與標準差 : {x_train[1].mean():.2f}, {x_train[1].std():.2f}")
print(f"特徵縮放 後, 資料的平均值與標準差 : {x_train_std[1].mean():.2f}, {x_train_std[1].std():.2f}")
print("第2欄")
print(f"特徵縮放 前, 資料的平均值與標準差 : {x_train[2].mean():.2f}, {x_train[2].std():.2f}")
print(f"特徵縮放 後, 資料的平均值與標準差 : {x_train_std[2].mean():.2f}, {x_train_std[2].std():.2f}")
print("第3欄")
print(f"特徵縮放 前, 資料的平均值與標準差 : {x_train[3].mean():.2f}, {x_train[3].std():.2f}")
print(f"特徵縮放 後, 資料的平均值與標準差 : {x_train_std[3].mean():.2f}, {x_train_std[3].std():.2f}")

plt.subplot(121)
plt.scatter(x_train[:, 0], x_train[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train[:, 2], x_train[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.subplot(122)
plt.scatter(x_train_std[:, 0], x_train_std[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train_std[:, 2], x_train_std[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.suptitle("STD特徵縮放 => 平均值0 標準差1")
plt.show()

print("------------------------------")  # 30個

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
x_train_mms = scaler.fit_transform(x_train)  # MMS特徵縮放

plt.subplot(121)
plt.scatter(x_train[:, 0], x_train[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train[:, 2], x_train[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.subplot(122)
plt.scatter(x_train_mms[:, 0], x_train_mms[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train_mms[:, 2], x_train_mms[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.suptitle("MMS特徵縮放 => [0, 1]")
plt.show()

print("------------------------------")  # 30個

from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
x_train_mas = scaler.fit_transform(x_train)  # MAS特徵縮放

plt.subplot(121)
plt.scatter(x_train[:, 0], x_train[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train[:, 2], x_train[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.subplot(122)
plt.scatter(x_train_mas[:, 0], x_train_mas[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train_mas[:, 2], x_train_mas[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.suptitle("MAS特徵縮放 => [-1, 1]")
plt.show()

print("MAS特徵縮放")

data = np.array([[1.0, -1.0, 2.0], [2.0, 0.0, 0.0], [0.0, 1.0, -1.0]])
print(data)

scaler = MaxAbsScaler()
cc = scaler.fit_transform(data)
print(cc)

# 驗證
# 計算最大值
max1 = np.max(data, axis=0)
# MaxAbsScaler計算
cc = data / max1
print(cc)

print("------------------------------")  # 30個

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
x_train_rs = scaler.fit_transform(x_train)  # RS特徵縮放

plt.subplot(121)
plt.scatter(x_train[:, 0], x_train[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train[:, 2], x_train[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.subplot(122)
plt.scatter(x_train_rs[:, 0], x_train_rs[:, 1], s=30, c="r", label="真實資料")  # 真實資料, 藍點
plt.scatter(x_train_rs[:, 2], x_train_rs[:, 3], s=30, c="g", label="真實資料")  # 真實資料, 藍點
plt.suptitle("RS特徵縮放 中位數和四分位數標準化")
plt.show()

print("RS特徵縮放")

data = np.array([[1.0, -2.0, 2.0], [-2.0, 1.0, 3.0], [4.0, 1.0, -2.0]])
print(data)

scaler = RobustScaler()
cc = scaler.fit_transform(data)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data = scaler.fit_transform([[156,56,34,800000], 
                          [180,73,21,620000], 
                          [175,76,18,1000000], 
                          [148,46,26,430000]])
print(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data = scaler.fit_transform([[156,56,34,800000], 
                         [180,73,21,620000], 
                         [175,76,18,1000000], 
                         [148,46,26,430000]])
print(data)


from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold

scaler = MinMaxScaler()
data = scaler.fit_transform([[3,2,61,10000], 
                         [3,8,54,12000], 
                         [3,4,60,10500], 
                         [3,1,58,11000]])
print('原始特徵：')
print(data)
vari = VarianceThreshold(threshold=0.0)
#vari = VarianceThreshold(threshold=0.14)
data2 = vari.fit_transform(data)
print('特徵選擇後：')
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
