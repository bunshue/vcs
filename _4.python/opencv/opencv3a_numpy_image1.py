"""
opencv + numpy製作資料

"""

import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import random

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

W = 640
H = 480
D = 3

print("------------------------------------------------------------")  # 60個

image = np.zeros((H, W, D), dtype="uint8") * 255

print("初始化 H X W X D 陣列")
# print(image)
print(image.shape)

print("---------------")

# image[0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3, 0 : 3] = 10   #x方向

print("將所有點著色 著紅色")
image[:] = (0, 0, 255)
# print(image)

# image[0 : 50, 0 : 50] = 123 #前x, 後y
# image[2 : 6, 2 : 6] = 126

print("顯示原圖 BGR 排列")
cv2.imshow("image original B-G-R arrangement", image)

print("BGR轉RGB")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("R-G-B arrangement, wrong", rgb)

print("RGB轉BGR")
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
cv2.imshow("B-G-R arrangement", bgr)

# print("image = \n", image)
# print("rgb = \n", rgb)
# print("bgr = \n", bgr)

# plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.figure("建立圖檔 RGB與BGR排列", figsize=(12, 6))

plt.subplot(121)
plt.imshow(rgb)
plt.title("R-G-B 排列")

plt.subplot(122)
plt.imshow(bgr)
plt.title("B-G-R 排列")

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

w = int(640 / 20)
h = int(480 / 20)
D = 3

image = np.random.randint(
    0, 256, size=[h, w, D], dtype=np.uint8
)  # np.random之randint不含尾
print(image.shape)
rst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(rst.shape)
# print("image = \n", image)
print("rst = \n", rst)
print(
    "像素點 (1, 0) 直接計算得到的值 = ",
    image[1, 0, 0] * 0.114 + image[1, 0, 1] * 0.587 + image[1, 0, 2] * 0.299,
)
print("像素點 (1, 0) 使用公式cv2.cvtColor()轉換值 = ", rst[1, 0])
"""
print(image[1, 0, 0])
print(image[1, 0, 1])
print(image[1, 0, 2])
"""

# BGR排列轉RGB排列
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# RGB排列轉BGR排列
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
"""
print("image = \n", image)
print("rgb = \n", rgb)
print("bgr = \n", bgr)
"""

plt.figure("Random建立二維陣列 深度為3 轉灰階", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("轉灰階")

plt.show()

print("------------------------------------------------------------")  # 60個

w = int(640 / 20)
h = int(480 / 20)
image = np.random.randint(0, 256, size=[h, w], dtype=np.uint8)  # np.random之randint不含尾
print(image.shape)
rst = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
print(rst.shape)
# print("image = \n", image)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1 轉灰階", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("轉灰階")

plt.show()

print("------------------------------------------------------------")  # 60個

print("Random建立二維陣列為影像1")
image1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)  # np.random之randint不含尾
# print("image1 = \n", image1)

print("Random建立二維陣列為影像2")
image2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)  # np.random之randint不含尾
# print("image2 = \n", image2)

print("兩影像用cv2相加")
image3 = cv2.add(image1, image2)
# print("cv2.add(image1, image2) = \n", image3)

plt.figure("兩影像用cv2相加", figsize=(12, 6))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩影像用cv2相加")

plt.show()

print("------------------------------------------------------------")  # 60個

print("Random建立二維陣列為影像 a")
a = np.random.randint(0, 255, (5, 5), dtype=np.uint8)  # np.random之randint不含尾

b = np.zeros((5, 5), dtype=np.uint8)

b[0:3, 0:3] = 255
b[4, 4] = 255
c = cv2.bitwise_and(a, b)

# print("a = \n", a)
# print("b = \n", b)
# print("c = \n", c)

plt.figure("xxxxx", figsize=(12, 6))

plt.subplot(131)
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))
plt.title("影像3")

plt.show()

print("------------------------------------------------------------")  # 60個

image1 = np.ones((4, 4), dtype=np.uint8) * 3
print("image1 = \n", image1)

image2 = np.ones((4, 4), dtype=np.uint8) * 5
print("image2 = \n", image2)

mask = np.zeros((4, 4), dtype=np.uint8)
mask[2:4, 2:4] = 1
print("mask = \n", mask)

image3 = np.ones((4, 4), dtype=np.uint8) * 66
print("初始值image3 = \n", image3)

image3 = cv2.add(image1, image2, mask=mask)
print("求和后image3 = \n", image3)

plt.figure("xxxxx2", figsize=(12, 6))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("影像3")

plt.show()

print("------------------------------------------------------------")  # 60個

image1 = np.ones((4, 4), dtype=np.uint8) * 3
print("image1 = \n", image1)

