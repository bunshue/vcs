"""


"""

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個
'''
img = cv2.imread(filename, 1)

print('改變圖片大小')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

print('旋轉')
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#cv2.imwrite("tmp_pic01.jpg", img)     # 將檔案寫入 tmp_pic01.jpg

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

import random

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

img = cv2.imread(filename, -1)

print(img.shape)
print(img.shape[0])     #H
print(img.shape[1])     #W

print('將一些點數改為亂數點數')
for i in range(30):
        for j in range(img.shape[1]//2):
                img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('複製貼上圖片的一部分')

# Copy part of image
#          H        W
tag = img[100:200, 130:230]
img[20:120, 180:280] = tag

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

import os

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cv2.namedWindow("Peony1")                       # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)    # 可以調整大小
img1 = cv2.imread(filename)                         # 彩色讀取
img2 = cv2.imread(filename, 0)                      # 灰色讀取
cv2.imshow("Peony1", img1)                      # 顯示影像img1
cv2.imshow("Peony2", img2)                      # 顯示影像img2
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyWindow("Peony1")                     # 刪除Peony1
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyAllWindows()                             # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cv2.namedWindow("Peony")        # 使用預設
img = cv2.imread(filename)          # 彩色讀取
cv2.imshow("Peony", img)        # 顯示影像img
cv2.imwrite("tmp_pic01.jpg", img)     # 將檔案寫入 tmp_pic01.jpg
cv2.waitKey(3000)                   # 等待3秒
cv2.destroyAllWindows()             # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)                # BGR 讀取
cv2.imshow("Peony", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)                  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cv2.namedWindow("Peony")                            # 使用預設
img = cv2.imread(filename)                     # 彩色讀取
cv2.line(img,(10,300),(250,300),(255,0,0),5)          # 輸出線條
cv2.rectangle(img,(20,20),(240,250),(0,0,255),2)     # 輸出矩陣
cv2.putText(img,"Peony",(10,250),              # 輸出文字
            cv2.FONT_ITALIC,3,(255,0,0), 8)
cv2.imshow("Peony", img)                            # 顯示影像img
cv2.waitKey(3000)                                       # 等待3秒
cv2.destroyAllWindows()                                 # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

""" 人臉辨識
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)          # 建立辨識物件
img = cv2.imread(filename)                              # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
cv2.imshow("Face", img)                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)          # 建立辨識物件
img = cv2.imread("data/g2.jpg")                              # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
cv2.imshow("Face", img)                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

if not os.path.exists("facedata"):                  # 如果不存在資料夾
    os.mkdir("facedata")                            # 就建立facedata

pictPath = r'C:\opencv\data\haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(pictPath)      # 建立辨識檔案物件
img = cv2.imread("data/g5.jpg")                          # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))          # 偵測影像
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
# 同時將影像儲存在facedata資料夾, 但是必須先建立此資料夾
num = 1                                             # 檔名編號
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    filename = "facedata\\face" + str(num) + ".jpg" # 路徑 + 檔名
    imageCrop = img[y:y+h,x:x+w]                    # 裁切
    imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
    cv2.imwrite(filename, imageResize)              # 儲存影像
    num += 1                                        # 檔案編號                                
    
cv2.imshow("Face", img)                             # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import Image

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)       # 將影像寫入tmp_photo.jpg
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_faceout.jpg")                       # 儲存檔案
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)
"""
print("------------------------------------------------------------")  # 60個

print('檢查兩圖之差異度')

from functools import reduce
from PIL import Image
import math, operator

filename_face1 = "data/face1.jpg"
filename_face2 = "data/face1.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
print("RMS = ", RMS)

filename_face1 = "data/face1.jpg"
filename_face2 = "data/faceout.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
print("RMS = ", RMS)

print("------------------------------------------------------------")  # 60個
"""
from PIL import Image
from functools import reduce
import math, operator

ID = input("請輸入身份證字號 = ")               # 讀取所輸入的身分證字號
face = ID + ".jpg"                              # 未來的臉形檔案

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)       # 將影像寫入tmp_photo.jpg           
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_newface.jpg")                       # 儲存檔案

print('檢查兩圖之差異度')
h1 = Image.open(face).histogram()
h2 = Image.open("tmp_newface.jpg").histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
if RMS <= 100:
    print("歡迎出入境")
else:
    print("比對失敗")       
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

from PIL import Image

ID = input("請輸入身份證字號 = ")               # 讀取所輸入的身分證字號
print("臉形檔案將儲存在 ", ID + ".jpg")
faceFile = "tmp_" + ID + ".jpg"                          # 未來的臉形檔案

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)       # 將影像寫入tmp_photo.jpg
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save(faceFile)                            # 儲存檔案
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)
"""



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print("absolute")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #確定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result
    
original_image_test1 = cv2.imread('data/lena.png',0)
def my_laplace_result_add_abs(image, model):
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            if model[i][j] < 0:
                model[i][j] = 0
            if model[i][j] > 255:
                model[i][j] = 255
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

# 調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type='big')
# 繪制結果
fig = plt.figure()
fig.add_subplot(121)
plt.title('原始圖像')
plt.imshow(original_image_test1)
fig.add_subplot(122)
plt.title('銳化濾波')
plt.imshow(my_laplace_result_add_abs(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("Canny1")

import matplotlib.pyplot as plt
import numpy as np  

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

original_img = cv2.imread("data/lena.png", 0)
#canny(): 邊緣檢測
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)   #執行高斯模糊化
canny = cv2.Canny(img1, 50, 150)

#形態學：邊緣檢測
_,Thr_img = cv2.threshold(original_img,210,255,cv2.THRESH_BINARY)#設定紅色通道閾值210（閾值影響梯度運算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))         #定義矩形結構元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度

plt.subplot(131)
cv2.imshow("原始圖像", original_img) 

plt.subplot(132)
cv2.imshow("梯度", gradient) 

plt.subplot(133)
cv2.imshow('Canny函數', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("CannyThreshold")

import numpy as np
 
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0) #執行高斯模糊化
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # 只需在原始圖像的邊緣添加一些顏色
    cv2.imshow('canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3 
img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.namedWindow('canny demo') 
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
 
CannyThreshold(0)  # 初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("createCLAHE_image")

import numpy as np

img = cv2.imread('data/building.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('img',img)
cv2.imshow('cl1',cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("defogging")

import numpy as np

def zmMinFilterGray(src, r=7):
    #最小值濾波，r是濾波器半徑
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))

def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I * p, -1, (r, r))
    cov_Ip = m_Ip - m_I * m_p
    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I

    a = cov_Ip / (var_I + eps)
    b = m_p - a * m_I
    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))
    return m_a * I + m_b

def Defog(m, r, eps, w, maxV1):                 #輸入rgb圖像，值范圍[0,1]
    #計算大氣遮罩圖像V1和光照值A, V1 = 1-t/A
    V1 = np.min(m, 2)                           #得到暗通道圖像
    Dark_Channel = zmMinFilterGray(V1, 5)
    cv2.imshow('wu_Dark',Dark_Channel)    #查看暗通道
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    V1 = guidedfilter(V1, Dark_Channel, r, eps)  #使用引導濾波優化
    bins = 2000
    ht = np.histogram(V1, bins)                  #計算大氣光照A
    d = np.cumsum(ht[0]) / float(V1.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()
    V1 = np.minimum(V1 * w, maxV1)               #對值范圍進行限制
    return V1, A

def deHaze(m, r=81, eps=0.001, w=0.95, maxV1=0.80, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxV1)             #得到遮罩圖像和大氣光照

    for k in range(3):
        Y[:,:,k] = (m[:,:,k] - Mask_img)/(1-Mask_img/A)  #顏色校正
    Y = np.clip(Y, 0, 1)
    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))       #gamma校正,默認不進行該操作
    return Y

m = deHaze(cv2.imread('data/wu.jpg') / 255.0) * 255
cv2.imwrite('tmp_wu_2.png', m)

print("------------------------------------------------------------")  # 60個

print("equalizeHist_image")

import numpy as np

img = cv2.imread('data/wu_2.png',0)
equ = cv2.equalizeHist(img) #只能傳入灰度圖
res = np.hstack((img,equ))  #圖像列拼接（用于顯示）

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("gaussion")

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

print('跑很久 skip')
"""
#高斯濾波函數
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*math.pi*sigma**2)

#產生高斯濾波矩陣
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根據尺寸和sigma值計算高斯矩陣
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    #將高斯矩陣歸一化
    blur_retric = blur_retric / blur_retric[0][0]
    #將高斯矩陣轉換為整數
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩陣
    return blur_retric

#計算灰度圖像的高斯濾波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data += image[i+ii-sizepart][j+jj-sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0
    #返回變換后的圖像矩陣
    return image

#計算彩色圖像的高斯濾波
def my_gaussion_blur_RGB(image, size, sigma):
    (b ,r, g) = cv2.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

image_test1 = cv2.imread('data/lena.png')
#進行高斯濾波器比較
my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
computer_image_blur_gaussion = cv2.GaussianBlur(image_test1, (5, 5), 0.75)  #執行高斯模糊化

fig = plt.figure(figsize = (20, 15))

fig.add_subplot(131)
plt.title('原始圖像')
plt.imshow(image_test1)

fig.add_subplot(132)
plt.title('自定義高斯濾波器')
plt.imshow(my_image_blur_gaussion)

fig.add_subplot(133)
plt.title('庫高斯濾波器')
plt.imshow(computer_image_blur_gaussion)

plt.show()
"""
print("------------------------------------------------------------")  # 60個

print("gradient")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 輸入圖像，輸出提取的邊緣信息
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape,dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    # 確定拉普拉斯模板的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += image[i+ii-1][j+jj-1] * my_model_x[ii][jj]
                        result_y[i][j] += image[i+ii-1][j+jj-1] * my_model_y[ii][jj]
            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            if result[i][j] > 255:
                result[i][j] = 255
    return result


# 將邊緣信息按一定比例加到原始圖像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result



original_image_lena= cv2.imread('data/lena.png', 0)

# 獲得圖像邊界信息
edge_image_lena = my_sobel_sharpen(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_result_add(original_image_lena, edge_image_lena, -0.5)

# 顯示結果
plt.subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('邊緣檢測')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('梯度處理')
plt.imshow(sharpen_image_lena)

plt.show()


print("------------------------------------------------------------")  # 60個

print("imaeg_laplace")

import matplotlib.pyplot as plt
import math
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

original_image_test1 = cv2.imread('data/lena.png',0)
#用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #確定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result

#將計算結果限制為正值
def my_show_edge(model):
    #這里一定要用copy函數，不然會改變原來數組的值
    mid_model = model.copy()
    for i in range(mid_model.shape[0]):
        for j in range(mid_model.shape[1]):
            if mid_model[i][j] < 0:
                mid_model[i][j] = 0
            if mid_model[i][j] > 255:
                mid_model[i][j] = 255
    return mid_model

#調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type='big')
#繪制結果
fig = plt.figure()
fig.add_subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_test1)
fig.add_subplot(132)
plt.title('邊緣檢測')
plt.imshow(my_show_edge(result))
fig.add_subplot(133)
plt.title('銳化處理')
plt.imshow(my_laplace_result_add(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")

from matplotlib import pyplot as plt

# 用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image-model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

original_image_test1 = cv2.imread('data/lena.png',0)
# 函數中的參數ddepth為輸出圖像的深度，也就是每個像素點是多少位的。
# CV_16S表示16位有符號數
computer_result = cv2.Laplacian(original_image_test1,ksize=3,ddepth=cv2.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_dft2")

import numpy as np
import matplotlib.pyplot as plt

print('跑不出來 skip')
"""
PI = 3.141591265

img = plt.imread('data/castle3.jpg')
#根據公式轉成灰度圖
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]

#顯示原圖
plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')

#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(img)
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(132),plt.imshow(log_fft2,'gray'),plt.title('log_fft2')

h , w = img.shape
#生成一個同樣大小的復數矩陣
F = np.zeros([h,w],'complex128')
for u in range(h):
    for v in range(w):
        res = 0
        for x in range(h):
            for y in range(w):
                res += img[x,y] * np.exp(-1.j * 2 * PI * (u * x / h + v * y / w))
        F[u,v] = res

log_F = np.log(1 + np.abs(F))
plt.subplot(133)
plt.imshow(log_F,'gray')
plt.title('log_F')
"""

print("------------------------------------------------------------")  # 60個

print("image_fft")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pylab import mpl

#mpl.rcParams['font.sans-serif'] = ['SimHei']   #顯示中文
#mpl.rcParams['axes.unicode_minus']=False       #顯示負號

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

Fs=1200;  #采樣頻率
Ts=1/Fs;  #采樣區間
x=np.arange(0,1,Ts)  #時間向量，1200個
y=5*np.sin(2*np.pi*600*x)
N=1200
frq=np.arange(N)            #頻率數1200個數
half_x=frq[range(int(N/2))]  #取一半區間
fft_y=np.fft.fft(y)
abs_y=np.abs(fft_y)                #取復數的絕對值，即復數的模(雙邊頻譜)
angle_y=180*np.angle(fft_y)/np.pi   #取復數的弧度,并換算成角度
gui_y=abs_y/N                       #歸一化處理（雙邊頻譜）                              
gui_half_y = gui_y[range(int(N/2))] #由于對稱性，只取一半區間（單邊頻譜）
#畫出原始波形的前50個點
plt.subplot(231)
plt.plot(frq[0:50],y[0:50])   
plt.title('原始波形')
#畫出雙邊未求絕對值的振幅譜
plt.subplot(232)
plt.plot(frq,fft_y,'black')
plt.title('雙邊振幅譜(未求振幅絕對值)') 
#畫出雙邊求絕對值的振幅譜
plt.subplot(233)
plt.plot(frq,abs_y,'r')
plt.title('雙邊振幅譜(未歸一化)') 
#畫出雙邊相位譜
plt.subplot(234)
plt.plot(frq[0:50],angle_y[0:50],'violet')
plt.title('雙邊相位譜(未歸一化)')
#畫出雙邊振幅譜(歸一化)
plt.subplot(235)
plt.plot(frq,gui_y,'g')
plt.title('雙邊振幅譜(歸一化)')

#畫出單邊振幅譜(歸一化)
plt.subplot(236)
plt.plot(half_x,gui_half_y,'blue')
plt.title('單邊振幅譜(歸一化)')
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

img = plt.imread('data/castle3.jpg')

#根據公式轉成灰度圖
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]

#顯示原圖
plt.subplot(231)
plt.imshow(img,'gray')
plt.title('原始圖像')
#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(img)
plt.subplot(232)
plt.imshow(np.abs(fft2),'gray')
plt.title('二維傅里葉變換')
#將圖像變換的原點移動到頻域矩形的中心，并顯示效果
shift2center = np.fft.fftshift(fft2)
plt.subplot(233)
plt.imshow(np.abs(shift2center),'gray')
plt.title('頻域矩形的中心')
#對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(235)
plt.imshow(log_fft2,'gray')
plt.title('傅立葉變換對數變換')
#對中心化后的結果進行對數變換，并顯示結果
log_shift2center = np.log(1 + np.abs(shift2center))
plt.subplot(236)
plt.imshow(log_shift2center,'gray')
plt.title('中心化的對數變化')

plt.show()

print("------------------------------------------------------------")  # 60個

print("magnitude_spectrum")

import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

img = cv2.imread('data/lena.png',0)  
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('原始圖像')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('級頻譜')
plt.xticks([]), plt.yticks([])

plt.show()

print("------------------------------------------------------------")  # 60個

print("median 跑一陣子")

import matplotlib.pyplot as plt
import math
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def get_median(data):
    data.sort()
    half = len(data) // 2
    return data[half]

#計算灰度圖像的中值濾波
def my_median_blur_gray(image, size):
    data = []
    sizepart = int(size/2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #首先判斷所以是否超出范圍，也可以事先對圖像進行零填充
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data.append(image[i+ii-sizepart][j+jj-sizepart])
            #取每個區域內的中位數
            image[i][j] = int(get_median(data))
            data=[]
    return image

#計算彩色圖像的中值濾波
def my_median_blur_RGB(image, size):
    (b ,r, g) = cv2.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

if __name__ == '__main__':
    image_test1 = cv2.imread('data/worm.jpg')
    #調用自定義函數
    my_image_blur_median = my_median_blur_RGB(image_test1, 5)
    #調用庫函數
    computer_image_blur_median = cv2.medianBlur(image_test1, 5)
    fig = plt.figure()
    fig.add_subplot(131)
    plt.title('原圖')
    plt.imshow(image_test1)
    fig.add_subplot(132)
    plt.title('自定義函數濾波')
    plt.imshow(my_image_blur_median)
    fig.add_subplot(133)
    plt.title('庫函數濾波')
    plt.imshow(computer_image_blur_median)
    plt.show()

print("------------------------------------------------------------")  # 60個

print("optimize")

import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def ComputeMinLevel(hist, pnum):
    index = np.add.accumulate(hist)
    return np.argwhere(index>pnum * 8.3 * 0.01)[0][0]

def ComputeMaxLevel(hist, pnum):
    hist_0 = hist[::-1]
    Iter_sum = np.add.accumulate(hist_0)
    index = np.argwhere(Iter_sum > (pnum * 2.2 * 0.01))[0][0]
    return 255-index

def LinearMap(minlevel, maxlevel):
    if (minlevel >= maxlevel):
        return []
    else:
        index = np.array(list(range(256)))
        screenNum = np.where(index<minlevel,0,index)
        screenNum = np.where(screenNum> maxlevel,255,screenNum)
        for i in range(len(screenNum)):
            if screenNum[i]> 0 and screenNum[i] < 255:
                screenNum[i] = (i - minlevel) / (maxlevel - minlevel) * 255
        return screenNum

def CreateNewImg(img):
    h, w, d = img.shape
    newimg = np.zeros([h, w, d])
    for i in range(d):
        imghist = np.bincount(img[:, :, i].reshape(1, -1)[0])
        minlevel = ComputeMinLevel(imghist,  h * w)
        maxlevel = ComputeMaxLevel(imghist, h * w)
        screenNum = LinearMap(minlevel, maxlevel)
        if (screenNum.size == 0):
            continue
        for j in range(h):
            newimg[j, :, i] = screenNum[img[j, :, i]]
    return newimg

img = cv2.imread('data/building.png')
newimg = CreateNewImg(img)
cv2.imshow('原始圖像', img)
cv2.imshow('去霧后圖像', newimg / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("sharpening")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #顯示中文標簽
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 圖像銳化函數
def my_not_sharpen(image, k, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    # 注意不能直接用減法，對于圖像格式結果為負時會自動加上256
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    # 兩個矩陣中有一個不是圖像格式，則結果就不會轉換為圖像格式
    sharpen_image = image + k * model   
    sharpen_image = cv2.convertScaleAbs(sharpen_image)
    return sharpen_image

# 提取圖像邊界信息函數
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv2.convertScaleAbs(model)
    return model

original_image_lena = cv2.imread('data/lena.png', 0)

# 獲得圖像邊界信息
edge_image_lena = my_get_model(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_not_sharpen(original_image_lena, 3)

# 顯示結果
plt.subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('邊緣檢測')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('非銳化')
plt.imshow(sharpen_image_lena)
plt.show()

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個

print('open-close')

import cv2
import numpy as np

original_img = cv2.imread('data/flower.png',0)
gray_res = cv2.resize(original_img,None,fx=0.8,fy=0.8,
                 interpolation = cv2.INTER_CUBIC)#圖形太大了縮小一點
# B, G, img = cv2.split(res)
# _,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY) #設定紅色通道閾值160（閾值影響開閉運算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))   #定義矩形結構元素
#閉運算1
closed1 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=1) 
#閉運算2   
closed2 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=3)  
#開運算1  
opened1 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=1)  
#開運算2   
opened2 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=3)   
#梯度  
gradient = cv2.morphologyEx(gray_res, cv2.MORPH_GRADIENT, kernel)      

#顯示如下腐蝕后的圖像
cv2.imshow("gray_res", gray_res)
cv2.imshow("Close1",closed1)
cv2.imshow("Close2",closed2)
cv2.imshow("Open1", opened1)
cv2.imshow("Open2", opened2)
cv2.imshow("gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()




print('------------------------------------------------------------')	#60個

print('morphology 形態學')


import cv2

original_img0 = cv2.imread('data/lena.png')
original_img = cv2.imread('data/lena.png',0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))                  #定義矩形結構元素
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)     #頂帽運算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel) #黒帽運算

#顯示圖像
cv2.imshow("original_img0", original_img0)
cv2.imshow("original_img", original_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('erode-dilate')

import cv2
import numpy as np

original_img = cv2.imread('data/flower.png')
res = cv2.resize(original_img,None,fx=0.6, fy=0.6,
                 interpolation = cv2.INTER_CUBIC) #圖形太大了縮小一點
B, G, R = cv2.split(res)                    #獲取紅色通道
img = R
_,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
#OpenCV定義的結構矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
eroded = cv2.erode(RedThresh,kernel)        #腐蝕圖像
dilated = cv2.dilate(RedThresh,kernel)      #膨脹圖像

cv2.imshow("original_img", res)             #原圖像
cv2.imshow("R_channel_img", img)            #紅色通道圖
cv2.imshow("RedThresh", RedThresh)          #紅色閾值圖像
cv2.imshow("Eroded Image",eroded)           #顯示腐蝕后的圖像
cv2.imshow("Dilated Image",dilated)         #顯示膨脹后的圖像

#NumPy定義的結構元素
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(RedThresh,NpKernel)       #腐蝕圖像

cv2.imshow("Eroded by NumPy kernel",Nperoded)  #顯示腐蝕后的圖像
cv2.waitKey(0)
cv2.destroyAllWindows()



print('------------------------------------------------------------')	#60個

print('Canny')


import cv2
import numpy 

image = cv2.imread("data/jianzhu.png",cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilate_img = cv2.dilate(image, kernel)
erode_img = cv2.erode(image, kernel) 
"""
將兩幅圖像相減獲得邊；cv2.absdiff參數：(膨脹后的圖像，腐蝕后的圖像)
上面得到的結果是灰度圖，將其二值化以便觀察結果
反色，對二值圖每個像素取反
"""
absdiff_img = cv2.absdiff(dilate_img,erode_img);
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY); 
result = cv2.bitwise_not(threshold_img); 
cv2.imshow("jianzhu",image)
cv2.imshow("dilate_img",dilate_img)
cv2.imshow("erode_img",erode_img)
cv2.imshow("absdiff_img",absdiff_img)
cv2.imshow("threshold_img",threshold_img)
cv2.imshow("result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('bitwise')

import cv2

original_img = cv2.imread('data/lena.png',0)
gray_img = cv2.resize(original_img,None,fx=0.8, fy=0.8,
                 interpolation = cv2.INTER_CUBIC) #圖形太大了縮小一點

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))              #定義矩形結構元素(核大小為3效果好)
TOPHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_TOPHAT, kernel)     #頂帽運算
BLACKHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, kernel) #黒帽運算

bitwiseXor_gray = cv2.bitwise_xor(gray_img,TOPHAT_img)

#顯示如下腐蝕后的圖像
cv2.imshow("gray_img", gray_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)
cv2.imshow("bitwiseXor_gray",bitwiseXor_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('absdiff')

import cv2 

image = cv2.imread("data/jianzhu.png",0)
original_image = image.copy()
#構造5×5的結構元素，分別為十字形、菱形、方形和X型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
diamond = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))  #構造方形結構元素
x = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))     

dilate_cross_img = cv2.dilate(image,cross)                #使用cross膨脹圖像
erode_diamond_img = cv2.erode(dilate_cross_img, diamond)  #使用菱形腐蝕圖像

dilate_x_img = cv2.dilate(image, x)                       #使用X膨脹原圖像 
erode_square_img = cv2.erode(dilate_x_img,square)         #使用方形腐蝕圖像 

result = cv2.absdiff(erode_square_img, erode_diamond_img)          #將兩幅閉運算的圖像相減獲得角
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY) #使用閾值獲得二值圖

#在原圖上用半徑為5的圓圈將點標出。
for j in range(result.size):
    y = int(j / result.shape[0])
    x = int(j % result.shape[0])
    if result[x, y] == 255:                                        #result[] 只能傳入整型
        cv2.circle(image,(y,x),5,(255,0,0))

cv2.imshow("original_image", original_image)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

