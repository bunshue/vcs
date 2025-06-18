"""
opencv + numpy製作資料

"""

W, H, D = 640, 480, 3

from opencv_common import *

print("------------------------------------------------------------")  # 60個

print("初始化 H X W X D 陣列")
W, H, D = 640, 480, 3
image = np.zeros((H, W, D), dtype="uint8") * 255

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

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

w = int(640 / 20)
h = int(480 / 20)
W, H, D = 640, 480, 3
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

show()

print("------------------------------------------------------------")  # 60個

w = int(640 / 20)
h = int(480 / 20)
W, H, D = 640, 480, 3
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

show()

print("------------------------------------------------------------")  # 60個

print("Random建立二維陣列為影像1")
W, H, D = 3, 3, 3
image1 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
# print("image1 = \n", image1)

print("Random建立二維陣列為影像2")
W, H, D = 3, 3, 3
image2 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個

print("Random建立二維陣列為影像 a")
W, H, D = 5, 5, 3
a = np.random.randint(0, 255, (H, W), dtype=np.uint8)  # np.random之randint不含尾
b = np.zeros((H, W), dtype=np.uint8)

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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 4, 4, 3
image1 = np.ones((H, W), dtype=np.uint8) * 3
print("image1 = \n", image1)

W, H, D = 4, 4, 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
print("image2 = \n", image2)

W, H, D = 4, 4, 3
mask = np.zeros((H, W), dtype=np.uint8)
mask[2:4, 2:4] = 1
print("mask = \n", mask)

W, H, D = 4, 4, 3
image3 = np.ones((H, W), dtype=np.uint8) * 66
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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 4, 4, 3
image1 = np.ones((H, W), dtype=np.uint8) * 3
print("image1 = \n", image1)

W, H, D = 4, 4, 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 4, 3, 3
image1 = np.ones((H, W), dtype=np.uint8) * 100
image2 = np.ones((H, W), dtype=np.uint8) * 10

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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3
image = np.random.randint(
    0, 256, size=[H, W, D], dtype=np.uint8
)  # np.random之randint不含尾
print(image.shape)

plt.figure("Random建立二維陣列 深度為3", figsize=(12, 6))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random建立二維陣列 深度為3")

show()

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

W, H, D = 5, 5, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 5, 5, 3
image = np.ones([H, W], dtype=np.uint8) * 9
mask = np.zeros([H, W], dtype=np.uint8)

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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 3, 2, 3
image = np.random.randint(
    0, 256, size=[H, W, D], dtype=np.uint8
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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(
    -256, 256, size=[H, W], dtype=np.int16
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

show()
"""

print("------------------------------------------------------------")  # 60個

W, H, D = 5, 5, 3
image = np.zeros((H, W), np.uint8)
image[1:4, 1:4] = 1

W, H, D = 1, 3, 3
kernel = np.ones((H, W), np.uint8)
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

show()

print("------------------------------------------------------------")  # 60個

W, H, D = 5, 5, 3
image = np.zeros((H, W), np.uint8)
image[2:3, 1:4] = 1

W, H, D = 1, 3, 3
kernel = np.ones((H, W), np.uint8)
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

show()

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
