#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
# sudo apt-get install python-numpy python3-numpy python-matplotlib python3-matplotlib

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#from tensorflow.examples.tutorials.mnist
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random as ran

import tensorflow as tf



# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
print('x_train = ' + str(x_train.shape))
print('y_train = ' + str(y_train.shape))

# 顯示資料內容
def printMatrixE(a):
   rows = a.shape[0]
   cols = a.shape[1]
   for i in range(0,rows):
      str1=""
      for j in range(0,cols):
         str1=str1+("%3.0f " % a[i, j])
      print(str1)
   print("")

printMatrixE(x_train[0])
print('y_train[0] = ' + str(y_train[0]))






