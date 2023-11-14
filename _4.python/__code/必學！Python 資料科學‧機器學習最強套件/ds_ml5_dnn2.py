"""

必學！Python 資料科學‧機器學習最強套件 DNN 2

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


15-1 建構神經網路模型

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

​

​

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

​

#超參數設定(二)：加入Dropout層

​

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

​

#超參數設定(三)：損失函數與優化器

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

#超參數設定(四)：batch_size

#超參數設定(五)：epochs

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

​

Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

11493376/11490434 [==============================] - 0s 0us/step

evaluate loss: 0.2699148654937744

evaluate acc: 0.9211999773979187

15-2 超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

​

​

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

​

model.add(Dense(256, activation='sigmoid', input_dim=784))

​

def funcA():

    model.add(Dense(128, activation='sigmoid'))

​

def funcB():

    model.add(Dense(128, activation='sigmoid'))

    model.add(Dense(128, activation='sigmoid'))

    model.add(Dense(128, activation='sigmoid'))

​

def funcC():

    model.add(Dense(1568, activation='sigmoid'))

    

# 選用模型A時就將B和C這兩行註解掉

# ---------------------------

funcA()

#funcB()

#funcC()

# ---------------------------

​

​

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

​

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

evaluate loss: 0.2971647381782532

evaluate acc: 0.9146999716758728

#15-3 超參數設定(二)：加入Dropout層

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

​

#超參數設定(二)：Dropout

​

#model.add(Dropout(rate=0.5))

​

model.add(Dense(10, activation='softmax'))

​

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

evaluate loss: 0.25099998712539673

evaluate acc: 0.9276999831199646

#15-4 超參數設定(三)：損失函數與優化器

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

​

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

​

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

​

#超參數設定(三)：優化器與學習率

​

def funcA():

    global lr

    lr = 0.01

​

def funcB():

    global lr

    lr = 0.1

​

def funcC():

    global lr

    lr = 1.0

​

# 選用模型A時就將B和C這兩行註解掉

# ---------------------------

funcA()

#funcB()

#funcC()

# ---------------------------

​

sgd = optimizers.SGD(learning_rate=lr)

​

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

model.fit(X_train, y_train, verbose=0, batch_size=32,epochs=3)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

​

evaluate loss: 0.2721501886844635

evaluate acc: 0.9229000210762024

#15-5 超參數設定(四)：batch_size

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

​

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

​

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

#超參數設定(四)：batch_size

def funcA():

    global batch_size

    batch_size = 16

​

def funcB():

    global batch_size

    batch_size = 32

​

def funcC():

    global batch_size

    batch_size = 64

​

# 選用模型A時就將B和C這兩行註解掉

# ---------------------------

funcA()

#funcB()

#funcC()

# ---------------------------

​

model.fit(X_train, y_train, verbose=0, batch_size=batch_size,epochs=3)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

evaluate loss: 0.2627638280391693

evaluate acc: 0.92330002784729

#15-6 超參數設定(五)：epochs

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense,Dropout

from tensorflow.keras import optimizers

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

%matplotlib inline

​

(X_train, y_train), (X_test, y_test) = mnist.load_data()

​

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

​

model = Sequential()

​

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

​

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

​

sgd = optimizers.SGD(learning_rate=0.01)

model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

​

#超參數設定(五)：epochs

​

def funcA():

    global epochs

    epochs = 5

​

def funcB():

    global epochs

    epochs = 10

​

def funcC():

    global epochs

    epochs = 60

​

# ---------------------------

# epochs: 5

funcA()

# epochs: 10

#funcB()

# epochs: 60

#funcC()

# ---------------------------

​

model.fit(X_train, y_train, verbose=1, batch_size=32,epochs=epochs)

​

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

Epoch 1/5

1875/1875 [==============================] - 4s 2ms/step - loss: 1.1571 - accuracy: 0.6310

Epoch 2/5

1875/1875 [==============================] - 3s 2ms/step - loss: 0.4723 - accuracy: 0.8590

Epoch 3/5

1875/1875 [==============================] - 3s 2ms/step - loss: 0.3932 - accuracy: 0.8846

Epoch 4/5

1875/1875 [==============================] - 3s 2ms/step - loss: 0.3535 - accuracy: 0.8963

Epoch 5/5

1875/1875 [==============================] - 3s 2ms/step - loss: 0.3386 - accuracy: 0.9003

evaluate loss: 0.23109018802642822

evaluate acc: 0.9323999881744385




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


