# -*- coding: utf-8 -*-

from numpy import *
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml')

img = cv2.imread('mypicture.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ʶ������ͼƬ�е���������.���ض���ľ��γߴ�
# ����ԭ��detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray��Ҫʶ���ͼƬ
# 1.2����ʾÿ��ͼ��ߴ��С�ı���
# 3����ʾÿһ��Ŀ������Ҫ����⵽4�β��������Ŀ��(��Ϊ��Χ�����غͲ�ͬ�Ĵ��ڴ�С�����Լ�⵽����)
# CV_HAAR_SCALE_IMAGE��ʾ�������ŷ���������⣬��������ͼ��Size(30, 30)ΪĿ�����С���ߴ�
# faces����ʾ��⵽������Ŀ������
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for (x,y,w,h) in faces:
	img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),4)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("paulwalker.head.jpg", img) # ����ͼƬ