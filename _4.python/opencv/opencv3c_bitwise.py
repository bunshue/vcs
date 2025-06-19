"""
影像的位元運算(4)
cv2.bitwise_and()
cv2.bitwise_or()
cv2.bitwise_not()
cv2.bitwise_xor() 異或

"""

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

mask_filename = "C:/_git/vcs/_4.python/opencv/data/_mask/mask1.png"

from opencv_common import *

print("------------------------------------------------------------")  # 60個

# 灰階/彩色 mask 運算

plt.figure(figsize=(12, 8))

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階
plt.subplot(4, 3, 1)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("原圖")

mask = np.zeros(src.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360] = 255  # 設定mask, 先高後寬
plt.subplot(4, 3, 2)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("mask")

dst = cv2.bitwise_and(src, mask)  # 執行AND運算
plt.subplot(4, 3, 3)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("AND")

src = cv2.imread(filename2)  # 彩色
plt.subplot(4, 3, 4)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("原圖")

mask = np.zeros(src.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列
plt.subplot(4, 3, 5)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("mask")

dst = cv2.bitwise_and(src, mask)  # 執行AND運算
plt.subplot(4, 3, 6)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("AND")

src = cv2.imread(filename2)  # 彩色
plt.subplot(4, 3, 7)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("原圖")

mask = np.zeros(src.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列
plt.subplot(4, 3, 8)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("mask")

dst = cv2.bitwise_or(src, mask)  # 執行OR運算
plt.subplot(4, 3, 9)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("OR")

# ------------------------------------------------------------


# ------------------------------------------------------------

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)

# 建立mask
height, width = image.shape[:2]
mask = np.zeros(image.shape[:2], np.uint8)
mask[height // 8 : 7 * height // 8, width // 8 : 7 * width // 8] = 255

# 讀取圖檔做mask
mask_filename = "C:/_git/vcs/_4.python/opencv/data/_mask/mask1.png"
mask = cv2.imread(mask_filename, 0)
mask = cv2.resize(mask, (width, height))  # 調整mask大小

# 套用mask
masked_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.bitwise_xor() ST
print("------------------------------------------------------------")  # 60個

# XOR 加密解密

src = cv2.imread(filename1, 0)  # 灰階
src = cv2.imread(filename1)  # 彩色

key = np.random.randint(0, 256, size=src.shape, dtype=np.uint8)  # 密鑰影像
encryption = cv2.bitwise_xor(src, key)  # 執行XOR運算
decryption = cv2.bitwise_xor(encryption, key)  # 執行XOR運算

plt.figure(figsize=(12, 8))
plt.subplot(141)
plt.title("原圖, 灰階/彩色")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))

plt.subplot(142)
plt.title("密鑰影像")
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(143)
plt.title("加密")
plt.imshow(cv2.cvtColor(encryption, cv2.COLOR_BGR2RGB))

plt.subplot(144)
plt.title("解密")
plt.imshow(cv2.cvtColor(decryption, cv2.COLOR_BGR2RGB))

plt.suptitle("XOR 加密解密")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
src = cv2.imread(filename, 0)

mask1 = np.zeros(src.shape, dtype=np.uint8)  # 建立mask
mask1[220:400, 220:380] = 1  # 設定mask, 先高後寬  # 建立mask白色區塊

# 獲取一個key,打碼、解碼所使用的密鑰
key = np.random.randint(0, 256, size=src.shape, dtype=np.uint8)

# ============獲取打碼臉============
# 使用密鑰key加密原始圖像lena
lenaXorKey = cv2.bitwise_xor(src, key)  # 執行XOR運算

# 獲取加密圖像的臉部信息encryptFace
encryptFace = cv2.bitwise_and(lenaXorKey, mask1 * 255)  # 執行AND運算

# 將圖像lena內的臉部值設置為0，得到noFace1
mask2 = 1 - mask1
noFace1 = cv2.bitwise_and(src, mask2 * 255)  # 執行AND運算

# 得到打碼的lena圖像
maskFace = encryptFace + noFace1

# ============將打碼臉解碼============
# 將臉部打碼的lena與密鑰key XOR，得到臉部的原始信息
extractOriginal = cv2.bitwise_xor(maskFace, key)  # 執行XOR運算

