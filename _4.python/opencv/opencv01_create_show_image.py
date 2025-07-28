"""
OpenCV 基本使用

建立影像 ST
二維灰階/二維深度1 全黑/全白/隨機/著色
三維彩色/二維深度3 全黑/全白/隨機/著色

開啟檔案
	彩色/黑白/其他參數
存檔

CV視窗之使用

顯示圖片 / 使用 cv2 顯示圖片 / 使用 matplotlib 顯示圖片

讀取圖片 存圖

以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列
查看資料型態
print(type(image))
print(type(image_gray))
<class "numpy.ndarray">

#此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度
#第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）

H ,W, D = image.shape
print("Image Size: %d x %d, channel = %d" % (W, H, D))

H ,W = image_gray.shape
#print("Image Size: %d x %d, channel = %d" % (W, H, D))

此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度，第三個維度則是圖片的 channel
（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）。
"""

from opencv_common import *

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("取得 OpenCV 版本")

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split(".")

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print("------------------------------------------------------------")  # 60個
# 建立影像 ST
# 二維灰階/二維深度1 全黑/全白/隨機/著色
# 三維彩色/二維深度3 全黑/全白/隨機/著色
print("------------------------------------------------------------")  # 60個

print("二維黑圖")
image = np.zeros((H, W), dtype=np.uint8)

print("三維黑圖")
image = np.zeros((H, W, D), np.uint8)  # 三維黑圖
image = np.zeros((H, W, D), dtype="uint8")
image = np.zeros((H, W, D), dtype=np.uint8)  # 空白畫布

print("三維白圖")
image = np.ones((H, W, D), np.uint8) * 255  # 白底畫布
image = np.ones((H, W, D), dtype="uint8") * 255

# 灰色背景
image[:] = (128, 128, 128)

# 將這個矩陣全部填入指定顏色
image[:] = [48, 213, 254]

# 將所有點著色 著紅色
image[:] = RED

# 用(B, G, R) = (255, 255, 255): 白色填滿畫布

image.fill(255)  # 將這個矩陣全部填入255 => 白色, 128 => 灰色


image1 = np.ones((H, W), dtype=np.uint8) * 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
mask = np.zeros((H, W), dtype=np.uint8)
mask[2:4, 2:4] = 1
image3 = np.ones((H, W), dtype=np.uint8) * 66
image3 = cv2.add(image1, image2, mask=mask)

image1 = np.ones((H, W), dtype=np.uint8) * 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
image3 = cv2.add(image1, image2)

