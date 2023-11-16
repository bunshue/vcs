#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np


iris = datasets.load_iris()

category=3
dim=4
x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)
y_train2=tf.contrib.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2=tf.contrib.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]",x_train[:4])
print("y_train[:4]",y_train[:4])
print("y_train2[:4]",y_train2[:4])

# 建立模型
model = tf.contrib.keras.models.Sequential()
model.add(tf.contrib.keras.layers.Dense(units=10,
    activation=tf.nn.relu,
    input_dim=dim))
model.add(tf.contrib.keras.layers.Dense(units=10,
    activation=tf.nn.relu ))
model.add(tf.contrib.keras.layers.Dense(units=category,
    activation=tf.nn.softmax ))
model.compile(optimizer='adam',
    loss=tf.contrib.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])

"""
# 使用Adam 每次計算移動0.001
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
    loss=tf.contrib.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])
"""
#
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.01, clipnorm=1.),
    loss=tf.contrib.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])


history=model.fit(x_train, y_train2,
          epochs=200,
          batch_size=128)

#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])


