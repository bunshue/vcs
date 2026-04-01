"""
找網球


"""
print("------------------------------------------------------------")  # 60個

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# image = cv2.imread('tennis1.png')


"""
# 找輪廓

import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('tennis1.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定義網球的顏色範圍 (亮黃綠色)
lower_yellow = np.array([25, 80, 80])
upper_yellow = np.array([45, 255, 255])

# 建立遮罩
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 找出輪廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 在原圖上標記輪廓
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:  # 過濾太小的雜訊
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, 'Tennis Ball', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 顯示結果
cv2.imshow('Detected Tennis Ball', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 霍夫圓變換 (Hough Circle Transform)

circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 50,
                           param1=100, param2=30, minRadius=10, maxRadius=100)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np

# Python 即時攝影機版網球偵測程式


# 開啟攝影機（0 表示預設攝影機）
cap = cv2.VideoCapture(0)

# 定義網球的顏色範圍 (亮黃綠色)
lower_yellow = np.array([25, 80, 80])
upper_yellow = np.array([45, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 轉換成 HSV 色彩空間
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 建立遮罩
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 找出輪廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 在畫面上標記輪廓
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # 過濾太小的雜訊
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Tennis Ball', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # 顯示結果
    cv2.imshow('Tennis Ball Detection', frame)

    # 按下 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機與視窗
cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 結合顏色篩選 + 霍夫圓偵測 (HoughCircles) 


import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('tennis1.png')
output = image.copy()

# 轉換成 HSV 色彩空間
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定義網球顏色範圍 (亮黃綠色)
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([60, 255, 255])

# 建立遮罩
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 模糊處理，減少雜訊
mask_blur = cv2.GaussianBlur(mask, (9, 9), 2)

# 使用霍夫圓偵測
circles = cv2.HoughCircles(mask_blur, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                           param1=100, param2=30, minRadius=10, maxRadius=100)

# 如果找到圓形，畫出來
if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(output, (x, y), r, (0, 0, 255), 2)   # 畫圓
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 255, 0), -1) # 標記中心
        cv2.putText(output, 'Tennis Ball', (x - 20, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 顯示結果
cv2.imshow('Detected Tennis Ball', output)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""

# image = cv2.imread('tennis1.png')

import torch
from yolov5 import YOLO

sys.exit()

# 載入模型 (預訓練或你自己訓練的)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 偵測圖片
results = model('grass_tennis_ball.jpg')

# 顯示結果
results.show()



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""

嘗試更寬的 HSV 範圍，例如：
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([60, 255, 255])


- 先做模糊與形態學處理  這樣可以去掉雜訊，讓球的輪廓更清晰。

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask = cv2.GaussianBlur(mask, (5, 5), 0)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

- 改用霍夫圓偵測 (HoughCircles)
網球是圓形，用圓形偵測比輪廓更穩定：

circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 50,
                           param1=100, param2=20, minRadius=10, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(image, (x, y), r, (0, 0, 255), 2)
        cv2.putText(image, 'Tennis Ball', (x-20, y-20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


"""      

