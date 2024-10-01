import matplotlib.pyplot as plt
import numpy as np

plt.plot([9, 9.2, 9.6, 9.2, 6.7, 7, 7.6], [9.0, 9.2, 9.2, 9.2, 7.1, 7.4, 7.5], "yx")
plt.plot(
    [7.2, 7.3, 7.2, 7.3, 7.2, 7.3, 7.3], [10.3, 10.5, 9.2, 10.2, 9.7, 10.1, 10.1], "g."
)
plt.plot([7], [9], "r^")

circle1 = plt.Circle((7, 9), 1.2, color="#aaaaaa")
plt.gcf().gca().add_artist(circle1)
plt.axis([6, 11, 6, 11])


plt.ylabel("H cm")
plt.xlabel("W cm")
plt.legend(("Orange", "Lemons"), loc="upper right")
plt.show()

print("------------------------------------------------------------")  # 60個

# 02-kNN-Lemon.py

X = [
    [9, 9],
    [9.2, 9.2],
    [9.6, 9.2],
    [9.2, 9.2],
    [6.7, 7.1],
    [7, 7.4],
    [7.6, 7.5],
    [7.2, 10.3],
    [7.3, 10.5],
    [7.2, 9.2],
    [7.3, 10.2],
    [7.2, 9.7],
    [7.3, 10.1],
    [7.3, 10.1],
]
y = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
print("預測答案＝", neigh.predict([[7, 9]]))
print("預測樣本距離＝", neigh.predict_proba([[7, 9]]))  #      測試數據X的返回概率估計。

print("------------------------------------------------------------")  # 60個

# 03-Iris.py

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


# Load the diabetes dataset
iris = datasets.load_iris()

print("iris.data.shape=", iris.data.shape)
print("dir(iris)", dir(iris))
print("iris.target.shape=", iris.target.shape)
try:
    print("iris.feature_names=", iris.feature_names)
except:
    print("No iris.feature_names=")

import xlsxwriter
import pandas as pd

try:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
except:
    df = pd.DataFrame(
        iris.data,
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )

df["target"] = iris.target

print(df.head())
df.to_csv("tmp_iris.csv", sep="\t")

writer = pd.ExcelWriter("tmp_iris.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer.save()


print("------------------------------------------------------------")  # 60個

# 04-Iris-KNN.py

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
iris = datasets.load_iris()


iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)


knn = KNeighborsClassifier()


knn.fit(iris_X_train, iris_y_train)


print("預測", knn.predict(iris_X_test))
print("實際", iris_y_test)

print("準確率: %.2f" % knn.score(iris_X_test, iris_y_test))

print("------------------------------------------------------------")  # 60個
