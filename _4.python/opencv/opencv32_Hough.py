"""
霍夫變換

cv2.HoughLines
cv2.HoughLinesP
cv2.HoughCircles

"""
from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星
filename = "data/_Hough/computer.jpg"

img = cv2.imread(filename)  # 彩色讀取

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
orgb = img
oShow = orgb.copy()

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 140)
print("共找到 :", len(lines), "條直線")

for line in lines:
    # print(line)
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(orgb, (x1, y1), (x2, y2), RED, 2)

plt.subplot(121)
plt.imshow(cv2.cvtColor(oShow, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(orgb, cv2.COLOR_BGR2RGB))
plt.title("尋找霍夫直線")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直線檢測
filename = "data/_Hough/japanese_schedule.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 100, 200)

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 220)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

# 繪製直線 在 src 上
index = 0
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), GREEN, 2)  # 繪製綠色線條
    # cv2.line(src, (x1, y1), (x2, y2), colors[index%6], 2)  # 繪製綠色線條
    index += 1

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("邊緣檢測")

plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/_Hough/lane2.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 100, 200)
cv2.imshow("edges", edges)

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("邊緣檢測")

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
print("共找到 :", len(lines), "條直線")

# 繪製直線, 畫在src上
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), RED, 2)  # 繪製紅色線條

cv2.imshow("dst", src)

plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星
filename = "data/_Hough/computer.jpg"

img = cv2.imread(filename, -1)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
orgb = img
oShow = orgb.copy()

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=100, maxLineGap=10)
print("共找到 :", len(lines), "條直線")

for line in lines:
    # print(line)
    x1, y1, x2, y2 = line[0]
    cv2.line(orgb, (x1, y1), (x2, y2), RED, 2)

plt.subplot(121)
plt.imshow(cv2.cvtColor(oShow, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(orgb, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 無人駕駛車道檢測

src = cv2.imread("data/_Hough/roadtest.jpg", cv2.IMREAD_COLOR)

cv2.imshow("src", src)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 50, 200)

cv2.imshow("Canny", edges)

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("Canny")

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
print("共找到 :", len(lines), "條直線")

# 繪製檢測到的直線, 畫在src上
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), BLUE, 3)  # 繪製藍色線條
cv2.imshow("dst", src)

plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/_Hough/chess.jpg", 0)
imgo = cv2.imread("data/_Hough/chess.jpg", -1)

# o = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
o = imgo
                 
oshow = o.copy()
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(
    img, cv2.HOUGH_GRADIENT, 1, 300, param1=50, param2=30, minRadius=100, maxRadius=200
)

print('轉成整數')
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0, :]:
    cv2.circle(o, (i[0], i[1]), i[2], RED, 12) # 畫外圓
    cv2.circle(o, (i[0], i[1]), 2, GREEN, 12) # 畫圓心

