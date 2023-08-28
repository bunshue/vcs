import numpy as np
import cv2 

lane = cv2.imread("lane.jpg")
# 高斯模糊，Canny边缘检测需要的
lane = cv2.GaussianBlur(lane, (5, 5), 0)
# 进行边缘检测，减少图像空间中需要检测的点数量
lane = cv2.Canny(lane, 50, 150)
cv2.imshow("lane", lane)
cv2.waitKey()

rho = 1  # 距离分辨率
theta = np.pi / 180  # 角度分辨率
threshold = 10  # 霍夫空间中多少个曲线相交才算作正式交点
min_line_len = 10  # 最少多少个像素点才构成一条直线
max_line_gap = 50  # 线段之间的最大间隔像素
lines = cv2.HoughLinesP(lane, rho, theta, threshold, maxLineGap=max_line_gap)
line_img = np.zeros_like(lane)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_img, (x1, y1), (x2, y2), 255, 1)
cv2.imshow("line_img", line_img)
cv2.waitKey()
