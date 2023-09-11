from sklearn.datasets import load_iris

iris = load_iris()
print('特徵值：')
print(iris.data[0:3])
print('目標值：')
print(iris.target)
print('特徵名稱：')
print(iris.feature_names)
print('目標名稱：')
print(iris.target_names)
