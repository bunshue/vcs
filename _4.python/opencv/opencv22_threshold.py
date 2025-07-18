"""
閾值處理 cv2.threshold

# cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)

# 直方圖二值化
# 不同模式的Threshold方法
# 0 cv2.THRESH_BINARY      # 如果大於 閾值 就等於 255，反之等於 0。
# 1 cv2.THRESH_BINARY_INV  # 如果大於 閾值 就等於 0，反之等於 255。  # 轉為反相黑白
# 2 cv2.THRESH_TRUNC       # 如果大於 閾值 就等於 thresh，反之數值不變。
# 3 cv2.THRESH_TOZERO      # 如果大於 閾值 數值不變，反之數值等於 0。
# 4 cv2.THRESH_TOZERO_INV  # 如果大於 閾值 等於 0，反之數值不變。

# 圖片的二值化處理, 要先轉成灰階, 再二值化
# 轉換前，都先將圖片轉換成灰階色彩
"""

from opencv_common import *

filename = "C:/_git/vcs/_4.python/opencv/data/threshold/threshold1.png"
filename = "C:/_git/vcs/_4.python/opencv/data/threshold/gray_scale.jpg"

maxval = 255  # 定義像素最大值, 閾值

print("------------------------------------------------------------")  # 60個

print("二值化範例, 只能處理灰階圖")
print("二值化圖, 閥值, 小於變全黑, 大於變全白")

# 轉換前，都先將圖片轉換成灰階色彩
src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

thresh = 63  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
#         cv2.threshold(src, 閥值, 最大灰度值, 使用的二值化方法)
ret, dst1 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, dst2 = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
ret, dst3 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
ret, dst4 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
ret, dst5 = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)

plt.figure(figsize=(10, 10))
plt.subplot(331)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(332)
plt.title("BINARY")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(333)
plt.title("BINARY_INV")
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(334)
plt.title("TRUNC")
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(335)
plt.title("TOZERO")
plt.imshow(cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(336)
plt.title("TOZERO_INV")
plt.imshow(cv2.cvtColor(dst5, cv2.COLOR_BGR2RGB))
plt.axis("off")

print("做 OTSU 二值化, Otsu : 找出最佳的閾值")
otsu_thresh = 0  # OTSU, 定義閾值 = 0, 必須
ret, dst9 = cv2.threshold(src, otsu_thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# ret 是 Ostu方法計算的閾值, dst是回傳的影像
print("Otsu : 找出最佳的閾值 :", ret)

plt.subplot(337)
plt.title("threshold + Otsu")
plt.imshow(cv2.cvtColor(dst9, cv2.COLOR_BGR2RGB))
plt.axis("off")

print("建立 4X5 陣列, 數值為100")
src = np.ones((4, 5), dtype=np.uint8) * 100  # 設定陣列是 100
src[0:2, 0:2] = 110

print("做 OTSU 二值化, Otsu : 找出最佳的閾值")
otsu_thresh = 0  # OTSU, 定義閾值 = 0, 必須
ret, dst = cv2.threshold(src, otsu_thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# ret 是 Ostu方法計算的閾值, dst是回傳的影像
print("Otsu : 找出最佳的閾值 :", ret)

plt.subplot(338)
plt.title("原圖100和110組成")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(339)
plt.title("OTSU找出最佳的閾值 :" + str(ret))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.suptitle("二值化圖, 閥值 = " + str(thresh))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("閾值分割 threshold")

src = np.array(
    [[123, 234, 68], [33, 51, 17], [48, 98, 234], [129, 89, 27], [45, 167, 134]],
    np.uint8,
)

# 手動設置閾值
thresh = 150  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# TRIANGLE 閾值處理
triThe = 0
triThe, dst_tri = cv2.threshold(src, triThe, maxval, cv2.THRESH_TRIANGLE)
print(triThe, dst_tri)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# 自適應閾值計算方法為ADAPTIVE_THRESH_MEAN_C
dst_mean = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)

# 3, 5 =>  11, 2

# 自適應閾值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)

plt.subplot(221)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("THRESH_BINARY 二值化處理")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst_mean, cv2.COLOR_BGR2RGB))
plt.title("ADAPTIVE_THRESH_MEAN_C 自適應閾值")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst_gauss, cv2.COLOR_BGR2RGB))
plt.title("ADAPTIVE_THRESH_GAUSSIAN_C 自適應閾值")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/threshold/brain.jpg"
gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("做 OTSU 二值化, Otsu : 找出最佳的閾值")
otsu_thresh = 0  # OTSU, 定義閾值 = 0, 必須
ret, dst = cv2.threshold(
    gray, otsu_thresh, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)
# ret 是 Ostu方法計算的閾值, dst是回傳的影像
print("Otsu : 找出最佳的閾值 :", ret)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel, iterations=2)

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

plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("原圖灰階")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("OTSU二值化")

plt.subplot(223)
plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.title("opening")

plt.subplot(224)
plt.imshow(cv2.cvtColor(sure_fg, cv2.COLOR_BGR2RGB))
plt.title("sure_fg")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用Trackbar")


def do_trackbar_event1(val):
    if val > 255:
        cv2.imshow("OpenCV", gray)
    else:
        # print("數值 :", val, end=" ")
        thresh = val  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
        ret, dst = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
        cv2.imshow("OpenCV", dst)


image = cv2.imread(filename2)  # 彩色讀取
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
# gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

cv2.imshow("OpenCV", gray)

cv2.createTrackbar("Threshold ", "OpenCV", 0, 300, do_trackbar_event1)
cv2.setTrackbarPos("Threshold ", "OpenCV", 127)  # 設定預設值

# 取得Trackbar數值
value = cv2.getTrackbarPos("Threshold ", "OpenCV")
do_trackbar_event1(value)  # 套用一次設定值

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()


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
