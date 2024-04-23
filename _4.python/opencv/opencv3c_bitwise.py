"""

cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
cv2.bitwise_xor(a,b)
cv2.bitwise_or(a,b)
cv2.bitwise_not(a)


"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
a = cv2.imread(filename, 0)  # 通道不同

b = np.zeros(a.shape, dtype=np.uint8)  # 與a一樣大的黑圖
b[100:400, 200:400] = 255  # 某塊做mask
b[100:500, 100:200] = 255  # 某塊做mask

print("顯示原圖與mask作用後的圖")
c = cv2.bitwise_and(a, b)  # ab都成立的 擷取出來
print("a.shape=", a.shape)
print("b.shape=", b.shape)

plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("mask")
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("顯示原圖與mask作用後的圖")
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

plt.show()


print("------------------------------------------------------------")  # 60個

plt.figure("mask", figsize=(16, 12))

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 三維 1
a = cv2.imread(filename, 1)  # 通道不同
# w, h, c = a.shape
print(a.shape)

plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

mask = np.zeros(a.shape, dtype=np.uint8)  # 與a一樣大的黑圖 三維mask
print(mask.shape)
#     y       x
mask[30:170, 30:270] = 255  # 某塊做mask
mask[30:370, 80:220] = 255  # 某塊做mask

plt.subplot(132)
plt.title("mask")
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))

print("顯示原圖與mask作用後的圖")
c = cv2.bitwise_and(a, mask)  # a mask都成立的 擷取出來 #三維XOR
print("a.shape=", a.shape)
print("mask.shape=", mask.shape)

plt.subplot(133)
plt.title("顯示原圖與mask作用後的圖")
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個


# 異或加密解密
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
# filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 三維 1
lena = cv2.imread(filename, 1)  # 以下程式只能處理灰階 因為xor操作維度錯誤
print(lena.shape)

# 一維 0
lena = cv2.imread(filename, 0)  # 以下程式只能處理灰階 因為xor操作維度錯誤
print(lena.shape)

cc = lena.shape
print(cc)

key = np.random.randint(0, 256, size=[cc[0], cc[1]], dtype=np.uint8)
encryption = cv2.bitwise_xor(lena, key)
decryption = cv2.bitwise_xor(encryption, key)

plt.figure("new01", figsize=(16, 12))
plt.subplot(141)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(142)
plt.title("key")
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(143)
plt.title("encryption")
plt.imshow(cv2.cvtColor(encryption, cv2.COLOR_BGR2RGB))

plt.subplot(144)
plt.title("decryption")
plt.imshow(cv2.cvtColor(decryption, cv2.COLOR_BGR2RGB))

plt.suptitle("XOR 加密解密")
plt.show()

print("------------------------------------------------------------")  # 60個


# 讀取原始載體圖像
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
lena = cv2.imread(filename, 0)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/watermark.bmp"
# 讀取水印圖像
watermark = cv2.imread(filename, 0)
print("顯示原圖")

# 將水印內的255處理為1，以方便嵌入
# 后續章節會介紹使用threshold處理。
w = watermark[:, :] > 0
watermark[w] = 1
# 讀取原始載體圖像的shape值
r, c = lena.shape
# ============嵌入過程============
# 生成內部值都是254的數組
t254 = np.ones((r, c), dtype=np.uint8) * 254
# 獲取lena圖像的高7位
lenaH7 = cv2.bitwise_and(lena, t254)
# 將watermark嵌入到lenaH7內
e = cv2.bitwise_or(lenaH7, watermark)
# ============提取過程============
# 生成內部值都是1的數組
t1 = np.ones((r, c), dtype=np.uint8)
# 從載體圖像內，提取水印圖像
wm = cv2.bitwise_and(e, t1)
print(wm)
# 將水印內的1處理為255以方便顯示
# 后續章節會介紹threshold實現。
w = wm[:, :] > 0
wm[w] = 255

plt.figure("new02", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("watermark")
# 當前watermark內最大值為1
plt.imshow(cv2.cvtColor(watermark * 255, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("e")
plt.imshow(cv2.cvtColor(e, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("wm")
plt.imshow(cv2.cvtColor(wm, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

# 讀取原始載體圖像
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
lena = cv2.imread(filename, 0)

# 讀取原始載體圖像的shape值
r, c = lena.shape
mask = np.zeros((r, c), dtype=np.uint8)
mask[220:400, 250:350] = 1
# 獲取一個key,打碼、解碼所使用的密鑰
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
# ============獲取打碼臉============
# 使用密鑰key加密原始圖像lena
lenaXorKey = cv2.bitwise_xor(lena, key)
# 獲取加密圖像的臉部信息encryptFace
encryptFace = cv2.bitwise_and(lenaXorKey, mask * 255)
# 將圖像lena內的臉部值設置為0，得到noFace1
noFace1 = cv2.bitwise_and(lena, (1 - mask) * 255)
# 得到打碼的lena圖像
maskFace = encryptFace + noFace1
# ============將打碼臉解碼============
# 將臉部打碼的lena與密鑰key異或，得到臉部的原始信息
extractOriginal = cv2.bitwise_xor(maskFace, key)
# 將解碼的臉部信息extractOriginal提取出來得到extractFace
extractFace = cv2.bitwise_and(extractOriginal, mask * 255)
# 從臉部打碼的lena內提取沒有臉部信息的lena圖像，得到noFace2
noFace2 = cv2.bitwise_and(maskFace, (1 - mask) * 255)
# 得到解碼的lena圖像
extractLena = noFace2 + extractFace

plt.figure("new03", figsize=(16, 12))
plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("mask")
plt.imshow(cv2.cvtColor(mask * 255, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title("1-mask")
plt.imshow(cv2.cvtColor((1 - mask) * 255, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("key")
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("lenaXorKey")
plt.imshow(cv2.cvtColor(lenaXorKey, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("encryptFace")
plt.imshow(cv2.cvtColor(encryptFace, cv2.COLOR_BGR2RGB))

plt.show()

plt.figure("new04", figsize=(16, 12))

plt.subplot(231)
plt.title("noFace1")
plt.imshow(cv2.cvtColor(noFace1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("maskFace")
plt.imshow(cv2.cvtColor(maskFace, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title("extractOriginal")
plt.imshow(cv2.cvtColor(extractOriginal, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("extractFace")
plt.imshow(cv2.cvtColor(extractFace, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("noFace2")
plt.imshow(cv2.cvtColor(noFace2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("extractLena")
plt.imshow(cv2.cvtColor(extractLena, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

# 圖層提取
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
lena = cv2.imread(filename, 0)

print("顯示原圖")

plt.figure("new05", figsize=(16, 12))
plt.subplot(331)
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))
plt.title("原圖")

r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i

r = np.zeros((r, c, 8), dtype=np.uint8)

for i in range(8):
    print(i)
    r[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
    mask = r[:, :, i] > 0
    r[mask] = 255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(r[:, :, i], cv2.COLOR_BGR2RGB))
    plt.title(str(i))

plt.show()

print("------------------------------------------------------------")  # 60個


# filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'
filename = "C:/_git/vcs/_1.data/______test_files1/_opencv/opencv.png"
image = cv2.imread(filename)

print("原圖 BGR 轉 HSV")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# =============指定藍色值的范圍=============
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
# 確定藍色區域
mask = cv2.inRange(hsv, minBlue, maxBlue)
# 通過掩碼控制的按位與，鎖定藍色區域
blue = cv2.bitwise_and(image, image, mask=mask)

# =============指定綠色值的范圍=============
minGreen = np.array([50, 50, 50])
maxGreen = np.array([70, 255, 255])
# 確定綠色區域
mask = cv2.inRange(hsv, minGreen, maxGreen)
# 通過掩碼控制的按位與，鎖定綠色區域
green = cv2.bitwise_and(image, image, mask=mask)

# =============指定紅色值的范圍=============
minRed = np.array([0, 50, 50])
maxRed = np.array([30, 255, 255])
# 確定紅色區域
mask = cv2.inRange(hsv, minRed, maxRed)
# 通過掩碼控制的按位與，鎖定紅色區域
red = cv2.bitwise_and(image, image, mask=mask)

plt.figure("new34 影像處理", figsize=(16, 12))
plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("HSV")
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))

# plt.subplot(233)
# plt.title('')

plt.subplot(234)
plt.title("R")
plt.imshow(cv2.cvtColor(red, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("G")
plt.imshow(cv2.cvtColor(green, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("B")
plt.imshow(cv2.cvtColor(blue, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lesson2.jpg"
img = cv2.imread(filename)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask=mask)

plt.figure("new35 影像處理", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("ROI")
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

print("將圖片顏色反轉 (負片效果) 原圖")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

img = cv2.imread(filename)

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("將圖片顏色反轉 (負片效果) 效果")
img_invert = cv2.bitwise_not(img)

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_invert, cv2.COLOR_BGR2RGB))
plt.title("負片效果")

plt.show()

print("------------------------------------------------------------")  # 60個

print("遮罩")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
img = cv2.imread(filename)
H = img.shape[0]
W = img.shape[1]
mask = cv2.imread(r"images/mask.jpg", cv2.IMREAD_GRAYSCALE)
# 調整mask大小
mask = cv2.resize(mask, (W, H))
img_masked = cv2.bitwise_and(img, img, mask=mask)

plt.subplot(121)
plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果")

print("遮罩")

mask = cv2.bitwise_not(mask)
img_masked = cv2.bitwise_and(img, img, mask=mask)

plt.subplot(122)
plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果")

plt.show()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

output = cv2.bitwise_and(img1, img2)  # 使用 bitwise_and

cv2.imshow("image", output)
cv2.waitKey(0)  # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

output = cv2.bitwise_or(img1, img2)  # 使用 bitwise_or

cv2.imshow("image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

output = cv2.bitwise_xor(img1, img2)  # 使用 bitwise_xor

cv2.imshow("image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
img1 = cv2.imread(filename1)

output = cv2.bitwise_not(img1)  # 使用 bitwise_not

cv2.imshow("image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" TBD
filename1 = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.png'
filename2 = 'C:/_git/vcs/_4.python/opencv/data/RGB_G.png'
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

H = img1.shape[0]
W = img1.shape[1]

mask = cv2.imread('mask.png')                    # 遮罩圖片

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)    # 轉換成灰階模式
output = cv2.bitwise_xor(img1, img2, mask=mask)  # 加入 mask 參數

cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_29")

""" TBD
logo_filename = 'C:/_git/vcs/_4.python/opencv/data/opencv_logo.png'

