"""
影像分析工具 - 影像直方圖
cv2.calcHist()
cv2.equalizeHist()  # 直方圖均衡化處理, 只能處理灰階圖

用直方圖分析一張圖片的顏色組成

hist = cv2.calcHist(image, channels, mask, histSize, ranges, accumulate) 函數統計直方圖
參數都要加［］括起來
image：原圖像
channels：如果輸入的圖像是灰度圖，它的值就是[0]，如果是彩色圖像，傳入的參數可以是[0]、[1]、[2],分布對應著b,g,r。
mask：掩膜圖像。要統計整幅圖像的直方圖就把這個參數設為None，如果要統計掩膜部分的圖像的直方圖，就需要這個參數。
histSize：bins的個數,就是分多少個組距。例如[256]或者[16]，都要用方括號括起來。
ranges：像素值範圍，通常為[0, 256]
accumulate：累計(累積、疊加)標識，默認值是False。
這個函數返回的對象hist是一個一維數組，數組內的元素是各個灰度級的像素個數。

https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

plt.hist(image,ravel(), hitsizes, ranges, color)

img.ravel() 將原圖像的array數組轉成一維的數組
hitsizes 為直方圖的灰度級數
ranges 為灰度範圍[0,255]
color 是參數，需要使用color=''來指定顏色

plt.hist(image.ravel(), num_bins, [0, 256], log = True)
這邊使用到 matplotlib.pyplot 的 hist，它接受一組資料，計算清單中各值出現的次數，上面的範例
透過 NumPy 陣列的 ravel 方法，取得圖片攤平後的資料（只是個 NumPy 視圖）
，hist 的第二個參數指定要切出幾個直條，第三個參數指定要計算的值範圍，log 指定了是否 y 軸是否使用對數結果顯示。

OpenCV 本身也有計算直方圖資料的函式 cv2.calcHist，而且是專門針對圖片進行計算，它的參數有：

    images：一組要分析的圖片。
    channels：要分析的頻道，若是灰階圖片就指定 [0]，若是彩色圖片，可分別使用 [0]、[1]、[2] 指定 BGR 頻道。
    mask：圖片遮罩，預設為 None。
    histSize：各頻道要切分出幾個直條。
    ranges：要計算的像素值範圍，通常都是設為 [0, 256]。

計算出來的資料，可以直接透過 matplotlib.pyplot 的 plot 繪製折線圖，或者是透過 bar 繪製直條圖。

image0 原圖 彩圖
image1 灰階
image2 遮罩過後
"""

from opencv_common import *

# 測試圖片
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"
filename = "data/pic_brightness1.bmp"
filename = "data/pic_brightness2.bmp"
filename = "data/pic_brightness3.bmp"
filename = "data/pic_calcHist.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/pic_gray_400X400_100-200.png"

filename4a = "C:/_git/vcs/_4.python/opencv/data/ims_640X480.bmp"
filename4b = "C:/_git/vcs/_4.python/opencv/data/ims_320X240.jpg"

num_bins = 256  # 直方圖顯示時的束數

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.title("原圖灰階")

