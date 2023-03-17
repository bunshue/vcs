import cv2	#導入 OpenCV 模組
import numpy as np

filename = "C:\\______test_files\\picture1.jpg"

img = cv2.imread(filename)	#讀取本機圖片

#另存新檔
#cv2.imwrite('aaaa.bmp', img);

shape = img.shape
h = shape[0]    #高
w = shape[1]    #寬
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階

print("寬 = ",w,", 高 = ",h,", D = ",d)

#裁剪圖片

import matplotlib.pyplot as plt #匯入模組
import matplotlib.image as img  #匯入模組

image = img.imread(filename)
plt.imshow(image)	#顯示圖片
plt.show()

x_l, x_r = 100, 200 #保留的部分，由左而右
y_u, y_d = 100, 200 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]
plt.imshow(cut_img)
plt.show()




'''
cv2.imshow('image', img)

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗
'''



# python import module : OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組

#建立 detectFace Function 並可帶入 img 圖片名稱變數

def detectFace(img):
#取得將使用的檔案名稱，並讀取圖檔，接著把圖檔透過轉換函式轉為灰階影像，定義框出人臉時的框顏色

    print(img)
    filename = img.split(".")[0] # 取得檔案名稱(不添加副檔名)
    print(filename)
    img = cv2.imread(img)	#讀取本機圖片
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 透過轉換函式轉為灰階影像
    color = (0, 255, 0)  # 定義框的顏色

    # OpenCV 人臉識別分類器
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # 調用偵測識別人臉函式
    faceRects = face_classifier.detectMultiScale(
        grayImg, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

    #參數
    #image 	        待檢測圖片，一般為灰階影像，以便加快偵測速度
    #scaleFactor 	在前後兩次相繼的掃描中，搜索範圍的比例係數，默認值為 1.1
    #minNeighbors 	構成偵測目標的相鄰矩形的最小個數，默認值為 3
    #minSize & maxSize 	用來限制得到的目標區域範圍
    
    # 大於 0 則檢測到人臉
    if len(faceRects):  
        # 框出每一張人臉
        for faceRect in faceRects: 
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)

    # 將結果圖片輸出

    filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/human_face.jpg'
    print(filename2)
    cv2.imwrite(filename2, img)	#寫入本機圖片


print("框出照片中的人臉")
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human.jpg'
detectFace(filename)