image4 = cv2.add(image1, 6)
image5 = cv2.add(6, image2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

# 建立白圖 二維灰階/二維深度1
image = np.ones((H, W), dtype=np.uint8) * 255

# 建立黑圖 二維灰階/二維深度1
image = np.zeros((H, W), dtype=np.uint8)

# 建立黑圖 二維灰階/二維深度1
image = np.zeros((H, W), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

print("某些塗為白色")

for y in range(0, H, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

print("建立 隨機影像 二維灰階/二維深度1")
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # 灰階, 1維隨機影像

print("建立 隨機影像 三維彩色/二維深度3")
W, H, D = 640, 480, 3
image = np.random.randint(0, 256, size=[H, W, D], dtype=np.uint8)  # 彩色, 3維隨機影像
image = np.random.randint(0, 256, size=(H, W))  # 灰階, 1維隨機影像

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(image)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3

print("建立 隨機影像 三維彩色/二維深度3")
image = np.random.randint(0, 256, size=[H, W, D], dtype=np.uint8)  # 彩色, 3維隨機影像

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

print(
    "像素點 (1, 0) 直接計算得到的值 = ",
    image[1, 0, 0] * 0.114 + image[1, 0, 1] * 0.587 + image[1, 0, 2] * 0.299,
)
print("像素點 (1, 0) 使用公式cv2.cvtColor()轉換值 = ", image_gray[1, 0])
"""
print(image[1, 0, 0])
print(image[1, 0, 1])
print(image[1, 0, 2])
"""

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("隨機影像 三維彩色/二維深度3")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
plt.title("轉灰階")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# itemset()

W, H, D = 5, 3, 3  # 影像寬, 影像高, 深度

image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # 灰階, 1維隨機影像

print("取得影像內容")
print(f"修改前image.item(1,3) = {image.item(1,3)}")

print("修改影像內容")
image.itemset((1, 3), 255)  # 修訂內容為 255
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

# 建立黑圖 二維灰階/二維深度1
image = np.zeros((H, W), np.uint8)

image.fill(255)  # 將這個矩陣全部填入255 => 白色, 128 => 灰色

# 建立白圖 二維灰階/二維深度1
image = np.ones((H, W), np.uint8) * 255

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

# R, 建立黑圖 三維彩色/二維深度3 改 R 通道
red_image = np.zeros((H, W, D), np.uint8)  # 三維黑圖
red_image[:, :, 2] = 255  # 建立 R 通道像素值, 填滿紅色

# G, 建立黑圖 三維彩色/二維深度3 改 G 通道
green_image = np.zeros((H, W, D), np.uint8)  # 三維黑圖
green_image[:, :, 1] = 255  # 建立 G 通道像素值, 填滿綠色

# B, 建立黑圖 三維彩色/二維深度3 改 B 通道
blue_image = np.zeros((H, W, D), np.uint8)  # 三維黑圖
blue_image[:, :, 0] = 255  # 建立 B 通道像素值, 填滿藍色

# Y, 建立黑圖 三維彩色/二維深度3 改 RG 通道
yellow_image = np.zeros((H, W, D), np.uint8)  # 三維黑圖
yellow_image[:, :, 2] = 255  # 建立 R 通道像素值, 填滿紅色
yellow_image[:, :, 1] = 255  # 建立 G 通道像素值, 填滿綠色

plt.subplot(231)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))
plt.title("R")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))
plt.title("B")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))
plt.title("Y")
plt.axis("off")

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

# 建立黑圖 三維彩色/二維深度3
image = np.zeros((H, W, D), np.uint8)  # 三維黑圖

image[0:96, :, 2] = 255  # 2, R通道
image[96 : 96 * 2, :, 1] = 255  # 1, G通道
image[96 : 96 * 2, :, 2] = 255  # 2, R通道
image[96 * 2 : 96 * 3, :, 0] = 255  # 0, B通道
image[96 * 3 : 96 * 4, :, 0] = 255  # 0, B通道
image[96 * 3 : 96 * 4, :, 1] = 255  # 1, G通道
image[96 * 3 : 96 * 4, :, 2] = 255  # 2, R通道

plt.subplot(235)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("五色旗")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 建立影像 SP
# 二維灰階/二維深度1 全黑/全白/隨機/著色
# 三維彩色/二維深度3 全黑/全白/隨機/著色
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 讀取圖片
print("------------------------------------------------------------")  # 60個
"""
cv2.imread 參數:
cv2.IMREAD_COLOR     彩色 + 無透明度 (預設)
cv2.IMREAD_GRAYSCALE 灰階
cv2.IMREAD_UNCHANGED 彩色 + 有透明度

# 讀取本機圖片, 0: 黑白圖片 1: 原色圖片
# image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)	# -1 讀取本機圖片, 不改變顏色通道
# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#  0 讀取本機圖片, 直接變成灰階
# image = cv2.imread(filename, cv2.IMREAD_COLOR)        #  1 讀取本機圖片, 改為BGR三通道(預設)

# cv2.IMREAD_UNCHANGED = -1
# cv2.IMREAD_GRAYSCALE =  0
# cv2.IMREAD_COLOR     =  1 (預設)
"""

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image = cv2.imread(filename1)  # 彩色讀取

print("圖像屬性 :")
print("image.shape=", image.shape)
print("image.size=", image.size)
print("image.dtype=", image.dtype)
print("image.shape格式 :", type(image.shape))
print("image.shape內容 :", image.shape)

H = image.shape[0]  # 高
W = image.shape[1]  # 寬
D = image.shape[2]  # 深
H, W, D = image.shape  # D為dimension D=3 全彩, D=1 灰階
print("寬 = ", W, ", 高 = ", H, ", D = ", D)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image_bgr = cv2.imread(filename1)  # 彩色讀取

