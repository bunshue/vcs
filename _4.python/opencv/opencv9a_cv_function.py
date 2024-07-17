"""

cv2之各種影像處理功能



"""
import sys
import cv2
import numpy as np

W = 640
H = 480

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

white = (255, 255, 255)

print("------------------------------------------------------------")  # 60個

print("cv2.goodFeaturesToTrack 角點偵測")

filename = "C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png"

img = cv2.imread(filename)
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print(len(corners))

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("cv2.goodFeaturesToTrack 角點偵測")


def getkpoints(imag, input1):
    mask1 = np.zeros_like(input1)
    x = 0
    y = 0
    w1, h1 = input1.shape
    input1 = input1[0:w1, 200:h1]
    try:
        w, h = imag.shape
    except:
        return None
    mask1[y : y + h, x : x + w] = 255  # 整张图片像素
    keypoints = []
    kp = cv2.goodFeaturesToTrack(input1, 200, 0.04, 7)
    if kp is not None and len(kp) > 0:
        for x, y in np.float32(kp).reshape(-1, 2):
            keypoints.append((x, y))
    return keypoints


def process(image):
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
    gray = cv2.equalizeHist(gray1)  # 直方圖均衡化處理, 只能處理灰階圖
    #cv2.imshow("frame", gray)
    keypoints = getkpoints(gray, gray1)
    #print(keypoints)
    if keypoints is not None and len(keypoints) > 0:
        for x, y in keypoints:
            cv2.circle(image, (int(int(x) + 200), int(y)), 10, (0, 255, 255))
    return image


#video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"
video_filename = 'D:/內視鏡影片/_ims影片2/180824-1025.mp4'

cap = cv2.VideoCapture(video_filename)
#cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#boxPoints


def draw_boxpoints(points):
    #print(points)  # 打印四個頂點
    for i in range(4):
        # 相鄰的點
        p1 = points[i, :]
        j = (i + 1) % 4
        p2 = points[j, :]
        #print(i, points[i], points[j])

        # 畫出直線
        cv2.line(
            image,
            (int(p1[0]), int(p1[1])),
            (int(p2[0]), int(p2[1])),
            red,
            7,
            lineType=cv2.LINE_AA,
            )
        
        # 畫出來, 另法, 用drawContours
        points = np.int0(points)  # 取整數
        cv2.drawContours(image, [points], 0, green, 3)

# boxPoints返回四個點順序：右下→左下→左上→右上

image = cv2.imread("data/cc.bmp")

imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

contours, hierarchy = cv2.findContours(
    imagegray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
rect = cv2.minAreaRect(contours[0])  # 得到最小外接矩形的（中心(x,y), (寬,高), 旋轉角度）
print(type(rect))
print('rect', rect)
print('中心 :', rect[0])
print('寬高 :', rect[1])
print('旋轉角度 :', rect[2])

cx = rect[0][0]
cy = rect[0][1]
print(cx, cy)
W = rect[1][0]*2
H = rect[1][1]*2
print(W, H)

points = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
print(points)  #

#把矩形的四個頂點標出來
for point in points:
    cv2.circle(image, (int(point[0]), int(point[1])), 10, 255, -1)

draw_boxpoints(points)# 畫出四個頂點連線

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")

cv2.imshow("original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n", rect)
points = cv2.boxPoints(rect)
print("\n轉換后的points：\n", points)

draw_boxpoints(points)# 畫出四個頂點連線

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

W, H = 400, 400

# 根據四個頂點在黑色畫板上畫出該矩形
image = np.zeros((H, W, 3), np.uint8)

cx, cy = 200, 200
w, h = W//2 , H//4

rotating_angle = 0  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)# 畫出四個頂點連線

rotating_angle = 20  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)# 畫出四個頂點連線

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