logo = cv2.imread(logo_filename)                    # 讀取 OpenCV 的 logo
size = logo.shape                                # 讀取 logo 的長寬尺寸

img = np.zeros((360,480,3), dtype='uint8')       # 產生一張 480x360 背景全黑的圖
img[0:360, 0:480] = '255'                        # 將圖片變成白色 ( 配合 logo 是白色底 )
img[0:size[0], 0:size[1]] = logo                 # 將圖片的指定區域，換成 logo 的圖案
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 產生一張灰階的圖片作為遮罩使用
ret, mask1  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)  # 使用二值化的方法，產生黑白遮罩圖片
logo = cv2.bitwise_and(img, img, mask = mask1 )  # logo 套用遮罩

bg = cv2.imread(filename)                      # 讀取底圖
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)      # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask = mask2 )      # 底圖套用遮罩

output = cv2.add(bg, logo)                       # 使用 add 方法將底圖和 logo 合併

cv2.imshow('image', output)

cv2.waitKey()
cv2.destroyAllWindows()

"""

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_49")

lower = np.array([30, 40, 200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90, 100, 255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
img = cv2.imread(filename)

mask = cv2.inRange(img, lower, upper)  # 使用 inRange
output = cv2.bitwise_and(img, img, mask=mask)  # 套用影像遮罩
cv2.imwrite("tmp_output.jpg", output)

cv2.imshow("Image", output)
cv2.waitKey(0)  # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

"""
彩色影像轉HSV(RGB to HSV 或 BGR to HSV)