image2 = np.ones((4, 4), dtype=np.uint8) * 5
print("image2 = \n", image2)

image3 = cv2.add(image1, image2)
print("cv2.add(image1, image2) = \n", image3)

image4 = cv2.add(image1, 6)
print("cv2.add(image1,6)\n", image4)

image5 = cv2.add(6, image2)
print("cv2.add(6, image2)=\n", image5)


plt.figure("xxxxx3", figsize=(12, 6))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(233)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("影像3")

plt.subplot(234)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("影像4")

plt.subplot(235)
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))
plt.title("影像5")

plt.show()

print("------------------------------------------------------------")  # 60個

image1 = np.ones((3, 4), dtype=np.uint8) * 100
image2 = np.ones((3, 4), dtype=np.uint8) * 10
gamma = 3
image3 = cv2.addWeighted(image1, 0.6, image2, 5, gamma)
print(image3)

plt.figure("兩影像用cv2權重gamma相加", figsize=(12, 6))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩影像用cv2權重gamma相加")

plt.show()

print("------------------------------------------------------------")  # 60個

W = 640
H = 480
D = 3
image = np.random.randint(
    0, 256, size=[H, W, D], dtype=np.uint8
)  # np.random之randint不含尾
print(image.shape)

plt.figure("Random建立二維陣列 深度為3", figsize=(12, 6))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random建立二維陣列 深度為3")

plt.show()

print("------------------------------------------------------------")  # 60個

# =========測試下OpenCV中藍色的HSV模式值=============
imageBlue = np.zeros([1, 1, 3], dtype=np.uint8)
imageBlue[0, 0, 0] = 255
Blue = imageBlue
BlueHSV = cv2.cvtColor(Blue, cv2.COLOR_BGR2HSV)
print("Blue = \n", Blue)
print("BlueHSV = \n", BlueHSV)

# =========測試下OpenCV中綠色的HSV模式值=============
imageGreen = np.zeros([1, 1, 3], dtype=np.uint8)
imageGreen[0, 0, 1] = 255
Green = imageGreen
GreenHSV = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)
print("Green = \n", Green)
print("GreenHSV = \n", GreenHSV)

# =========測試下OpenCV中紅色的HSV模式值=============
imageRed = np.zeros([1, 1, 3], dtype=np.uint8)
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

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)  # np.random之randint不含尾
min = 100
max = 200
mask = cv2.inRange(image, min, max)
print("image = \n", image)
print("mask = \n", mask)

plt.figure("mask", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("image")

plt.subplot(122)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.ones([5, 5], dtype=np.uint8) * 9
mask = np.zeros([5, 5], dtype=np.uint8)
mask[0:3, 0] = 1
mask[2:5, 2:4] = 1
roi = cv2.bitwise_and(image, image, mask=mask)
print("image = \n", image)
print("mask = \n", mask)
print("roi = \n", roi)

plt.figure("mask roi", figsize=(12, 6))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("image")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(133)
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("roi")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(
    0, 256, size=[2, 3, 3], dtype=np.uint8
)  # np.random之randint不含尾
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

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(
    -256, 256, size=[4, 5], dtype=np.int16
)  # np.random之randint不含尾
rst = cv2.convertScaleAbs(image)
print("image = \n", image)
print("rst = \n", rst)

""" 有負的數值 不能顯示
plt.figure('Random建立二維陣列 深度為1', figsize = (12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Random 二維陣列')

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title('xxxx')

plt.show()
"""

print("------------------------------------------------------------")  # 60個

image = np.zeros((5, 5), np.uint8)
image[1:4, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
erosion = cv2.erode(image, kernel)
print("image = \n", image)
print("kernel = \n", kernel)
print("erosion = \n", erosion)

plt.figure("erosion", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))
plt.title("erosion")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.zeros((5, 5), np.uint8)
image[2:3, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
dilation = cv2.dilate(image, kernel)
print("image = \n", image)
print("kernel = \n", kernel)
print("dilation\n", dilation)

plt.figure("dilation", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))
plt.title("dilation")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)  # np.random之randint不含尾
t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print("image = \n", image)
print("t = ", t)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)  # np.random之randint不含尾
t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
print("image = \n", image)
print("t = ", t)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

plt.show()

print("------------------------------------------------------------")  # 60個
image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)  # np.random之randint不含尾
t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
print("image = \n", image)
print("t = ", t)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)  # np.random之randint不含尾
t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
print("image = \n", image)
print("t = ", t)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)  # np.random之randint不含尾
t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
print("image = \n", image)
print("t = ", t)
print("rst = \n", rst)

