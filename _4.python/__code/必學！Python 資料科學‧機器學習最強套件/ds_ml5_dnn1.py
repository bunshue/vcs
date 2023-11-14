"""

必學！Python 資料科學‧機器學習最強套件 DNN 1

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


14-2-3 Final 建構神經網路模型

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.utils import plot_model

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

​

model = Sequential()

​

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

​

​

plot_model(model, show_shapes=True, show_layer_names=False)

​

Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

11493376/11490434 [==============================] - 0s 0us/step

14-2-4 Final 訓練模型

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.utils import plot_model

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

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

​

history = model.fit(X_train, y_train, verbose=1, batch_size=32,epochs=3)

​

plt.plot(history.history["accuracy"], label="accuracy")

plt.ylabel("accuracy")

plt.xlabel("epoch")

plt.legend(loc="best")

plt.show()

Epoch 1/3

1875/1875 [==============================] - 7s 2ms/step - loss: 0.1026 - accuracy: 0.8323

Epoch 2/3

1875/1875 [==============================] - 4s 2ms/step - loss: 0.0411 - accuracy: 0.9319

Epoch 3/3

1875/1875 [==============================] - 4s 2ms/step - loss: 0.0349 - accuracy: 0.9420

14-2-5 Final 評估模型成效

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.utils import plot_model

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

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0)

​

score = model.evaluate(X_test, y_test,verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

​

evaluate loss: 0.0431341715157032

evaluate acc: 0.9291999936103821

#14-2-6 Final 用模型預測答案

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.utils import plot_model

from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt

import numpy as np

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

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0)

​

​

for i in range(10):

    plt.subplot(1, 10, i+1)

    plt.imshow(X_test[i].reshape((28,28)), "gray")

plt.show()

​

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

​

[7 2 1 0 4 1 4 9 4 9]




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