plt.subplot(121)
plt.imshow(cv2.cvtColor(oshow, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print("這個做很久~~~~~~~")

img = cv2.imread("data/_Hough/chess.jpg", 0)
imgo = cv2.imread("data/_Hough/chess.jpg", -1)

# o = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
o = imgo

oshow = o.copy()
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(
    img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0
)
print('轉成整數')
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0, :]:
    cv2.circle(o, (i[0], i[1]), i[2], BLUE, 12)# 畫外圓  # 注意如果是白色，会显示满屏白色，不仔细分析还会以为程序错了呢
    cv2.circle(o, (i[0], i[1]), 2, BLUE, 12)# 畫圓心

plt.subplot(121)
plt.imshow(cv2.cvtColor(oshow, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/_Hough/jianzhu.png")  # 彩色讀取

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 200)

plt.figure("霍夫變換 HoughLines", figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("灰階")

plt.subplot(223)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("Canny邊緣檢測")

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

lines1 = lines[:, 0, :]  # 提取为为二维
for rho, theta in lines1[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), RED, 1)

plt.subplot(224)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("霍夫變換 HoughLines")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lane1 = cv2.imread("data/_Hough/lane.jpg")  # 彩色讀取

# 高斯模糊，Canny边缘检测需要的
lane2 = cv2.GaussianBlur(lane1, (5, 5), 0)  # 執行高斯模糊化

# Canny邊緣檢測，减少图像空间中需要检测的点数量
lane3 = cv2.Canny(lane2, 50, 150)

plt.figure("霍夫變換 HoughLinesP", figsize=(10, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(lane1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(lane2, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊")

plt.subplot(223)
plt.imshow(cv2.cvtColor(lane3, cv2.COLOR_BGR2RGB))
plt.title("Canny邊緣檢測")

rho = 1  # 距离分辨率
theta = np.pi / 180  # 角度分辨率
threshold = 10  # 霍夫空间中多少个曲线相交才算作正式交点
min_line_len = 10  # 最少多少个像素点才构成一条直线
max_line_gap = 50  # 线段之间的最大间隔像素

lines = cv2.HoughLinesP(lane3, rho, theta, threshold, maxLineGap=max_line_gap)
print("共找到 :", len(lines), "條直線")

lane4 = np.zeros_like(lane3)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(lane4, (x1, y1), (x2, y2), 255, 1)

plt.subplot(224)
plt.imshow(cv2.cvtColor(lane4, cv2.COLOR_BGR2RGB))
plt.title("霍夫變換 HoughLinesP")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img1 = cv2.imread("data/_Hough/4.png", 0)  # 灰階讀取
img2 = cv2.medianBlur(img1, 5)
img3 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

plt.figure("霍夫變換 HoughCircles", figsize=(12, 10))
plt.subplot(221)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("medianBlur")

plt.subplot(223)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("COLOR_GRAY2BGR")

circles = cv2.HoughCircles(
    img2,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=100,
    param2=30,
    minRadius=100,
    maxRadius=200,
)
print("共找到 :", len(circles), "個圓")
print(circles)

print('轉成整數')
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0, :]:
    cv2.circle(img3, (i[0], i[1]), i[2], GREEN, 2)  # 畫外圓
    cv2.circle(img3, (i[0], i[1]), 2, RED, 3)  # 畫圓心

plt.subplot(224)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("霍夫變換 HoughCircles")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 霍夫圓形檢測

filename = "data/_Hough/cup.jpg"

image = cv2.imread(filename, -1)  # 彩色讀取

plt.subplot(211)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

shape = image.shape
h = shape[0]  # 高
w = shape[1]  # 寬
h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

image = cv2.resize(image, (int(w / 10), int(h / 10)))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray = cv2.GaussianBlur(gray, (5, 5), 0)  # 執行高斯模糊化
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,  # 偵測方法目前只支援這個參數
    1,  # 1代表偵測圖與輸入圖大小一致，填1即可
    20,  # 各圓心間的最小距離，設太小容易誤判，太大會將數個圓當成一個
    None,  # 固定填 None
    10,  # canny演算法的高閾值，此值一半為低閾值
    75,  # 超過此閾值才會被當作圓
    3,  # 最小圓半徑
    75,  # 最大圓半徑
)
print("共找到 :", len(circles), "個圓")
print(circles)

"""
if circles == None:
    print('找不到圓形, 離開')
    sys.exit()
"""

circles = circles.astype(int)
print(circles)

if len(circles) > 0:
    out = image.copy()
    for x, y, r in circles[0]:
        print("圓 :", x, y, r)
        cv2.circle(out, (x, y), r, RED, 3)# 畫外圓
        cv2.circle(out, (x, y), 2, GREEN, 3)# 畫圓心
    image = cv2.hconcat([image, out])

plt.subplot(212)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("霍夫圓形檢測")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# add_collection 只能用 ax

# 使用HoughLinesP()檢驗圖形中的直線
img = cv2.imread("data/_Hough/building.jpg", cv2.IMREAD_GRAYSCALE)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('原圖')
show()

# Canny邊緣檢測，减少图像空间中需要检测的点数量
img_binary = cv2.Canny(img, 100, 255)

lines = cv2.HoughLinesP(
    img_binary,
    rho=1,
    theta=np.deg2rad(0.1),
    threshold=96,
    minLineLength=33,
    maxLineGap=4,
)
print("共找到 :", len(lines), "條直線")

fig, ax = plt.subplots(figsize=(6, 6))
plt.imshow(img, cmap="gray")
# plt.imshow(cv2.cvtColor(xxxx, cv2.COLOR_BGR2RGB))

from matplotlib.collections import LineCollection
lc = LineCollection(lines.reshape(-1, 2, 2))
ax.add_collection(lc)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檢驗圓形
# add_collection 只能用 ax

# 使用HoughCircles()檢驗圖形中的圓形
coin_filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
img = cv2.imread(coin_filename, cv2.IMREAD_GRAYSCALE)

img_blur = cv2.GaussianBlur(img, (0, 0), 1.8)
circles = cv2.HoughCircles(
    img_blur,
    cv2.HOUGH_GRADIENT,
    dp=2.0,
    minDist=20.0,
    param1=170,
    param2=44,
    minRadius=16,
    maxRadius=40,
)

x, y, r = circles[0].T

fig, ax = plt.subplots(figsize=(12, 10))
plt.imshow(img, cmap="gray")
# plt.imshow(cv2.cvtColor(xxxx, cv2.COLOR_BGR2RGB))

from matplotlib.collections import EllipseCollection

ec = EllipseCollection(
    widths=2 * r,
    heights=2 * r,
    angles=0,
    units="xy",
    facecolors="none",
    edgecolors="red",
    transOffset=ax.transData,
    offsets=np.c_[x, y],
)
ax.add_collection(ec)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/_Hough/shapes.jpg")

plt.subplot(211)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

src = cv2.medianBlur(src, 5)  # 過濾雜訊

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

circles = cv2.HoughCircles(
    src_gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=50,
    param2=30,
    minRadius=70,
    maxRadius=200,
)

print("共找到 :", len(circles), "個圓")
print(circles)

print('轉成整數')
circles = np.uint(np.around(circles))
print(circles)
print()
print(circles[0])

# 繪製檢測到的直線, 畫在src上
for c in circles[0]:
    print("圓 :", c)
    x, y, r = c
    cv2.circle(src, (x, y), r, GREEN, 3)# 畫外圓
    cv2.circle(src, (x, y), 2, RED, 2)# 畫圓心

plt.subplot(212)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughCircles")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 參數使用
# 尋找霍夫直線
lines = cv2.HoughLines(canny_image, 1, np.pi/180, 180)
canny_image：经过图像边缘处理后的图像
1：像素之间的距离为1
np.pi/180：直线角度范围，2pi/(pi/180) = 360°
180：一条预选直线上的最少像素点个数
注意：
如果距离是1，180个像素即可生成直线，
如果距离是2，至少360个像素才可以生成直线。
"""
"""
霍夫直线的返回参数
cv2.HoughLines 的返回参数 line == [\rho ,\Theta ]，
其中，第一个参数表示图像原点距离直线的长度，第二个参数表示沿着x轴的角度大小。
如下图所示，首先通过 cv.HoughLines 得到 line，
此时已经确定了直线的位置，然后需要确定直线上的两个坐标点来充当 cv.line 的输入参数，
最后，在源图像上通过 cv.line 来绘制直线。
"""

"""
图解cv2.HoughLines的返回参数
        # 延长直线的长度，保证在整幅图像上绘制直线
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))
前面讲到， 霍夫直线值仅仅返回两个参数，并不会直接返回直线上的坐标点，
我们在选取直线坐标点的时候，需要尽量选取图像外部的点（即负数），
这样才会过整幅图像绘制直线。
"""

img = cv2.imread("data/_Hough/FerrisWheel4.png")  # 彩色讀取

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
canny_image = cv2.Canny(img_gray, 200, 200)

plt.subplot(132)
plt.imshow(cv2.cvtColor(canny_image, cv2.COLOR_BGR2RGB))
plt.title("灰階+Canny")

# 尋找霍夫直線
lines = cv2.HoughLines(canny_image, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

# 绘画霍夫直线
if lines is not None:
    for n, line in enumerate(lines):
        # 沿着左上角的原点，作目标直线的垂线得到长度和角度
        rho = line[0][0]
        theta = line[0][1]
        # if np.pi / 3 < theta < np.pi * (3 / 4):
        a = np.cos(theta)
        b = np.sin(theta)
        # 得到目标直线上的点
        x0 = a * rho
        y0 = b * rho

        # 延长直线的长度，保证在整幅图像上绘制直线
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))

        # 连接两点画直线
        cv2.line(img, (x1, y1), (x2, y2), GREEN, 1)


plt.subplot(133)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
    blur = cv2.GaussianBlur(gray, (13, 13), 0)  # 高斯模糊
    canny = cv2.Canny(blur, 50, 150)  # 邊緣偵測
    return canny


def get_roi(img):
    mask = np.zeros_like(img)  # 全黑遮罩
    points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊形座標
    cv2.fillPoly(mask, points, 255)  # 多邊三角形
    roi = cv2.bitwise_and(img, mask)
    return roi

def draw_lines(img, lines):  # 建立自訂函式
    for line in lines:
        points = line.reshape(
            4,
        )  # 降成一維 shape = (4,)
        x1, y1, x2, y2 = points  # 取出直線座標
        cv2.line(img, (x1, y1), (x2, y2), RED, 3)  # 繪製直線
    return img  # 回傳繪製直線後的影像


def get_avglines(lines):
    if lines is None:  # 如果有找到線段
        print("偵測不到直線線段")
        return None
    # -----↓先依斜率分到左組或右組↓
    lefts = []
    rights = []
    for line in lines:
        points = line.reshape(
            4,
        )
        x1, y1, x2, y2 = points
        slope, b = np.polyfit((x1, x2), (y1, y2), 1)  # y = slope*x + b
        # print(f'y = {slope} x + {b}')  #若有需要可將斜率與截距印出
        if slope > 0:  # 斜率 > 0, 右邊的直線函數
            rights.append([slope, b])  # 以 list 存入
        else:  # 斜率 < 0, 左邊的直線函數
            lefts.append([slope, b])  # 以 list 存入

    # -----↓再計算左組與右組的平圴線↓
    if rights and lefts:  # 必須同時有左右兩邊的直線函數
        right_avg = np.average(rights, axis=0)  # 取得右邊的平均直線
        left_avg = np.average(lefts, axis=0)  # 取得左邊的平均直線
        return np.array([right_avg, left_avg])
    else:
        print("無法同時偵測到左右邊緣")
        return None


def get_sublines(img, avglines):
    sublines = []  # 用於儲存線段座標
    for line in avglines:  # 一一取出所有直線函數
        slope, b = line  # y = slope*x + b
        y1 = img.shape[0]  # 影像高度 (即影像的最底部位
        y2 = int(y1 * (3 / 5))  # 取影像高度的 3/5 位置為線段
        x1 = int((y1 - b) / slope)  # x = (y-b/m), 取得線段 x 座標
        x2 = int((y2 - b) / slope)
        sublines.append([x1, y1, x2, y2])  # 座標存入串列中
    return np.array(sublines)  # 將串列轉為陣列回傳


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_road = "C:/_git/vcs/_4.python/opencv/data/_Hough/road.jpg"

img = cv2.imread(filename_road)

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

plt.subplot(121)
plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("顯示邊緣圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("顯示ROI圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_road = "C:/_git/vcs/_4.python/opencv/data/_Hough/road.jpg"

img = cv2.imread(filename_road)

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
print(lines)
if lines is not None:  # 如果有找到線段
    img = draw_lines(img, lines)  # 在原圖繪製線段
else:
    print("偵測不到直線線段")
cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("顯示直線線段圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_road = "C:/_git/vcs/_4.python/opencv/data/_Hough/road.jpg"

img = cv2.imread(filename_road)

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
if avglines is not None:
    lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
    img = draw_lines(img, lines)  # 畫出線段
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("顯示直線圖")
    show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

video_filename = (
    "C:/_git/__大檔與暫存區/GRENZEL 雲創 E3W WiFi 行車記錄器 1080 30fps 日間測試 高速公路 - Mobile01.mp4"
)
video_filename = "C:/_git/__大檔與暫存區/DOD行車記錄器-LS300W 日間高速公路實拍.mp4"
video_filename = "C:/_git/__大檔與暫存區/響尾蛇行車記錄器高解析度1080P - 高速公路白天行駛記錄 -.mp4"
video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/road.mp4"

capture = cv2.VideoCapture(video_filename)  # 建立 VideoCapture 物件

if capture.isOpened():
    while True:
        sucess, img = capture.read()
        if sucess:
            edge = get_edge(img)  # 邊緣偵測
            roi = get_roi(edge)  # 取得 ROI
            lines = cv2.HoughLinesP(
                image=roi,  # Hough 轉換
                rho=3,
                theta=np.pi / 180,
                threshold=30,
                minLineLength=50,
                maxLineGap=40,
            )
            avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
            if avglines is not None:
                lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
                img = draw_lines(img, lines)  # 畫出線段
            cv2.imshow("Frame", img)  # 顯示影像

        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break
else:
    print("開啟攝影機失敗")

print("------------------------------------------------------------")  # 60個
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
