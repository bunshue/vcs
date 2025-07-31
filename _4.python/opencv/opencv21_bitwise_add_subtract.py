"""
cv2.add() : 兩圖用cv相加
cv2.addWeighted()  # 加權和, 要一樣大的圖
cv2.subtract()

影像的位元運算(4) AND OR NOT XOR ST
cv2.bitwise_and()
cv2.bitwise_or()
cv2.bitwise_not()
cv2.bitwise_xor() 異或

# 加權和 alpha beta gamma
cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
src1, src2：一樣大的影像
alpha：src1的权重
beta：src2的权重
gamma：gamma修正系数，不需要修正设置为0, 整體墊高值
dst：可选参数
dtype：可选参数
"""
from opencv_common import *

print("------------------------------------------------------------")  # 60個
# cv2.add() cv2.addWeighted() cv2.subtract() ST
print("------------------------------------------------------------")  # 60個

add_filename1 = "C:/_git/vcs/_4.python/_data/picture_add1.bmp"
add_filename2 = "C:/_git/vcs/_4.python/_data/picture_add2.bmp"

image1 = cv2.imread(add_filename1)  # 彩色讀取
image2 = cv2.imread(add_filename2)  # 彩色讀取

print("兩圖直接相加")
result1 = image1 + image2

print("cv2.add():兩圖用cv相加")
result2 = cv2.add(image1, image2)

print("兩圖做比例疊加 左1.0 右1.0")
print("cv2.addWeighted():兩圖用cv比例疊加")
result3a = cv2.addWeighted(image1, 1.0, image2, 1.0, 0)  # 整體墊高值 0
result3b = cv2.addWeighted(image1, 1.0, image2, 1.0, 100)  # 整體墊高值100

plt.figure(num="相加", figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(233)
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))
plt.title("兩圖直接相加")

plt.subplot(234)
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))
plt.title("兩圖用cv相加")

plt.subplot(235)
plt.imshow(cv2.cvtColor(result3a, cv2.COLOR_BGR2RGB))
plt.title("兩圖做比例疊加 左1.0 右1.0")

plt.subplot(236)
plt.imshow(cv2.cvtColor(result3b, cv2.COLOR_BGR2RGB))
plt.title("兩圖做比例疊加 左1.0 右1.0 整體墊高100")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 灰階/彩色影像相加, 變得更白/更亮
# 用相加的，像素值會破表

# 製作影像
W, H = 100, 100
image1 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)
image2 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)

# 真實影像
image1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image2 = image1

# 像素值直接相加會破表
res1 = image1 + image2

print("cv2.add():兩圖用cv相加")
res2 = cv2.add(image1, image2)

