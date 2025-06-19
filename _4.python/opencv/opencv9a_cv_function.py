"""
cv2之各種影像處理功能

色彩空間轉換
圖像金字塔

"""

from opencv_common import *

W, H = 640, 480

print("------------------------------------------------------------")  # 60個
# Color Space Conversions ST
print("------------------------------------------------------------")  # 60個

"""
Color Space Conversions

RGB、灰階、HLS、HSV 轉換

會用到的轉換

BGR轉RGB

BGR轉GRAY
BGR轉BGRA
BGR轉HSV
HSV轉BGR
BGR轉Lab
"""

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

print("圖片色彩空間的轉換")

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(image1)
plt.title("未轉換 BGR")

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.subplot(232)
plt.imshow(image2)
plt.title("BGR轉RGB")

image3 = cv2.cvtColor(image1, cv2.COLOR_BGR2Lab)

plt.subplot(233)
plt.imshow(image3)
plt.title("BGR轉LAB")

plt.subplot(234)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("BGR轉LAB再轉RGB")

show()

print("------------------------------------------------------------")  # 60個
# Color Space Conversions SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# color space 色彩空間轉換 ST
print("------------------------------------------------------------")  # 60個

"""
color space 色彩空間轉換
cv2.split
cv2.merge
"""

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

img = cv2.imread(filename1)  # BGR讀取
cv2.imshow("BGR Color Space", img)

print("BGR 轉 RGB")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RGB
cv2.imshow("RGB Color Space", img_rgb)

print("RGB 轉 BGR")
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)  # RGB 轉 BGR
cv2.imshow("BGR Color Space", img_bgr)

print("BGR 轉 GRAY")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

pt_x = 169
pt_y = 118
img = cv2.imread(filename1)  # BGR讀取

print("BGR 轉 GRAY")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", img_gray)
px = img_gray[pt_x, pt_y]
print(f"Gray Color 通道值 = {px}")

print("GRAY 轉 BGR")
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR Color Space", img_gray)
px = img_color[pt_x, pt_y]
print(f"BGR Color  通道值 = {px}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # BGR讀取
cv2.imshow("BGR Color Space", img)

print("BGR 轉 HSV")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(filename)
cv2.imshow("bgr", image)

blue, green, red = cv2.split(image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

print(f"B通道影像屬性 shape = {blue.shape}")
print("列印B通道內容")
print(blue)

print(f"BGR  影像 : {image.shape}")
print(f"B通道影像 : {blue.shape}")
print(f"G通道影像 : {green.shape}")
print(f"R通道影像 : {red.shape}")

print("B通道內容 : ")
print(blue)
print("G通道內容 : ")
print(green)
print("R通道內容 : ")
print(red)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)
cv2.imshow("bgr", image)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_image)
cv2.imshow("hsv", hue)
cv2.imshow("saturation", saturation)
cv2.imshow("value", value)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)
blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)
hsv_image = cv2.merge([hue, saturation, value])  # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv[:, :] = 200  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv.fill(200)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
saturation.fill(255)  # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
value.fill(255)  # 修訂 value 內容
hsv_image = cv2.merge([hsv, saturation, value])  # 依據H S V順序合併

print("HSV 轉 BGR")
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = cv2.imread(filename)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# 原圖(BGR) 轉HSV 再轉 BGR, 再轉RGB顯示
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

plt.subplot(132)
plt.imshow(cv2.cvtColor(hsv_bgr, cv2.COLOR_BGR2RGB))
plt.title("原圖轉HSV")

h, s, v = cv2.split(hsv)
v[:, :] = 255
newHSV = cv2.merge([h, s, v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

plt.subplot(133)
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))
plt.title("修改V值")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)
cv2.imshow("The Image", image)  # 顯示BGR影像

print("BGR 轉 BGRA")
bgra_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

b, g, r, a = cv2.split(bgra_image)
print("列出轉成含A通道影像物件後的alpha值")
print(a)

