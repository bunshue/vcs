import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


'''
print('------------------------------------------------------------')	#60個

from sklearn.metrics.pairwise import euclidean_distances

rating_matrix = np.array(
    [[4,3,0,0,5,0],
     [5,0,4,0,4,0],
     [4,0,5,3,4,0],
     [0,3,0,0,0,5],
     [0,4,0,0,0,4],
     [0,0,2,4,0,5]
    ]
)

dist = euclidean_distances(rating_matrix)
print(dist)


from sklearn.metrics.pairwise import cosine_similarity
sim = cosine_similarity(rating_matrix)
print(sim)

print('------------------------------------------------------------')	#60個

'''

print('------------------------------------------------------------')	#60個


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

text =["小贝来到北京清华大学", 
        "小花来到了网易杭研大厦",   
        "小明硕士毕业于中国科学院",
        "小明爱北京小明爱北京天安门"
]
               
corpus=["小贝 来到 北京 清华大学", 
        "小花 来到 了 网易 杭研 大厦",   
        "小明 硕士 毕业 于 中国 科学院",
        "小明 爱 北京 小明 爱 北京 天安门"
]



print('------------------------------------------------------------')	#60個
print('二值化、词频')
vectorizer = CountVectorizer(min_df=1,binary=True) #Transformer
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)
print(len(features))


print(data.todense())

doc_df = pd.DataFrame(data.toarray(), index=text, columns=vectorizer.get_feature_names_out()).head(10)

print(doc_df)

print('------------------------------------------------------------')	#60個

from sklearn.metrics.pairwise import cosine_similarity
cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index = text, columns = text)
print(sims_df)


print('------------------------------------------------------------')	#60個

#tf-idf

vectorizer = TfidfVectorizer(min_df=1)
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)

print('------------------------------------------------------------')	#60個

pd.set_option('display.precision', 2)
doc_df = pd.DataFrame(data.toarray(), index=text, columns=vectorizer.get_feature_names_out()).head(10)
print(doc_df)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