plt.figure(num="兩圖相加", figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(223)
plt.imshow(cv2.cvtColor(res1, cv2.COLOR_BGR2RGB))
plt.title("兩圖 +")

plt.subplot(224)
plt.imshow(cv2.cvtColor(res2, cv2.COLOR_BGR2RGB))
plt.title("兩圖 cv2.add")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 淡入淡出 效果")
print("按 ESC 離開")

image = cv2.imread(filename1)  # 彩色讀取
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = image.shape[1]  # 取得寬度
h = image.shape[0]  # 取得高度
white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 建立白色圖
a = 1  # 一開始 a 為 1

while True:
    a = a - 0.005  # a 不斷減少 0.001
    if a < 0:
        a = 0  # a最小為0
    # print("cv2.addWeighted():兩圖用cv比例疊加")
    output = cv2.addWeighted(white, a, image, 1 - a, 0)  # 根據 a 套用權重
    cv2.imshow("image", output)  # 顯示圖片
    k = cv2.waitKey(1)
    if k == ESC:
        break

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("兩圖相減")

compare_filename1 = "data/_compare/diffb1.jpg"
compare_filename2 = "data/_compare/diffb2.jpg"

image1 = cv2.imread(compare_filename1)  # 彩色讀取
image2 = cv2.imread(compare_filename2)  # 彩色讀取

# image3 = math.fabs(image1-image2)
image3 = image1 - image2

print("cv2.subtract():兩圖用cv相減")
image4 = cv2.subtract(image1, image2)  # 相減

plt.figure(num="兩圖相減1", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減 -")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減 cv2.subtract")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("用 cv2.add() 做 亮度調整")

# 影像計算 影像相加 cv2.add

image1 = cv2.imread(filename2)  # 彩色讀取

value = 60  # 亮度調整值
coff = np.ones(image1.shape, dtype=np.uint8) * value
res1 = cv2.add(image1, coff)  # 調整亮度結果

value = 120  # 亮度調整值
coff = np.ones(image1.shape, dtype=np.uint8) * value
res2 = cv2.add(image1, coff)  # 調整亮度結果

value = 180  # 亮度調整值
coff = np.ones(image1.shape, dtype=np.uint8) * value
res3 = cv2.add(image1, coff)  # 調整亮度結果

plt.figure(num="兩圖相加", figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(res1, cv2.COLOR_BGR2RGB))
plt.title("亮度+60")

plt.subplot(223)
plt.imshow(cv2.cvtColor(res2, cv2.COLOR_BGR2RGB))
plt.title("亮度+120")

plt.subplot(224)
plt.imshow(cv2.cvtColor(res3, cv2.COLOR_BGR2RGB))
plt.title("亮度+180")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

b = np.zeros((height, width, 3), np.uint8)  # b影像
g = np.zeros((height, width, 3), np.uint8)  # g影像
r = np.zeros((height, width, 3), np.uint8)  # r影像
b[:, :, 0] = 255  # 設定藍色
g[:, :, 1] = 255  # 設定綠色
r[:, :, 2] = 255  # 設定紅色

print("cv2.add():兩圖用cv相加")
img1 = cv2.add(b, g)  # b + g影像
img2 = cv2.add(g, r)  # g + r影像
img3 = cv2.add(img1, r)  # b + g + r影像

plt.subplot(231)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("B+G=天青")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("G+R=黃")
plt.axis("off")

plt.subplot(236)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("B+G+R=白")
plt.axis("off")

show()

""" size error
# 製作mask
# mask = np.zeros((4, 5), dtype=np.uint8)
mask = np.zeros((height, width, 3), np.uint8)
mask[100:300, 100:, -1] = 255  # 設定mask, 先高後寬

print("cv2.add():兩圖用cv相加+mask")
img4 = cv2.add(b, g, mask=mask)  # b + g影像 + mask

cv2.imshow("img4", img4)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 影像相加 影像取mask

img1 = np.ones((4, 5), dtype=np.uint8) * 8
img2 = np.ones((4, 5), dtype=np.uint8) * 9

# 製作mask
mask = np.zeros((4, 5), dtype=np.uint8)
mask[1:3, 1:4] = 255  # 設定mask, 先高後寬

print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)

print("cv2.add():兩圖用cv相加+mask")
dst = cv2.add(img1, img2, mask=mask)
print("結果值 dst =\n", dst)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

img1 = np.zeros((height, width, 3), np.uint8)  # 建立img1影像
img1[:, :, 2] = 255  # 紅色

img2 = np.zeros((height, width, 3), np.uint8)  # 建立img2影像
img2[:, :, 1] = 255  # 綠色

# 製作mask
mask = np.zeros((height, width, 1), np.uint8)  # 建立mask影像
mask[50:350, 100:300, :] = 255  # 建立 ROI, 白色

print("cv2.add():兩圖用cv相加")
img3 = cv2.add(img1, img2)  # 不含mask的影像相加

# 使用cv2.add相加, 使用mask
print("cv2.add():兩圖用cv相加+mask")
img4 = cv2.add(img1, img2, mask=mask)  # 含mask的影像相加

plt.subplot(231)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("R")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("R+G by cv2.add")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
plt.title("R+G+mask by cv2.add")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.addWeighted():兩圖用cv比例疊加")

# 製作影像
W, H = 10, 5

image1 = np.ones((H, W), dtype=np.uint8) * 100  # 全值影像
print(f"image1 = \n {image1}")

image2 = np.ones((H, W), dtype=np.uint8) * 200  # 全值影像
print(f"image2 = \n {image2}")

# 真實影像

filename_rgb_r = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename_rgb_g = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

image1 = cv2.imread(filename_rgb_r)  # 彩色讀取
image2 = cv2.imread(filename_rgb_g)  # 彩色讀取

alpha = 0.5
beta = 0.5
gamma = 10  # 整體墊高值 10
dst = cv2.addWeighted(image1, alpha, image2, beta, gamma)  # 加權和
# print(f"dst = \n {dst}")

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("權重疊合影像")

plt.suptitle("addWeighted")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.add() cv2.addWeighted() cv2.subtract() SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# 影像的位元運算(4) AND OR NOT XOR ST
# cv2.bitwise_and()
# cv2.bitwise_or()
# cv2.bitwise_not()
# cv2.bitwise_xor() 異或
print("------------------------------------------------------------")  # 60個

# 灰階/彩色 mask 運算

plt.figure(figsize=(12, 8))

image = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.subplot(4, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

mask = np.zeros(image.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360] = 255  # 設定mask, 先高後寬
plt.subplot(4, 3, 2)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")
plt.axis("off")

dst = cv2.bitwise_and(image, mask)  # 執行AND運算
plt.subplot(4, 3, 3)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("AND")
plt.axis("off")

image = cv2.imread(filename2)  # 彩色讀取

plt.subplot(4, 3, 4)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

mask = np.zeros(image.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列
plt.subplot(4, 3, 5)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")
plt.axis("off")

dst = cv2.bitwise_and(image, mask)  # 執行AND運算
plt.subplot(4, 3, 6)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("AND")
plt.axis("off")

image = cv2.imread(filename2)  # 彩色讀取

plt.subplot(4, 3, 7)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

mask = np.zeros(image.shape, dtype=np.uint8)  # 建立mask
mask[50:520, 150:360, :] = 255  # 設定mask, 先高後寬  # 這是3維陣列
plt.subplot(4, 3, 8)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")
plt.axis("off")

dst = cv2.bitwise_or(image, mask)  # 執行OR運算

plt.subplot(4, 3, 9)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("OR")
plt.axis("off")

# ------------------------------------------------------------


# ------------------------------------------------------------

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# 建立mask
height, width = image.shape[:2]
mask = np.zeros(image.shape[:2], np.uint8)
mask[height // 8 : 7 * height // 8, width // 8 : 7 * width // 8] = 255

# 讀取圖檔做mask
mask_filename = "C:/_git/vcs/_4.python/opencv/data/_mask/mask1.png"
mask = cv2.imread(mask_filename, 0)  # 0, 灰階讀取
mask = cv2.resize(mask, (width, height))  # 調整mask大小

plt.subplot(132)
# 當前watermark內最大值為1
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

# 套用mask
masked_image = cv2.bitwise_and(image, image, mask=mask)  # 執行AND運算, 使用mask

plt.subplot(133)
plt.imshow(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB))
plt.title("masked_image")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("遮罩")

image = cv2.imread(filename2)  # 彩色讀取

H = image.shape[0]
W = image.shape[1]

mask = cv2.imread(r"images/mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask = cv2.resize(mask, (W, H))  # 調整mask大小

# 直接使用遮罩
image_masked1 = cv2.bitwise_and(image, image, mask=mask)  # 執行AND運算, 使用mask

# 反相使用遮罩
mask = cv2.bitwise_not(mask)  # 執行NOT運算
image_masked2 = cv2.bitwise_and(image, image, mask=mask)  # 執行AND運算, 使用mask

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image_masked1, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果 bitwise_and")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image_masked2, cv2.COLOR_BGR2RGB))
plt.title("遮罩效果 bitwise_not")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("執行AND運算, 使用mask")

W, H, D = 5, 5, 3
image = np.ones([H, W], dtype=np.uint8) * 9

mask = np.zeros([H, W], dtype=np.uint8)
mask[0:3, 0] = 1
mask[2:5, 2:4] = 1

roi = cv2.bitwise_and(image, image, mask=mask)  # 執行AND運算, 使用mask
print("image = \n", image)
print("mask = \n", mask)
print("roi = \n", roi)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# cv2.bitwise_and

image = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
row, column = image.shape  # 取得列高和欄寬

h100 = np.ones((row, column), dtype=np.uint8) * 100  # 建立像素值是100的影像

new_image = cv2.bitwise_and(image, h100)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(h100, cv2.COLOR_BGR2RGB))
plt.title("灰階100")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title("原圖取出灰階100")
plt.axis("off")

plt.suptitle("cv2.bitwise_and")
show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(12, 8))
plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

row, column = image.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重, 第0層1, 第2層2, ... 第7層2^7
    print(x[5, 5, i])

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(image, x[:, :, i])  # image AND 第i層
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(result[:, :, i], cv2.COLOR_BGR2RGB))
    plt.title(str(i))

plt.suptitle("圖層提取")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_29")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

logo = cv2.imread(logo_filename)  # 彩色讀取  # 讀取 OpenCV 的 logo
size = logo.shape  # 讀取 logo 的長寬尺寸
print(size)

W, H = 800, 531  # 大象圖
# 建立黑圖
image1 = np.zeros((H, W, 3), dtype="uint8")  # 產生一張 WxH 背景全黑的圖
# 塗色
image1[0:H, 0:W] = 255  # 將圖片變成白色
# 貼上logo
image1[0 : size[0], 0 : size[1]] = logo  # 將圖片的指定區域，換成 logo 的圖案

cv2.imshow("image", image1)
cv2.waitKey()
cv2.destroyAllWindows()

image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 產生一張灰階的圖片作為遮罩使用

ret, mask1 = cv2.threshold(
    image_gray, 200, 255, cv2.THRESH_BINARY_INV
)  # 使用二值化的方法，產生黑白遮罩圖片

cv2.imshow("image", mask1)
cv2.waitKey()
cv2.destroyAllWindows()

logo = cv2.bitwise_and(image1, image1, mask=mask1)  # 執行AND運算, 使用mask  # logo 套用遮罩

cv2.imshow("image", logo)
cv2.waitKey()
cv2.destroyAllWindows()

# 檔案問題 size

bg = cv2.imread(filename2)  # 彩色讀取  # 讀取底圖
ret, mask2 = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)  # 使用二值化的方法，產生黑白遮罩圖片
bg = cv2.bitwise_and(bg, bg, mask=mask2)  # 執行AND運算, 使用mask # 底圖套用遮罩

print("cv2.add():兩圖用cv相加")
output = cv2.add(bg, logo)  # 使用 add 方法將底圖和 logo 合併

cv2.imshow("image", output)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.bitwise_xor() ST
print("------------------------------------------------------------")  # 60個

# XOR 加密解密

image = cv2.imread(filename1, 0)  # 0, 灰階讀取
image = cv2.imread(filename1)  # 彩色讀取

# 建立密鑰影像
key = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)  # 製作密鑰影像, 同原圖大小

# 建立加密影像
encryption = cv2.bitwise_xor(image, key)  # 執行XOR運算

# 建立解密影像
decryption = cv2.bitwise_xor(encryption, key)  # 執行XOR運算

plt.figure(figsize=(12, 8))
plt.subplot(141)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖, 灰階/彩色")

plt.subplot(142)
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))
plt.title("密鑰影像")

plt.subplot(143)
plt.imshow(cv2.cvtColor(encryption, cv2.COLOR_BGR2RGB))
plt.title("加密影像")

plt.subplot(144)
plt.imshow(cv2.cvtColor(decryption, cv2.COLOR_BGR2RGB))
plt.title("解密影像")

plt.suptitle("XOR 加密解密")
show()


# 兩圖 XOR + mask, 要一樣長寬
# output = cv2.bitwise_xor(img1, img2, mask=mask)  # 執行XOR運算, 使用mask

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_lena_gray, 0)  # 0, 灰階讀取

mask1 = np.zeros(image.shape, dtype=np.uint8)  # 建立mask
mask1[220:400, 220:380] = 1  # 設定mask, 先高後寬  # 建立mask白色區塊

# 獲取一個key,打碼、解碼所使用的密鑰
key = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)

# ============獲取打碼臉============
# 使用密鑰key加密原始圖像lena
lenaXorKey = cv2.bitwise_xor(image, key)  # 執行XOR運算

# 獲取加密圖像的臉部信息encryptFace
encryptFace = cv2.bitwise_and(lenaXorKey, mask1 * 255)  # 執行AND運算

# 將圖像lena內的臉部值設置為0，得到noFace1
mask2 = 1 - mask1
noFace1 = cv2.bitwise_and(image, mask2 * 255)  # 執行AND運算

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

plt.figure(figsize=(12, 8))
plt.subplot(341)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(342)
plt.imshow(cv2.cvtColor(mask1 * 255, cv2.COLOR_BGR2RGB))
plt.title("建立mask1")

plt.subplot(343)
plt.imshow(cv2.cvtColor(mask2 * 255, cv2.COLOR_BGR2RGB))
plt.title("建立mask2=mask1反相")

plt.subplot(344)
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))
plt.title("建立密鑰影像")

plt.subplot(345)
plt.imshow(cv2.cvtColor(lenaXorKey, cv2.COLOR_BGR2RGB))
plt.title("全圖加密")

plt.subplot(346)
plt.imshow(cv2.cvtColor(encryptFace, cv2.COLOR_BGR2RGB))
plt.title("全圖加密+mask1取一部份出來")

plt.subplot(347)
plt.imshow(cv2.cvtColor(noFace1, cv2.COLOR_BGR2RGB))
plt.title("原圖+mask2")

plt.subplot(348)
plt.imshow(cv2.cvtColor(maskFace, cv2.COLOR_BGR2RGB))
plt.title("前兩圖相加")

plt.subplot(349)
plt.imshow(cv2.cvtColor(extractOriginal, cv2.COLOR_BGR2RGB))
plt.title("上圖XOR密鑰影像")

plt.subplot(3, 4, 10)
plt.imshow(cv2.cvtColor(extractFace, cv2.COLOR_BGR2RGB))
plt.title("上圖+mask1")

plt.subplot(3, 4, 11)
plt.imshow(cv2.cvtColor(noFace2, cv2.COLOR_BGR2RGB))
plt.title("圖8+mask2")

plt.subplot(3, 4, 12)
plt.imshow(cv2.cvtColor(extractLena, cv2.COLOR_BGR2RGB))
plt.title("前兩圖相加 得到 原圖")

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

image = cv2.imread(filename_lena_gray, 0)  # 0, 灰階讀取

# 讀取水印圖像
watermark_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/watermark.bmp"
)
watermark = cv2.imread(watermark_filename, 0)  # 0, 灰階讀取

# 將水印內的255處理為1，以方便嵌入
w = watermark[:, :] > 0
watermark[w] = 1

# ============嵌入過程============
# 生成內部值都是254的數組
t254 = np.ones(image.shape, dtype=np.uint8) * 254
# 獲取lena圖像的高7位
lenaH7 = cv2.bitwise_and(image, t254)  # 執行AND運算
# 將watermark嵌入到lenaH7內
e = cv2.bitwise_or(lenaH7, watermark)  # 執行OR運算
# ============提取過程============
# 生成內部值都是1的數組
t1 = np.ones(image.shape, dtype=np.uint8)
# 從載體圖像內，提取水印圖像
wm = cv2.bitwise_and(e, t1)  # 執行AND運算
print(wm)
# 將水印內的1處理為255以方便顯示
# 后續章節會介紹threshold實現。
w = wm[:, :] > 0
wm[w] = 255

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
# 當前watermark內最大值為1
plt.imshow(cv2.cvtColor(watermark * 255, cv2.COLOR_BGR2RGB))
plt.title("watermark")

plt.subplot(223)
plt.imshow(cv2.cvtColor(e, cv2.COLOR_BGR2RGB))
plt.title("e")

plt.subplot(224)
plt.imshow(cv2.cvtColor(wm, cv2.COLOR_BGR2RGB))
plt.title("wm")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在影像中藏入訊息

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

h7 = np.ones(image.shape, dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_image = cv2.bitwise_and(image, h7)  # 原始影像最低有效位元是 0

watermark = cv2.imread("data/peony.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

# 浮水印影像嵌入 最低有效位元是0 的 原始影像
new_image = cv2.bitwise_or(tmp_image, wm)  # 執行OR運算

# 擷取浮水印
h0 = np.ones(image.shape, dtype=np.uint8)
wm = cv2.bitwise_and(new_image, h0)
ret, dst = cv2.threshold(wm, 0, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB))
plt.title("浮水印")

plt.subplot(223)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title("浮水印影像嵌入")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("顯示浮水印")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.bitwise_not() ST
print("------------------------------------------------------------")  # 60個

print("將圖片顏色反轉 (負片效果)")

image = cv2.imread(filename2)  # 彩色讀取

# 全圖NOT =>全圖負片
dst = cv2.bitwise_not(image)  # 執行NOT運算

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("NOT 負片效果")

image = cv2.imread(filename2)  # 彩色讀取

mask = np.zeros(image.shape, np.uint8)  # 建立mask
mask[:, 140:360, :] = 255  # 設定mask, 先高後寬  # 建立mask白色區塊

# 只有mask部分做XOR => 部分負片
dst = cv2.bitwise_xor(image, mask)  # 執行XOR運算

plt.subplot(234)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(235)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(236)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("XOR 負片效果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

bitwise_filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
bitwise_filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
img1 = cv2.imread(bitwise_filename1)  # 彩色讀取
img2 = cv2.imread(bitwise_filename2)  # 彩色讀取

output0 = cv2.bitwise_not(img1)  # 執行NOT運算
output1 = cv2.bitwise_and(img1, img2)  # 執行AND運算
output2 = cv2.bitwise_or(img1, img2)  # 執行OR運算
output3 = cv2.bitwise_xor(img1, img2)  # 執行XOR運算

plt.subplot(231)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(232)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(233)
plt.imshow(cv2.cvtColor(output0, cv2.COLOR_BGR2RGB))
plt.title("NOT")

plt.subplot(234)
plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
plt.title("AND")

plt.subplot(235)
plt.imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
plt.title("OR")

plt.subplot(236)
plt.imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
plt.title("XOR")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 影像的位元運算(4) AND OR NOT XOR SP
# cv2.bitwise_and()
# cv2.bitwise_or()
# cv2.bitwise_not()
# cv2.bitwise_xor() 異或
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("取兩圖的影像差異 diff")

filename_diff1 = "C:/_git/vcs/_1.data/______test_files1/compare/compare1.jpg"
filename_diff2 = "C:/_git/vcs/_1.data/______test_files1/compare/compare2.jpg"

img1 = cv2.imread(filename_diff1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img2 = cv2.imread(filename_diff2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("image1.shape內容 :", img1.shape)
print("image2.shape內容 :", img2.shape)

# 比較並顯示差異影像
diff = cv2.absdiff(img1, img2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
plt.title("Difference")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("疊合")

filename_add1 = "C:/_git/vcs/_1.data/______test_files1/ims02.bmp"
filename_add2 = "C:/_git/vcs/_1.data/______test_files1/ims03.bmp"

img1 = cv2.imread(filename_add1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img2 = cv2.imread(filename_add2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

blended = cv2.addWeighted(img1, 1, img2, 1, 0)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
plt.title("疊合")

show()

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
