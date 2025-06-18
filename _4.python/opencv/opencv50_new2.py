"""
opencv 集合 新進2

"""

from opencv_common import *

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("------------------------------------------------------------")  # 60個

# 01loadimg.py

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

img = cv2.imread(filename, 0)  # 0 黑白图片；1 原色图片

cv2.imshow(win_name, img)  # 显示图片

cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁创建的对象

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" no file
# 02opencvmatplotlib.py

# 读取图片
img = cv2.imread("tmp_picture1.mono.pgm", 0)  # 黑白图片

plt.imshow(img, cmap="gray", interpolation="bicubic")

plt.xticks([]), plt.yticks([])  # 隐藏 X Y 坐标
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03drawrectangle.py

# Create a black image
img = np.zeros((512, 512, 3))

# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色: BLUE，宽度:2
cv2.line(img, (0, 0), (511, 511), BLUE, 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04drawGeometry.py

img = np.zeros((512, 512, 3))
cv2.rectangle(img, (384, 0), (510, 128), GREEN, 3)  # 矩形
cv2.circle(img, (447, 63), 63, RED, -1)  # 圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)  # 椭圆

# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, YELLOW, 1)

# 写入文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, WHITE, 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05drawcirlcle.py

img = np.zeros((512, 512, 3))

# 绘制圆：圆心(255, 255), 半径60, 颜色 YELLOW, 像素1
cv2.circle(img, (255, 150), 60, YELLOW, 2)  # 圆

# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100
# 360表示整个椭圆；颜色 CYAN；像素2；
cv2.ellipse(img, (255, 350), (100, 50), 0, 0, 360, CYAN, 2)  # 椭圆

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt_tree.xml"
picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
)

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("製作影像")

width, height = 640, 480  # 影像寬, 影像高

# 建立 640 X 480 之黑圖
fig = np.zeros((height, width), dtype=np.uint8)

# 建立 640 X 480 之白圖
fig = np.ones((height, width), dtype=np.uint8) * 255

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

print("某些塗為白色")

for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)

# R
red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值

# G
green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值

# B
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值

# Y
yellow_image = image.copy()
yellow_image[:, :, 2] = 255  # 建立 R 通道像素值
yellow_image[:, :, 1] = 255  # 建立 G 通道像素值

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("製作隨機影像")

# 使用random.randint()建立GRAY影像陣列
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)  # 灰階, 1維
# src = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)  # 彩色, 3維

cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

src = np.random.randint(256, size=(height, width))  # 建立矩陣
# print(f"矩陣內容 = \n{src}")

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# 製作隨機影像
width, height = 64, 48  # 影像寬, 影像高
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個
# OpenCV_05_建立空影像
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.ones((height, width), np.uint8) * 255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩

cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("-------------------- ----------------------------------------")  # 60個
# OpenCV 運算
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

channels = cv2.mean(src)  # 計算影像各通道的均值
print(f"均值   = \n{channels}")

mean, std = cv2.meanStdDev(src)  # 計算影像各通道的標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("Peony")  # 關閉視窗