plt.subplot(122)
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.title("原圖灰階直方圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_eq1 = "C:/_git/vcs/_4.python/_data/eq1.bmp"  # 560X400

print("測試 01 ravel() 的用法")
print("一張彩圖的RGB與灰度的統計資料1")
print("直接把影像的 灰階值 或 RGB值 用直方圖統計出來")
print("原圖的直方圖 RGB值 3通道分開畫")

image0 = cv2.imread(filename_eq1)  # 彩色讀取
image1 = cv2.imread(filename_eq1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("灰階")

b, g, r = cv2.split(image0)  # 拆分彩色影像3通道

plt.subplot(223)
plt.hist(b.ravel(), num_bins, [0, 256], color="b", alpha=0.5)  # 藍通道 拉成一維
plt.hist(g.ravel(), num_bins, [0, 256], color="g", alpha=0.5)  # 綠通道 拉成一維
plt.hist(r.ravel(), num_bins, [0, 256], color="r", alpha=1.0)  # 紅通道 拉成一維
plt.hist(image1.ravel(), num_bins, [0, 256], color="gray", alpha=0.5)  # 灰階 拉成一維

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.title("原圖的直方圖 RGB值 3通道/灰階")

print("使用 calcHist")

# image1 灰階影像
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
print(hist.shape)
print(hist.size)

plt.subplot(224)
plt.plot(hist, color="b", label="plot", lw=2)
plt.plot(np.arange(0, 256), hist.ravel(), color="gold", label="plot", lw=2)  # 同上
plt.bar(np.arange(0, 256), hist.ravel(), color="gray", label="bar", lw=2)  # 要這麼寫
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.title("用 plot 和 bar 顯示 calcHist 的結果")

show()

print("測試 03 calcHist----------------------------------------------------------")  # 60個

print("一張彩圖的RGB與灰度的統計資料2")

# 對於彩色的圖片，
# 可以用 OpenCV 的 calcHist 函數分別計算統計值，
# 並畫出 RGB 三種顏色的分佈圖

image0 = cv2.imread(filename)  # 彩色讀取

# ---------使用cv2.calcHist()函數繪圖----
# 這個函數可以傳入彩圖，因為它還有一個channel參數，就把通道分開了
# 計算直方圖每個 bin 的數值, 將彩圖的RGB通道分離出來

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# RGB畫在一起
# 使用 ravel 將所有的像素資料轉為一維的陣列
plt.hist(image0.ravel(), num_bins, [0, 256], color="gray", alpha=0.3, density=False)
# plt.hist(image0.ravel(), bins = num_bins, color="gray", alpha = 0.3, density=False)

# RGB分開畫
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.legend(loc="best")

show()

print("測試 04 calcHist----------------------------------------------------------")  # 60個

print("一張彩圖的RGB與灰度的統計資料3 使用mask")
print("使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階")

image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image1.shape, np.uint8)

H = image1.shape[0]
W = image1.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

"""顯示原圖與mask
plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB), "gray")
plt.subplot(122)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")
show()
"""

# 灰階 全圖
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])

# 灰階 部分圖
hist2 = cv2.calcHist([image1], [0], mask, [256], [0, 256])

plt.plot(hist1, "r", label="全圖", lw=3)
plt.plot(hist2, "g", label="部分圖", lw=2)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

show()

print("測試 05 calcHist----------------------------------------------------------")  # 60個

print("配合圖形遮罩計算直方圖")


print("使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階")

image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image1.shape, np.uint8)

H = image1.shape[0]
W = image1.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(image1, image1, mask=mask)

