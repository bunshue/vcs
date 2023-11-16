#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import tensorflow as tf

import numpy as np


x1=np.random.random((500,1))
x2=np.random.random((500,1))+1
x_train=np.concatenate((x1, x2))

y1=np.zeros((500,), dtype=int)
y2=np.ones((500,), dtype=int)
y_train=np.concatenate((y1, y2))

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=1),
  tf.keras.layers.Dense(units=10, activation=tf.nn.relu),
  tf.keras.layers.Dense(units=2, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)


#測試
x_test=np.array([[0.22],[0.31],[1.22],[1.33]])
y_test=np.array([0,0,1,1])

score = model.evaluate(x_test, y_test, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("predict:",predict)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])