# BGR 轉 RGB
image_rgb1 = image_bgr[:, :, ::-1]  # 將 BGR 圖片轉為 RGB 圖片

# BGR 轉 RGB
image_rgb2 = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.subplot(131)
plt.imshow(image_bgr)
plt.title("直接顯示BGR(錯誤)")
plt.subplot(132)
plt.imshow(image_rgb1)
plt.title("陣列換行")
plt.subplot(133)
plt.imshow(image_rgb2)
plt.title("cvtColor(用此)")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("像素操作 底片效果 半張負片")

image = cv2.imread(filename1)  # 彩色讀取

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

rows = image.shape[0]  # 取得高度的總像素
cols = image.shape[1]  # 取得寬度的總像素

for row in range(int(rows / 2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        image[row, col, 0] = 255 - image[row, col, 0]  # 255 - 藍色
        image[row, col, 1] = 255 - image[row, col, 1]  # 255 - 綠色
        image[row, col, 2] = 255 - image[row, col, 2]  # 255 - 紅色

plt.subplot(132)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("半張負片")

print("像素操作 全張負片")

image = cv2.imread(filename1)  # 彩色讀取

image = 255 - image  # 使用 255 減去陣列中所有數值

plt.subplot(133)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("全張負片")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("並列一圖 hconcat")

image1 = cv2.imread(filename1)  # 彩色讀取

image2 = cv2.hconcat([image1, image1, image1, image1, image1, image1])

plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("並列一圖 hconcat")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取
image_r = cv2.imread(filename1)  # 彩色讀取
image_g = cv2.imread(filename1)  # 彩色讀取
image_b = cv2.imread(filename1)  # 彩色讀取

image_r[:, :, 0] = 0  # 將藍色設為 0
image_r[:, :, 1] = 0  # 將綠色設為 0

image_g[:, :, 0] = 0  # 將藍色設為 0
image_g[:, :, 2] = 0  # 將紅色設為 0

image_b[:, :, 1] = 0  # 將綠色設為 0
image_b[:, :, 2] = 0  # 將紅色設為 0

plt.figure(figsize=(10, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image_r, cv2.COLOR_BGR2RGB))
plt.title("R通道")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image_g, cv2.COLOR_BGR2RGB))
plt.title("G通道")

plt.subplot(233)
plt.imshow(cv2.cvtColor(image_b, cv2.COLOR_BGR2RGB))
plt.title("B通道")

print("原圖 彩色 轉 灰階1通道")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

print("灰階 轉 BGR3通道")
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print("rgb.shape=", rgb.shape)

plt.subplot(234)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖 彩色")

plt.subplot(235)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("灰階1通道")

