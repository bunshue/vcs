"""
MLPClassifier（多層感知器分類器）



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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import tensorflow as tf
from sklearn import datasets
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from time import time


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = [[0.0, 0.0], [1.0, 1.0]]
y = [0, 1]

mlp = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 5), random_state=1
)  # 多層感知器分類器 函數學習機

mlp.fit(X, y)  # 學習訓練.fit

y_pred = mlp.predict(X)
print(y_pred)

print("多層感知器分類器 參數")
print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iris 資料 全部")

iris = datasets.load_iris()
data = iris.data
labels = iris.target

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 多層感知器分類器 函數學習機

mlp.fit(data, labels)  # 學習訓練.fit

pred = mlp.predict(data)  # 預測.predict

print("Accuracy: %.2f" % accuracy_score(labels, pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iris 資料 分割+標準化")

iris = datasets.load_iris()
data = iris.data
labels = iris.target

data_train, data_test, labels_train, labels_test = train_test_split(
    data, labels, test_size=0.5
)

scaler = StandardScaler()
scaler.fit(data)
data_train_std = scaler.transform(data_train)
data_test_std = scaler.transform(data_test)

data_train = data_train_std
data_test = data_test_std

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 多層感知器分類器 函數學習機

mlp.fit(data, labels)  # 學習訓練.fit

mlp.fit(data_train, labels_train)  # 學習訓練.fit

pred = mlp.predict(data_test)  # 預測.predict

print("Misclassified samples: %d" % (labels_test != pred).sum())
print("Accuracy: %.2f" % accuracy_score(labels_test, pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap

# 0萼長 1萼寬 2瓣長 3瓣寬
M = {
    0: "sepal length 萼長",
    1: "sepal width 萼寬",
    2: "petal length 瓣長",
    3: "petal width 瓣寬",
}

# Choose two features
x = 1  # 1 corresponds to the sepal width 萼寬
y = 3  # 3 corresponds to the petal width 瓣寬

iris = datasets.load_iris()
data = iris.data[:, [x, y]]

labels = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.5)

reg = StandardScaler()
reg.fit(data)
X_train_std = reg.transform(X_train)
X_test_std = reg.transform(X_test)

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 多層感知器分類器 函數學習機

mlp.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = mlp.predict(X_test_std)  # 預測.predict

print("Misclassified samples: %d" % (y_test != y_pred).sum())
print("Accuracy: %.2f" % accuracy_score(y_test, y_pred))


def plot_decision_regions(data, labels, classifier, resolution=0.01):
    markers = ("s", "*", "^")
    colors = ("blue", "green", "red")
    cmap = ListedColormap(colors)
    # plot the decision surface
    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

    x, y = np.meshgrid(
        np.arange(x_min, x_max, resolution), np.arange(y_min, y_max, resolution)
    )

    Z = classifier.predict(np.array([x.ravel(), y.ravel()]).T)  # 預測.predict
    Z = Z.reshape(x.shape)

    plt.pcolormesh(x, y, Z, cmap=cmap)
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    colors = ("yellow", "white", "black")
    # cmap = ListedColormap(colors)
    # plot the data
    classes = ["setosa", "versicolor", "verginica"]
    for index, cl in enumerate(np.unique(labels)):
        plt.scatter(
            data[labels == cl, 0],
            data[labels == cl, 1],
            c=cmap(index),
            marker=markers[index],
            edgecolor="black",
            alpha=1.0,
            s=50,
            label=classes[index],
        )


X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined_std, y_combined, classifier=mlp)

plt.xlabel(M[x] + " (標準化)")
plt.ylabel(M[y] + " (標準化)")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mnist_filename = "D:/_git/vcs/_big_files/mnist.pkl.gz"

# 使用sklearn中的神经网络模块MLPClassifier处理分类问题
# MLPClassifier（多层感知器分类器）

"""
二.MNIST数据集的下载
MNIST是一些手写数字的图片，通过http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz下载数据集。
三.使用神经网络训练MNIST数据集并实现分类
"""
import pickle
import gzip

# 加载数据
with gzip.open(mnist_filename) as fp:
    training_data, valid_data, test_data = pickle.load(fp, encoding="latin1")

x_training_data, y_training_data = training_data
x_valid_data, y_valid_data = valid_data
x_test_data, y_test_data = test_data
classes = np.unique(y_test_data)

# 将验证集和训练集合并
x_training_data_final = np.vstack((x_training_data, x_valid_data))
y_training_data_final = np.append(y_training_data, y_valid_data)


# 设置神经网络模型参数
# mlp = MLPClassifier(solver='lbfgs', activation='relu',alpha=1e-4,hidden_layer_sizes=(50,50), random_state=1,max_iter=10,verbose=10,learning_rate_init=.1)
# 使用solver='lbfgs',准确率为79%，比较适合小(少于几千)数据集来说，且使用的是全训练集训练，比较消耗内存
# mlp = MLPClassifier(solver='adam', activation='relu',alpha=1e-4,hidden_layer_sizes=(50,50), random_state=1,max_iter=10,verbose=10,learning_rate_init=.1)
# 使用solver='adam'，准确率只有67%
mlp = MLPClassifier(
    solver="sgd",
    activation="relu",
    alpha=1e-4,
    hidden_layer_sizes=(50, 50),
    random_state=1,
    max_iter=10,
    verbose=10,
    learning_rate_init=0.1,
)  # 多層感知器分類器 函數學習機
# 使用solver='sgd'，准确率为98%，且每次训练都会分batch，消耗更小的内存

# 训练模型
mlp.fit(x_training_data_final, y_training_data_final)

print("查看模型结果")
print(mlp.score(x_test_data, y_test_data))

print("多層感知器分類器 參數")
print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)

"""
四.分析简单实例1和实例2
对于神经网络的输出层（即mlp.out_activation_,且mlp.out_activation_不可设置），激活函数的选取还是有一定的原则的：
1) 如果是两类判别，输出层只有一个神经元，那么选logistic，即实例1mlp.out_activation_输出；
2) 如果是n类判别，输出层有n个神经元，那么选softmax即实例2，输出0-9多分类；
3) 如果是回归，那么选线性。
这些选择并不是为了提高性能，而只是让输出的范围合理。
对于判别问题，输出是概率，所以必须在0到1之间，多类判别时还需要加起来等于1；
对于回归问题，一般没有理由要求输出在0到1之间。
五.fit和partial_fit进行训练的区别
可以看出即使训练的顺序和迭代的次数一样但准确率仍然有区别。
"""
import pickle
import gzip

# 加载数据
with gzip.open(mnist_filename) as fp:
    training_data, valid_data, test_data = pickle.load(fp, encoding="latin1")

x_training_data, y_training_data = training_data
x_valid_data, y_valid_data = valid_data
x_test_data, y_test_data = test_data
classes = np.unique(y_test_data)

# 将验证集和训练集合并
x_training_data_final = np.vstack((x_training_data, x_valid_data))
y_training_data_final = np.append(y_training_data, y_valid_data)

# 将数据切割成batch
x_training_data_final1 = x_training_data_final[:30000]
y_training_data_final1 = y_training_data_final[:30000]
x_training_data_final2 = x_training_data_final[30000:]
y_training_data_final2 = y_training_data_final[30000:]

# 设置神经网络模型参数
mlp = MLPClassifier(
    solver="sgd",
    activation="relu",
    alpha=1e-4,
    hidden_layer_sizes=(50, 50),
    random_state=1,
    max_iter=10,
    verbose=10,
    learning_rate_init=0.1,
)  # 多層感知器分類器 函數學習機

# 训练模型
mlp.fit(x_training_data_final, y_training_data_final)

# #partial_fit只会进行一次迭代，需要循环进行迭代max_iter=10
# for i in range(10):
#     #第一次调用需要加classes
#     mlp.partial_fit(x_training_data_final1,y_training_data_final1,classes)
#     mlp.partial_fit(x_training_data_final2,y_training_data_final2)

print("查看模型结果")
print(mlp.score(x_test_data, y_test_data))

print("多層感知器分類器 參數")
print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)


"""
六.neural_network中MLPClassifier各个参数
例如:mlp = MLPClassifier(solver=’sgd’, activation=’relu’,alpha=1e-4,hidden_layer_sizes=(50,50), random_state=1,max_iter=10,verbose=10,learning_rate_init=.1)