# 以原圖計算直方圖
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_full = cv2.calcHist([image1], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([image1], [0], mask, [256], [0, 256])

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(223)
plt.imshow(cv2.cvtColor(masked_gray, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(224)
plt.plot(hist_full, "r", label="全圖", lw=3)
plt.plot(hist_mask, "g", label="部分圖", lw=2)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("將一圖分解成 藍 綠 紅 三通道")

image0 = cv2.imread(filename)  # 彩色讀取

cut = 50

b, g, r = cv2.split(image0)  # 拆分彩色影像3通道

rr = r[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
# show()

rrr = rr.reshape(rr.shape[0] * rr.shape[1], 1)
# print(rrr.shape)
rrr = rrr[0 : len(rrr) : 5]
plt.hist(rrr, num_bins, color="r", label="R", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
# show()

ggg = gg.reshape(gg.shape[0] * gg.shape[1], 1)
# print(ggg.shape)
plt.hist(ggg, num_bins, color="g", label="G", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

bb = b[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
# show()

bbb = bb.reshape(bb.shape[0] * bb.shape[1], 1)
# print(bbb.shape)

plt.hist(bbb, num_bins, color="b", label="B", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用
show()

print("測試 07 calcHist----------------------------------------------------------")  # 60個

image0 = cv2.imread(filename)  # 彩色讀取
image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_gray = cv2.calcHist([image1], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 8))
plt.plot(hist_gray, color="gray", label="灰", lw=3)
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)

plt.plot(hist_gray, color="gray")
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖各分量與灰階的直方圖")

show()

print("測試 08 calcHist----------------------------------------------------------")  # 60個

# 使用 mask 繪製直方圖

image0 = cv2.imread(filename)  # 彩色讀取

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image0.shape, np.uint8)

H = image0.shape[0]
W = image0.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

image_mask = cv2.bitwise_and(image0, mask)

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# 原圖+mask後之統計數據
hist_image_mask0 = cv2.calcHist([image0], [0], mask[:, :, 0], [256], [0, 256])

# 原圖+mask後之統計數據
hist_image_mask1 = cv2.calcHist([image0], [1], mask[:, :, 0], [256], [0, 256])

# 原圖+mask後之統計數據
hist_image_mask2 = cv2.calcHist([image0], [2], mask[:, :, 0], [256], [0, 256])

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_mask, cv2.COLOR_BGR2RGB))  # 原圖
plt.title("原圖mask後")

plt.subplot(223)
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(224)
# 畫出 B 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask0, "b")  # 無掩膜和有掩膜的直方圖畫到一起
# 畫出 G 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask1, "g")  # 無掩膜和有掩膜的直方圖畫到一起
# 畫出 R 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask2, "r")  # 無掩膜和有掩膜的直方圖畫到一起
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

show()

print("測試 09 calcHist----------------------------------------------------------")  # 60個

image0 = cv2.imread(filename2)  # 彩色讀取

bgr_planes = cv2.split(image0)  # 拆分彩色影像3通道

hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])
histRange = (0, 256)  # the upper boundary is exclusive
accumulate = False

histSize = 256
# 生成圖像之直方圖, 256束, B bgr_planes 之 第0通道
b_hist = cv2.calcHist(
    bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate
)

# 生成圖像之直方圖, 256束, G bgr_planes 之 第1通道
g_hist = cv2.calcHist(
    bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate
)

# 生成圖像之直方圖, 256束, R bgr_planes 之 第2通道
r_hist = cv2.calcHist(
    bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate
)

## [Draw the histograms for B, G and R]
hist_w = 512
hist_h = 400
bin_w = int(round(hist_w / histSize))

histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
## [Draw the histograms for B, G and R]

## [Normalize the result to ( 0, histImage.rows )]
cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
## [Normalize the result to ( 0, histImage.rows )]

## [Draw for each channel]
for i in range(1, histSize):
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(b_hist[i - 1])),
        (bin_w * (i), hist_h - int(b_hist[i])),
        BLUE,
        thickness=2,
    )
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(g_hist[i - 1])),
        (bin_w * (i), hist_h - int(g_hist[i])),
        GREEN,
        thickness=2,
    )
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(r_hist[i - 1])),
        (bin_w * (i), hist_h - int(r_hist[i])),
        RED,
        thickness=2,
    )