print("------------------------------------------------------------")  # 60個
"""
# 設定 cv 視窗
cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小

img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
# img2 = cv2.imread(filename1, 0)  # 灰色讀取 same

cv2.imshow("Peony1", img1)
cv2.imshow("Peony2", img2)

cv2.waitKey()
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取某點的灰階/RGB值

pt_y = 169
pt_x = 118

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點

print(type(px))
print(f"BGR = {px}")

img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個

# 修改影像的RGB值

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_06_影像處理
print("------------------------------------------------------------")  # 60個

print("修改圖片的像素值 灰階")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = 127

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階")
plt.axis("off")

print("修改圖片的像素值 彩色")

img = cv2.imread(filename1)  # 彩色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = [255, 0, 0]

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("彩色")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立紅色red底的彩色影像陣列
red_image = np.zeros((height, width, 3), np.uint8)
red_image[:, :, 2] = 255  # 填滿紅色

# 建立綠色green底的彩色影像陣列
green_image = np.zeros((height, width, 3), np.uint8)
green_image[:, :, 1] = 255  # 填滿綠色

# 建立藍色blue底的彩色影像陣列
blue_image = np.zeros((height, width, 3), np.uint8)
blue_image[:, :, 0] = 255  # 填滿藍色

# 建立黃色yellow底的彩色影像陣列
yellow_image = np.zeros((height, width, 3), np.uint8)
yellow_image[:, :, 2] = 255  # 填滿紅色
yellow_image[:, :, 1] = 255  # 填滿綠色

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1] = {blue[0,1]}")

blue[0, 1] = [50, 100, 150]  # 修訂像素點
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue[0,1,2]}")

blue[0, 1, 2] = 50  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue[0,1,2]}")

print("------------------------------------------------------------")  # 60個

# 取出像素值, 修改之

img = cv2.imread(filename1)  # 彩色讀取

print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")

# 紫色長條
img[115:125, 110:210] = [255, 0, 255]

# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代

# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代

cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("修改alpha通道值 255=>127")

# 4通道的PNG圖
filename5 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"

img = cv2.imread(filename5, cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(img.shape)
print(f"修改前img[210,150] = {img[210,150]}")
print(f"修改前img[250,199] = {img[250,199]}")

for z in range(0, img.shape[1]):  # 一次一個修改alpha通道值
    for y in range(0, img.shape[0]):
        img[z, y, 3] = 127  # 修改alpha通道值

img[0:200, 0:200, 3] = 127  # 修改alpha通道值

print(f"修改後img[210,150] = {img[210,150]}")
print(f"修改後img[250,199] = {img[250,199]}")

cv2.imshow("After", img)  # 顯示修改前影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")

image.itemset((1, 3), 255)  # 修訂內容為 255

print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個

print("灰階讀取, 部分塗成灰色")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img

for y in range(30, 100):  # 修改影像
    for x in range(180, 280):
        img.itemset((y, x), 127)
cv2.imshow("After", img)  # 顯示修改後影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

blue.itemset((0, 1, 2), 50)  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {img.item(115,110,1)}")
print(f"修改前img[125,110,1] = {img.item(125,110,1)}")
print(f"修改前img[135,110,1] = {img.item(135,110,1)}")

# 白色長條
for z in range(30, 100):  # 修改影像:一次一個通道值
    for y in range(180, 280):
        for x in range(0, 3):  # 一次一個通道值
            img.itemset((z, y, x), 127)  # 白色取代
cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110,1] = {img.item(115,110,1)}")
print(f"修改後img[125,110,1] = {img.item(125,110,1)}")
print(f"修改後img[135,110,1] = {img.item(135,110,1)}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)

# ROI大小區塊建立馬賽克
w, h = 100, 70
face = np.random.randint(0, 256, size=(h, w, 3))  # 馬賽克效果
img[30 : 30 + h, 180 : 180 + w] = face  # ROI, 先高後寬
cv2.imshow("Face", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

big = cv2.imread(filename2)  # 彩色讀取, 大圖

small = cv2.imread(filename1)  # 彩色讀取, 小圖

roi = small[110:200, 130:220]  # ROI, 先高後寬

big[110:200, 70:160] = roi  # 小圖貼到大圖上

cv2.imshow("Image", big)

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)

plt.subplot(331)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(result[:, :, i], cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
    plt.title(str(i))
    plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# cv2.bitwise_and

src = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)
row, column = src.shape  # 取得列高和欄寬

h100 = np.ones((row, column), dtype=np.uint8) * 100  # 建立像素值是100的影像

new_src = cv2.bitwise_and(src, h100)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(h100, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階100")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(new_src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖取出灰階100")
plt.axis("off")

plt.suptitle("cv2.bitwise_and")
show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
opencv 集合 新進3

"""

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

maxval = 255  # 定義像素最大值, 閾值
width, height = 640, 480  # 影像寬, 影像高

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# Character_recognition.py

img = cv2.imread("data/brain.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)  # 膨胀

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, 1, 5)
ret, sure_fg = cv2.threshold(
    dist_transform, 0.2 * dist_transform.max(), 255, 0
)  # 参数改小了，出现不确定区域

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)  # 减去前景

cv2.imshow("p", sure_fg)

plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(221)
plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(223)
plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(224)
plt.imshow(cv2.cvtColor(sure_fg, cv2.COLOR_BGR2RGB))
plt.title("")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

