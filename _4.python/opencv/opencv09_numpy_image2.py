import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

images=[]
images.append(cv2.imread("images/a1.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/a2.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/b1.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/b2.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("images/a3.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)

print('------------------------------------------------------------')	#60個

images=[]
images.append(cv2.imread("images/e01.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/e02.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/e11.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/e12.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("images/eTest.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)

print('------------------------------------------------------------')	#60個

images=[]
images.append(cv2.imread("images/f01.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/f02.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/f11.png",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("images/f12.png",cv2.IMREAD_GRAYSCALE))
labels=[0,0,1,1]
#print(labels)
recognizer = cv2.face.FisherFaceRecognizer_create()
recognizer.train(images, np.array(labels))  
predict_image=cv2.imread("images/fTest.png",cv2.IMREAD_GRAYSCALE)
label,confidence= recognizer.predict(predict_image) 
print("label=",label)
print("confidence=",confidence)

print('------------------------------------------------------------')	#60個

