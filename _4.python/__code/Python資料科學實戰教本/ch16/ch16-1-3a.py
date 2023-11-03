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
