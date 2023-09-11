import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=["Species"])
df = pd.concat([X, y], axis=1)

print(df.head())

print('------------------------------------------------------------')	#60個

#學習分類
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

X = data.data
y = data.target


X = X[:, :10]


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X, y)

y_pred = model.predict(X)

from sklearn.metrics import accuracy_score
accuracy_score(y, y_pred)





print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_wine
data = load_wine()

X = data.data[:, [0, 9]]


from sklearn.cluster import KMeans
n_clusters = 3
model = KMeans(n_clusters=n_clusters)


pred = model.fit_predict(X)




import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(X[pred==0, 0], X[pred==0, 1], color='red', marker='s', label='Label1')
ax.scatter(X[pred==1, 0], X[pred==1, 1], color='blue', marker='s', label='Label2')
ax.scatter(X[pred==2, 0], X[pred==2, 1], color='green', marker='s', label='Label3')
ax.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=200, color='yellow', marker="*", label="center")
ax.legend()
plt.show()


print('------------------------------------------------------------')	#60個


from sklearn.datasets import load_wine
data = load_wine()

x3 = data.data[:, [0]]
y3 = data.data[:, [9]]

plt.scatter(x3, y3)
plt.show()


plt.hist(y3, bins=5)
plt.show()


print('------------------------------------------------------------')	#60個


import pandas as pd

from sklearn.datasets import load_wine
data = load_wine()
df_X = pd.DataFrame(data.data, columns=data.feature_names)

print(df_X.head())

df_y = pd.DataFrame(data.target, columns=["kind(target)"])

print(df_y.head())

df = pd.concat([df_X, df_y], axis=1)

print(df.head())

plt.hist(df.loc[:, "alcohol"])



plt.show()

plt.boxplot(df.loc[:, "alcohol"])


plt.show()

print(df.corr())
print(df.describe())

print('------------------------------------------------------------')	#60個

from pandas.plotting import scatter_matrix
_ = scatter_matrix(df, figsize=(15, 15))

plt.show()


_ = scatter_matrix(df.iloc[:, [0, 9, -1]])

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
