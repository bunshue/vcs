from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import joblib

iris = load_iris()
x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
joblib.dump(knn, 'data/iris.pkl')
