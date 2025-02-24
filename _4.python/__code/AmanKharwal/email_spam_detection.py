"""
email_spam_detection

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

# from google.colab import files
# uploaded = files.upload()

import nltk
from nltk.corpus import stopwords
import string

df = pd.read_csv("data/emails.csv")
cc = df.head()
print(cc)

cc = df.shape
print(cc)

cc = df.columns
print(cc)

df.drop_duplicates(inplace=True)
print(df.shape)

# 檢查資料缺失 to show the number of missing data
print(df.isnull().sum())

# download the stopwords package
nltk.download("stopwords")

# [nltk_data] Downloading package stopwords to /root/nltk_data...
# [nltk_data]   Unzipping corpora/stopwords.zip.


def process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = "".join(nopunc)

    clean = [
        word
        for word in nopunc.split()
        if word.lower() not in stopwords.words("english")
    ]
    return clean


# to show the tokenization
cc = df["text"].head().apply(process)
print(cc)

print("這邊要做很久~~~~~~")

from sklearn.feature_extraction.text import CountVectorizer

message = CountVectorizer(analyzer=process).fit_transform(df["text"])


print("b")
# split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(
    message, df["spam"], test_size=0.20, random_state=0
)
print(message.shape)


print("c")


# create and train the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB().fit(xtrain, ytrain)

print("d")

print(classifier.predict(xtrain))

print(ytrain.values)

# Evaluating the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

pred = classifier.predict(xtrain)
print(classification_report(ytrain, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytrain, pred))
print("Accuracy: \n", accuracy_score(ytrain, pred))

# print the predictions
print(classifier.predict(xtest))
# print the actual values
print(ytest.values)

# Evaluating the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

pred = classifier.predict(xtest)
print(classification_report(ytest, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytest, pred))
print("Accuracy: \n", accuracy_score(ytest, pred))

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


print("------------------------------")  # 30個
