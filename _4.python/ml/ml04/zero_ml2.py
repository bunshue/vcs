import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
n_components = 2 # 削減後の次元を2に設定
model = PCA(n_components=n_components)
model = model.fit(data.data)
print(model.transform(data.data)) # 変換したデータ

print('------------------------------------------------------------')	#60個

from sklearn.decomposition import TruncatedSVD

data = [[1, 0, 0, 0],
[1, 0, 0, 0],
[1, 1, 0, 0],
[0, 1, 0, 0],
[0, 0, 1, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 0, 0, 1]]
n_components = 2 # 潜在変数の数
model = TruncatedSVD(n_components=n_components)
model.fit(data)
print(model.transform(data)) # 変換したデータ 
print(model.explained_variance_ratio_) # 寄与率 
print(sum(model.explained_variance_ratio_)) # 累積寄与率

print('------------------------------------------------------------')	#60個

from sklearn.decomposition import NMF
#from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

centers = [[5, 10, 5], [10, 4, 10], [6, 8, 8]]
X, _ = make_blobs(centers=centers) # centersを中心としたデータを生成
n_components = 2 # 潜在変数の数
model = NMF(n_components=n_components)
model.fit(X)
W = model.transform(X) # 分解後の行列
H = model.components_
print(W)
print(H)

print('------------------------------------------------------------')	#60個

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
 

# removeで本文以外の情報を取り除く
data = fetch_20newsgroups(remove=('headers', 'footers', 'quotes'))
max_features = 1000
# 文書 データをベクトルに変換
tf_vectorizer = CountVectorizer(max_features=max_features,
stop_words='english')
tf = tf_vectorizer.fit_transform(data.data)
n_topics = 20
model = LatentDirichletAllocation(n_components=n_topics)
model.fit(tf)
print(model.components_) # 各トピックが持つ単語分布 
print(model.transform(tf)) # トピックで表現された文書

print('------------------------------------------------------------')	#60個

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

data = load_iris()
n_clusters = 3 # クラスタ数を3に設定
model = KMeans(n_clusters=n_clusters)
model.fit(data.data)
print(model.labels_) # 各データ点が所属するクラスタ 
print(model.cluster_centers_) # fit()によって計算された重心

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

data = load_iris()
n_components = 3 # ガウス分布の数
model = GaussianMixture(n_components=n_components)
model.fit(data.data) 
print(model.predict(data.data)) # クラスを予測 
print(model.means_) # 各ガウス分布の平均 
print(model.covariances_) # 各ガウス分布の分散


print('------------------------------------------------------------')	#60個

''' import fail
from sklearn.datasets import samples_generator
from sklearn.manifold import LocallyLinearEmbedding


data, color = samples_generator.make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍点の数 
n_components = 2 # 削減後の次元数
model = LocallyLinearEmbedding(n_neighbors=n_neighbors,
n_components=n_components)
model.fit(data)
print(model.transform(data)) # 変換したデータ
'''

print('------------------------------------------------------------')	#60個

from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

data = load_digits()
n_components = 2 # 削減後の次元を2に設定
model = TSNE(n_components=n_components)
print(model.fit_transform(data.data))

print('------------------------------------------------------------')	#60個