"""
print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 ST
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)  # 讀取影像

mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (150, 50, 200, 480)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1

# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)

# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

dst = cv2.rectangle(dst, rect, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/tmp1/hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)

""" NG
maskpict = cv2.imread("data/tmp1/hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("data/tmp1/hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/tmp1/lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 全景圖 ST
print("------------------------------------------------------------")  # 60個

"""
filename1 = 'C:/_git/vcs/_4.python/_data/penguin3.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/penguin4.jpg'
output_filename = 'tmp_penguin_all.jpg'
filenames = [filename1, filename2]
"""

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF2.jpg"
filename3 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF3.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF4.jpg"
filename5 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF5.jpg"
filename6 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF6.jpg"
filename7 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF7.jpg"
filename8 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF8.jpg"
output_filename = "tmp_SF_all.jpg"
filenames = [
    filename1,
    filename2,
    filename3,
    filename4,
    filename5,
    filename6,
    filename7,
    filename8,
]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)

stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", pano)
    cv2.imwrite(output_filename, pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")
else:
    print("error: {}".format(status))

print("------------------------------------------------------------")  # 60個
# 全景圖 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.selectROI ST
print("------------------------------------------------------------")  # 60個

print("OpenCV selectROI 之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

roi = cv2.selectROI("image", image)
print("選取區域 :", roi)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.selectROI SP
print("------------------------------------------------------------")  # 60個

"""
print("------------------------------------------------------------")  # 60個
# Two Frames ST
print("------------------------------------------------------------")  # 60個

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# cap = cv2.VideoCapture(video_filename)  # 開啟影片
cap = cv2.VideoCapture("video.avi")  # 開啟影片

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
length = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

print("W :", W)
print("H :", H)
print("frames :", frames)
print("fps :", fps)
print("length :", length)

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

frameNum = 0

while True:
    # 获取一帧
    ret, frame = cap.read()  # 從影片擷取一張影像
    frameNum += 1
    if ret == True:
        frame = cv2.resize(frame, (W // 3, H // 3))
        tempframe = frame
        if frameNum == 1:  # 第1張圖
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)

        if frameNum >= 2:  # 第2張圖以後
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            currentframe = cv2.absdiff(currentframe, previousframe)
            median = cv2.medianBlur(currentframe, 3)
            ret, threshold_frame = cv2.threshold(
                currentframe, 20, 255, cv2.THRESH_BINARY
            )
            gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)  # 執行高斯模糊化

            cv2.imshow("Original", frame)
            cv2.imshow("Frame", currentframe)
            cv2.imshow("medianBlur", median)

            # 按键盘上的Q键退出
            if cv2.waitKey(33) & 0xFF == ord("q"):
                break
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
    else:
        print("播放結束")
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# Two Frames SP
print("------------------------------------------------------------")  # 60個
"""

"""
#GaussianBlur
#Canny
"""


def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階處理
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
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)  # 繪製直線
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

filename = "data/tmp1/road.jpg"

print("------------------------------------------------------------")  # 60個

# 彩色讀取
img = cv2.imread(filename)  # 讀取圖片

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (3, 3), 0)

plt.figure(figsize=(12, 8))
plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(312)
plt.title("灰階")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(313)
plt.title("高斯模糊")
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

cv2.imshow("Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("顯示邊緣圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

mask = np.zeros_like(edge)  # 全黑遮罩
points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊座標
cv2.fillPoly(mask, points, 255)  # 繪製三角形
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("顯示mask圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("顯示ROI圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

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

img = cv2.imread(filename)  # 讀取圖片

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
video_filename = "road.mp4"

capture = cv2.VideoCapture(video_filename)  # 建立 VideoCapture 物件
if capture.isOpened():
    while True:
        sucess, img = capture.read()  # 讀取影像
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
        if k == ord("q") or k == ord("Q"):  # 按下 Q(q) 結束迴圈
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break
else:
    print("開啟攝影機失敗")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.inpaint 影像修復 ST
print("------------------------------------------------------------")  # 60個

# 修復影像 inpaint

fail_filename = "C:/_git/vcs/_4.python/opencv/data/elephant_fail.jpg"

lisa = cv2.imread("data/mona_fail1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lisa = cv2.imread("data/mona_fail2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# cv2.inpaint 影像修復 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# cv2.imwrite("_tmp_face1.jpg", img)  # 存圖


# 存成pgm檔
cv2.imwrite("tmp_picture1.mono.pgm", img)

# cv2.imwrite("_tmp_face2.jpg", img)  # 存圖
