#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#from tensorflow.examples.tutorials.mnist
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np



# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
print('x_train = ' + str(x_train.shape))
print('y_train = ' + str(y_train.shape))



import tensorflow as tf
import numpy as np
from sklearn.datasets import load_digits
import tensorflow as tf

# 影像的類別數目
num_classes = 10

# 輸入的手寫影像解析度
img_rows, img_cols = 28, 28

# 載入資料（將資料打散，放入 train 與 test 資料集）
#(x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()



print('x_train before reshape:', x_train.shape)
# 將原始資料轉為正確的影像排列方式
dim=img_rows*img_cols*1
x_train = x_train.reshape(x_train.shape[0], dim)
x_test = x_test.reshape(x_test.shape[0], dim)
print('x_train after reshape:', x_train.shape)

# 標準化輸入資料
print('x_train before div 255:',x_train[0][180:195])
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train before div 255 ', x_train[0][180:195])







print('y_train shape:', y_train.shape)
print(y_train[:10])
# 將數字轉為 One-hot 向量
category=10
y_train2 = tf.contrib.keras.utils.to_categorical(y_train, category)
y_test2 = tf.contrib.keras.utils.to_categorical(y_test, category)
print("y_train2 to_categorical shape=",y_train2.shape)     #輸出 (60000, 10)
print(y_train2[:10])