plt.figure("Random建立二維陣列 深度為1", figsize=(12, 6))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

plt.show()

print("------------------------------------------------------------")  # 60個

image = np.zeros((5, 5), dtype=np.uint8)
image[0:6, 0:6] = 123
image[2:6, 2:6] = 126
print("image = \n", image)

t1, thd = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print("thd = \n", thd)

t2, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("otsu = \n", otsu)

print("------------------------------------------------------------")  # 60個

d = 400
image = np.ones((d, d, 3), dtype="uint8") * 255
(centerX, centerY) = (round(image.shape[1] / 2), round(image.shape[0] / 2))
# 將圖像的中心作為圓心,實際值為 d / 2
red = (0, 0, 255)  # 設置白色變量
for r in range(5, round(d / 2), 12):
    cv2.circle(image, (centerX, centerY), r, red, 3)
    # circle(載體圖像，圓心，半徑，顏色)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 1")
plt.show()

cv2.imshow("Demo19.3", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

d = 400
image = np.ones((d, d, 3), dtype="uint8") * 255
# 生成白色背景
for i in range(0, 100):
    centerX = np.random.randint(0, high=d)  # np.random之randint不含尾
    # 生成隨機圓心X,確保在畫布image內
    centerY = np.random.randint(0, high=d)  # np.random之randint不含尾
    # 生成隨機圓心Y,確保在畫布image內
    radius = np.random.randint(5, high=d / 5)  # np.random之randint不含尾
    # 生成隨機半徑，值范圍：[5, d/5)，最大半徑是 d / 5
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
    # 生成隨機顏色，3個[0, 256)的隨機數
    cv2.circle(image, (centerX, centerY), radius, color, -1)
    # 使用上述隨機數，在畫布image內畫圓


plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 2")
plt.show()

cv2.imshow("demo19.4", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

d = 400
image = np.ones((d, d, 3), dtype="uint8") * 255
# 生成白色背景
center = (round(d / 2), round(d / 2))
# 注意數值類型，center = (d / 2, d / 2)不可以
size = (100, 200)
# 軸的長度
for i in range(0, 10):
    angle = np.random.randint(0, 361)  # np.random之randint不含尾
    # 偏移角度
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
    # 生成隨機顏色，3個[0, 256)的隨機數
    thickness = np.random.randint(1, 9)  # np.random之randint不含尾
    cv2.ellipse(image, center, size, angle, 0, 360, color, thickness)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 3")
plt.show()

cv2.imshow("demo19.5", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

d = 400
image = np.ones((d, d, 3), dtype="uint8") * 255
# 生成白色背景
pts = np.array([[200, 50], [300, 200], [200, 350], [100, 200]], np.int32)
# 生成各個頂點,注意數據類型為int32
pts = pts.reshape((-1, 1, 2))
# 第1個參數為-1, 表明這一維的長度是根據后面的維度的計算出來的。
cv2.polylines(image, [pts], True, (0, 255, 0), 8)
# 調用函數polylines完成多邊形繪圖，注意第3個參數控制多邊形封閉
# cv2.polylines(image, [pts], False, (0, 255, 0), 8)  #不閉合的的多邊形

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 4")
plt.show()

cv2.imshow("demo19.6", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" fail
def changeColor(x):
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    image[ : ] = [b, g, r]
image = np.zeros((100,700,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image', 100, 255, changeColor)
cv2.createTrackbar('G','image', 0, 255, changeColor)
cv2.createTrackbar('B','image', 0, 255, changeColor)
while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break   

cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

""" fail
Type = 0  #閾值處理類型值
Value = 0 #使用的閾值
def onType(a):
    Type = cv2.getTrackbarPos(tType, windowName)
    Value = cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type) 
    cv2.imshow(windowName,dst)
 
def onValue(a):
    Type = cv2.getTrackbarPos(tType, windowName)
    Value = cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type) 
    cv2.imshow(windowName,dst)

o = cv2.imread("images/lena512.bmp", 0)
windowName = "Demo19.13"  #窗體名
cv2.namedWindow(windowName)
cv2.imshow(windowName,o)
#創建兩個滑動條
tType = "Type"  #用來選取閾值處理類型的滾動條
tValue = "Value"    #用來選取閾值的滾動條
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tValue, windowName, 0, 255, onValue) 

if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()

"""

print("------------------------------------------------------------")  # 60個

"""

print('------------------------------------------------------------')	#60個

def changeColor(x):
    g = cv2.getTrackbarPos('R','image')
    if g == 0:
        image[:] = 0
    else:
        image[:] = 255
image = np.zeros((100, 1000, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 1, changeColor)
while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break   

cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
