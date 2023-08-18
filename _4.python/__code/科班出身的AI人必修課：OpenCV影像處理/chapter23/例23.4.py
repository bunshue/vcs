# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:33:03 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
images=[]
images.append(cv2.imread("f01.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("f02.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("f11.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("f12.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.FisherFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("fTest.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)
