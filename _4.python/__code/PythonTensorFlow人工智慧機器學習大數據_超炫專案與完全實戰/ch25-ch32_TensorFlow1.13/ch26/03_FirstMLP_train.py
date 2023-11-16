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
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_dim=1),
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)



