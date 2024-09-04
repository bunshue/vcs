"""

必學！Python 資料科學‧機器學習最強套件 DNN 1


pip install pydot

"""

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# Final 建構神經網路模型

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

# plot_model(model, show_shapes=True, show_layer_names=False)
# 目前plot_model不能用

print("------------------------------------------------------------")  # 60個

# Final 訓練模型

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

# 跑很久
"""
#history = model.fit(X_train, y_train, verbose=1, batch_size=32,epochs=3)
history = model.fit(X_train, y_train, verbose=1, batch_size=960,epochs=1)

plt.plot(history.history["accuracy"], label="accuracy")

plt.ylabel("accuracy")

plt.xlabel("epoch")

plt.legend(loc="best")

plt.show()
"""
print("------------------------------------------------------------")  # 60個

# Final 評估模型成效

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, verbose=0)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

# evaluate loss: 0.0431341715157032
# evaluate acc: 0.9291999936103821

print("------------------------------------------------------------")  # 60個

# Final 用模型預測答案

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, verbose=0)

for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(X_test[i].reshape((28, 28)), "gray")

plt.show()

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

print("------------------------------------------------------------")  # 60個
"""
#建構神經網路模型

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

#(X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist['x_train'], mnist['y_train']  
X_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元
model.add(Dense(256, activation='sigmoid', input_dim=784))
model.add(Dense(128, activation='relu'))

#超參數設定(二)：加入Dropout層
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation='softmax'))

#超參數設定(三)：損失函數與優化器
sgd = optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

#超參數設定(四)：batch_size

#超參數設定(五)：epochs
model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2699148654937744
#evaluate acc: 0.9211999773979187

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

#(X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist['x_train'], mnist['y_train']
X_test, y_test = mnist['x_test'], mnist['y_test']
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

model.add(Dense(256, activation='sigmoid', input_dim=784))

def funcA():
    model.add(Dense(128, activation='sigmoid'))

def funcB():
    model.add(Dense(128, activation='sigmoid'))
    model.add(Dense(128, activation='sigmoid'))
    model.add(Dense(128, activation='sigmoid'))

def funcC():
    model.add(Dense(1568, activation='sigmoid'))

# 選用模型A時就將B和C這兩行註解掉
# ---------------------------
funcA()

#funcB()

#funcC()

# ---------------------------

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2971647381782532
#evaluate acc: 0.9146999716758728

#15-3 超參數設定(二)：加入Dropout層

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

#(X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist['x_train'], mnist['y_train']
X_test, y_test = mnist['x_test'], mnist['y_test']
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

#超參數設定(二)：Dropout

#model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.25099998712539673
#evaluate acc: 0.9276999831199646

#15-4 超參數設定(三)：損失函數與優化器

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

#(X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist['x_train'], mnist['y_train']
X_test, y_test = mnist['x_test'], mnist['y_test']
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation='sigmoid', input_dim=784))
model.add(Dense(128, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation='softmax'))

#超參數設定(三)：優化器與學習率

def funcA():
    global lr
    lr = 0.01

def funcB():
    global lr
    lr = 0.1

def funcC():
    global lr
    lr = 1.0

# 選用模型A時就將B和C這兩行註解掉
# ---------------------------

funcA()
#funcB()
#funcC()

# ---------------------------

sgd = optimizers.SGD(learning_rate=lr)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2721501886844635

#evaluate acc: 0.9229000210762024

print('------------------------------------------------------------')	#60個
"""
# 超參數設定(四)：batch_size

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))
model.add(Dense(128, activation="relu"))
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation="softmax"))

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# 超參數設定(四)：batch_size


def funcA():
    global batch_size
    batch_size = 16


def funcB():
    global batch_size
    batch_size = 32


def funcC():
    global batch_size
    batch_size = 64


# 選用模型A時就將B和C這兩行註解掉
# ---------------------------

funcA()

# funcB()

# funcC()

# ---------------------------

model.fit(X_train, y_train, verbose=0, batch_size=batch_size, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

# evaluate loss: 0.2627638280391693
# evaluate acc: 0.92330002784729

print("------------------------------------------------------------")  # 60個

# 超參數設定(五)：epochs

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation="softmax"))

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# 超參數設定(五)：epochs


def funcA():
    global epochs
    epochs = 5


def funcB():
    global epochs
    epochs = 10


def funcC():
    global epochs
    epochs = 60


# ---------------------------
# epochs: 5


funcA()

# epochs: 10

# funcB()

# epochs: 60

# funcC()

# ---------------------------

"""
#做很久
model.fit(X_train, y_train, verbose=1, batch_size=32,epochs=epochs)
score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.23109018802642822

#evaluate acc: 0.9323999881744385
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
