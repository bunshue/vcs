"""
cv2.findContours
cv2.drawContours  # 繪製圖形外輪廓

圖片邊緣檢測

圖片轉換成灰階Grayscale的部分，
利用Canny邊緣檢測使用多階段算法來檢測圖像中的各種邊緣。

OpenCV具有findContour()幫助從圖像中提取輪廓的功能。

cv2.findContours        抓取顏色範圍的輪廓座標

輪廓檢索模式(Contour Retrieval Mode)
cv2.RETR_LIST # 所有輪廓, 所有檢測到的輪廓均為同層輪廓。
cv2.RETR_TREE # 所有輪廓，並將它們組織成一個層次樹狀結構。
cv2.RETR_CCOMP # 所有輪廓，但將輪廓會被分為兩個層次，最外層的輪廓位於第一層，而內部的輪廓位於第二層。
cv2.RETR_EXTERNAL # 只取外輪廓。

1. cv2.RETR_LIST
父子结构都不管了，他们只是单纯的边界结构，他们都属于同一层。
2. cv2.RETR_EXTERNAL
这个模式只返回外层边界，所有的子层都不要了
在这个规则下，只考虑“最老的人”，其他人全都不考虑。
当你只要外层边界的时候，这个标志位很有用。
3. cv2.RETR_CCOMP
这个标志会返回全部的边界，但是会把它们分为两层，可以算是一种简化吧，例如：
用两种颜色标志就是下面这样的：一层绿色一层粉色
所以可以看到只有两层结构，要么是外层要么是里层，
4. cv2.RETR_TREE
也就说，保存了全部的层次结构

取值演算法:
cv2.CHAIN_APPROX_SIMPLE
cv2.CHAIN_APPROX_NONE
cv2.CHAIN_APPROX_TC89_L1

輪廓近似方法 的選項:
CHAIN_APPROX_TC89_KCOS
CHAIN_APPROX_SIMPLE

"""

from opencv_common import *