a[:, :] = 32  # 修訂alpha內容
a32_image = cv2.merge([b, g, r, a])  # alpha=32影像物件
cv2.imshow("The a32 Image", a32_image)  # 顯示alpha=32影像

a.fill(128)  # 修訂alpha內容
a128_image = cv2.merge([b, g, r, a])  # alpha=128影像物件
cv2.imshow("The a128 Image", a128_image)  # 顯示alpha=128影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
# 檔案 => cv2影像
image = cv2.imread(filename)

bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

plt.figure(
    num="new36 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("bgra")
plt.imshow(cv2.cvtColor(bgra, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("bgra125")
plt.imshow(cv2.cvtColor(bgra125, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("bgra0")
plt.imshow(cv2.cvtColor(bgra0, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
# color space 色彩空間轉換 SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("cv2.goodFeaturesToTrack 角點偵測")

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"

image = cv2.imread(filename)
image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print(len(corners))

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 10, RED, 2)

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
            cv2.circle(image, (int(int(x) + 200), int(y)), 10, YELLOW)
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
            RED,
            7,
            lineType=cv2.LINE_AA,
        )

        # 畫出來, 另法, 用drawContours
        points = np.int0(points)  # 取整數
        cv2.drawContours(image, [points], 0, GREEN, 3)


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
    cv2.circle(I, (points[i, 0], points[i, 1]), 6, RED, -1)

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
        GREEN,
        2,
    )

# 首尾相接
cv2.line(
    I,
    (convexhull[k - 1, 0, 0], convexhull[k - 1, 0, 1]),
    (convexhull[0, 0, 0], convexhull[0, 0, 1]),
    BLUE,
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
draw_points(points, RED)

print("包覆三角形")
# 最小外包直立矩形
area, triangle = cv2.minEnclosingTriangle(points)
print("面積 :", area)
print("包覆所有點的三角形之頂點座標 :", triangle)
print(type(triangle))
print(triangle.dtype)
draw_lines(triangle, GREEN)

print("包覆矩形")
rectangle = cv2.boundingRect(points)
print(rectangle)
x_st = rectangle[0]
y_st = rectangle[1]
w = rectangle[2]
h = rectangle[3]
x_sp, y_sp = x_st + w, y_st + h
cv2.rectangle(image, (x_st, y_st), (x_sp, y_sp), BLUE, 3)

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

draw_points(points, RED)

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

draw_points(contour, RED)

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

draw_points(contour, RED)

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

print("vconcat / hconcat")

image = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)
cv2.imshow("image1", image)

image_h = cv2.hconcat([image, image, image])
image_v = cv2.vconcat([image, image, image])

cv2.imshow("image_h", image_h)
cv2.imshow("image_v", image_v)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# 圖像金字塔 ST
print("------------------------------------------------------------")  # 60個

"""
圖像金字塔
影像金字塔

pyrDown 这里的down是指图像变小，所以原始图像在金字塔的底部。
pyrUp   这里的up是指将图像的尺寸变大，所以原始图像位于图像金字塔的顶层。
"""

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("顯示原圖")
cv2.imshow("original", o)

print("------------------------------------------------------------")  # 60個

# 连续3次进行pyrDown

print("cv2.__version__:", cv2.__version__)

img = cv2.imread(filename)
img_down = cv2.pyrDown(img, dstsize=(img.shape[1] // 2, img.shape[0] // 2))
img_down2 = cv2.pyrDown(
    img_down, dstsize=(img_down.shape[1] // 2, img_down.shape[0] // 2)
)
img_down3 = cv2.pyrDown(
    img_down2, dstsize=(img_down2.shape[1] // 2, img_down2.shape[0] // 2)
)
print("img.shape", img.shape)
print("img_down.shape", img_down.shape)
print("img_down2.shape", img_down2.shape)
print("img_down3.shape", img_down3.shape)
cv2.imshow("img", img)
cv2.imshow("img_down", img_down)
cv2.imshow("img_down2", img_down2)
cv2.imshow("img_down3", img_down3)

cv2.waitKey()
cv2.destroyAllWindows()

print("cv2.__version__:", cv2.__version__)

img = cv2.imread(filename)
img = cv2.resize(img, None, fx=0.15, fy=0.15)  # 为了观察方便缩小原图
img_up = cv2.pyrUp(img, dstsize=(2 * img.shape[1], 2 * img.shape[0]))
img_up2 = cv2.pyrUp(img_up, dstsize=(2 * img_up.shape[1], 2 * img_up.shape[0]))
img_up3 = cv2.pyrUp(img_up2, dstsize=(2 * img_up2.shape[1], 2 * img_up2.shape[0]))
print("img.shape", img.shape)
print("img_up.shape", img_up.shape)
print("img_up2.shape", img_up2.shape)
print("img_up3.shape", img_up3.shape)
cv2.imshow("img", img)
cv2.imshow("img_up", img_up)
cv2.imshow("img_up2", img_up2)
cv2.imshow("img_up3", img_up3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("顯示原圖")
cv2.imshow("original", o)

print("------------------------------------------------------------")  # 60個

print("顯示xxxx")
r1 = cv2.pyrDown(o)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_small.bmp"

o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
r1 = cv2.pyrUp(o)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up - o  # 構造diff圖像，查看up與o的區別
print("o.shape=", o.shape)
print("up.shape=", up.shape)
cv2.imshow("up", up)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down - o  # 構造diff圖像，查看down與o的區別
print("o.shape=", o.shape)
print("down.shape=", down.shape)
cv2.imshow("down", down)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
G0 = O
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)
print("L0.shape=", L0.shape)
print("L1.shape=", L1.shape)
print("L2.shape=", L2.shape)
cv2.imshow("L0", L0)
cv2.imshow("L1", L1)
cv2.imshow("L2", L2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
G0 = O
G1 = cv2.pyrDown(G0)
L0 = O - cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)  # 通過拉普拉斯圖像復原的原始圖像
print("O.shape=", O.shape)
print("RO.shape=", RO.shape)
result = RO - O  # 將o和ro做減法
# 計算result的絕對值，避免求和時負負為正3+(-3)=0
result = abs(result)
# 計算result所有元素的和
print("原始圖像O與恢復圖像RO差值的絕對值和：", np.sum(result))

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
# =================生成高斯金字塔======================
G0 = O
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
# ===============生成拉普拉斯金字塔====================
L0 = G0 - cv2.pyrUp(G1)  # 拉普拉斯金字塔第0層
L1 = G1 - cv2.pyrUp(G2)  # 拉普拉斯金字塔第1層
L2 = G2 - cv2.pyrUp(G3)  # 拉普拉斯金字塔第2層
# =================復原G0======================
RG0 = L0 + cv2.pyrUp(G1)  # 通過拉普拉斯圖像復原的原始圖像G0
print("G0.shape=", G0.shape)
print("RG0.shape=", RG0.shape)
result = RG0 - G0  # 將RG0和G0做減法
# 計算result的絕對值，避免求和時負負為正3+(-3)=0
result = abs(result)
# 計算result所有元素的和
print("原始圖像G0與恢復圖像RG0差值的絕對值和：", np.sum(result))
# =================復原G1======================
RG1 = L1 + cv2.pyrUp(G2)  # 通過拉普拉斯圖像復原G1
print("G1.shape=", G1.shape)
print("RG1.shape=", RG1.shape)
result = RG1 - G1  # 將o和ro做減法
print("原始圖像G1與恢復圖像RG1差值的絕對值和：", np.sum(abs(result)))
# =================復原G2======================
RG2 = L2 + cv2.pyrUp(G3)  # 通過拉普拉斯圖像復原G2
print("G2.shape=", G2.shape)
print("RG2.shape=", RG2.shape)
result = RG2 - G2  # 將o和ro做減法
print("原始圖像G2與恢復圖像RG2差值的絕對值和：", np.sum(abs(result)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/macau.jpg")
cv2.imshow("src", src)

dst1 = cv2.pyrDown(src)  # 第 1 次向下採樣
dst2 = cv2.pyrDown(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrDown(dst2)  # 第 3 次向下採樣
print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/macau_small.jpg")

dst1 = cv2.pyrUp(src)  # 第 1 次向下採樣
dst2 = cv2.pyrUp(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrUp(dst2)  # 第 3 次向下採樣

print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")
cv2.imshow("drc", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src1 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
src2 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
dst = src1 + src2
print(f"src1 = \n{src1}")
print(f"src2 = \n{src2}")
print(f"dst = \n{dst}")

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減

cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_down = cv2.pyrDown(src)  # 向下採樣
print(f"向下採樣大小 = \n{dst_down.shape}")
dst_up = cv2.pyrUp(dst_down)  # 向上採樣, 復原大小
print(f"向上採樣大小 = \n{dst_up.shape}")
dst = dst_up - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_up)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_up = cv2.pyrUp(src)  # 向上採樣
print(f"向上採樣大小 = \n{dst_up.shape}")
dst_down = cv2.pyrDown(dst_up)  # 向下採樣, 復原大小
print(f"向下採樣大小 = \n{dst_down.shape}")
dst = dst_down - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_down)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
G2 = cv2.pyrDown(G1)  # 第 2 次向下採樣

L0 = G0 - cv2.pyrUp(G1)  # 建立第 0 層拉普拉斯金字塔
L1 = G1 - cv2.pyrUp(G2)  # 建立第 1 層拉普拉斯金字塔
print(f"L0.shape = \n{L0.shape}")  # 列印第 0 層拉普拉斯金字塔大小
print(f"L1.shape = \n{L1.shape}")  # 列印第 1 層拉普拉斯金字塔大小
cv2.imshow("Laplacian L0", L0)  # 顯示第 0 層拉普拉斯金字塔
cv2.imshow("Laplacian L1", L1)  # 顯示第 1 層拉普拉斯金字塔

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("Src", src)

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
L0 = src - cv2.pyrUp(G1)  # 拉普拉斯影像
dst = L0 + cv2.pyrUp(G1)  # 恢復結果影像

print(f"src.shape = \n{src.shape}")  # 列印原始影像大小
print(f"dst.shape = \n{dst.shape}")  # 列印恢復影像大小
cv2.imshow("Dst", dst)  # 顯示恢復影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用二元視覺圖形計算深度訊息

img_left = cv2.pyrDown(cv2.imread("data/aloeL.jpg"))
img_right = cv2.pyrDown(cv2.imread("data/aloeR.jpg"))

img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB)
img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB)

stereo_parameters = dict(
    SADWindowSize=5,
    numDisparities=192,
    preFilterCap=4,
    minDisparity=-24,
    uniquenessRatio=1,
    speckleWindowSize=150,
    speckleRange=2,
    disp12MaxDiff=10,
    fullDP=False,
    P1=600,
    P2=2400,
)

stereo = cv2.StereoSGBM(**stereo_parameters)
# NG disparity = stereo.compute(img_left, img_right).astype(np.float32) / 16

# 用remap重疊左右兩幅圖形
h, w = img_left.shape[:2]
ygrid, xgrid = np.mgrid[:h, :w]
ygrid = ygrid.astype(np.float32)
xgrid = xgrid.astype(np.float32)
# NG res = cv2.remap(img_right, xgrid - disparity, ygrid, cv2.INTER_LINEAR)

fig, axes = plt.subplots(1, 3, figsize=(9, 3))
axes[0].imshow(img_left)
axes[0].imshow(img_right, alpha=0.5)
# axes[1].imshow(disparity, cmap="gray")
axes[2].imshow(img_left)
# axes[2].imshow(res, alpha=0.5)
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 圖像金字塔 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
