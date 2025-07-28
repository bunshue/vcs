"""
cv2之各種影像處理功能

cv2.split / cv2.merge

color space 色彩空間轉換

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

print("圖片色彩空間的轉換")

image1 = cv2.imread(filename_barbara, cv2.IMREAD_UNCHANGED)

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
cv2.split / cv2.merge
"""

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取 BGR
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
print("------------------------------------------------------------")  # 60個

pt_x = 169
pt_y = 118
img = cv2.imread(filename1)  # 彩色讀取 BGR

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
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取 BGR
cv2.imshow("BGR Color Space", img)

print("BGR 轉 HSV")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 彩色讀取 BGR
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp"

image = cv2.imread(filename)  # 彩色讀取

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 轉換為RGB
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # 轉換為HSV

print("coordinate")
coordinate = rgb[131, 81]  # 輸入要取得顏色的指定座標
print(coordinate)

# print("取得cv影像陣列中的資料")
# print(array([255, 219,  79], dtype=uint8))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# =========測試下OpenCV中藍色的HSV模式值=============

W, H, D = 1, 1, 3
imageBlue = np.zeros([H, W, D], dtype=np.uint8)
imageBlue[0, 0, 0] = 255
Blue = imageBlue
BlueHSV = cv2.cvtColor(Blue, cv2.COLOR_BGR2HSV)
print("Blue = \n", Blue)
print("BlueHSV = \n", BlueHSV)

# =========測試下OpenCV中綠色的HSV模式值=============
W, H, D = 1, 1, 3
imageGreen = np.zeros([H, W, D], dtype=np.uint8)
imageGreen[0, 0, 1] = 255
Green = imageGreen
GreenHSV = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)
print("Green = \n", Green)
print("GreenHSV = \n", GreenHSV)

# =========測試下OpenCV中紅色的HSV模式值=============
W, H, D = 1, 1, 3
imageRed = np.zeros([H, W, D], dtype=np.uint8)
imageRed[0, 0, 2] = 255
Red = imageRed
RedHSV = cv2.cvtColor(Red, cv2.COLOR_BGR2HSV)
print("Red = \n", Red)
print("RedHSV = \n", RedHSV)

plt.figure("BGR轉HSV", figsize=(12, 6))
plt.subplot(231)
plt.imshow(cv2.cvtColor(Red, cv2.COLOR_BGR2RGB))
plt.title("Red")

plt.subplot(232)
plt.imshow(cv2.cvtColor(Green, cv2.COLOR_BGR2RGB))
plt.title("Green")

plt.subplot(233)
plt.imshow(cv2.cvtColor(Blue, cv2.COLOR_BGR2RGB))
plt.title("Blue")

plt.subplot(234)
plt.imshow(cv2.cvtColor(RedHSV, cv2.COLOR_BGR2RGB))
plt.title("RedHSV")

plt.subplot(235)
plt.imshow(cv2.cvtColor(GreenHSV, cv2.COLOR_BGR2RGB))
plt.title("GreenHSV")

plt.subplot(236)
plt.imshow(cv2.cvtColor(BlueHSV, cv2.COLOR_BGR2RGB))
plt.title("BlueHSV")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image_bgr = cv2.imread(filename1)  # 彩色讀取

b, g, r = cv2.split(image_bgr)
image_rgb = cv2.merge([r, g, b])

plt.imshow(image_rgb)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 3, 2, 3
image = np.random.randint(0, 256, size=[H, W, D], dtype=np.uint8)
bgra1 = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# print("image = \n", image)
# print("bgra1 = \n", bgra1)

b, g, r, a = cv2.split(bgra1)
# print("a = \n",a)
a[:, :] = 125

bgra2 = cv2.merge([b, g, r, a])
# print("bgra2 = \n", bgra2)

plt.figure("cv2.split & cv2.merge", figsize=(12, 6))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(bgra1, cv2.COLOR_BGR2RGB))
plt.title("bgra1")

plt.subplot(233)
plt.imshow(cv2.cvtColor(bgra2, cv2.COLOR_BGR2RGB))
plt.title("bgra2")

plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R")

plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G")

plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_rgb512 = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(filename_rgb512)  # 彩色讀取 BGR
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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR
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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

blue, green, red = cv2.split(image)
bgr_image = cv2.merge([blue, green, red])  # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])  # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

print("BGR 轉 HSV")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image)
hsv_image = cv2.merge([hue, saturation, value])  # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取 BGR

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

image = cv2.imread(filename2)  # 彩色讀取 BGR

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

image = cv2.imread(filename1)  # 彩色讀取 BGR
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
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_color)  # 彩色讀取 BGR

bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

b, g, r, a = cv2.split(bgra)
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

plt.figure(figsize=(12, 8))

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

image = cv2.imread(filename)  # 彩色讀取

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


print("------------------------------------------------------------")  # 60個
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

image = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)  # 彩色讀取

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

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

cv2.imshow("original", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 连续3次进行pyrDown

print("cv2.__version__:", cv2.__version__)

img = cv2.imread(filename1)  # 彩色讀取

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

img = cv2.imread(filename1)  # 彩色讀取

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

image = cv2.imread(filename_lena_gray, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

cv2.imshow("original", image)

r1 = cv2.pyrDown(image)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
print("image.shape=", image.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)

cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename_lena_small = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_small.bmp"
)

image = cv2.imread(filename_lena_small)  # 彩色讀取

cv2.imshow("original", image)

r1 = cv2.pyrUp(image)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)
print("image.shape=", image.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)

cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_gray)  # 彩色讀取

cv2.imshow("original", image)

down = cv2.pyrDown(image)
up = cv2.pyrUp(down)
diff = up - image  # 構造diff圖像，查看up與o的區別
print("image.shape=", image.shape)
print("up.shape=", up.shape)
cv2.imshow("up", up)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_gray)  # 彩色讀取

cv2.imshow("original", image)

up = cv2.pyrUp(image)
down = cv2.pyrDown(up)
diff = down - image  # 構造diff圖像，查看down與o的區別
print("image.shape=", image.shape)
print("down.shape=", down.shape)
cv2.imshow("down", down)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_gray)  # 彩色讀取

G0 = image
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

image = cv2.imread(filename_lena_gray)  # 彩色讀取

G0 = image
G1 = cv2.pyrDown(G0)
L0 = image - cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)  # 通過拉普拉斯圖像復原的原始圖像
print("image.shape=", image.shape)
print("RO.shape=", RO.shape)
result = RO - image  # 將 image 和 R0 做減法
# 計算result的絕對值，避免求和時負負為正3+(-3)=0
result = abs(result)
# 計算result所有元素的和
print("原始圖像O與恢復圖像RO差值的絕對值和：", np.sum(result))

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_gray)  # 彩色讀取