参数说明:
1. hidden_layer_sizes :例如hidden_layer_sizes=(50, 50)，表示有两层隐藏层，第一层隐藏层有50个神经元，第二层也有50个神经元。
2. activation :激活函数,{‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, 默认relu
- identity：f(x) = x
- logistic：其实就是sigmod,f(x) = 1 / (1 + exp(-x)).
- tanh：f(x) = tanh(x).
- relu：f(x) = max(0, x)
3. solver： {‘lbfgs’, ‘sgd’, ‘adam’}, 默认adam，用来优化权重
- lbfgs：quasi-Newton方法的优化器
- sgd：随机梯度下降
- adam： Kingma, Diederik, and Jimmy Ba提出的机遇随机梯度的优化器
注意：默认solver ‘adam’在相对较大的数据集上效果比较好（几千个样本或者更多），对小数据集来说，lbfgs收敛更快效果也更好。
4. alpha :float,可选的，默认0.0001,正则化项参数
5. batch_size : int , 可选的，默认’auto’,随机优化的minibatches的大小batch_size=min(200,n_samples)，如果solver是’lbfgs’，分类器将不使用minibatch
6. learning_rate :学习率,用于权重更新,只有当solver为’sgd’时使用，{‘constant’，’invscaling’, ‘adaptive’},默认constant
- ‘constant’: 有’learning_rate_init’给定的恒定学习率
- ‘incscaling’：随着时间t使用’power_t’的逆标度指数不断降低学习率learning_rate_ ，effective_learning_rate = learning_rate_init / pow(t, power_t)
- ‘adaptive’：只要训练损耗在下降，就保持学习率为’learning_rate_init’不变，当连续两次不能降低训练损耗或验证分数停止升高至少tol时，将当前学习率除以5.
7. power_t: double, 可选, default 0.5，只有solver=’sgd’时使用，是逆扩展学习率的指数.当learning_rate=’invscaling’，用来更新有效学习率。
8. max_iter: int，可选，默认200，最大迭代次数。
9. random_state:int 或RandomState，可选，默认None，随机数生成器的状态或种子。
10. shuffle: bool，可选，默认True,只有当solver=’sgd’或者‘adam’时使用，判断是否在每次迭代时对样本进行清洗。
11. tol：float, 可选，默认1e-4，优化的容忍度
12. learning_rate_int:double,可选，默认0.001，初始学习率，控制更新权重的补偿，只有当solver=’sgd’ 或’adam’时使用。
14. verbose : bool, 可选, 默认False,是否将过程打印到stdout
15. warm_start : bool, 可选, 默认False,当设置成True，使用之前的解决方法作为初始拟合，否则释放之前的解决方法。
16. momentum : float, 默认 0.9,动量梯度下降更新，设置的范围应该0.0-1.0. 只有solver=’sgd’时使用.
17. nesterovs_momentum : boolean, 默认True, Whether to use Nesterov’s momentum. 只有solver=’sgd’并且momentum > 0使用.
18. early_stopping : bool, 默认False,只有solver=’sgd’或者’adam’时有效,判断当验证效果不再改善的时候是否终止训练，当为True时，自动选出10%的训练数据用于验证并在两步连续迭代改善，低于tol时终止训练。
19. validation_fraction : float, 可选, 默认 0.1,用作早期停止验证的预留训练数据集的比例，早0-1之间，只当early_stopping=True有用
20. beta_1 : float, 可选, 默认0.9，只有solver=’adam’时使用，估计一阶矩向量的指数衰减速率，[0,1)之间
21. beta_2 : float, 可选, 默认0.999,只有solver=’adam’时使用估计二阶矩向量的指数衰减速率[0,1)之间
22. epsilon : float, 可选, 默认1e-8,只有solver=’adam’时使用数值稳定值。
属性说明：
- classes_:每个输出的类标签
- loss_:损失函数计算出来的当前损失值
- coefs_:列表中的第i个元素表示i层的权重矩阵
- intercepts_:列表中第i个元素代表i+1层的偏差向量
- n_iter_ ：迭代次数
- n_layers_:层数
- n_outputs_:输出的个数
- out_activation_:输出激活函数的名称。
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
