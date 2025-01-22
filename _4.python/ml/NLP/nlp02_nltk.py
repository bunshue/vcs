"""
#WordNet是一個由普林斯頓大學認識科學實驗室在心理學教授喬治·A·米勒的指導下建立和維護的英語字典。

import nltk
nltk.download('wordnet')
nltk.download('stopwords')

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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import classification_report  # 分類報告
from sklearn.naive_bayes import GaussianNB


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import string
import re

import nltk

stemmer = nltk.SnowballStemmer("english")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# spam_classification_with_tfidf
# 垃圾信分類

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
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

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

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict
cc = accuracy_score(y_pred, y_test)
print(cc)
# 0.9668161434977578

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
cc = logistic_regression.predict(X_new.toarray())  # 預測.predict
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_11_naive_bayes_spam

# 垃圾信分類

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
show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8114)

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
# 模型訓練

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

y_pred = clf.predict(X_test)
cc = accuracy_score(y_pred, y_test)
print(cc)
# 0.895067264573991

print(classification_report(y_test, y_pred))

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
cc = clf.predict(X_new.toarray())
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Hate-Speech-Detection-Model

print("------------------------------------------------------------")  # 60個

data = pd.read_csv("data/twitter.csv")
cc = data.head()

print(cc)

data["labels"] = data["class"].map(
    {0: "Hate Speech", 1: "Offensive Language", 2: "No Hate and Offensive"}
)
cc = data.head()

print(cc)

print("------------------------------------------------------------")  # 60個


data = data[["tweet", "labels"]]
cc = data.head()
print(cc)

print("------------------------------------------------------------")  # 60個

stopword = set(stopwords.words("english"))


def clean(text):
    text = str(text).lower()
    text = re.sub("", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = [word for word in text.split(" ") if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(" ")]
    text = " ".join(text)
    return text


data["tweet"] = data["tweet"].apply(clean)
data.head()

print("------------------------------------------------------------")  # 60個


x = np.array(data["tweet"])
y = np.array(data["labels"])

cv = CountVectorizer()
X = cv.fit_transform(x)  # Fit the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

# user = input("Enter a Text: ")
user = "Let's unite and kill all the people who don't value our religion."
data = cv.transform([user]).toarray()
output = clf.predict(data)
print(output)

"""
Enter a Text: Let's unite and kill all the people who don't value our religion.
['Hate Speech']
Enter a Text: this is a lion
['No Hate and Offensive']
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