# 將解碼的臉部信息extractOriginal提取出來得到extractFace
extractFace = cv2.bitwise_and(extractOriginal, mask1 * 255)  # 執行AND運算

# 從臉部打碼的lena內提取沒有臉部信息的lena圖像，得到noFace2
noFace2 = cv2.bitwise_and(maskFace, mask2 * 255)  # 執行AND運算

# 得到解碼的lena圖像
extractLena = noFace2 + extractFace

plt.figure(figsize=(12, 10))
plt.subplot(341)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))

plt.subplot(342)
plt.title("建立mask1")
plt.imshow(cv2.cvtColor(mask1 * 255, cv2.COLOR_BGR2RGB))

plt.subplot(343)
plt.title("建立mask2=mask1反相")
plt.imshow(cv2.cvtColor(mask2 * 255, cv2.COLOR_BGR2RGB))

plt.subplot(344)
plt.title("建立密鑰影像")
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(345)
plt.title("全圖加密")
plt.imshow(cv2.cvtColor(lenaXorKey, cv2.COLOR_BGR2RGB))

plt.subplot(346)
plt.title("全圖加密+mask1取一部份出來")
plt.imshow(cv2.cvtColor(encryptFace, cv2.COLOR_BGR2RGB))

plt.subplot(347)
plt.title("原圖+mask2")
plt.imshow(cv2.cvtColor(noFace1, cv2.COLOR_BGR2RGB))

plt.subplot(348)
plt.title("前兩圖相加")
plt.imshow(cv2.cvtColor(maskFace, cv2.COLOR_BGR2RGB))

plt.subplot(349)
plt.title("上圖XOR密鑰影像")
plt.imshow(cv2.cvtColor(extractOriginal, cv2.COLOR_BGR2RGB))

plt.subplot(3, 4, 10)
plt.title("上圖+mask1")
plt.imshow(cv2.cvtColor(extractFace, cv2.COLOR_BGR2RGB))

plt.subplot(3, 4, 11)
plt.title("圖8+mask2")
plt.imshow(cv2.cvtColor(noFace2, cv2.COLOR_BGR2RGB))

plt.subplot(3, 4, 12)
plt.title("前兩圖相加 得到 原圖")
plt.imshow(cv2.cvtColor(extractLena, cv2.COLOR_BGR2RGB))

show()

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
# cv2.bitwise_xor() SP
print("------------------------------------------------------------")  # 60個

# 讀取原圖
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
src = cv2.imread(filename, 0)

# 讀取水印圖像
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/watermark.bmp"
watermark = cv2.imread(filename, 0)

# 將水印內的255處理為1，以方便嵌入
# 后續章節會介紹使用threshold處理。
w = watermark[:, :] > 0
watermark[w] = 1

# ============嵌入過程============
# 生成內部值都是254的數組
t254 = np.ones(src.shape, dtype=np.uint8) * 254
# 獲取lena圖像的高7位
lenaH7 = cv2.bitwise_and(src, t254)  # 執行AND運算
# 將watermark嵌入到lenaH7內
e = cv2.bitwise_or(lenaH7, watermark)  # 執行OR運算
# ============提取過程============
# 生成內部值都是1的數組
t1 = np.ones(src.shape, dtype=np.uint8)
# 從載體圖像內，提取水印圖像
wm = cv2.bitwise_and(e, t1)  # 執行AND運算
print(wm)
# 將水印內的1處理為255以方便顯示
# 后續章節會介紹threshold實現。
w = wm[:, :] > 0
wm[w] = 255

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 圖層提取
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
src = cv2.imread(filename, 0)

print("顯示原圖")

plt.figure(figsize=(12, 8))
plt.subplot(331)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

