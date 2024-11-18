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

filename = "C:/_git/vcs/_4.python/opencv/data/dilate_erode1.png"

image = cv2.imread(filename)
image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print(len(corners))

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 10, (0, 0, 255), 2)

cv2.imshow("Frame", image)
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
    # cv2.imshow("frame", gray)
    keypoints = getkpoints(gray, gray1)
    # print(keypoints)
    if keypoints is not None and len(keypoints) > 0:
        for x, y in keypoints:
            cv2.circle(image, (int(int(x) + 200), int(y)), 10, (0, 255, 255))
    return image


"""
video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"
#video_filename = "D:/內視鏡影片/_ims影片2/180824-1025.mp4"

cap = cv2.VideoCapture(video_filename)
# cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

# boxPoints 帶有旋轉的矩形框座標


def draw_boxpoints(points):
    # print(points)  # 打印四個頂點
    for i in range(4):
        # 相鄰的點
        p1 = points[i, :]
        j = (i + 1) % 4
        p2 = points[j, :]
        # print(i, points[i], points[j])

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

print("最小外接矩形 :", rect)
print("中心 :", rect[0])
print("寬高 :", rect[1])
print("旋轉角度 :", rect[2])

cx = rect[0][0]
cy = rect[0][1]

print("中心 :", cx, cy)
W = rect[1][0] * 2
H = rect[1][1] * 2
print("W = ", W, "H = ", H)

points = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
print("最小外接矩形 :", points)

# 把矩形的四個頂點標出來
for point in points:
    cv2.circle(image, (int(point[0]), int(point[1])), 10, 255, 5)

draw_boxpoints(points)  # 畫出四個頂點連線

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

draw_boxpoints(points)  # 畫出四個頂點連線

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

W, H = 400, 400

# 根據四個頂點在黑色畫板上畫出該矩形
image = np.zeros((H, W, 3), np.uint8)

cx, cy = 200, 200
w, h = W // 2, H // 4

rotating_angle = 0  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

rotating_angle = 20  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 convexHull")

W, H = 400, 400
I = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

MIN = 50
MAX = W - 50
N = 50  # 隨機生成 N 個坐標點，每一行存儲一個坐標
# 隨機生成 橫縱坐標均在 MIN 至 MAX 的坐標點
points = np.random.randint(MIN, MAX, (N, 2), np.int32)
print(points)
# 把上述點集處的灰度值設置為 255,單個白色像素點不容易觀察，用一個小圓標注一下
for i in range(N):
    cv2.circle(I, (points[i, 0], points[i, 1]), 6, red, -1)

# 求點集 points 的凸包
convexhull = cv2.convexHull(points, clockwise=False)
# ----- 打印凸包的信息 ----
print(type(convexhull))
print(convexhull.shape)

# 連接凸包的各個點
k = convexhull.shape[0]
for i in range(k - 1):
    cv2.line(
        I,
        (convexhull[i, 0, 0], convexhull[i, 0, 1]),
        (convexhull[i + 1, 0, 0], convexhull[i + 1, 0, 1]),
        green,
        2,
    )

# 首尾相接
cv2.line(
    I,
    (convexhull[k - 1, 0, 0], convexhull[k - 1, 0, 1]),
    (convexhull[0, 0, 0], convexhull[0, 0, 1]),
    blue,
    2,
)

# 顯示圖片
cv2.imshow("I", I)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


def draw_points(points, color):
    N = len(points)
    print("N =", N)
    for point in points:
        cv2.circle(image, (int(point[0]), int(point[1])), 6, color, -1)


def draw_lines(points, color):
    N = len(points)
    print("N =", N)
    # 畫出來, 另法, 用drawContours
    points = np.int0(points)  # 取整數
    cv2.drawContours(image, [points], 0, color, 3)  # 多點頭尾連線


print("包覆三角形 與 包覆矩形")
print("幾何形狀的檢測和擬合 minEnclosingTriangle")
print("用一個三角形把所有點包起來")

W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

points = np.array([[[1, 1]], [[5, 10]], [[5, 1]], [[1, 10]], [[2, 5]]], np.float32)
points = np.array([[1, 1], [5, 10], [5, 1], [1, 10], [2, 5]], np.float32)

points = np.array([[0, 0], [100, 0], [0, 100]], np.float32)
points = np.array([[0, 0], [100, 0], [100, 100], [0, 100]], np.float32)

MIN = 100
MAX = W - 100
N = 30  # 隨機生成 N 個坐標點，每一行存儲一個坐標
# 隨機生成 橫縱坐標均在 MIN 至 MAX 的坐標點
points = np.random.randint(MIN, MAX, (N, 2), np.int32)
# print(points)
draw_points(points, red)

print("包覆三角形")
# 最小外包直立矩形
area, triangle = cv2.minEnclosingTriangle(points)
print("面積 :", area)
print("包覆所有點的三角形之頂點座標 :", triangle)
print(type(triangle))
print(triangle.dtype)
draw_lines(triangle, green)

print("包覆矩形")
rectangle = cv2.boundingRect(points)
print(rectangle)
x_st = rectangle[0]
y_st = rectangle[1]
w = rectangle[2]
h = rectangle[3]
x_sp, y_sp = x_st + w, y_st + h
cv2.rectangle(image, (x_st, y_st), (x_sp, y_sp), blue, 3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 arcLength")


def draw_points(points, color):
    N = len(points)
    print("N =", N)
    for point in points:
        cv2.circle(image, (int(point[0]), int(point[1])), 6, color, -1)


W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

# 點集
# points = np.array([[0,0],[100,0],[0,100]] ,np.float32)
points = np.array([[0, 0], [100, 0], [100, 100], [0, 100]], np.float32)
print(points.shape)

draw_points(points, red)

# 計算點集的所圍區域的周長
length1 = cv2.arcLength(points, False)  # 首尾不相連
length2 = cv2.arcLength(points, True)  # 首尾相連

# 計算點集所圍區域的面積
area = cv2.contourArea(points)

# 打印周長和面積
print("首尾不相連 線長 :", length1)
print("首尾相連 線長 :", length2)
print("面積 :", area)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 convexityDefects")

W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

# 輪廓
contour = np.array(
    [[20, 20], [50, 70], [20, 120], [120, 120], [100, 70], [120, 20]], np.int32
)

draw_points(contour, red)

# 輪廓的凸包
hull = cv2.convexHull(contour, returnPoints=False)
defects = cv2.convexityDefects(contour, hull)

# 打印凸包
print(hull)

# 打印凸包的缺陷
print(defects)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 pointPolygonTest")

W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

# 點集
contour = np.array([[0, 0], [50, 30], [100, 100], [100, 0]], np.float32)

draw_points(contour, red)

# 判斷三個點和點集構成的輪廓的關系
dist1 = cv2.pointPolygonTest(contour, (80, 40), False)
dist2 = cv2.pointPolygonTest(contour, (50, 0), False)
dist3 = cv2.pointPolygonTest(contour, (40, 80), False)
# 打印結果
print(dist1)
print(dist2)
print(dist3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
