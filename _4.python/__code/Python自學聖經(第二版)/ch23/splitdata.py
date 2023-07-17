from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
print('原始_特徵：{}, 原始_目標：{}'.format(iris.data.shape, iris.target.shape))
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
print('訓練_特徵：{}, 訓練_目標：{}'.format(x_train.shape, y_train.shape))
print('測試_特徵：{}, 測試_目標：{}'.format(x_test.shape, y_test.shape))