# =================生成高斯金字塔======================
G0 = image
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
result = RG1 - G1  # 將 image 和 ro 做減法
print("原始圖像G1與恢復圖像RG1差值的絕對值和：", np.sum(abs(result)))
# =================復原G2======================
RG2 = L2 + cv2.pyrUp(G3)  # 通過拉普拉斯圖像復原G2
print("G2.shape=", G2.shape)
print("RG2.shape=", RG2.shape)
result = RG2 - G2  # 將 image 和 ro 做減法
print("原始圖像G2與恢復圖像RG2差值的絕對值和：", np.sum(abs(result)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/macau.jpg")  # 彩色讀取

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

src = cv2.imread("data/pyramid/macau_small.jpg")  # 彩色讀取

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

src = cv2.imread("data/pyramid/pengiun.jpg")  # 彩色讀取

cv2.imshow("src", src)

dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減

cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")  # 彩色讀取

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

src = cv2.imread("data/pyramid/pengiun.jpg")  # 彩色讀取

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

src = cv2.imread("data/pyramid/pengiun.jpg")  # 彩色讀取

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

src = cv2.imread("data/pyramid/pengiun.jpg")  # 彩色讀取

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

img_left = cv2.pyrDown(cv2.imread("data/aloeL.jpg"))  # 彩色讀取
img_right = cv2.pyrDown(cv2.imread("data/aloeR.jpg"))  # 彩色讀取

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
# axes[1].imshow(disparity, cmap="gray")  # 灰階顯示
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

print("opencv 46 測試 cv2.linearPolar 空間變換 極座標變換")

src = cv2.imread(filename1, cv2.IMREAD_ANYCOLOR)  # 彩色讀取

# 圖像的極坐標變換
dst = cv2.linearPolar(src, (508, 503), 550, cv2.INTER_LINEAR)

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("極座標變換")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 47 測試 cv2.logPolar 空間變換 極座標變換")

src = cv2.imread(filename1, cv2.IMREAD_ANYCOLOR)  # 彩色讀取

# 圖像的極坐標變換
M = 150
dst = cv2.logPolar(src, (400 // 2, 300 // 2), M, cv2.WARP_FILL_OUTLIERS)

# 顯示極坐標變化的結果
print(src.shape)
print(dst.shape)

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("極座標變換")

show()

# 看不出什麼東西

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 51 邊緣擴充/擴充邊界 copyMakeBorder")

image0 = cv2.imread(filename1)  # 彩色讀取

# 擴充邊界
top = 50
bottom = 100
left = 150
right = 200
image1 = cv2.copyMakeBorder(image0, top, bottom, left, right, cv2.BORDER_DEFAULT)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("邊緣擴充")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

show()

# 三個影像橫向拼接 np.hstack
image_hstack = np.hstack((image, image, image))

# 二個影像縱向拼接 np.vstack
image_vstack = np.vstack((image_hstack, image_hstack))

plt.imshow(cv2.cvtColor(image_vstack, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 去除圖片的雜訊 fastNlMeansDenoisingColored

image = cv2.imread(filename2)  # 彩色讀取

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# 去除圖片的雜訊 fastNlMeansDenoisingColored
image_denoised = cv2.fastNlMeansDenoisingColored(image, h=5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_denoised, cv2.COLOR_BGR2RGB))
plt.title("Denoise")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("對比度增強 CLAHE")
print("生成自適應均衡化圖像 createCLAHE")

# 自適應直方圖均衡化（Adaptive Histogram Equalization, AHE）
# 限制對比度 自適應直方圖均衡化(Contrast Limited Adaptive Histogram Equalization, CLAHE)

image = cv2.imread("data/building.png", 0)  # 灰階讀取
# image = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 創建 CLAHE  對象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 創建 CLAHE  對象
# clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(28, 28))

# 限制對比度的自適應閾值均衡化
cl1 = clahe.apply(image)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原始圖像")

plt.subplot(122)
plt.imshow(cv2.cvtColor(cl1, cv2.COLOR_BGR2RGB))
plt.title("生成自適應均衡化圖像\ncreateCLAHE")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

output = image  # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(image, output, alpha, beta)  # 套用 convertScaleAbs

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.floodFill() 填充 1")


def floodFill(
    source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE
):
    result = source.copy()
    cv2.floodFill(
        result,
        mask=mask,
        seedPoint=seedPoint,
        newVal=newVal,
        loDiff=loDiff,
        upDiff=upDiff,
        flags=flags,
    )
    return result


image = cv2.imread(filename1)  # 彩色讀取

h, w = image.shape[:2]

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 製作 mask，長寬都要加上 2
image1 = floodFill(image, mask, (100, 10), RED, (100, 100, 60), (100, 100, 100))

image = cv2.imread(filename1)  # 彩色讀取

h, w = image.shape[:2]

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 全黑遮罩
mask = 255 - mask  # 變成全白遮罩
mask[0:100, 0:200] = 0  # 將左上角長方形變成黑色

# 只處理mask區域
image2 = floodFill(image, mask, (100, 10), RED, (100, 100, 60), (200, 200, 200))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("image1")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("image2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.floodFill() 填充 2")

"""
有些特殊的卷积核可以表示成一个列矢量和一个行矢量的乘积，
这时只需要将原始图像按 顺序与这两个矢量进行卷积，
所得到的最终结果和直接与卷积核进行卷积的结果相同。
对于较大的卷积核能大幅度地提高 计算速度。

OpenCV提供了 sepFilter2D()来进行这种分步卷积，调用参数如下：
sepFilter2D(src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]])
比较filter2D()和sepFilter2D() 的计算速度：
"""

img = np.random.rand(1000, 1000)

row = cv2.getGaussianKernel(7, -1)
col = cv2.getGaussianKernel(5, -1)

kernel = np.dot(col[:], row[:].T)

img2 = cv2.filter2D(img, -1, kernel)
img3 = cv2.sepFilter2D(img, -1, row, col)
print("error=", np.max(np.abs(img2[:] - img3[:])))

"""
OpenCV提供了一些高级函数数来直接完成与某种特定卷积核的 卷积计算。

形态学运算
dilate
()对图像进行膨胀处理，而erode
()则对图像进行腐蚀处理。

mpiphologyEx()使用膨胀和收缩实现一些更高级的形态学处理。
这 些函数都可以对多值图像进行操作，对于多通道图像，它们将对每个通道进行相同的运算。

dilate()和erode()的调用参数相同：
dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

膨胀运算可以用下面的公式描述：
将结构元素kernel的锚点与原始图像中的每个像素(x,y)对齐之后，计算所有结构元素值不为0 的像素的最大值，写入目标图像的(x,y)像素点。而腐蚀运算则是计算所有结构元素不为0的像 素的最小值。
morphologyEx()的参数如下：
morphologyEx(src, op, kernel[, dst[, anchoriterationsborderType[, borderValue]]]]])
op参数，用于指定运算的类型。
moiphologyEx()的高级运算包括：
• MORPH_OPEN:开运算，可以用来区分两个靠得很近的区域。算法为先腐蚀再膨胀: dst=dilate(erode(src))
• MORPH_CLOSE:闭运算，可以用来连接两个靠得很近的区域。算法为先膨胀再腐蚀： dst=erode(dilate(src))
• MORPH_GRADIENT:形态梯度，能够找出图像区域的边缘。算法为膨胀减去腐蚀： dst=dilate(src)- erode(src)
• MORPH_TOPHAT:顶帽运算，算法为原始图像减去开运算：dst = src-open(src)。
• MORPH_BLACKHAT:黑帽运算，算法为闭运算减去原始图像：dst=close(src)-src。

    填充-floodFill

填充函数floodFill()在图像处理中经常用于标识或分离图像中的某些特定部分。它的调用方 式为:
floodFill(image, mask, seedPoint, newVal[, loDiff[, upDiff[, flags]]])
seedPoint参数为填充的起始点，为种子点； newVal参数为填充所使用的颜色值；loDiff和upDiff参数是填充的下限和上限容差；flags参数 是填充的算法标志。
填充从seedPoint指定的种子坐标开始，图像中与当前的填充区域颜色相近的点将被添加进 填充区域，从而逐步扩大填充区域，直到没有新的点能添加进填充区域为止。
颜色相近的判断 方法有两种：
    默认使用相邻点为基点进行判断。
•如果开启了 flags中的FL00DFILL_F1XED_RANGE标志位，则以种子点为基点进行判断。
假设图像中某个点(x,y)的颜色为C(x,y), C0为基点颜色，则下面的条件满足时，（x,y)将 被添加进填充区域：
C0 — loDiff < C(x，y) < C0 + hiDiff
此外还可以通过flags指定相邻点的定义：四连通或八连通。
当mask参数不为None时，它是一个宽和高比image都大两个像素的单通道8位图像
。image 图像中的像素(x,y)与mask中的(x + 1,y + 1)对应。填充只针对mask中的值为0的像素进行。 进行填充之后，mask中所有被填充的像素将被赋值为1。如果只希望修改mask,而不对原始图 像进行填充，可以开启flags标志中FLOODFTLL_MASK_ONLY。
#floodFill()的填充效果
"""
# 形態學運算
#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。
# 填充-floodFill
# 示範floodFill()的填充效果
#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。
# 去瑕疵-inpaint
#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。

coin_filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
img = cv2.imread(coin_filename)  # 彩色讀取
print("img.shape :", img.shape)

seed1 = 344, 188
seed2 = 152, 126
diff = (13, 13, 13)
h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(img, mask, seed1, BLACK, diff, diff, cv2.FLOODFILL_MASK_ONLY)
cv2.floodFill(img, None, seed2, RED, diff, diff)
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(~mask, cmap="gray")  # 灰階顯示
axes[1].imshow(img)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(-256, 256, size=[3, 5], dtype=np.int16)
print(f"image = \n {image}")

print("取絕對值")
dst1 = cv2.convertScaleAbs(image)
print(f"dst1 = \n {dst1}")

print("取限制100~200")
dst2 = np.clip(image, 100, 200)
print(f"dst2 = \n {dst2}")

print("------------------------------------------------------------")  # 60個
# cv2.remap() 重映射 ST
# 重映射，即把一幅图像内的像素点放置到另外一幅图像内的指定位置
print("------------------------------------------------------------")  # 60個

image1 = np.random.randint(0, 256, (3, 5), dtype="uint8")

# image1[3, 2]的值 對應到整個陣列
mapx = np.ones(image1.shape, dtype=np.float32) * 3
mapy = np.ones(image1.shape, dtype=np.float32) * 2

image2 = cv2.remap(image1, mapx, mapy, interpolation=cv2.INTER_LINEAR)

print(image1)
print(mapx)
print(mapy)
print(image2)

w, h = 10, 5
mapy, mapx = np.mgrid[0 : h * 3 : 3, 0 : w * 2 : 2]

print(mapx.shape)
print(mapy.shape)
print(mapx)
print(mapy)

# 重映射-remap

w, h = 640, 480

filename4a = "C:/_git/vcs/_4.python/opencv/data/ims_640X480.bmp"

img = cv2.imread(filename4a)  # 彩色讀取
img = cv2.imread(filename4a, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
print(img.shape)

mapy, mapx = np.mgrid[0 : h * 1 : 20, 0 : w * 1 : 20]
print(mapx.shape)
print(mapy.shape)

img2 = cv2.remap(img, mapx.astype("float32"), mapy.astype("float32"), cv2.INTER_LINEAR)

plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

"""
img2 = cv2.remap(
    img,
    (offsetx_blur + gridx).astype("f4"),
    (offsety_blur + gridy).astype("f4"),
    cv2.INTER_LINEAR,
)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 cv2.remap()")
W, H = 5, 4
print("建立 隨機影像 二維灰階/二維深度1")
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # 灰階, 1維隨機影像

H, W = image.shape

map_x = np.zeros(image.shape, np.float32)  # 必須是float
map_y = np.zeros(image.shape, np.float32)  # 必須是float
for i in range(H):
    for j in range(W):
        map_x.itemset((i, j), j)
        map_y.itemset((i, j), i)

map_image = cv2.remap(image, map_x, map_y, cv2.INTER_LINEAR)
print("image = \n", image)
print("map_x = \n", map_x)
print("map_y = \n", map_y)
print("map_image = \n", map_image)
print("map_image.shape = \n", map_image.shape)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
rows, cols = image.shape
mapx = np.ones(image.shape, np.float32) * 3  # 設定 mapx
mapy = np.ones(image.shape, np.float32) * 2  # 設定 mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)

for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            mapx.itemset((r, c), 2 * (c - cols * 0.25))  # 計算對應的 x
            mapy.itemset((r, c), 2 * (r - rows * 0.25))  # 計算對應的 y
        else:
            mapx.itemset((r, c), 0)  # 取x座標為 0
            mapy.itemset((r, c), 0)  # 取y座標為 0
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)
        mapy.itemset((r, c), 2 * r)
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.remap() 重映射 SP
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

# split & merge

# split image into channels
r, g, b = cv2.split(image)

plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
show()

plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
show()

plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
show()

# img_a = cv2.merge((r, g, b, mask.astype('float32') / 255.0))
# plt.imshow(img_a)
# show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
