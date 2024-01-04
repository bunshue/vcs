"""
pip install scikit-learn

"""


print('------------------------------------------------------------')	#60個

import sklearn as skl
print(skl.__version__)


from sklearn import datasets, svm, metrics
print(dir(datasets))

import sklearn
print(sklearn)

print('------------------------------------------------------------')	#60個

import numpy as np
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

#---------------------------------------------------------------------------------------

import seaborn as sns #海生, 自動把圖畫得比較好看

iris = sns.load_dataset('iris')
iris.head()

sns.set()
sns.pairplot(iris, hue='species', height=3);

print(iris)
print('cccc')

# seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
#import squarify

plt.rcParams["font.sans-serif"]='Microsoft JhengHei'


tips = sns.load_dataset("tips")
print(tips)


print('作業完成')
