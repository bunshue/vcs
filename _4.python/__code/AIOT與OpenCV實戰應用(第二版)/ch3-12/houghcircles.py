import cv2
import numpy as np

src = cv2.imread('cup.jpg', -1)
src = cv2.resize(src, (403, 302))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
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

circles = circles.astype(int)
if len(circles) > 0:
    out = src.copy()
    for x, y, r in circles[0]:
        # 畫圓
        cv2.circle(out, (x, y), r, (0,0,255), 3)
        # 畫圓心
        cv2.circle(out, (x, y), 2, (0,255,0), 3)
    src = cv2.hconcat([src, out])

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', src)

cv2.waitKey(0)
cv2.destroyAllWindows()

