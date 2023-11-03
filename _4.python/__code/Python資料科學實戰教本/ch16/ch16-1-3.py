from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
print("---------------------------")
print(iris.data.shape)
print("---------------------------")
print(iris.feature_names)
print("---------------------------")
print(iris.DESCR)