## [Draw for each channel]

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(histImage, cv2.COLOR_BGR2RGB))
plt.title("均衡化之圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("equalizeHist  # 直方圖均衡化處理, 只能處理灰階圖")

image1 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖轉灰階")

plt.subplot(222)
plt.hist(image1.ravel(), num_bins, [0, 256], color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖的影像直方圖")

# 直方圖均衡化處理

image1 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(223)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("均衡化之圖")

# 均值化的影像
# 均衡化後的灰度直方圖分布
plt.subplot(224)
plt.hist(equ.ravel(), num_bins, [0, 256], color="g")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("均衡化後的直方圖分布")

show()

# 加 mask 處理

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("equalizeHist  # 直方圖均衡化處理, 只能處理灰階圖")

image0 = cv2.imread(filename2)  # 彩色讀取
image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)  # 轉灰階

equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖
plt.title("原圖")

plt.subplot(222)
plt.imshow(image1, cmap="gray")
plt.title("原圖轉灰階")

plt.subplot(223)
plt.imshow(equ, cmap="gray")
plt.title("均衡化之圖a")

plt.subplot(224)
plt.imshow(equ, cmap="gray_r")
plt.title("均衡化之圖b")

show()

# ----------------------直方圖對比----------------

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_image1 = cv2.calcHist([image1], [0], None, [256], [0, 256])

hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])  # 生成均衡化後的圖像的直方圖

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.plot(hist_image1)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(222)
plt.plot(hist_equ)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(223)
plt.hist(image1.ravel(), num_bins, color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(224)
plt.hist(equ.ravel(), num_bins, color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("equalizeHist  # 直方圖均衡化處理, 只能處理灰階圖")

image1 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試 15 calcHist equalizeHist")

"""
opencv之影像直方圖均衡化 直方圖均衡化處理 cv2.equalizeHist
函數原型：cv2.calcHist(image,channels,mask,histSize,ranges)
image為待計算直方圖的圖像，需用[]包裹
channels指定待計算直方圖的圖像的哪一通道用來計算直方圖，RGB圖像可以指定[0,1,2]，灰度圖像只有[0],需用[]包裹,
mask為掩碼，可以指定圖像的範圍，如果是全圖，默認為none
hitsize為直方圖的灰度級數，例如[0,255]一共256級，故參數為256，需用[]包裹
range為像素值範圍，為[0,255]
返回值為hist，直方圖
"""

image1 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])

# 法一: 用plt.plot畫圖
plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.plot(hist, "r")
plt.title("用plot")

# 法二: 用 plot 或 bar 顯示 calcHist 的結果
plt.subplot(232)
plt.plot(np.arange(0, 256), hist.ravel())  # 拉成一維 並畫出
plt.title("用plot")

plt.subplot(233)
plt.bar(np.arange(0, 256), hist.ravel())  # 拉成一維 並畫出
plt.title("用bar")

# 法三: 用plt.hist()畫圖
plt.subplot(234)
plt.hist(image1.ravel(), num_bins, [0, 256], color="b")  # 拉成一維
plt.title("用hist")

"""
三、直方圖均衡化
影像的直方圖是對影像對比度效果上的一種處理，旨在使得影像整體效果均勻，黑與白之間的各個畫素級之間的點更均勻一點。 
通過這種方法，亮度可以更好地在直方圖上分佈。這樣就可以用於增強區域性的對比度而不影響整體的對比度，直方圖均衡化通過有效地擴充套件常用的亮度來實現這種功能。
這種方法對於背景和前景都太亮或者太暗的影像非常有用，這種方法尤其是可以帶來X光影像中更好的骨骼結構顯示以及曝光過度或者曝光不足照片中更好的細節。
利用
cv2.equalizeHist(img)，將要均衡化的原影像【要求是灰度影像】作為引數傳入，則返回值即為均衡化後的影像。
"""

plt.subplot(235)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image2 = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(236)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H = 640, 480
cx, cy = W // 2, H // 2

print("把 直方圖均衡化處理 套用在webcam上 黑白")
print("把 直方圖均衡化處理 套用在webcam上 彩色")

video_filename = "D:/內視鏡影片/NBI錄影_V20241009_081309.mp4"
# cap = cv2.VideoCapture(video_filename)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

