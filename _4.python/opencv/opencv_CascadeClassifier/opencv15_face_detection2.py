# OpenCV 人臉辨識

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("框出照片中的人臉")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/SolvayConference1927.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg'

# OpenCV 人臉識別分類器
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default333.xml"
# face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

# 讀取待檢測的圖像
image = cv2.imread(filename)
# 獲取xml文件,加載人臉檢測器
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
# 色彩轉換，轉換為灰度圖像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 調用函數detectMultiScale
faces = face_cascade_classifier.detectMultiScale(
    gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5)
)
print(faces)
# 打印輸出測試結果
print("發現{0}個人臉!".format(len(faces)))
# 逐個標記人臉
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)  # 矩形標注
    # cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)

# 顯示結果
cv2.imshow("dect", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