plt.subplot(236)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))
plt.title("BGR3通道")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(8, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("修改一部份資料 1")
for i in range(20, 60):  # y
    for j in range(20, 100):  # x
        image[i, j] = 255

print("修改一部份資料 2")
# 測試讀取、修改單個像素值
print("讀取像素點image.item(3,2)=", image.item(3, 2))
image.itemset((3, 2), 255)
print("修改後像素點image.item(3,2)=", image.item(3, 2))
# 測試修改一個區域的像素值
for i in range(100, 200):  # y
    for j in range(20, 60):  # x
        image.itemset((i, j), 220)

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("修改後的圖")

print("------------------------------")  # 30個

image = cv2.imread(filename1)  # 彩色讀取

plt.subplot(223)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("讀取 image[0, 0] =", image[0, 0])
print("讀取 image[0, 0, 0] =", image[0, 0, 0])
print("讀取 image[0, 0, 1] =", image[0, 0, 1])
print("讀取 image[0, 0, 2] =", image[0, 0, 2])
print("讀取 image[50, 0] =", image[50, 0])
print("讀取 image[100, 0] =", image[100, 0])

# 區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            image[i, j, k] = 255  # 白色
# 區域2
for i in range(50, 100):
    for j in range(0, 100):
        image[i, j] = [128, 128, 128]  # 灰色

# 區域3
for i in range(100, 150):
    for j in range(0, 100):
        image[i, j] = 0  # 黑色

# 區域4
print("讀取 image.item(0, 0, 0) =", image.item(0, 0, 0))
print("讀取 image.item(0, 0, 1) =", image.item(0, 0, 1))
print("讀取 image.item(0, 0, 2) =", image.item(0, 0, 2))

for i in range(200, 250):
    for j in range(0, 100):
        for k in range(0, 3):
            image.itemset((i, j, k), 255)  # 白色

print("修改後 image.item(0, 0, 0) =", image.item(0, 0, 0))
print("修改後 image.item(0, 0, 1) =", image.item(0, 0, 1))
print("修改後 image.item(0, 0, 2) =", image.item(0, 0, 2))
print("修改後 image[0, 0] =", image[0, 0])
print("修改後 image[0, 0, 0] =", image[0, 0, 0])
print("修改後 image[0, 0, 1] =", image[0, 0, 1])
print("修改後 image[0, 0, 2] =", image[0, 0, 2])
print("修改後 image[50, 0] =", image[50, 0])
print("修改後 image[100, 0] =", image[100, 0])

plt.subplot(224)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("修改後的圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lena_color_filename = "C:/_git/vcs/_4.python/opencv/data/lena_color.png"

lena_color = cv2.imread(lena_color_filename)  # 彩色讀取
print(lena_color.shape)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(lena_color, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("擷取一塊出來, 並顯示之")
face = lena_color[200:400, 200:380]  # H, W

plt.subplot(132)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.title("擷取一塊出來")

print("將其中一塊亂碼化, 並顯示之")
x_st, y_st, W, H = 50, 50, 100, 180
face = np.random.randint(0, 256, (H, W, 3))  # 彩色, 3維隨機影像
lena_color[y_st : y_st + H, x_st : x_st + W] = face

plt.subplot(133)
plt.imshow(cv2.cvtColor(lena_color, cv2.COLOR_BGR2RGB))
plt.title("將其中一塊亂碼化")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("漸層色")

W, H = 400, 400
image = np.zeros([H, W, 3])
for i in range(H):
    for j in range(W):
        image[i, j, 0] = int(256 * (j + i) / (W + H))
        image[i, j, 2] = int(256 * (j + i) / (W + H))

image = image.astype("float32") / 255

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("漸層色")

print("------------------------------")  # 30個

W, H = 400, 400
image = np.zeros([H, W, 3])
for i in range(H):
    image[i, :, 1] = int(256 * i / 400)  # 從上往下填入綠色漸層

image = image.astype("float32") / 255  # 轉換內容類型

plt.subplot(132)
# NG plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.imshow(image)
plt.title("漸層色")

print("------------------------------")  # 30個

W, H = 400, 400
image = np.zeros([H, W, 4])  # 第三個值為 4
for i in range(H):
    image[i, :, 3] = int(256 * i / 400)  # 設定第四個值 ( 透明度 )

image = image.astype("float32") / 255

plt.subplot(133)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("黑圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3

image = np.zeros((H, W, D), dtype="uint8") * 255
print(image.shape)

print("---------------")

# image[0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3, 0 : 3] = 10   #x方向

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

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("使用 matplotlib 顯示圖片, 需先BGR轉RGB")

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

filename = filename1

cv2.namedWindow("OpenCV")
image = cv2.imread(filename)  # 彩色讀取

cv2.imshow("OpenCV", image)  # 顯示影像img

cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("OpenCV222")  # 刪除OpenCV222
cv2.destroyAllWindows()  # 刪除所有視窗

# cv2.waitKey(2000)       # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 取出像素值, 修改之

image = cv2.imread(filename1)  # 彩色讀取

print(f"修改前img[115,110] = {image[115,110]}")
print(f"修改前img[125,110] = {image[125,110]}")
print(f"修改前img[135,110] = {image[135,110]}")

# 紫色長條
image[115:125, 110:210] = [255, 0, 255]

# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            image[z, y, x] = 255  # 白色取代

# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        image[y, x] = [0, 255, 255]  # 黃色取代

cv2.imshow("After", image)  # 顯示修改後影像img

print(f"修改後img[115,110] = {image[115,110]}")
print(f"修改後img[125,110] = {image[125,110]}")
print(f"修改後img[135,110] = {image[135,110]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("修改alpha通道值 255=>127")

# 4通道的PNG圖
filename_RGB_R = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"

image = cv2.imread(filename_RGB_R, cv2.IMREAD_UNCHANGED)  # PNG讀取  # 彩色讀取 + 有透明度
cv2.imshow("Before", image)  # 顯示修改前影像img
print(image.shape)
print(f"修改前img[210,150] = {image[210,150]}")
print(f"修改前img[250,199] = {image[250,199]}")

for z in range(0, image.shape[1]):  # 一次一個修改alpha通道值
    for y in range(0, image.shape[0]):
        image[z, y, 3] = 127  # 修改alpha通道值

image[0:200, 0:200, 3] = 127  # 修改alpha通道值

print(f"修改後img[210,150] = {image[210,150]}")
print(f"修改後img[250,199] = {image[250,199]}")

cv2.imshow("After", image)  # 顯示修改前影像img
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("灰階讀取, 部分塗成灰色")

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
cv2.imshow("Before", image)  # 顯示修改前影像img

for y in range(30, 100):  # 修改影像
    for x in range(180, 280):
        image.itemset((y, x), 127)

cv2.imshow("After", image)  # 顯示修改後影像img
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
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

image = cv2.imread(filename1)  # 彩色讀取

cv2.imshow("Before", image)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {image.item(115,110,1)}")
print(f"修改前img[125,110,1] = {image.item(125,110,1)}")
print(f"修改前img[135,110,1] = {image.item(135,110,1)}")

# 白色長條
for z in range(30, 100):  # 修改影像:一次一個通道值
    for y in range(180, 280):
        for x in range(0, 3):  # 一次一個通道值
            image.itemset((z, y, x), 127)  # 白色取代
cv2.imshow("After", image)  # 顯示修改後影像img

print(f"修改後img[115,110,1] = {image.item(115,110,1)}")
print(f"修改後img[125,110,1] = {image.item(125,110,1)}")
print(f"修改後img[135,110,1] = {image.item(135,110,1)}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

建立
print("用np建立一個影像陣列")

W = 640
H = 480
D = 3

# 建立陣列
image = np.ones([H, W, D], dtype=np.uint8) * 128  # 填滿 128

# 改變陣列內容
image[:, :, 0] = 0
# 第0通道 B
image[:, :, 1] = 255
# 第1通道 G
image[:, :, 2] = 255
# 第2通道 R

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

image[0, 0] = [0, 0, 255]
image[10:100, 10:100] = [0, 255, 0]

cv2.imshow("OpenCV", image)
cv2.waitKey(0)  # 0, 無限等待使用者按鍵
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ????

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

image = cv2.imread(filename1, 1)  # 讀取本機圖片, 0: 黑白圖片 1: 原色圖片

image_gray = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # 轉灰階

image_gray = cv2.convertScaleAbs(image)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

cv2.imshow("Image", image)

while True:
    # k = cv2.waitKey(100)  #每 100 msec 讀一次鍵盤
    k = cv2.waitKey(1)  # 每 1 msec 讀一次鍵盤
    if k == ESC:
        break

# cv2.waitKey() # 按任意鍵繼續

cv2.destroyAllWindows()


W, H, D = 10, 10, 3

print("建立 隨機影像 二維灰階/二維深度1")
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # 灰階, 1維隨機影像

# 建立mask
mask = np.zeros((H, W), dtype=np.uint8)
mask[2:8, 2:8] = 255
image_mask = cv2.bitwise_and(image, mask)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3  # 影像寬, 影像高, 深度

image = np.zeros([H, W], np.uint8)  # 建立影像
image[50 : H - 50, 50 : W - 50] = 255  # 在影像內建立遮罩

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("兩影像用cv2相加")
image3 = cv2.add(image1, image2)

image1 = np.ones((H, W), dtype=np.uint8) * 100
image2 = np.ones((H, W), dtype=np.uint8) * 10

# 兩影像用cv2權重gamma相加
gamma = 3
image3 = cv2.addWeighted(image1, 0.6, image2, 5, gamma)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# cv2 之 存檔 可透過圖片的副檔名來指定輸出的圖檔格式
# jpg/png/bmp/pgm/tiff

filename = "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
cv2.imwrite(filename, image)
cv2.imwrite(filename=filename, img=image)
print("已存圖, 檔案 :", filename)

# 部分圖片寫入圖檔
# cv2.imwrite(filename, image[y:y + H, x:x + W])

cv2.imwrite("tmp_char%s.jpg" % flag, thresh1[y : y + H, x : x + W])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

print(type(image))
print(image.shape)

# 建立相同大小的黑圖
result = np.zeros_like(image)
print(type(result))
print(result.shape)

# 建立相同大小的白圖
result = np.ones_like(image) * 255
print(type(result))
print(result.shape)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
# 將 OpenCV 讀入的 BGR 格式轉為 Matplotlib 用的 RGB 格式，再交給 Matplotlib 顯示

# plt.imshow(image_gray, cmap="gray")  # 灰階顯示
# plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))

# 等同於 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # BGR轉RGB再交由matplotlib顯示之

# BGR排列轉RGB排列
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# RGB排列轉BGR排列
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


image = cv2.imread(filename1)

for i in range(20, 80):
    image[i, 180] = RED  # 紅色一點

#       H        W
image[10:100, 200:290] = GREEN  # 綠色 一塊 90X90

"""
OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：

數值  1 cv2.IMREAD_COLOR
此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。

數值  0 cv2.IMREAD_GRAYSCALE
以灰階的格式來讀取圖片。

數值 -1 cv2.IMREAD_UNCHANGED
讀取圖片中所有的 channels，包含透明度的 channel。

窗口显示方式，cv2.WINDOW_NORMAL为正常显示，可以调整大小
# cv2.WINDOW_AUTOSIZE显示原图片的大小，用户不能调整大小

opencv之paste
x_st, y_st, W, H

小圖先縮放至所需大小 W, H
大圖之(y_st:y_st+H, x_st:x_st+W) = 小圖之全部

後面還有一個參數
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), "gray")

#輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite(filename, image, [cv2.IMWRITE_JPEG_QUALITY, 90])

print("存圖, 質量為5")
cv2.imwrite(filename, image, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
print("存圖, 質量為100")
cv2.imwrite(filename, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite(filename, image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
cv2.imwrite(filename, image, [cv2.IMWRITE_JPEG_QUALITY, 80])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite("filename.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 5])
print("存圖, 壓縮為0")
cv2.imwrite("filename.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
print("存圖, 壓縮為9")
cv2.imwrite("filename.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

cv 搬出
#另存新檔
cv2.imwrite(filename, image)	#寫入本機圖片

一樣的意思
plt.imshow(image0[:, :, ::-1])  # 原圖 # same
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖

src = cv2.imread(filename)  # 彩色讀取
src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 黑白讀取
"""
print("------------------------------------------------------------")  # 60個
# CV視窗之使用 ST
print("------------------------------------------------------------")  # 60個

"""
這裡 cv2.waitKey 函數是用來等待與讀取使用者按下的按鍵，而其參數是等待時間（單位為毫秒），
若設定為 0 就表示持續等待至使用者按下按鍵為止，
這樣當我們按下任意按鍵之後，就會呼叫 cv2.destroyAllWindows 關閉所有 OpenCV 的視窗。

如果在程式中有許多的 OpenCV 視窗，而我們只要關閉特定的視窗時，
可以改用 cv2.destroyWindow 加上視窗名稱，關閉指定的視窗

# 關閉 "OpenCV333" 視窗
cv2.destroyWindow("OpenCV333")

在預設的狀況下，以 cv2.imshow 所開啟的視窗會依據圖片來自動調整大小，
但若是圖片太大、佔滿整個螢幕時，我們會希望可以自由縮放視窗的大小，
這時候就可以使用 cv2.namedWindow 將視窗設定為 cv2.WINDOW_NORMAL：

cv2.imshow("OpenCV", image)

print("在此等待任意鍵繼續, 繼續後刪除本視窗")
cv2.waitKey()
cv2.destroyAllWindows()

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)  # 0, 無限等待使用者按鍵
cv2.destroyAllWindows() # 關閉所有 OpenCV 的視窗

# 關閉 "OpenCV333" 視窗
# cv2.destroyWindow("OpenCV333") 指名關閉某視窗

使用 OpenCV 開啟的圖形視窗會類似這樣：

OpenCV 顯示圖片視窗

灰階的圖片也可以顯示，用法都相同：
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

cv2.imshow("OpenCV", image)
cv2.destroyWindow("OpenCV")  # 關閉視窗

k = cv2.waitKey(0)  # 0, 無限等待使用者按鍵
cv2.destroyWindow("OpenCV")  # 關閉視窗

k = cv2.waitKey(5000)  # 等待 5000 msec
cv2.destroyWindow("OpenCV")  # 關閉視窗

k = cv2.waitKey(0)  # 0, 無限等待使用者按鍵

""" 視窗功能
k = cv2.waitKey(200)  # 0.2秒檢查一次

if k == ord("a") or k == ord("A"):  # 如果按A或a
    do_something()

elif k == ord("s"):  # 若按下 s 鍵則存圖

if k == ord("Q") or k == ord("q"):
    cv2.destroyWindow("OpenCV")  # 關閉視窗
 
WINDOW_NORMAL – Allows to manually change window size
WINDOW_AUTOSIZE(Default) – Automatically sets the window size
WINDOW_FULLSCREEN – Changes the window size to fullscreen

# 設定 cv 視窗
cv2.namedWindow("OpenCV")

# 若有多個視窗 要指名視窗名稱
cv2.namedWindow("OpenCV", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("OpenCV", cv2.WINDOW_NORMAL)  # 讓視窗可以自由縮放大小
cv2.namedWindow("OpenCV", cv2.WINDOW_NORMAL)  # 可調整大小

# 可調整大小 並 保持比例
cv2.namedWindow("OpenCV", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)


# 設定視窗參數, 若不設定, 即是 圖片滿框、不可調整大小
# 預設 flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO |WINDOW_GUI_EXPANDED

# WINDOW_FREERATIO 不 保持比例
# WINDOW_KEEPRATIO    保持比例

cv2.destroyWindow("OpenCV")  # 指明刪除特定的視窗
"""
print("測試CV視窗 : 全螢幕顯示一圖")

image = cv2.imread(filename1)  # 彩色讀取

cv2.setWindowProperty("OpenCV", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試CV視窗 : 設定視窗大小並依視窗縮放影像")

image = cv2.imread(filename1)  # 彩色讀取

cv2.namedWindow("OpenCV640X480", 0)
cv2.resizeWindow("OpenCV640X480", 640, 480)

# 設定視窗位置
x_st, y_st = 300, 100
cv2.moveWindow("OpenCV640X480", x_st, y_st)

cv2.imshow("OpenCV640X480", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" OK
print("使用 cv2 顯示圖片")

image = cv2.imread(filename1)  # 彩色讀取

cv2.imshow("Image", image)  #顯示圖片, 標題不支持中文

print("在此等待任意鍵繼續, 繼續後刪除本視窗")
cv2.waitKey()
cv2.destroyAllWindows()
"""

"""
#例外的寫法
image = cv2.imread(filename1)  # 彩色讀取
if image is None:
    raise Exception("we need the digits.png image from samples/data here !")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立影像
image = cv2.imread(filename1)  # 使用影像當畫布
image = np.ones((350, 500, 3), np.uint8) * 255  # 白底畫布
image[1:300, 1:300] = YELLOW  # 設定黃色底

"""
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
image = cv2.imread(filename)  # 彩色讀取
image = cv2.imread(filename, 0)  # 灰階讀取

"""

cv2.namedWindow("OpenCV")  # 建立一個名為 OpenCV 的視窗

while True:
    k = cv2.waitKey(0)  # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(k)  # 將 ASCII 代碼轉換成真實字元
    print(c, k)  # 印出結果
    if k == ESC:
        break  # 如果代碼等於 ESC(27)，結束迴圈

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 隨機生成
points = np.random.randint(100, 200, (10, 2), np.int32)
# print(points)
