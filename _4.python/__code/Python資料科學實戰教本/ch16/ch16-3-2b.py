import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import sklearn.metrics as sm

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [2,0,1]).astype(np.int64)
# 績效矩陣
print(sm.accuracy_score(y, pred_y))
print("---------------------------")
# 混淆矩陣
print(sm.confusion_matrix(y, pred_y))
 