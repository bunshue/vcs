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

#第十四讲 聚类
#1、层次聚类

import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
from sklearn import preprocessing
from sklearn.decomposition import PCA

#导入数据
orgData = pd.read_csv('cities_10.csv', index_col="AREA", encoding='gbk')
orgData.head()
#orgData.describe()

#标准化
x_scaled = preprocessing.scale(orgData+0.0)#归一化，但是只能用于浮点类型变量
pd.DataFrame(x_scaled).head()

#变量压缩
pca=PCA(n_components=2)
newData=pca.fit_transform(x_scaled)
cc = pca.explained_variance_ratio_
print(cc)

print(newData)

#1. 层次聚类
#生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(newData,'euclidean') 
#进行层次聚类:
Z=sch.linkage(disMat,method='average') 
#将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P=sch.dendrogram(Z)
plt.savefig('tmp_plot_dendrogram1.png')

#2、K-means聚类

from sklearn import cluster
from sklearn.decomposition import PCA
from sklearn import preprocessing

iris = pd.read_csv('iris.csv')
x=iris.ix[:,"Sepal.Length":"Petal.Width"] # NG
y=iris["Species"]

#归一化的使用说明 http://www.cnblogs.com/chaosimple/p/4153167.html

x_scaled = preprocessing.scale(x+0.0)#归一化，但是只能用于浮点类型变量
cc = pd.DataFrame(x_scaled).head()
print(cc)

pca=PCA(n_components=3)
newData=pca.fit_transform(x_scaled)
cc = pca.explained_variance_ratio_
print(cc)

score=pd.DataFrame(newData)
cc = score.head()
print(cc)

#http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

from sklearn.cluster import KMeans

kmeans = cluster.KMeans(n_clusters=3) #MiniBatchKMeans()分批处理
#kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result=kmeans.fit(x_scaled)
print(result)

cc = result.labels_
print(cc)

lo = plt.scatter(score[0][result.labels_==0],score[1][result.labels_==0], marker='x')
lo = plt.scatter(score[0][result.labels_==1],score[1][result.labels_==1], marker='o')
lo = plt.scatter(score[0][result.labels_==2],score[1][result.labels_==2], marker='+')

#聚类效果评估
#Silhouette Coefficient
#http://scikit-learn.org/stable/modules/clustering.html#clustering

from sklearn import metrics
cc = metrics.silhouette_score(x_scaled, result.labels_, metric='euclidean')
print(cc)

#Adjusted Rand index
#http://scikit-learn.org/stable/modules/clustering.html#clustering

from sklearn import metrics
cc = metrics.adjusted_rand_score(y, result.labels_ )
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

