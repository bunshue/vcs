# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:33:20 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""


import cv2
import numpy as np
#------------生成一个都是0值的a-------------------
a=np.zeros((5,5),dtype=np.uint8)
#-------随机将其中10个位置上的数值设置为1------------
#---times控制次数
#---i,j是随机生成的行、列位置
#---a[i,j]=1,将随机挑选出来的位置上的值设置为1
for times in range(10):
    i=np.random.randint(0,5)
    j=np.random.randint(0,5)
    a[i,j]=1
#-------打印a，观察a内值的情况-----------
print("a=\n",a)
#------查找a内非零值的位置信息------------
loc = cv2.findNonZero(a)
#-----将a内非零值的位置信息输出------------
print("a内非零值位置:\n",loc)
