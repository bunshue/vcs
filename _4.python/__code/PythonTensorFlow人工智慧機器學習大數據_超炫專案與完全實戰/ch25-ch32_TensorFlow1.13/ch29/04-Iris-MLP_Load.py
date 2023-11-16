#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
from time import time
from tensorflow.keras.models import model_from_json


iris = datasets.load_iris()

category=3
dim=4
x_train , x_test , y_train , y_test = train_test_split(iris.data,iris.target,test_size=0.2)
y_train2=tf.contrib.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2=tf.contrib.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]",x_train[:4])
print("y_train[:4]",y_train[:4])
print("y_train2[:4]",y_train2[:4])

# 讀取模型架構
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# 讀取模型權重
model.load_weights("model.h5")
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
    loss = tf.contrib.keras.losses.categorical_crossentropy,
    metrics = ['accuracy'])



#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

predict2 = model.predict_classes(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])

