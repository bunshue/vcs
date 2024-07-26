"""

必學！Python 資料科學‧機器學習最強套件 CNN 2


"""

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
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

import time

print('------------------------------------------------------------')	#60個
'''
#標準化

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i])

plt.suptitle('The original image', fontsize=12)
plt.show()

# 建立 ImageDataGenerator 的操作物件

datagen = ImageDataGenerator(samplewise_center=True, 
                samplewise_std_normalization=True)

# 進行標準化

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), X_batch.max())

X_batch += 127.0

X_batch = X_batch.astype('uint8')

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle('Standardization result', fontsize=12)

plt.show()

print('------------------------------------------------------------')	#60個

#白化

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""

X_train = X_train[:300]

X_test = X_test[:100]

y_train = y_train[:300]

y_test = y_test[:100]

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i])

plt.suptitle('The original image', fontsize=12)

plt.show()

# 建立ImageDataGenerator的操作物件

datagen = ImageDataGenerator(zca_whitening=True)

# 白化處理

datagen.fit(X_train)

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), abs(X_batch.max()))

X_batch += 127

X_batch = X_batch.astype('uint8')

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle('Whitening result', fontsize=12)

plt.show()
'''
print('------------------------------------------------------------')	#60個

#批次正規化

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Activation, Conv2D, Dense, Flatten, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical

#(X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist['x_train'], mnist['y_train']  
X_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

X_train = np.reshape(a=X_train, newshape=(-1,28,28,1))

X_test = np.reshape(a = X_test,newshape=(-1,28,28,1))

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 使用 ReLU 函數當做啟動函數

model = Sequential()

model.add(Conv2D(input_shape=(28, 28, 1), filters=32,
                 kernel_size=(2, 2), strides=(1, 1), padding="same"))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=(1, 1), padding="same"))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(256))

# 批次正規化

model.add(BatchNormalization())

model.add(Activation('relu'))

model.add(Dense(128))

# 批次正規化

model.add(BatchNormalization())

model.add(Activation('relu'))

model.add(Dense(10))

model.add(Activation('softmax'))

# 執行compile
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

"""
# 執行訓練
# 做很久
history = model.fit(X_train, y_train, batch_size=32, epochs=3, validation_data=(X_test, y_test))

# 做可視化處理

plt.plot(history.history['accuracy'], label='acc', ls='-', marker='o')

plt.plot(history.history['val_accuracy'], label='val_acc', ls='-', marker='x')

plt.ylabel('accuracy')

plt.xlabel('epoch')

plt.suptitle("model", fontsize=12)

plt.show()
"""

print('------------------------------------------------------------')	#60個

#遷移學習

#下載VGG16有問題

"""
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

#下載
#https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
#將檔案改名成
#cifar-10-batches-py.tar.gz
#放在C:/Users/070601/.keras/datasets/之下

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 定義輸入形式

input_tensor = Input(shape=(32, 32, 3))

vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

top_model = vgg16.output

top_model = Flatten(input_shape=vgg16.output_shape[1:])(top_model)

top_model = Dense(256, activation='sigmoid')(top_model)

top_model = Dropout(0.5)(top_model)

top_model = Dense(10, activation='softmax')(top_model)

# 將vgg16和top_model做連接, 建構出 model 模型

model = Model(inputs=vgg16.input, outputs=top_model)

# 將前19層的權重固定住, 不做訓練
for layer in model.layers[:19]:
    layer.trainable = False

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 訓練批量是32, epoch是3
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=5)

# 評估準確度

scores = model.evaluate(X_test, y_test, verbose=1)

print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 對前10張做可視化處理
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i])

plt.suptitle("The first ten of the test data",fontsize=16)

plt.show()

# 前10張的預測結果
pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)
"""
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


