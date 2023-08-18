# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:33:03 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
images=[]
images.append(cv2.imread("e01.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("e02.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("e11.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("e12.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("eTest.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)
