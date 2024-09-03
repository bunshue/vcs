
from sklearn.datasets import load_iris

print('iris data')

iris = load_iris()
print('特徵值：')
print(iris.data[0:3])
print('目標值：')
print(iris.target)
print('特徵名稱：')
print(iris.feature_names)
print('目標名稱：')
print(iris.target_names)

print("------------------------------------------------------------")  # 60個


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import joblib

print('save model')

iris = load_iris()
x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)

std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
joblib.dump(knn, 'data/iris.pkl')

print("------------------------------------------------------------")  # 60個


iris = load_iris()

x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)
print('預測結果：{}'.format(y_predict))
print('準確率：{}'.format(knn.score(x_test, y_test)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