cv2.namedWindow("Original")

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    cut = 80

    # 畫一些標記
    dd = 5
    topLeft = (cut - dd, cut - dd)
    topLeft = (cx - W // 2 + cut - dd, cy - H // 2 + cut - dd)

    bottomRight = (W - cut + dd, H - cut + dd)
    bottomRight = (cx + W // 2 - cut + dd, cy + H // 2 - cut + dd)

    cv2.rectangle(frame, topLeft, bottomRight, 255, 2)  # 藍色框

    # 原圖
    cv2.imshow("Original", frame)

    # 裁切圖片 ST
    # 裁切區域的 x 與 y 座標（左上角）
    x_st, y_st = cut, cut
    # 裁切區域的長度與寬度
    w, h = W - x_st * 2, H - y_st * 2
    frame2 = frame[y_st : y_st + h, x_st : x_st + w]
    frame3 = frame2
    # 裁切圖片 SP

    gray1 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # cv2.imshow("Gray", gray1)

    gray2 = cv2.equalizeHist(gray1)  # 直方圖均衡化處理, 只能處理灰階圖
    cv2.imshow("Histogram1", gray2)
    # 裁切圖片 SP

    b, g, r = cv2.split(frame3)  # 拆分彩色影像3通道

    bb = cv2.equalizeHist(b)  # 直方圖均衡化處理, 只能處理灰階圖
    gg = cv2.equalizeHist(g)  # 直方圖均衡化處理, 只能處理灰階圖
    rr = cv2.equalizeHist(r)  # 直方圖均衡化處理, 只能處理灰階圖

    frame3 = cv2.merge([bb, gg, rr])  # 影像3通道合併成彩色影像

    cv2.imshow("Histogram2", frame3)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直方圖均衡化—增強影像對比度

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖灰階")

plt.subplot(312)
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.title("原圖灰階直方圖")

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
# print(f"資料內容 \n{hist}")

hist = cv2.calcHist([src], [0], None, [256], [0, 258])  # 直方圖統計資料

plt.subplot(313)
plt.plot(hist)  # 用plot()繪直方圖

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_COLOR)  # 彩色讀取

plt.subplot(211)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖彩色")

b = cv2.calcHist([src], [0], None, [256], [0, 256])  # B 通道統計資料
g = cv2.calcHist([src], [1], None, [256], [0, 256])  # G 通道統計資料
r = cv2.calcHist([src], [2], None, [256], [0, 256])  # R 通道統計資料

plt.subplot(212)

plt.plot(b, color="b")  # 用plot()繪 B 通道
plt.plot(g, color="g")  # 用plot()繪 G 通道
plt.plot(r, color="r")  # 用plot()繪 R 通道
plt.title("三通道分別畫出")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖灰階")

mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:500, 50:400] = 255  # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)  # And運算

plt.subplot(312)
plt.imshow(cv2.cvtColor(masked, cv2.COLOR_BGR2RGB))
plt.title("加mask")

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料

plt.subplot(313)
plt.plot(hist, color="blue", label="全部")  # 用plot()繪影像直方圖
plt.plot(hist_mask, color="red", label="Mask部分")  # 用plot()繪遮罩直方圖
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 建立遮罩
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:500, 50:400] = 255  # 在遮罩影像內建立遮罩
aftermask = cv2.bitwise_and(src, src, mask=mask)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料

plt.subplot(221)
plt.imshow(src, "gray")  # 灰階顯示第1張圖

plt.subplot(222)
plt.imshow(mask, "gray")  # 灰階顯示第2張圖

plt.subplot(223)
plt.imshow(aftermask, "gray")  # 灰階顯示第3張圖

plt.subplot(224)
plt.plot(hist, color="blue", label="全部")
plt.plot(hist_mask, color="red", label="Mask部分")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 均衡化處理

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.subplot(221)
plt.imshow(src, "gray")  # 灰階顯示第1張圖

plt.subplot(222)
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖

plt.subplot(223)
dst = cv2.equalizeHist(src)  # 直方圖均衡化處理, 只能處理灰階圖
plt.imshow(dst, "gray")

plt.subplot(224)
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_COLOR)  # 彩色讀取

plt.subplot(211)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖彩色")

(b, g, r) = cv2.split(src)  # 拆分彩色影像3通道

blue = cv2.equalizeHist(b)  # 直方圖均衡化處理, 只能處理灰階圖 B通道
green = cv2.equalizeHist(g)  # 直方圖均衡化處理, 只能處理灰階圖 G通道
red = cv2.equalizeHist(r)  # 直方圖均衡化處理, 只能處理灰階圖 R通道

