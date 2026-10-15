"""

"""

import cv2
from PIL import Image

ESC = 27

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # pass
    plt.show()


def cvshow(title, img):
    # pass
    cv2.imshow(title, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# OpenCV_顏色共同
RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測正面人臉 haarcascade_frontalface_default.xml
xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

# 眼睛模型
eye_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
)

# 左眼模型
lefteye_xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lefteye_2splits.xml"

# 右眼模型
righteye_xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_righteye_2splits.xml"

# 嘴巴模型
mouth_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_mouth.xml"
)

# 鼻子模型
nose_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_nose.xml"
)

# 偵測上半身 haarcascade_upperbody.xml
upperbody_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_upperbody.xml"
)

# 正面的貓臉 haarcascade_frontalcatface.xml
frontalcatface_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalcatface.xml"
)

# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml
russian_plate_xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"

# 偵測側面的人臉 haarcascade_profileface.xml
profileface_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_profileface.xml"
)

# 偵測身形 路人偵測 haarcascade_fullbody.xml
fullbody_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_fullbody.xml"
)

# 下半身
lowerbody_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lowerbody.xml"
)

filename = "D:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/_face/face17.jpg"
# filename = "D:/_git/vcs/_4.python/opencv/data/_face/yalta1945.jpg"
# filename = "D:/_git/vcs/_4.python/opencv/data/_face/solvay1927a.jpg"
# filename = "D:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 共同 建立辨識物件

# 人臉偵測
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件 人臉

# 眼睛
eye_cascade_classifier = cv2.CascadeClassifier(eye_xml_filename)  # 建立辨識物件 眼睛

# 鼻子
nose_cascade_classifier = cv2.CascadeClassifier(nose_xml_filename)  # 建立辨識物件 鼻子

# 嘴巴
mouth_cascade_classifier = cv2.CascadeClassifier(mouth_xml_filename)  # 建立辨識物件 嘴巴

# 左眼
lefteye_cascade_classifier = cv2.CascadeClassifier(lefteye_xml_filename)  # 建立辨識物件 左眼

# 右眼
righteye_cascade_classifier = cv2.CascadeClassifier(righteye_xml_filename)  # 建立辨識物件 右眼

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# [ OpenCV ] 利用 OpenCV抓取相片中的臉部數據


"""
detectMultiScale中的數據參數分別是
圖片數據
ScaleFactor：每次搜尋方塊減少的比例
minNeighbers：每個目標至少檢測到幾次以上，才可被認定是真數據。
minSize：設定數據搜尋的最小尺寸 ，如 minSize=(40,40)
"""

import cv2

# 偵測正面人臉 haarcascade_frontalface_default.xml
xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

# 眼睛模型
eye_xml_filename = (
    "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
)

face_cascade = cv2.CascadeClassifier(xml_filename)
eye_cascade = cv2.CascadeClassifier(eye_xml_filename)
 
def detect(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=3,)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,
                                            scaleFactor=1.02,
                                            minNeighbors=3,
                                            minSize=(40,40),)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        for (ex,ey,ew,eh) in eyes:
            img = cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
    cv2.imwrite('tmp_get_face.jpg', img)


pic_filename = "D:/_git/vcs/_4.python/opencv/data/_face/5132324-PH.jpg"

detect(pic_filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
對臉部和眼睛進行辨識，至少辨識出兩隻眼睛(無論對錯)才進行儲存，輸出為 200x200的 png格式。
沒有設定minSize，因為我的數據有點少解析度落差也很大，所以不想要太嚴格。
'''
face_cascade = cv2.CascadeClassifier(xml_filename)
eye_cascade = cv2.CascadeClassifier(eye_xml_filename)
 
face_filename = 1
def detect(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=3,)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,
                                            scaleFactor=1.02,
                                            minNeighbors=3,)
        if len(eyes)>=2:
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            global face_filename
            name = './tmp_%d.png' % face_filename
            cv2.imwrite(name, f)
            face_filename += 1
        else:
            pass
    print('Working with %s' % filename)


pic_filename = "D:/_git/vcs/_4.python/opencv/data/_face/5132324-PH.jpg"

detect(pic_filename)
    

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
做法可能沒有很聰明，利用 os.walk把該資料夾中的各種格式的圖像名稱儲存成 list，再利用迴圈對圖像一個個辨識。
無論原圖解析度如何，全都會輸出統一的格式。
"""

img_list = []
for fileNames in os.walk("."):
    filename_extension = ['.jpg', '.png', '.jpeg', '.JPG', '.gif']
    for fe in filename_extension:
        for fileName in fileNames[-1]:
            if fileName.endswith(fe):
                img_list.append(fileName)
 
for img in img_list:
    detect(img)

    
print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