r, c = src.shape
x = np.zeros((r, c, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i

r = np.zeros((r, c, 8), dtype=np.uint8)

for i in range(8):
    print(i)
    r[:, :, i] = cv2.bitwise_and(src, x[:, :, i])  # 執行AND運算
    mask = r[:, :, i] > 0
    r[mask] = 255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(r[:, :, i], cv2.COLOR_BGR2RGB))
    plt.title(str(i))

plt.suptitle("圖層提取")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.bitwise_not() ST
print("------------------------------------------------------------")  # 60個

print("將圖片顏色反轉 (負片效果)")

src = cv2.imread(filename2)

dst = cv2.bitwise_not(src)  # 執行NOT運算

plt.subplot(231)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("NOT 負片效果")

src = cv2.imread(filename2)

mask = np.zeros(src.shape, np.uint8)  # 建立mask
mask[:, 140:360, :] = 255  # 設定mask, 先高後寬  # 建立mask白色區塊

dst = cv2.bitwise_xor(src, mask)  # 執行XOR運算

plt.subplot(234)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("原圖")

plt.subplot(235)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("mask")

plt.subplot(236)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("NOT")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("遮罩")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
img = cv2.imread(filename)
plt.subplot(221)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

H = img.shape[0]
W = img.shape[1]
mask = cv2.imread(r"images/mask.jpg", cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, (W, H))  # 調整mask大小

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

img_masked = cv2.bitwise_and(img, img, mask=mask)  # 執行AND運算, 使用mask

plt.subplot(223)
plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果")

print("遮罩")

mask = cv2.bitwise_not(mask)  # 執行NOT運算
img_masked = cv2.bitwise_and(img, img, mask=mask)  # 執行AND運算, 使用mask

plt.subplot(224)
plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果")

show()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

output1 = cv2.bitwise_and(img1, img2)  # 執行AND運算
output2 = cv2.bitwise_or(img1, img2)  # 執行OR運算
output3 = cv2.bitwise_xor(img1, img2)  # 執行XOR運算

plt.subplot(231)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("img1")

plt.subplot(232)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("img2")

plt.subplot(233)
plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
plt.title("AND")

plt.subplot(234)
plt.imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
plt.title("OR")

plt.subplot(235)
plt.imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
plt.title("XOR")

show()

print("------------------------------------------------------------")  # 60個
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
output = cv2.bitwise_xor(img1, img2, mask=mask)  # 執行XOR運算, 使用mask

cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
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
logo = cv2.bitwise_and(img, img, mask = mask1 )  # 執行AND運算  # logo 套用遮罩

bg = cv2.imread(filename)                      # 讀取底圖
ret, mask2  = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)      # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask = mask2 )  # 執行AND運算      # 底圖套用遮罩

output = cv2.add(bg, logo)                       # 使用 add 方法將底圖和 logo 合併

cv2.imshow('image', output)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("bitwise_and")

src1 = np.array([[255, 0, 255]])
src2 = np.array([[255, 0, 0]])

# AND運算
dst_and = cv2.bitwise_and(src1, src2)  # 執行AND運算
print("AND運算 的 結果：")
print(dst_and)

print("------------------------------------------------------------")  # 60個

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)

src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255  # 設定mask, 先高後寬

dst = cv2.bitwise_and(src1, src2)  # 執行AND運算

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("bitwise_or")

src1 = np.array([[255, 0, 255]])
src2 = np.array([[255, 0, 0]])

# OR運算
dst_or = cv2.bitwise_or(src1, src2)  # 執行OR運算
print("OR運算 的 結果：")
print(dst_or)

src1 = np.random.randint(0, 255, (3, 5), dtype=np.uint8)

src2 = np.zeros((3, 5), dtype=np.uint8)
src2[0:2, 0:2] = 255  # 設定mask, 先高後寬

dst = cv2.bitwise_or(src1, src2)  # 執行OR運算

print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在影像中藏入訊息

src = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)

h7 = np.ones(src.shape, dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_src = cv2.bitwise_and(src, h7)  # 原始影像最低有效位元是 0

watermark = cv2.imread("data/peony.jpg", cv2.IMREAD_GRAYSCALE)

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

# 浮水印影像嵌入 最低有效位元是0 的 原始影像
new_src = cv2.bitwise_or(tmp_src, wm)

# 擷取浮水印
h0 = np.ones(src.shape, dtype=np.uint8)
wm = cv2.bitwise_and(new_src, h0)
ret, dst = cv2.threshold(wm, 0, 255, cv2.THRESH_BINARY)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(222)
plt.title("浮水印")
plt.imshow(cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(223)
plt.title("浮水印影像嵌入")
plt.imshow(cv2.cvtColor(new_src, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(224)
plt.title("顯示浮水印")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")

show()

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


# cv2.imwrite("tmp_output.jpg", output)