dst = cv2.merge((blue, green, red))  # 影像3通道合併成彩色影像

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像3通道合併成彩色影像")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.subplot(211)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖灰階")

# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
dst = clahe.apply(src)  # 灰度影像與clahe物件關聯

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("自適應直方圖均衡化 CLAHE")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直方圖

# 影像的三個通道的直方圖統計、通道0和通道2的二維直方圖統計
img = cv2.imread(filename2)  # 彩色讀取

fig, ax = plt.subplots(1, 2, figsize=(12, 8))
colors = ["blue", "green", "red"]

for i in range(3):
    hist, x = np.histogram(img[:, :, i].ravel(), bins=256, range=(0, 256))
    ax[0].plot(0.5 * (x[:-1] + x[1:]), hist, label=colors[i], color=colors[i])

ax[0].legend(loc="upper left")
ax[0].set_xlim(0, 256)
hist2, x2, y2 = np.histogram2d(
    img[:, :, 0].ravel(),
    img[:, :, 2].ravel(),
    bins=(100, 100),
    range=[(0, 256), (0, 256)],
)
ax[1].imshow(hist2, extent=(0, 256, 0, 256), origin="lower", cmap="gray")
ax[1].set_ylabel("blue")
ax[1].set_xlabel("red")

show()

print("------------------------------")  # 30個

result = cv2.calcHist(
    [img],
    channels=(0, 1, 2),
    mask=None,
    histSize=(30, 20, 10),
    ranges=(0, 256, 0, 256, 0, 256),
)
cc = result.shape
print(cc)

# (30, 20, 10)

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