HSV簡單介紹分別為：
色相(H)：色彩的顏色名稱，如紅色、黃色等。
飽和度(S)：色彩的純度，越高色彩越純，低則逐漸變灰，數值為0-100%。
明度(V)：亮度，數值為0-100%。

使用 cv2.cvtColor 轉換顏色空間時，第二個參數與HSV相關的有：
cv2.COLOR_BGR2HSV
cv2.COLOR_HSV2BGR
cv2.COLOR_RGB2HSV
cv2.COLOR_HSV2RGB

opencv 預設的排列方式為BGR，而不是RGB

所以這邊使用的是 cv2.COLOR_BGR2HSV

當然實際上使用時不會只是單純RGB轉換成HSV就結束了，
通常會去針對HSV顏色區間去作後續的處理

範例. 物件偵測 - 找出綠色的物體

彩色轉HSV常見的應用可能有物件偵測，去背處理(排除綠色的背景)，
以下就來示範如何找出圖片中綠色的水果，類似的應用可能有找出草地的背景，

"""
image = cv2.imread("data/fruit.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

fig = plt.figure(
    num="彩色影像轉HSV",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))
plt.title("轉HSV")

lower_green = np.array([35, 43, 46])  # 綠色下限
upper_green = np.array([77, 255, 255])  # 綠色上限
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(133)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title("抓出綠色的部分")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
