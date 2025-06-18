"""
閾值處理 cv2.threshold

"""

from opencv_common import *

# filename = "C:/_git/vcs/_4.python/opencv/data/threshold/threshold1.png"

maxval = 255  # 定義像素最大值, 閾值

print("------------------------------------------------------------")  # 60個

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
thresh = 63  # 定義閾值

print("二值化範例, 只能處理灰階圖")
print("二值化圖, 閥值 = " + str(thresh) + ", 小於變全黑, 大於變全白")

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

#         cv2.threshold(src, 閥值, 最大灰度值, 使用的二值化方法)
ret, dst1 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
ret, dst2 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
ret, dst3 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
ret, dst4 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
ret, dst5 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)

plt.subplot(331)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(332)
plt.title("BINARY")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(333)
plt.title("BINARY_INV")
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(334)
plt.title("TRUNC")
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(335)
plt.title("TOZERO_INV")
plt.imshow(cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(336)
plt.title("TOZERO")
plt.imshow(cv2.cvtColor(dst5, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

thresh = 127  # 定義閾值 = 127
ret, dst8 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)

# Otsu : 找出最佳的閾值
thresh = 0  # OTSU, 定義閾值 = 0
ret, dst9 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# ret 是 Ostu方法計算的閾值, dst是回傳的影像

plt.subplot(337)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(338)
plt.title("threshold 127")
plt.imshow(cv2.cvtColor(dst8, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(339)
plt.title("threshold + Otsu")
plt.imshow(cv2.cvtColor(dst9, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# plt.suptitle("二值化圖, 閥值 = " + str(thresh))
plt.suptitle("二值化圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)

print("------------------------------------------------------------")  # 60個

print("建立 4X5 陣列, 數值為111")
src = np.ones((4, 5), dtype=np.uint8) * 111  # 設定陣列是 111
print(src)

print("將一部分陣列數值改小, 數值為110")
src[0:2, 0:2] = 110  # 設定陣列區間為 0
print(src)

print("做 OTSU 二值化, Otsu : 找出最佳的閾值")
thresh = 0  # OTSU, 定義閾值 = 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# ret 是 Ostu方法計算的閾值, dst是回傳的影像


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)  # np.random之randint不含尾
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 5, 3
image = np.zeros((H, W), dtype=np.uint8)
image[0:6, 0:6] = 123
image[2:6, 2:6] = 126
print("image = \n", image)

t1, thd = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print("thd = \n", thd)

t2, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("otsu = \n", otsu)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# 自適應閾值計算方法為ADAPTIVE_THRESH_MEAN_C
dst_mean = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)

# 自適應閾值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(222)
plt.title("THRESH_BINARY 二值化處理")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(223)
plt.title("ADAPTIVE_THRESH_MEAN_C 自適應閾值")
plt.imshow(cv2.cvtColor(dst_mean, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(224)
plt.title("ADAPTIVE_THRESH_GAUSSIAN_C 自適應閾值")
plt.imshow(cv2.cvtColor(dst_gauss, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 41 三種二值化方法")

THRESHOLD = 127

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = cv2.imread(filename, 0)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t1, thd = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY)

athdMEAN = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)

athdGAUS = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))
plt.title("thd")

plt.subplot(223)
plt.imshow(cv2.cvtColor(athdMEAN, cv2.COLOR_BGR2RGB))
plt.title("athdMEAN")

plt.subplot(224)
plt.imshow(cv2.cvtColor(athdGAUS, cv2.COLOR_BGR2RGB))
plt.title("athdGAUS")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 42")

THRESHOLD = 127

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp"

image = cv2.imread(filename, 0)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t1, thd = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))
plt.title("thd")

plt.subplot(133)
plt.imshow(cv2.cvtColor(otsu, cv2.COLOR_BGR2RGB))
plt.title("otsu")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 43 圖片的二值化處理, 要先轉成灰階, 再二值化")

THRESHOLD = 30
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
thr, image_binary = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TOZERO)
print(thr)

plt.imshow(cv2.cvtColor(image_binary, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

print("opencv 44 各種二值化")

THRESHOLD = 127

image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

# 轉換前，都先將圖片轉換成灰階色彩
#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
ret, output1 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_BINARY
)  # 如果大於 THRESHOLD 就等於 255，反之等於 0。

ret, output2 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_BINARY_INV
)  # 如果大於 THRESHOLD 就等於 0，反之等於 255。

ret, output3 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TRUNC
)  # 如果大於 THRESHOLD 就等於 THRESHOLD，反之數值不變。

ret, output4 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TOZERO
)  # 如果大於 THRESHOLD 數值不變，反之數值等於 0。

ret, output5 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TOZERO_INV
)  # 如果大於 THRESHOLD 等於 0，反之數值不變。

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
plt.title("output1")

plt.subplot(233)
plt.imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
plt.title("output2")

plt.subplot(234)
plt.imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
plt.title("output3")

plt.subplot(235)
plt.imshow(cv2.cvtColor(output4, cv2.COLOR_BGR2RGB))
plt.title("output4")

plt.subplot(236)
plt.imshow(cv2.cvtColor(output5, cv2.COLOR_BGR2RGB))
plt.title("output5")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 45")

THRESHOLD = 127

image = cv2.imread(filename)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

# 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(image_gray, THRESHOLD, 255, cv2.THRESH_BINARY)

output2 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

output3 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
plt.title("output1")

plt.subplot(223)
plt.imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
plt.title("output2")

plt.subplot(224)
plt.imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
plt.title("output3")

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
