from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
knnmodel = joblib.load("data/iris.pkl")
score = knnmodel.score(x_test, y_test)
print(score)
