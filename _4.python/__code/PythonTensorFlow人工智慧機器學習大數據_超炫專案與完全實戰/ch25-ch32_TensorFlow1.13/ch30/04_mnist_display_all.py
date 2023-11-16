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

# 顯示其中的圖形
num=0
plt.title('x_train[%d]  Label: %d' % (num, y_train[num]))
plt.imshow(x_train[num], cmap=plt.get_cmap('gray_r'))
plt.show()




def display_mult_flat(start, stop,label):
    images = x_train[start].reshape([1,784])  # 784=28*28
    for i in range(start+1,stop):
        label2=int(y_train[i])
        if label==label2:
           images = np.concatenate((images, x_train[i].reshape([1,28*28])))
    plt.imshow(images, cmap=plt.get_cmap('gray_r'))
    plt.show()


display_mult_flat(0,2000,7)
display_mult_flat(0,2000,1)





