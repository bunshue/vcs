#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import tensorflow as tf


# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()


print('x_train = ' + str(x_train.shape))
print('y_train = ' + str(y_train.shape))