def get_image_contours(src):
    image_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # 二值化處理影像
    thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
    ret, dst_binary = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_BINARY)
    # 找尋影像內的輪廓, 返回的 contours 是一個 list 列表
    contours, hierarchy = cv2.findContours(
        dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
    )
    contours, hierarchy = cv2.findContours(
        dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    contours, hierarchy = cv2.findContours(
        dst_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )
    contours, hierarchy = cv2.findContours(
        dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    get_contours_info(contours)
    return contours, hierarchy


def get_contours_info(contours):
    # print("資料類型 :", type(contours))
    print("輪廓數量 :", len(contours))
    # print(contours)
    """
    # 看 contours 資料 ST
    cnt = contours[0]  # 取得輪廓數據
    print(f"資料格式 = {type(cnt)}")
    print(f"資料維度 = {cnt.ndim}")
    print(f"資料長度 = {len(cnt)}")
    for i in range(3):  # 列印 3 個座標點
        print(cnt[i])
    # 看 contours 資料 SP
    """


print("------------------------------------------------------------")  # 60個

# 統一處理多圖，顯示在一起

filename1 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"
filename2 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02.bmp"
filename2b = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02b.png"
filename5 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02b.png"
filename3 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape03.png"
filename4 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape04.png"
# filename_star_blue = "C:/_git/vcs/_4.python/opencv/data/_shape/star_blue.bmp"
# filename_star_silver = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.bmp"
filename6 = "C:/_git/vcs/_4.python/opencv/data/_shape/star_blue.bmp"
filename7 = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.bmp"
# filename5 = "C:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename6 = "C:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
# filename7 = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
# filename8 = "C:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename8 = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"
filename3 = "C:/_git/vcs/_4.python/opencv/data/_Hough/shapes.jpg"
# filename4 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02b.png"


def draw_contours(filename):
    image10 = cv2.imread(filename)  # 彩色讀取
    image11 = image10.copy()
    image12 = cv2.cvtColor(image11, cv2.COLOR_BGR2GRAY)  # 轉灰階
    image13 = cv2.GaussianBlur(image12, (13, 13), 0)  # 執行高斯模糊化
    image13 = image12.copy()  # 不進行高斯模糊
    image14 = cv2.Canny(image13, 50, 150)
    contours, hierarchy = cv2.findContours(
        image14.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )
    image15 = cv2.drawContours(image11, contours, -1, RED, 10)
    return image10, image12, image13, image14, image15

image10, image12, image13, image14, image15 = draw_contours(filename1)
image20, image22, image23, image24, image25 = draw_contours(filename2)
image30, image32, image33, image34, image35 = draw_contours(filename3)
image40, image42, image43, image44, image45 = draw_contours(filename4)
image50, image52, image53, image54, image55 = draw_contours(filename8)

plt.figure(figsize=(14, 8))
plt.subplot(5, 5, 1), plt.imshow(cv2.cvtColor(image10, cv2.COLOR_BGR2RGB))
plt.title("原圖"), plt.axis("off")
plt.subplot(5, 5, 2), plt.imshow(cv2.cvtColor(image12, cv2.COLOR_BGR2RGB))
plt.title("轉灰階"), plt.axis("off")
plt.subplot(5, 5, 3), plt.imshow(cv2.cvtColor(image13, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊"), plt.axis("off")
plt.subplot(5, 5, 4), plt.imshow(cv2.cvtColor(image14, cv2.COLOR_BGR2RGB))
plt.title("邊緣檢測"), plt.axis("off")
plt.subplot(5, 5, 5), plt.imshow(cv2.cvtColor(image15, cv2.COLOR_BGR2RGB))
plt.title("畫輪廓"), plt.axis("off")
plt.subplot(5, 5, 6)
plt.imshow(cv2.cvtColor(image20, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 7)
plt.imshow(cv2.cvtColor(image22, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 8)
plt.imshow(cv2.cvtColor(image23, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 9)
plt.imshow(cv2.cvtColor(image24, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 10)
plt.imshow(cv2.cvtColor(image25, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 11)
plt.imshow(cv2.cvtColor(image30, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 12)
plt.imshow(cv2.cvtColor(image32, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 13)
plt.imshow(cv2.cvtColor(image33, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 14)
plt.imshow(cv2.cvtColor(image34, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 15)
plt.imshow(cv2.cvtColor(image35, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 16)
plt.imshow(cv2.cvtColor(image40, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 17)
plt.imshow(cv2.cvtColor(image42, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 18)
plt.imshow(cv2.cvtColor(image43, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 19)
plt.imshow(cv2.cvtColor(image44, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 20)
plt.imshow(cv2.cvtColor(image45, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 21)
plt.imshow(cv2.cvtColor(image50, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 22)
plt.imshow(cv2.cvtColor(image52, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 23)
plt.imshow(cv2.cvtColor(image53, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 24)
plt.imshow(cv2.cvtColor(image54, cv2.COLOR_BGR2RGB)), plt.axis("off")
plt.subplot(5, 5, 25)
plt.imshow(cv2.cvtColor(image55, cv2.COLOR_BGR2RGB)), plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# coin.jpg用圖片先處理方法一
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"
# filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

# 圖片先處理方法一
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
image_gray = cv2.GaussianBlur(image_gray, (13, 13), 0)  # 執行高斯模糊化
edged = cv2.Canny(image_gray, 50, 150)

# 找尋影像內的輪廓, 返回的 contours 是一個 list 列表
contours, hierarchy = cv2.findContours(
    edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

""" bad
# 圖片先處理方法二
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_BINARY)
# 找尋影像內的輪廓, 返回的 contours 是一個 list 列表
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
"""

get_contours_info(contours)

image2 = image.copy()

linewidth = 2  # 線寬

# 一起畫
# index = -1 # 指名要繪製的輪廓, -1代表全部
# image2 = cv2.drawContours(image2, contours, index, RED, linewidth)  # image2為三通道才能顯示輪廓, 用紅框標示出來

# 分開畫
n = len(contours)  # 輪廓數量
for index in range(n):
    # 繪製圖形外輪廓
    image2 = cv2.drawContours(
        image2, contours, index, color[index % 9], linewidth
    )  # image2為三通道才能顯示輪廓

plt.figure(figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("尋找 Contours")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
edged = cv2.Canny(image_gray, 30, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

get_contours_info(contours)

# 繪製圖形外輪廓
cv2.drawContours(image, contours, -1, BLUE, 2)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Contours")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02.bmp"
filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02b.png"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

edged = cv2.Canny(image_gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)

contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

get_contours_info(contours)

RECT, HEXAGON = 0, 1

print("=== 處理前")
print("矩形點數量：{}".format(len(contours[RECT])))
print("六邊形點數量：{}".format(len(contours[HEXAGON])))

approx_rect = cv2.approxPolyDP(contours[RECT], 30, True)
approx_hex = cv2.approxPolyDP(contours[HEXAGON], 30, True)

print("=== 處理後")
print("矩形點數量：{}".format(len(approx_rect)))
# 繪製圖形外輪廓
cv2.drawContours(image, [approx_rect], -1, RED, 5)

print("六邊形點數量：{}".format(len(approx_hex)))
# 繪製圖形外輪廓
cv2.drawContours(image, [approx_hex], -1, RED, 5)
print(approx_hex)
for i in range(len(approx_hex)):
    print(approx_hex[i])

plt.figure(figsize=(10, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("image")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多邊形凹凸點計算

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

h, w, d = image.shape  # d為dimension d = 3 全彩 d = 1 灰階

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

edged = cv2.Canny(image_gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)

contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

get_contours_info(contours)

cnt = contours[0]  # 取得輪廓數據

cnt = cv2.approxPolyDP(cnt, 30, True)
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("凸點數量：{}".format(len(hull)))
print("凹點數量：{}".format(len(defects)))

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(image, start, end, GREEN, 2)
    cv2.circle(image, far, 10, RED, -1)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"
# filename = "C:/_git/vcs/_4.python/opencv/data/_Hough/FerrisWheel3.jpg"
# filename = "data/findContours/lake.jpg"

src0 = cv2.imread(filename)  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 2)

# 繪製圖形外輪廓(填滿)
# dst = cv2.drawContours(src, contours, -1, GREEN, -1)

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_Hough/FerrisWheel3.jpg"
filename = "data/findContours/lake.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

src0 = cv2.imread(filename)  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

mask = np.zeros(src.shape, np.uint8)

# 繪製圖形外輪廓(填滿)
dst = cv2.drawContours(mask, contours, -1, GREEN, -1)

plt.subplot(221)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("繪製圖形輪廓")
plt.axis("off")

dst_result = cv2.bitwise_and(src, mask)

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst_result, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

src0 = cv2.imread(filename)  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 5)

print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("繪製圖形輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

src0 = cv2.imread(filename)  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 3)

print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("繪製圖形輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

src0 = cv2.imread(filename)  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 一次把全部輪廓都畫完 (參數 -1)
# 繪製圖形外輪廓
# dst = cv2.drawContours(src, contours, -1, GREEN, 5)# 繪製圖形外輪廓

# 依序畫每個輪廓
n = len(contours)  # 輪廓數量

for i in range(n):  # 輸出輪廓的屬性
    print(f"編號 = {i}")
    print(f"輪廓點的數量 = {len(contours[i])}")
    print(f"輪廓點的外形 = {contours[i].shape}")

print(contours[1])  # 列印編號1的輪廓點

dst = np.ones(src.shape, dtype=np.uint8) * 100

n = len(contours)  # 輪廓數量
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    img = np.ones(src.shape, dtype=np.uint8) * 127
    # 依序畫每個輪廓 (參數 i)
    print("第", i + 1, "個輪廓")
    # 繪製圖形外輪廓
    dst = cv2.drawContours(dst, contours, i, colors[i], 5)

plt.subplot(221)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

for i in range(n):  # 列印輪廓面積
    area = cv2.moments(contours[i])
    print(f"輪廓面積 str(i) = {area['m00']}")

""" many
for i in range(n):  # 列印影像矩
    M = cv2.moments(contours[i])
    print(f"列印影像矩 {str(i)} \n {M}")
"""

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 5)

for c in contours:  # 繪製中心點迴圈
    M = cv2.moments(c)  # 影像矩
    Cx = int(M["m10"] / M["m00"])  # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])  # 質心 y 座標
    cv2.circle(dst, (Cx, Cy), 5, BLUE, -1)  # 繪製中心點

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("繪製圖形輪廓")
plt.axis("off")

show()

n = len(contours)  # 輪廓數量
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    con_area = cv2.contourArea(contours[i])  # 計算輪廓面積
    print(f"輪廓 {i} 面積 = {con_area}")

n = len(contours)  # 輪廓數量
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    perimeter = cv2.arcLength(contours[i], True)  # 計算輪廓周長
    print(f"輪廓 {i} 周長 = {perimeter}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/3shapes.jpg")  # 彩色讀取
src0 = cv2.imread("data/findContours/myheart.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 2)

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

match0 = cv2.matchShapes(contours[0], contours[0], 1, 0)  # 輪廓0和0比較
print(f"輪廓0和0比較 = {match0}")

match1 = cv2.matchShapes(contours[0], contours[1], 1, 0)  # 輪廓0和1比較
print(f"輪廓0和1比較 = {match1}")

match2 = cv2.matchShapes(contours[0], contours[2], 1, 0)  # 輪廓0和2比較
print(f"輪廓0和2比較 = {match2}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("影像比較 形狀場景運算")

src10 = cv2.imread("data/findContours/mycloud1.jpg")  # 彩色讀取
src1 = src10.copy()

contours, hierarchy = get_image_contours(src1)
cnt1 = contours[0]  # 取得輪廓數據

src20 = cv2.imread("data/findContours/mycloud2.jpg")  # 彩色讀取
src2 = src20.copy()

contours, hierarchy = get_image_contours(src2)
cnt2 = contours[0]  # 取得輪廓數據

src30 = cv2.imread("data/findContours/explode1.jpg")  # 彩色讀取
src3 = src30.copy()

contours, hierarchy = get_image_contours(src3)
cnt3 = contours[0]  # 取得輪廓數據

print("------------------------------")  # 30個

sd = cv2.createShapeContextDistanceExtractor()  # 建立形狀場景運算子
match0 = sd.computeDistance(cnt1, cnt1)  # 影像1 和 影像1 比較
print(f"影像1 和 影像1 比較 = {match0}")

match1 = sd.computeDistance(cnt1, cnt2)  # 影像1 和 影像2 比較
print(f"影像1 和 影像2 比較 = {match1}")

match2 = sd.computeDistance(cnt1, cnt3)  # 影像1 和 影像3 比較
print(f"影像1 和 影像3 比較 = {match2}")

print("------------------------------")  # 30個

cnt3 = contours[0]  # 取得輪廓數據

hd = cv2.createHausdorffDistanceExtractor()  # 建立Hausdorff
match0 = hd.computeDistance(cnt1, cnt1)  # 影像1 和 影像1 比較
print(f"影像1 和 影像1 比較 = {match0}")

match1 = hd.computeDistance(cnt1, cnt2)  # 影像1 和 影像2 比較
print(f"影像1 和 影像2 比較 = {match1}")

match2 = hd.computeDistance(cnt1, cnt3)  # 影像1 和 影像3 比較
print(f"影像1 和 影像3 比較 = {match2}")

print("------------------------------")  # 30個

plt.subplot(131)
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))
plt.title("影像1")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))
plt.title("影像2")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))
plt.title("影像3")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_16_輪廓擬合與凸包的相關應用
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/explode1.jpg")  # 彩色讀取
src0 = cv2.imread("data/findContours/explode2.jpg")  # 彩色讀取
src0 = cv2.imread("data/findContours/explode3.jpg")  # 彩色讀取
src0 = cv2.imread("data/findContours/explode1.jpg")  # 彩色讀取

src1 = src0.copy()
src2 = src0.copy()

contours, hierarchy = get_image_contours(src1)

cnt = contours[0]  # 取得輪廓數據

# 輸出矩形格式
x, y, w, h = cv2.boundingRect(cnt)  # 輸出矩形格式
dst1 = cv2.rectangle(src1, (x, y), (x + w, y + h), GREEN, 2)
aspectratio = w / h  # 計算寬高比
print(f"寬高比 = {aspectratio}")

"""
left = tuple(cnt[cnt[:, :, 0].argmin()][0])  # left
right = tuple(cnt[cnt[:, :, 0].argmax()][0])  # right
top = tuple(cnt[cnt[:, :, 1].argmin()][0])  # top
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])  # bottom
print(f"最左點 = {left}")
print(f"最右點 = {right}")
print(f"最上點 = {top}")
print(f"最下點 = {bottom}")
dst = cv2.circle(src, left, 5, [0, 255, 0], -1)
dst = cv2.circle(src, right, 5, [0, 255, 0], -1)
dst = cv2.circle(src, top, 5, [0, 255, 255], -1)
dst = cv2.circle(src, bottom, 5, [0, 255, 255], -1)
"""
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst2 = cv2.circle(src2, center, radius, GREEN, 2)  # 繪圓

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(312)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("建構矩形")
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("圓圈框選")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/explode2.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

box = cv2.minAreaRect(cnt)  # 建構最小矩形

print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)  # 獲取頂點座標
points = np.int0(points)  # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")

# 繪製圖形外輪廓
dst = cv2.drawContours(src, [points], 0, GREEN, 2)

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("繪製輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/cloud.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(cnt)  # 取得最優擬合橢圓數據

print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(src, ellipse, GREEN, 2)  # 繪橢圓

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("最優擬合橢圓框選")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/heart.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 取得三角形面積與頂點座標
area, triangle = cv2.minEnclosingTriangle(cnt)

print(f"三角形面積   = {area}")
print(f"三角形頂點座標資料類型 = {type(triangle)}")
print(f"三角頂點座標 = \n{triangle}")
triangle = np.int0(triangle)  # 轉整數
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), GREEN, 2)

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("三角形框選")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/multiple.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 近似多邊形包圍

n = len(contours)  # 輪廓數量

src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
for i in range(n):
    approx = cv2.approxPolyDP(contours[i], 3, True)  # epsilon=3
    dst1 = cv2.polylines(src1, [approx], True, GREEN, 2)  # dst1
    approx = cv2.approxPolyDP(contours[i], 15, True)  # epsilon=15
    dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # dst2

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(312)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("多邊形框選 3")  # epsilon = 3
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("多邊形框選 15")  # epsilon = 15
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/unregular.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 擬合一條線
rows, cols = src.shape[:2]  # 輪廓大小
vx, vy, x, y = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)

print(f"共線正規化向量 = {vx}, {vy}")
print(f"直線經過的點   = {x}, {y}")
lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
dst = cv2.line(src, (0, lefty), (cols - 1, righty), GREEN, 2)  # 左到右繪線

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擬合一條線")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
src0 = cv2.imread("data/findContours/hand1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/hand1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

convex_area = cv2.contourArea(hull)  # 計算輪廓面積  # 凸包面積
print(f"凸包面積 = {convex_area}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/hand2.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 凸包

n = len(contours)  # 輪廓數量

for i in range(n):
    hull = cv2.convexHull(contours[i])  # 獲得凸包頂點座標
    dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/star.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包 -> 凸包缺陷
hull = cv2.convexHull(cnt, returnPoints=False)  # 獲得凸包
defects = cv2.convexityDefects(cnt, hull)  # 獲得凸包缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])  # 取得startPoint座標
    end = tuple(cnt[e][0])  # 取得endPoint座標
    far = tuple(cnt[f][0])  # 取得farPoint座標
    dst = cv2.line(src, start, end, [0, 255, 0], 2)  # 凸包連線
    dst = cv2.circle(src, far, 3, [0, 0, 255], -1)  # 繪製farPoint

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包
src1 = src.copy()  # 複製src影像
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst1 = cv2.polylines(src1, [hull], True, GREEN, 2)  # 將凸包連線
isConvex = cv2.isContourConvex(hull)  # 是否凸形
print(f"凸包是凸形       = {isConvex}")

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(312)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

# 近似多邊形包圍
src2 = src.copy()  # 複製src影像
approx = cv2.approxPolyDP(cnt, 10, True)  # epsilon=10
dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # 近似多邊形連線
isConvex = cv2.isContourConvex(approx)  # 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("近似多邊形包圍")  # epsilon = 10
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("點在凸包外")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 凸包
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("點在凸包外")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# OpenCV_17_輪廓的特徵
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/explode1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 3)

cnt = contours[0]  # 取得輪廓數據

con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

# 輸出矩形格式
x, y, w, h = cv2.boundingRect(cnt)  # 輸出矩形格式
dst = cv2.rectangle(src, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

show()

square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print(f"Extent = {extent}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/explode1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 3)

cnt = contours[0]  # 取得輪廓數據

con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

# 凸包
hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, YELLOW, 2)  # 將凸包連線

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找尋影像內的輪廓")
plt.axis("off")

show()

convex_area = cv2.contourArea(hull)  # 計算輪廓面積  # 凸包面積
solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/star1.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

# 繪製圖形外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 3)

cnt = contours[0]  # 取得輪廓數據

con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
dst = cv2.circle(src, (260, 110), int(ed / 2), GREEN, 3)  # 繪製圓

plt.subplot(211)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("等效面積")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")

nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/simple.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

image_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

mask1 = np.zeros(image_gray.shape, np.uint8)  # 建立畫布

# 繪製圖形外輪廓(填滿)
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓

points1 = np.transpose(np.nonzero(dst1))

mask2 = np.zeros(image_gray.shape, np.uint8)  # 建立畫布

# 繪製圖形外輪廓(填滿)
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓

points2 = np.transpose(np.nonzero(dst2))

print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(312)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("空心像素點")
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("實心像素點")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")

loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/simple.jpg")  # 彩色讀取
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

mask1 = np.zeros(image_gray.shape, np.uint8)  # 建立畫布

# 繪製圖形外輪廓(填滿)
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓

points1 = cv2.findNonZero(dst1)
mask2 = np.zeros(image_gray.shape, np.uint8)  # 建立畫布

# 繪製圖形外輪廓(填滿)
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓

points2 = cv2.findNonZero(dst2)
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)

plt.subplot(311)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(312)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("空心像素點")
plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("實心像素點")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/hand.jpg")  # 彩色讀取  # 手上有一黑點與一白點
src = src0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 製作mask
mask = np.zeros(image_gray.shape, np.uint8)  # 建立遮罩

# 繪製圖形外輪廓(填滿)
mask = cv2.drawContours(mask, [cnt], -1, WHITE, -1)

plt.subplot(221)
plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")
plt.axis("off")

# 在src_gray影像的mask遮罩區域找尋最大像素與最小像素值
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(image_gray, mask=mask)
print(f"最小像素值 = {minVal}")
print(f"最小像素值座標 = {minLoc}")
print(f"最大像素值 = {maxVal}")
print(f"最大像素值座標 = {maxLoc}")
cv2.circle(src, minLoc, 20, [0, 255, 0], 3)  # 最小像素值用綠色圓
cv2.circle(src, maxLoc, 20, [0, 0, 255], 3)  # 最大像素值用紅色圓

# 建立遮罩未來可以顯示此感興趣的遮罩區域
mask1 = np.zeros(src.shape, np.uint8)  # 建立遮罩

# 繪製圖形外輪廓(填滿)
mask1 = cv2.drawContours(mask1, [cnt], -1, WHITE, -1)

plt.subplot(223)
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))
plt.title("mask1")
plt.axis("off")

dst = cv2.bitwise_and(src, mask1)  # 顯示感興趣區域

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("顯示感興趣區域")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src0 = cv2.imread("data/findContours/hand.jpg")  # 彩色讀取  # 手上有一黑點與一白點
src = src0.copy()

image_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 在src_gray影像的mask遮罩區域計算均值

# 製作mask
mask = np.zeros(image_gray.shape, np.uint8)  # 建立遮罩

# 繪製圖形外輪廓(填滿)
mask = cv2.drawContours(mask, [cnt], -1, WHITE, -1)

channels = cv2.mean(src, mask=mask)  # 計算遮罩的均值
print(channels)

plt.imshow(cv2.cvtColor(src0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 contours")

image0 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image = image0.copy()

# 邊緣檢測或閾值分割的二值化
binaryImg = cv2.Canny(image, 50, 200)

# 尋找輪廓
contours, hierarchy = cv2.findContours(binaryImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

get_contours_info(contours)

# 對這些點集，求每一個點集最小
# 最小外包凸包
contoursImg = np.zeros(image.shape, np.uint8)

# 繪製圖形外輪廓
cv2.drawContours(contoursImg, contours, 7, 255, 3)  # 多點頭尾連線

circle = cv2.minEnclosingCircle(contours[7])
cv2.circle(contoursImg, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), 255, 2)

convexhull = cv2.convexHull(contours[7])

# 繪製圖形外輪廓
cv2.drawContours(contoursImg, contours, 7, 255, 3)  # 多點頭尾連線

n = len(contours)  # 輪廓數量
for i in range(n):
    # ----- 最小外包圓 -------
    circle = cv2.minEnclosingCircle(contours[i])
    # 畫圓
    # cv2.circle(image, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), 255, 2)
    # ---- 最小直立矩形 ----
    x, y, w, h = cv2.boundingRect(contours[i])  # 輸出矩形格式
    # cv2.rectangle(image, (x, y), (w, h), 255, 2)
    # ---- 最小外包的旋轉矩形 -----
    convexhull = cv2.convexHull(contours[i])

# 最小直立矩形
cvshow("image", image)

# 顯示輪廓
cvshow("contoursImg", contoursImg)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("image")

plt.subplot(122)
plt.imshow(cv2.cvtColor(contoursImg, cv2.COLOR_BGR2RGB))
plt.title("contoursImg")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合")

image0 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image = image0.copy()

# 第二步：邊緣檢測 或者 閾值處理 生成一張二值圖
image = cv2.GaussianBlur(image, (3, 3), 0.5)  # 高斯平滑處理    #執行高斯模糊化
binaryImg = cv2.Canny(image, 50, 200)
cvshow("binaryImg", binaryImg)

contours, hierarchy = cv2.findContours(
    binaryImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

get_contours_info(contours)

n = len(contours)  # 輪廓數量

contoursImg = []
# 畫出找到的輪廓
for i in range(n):
    # 創建一個黑色畫布
    temp = np.zeros(binaryImg.shape, np.uint8)
    contoursImg.append(temp)
    # 在第 i 個黑色畫布上，畫第 i 個輪廓
    # 繪製圖形外輪廓
    cv2.drawContours(contoursImg[i], contours, i, 255, 2)  # 多點頭尾連線
    cvshow("contour-" + str(i), contoursImg[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 findContours")

# filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image0 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image = image0.copy()

# 第一步：閾值化，生成二值圖
# 圖像平滑
dst = cv2.GaussianBlur(image, (3, 3), 0.5)  # 執行高斯模糊化
# Otsu 閾值分割
OtsuThresh = 0
OtsuThresh, dst = cv2.threshold(dst, OtsuThresh, 255, cv2.THRESH_OTSU)
# --- 形態學開運算（ 消除細小白點 ）
# 創建結構元
s = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, s, iterations=2)

# 第二步：尋找二值圖的輪廓，返回值是一個元組，hc[1] 代表輪廓
hc = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = hc[1]
print(contours)

get_contours_info(contours)

# 第三步：畫出找到的輪廓并用多邊形擬合輪廓
# 輪廓的數量
n = len(hc[1])
print("n =", n)
# 將輪廓畫在該黑板上
print(image.shape)

contoursImg = np.zeros(image.shape, np.uint8)

# NG
"""
for i in range(n):
    # 繪製圖形外輪廓
    cv2.drawContours(contoursImg, contours, i, 255, 2)  #  多點頭尾連線
    # 畫出輪廓的最小外包圓
    circle = cv2.minEnclosingCircle(contours[i])
    cv2.circle(image, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), 0, 5)
    # 多邊形逼近（注意與凸包區別）
    approxCurve = cv2.approxPolyDP(contours[i], 0.3, True)
    # 多邊形頂點個數
    k = approxCurve.shape[0]
    # 頂點連接，繪制多邊形
    for i in range(k - 1):
        cv2.line(
            image,
            (approxCurve[i, 0, 0], approxCurve[i, 0, 1]),
            (approxCurve[i + 1, 0, 0], approxCurve[i + 1, 0, 1]),
            0,
            5,
        )
    # 首尾相接
    cv2.line(
        image,
        (approxCurve[k - 1, 0, 0], approxCurve[k - 1, 0, 1]),
        (approxCurve[0, 0, 0], approxCurve[0, 0, 1]),
        0,
        5,
    )

# 顯示輪廓
cvshow("contours", contoursImg)

# 顯示擬合的多邊形
cvshow("dst", image)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(contoursImg, cv2.COLOR_BGR2RGB))
plt.title("顯示輪廓")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示擬合的多邊形")

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 形狀與結構分析
# 輪廓檢驗

coin_filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"

image0 = cv2.imread(coin_filename, cv2.IMREAD_COLOR)  # 彩色讀取
image = image0.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

img_coin_blur = cv2.GaussianBlur(image_gray, (0, 0), 1.5, 1.5)
img_coin_binary = cv2.Canny(img_coin_blur.copy(), 60, 60)
img_coin_binary = cv2.morphologyEx(
    img_coin_binary, cv2.MORPH_CLOSE, np.ones((3, 3), "uint8")
)

for approx in ["NONE", "SIMPLE", "TC89_KCOS", "TC89_L1"]:
    approx_flag = getattr(cv2, "CHAIN_APPROX_{}".format(approx))
    contours, hierarchy = cv2.findContours(
        img_coin_binary.copy(), cv2.RETR_EXTERNAL, approx_flag
    )
    print("{}: {}  ".format(approx, sum(contour.shape[0] for contour in contours)))

# NONE: 3179   SIMPLE: 1579   TC89_KCOS: 849   TC89_L1: 802


# 顯示所有圓度在0.8到1.2之間的輪廓
def circularity(contour):
    perimeter = cv2.arcLength(contour, True)  # 計算輪廓周長
    con_area = cv2.contourArea(contour) + 1e-6  # 計算輪廓面積
    return perimeter * perimeter / (4 * np.pi * con_area)


contours = [contour for contour in contours if 0.8 < circularity(contour) < 1.2]

# 繪製圖形外輪廓(填滿)
cv2.drawContours(image, contours, -1, RED)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("輪廓檢驗")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image0 = cv2.imread("data/nested_patterns.png")  # 彩色讀取
image = image0.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 二值化處理影像
thresh = 100  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    dst_binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1
)
get_contours_info(contours)

hierarchy.shape = -1, 4

root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]
print(root_index)

# [0, 7, 19]


def get_children(hierarchy, index):
    first_child = hierarchy.item(index, 2)
    if first_child >= 0:
        yield first_child
        brother = hierarchy.item(first_child, 0)
        while brother >= 0:
            yield brother
            brother = hierarchy.item(brother, 0)


def get_descendant(hierarchy, index, level=1):
    for child in get_children(hierarchy, index):
        yield level, child
        for item in get_descendant(hierarchy, child, level + 1):
            yield item


print(list(get_descendant(hierarchy, 0)))

# [(1, 1), (2, 2), (3, 3), (2, 4), (3, 5), (3, 6)]

# %figonly=顯示輪廓的階層結構
root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]

lines = []
levels = []

for index in root_index:
    items = zip(*get_descendant(hierarchy, index))
    if items:
        children_level, children_index = items
        lines.extend([contours[i] for i in children_index])
        levels.extend(children_level)
    lines.append(contours[index])
    levels.append(0)

lines = [line[:, 0, :] for line in lines]

# 使用matplotlib.collections顯示大量曲線
from matplotlib import collections as mc

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
polys = mc.PolyCollection(lines, array=np.array(levels), facecolors="none")
ax.add_collection(polys)
ax.set_xlim(0, image.shape[1])
ax.set_ylim(image.shape[0], 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_cs1 = "C:/_git/vcs/_4.python/opencv/data/cs1.bmp"

image = cv2.imread(filename_cs1)  # 彩色讀取
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 100  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# 找出圖像中的輪廓
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找出最大的輪廓
filtered_contours = max(contours, key=cv2.contourArea)

# 取得該輪廓的最小包圍矩形及角度
rect = cv2.minAreaRect(filtered_contours)  # ((center_x, center_y), (w, h), angle)
box = cv2.boxPoints(rect)  # 轉換為4個頂點

# box = np.int0(box)  # 將頂點轉換為整數座標 #np 1.24 以下使用
box = np.intp(box)

# 繪製最小包圍矩形
# 繪製圖形外輪廓
cv2.drawContours(image, [box], 0, RED, 3)  # 綠色框，線寬為2

# 取得旋轉矩形的中心點和旋轉角度
(center_x, center_y), (w, h), angle = rect

# 顯示中心點和旋轉角度在圖片上
center_text = f"Center: ({int(center_x)}, {int(center_y)})"
angle_text = f"Angle: {int(angle)} degrees"

cv2.circle(image, (int(center_x), int(center_y)), 10, BLUE, -1)  # 圆

# 在圖像上寫入文字
cv2.putText(
    image, center_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2
)  # 藍色字體
cv2.putText(
    image, angle_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2
)  # 藍色字體

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# boxPoints 帶有旋轉的矩形框座標


def draw_boxpoints(points):
    # print(points)  # 打印四個頂點
    for i in range(4):
        # 相鄰的點
        p1 = points[i, :]
        j = (i + 1) % 4
        p2 = points[j, :]
        # print(i, points[i], points[j])

        # 畫出直線
        cv2.line(
            image,
            (int(p1[0]), int(p1[1])),
            (int(p2[0]), int(p2[1])),
            RED,
            7,
            lineType=cv2.LINE_AA,
        )

        # 畫出來, 另法, 用drawContours
        points = np.int0(points)  # 取整數
        # 繪製圖形外輪廓
        cv2.drawContours(image, [points], 0, GREEN, 3)


# boxPoints返回四個點順序：右下→左下→左上→右上

image = cv2.imread("data/cc.bmp")  # 彩色讀取

imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

contours, hierarchy = cv2.findContours(
    imagegray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

rect = cv2.minAreaRect(contours[0])  # 得到最小外接矩形的（中心(x,y), (寬,高), 旋轉角度）

print("最小外接矩形 :", rect)
print("中心 :", rect[0])
print("寬高 :", rect[1])
print("旋轉角度 :", rect[2])

cx = rect[0][0]
cy = rect[0][1]

print("中心 :", cx, cy)
W = rect[1][0] * 2
H = rect[1][1] * 2
print("W = ", W, "H = ", H)

points = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
print("最小外接矩形 :", points)

# 把矩形的四個頂點標出來
for point in points:
    cv2.circle(image, (int(point[0]), int(point[1])), 10, 255, 5)

draw_boxpoints(points)  # 畫出四個頂點連線

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

cv2.imshow("original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n", rect)

points = cv2.boxPoints(rect)
print("\n轉換后的points：\n", points)

draw_boxpoints(points)  # 畫出四個頂點連線

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H = 400, 400

# 根據四個頂點在黑色畫板上畫出該矩形
image = np.zeros((H, W, 3), np.uint8)

cx, cy = 200, 200
w, h = W // 2, H // 4

rotating_angle = 0  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

rotating_angle = 20  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 輸出邊緣和結構信息

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure("輸出邊緣和結構信息", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

o = cv2.drawContours(image, contours, -1, RED, 5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("輸出邊緣和結構信息")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

n = len(contours)  # 輪廓數量

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 5)
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/loc3.jpg")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image.shape, np.uint8)

mask = cv2.drawContours(mask, contours, -1, WHITE, -1)

loc = cv2.bitwise_and(image, mask)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(133)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("location")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/moments.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 輪廓數量

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, 255, 3)
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

print("觀察各個輪廓的矩（moments）:")
for i in range(n):
    print("輪廓" + str(i) + "的矩:\n", cv2.moments(contours[i]))
print("觀察各個輪廓的面積:")
for i in range(n):
    print("輪廓" + str(i) + "的面積:%d" % cv2.moments(contours[i])["m00"])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 輪廓數量

contoursImg = []
for i in range(n):
    print("contours[" + str(i) + "]面積=", cv2.contourArea(contours[i]))
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 篩選出大于特定大小的輪廓

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(
    gray,
    thresh,
    maxval,
)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 輪廓數量

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    if cv2.contourArea(contours[i]) > 15000:
        # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
        index = "22" + str(i + 2)
        plt.subplot(int(index))
        plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
        plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cs1.bmp")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

HuM1 = cv2.HuMoments(cv2.moments(gray)).flatten()

print("cv2.moments(gray)=\n", cv2.moments(gray))
print("\nHuM1=\n", HuM1)
print(
    "\ncv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']=%f+%f=%f\n"
    % (
        cv2.moments(gray)["nu20"],
        cv2.moments(gray)["nu02"],
        cv2.moments(gray)["nu20"] + cv2.moments(gray)["nu02"],
    )
)
print("HuM1[0]=", HuM1[0])
print(
    "\nHu[0]-(nu02+nu20)=",
    HuM1[0] - (cv2.moments(gray)["nu20"] + cv2.moments(gray)["nu02"]),
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ----------------計算圖像1的Hu矩-------------------
image1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()

# ----------------計算圖像2的Hu矩-------------------
image2 = cv2.imread("data/cs3.bmp")  # 彩色讀取
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()

# ----------------計算圖像3的Hu矩-------------------
filename = filename_lena_gray

image3 = cv2.imread(filename)  # 彩色讀取
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

# ---------打印圖像1、圖像2、圖像3的特征值------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
print("cv2.moments(gray1)=\n", cv2.moments(gray1))
print("cv2.moments(gray2)=\n", cv2.moments(gray2))
print("cv2.moments(gray3)=\n", cv2.moments(gray3))
print("\nHuM1=\n", HuM1)
print("\nHuM2=\n", HuM2)
print("\nHuM3=\n", HuM3)

# ---------計算圖像1與圖像2、圖像3的Hu矩之差----------------
print("\nHuM1-HuM2=", HuM1 - HuM2)
print("\nHuM1-HuM3=", HuM1 - HuM3)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("original1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("original2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("original3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Opencv之利用matchshape算子实现简单的形状匹配
"""
使用OpenCV的matchShape算子进行形状匹配。
通过将待识别图像和模板图像转换为灰度并进行阈值处理，然后找到轮廓，
最后通过比较轮廓的Hu不变矩来确定匹配度。匹配分值越小，轮廓越相似。
matchShapes函数适用于识别大物体的形状，但对纹理复杂的图像识别率较低。
"""

# --------------讀取3幅原始圖像--------------------
image1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
image2 = cv2.imread("data/cs2.bmp")  # 彩色讀取
image3 = cv2.imread("data/cc.bmp")  # 彩色讀取

# ----------打印3幅原始圖像的shape屬性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)

# --------------色彩空間轉換--------------------
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# -------------進行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0.0)

# --------------打印差值--------------------
print("相同圖像的matchShape=", ret0)
print("相似圖像的matchShape=", ret1)
print("不相似圖像的matchShape=", ret2)

# --------------顯示3幅原始圖像--------------------
plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("original1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("original2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("original3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 輪廓比對")

img_patterns = cv2.imread("data/patterns.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

patterns, _ = cv2.findContours(img_patterns, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_targets = cv2.imread("data/targets.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

targets, _ = cv2.findContours(img_targets, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

patterns = [pattern - np.min(pattern, 0, keepdims=True) for pattern in patterns]
targets = [target - np.min(target, 0, keepdims=True) for target in targets]

patterns_simple = [cv2.approxPolyDP(pattern, 5, True) for pattern in patterns]
targets_simple = [cv2.approxPolyDP(target, 8, True) for target in targets]


for method in [1, 2, 3]:
    method_str = "CONTOURS_MATCH_I{}".format(method)
    method = getattr(cv2, method_str)
    scores = [
        cv2.matchShapes(targets_simple[0], patterns_simple[pidx], method, 0)
        for pidx in range(5)
    ]
    print(method_str, ", ".join("{: 8.4f}".format(score) for score in scores))

# CV_CONTOURS_MATCH_I1  11.3737,   0.3456,   0.0289,   1.0495,   0.0020
# CV_CONTOURS_MATCH_I2   4.8051,   2.2220,   0.0179,   0.3624,   0.0013
# CV_CONTOURS_MATCH_I3   0.9164,   0.4778,   0.0225,   0.4552,   0.0016

# %figonly=使用`matchShapes()`比較由`approxPolyDP()`近似之後的輪廓
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect("equal")

width = 180
for tidx, (target, target_simple) in enumerate(zip(targets, targets_simple)):
    scores = []
    texts = []
    for pidx, (pattern, pattern_simple) in enumerate(zip(patterns, patterns_simple)):
        index = np.s_[:, 0, :]
        pattern2 = pattern[index]
        target2 = target[index]
        pattern_simple2 = pattern_simple[index]
        target_simple2 = target_simple[index]

        x0 = pidx * width + width
        y0 = tidx * width + width

        if tidx == 0:
            pattern_poly = plt.Polygon(pattern2 + [x0, 0], color="black", alpha=0.6)
            ax.add_patch(pattern_poly)
            text = ax.text(x0 + width * 0.3, -50, str(pidx), fontsize=14, ha="center")
        if pidx == 0:
            target_poly = plt.Polygon(target2 + [0, y0], color="g", alpha=0.6)
            ax.add_patch(target_poly)
            text = ax.text(-50, y0 + width * 0.3, str(tidx), fontsize=14, ha="center")

        pattern_simple_poly = plt.Polygon(
            pattern_simple2 + [x0, 0], facecolor="none", alpha=0.6
        )
        ax.add_patch(pattern_simple_poly)
        target_simple_poly = plt.Polygon(
            target_simple2 + [0, y0], facecolor="none", alpha=0.6
        )
        ax.add_patch(target_simple_poly)

        score = cv2.matchShapes(target_simple, pattern_simple, cv2.CONTOURS_MATCH_I3, 0)
        text = ax.text(
            x0 + width * 0.3,
            y0 + width * 0.2,
            "{:5.4f}".format(score),
            ha="center",
            va="center",
            fontsize=16,
        )
        scores.append(score)
        texts.append(text)
    best_index = np.argmin(scores)
    texts[best_index].set_color("red")

ax.relim()
ax.set_axis_off()
ax.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ---------------返回頂點及邊長------------------
x, y, w, h = cv2.boundingRect(contours[0])
print("頂點及長寬的點形式:")
print("x=", x)
print("y=", y)
print("w=", w)
print("h=", h)
# ---------------僅有一個返回值的情況------------------
rect = cv2.boundingRect(contours[0])
print("\n頂點及長寬的元組（tuple）形式：")
print("rect=", rect)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv2.drawContours(image, [brcnt], -1, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(image, (x, y), (x + w, y + h), RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(image, center, radius, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("圓圈圈出來")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

ellipse = cv2.fitEllipse(contours[0])
print("ellipse=", ellipse)
cv2.ellipse(image, ellipse, GREEN, 3)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("橢圓形圈出來")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rows, cols = image.shape[:2]
[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(image, (cols - 1, righty), (0, lefty), GREEN, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("直線貫通")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# some NG
image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area, trgl = cv2.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl:", trgl)
for i in range(0, 3):
    print("x")
    # cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), WHITE, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ----------------獲取輪廓-------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ----------------epsilon=0.1*周長-------------------------------
adp = image.copy()
epsilon = 0.1 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(232)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.1")

# ----------------epsilon=0.09*周長-------------------------------
adp = image.copy()
epsilon = 0.09 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(233)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.09")

# ----------------epsilon=0.055*周長-------------------------------
adp = image.copy()
epsilon = 0.055 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(234)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.055")

# ----------------epsilon=0.05*周長-------------------------------
adp = image.copy()
epsilon = 0.05 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(235)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.05")

# ----------------epsilon=0.02*周長-------------------------------
adp = image.copy()
epsilon = 0.02 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(236)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.02")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])  # 返回坐標值
print("returnPoints為默認值True時返回值hull的值：\n", hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)  # 返回索引值
print("returnPoints為False時返回值hull的值：\n", hull2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# --------------提取輪廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------尋找凸包，得到凸包的角點------------------
hull = cv2.convexHull(contours[0])
# --------------繪製凸包------------------
cv2.polylines(o, [hull], True, GREEN, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("顯示凸包")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ----------------原圖--------------------------
img = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ----------------構造輪廓--------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# ----------------凸包--------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("defects=\n", defects)

# ----------------構造凸缺陷--------------------------
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, RED, 2)
    cv2.circle(img, far, 5, BLUE, -1)

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("顯示結果")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# --------------凸包----------------------
image1 = o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, GREEN, 2)
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：", cv2.isContourConvex(hull))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("result1")

# ------------逼近多邊形--------------------
image2 = o.copy()
epsilon = 0.01 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, RED, 2)
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：", cv2.isContourConvex(approx))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("result2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ----------------原始圖像-------------------------
o = cv2.imread("data/cs1.bmp")  # 彩色讀取

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)

# ----------------內部點A的距離-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)
# ----------------外部點B的距離-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)
# ------------正好處于邊緣上的點C的距離-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的


plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("邊緣")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs1.bmp")  # 彩色讀取

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)
# ----------------內部點A與多邊形的關系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)
# ----------------外部點B與多邊形的關系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)
# ----------------邊緣線上點C與多邊形的關系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("邊緣")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# -----------原始圖像o1邊緣--------------------
o1 = cv2.imread("data/cs1.bmp")  # 彩色讀取

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]

# -----------原始圖像o2邊緣--------------------
o2 = cv2.imread("data/cs3.bmp")  # 彩色讀取

gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]

# -----------原始圖像o3邊緣--------------------
o3 = cv2.imread("data/hand.bmp")  # 彩色讀取

gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]
# -----------構造距離提取算子--------------------
sd = cv2.createShapeContextDistanceExtractor()
# -----------計算距離--------------------
d1 = sd.computeDistance(cnt1, cnt1)
print("自身距離d1=", d1)
d2 = sd.computeDistance(cnt1, cnt2)
print("旋轉縮放后距離d2=", d2)
d3 = sd.computeDistance(cnt1, cnt3)
print("不相似對象距離d3=", d3)
# -----------顯示距離--------------------

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(o2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(o3, cv2.COLOR_BGR2RGB))
plt.title("原圖3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
o2 = cv2.imread("data/cs3.bmp")  # 彩色讀取
o3 = cv2.imread("data/hand.bmp")  # 彩色讀取

# -----------色彩轉換--------------------
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# -----------閾值處理--------------------

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# -----------提取輪廓--------------------
contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]

# -----------構造距離提取算子--------------------
hd = cv2.createHausdorffDistanceExtractor()

# -----------計算距離--------------------
d1 = hd.computeDistance(cnt1, cnt1)
print("自身Hausdorff距離d1=", d1)
d2 = hd.computeDistance(cnt1, cnt2)
print("旋轉縮放后Hausdorff距離d2=", d2)
d3 = hd.computeDistance(cnt1, cnt3)
print("不相似對象Hausdorff距離d3=", d3)

# -----------顯示距離--------------------

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(o2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(o3, cv2.COLOR_BGR2RGB))
plt.title("原圖3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(o, (x, y), (x + w, y + h), WHITE, 3)

aspectRatio = float(w) / h
print(aspectRatio)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.drawContours(o, contours[0], -1, RED, 3)
cv2.rectangle(o, (x, y), (x + w, y + h), BLUE, 3)

rectArea = w * h
cntArea = cv2.contourArea(contours[0])
extend = float(cntArea) / rectArea
print(extend)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o, contours[0], -1, RED, 3)
cntArea = cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o, [hull], True, GREEN, 2)
solidity = float(cntArea) / hullArea
print(solidity)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(o, contours[0], -1, RED, 3)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4 * cntArea / np.pi)
print(equiDiameter)
cv2.circle(o, (100, 100), int(equiDiameter / 2), RED, 3)  # 展示等直徑大小的圓

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
ellipse = cv2.fitEllipse(contours[0])
retval = cv2.fitEllipse(contours[0])
print("單個返回值形式：")
print("retval=\n", retval)
(x, y), (MA, ma), angle = cv2.fitEllipse(contours[0])
print("三個返回值形式：")
print("(x,y)=(", x, y, ")")
print("(MA,ma)=(", MA, ma, ")")
print("angle=", angle)
cv2.ellipse(o, ellipse, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ------------生成一個都是0值的a-------------------
a = np.zeros((5, 5), dtype=np.uint8)
# -------隨機將其中10個位置上的數值設置為1------------
# ---times控制次數
# ---i,j是隨機生成的行、列位置
# ---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1
# -------打印a，觀察a內值的情況-----------
print("a=\n", a)
# ------查找a內非零值的位置信息------------
loc = np.transpose(np.nonzero(a))
# -----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n", loc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# -----------------讀取原始圖像----------------------
o = cv2.imread("data/cc.bmp")  # 彩色讀取

# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))
plt.title("mask1")

plt.subplot(133)
plt.imshow(cv2.cvtColor(mask2, cv2.COLOR_BGR2RGB))
plt.title("mask2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ------------生成一個都是0值的a-------------------
a = np.zeros((5, 5), dtype=np.uint8)
# -------隨機將其中10個位置上的數值設置為1------------
# ---times控制次數
# ---i,j是隨機生成的行、列位置
# ---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1
# -------打印a，觀察a內值的情況-----------
print("a=\n", a)
# ------查找a內非零值的位置信息------------
loc = cv2.findNonZero(a)
# -----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n", loc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))
plt.title("mask1")

plt.subplot(133)
plt.imshow(cv2.cvtColor(mask2, cv2.COLOR_BGR2RGB))
plt.title("mask2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/ct.png")  # 彩色讀取

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]  # coutours[0]、coutours[1]是左側字母R
# --------使用掩膜獲取感興趣區域的最值-----------------
# 需要注意minMaxLoc處理的對象為灰度圖像，本例中處理對象為灰度圖像gray
# 如果希望獲取彩色圖像的，需要提取各個通道，將每個通道獨立計算最值
mask = np.zeros(gray.shape, np.uint8)
mask = cv2.drawContours(mask, [cnt], -1, 255, -1)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray, mask=mask)
print("minVal=", minVal)
print("maxVal=", maxVal)
print("minLoc=", minLoc)
print("maxLoc=", maxLoc)
# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
masko = cv2.drawContours(masko, [cnt], -1, WHITE, -1)
loc = cv2.bitwise_and(o, masko)

# 顯示灰度結果
# loc=cv2.bitwise_and(gray,mask)
# cv2.imshow("mask",loc)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/ct.png")  # 彩色讀取

# --------獲取輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]
# --------使用掩膜獲取感興趣區域的均值-----------------
mask = np.zeros(gray.shape, np.uint8)  # 構造mean所使用的掩膜，必須是單通道的
cv2.drawContours(mask, [cnt], 0, WHITE, -1)
meanVal = cv2.mean(o, mask=mask)  # mask是區域，所以必須是單通道的
print("meanVal=\n", meanVal)
# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
cv2.drawContours(masko, [cnt], -1, WHITE, -1)
loc = cv2.bitwise_and(o, masko)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs1.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# --------獲取并繪製輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
cnt = contours[0]
cv2.drawContours(mask, [cnt], 0, 255, -1)
# --------計算極值-----------------
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
# --------計算極值-----------------
print("leftmost=", leftmost)
print("rightmost=", rightmost)
print("topmost=", topmost)
print("bottommost=", bottommost)
# --------繪製說明文字-----------------
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, "A", leftmost, font, 1, RED, 2)
cv2.putText(o, "B", rightmost, font, 1, RED, 2)
cv2.putText(o, "C", topmost, font, 1, RED, 2)
cv2.putText(o, "D", bottommost, font, 1, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# OpenCV 輪廓檢測- contour detection(籃網偵測,字母模板偵測)

# 原圖
filename = "data/basketball.jpg"
image10 = cv2.imread(filename)  # 彩色讀取

cv2.imshow("BGR image", image10)
cv2.waitKey(0)
cv2.destroyAllWindows()

image11 = image10.copy()

# 轉灰階
image12 = cv2.cvtColor(image11, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image12)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 轉二元圖
ret, image13 = cv2.threshold(image12, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", image13)
cv2.waitKey(0)
cv2.destroyAllWindows()


contours, hierarchy = cv2.findContours(
    image13, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
# 設定一下drawContours的參數
contours_to_plot = -1  # 畫全部
plotting_color = (0, 0, 255)  # 畫紅色框
thickness = -1
# 開始畫contours
with_contours = cv2.drawContours(
    image10, contours, contours_to_plot, plotting_color, thickness
) # image10 也被畫上東西
cv2.imshow("contours", with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 標示矩形邊框
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    image = cv2.rectangle(image10, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 畫綠色框
cv2.imshow("contours", image10)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 根據面積，挑出籃網的部分
required_contour = max(contours, key=cv2.contourArea)  # 取出最大面積
x, y, w, h = cv2.boundingRect(required_contour)
image14 = cv2.rectangle(image11, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 畫藍色框
cv2.imshow("largest contour", image14)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.boundingRect
矩形邊框（Bounding Rectangle）是說，用一個最小的矩形，把找到的形狀包起來。
cv2.boundingRect(img)
img是一個二值圖，也就是它的參數；
返回四個值，分別是x，y，w，h（ x，y是矩型左上點的坐標，w，h是矩型的寬和高）

cv2.contourArea
計算輪廓的面積
cv2.contourArea(contour， oriented=True)
contour：表示某輸入單個輪廓，為array
oriented：表示某個方向上輪廓的面積值，這裡指順時針或者逆時針。若為True，該函數返回一個帶符號的面積值，正負值取決於輪廓的方向（順時針還是逆時針），若為False，表示以絕對值返回

cv2.arcLength
計算輪廓的周長
cv2.arcLength(contour， closed=True)
contour：表示某輸入單個輪廓，為array
closed：用於指示曲線是否封閉

cv2.approxPolyDP
cv2.approxPolyDP()函數是輪廓近似函數，是opencv中對指定的點集進行多邊形逼近的函數，其逼近的精度可通過參數設置
approxPolyDP(curve, epsilon, closed, approxCurve=None)
curve：表示輸入的點集
epslion：指定的精度，也即原始曲線與近似曲線之間的最大距離，不過這個值我們一般按照周長的大小進行比較
close：若為True，則說明近似曲線為閉合的；反之，若為False，則斷開

"""

# 找模板實作比對

# 原圖
filename = "data/phrase_handwritten.jpg"
image10 = cv2.imread(filename)  # 彩色讀取
cv2.imshow("Original image", image10)
cv2.waitKey(0)
cv2.destroyAllWindows()

image11 = image10.copy()

# 轉灰階
image12 = cv2.cvtColor(image10, cv2.COLOR_BGR2GRAY)

# 轉二元
ret, image13 = cv2.threshold(image12, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("binary image", image13)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 找輪廓
contours_list, hierarchy = cv2.findContours(
    image13, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
for cnt in contours_list:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image10, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 畫紅色框
cv2.imshow("Contours marked on RGB image", image10)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 做模板
filename = "data/b3.jpg"
ref_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
ret, ref_binary = cv2.threshold(ref_gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Reference image", ref_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 開始比較
ref_contour_list, hierarchy = cv2.findContours(
    ref_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print(len(ref_contour_list))
if len(ref_contour_list) == 1:
    ref_contour = ref_contour_list[0]
else:
    print("找到的模板輪廓超過1個，需要確認一下用哪一個?")
    ref_contour = ref_contour_list[0]

ctr = 0
dist_list = []
for cnt in contours_list:
    retval = cv2.matchShapes(cnt, ref_contour, cv2.CONTOURS_MATCH_I1, 0)
    dist_list.append(retval)
    ctr = ctr + 1

min_dist = min(dist_list)  # 找出距離最近的
ind_min_dist = dist_list.index(min_dist)  # 挑出那張圖
required_cnt = contours_list[ind_min_dist]
x, y, w, h = cv2.boundingRect(required_cnt)

filename = "data/phrase_handwritten.jpg"
imagecopy = cv2.imread(filename)  # 彩色讀取
cv2.rectangle(imagecopy, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow("Detected B", imagecopy)
cv2.waitKey(0)
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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------")  # 30個


"""
    for contour in contours:
        con_area = cv2.contourArea(contour)  # 計算輪廓面積
        # print("輪廓面積 :", con_area)
        if con_area > 300:
            x, y, w, h = cv2.boundingRect(contour)  # 輸出矩形格式
            img = cv2.rectangle(img, (x, y), (x + w, y + h), RED, 3)  # 繪製四邊形

    for contour in contours:
        con_area = cv2.contourArea(contour)  # 計算輪廓面積
        # print("輪廓面積 :", con_area)
        # 如果面積大於 300 再標記，避免標記到背景中太小的東西
        if con_area > 300:
            for i in range(len(contour)):
                if i > 0 and i < len(contour) - 1:
                    # 從第二個點開始畫線
                    img = cv2.line(
                        img,
                        (contour[i - 1][0][0], contour[i - 1][0][1]),
                        (contour[i][0][0], contour[i][0][1]),
                        RED,
                        3,
                    )
                elif i == len(contour) - 1:
                    # 如果是最後一個點，與第一個點連成一線
                    img = cv2.line(
                        img,
                        (contour[i][0][0], contour[i][0][1]),
                        (contour[0][0][0], contour[0][0][1]),
                        RED,
                        3,
                    )

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([[[186, 39]], [[181, 44]], [[180, 44]]])
print(f"原始資料data = \n{data}")
n = len(data)
print("取3維內的陣列資料")
for i in range(n):  # 列印 3 個座標點
    print(data[i])
print(f"資料維度   = {data.ndim}")  # 維度
max_i = data[:, :, 0].argmax()  # x 最大值索引索引
print(f"x 最大值索引 = {max_i}")  # 列印 x 最大值索引
right = tuple(data[data[:, :, 0].argmax()][0])  # 最大值元組
print(f"最大值元組 = {right}")  # 列印最大值元組
min_i = data[:, :, 0].argmin()  # x 最小值索引索引
print(f"x 最小值索引 = {min_i}")  # 列印 x 最小值索引
left = tuple(data[data[:, :, 0].argmin()][0])  # 最小值元組
print(f"最小值元組 = {left}")  # 列印最小值元組

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# dilate_erode1.png用圖片先處理方法二
# filename = "C:/_git/vcs/_4.python/opencv/data/dilate_erode1.png"

# 可刪除檔案
src = cv2.imread("data/findContours/heart.jpg")  # 彩色讀取
src = cv2.imread("data/findContours/3heart.jpg")  # 彩色讀取


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
2.retrieval_mode-擷取模式

cv2.RETR_EXTERNAL-只擷取最外圍的輪廓
cv2.RETR_LIST-擷取大大小小所有輪廓，擷取結果沒有父子關係，大家都平等
cv2.RETR_CCOMP-會列出內、外兩層關係
cv2.RETR_TREE-會列出完整所有關係

3.approx_method-輪廓紀錄方式

cv2.CHAIN_APPROX_NONE-最精細紀錄模式
cv2.CHAIN_APPROX_SIMPLE-只記錄畫出輪廓的關鍵點

把輪廓畫出來-
drawContours語法
marked_img = cv2.drawContours(img, contours, contourIdx,color,thickness, lineType = cv.LINE_8, hierarchy = cv.Mat(), maxLevel = INT_MAX, offset = cv.Point(0, 0)))
input的部分
1.img-BGR目標照片，要標註輪廓的照片
2.contours-我們偵測到的輪廓
3.contourIdx-你要畫的輪廓，如果你要畫全部的輪廓，就用-1
4.color-BGR，畫輪廓的顏色
5.lineType
6.offset-偏離程度

"""
