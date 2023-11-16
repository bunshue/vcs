#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import tensorflow as tf
import numpy as np
#from sklearn.datasets import load_digits
#import tensorflow as tf




# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
"""
x_train=x_train[:1000]
x_test=x_test[:1000]
y_train=y_train[:1000]
y_test=y_test[:1000]
"""

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28,28, 1)
x_test = x_test.reshape(x_test.shape[0], 28,28, 1)

# 標準化輸入資料
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 將數字轉為 One-hot 向量
y_train2 = tf.contrib.keras.utils.to_categorical(y_train, 10)
y_test2 = tf.contrib.keras.utils.to_categorical(y_test, 10)

# 建立模型
model = tf.contrib.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Conv2D(filters=3, kernel_size=(3, 3),
                 padding="same",
                 activation='relu',
                 input_shape=(28,28,1)))
# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
# 2D 的 Convolution Layer
model.add(tf.keras.layers.Conv2D(filters=9, kernel_size=(2, 2),padding="same", activation='relu'))
# Dropout Layer
model.add(tf.keras.layers.Dropout(rate=0.33))

# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())
# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(10, activation='relu'))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(units=10,
    activation=tf.nn.softmax ))



# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(loss=tf.contrib.keras.losses.categorical_crossentropy,
              optimizer=tf.contrib.keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.summary()

# 訓練模型
model.fit(x_train, y_train2,
          batch_size=1024,
          epochs=20,
          verbose=1)




#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])






#保存模型架構
with open("model.json", "w") as json_file:
   json_file.write(model.to_json())
#保存模型權重
model.save_weights("model.h5")
