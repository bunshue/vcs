import sys
import cv2
import numpy as np

filename = 'cup.jpg'

print('顯示圖片')
image = cv2.imread(filename, -1)

shape = image.shape
h = shape[0]    #高
w = shape[1]    #寬
h, w, d = image.shape   #d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

image = cv2.resize(image, (int(w / 10), int(h / 10)))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)    #執行高斯模糊化
circles = cv2.HoughCircles(
    gray, 
    cv2.HOUGH_GRADIENT, # 偵測方法目前只支援這個參數
    1,      # 1代表偵測圖與輸入圖大小一致，填1即可
    20,     # 各圓心間的最小距離，設太小容易誤判，太大會將數個圓當成一個
    None,   # 固定填 None
    10,     # canny演算法的高閾值，此值一半為低閾值
    75,     # 超過此閾值才會被當作圓
    3,      # 最小圓半徑
    75      # 最大圓半徑
)

print(circles)

'''
if circles == None:
    print('找不到圓形, 離開')
    sys.exit()
'''

circles = circles.astype(int)
print(circles)

if len(circles) > 0:
    out = image.copy()
    for x, y, r in circles[0]:
        # 畫圓
        cv2.circle(out, (x, y), r, (0, 0, 255), 3)
        # 畫圓心
        cv2.circle(out, (x, y), 2, (0, 255, 0), 3)
    image = cv2.hconcat([image, out])

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

