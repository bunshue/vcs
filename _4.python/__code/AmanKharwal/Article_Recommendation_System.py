"""
Article_Recommendation_System

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

from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv",
    encoding="latin1",
)
# print(data)

cc = data.isnull().sum()
print(cc)

"""
Article    0
Title      0
dtype: int64
"""

articles = data["Article"].tolist()

uni_tfidf = text.TfidfVectorizer(input=articles, stop_words="english")

# NG uni_matrix = uni_tfidf.fit_transform(articles)
"""  
uni_sim = cosine_similarity(uni_matrix)
     

def recommend_articles(x):
    return ", ".join(data["Title"].loc[x.argsort()[-5:-1]])
    
data["Recommended Articles"] = [recommend_articles(x) for x in uni_sim]
cc = data.head()
print(cc)

print(data["Recommended Articles"][22])

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


print("------------------------------")  # 30個
