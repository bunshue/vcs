#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import tensorflow as tf
import numpy as np
from sklearn.datasets import load_digits
import tensorflow as tf

from tensorflow.keras.callbacks import TensorBoard

# 影像的類別數目
category = 10



# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


# 標準化輸入資料
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)


# 建立模型
model = tf.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3),
                 padding="same",
                 activation='relu',
                 input_shape=(28,28,1)))

model.add(tf.keras.layers.Conv2D(filters=40, kernel_size=(2, 2),padding="same", activation='relu'))

# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
model.add(tf.keras.layers.Conv2D(filters=40, kernel_size=(2, 2),padding="same", activation='relu'))

# Dropout Layer
model.add(tf.keras.layers.Dropout(rate=0.01))

# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())
# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation='relu'))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation='relu'))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(units=category,
    activation=tf.nn.softmax ))

model.summary()

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adadelta(),
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir="logs")
# 訓練模型


gen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=8, width_shift_range=0.08, shear_range=0.3,
                         height_shift_range=0.08, zoom_range=0.08)


train_generator = gen.flow(x_train, y_train2, batch_size=128)
# 讀取模型架構
try:
    with open('model_ImageDataGenerator.h5', 'r') as load_weights:
        # 讀取模型權重
        model.load_weights("model_ImageDataGenerator.h5")

except IOError:
    print("File not accessible")

checkpoint = tf.keras.callbacks.ModelCheckpoint("model_ImageDataGenerator.h5", monitor='accuracy', verbose=1,
    save_best_only=True, mode='auto', save_freq=1)

#保存模型架構
with open("model_ImageDataGenerator.json", "w") as json_file:
   json_file.write(model.to_json())
# 訓練模型

# 訓練模型

history=model.fit(train_generator,
							  callbacks=[checkpoint],
          epochs=400)


#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2[:20])
print("y_test",y_test[:20])

import matplotlib.pyplot as plt
plt.plot(history.history['acc'])
plt.plot(history.history['loss'])
plt.title('model accuracy')
plt.ylabel('acc & loss')
plt.xlabel('epoch')
plt.legend(['acc', 'loss'], loc='upper left')
plt.show()


#保存模型架構
with open("model_img.json", "w") as json_file:
   json_file.write(model.to_json())
#保存模型權重
model.save_weights("model_img.h5")
