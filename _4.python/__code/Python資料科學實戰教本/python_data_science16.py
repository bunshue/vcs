"""
Python資料科學實戰教本

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
print("---------------------------")
print(iris.data.shape)
print("---------------------------")
print(iris.feature_names)
print("---------------------------")
print(iris.DESCR)

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("data/titanic.csv")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([titanic["SexCode"],
                  encoded_class]).T
X.columns = ["SexCode", "PClass"]
y = titanic["Survived"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier()
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
preds = dtree.predict_proba(X=XTest)
print(pd.crosstab(preds[:,0], columns=[XTest["PClass"],
                                       XTest["SexCode"]]))
pd.crosstab(preds[:,0], columns=[XTest["PClass"],
                                       XTest["SexCode"]]).to_html("tmp_ch16-1-2.html")

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("data/titanic.csv")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([titanic["SexCode"],
                  encoded_class]).T
X.columns = ["SexCode", "PClass"]
y = titanic["Survived"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier()
dtree.fit(XTrain, yTrain)

with open("tmp_tree.dot", "w") as f:
    f = tree.export_graphviz(dtree,
                             feature_names=["Sex", "Class"],
                             out_file=f)
 
print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier(max_depth = 8)
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
print(dtree.predict(XTest))
print("---------------------------")
print(yTest.values)

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier(max_depth = 8)
dtree.fit(XTrain, yTrain)

with open("tmp_tree2.dot", "w") as f:
    f = tree.export_graphviz(dtree,
                             feature_names=iris.feature_names,
                             out_file=f)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import neighbors

X = pd.DataFrame({
   "耐酸性": [7, 7, 3, 1],
   "強度":   [7, 4, 4, 4]
})

y = np.array([0, 0, 1, 1])
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = pd.DataFrame(np.array([[3, 7]]),
                          columns=["耐酸性", "強度"])
pred = knn.predict(new_tissue)
print(pred)


print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["sepal_length"], X["sepal_width"], color=colmap[y])
plt.xlabel("花萼長度(Sepal Length)")
plt.ylabel("花萼寬度(Sepal Width)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

print("準確率:", knn.score(XTest, yTest))
print("---------------------------")
print(knn.predict(XTest))
print("---------------------------")
print(yTest.values)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

Ks = np.arange(1, round(0.2*len(XTrain) + 1))
accuracies=[]
for k in Ks:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    accuracy = knn.score(XTest, yTest)
    accuracies.append(accuracy)
    
plt.plot(Ks, accuracies)

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

Ks = np.arange(1, round(0.2*len(X) + 1))
accuracies=[]
for k in Ks:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, scoring="accuracy",
                            cv=10)
    accuracies.append(scores.mean())

plt.plot(Ks, accuracies)

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

df = pd.DataFrame({
   "length": [51, 46, 51, 45, 51, 50, 33,
              38, 37, 33, 33, 21, 23, 24],
   "weight": [10.2, 8.8, 8.1, 7.7, 9.8, 7.2, 4.8,
              4.6, 3.5, 3.3, 4.3, 2.0, 1.0, 2.0]
})
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(df)
print(kmeans.labels_)

colmap = np.array(["r", "g", "y"])
plt.scatter(df["length"], df["weight"], color=colmap[kmeans.labels_])

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print(kmeans.labels_)
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("真實分類(Real Classification)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[kmeans.labels_])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("K-means分類(K-means Classification)")

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print("K-means分類(K-means Classification):")
print(kmeans.labels_)
# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [2,0,1]).astype(np.int64)
print("K-means修正分類(K-means Fix Classification):")
print(pred_y) 
print("真實分類(Real Classification):")
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("真實分類(Real Classification)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[pred_y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("K-means分類(K-means Classification)")

plt.show()

print("------------------------------------------------------------")  # 60個

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
 

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