"""

cv2.calcHist


    1、使用 plt.hist(x, bins)函数绘制直方图
    　　x：数据，必须是一维的。图像数据通常是二维的，所以要用ravel()函数将其拉成一维的数据后再作为参数使用。
    　　bins：表示x轴分多少组。

    2、使用 hist = cv2.calcHist(img, channels, mask, histSize, ranges, accumulate)函数统计直方图，然后用plt.plot()函数将其绘制出来
    　　这个函数里面的参数都要加［］括起来，这是底层代码写死的，不然无法识别。
    　　img：原图像
    　　channels：如果输入的图像是灰度图，它的值就是[0]，如果是彩色图像，传入的参数可以是[0]、[1]、[2],分布对应着b,g,r。
    　　mask：掩膜图像。要统计整幅图像的直方图就把这个参数设为None，如果要统计掩膜部分的图像的直方图，就需要这个参数。
    　　histSize：bins的个数,就是分多少个组距。例如[256]或者[16]，都要用方括号括起来。
    　　ranges：像素值范围，通常为[0, 256]
    　　accumulate：累计(累积、叠加)标识，默认值是False。
    　　这个函数返回的对象hist是一个一维数组，数组内的元素是各个灰度级的像素个数。




    3、绘制掩膜部分的图像的直方图
    掩膜在遥感影像处理中使用较多，当提取道路或者河流或者房屋时，通过一个掩膜矩阵来对原图进行过滤，然后将我们感兴趣的物体凸显出来。




三、直方图均衡化

    1、什么是直方图均衡化？为啥要均衡化？
    如果一幅图像的灰度值都集中在一个小的范围内，那么这幅图看起来就是一个色调，图像里面的画面也没有什么对比度。
    如果一幅图像的灰度值均匀的分布在所有灰度级上，那这幅画看起来就有较高的色彩对比度，也就是画面更加清晰，色彩丰富。
    直方图均衡化的注意目的就是：将原始图像的灰度级均匀的映射到整个灰度级范围内，得到一个灰度级分布均匀的图像。并且这种均衡化，既实现了灰度值统计上的概率均衡，还实现了人类视觉系统(human visual system, HVS)上的视觉均衡。

 直方图均衡化是对图像进行非线性拉伸，重新分配图像像素值，使一定灰度范围内的像素数量大致相同。这种方法可以提高图像整体的对比度，特别是有用数据的像素值分布比较接近时，在X光图像中使用广泛，可以提高骨架结构的显示，另外在曝光过度或者曝光不足的图像中可以更好的突出细节。另外通过均衡化处理后，图像特征也更突出，便于后面的处理，所以广泛用于图像处理、车票识别、人脸识别等领域。

    2、直方图均衡化的原理
    直方图均衡化算法主要包括2个步骤：
    （1）计算累计直方图
    （2）对累计直方图进行区间转换
    说明：因为人眼对像素值越大的点看得越清晰，所以用累计概率。当像素值越大，累计概率就越大，此时就越有更多的像素点被映射到像素值更大的区间。

图像均衡化的具体步骤：
（1）读取一幅图像。一般情况下我们图像均衡化处理的都是灰度图，如果非要处理彩图，就必须按通道分别处理。
（2）将图像转化为灰度图像。
（3）统计灰度级和各个灰度级上的像素个数。灰度级就是灰度图像中各个像素点的像素值。就是统计所有像素值以及这些像素值对应的像素个数。
（4）计算归一化统计直方图。就是将各个灰度级下的像素个数/总像素个数，变成概率的形式。
（5）计算累计概率。就是将各个灰度级下的概率变成累计概率。
（6）对累计概率进行区间转换。就是转换各个累计概率对应的灰度级。这里有2种情况：
情况1：在原来的灰度范围内转换：用原来的最大灰度值x累计概率，得到新的灰度级，统计新的灰度级下对应的像素个数，即可得到均衡化的直方图。也就是原来的像素点都映射到新的灰度级上了，图像就实现了均衡化。
情况2：不在原来的灰度范围内转换：用你想要的的灰度范围，比如像要[0,255]256个灰度级的范围内均衡化，就用255x累计概率=新的灰度级。然后统计新的灰度级下对应的像素个数，即可得到均衡化后的直方图，进而得到均衡化后的图像。

一个小案例展示计算过程：左图是原图，右图是均衡化后的图像，下面的表格是计算的过程。

    3、API：dst = cv2.equalizeHist(img)
    img：灰度图像
    dst：均衡化后的图像



    四、自适应的直方图均衡化

    上面讲的直方图均衡化是从整个图像的所有像素点进行均衡处理的。在很多情况下，这样做其实效果并不好，因为对比度改变了实际上我们会丢失很多信息，比如一些细小的边缘信息，实际上是会丢失的。为了解决这个问题，我们要进行自适应的直方图均衡化。

    具体操作区别有：
    （1）将整幅图像分成很多小块，然后对每个小块分别进行直方图均衡化，这样均衡化操作就会集中在一个个小的区域内。
    （2）图像被划分成很多小块，很容易出现小块与小块之间的边界，为避免这种情况，使用双线性插值，对每一个小块进行拼接。
    （3）如果图像有噪声的话，噪声就会被放大，为了避免这种情况，要使用对比度限制。就是对每个小块来说，如果直方图中的某些像素值的频率超过设定的上限的话，就把这些像素点平均分配到其他bins里，然后再进行直方图均衡化。

    API：clahe = cv2.createCLAHE(clipLimit, tileGridSize)　,　　clahe.apply(img)
    clipLimit：对比度限制，默认是40
    tileGridSize：分块的大小，默认是8x8

        #例13.4 实现自适应图像均衡化处理    
        import cv2
        import numpy as np
        import matplotlib.pyplot as plt
         
        img = cv2.imread(r'C:/Users/25584/Desktop/equ.bmp',0) # 灰階讀取?
         
        equ = cv2.equalizeHist(img)    #普通的均衡化处理     
         
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #自适应均衡化处理
        cl = clahe.apply(img)
         
        img_ = np.hstack((img, equ, cl))   #三张图片合到一起
        plt.imshow(img_, cmap='gray') 
        plt.show()

"""
print("------------------------------")  # 30個


print("------------------------------------------------------------")  # 60個
