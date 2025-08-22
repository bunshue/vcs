"""
cv2.findContours  # 抓取顏色範圍的輪廓座標
cv2.drawContours  # 繪製輪廓

圖片邊緣檢測

圖片轉換成灰階Grayscale的部分，
利用Canny邊緣檢測使用多階段算法來檢測圖像中的各種邊緣。

OpenCV具有findContour()幫助從圖像中提取輪廓的功能。

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

輪廓近似方法 的選項 : 取值演算法(4)
cv2.CHAIN_APPROX_SIMPLE
cv2.CHAIN_APPROX_NONE
cv2.CHAIN_APPROX_TC89_L1
cv2.CHAIN_APPROX_TC89_KCOS

2.retrieval_mode-擷取模式

cv2.RETR_EXTERNAL-只擷取最外圍的輪廓
cv2.RETR_LIST-擷取大大小小所有輪廓，擷取結果沒有父子關係，大家都平等
cv2.RETR_CCOMP-會列出內、外兩層關係
cv2.RETR_TREE-會列出完整所有關係

3.approx_method-輪廓紀錄方式

cv2.CHAIN_APPROX_NONE-最精細紀錄模式
cv2.CHAIN_APPROX_SIMPLE-只記錄畫出輪廓的關鍵點

drawContours 將輪廓畫在src上，並複製到dst
drawContours 語法
畫上                   畫上  輪廓      第幾       顏色   線寬
dst = cv2.drawContours(src, contours, contourIdx, color, thickness, lineType = cv2.LINE_8, hierarchy = cv2.Mat(), maxLevel = INT_MAX, offset = cv2.Point(0, 0)))

畫上 : BGR目標照片，要標註輪廓的照片
輪廓 : 我們偵測到的輪廓
第幾 : 你要畫的輪廓，如果你要畫全部的輪廓，就用-1
offset : 偏離程度
"""

from opencv_common import *

filename_circle = "C:/_git/vcs/_4.python/opencv/data/_mask/mask1.png"

font = cv2.FONT_HERSHEY_SIMPLEX

# 擷取模式
RETRIEVAL_MODE = cv2.RETR_EXTERNAL
# cv2.RETR_EXTERNAL  -只擷取最外圍的輪廓
# cv2.RETR_LIST      -擷取大大小小所有輪廓，擷取結果沒有父子關係，大家都平等
# cv2.RETR_CCOMP     -會列出內、外兩層關係
# cv2.RETR_TREE      -會列出完整所有關係


# 輪廓紀錄方式
APPROX = cv2.CHAIN_APPROX_SIMPLE
# cv2.CHAIN_APPROX_NONE-最精細紀錄模式
# cv2.CHAIN_APPROX_SIMPLE-只記錄畫出輪廓的關鍵點


def get_image_contours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # 二值化處理影像
    thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
    ret, dst_binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)

    # 找出輪廓, 模式, 演算法
    contours, hierarchy = cv2.findContours(
        dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
    )
    get_contours_info(contours)
    return contours, hierarchy


def get_contours_info(contours):
    n = len(contours)  # 輪廓數量
    print("輪廓數量 :", n)
    # print("資料類型 :", type(contours))
    # print(contours)
    """
    # 看 contours 資料 ST
    for i in range(n):  # 輸出輪廓的屬性
        cnt = contours[i]  # 取得輪廓數據
        print("第", i, "個輪廓")
        print(f"輪廓點的數量 = {len(cnt)}")
        print(f"輪廓點的外形 = {cnt.shape}")
        print(f"資料格式 = {type(cnt)}")
        print(f"資料維度 = {cnt.ndim}")
        print(f"資料長度 = {len(cnt)}")
        for i in range(3):  # 列印 3 個座標點
            print(cnt[i])
    # 看 contours 資料 SP
    """


# 計算圓度
def circularity(cnt):
    perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長
    con_area = cv2.contourArea(cnt) + 1e-6  # 計算輪廓面積
    cc = perimeter * perimeter / (4 * np.pi * con_area)
    print("圓度 :", cc)
    return cc


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 簡易範本

image0 = cv2.imread(filename_star_white)  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)  # 要傳入彩圖

# image = dst, 會汙染
dst = cv2.drawContours(image, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 統一處理多圖，顯示在一起

filename1 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"
filename2 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape02.bmp"
filename3 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape03.png"
filename4 = "C:/_git/vcs/_4.python/opencv/data/_shape/shape04.png"
filename6 = "C:/_git/vcs/_4.python/opencv/data/_shape/star_blue.bmp"
filename7 = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.bmp"
# filename5 = "C:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename6 = "C:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
# filename7 = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
# filename8 = "C:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename8 = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"
filename3 = "C:/_git/vcs/_4.python/opencv/data/_Hough/shapes.jpg"


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
    image15 = cv2.drawContours(image11, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬
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
plt.title("找出輪廓"), plt.axis("off")
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

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
src = image0.copy()

contours, hierarchy = get_image_contours(src)

# 紅外框
dst = cv2.drawContours(src, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬
# 綠實心
dst = cv2.drawContours(src, contours, -1, GREEN, -1)  # 繪製輪廓/-1:全部/綠/-1:填滿

n = len(contours)  # 輪廓數量
print("每個輪廓分別處理:")
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    moment = cv2.moments(cnt)  # 影像矩
    # 計算輪廓面積1, 用輪廓矩
    # print("第", i, "個輪廓, 矩", moment)
    print("第", i, "個輪廓, 面積", moment["m00"])
    # 計算輪廓面積2, 用cv2.contourArea()
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("第", i, "個輪廓, 面積", con_area)
    perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長
    print("第", i, "個輪廓, 周長", perimeter)

    # 畫輪廓質心
    cx = int(moment["m10"] / moment["m00"])  # 質心 x 座標
    cy = int(moment["m01"] / moment["m00"])  # 質心 y 座標
    cv2.circle(dst, (cx, cy), 5, BLUE, -1)  # 畫實心圓, 畫質心
    print("第", i, "個輪廓, 質心座標 :", "(" + str(cx) + ", " + str(cy) + ")")
    x_st = cx - 70
    y_st = cy + 100
    cv2.putText(dst, str(i), (x_st, y_st), font, 1, YELLOW, 2)
    y_st += 50
    cv2.putText(
        dst, "(" + str(cx) + "," + str(cy) + ")", (x_st, y_st), font, 1, YELLOW, 2
    )
    y_st += 50
    cv2.putText(dst, "A:" + str(int(con_area)), (x_st, y_st), font, 1, YELLOW, 2)
    y_st += 50
    cv2.putText(dst, "L:" + str(int(perimeter)), (x_st, y_st), font, 1, YELLOW, 2)

plt.figure(figsize=(10, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"
filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

# shape05.png 500X500黑圖正中央有一個斜30度的400X100白色長方形
# 故質心在 (250, 250), 面積 400*100, 周長 2*(400+100)=1000
print("真實質心 : (250, 250)")
print("真實面積", 400 * 100)
print("真實周長", 2 * (400 + 100))

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

# 紅外框
image1 = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬
# 綠實心
image1 = cv2.drawContours(image1, contours, -1, GREEN, -1)  # 繪製輪廓/-1:全部/紅/-1:填滿

n = len(contours)  # 輪廓數量
print("每個輪廓分別處理:")
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    # 計算輪廓面積2, 用cv2.contourArea()
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("第", i, "個輪廓, 面積", con_area)
    perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長
    print("第", i, "個輪廓, 周長", perimeter)
    print("最小邊界矩形(包圍盒) 藍")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    dst = cv2.rectangle(image1, (x, y), (x + w, y + h), BLUE, 2)
    # 輪廓 => 最小外接矩形 => 畫上
    rect = cv2.minAreaRect(cnt)  # 最小外接矩形 (中心(x,y), (寬,高), 旋轉角度)
    box = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
    box = np.intp(box)  # 將頂點轉換為整數座標
    cv2.drawContours(image1, [box], 0, CYAN, 2)  # 繪製 最小外接矩形 輪廓
    print("最小外接圓 洋紅")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)
    dst = cv2.circle(image1, center, radius, MAGENTA, 2)  # 畫圓 外接圓
    dst = cv2.circle(image1, center, 25, RED, -1)  # 畫實心圓 圓心
    print("橢圓擬合, 旋轉邊界的內切圓 黃")
    ellipse = cv2.fitEllipse(cnt)  # 橢圓擬合, 旋轉邊界的內切圓
    cv2.ellipse(image1, ellipse, YELLOW, 2)
    print("直線擬合, 根據圖像中的點擬合出一條直線 紅")
    rows, cols = image1.shape[:2]
    print(rows, cols)
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)  # 直線擬合
    print(f"共線正規化向量 = {vx}, {vy}")
    print(f"直線經過的點   = {x}, {y}")
    print([vx, vy, x, y])
    lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
    print(lefty)
    righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
    print(righty)
    cv2.line(image1, (cols - 1, righty), (0, lefty), RED, 5)
    # cv2.line(src, (0, lefty), (cols - 1, righty), RED, 5)  # 左到右繪線

plt.figure(figsize=(8, 10))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")

print("------------------------------")  # 30個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒) 藍")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), BLUE, 2)

# 取得圓中心座標和圓半徑
print("最小外接圓")
(x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
center = (int(x), int(y))  # 圓心座標取整數
radius = int(radius)  # 圓半徑取整數
image1 = cv2.circle(image1, center, radius, MAGENTA, 2)  # 畫圓 外接圓
image1 = cv2.circle(image1, center, 25, RED, -1)  # 畫實心圓 圓心

left = tuple(cnt[cnt[:, :, 0].argmin()][0])  # 最左點
right = tuple(cnt[cnt[:, :, 0].argmax()][0])  # 最右點
top = tuple(cnt[cnt[:, :, 1].argmin()][0])  # 最上點
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])  # 最下點
print(f"紅 最左點 = {left}")
print(f"綠 最右點 = {right}")
print(f"藍 最上點 = {top}")
print(f"青 最下點 = {bottom}")
image1 = cv2.circle(image1, left, 25, RED, -1)  # 畫實心圓
image1 = cv2.circle(image1, right, 25, GREEN, -1)  # 畫實心圓
image1 = cv2.circle(image1, top, 25, BLUE, -1)  # 畫實心圓
image1 = cv2.circle(image1, bottom, 25, CYAN, -1)  # 畫實心圓

plt.subplot(223)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 三角形框選

image0 = cv2.imread(filename_star_white)  # 彩色讀取
src = image0.copy()

contours, hierarchy = get_image_contours(src)

cnt = contours[0]  # 取得輪廓數據

# 取得三角形面積與頂點座標
area, triangle = cv2.minEnclosingTriangle(cnt)

print(f"三角形面積   = {area}")
print(f"三角形頂點座標資料類型 = {type(triangle)}")
print(f"三角頂點座標 = \n{triangle}")
triangle = np.intp(triangle)  # 轉為整數
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), GREEN, 2)

plt.figure(figsize=(10, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("三角形框選")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.approxPolyDP() 輪廓近似 多邊形框選")
# 原先抓到的輪廓，是多點座標，使用輪廓近似，可以近似成多邊形

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 50, 150)
canny = cv2.dilate(canny, None, iterations=1)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
get_contours_info(contours)

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    print("處理前")
    print("輪廓邊點數量：{}".format(len(cnt)))
    # approxPolyDP 輪廓近似
    epsilon = 30  # 指定輪廓近似的精度
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print("處理後")
    print("輪廓邊點數量：{}".format(len(approx)))
    cv2.drawContours(image, [approx], -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

plt.figure(figsize=(10, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("輪廓近似")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.approxPolyDP() 輪廓近似 多邊形框選")
# 原先抓到的輪廓，是多點座標，使用輪廓近似，可以近似成多邊形

image0 = cv2.imread("data/findContours/multiple.jpg")  # 彩色讀取
src = image0.copy()
src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
src3 = src.copy()  # 複製src影像

contours, hierarchy = get_image_contours(src)

# 近似多邊形包圍

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據

    # approxPolyDP 輪廓近似
    epsilon = 3  # 指定輪廓近似的精度
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    dst1 = cv2.polylines(src1, [approx], True, GREEN, 2)  # dst1

    epsilon = 15  # 指定輪廓近似的精度
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # dst2

    epsilon = 30  # 指定輪廓近似的精度
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    dst3 = cv2.polylines(src3, [approx], True, GREEN, 2)  # dst3

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("多邊形框選 epsilon=3")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("多邊形框選 epsilon=15")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("多邊形框選 epsilon=30")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 近似多邊形包圍

image0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
image = image0.copy()
src1 = image.copy()  # 複製src影像
src2 = image.copy()  # 複製src影像
src3 = image.copy()  # 複製src影像

contours, hierarchy = get_image_contours(image)

cnt = contours[0]  # 取得輪廓數據

hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
dst1 = cv2.polylines(src1, [hull], True, GREEN, 2)  # 將凸包連線
isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
print(f"凸包是凸形       = {isConvex}")

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

# approxPolyDP 輪廓近似
epsilon = 10  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)
dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # 近似多邊形連線
isConvex = cv2.isContourConvex(approx)  # 凸檢測, 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

epsilon = 30  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)
dst3 = cv2.polylines(src3, [approx], True, GREEN, 2)  # 近似多邊形連線
isConvex = cv2.isContourConvex(approx)  # 凸檢測, 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("近似多邊形包圍 epsilon=10")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("近似多邊形包圍 epsilon=30")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 擬合一條線

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)

cnt = contours[0]  # 取得輪廓數據

rows, cols = image.shape[:2]  # 輪廓大小
vx, vy, x, y = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)  # 直線擬合
print(f"共線正規化向量 = {vx}, {vy}")
print(f"直線經過的點   = {x}, {y}")

lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
dst = cv2.line(image, (0, lefty), (cols - 1, righty), GREEN, 10)  # 左到右繪線

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擬合一條線")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape06.png"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
    dst = cv2.polylines(image, [hull], True, GREEN, 2)  # 將凸包連線
    # 計算輪廓面積
    convex_area = cv2.contourArea(hull)  # 計算輪廓面積  # 凸包面積
    print(f"凸包面積 = {convex_area}")


plt.figure(figsize=(8, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多邊形凹凸點計算

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

h, w, d = image.shape  # d為dimension, d = 3 全彩, d = 1 灰階
print(h, w, d)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 50, 150)
canny = cv2.dilate(canny, None, iterations=1)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
get_contours_info(contours)

cnt = contours[0]  # 取得輪廓數據

# approxPolyDP 輪廓近似
epsilon = 3  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)
image = cv2.polylines(image, [approx], True, RED, 5)

# 凸包 -> 凸包缺陷
hull = cv2.convexHull(cnt, returnPoints=False)  # 計算凸包
print("凸點數量：{}".format(len(hull)))

defects = cv2.convexityDefects(cnt, hull)  # 獲得凸包缺陷
print("凹點數量：{}".format(len(defects)))

"""
每一个Vec4i由四个整型数据构成，
这四个整型数据的名称分别为：start_index, end_index, farthest_pt_index, fixpt_depth
"""

# 構造凸缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    print("第", i, "個凹點索引 :", defects[i, 0])
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]  # 取得index
    start = tuple(cnt[s][0])  # 由index取得start_point座標
    end = tuple(cnt[e][0])  # 由index取得end_point座標
    far = tuple(cnt[f][0])  # 由index取得far_point座標
    dst = cv2.line(image, start, end, GREEN, 10)  # 凸包連線
    dst = cv2.circle(image, far, 10, BLUE, -1)  # 畫實心圓
    print("start :", start)
    print("end :", end)
    print("far :", far)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)

cnt = contours[0]  # 取得輪廓數據

hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
dst = cv2.polylines(image, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(image, pointa, 5, RED, -1)  # 畫實心圓  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(image, pointb, 5, RED, -1)  # 畫實心圓  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(image, pointc, 5, RED, -1)  # 畫實心圓  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("點在凸包外")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image0 = cv2.imread("data/findContours/heart1.jpg")  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)

cnt = contours[0]  # 取得輪廓數據

hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
dst = cv2.polylines(image, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(image, pointa, 5, RED, -1)  # 畫實心圓  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(image, pointb, 5, RED, -1)  # 畫實心圓  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(image, pointc, 5, RED, -1)  # 畫實心圓  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
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

image0 = cv2.imread(filename_star_white)  # 彩色讀取

image = image0.copy()

contours, hierarchy = get_image_contours(image)

dst = cv2.drawContours(image, contours, -1, RED, 10)

cnt = contours[0]  # 取得輪廓數據

# 計算輪廓面積
con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

print("最小邊界矩形(包圍盒) 黃")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print("輪廓面積 佔 最小邊界矩形的 :", extent)

dst = cv2.rectangle(image, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image0 = cv2.imread(filename_star_white)  # 彩色讀取
image = image0.copy()

contours, hierarchy = get_image_contours(image)

dst = cv2.drawContours(image, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

cnt = contours[0]  # 取得輪廓數據

# 計算輪廓面積
con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
(cx, cy) = (250, 250)
r = int(ed / 2)
dst = cv2.circle(image, (cx, cy), r, GREEN, 3)  # 畫圓

hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
dst = cv2.polylines(image, [hull], True, BLUE, 2)  # 將凸包連線

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")

show()

# 計算輪廓面積
convex_area = cv2.contourArea(hull)  # 計算輪廓面積  # 凸包面積
print("凸包面積 :", convex_area)

solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

image = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{image}")

nonzero_img = np.nonzero(image)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
image = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{image}")
nonzero_img = np.nonzero(image)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

image = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{image}")

loc_img = cv2.findNonZero(image)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 contours")

image0 = cv2.imread(filename_star_white)  # 彩色讀取
image1 = image0.copy()  # image1 拿來處理
image2 = image0.copy()  # image2 拿來畫圖上去

contours, hierarchy = get_image_contours(image1)
get_contours_info(contours)

# drawContours 將輪廓畫在image2上，並複製到dst
dst = cv2.drawContours(image2, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    print("最小外接圓")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)  # 圓半徑取整數
    cv2.circle(dst, center, radius, MAGENTA, 2)  # 畫圓  外接圓
    cv2.circle(dst, center, 25, RED, -1)  # 畫實心圓 圓心
    print("最小邊界矩形(包圍盒) 藍")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    cv2.rectangle(dst, (x, y), (w, h), BLUE, 3)
    print("最小外接的旋轉矩形")
    hull = cv2.convexHull(cnt)  # 獲得凸包頂點座標  # 計算凸包
    dst = cv2.polylines(dst, [hull], True, CYAN, 2)  # 將凸包連線
    print("凸點數量：{}".format(len(hull)))

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合")

image0 = cv2.imread(filename_star_white)  # 彩色讀取
image1 = image0.copy()  # image1 拿來處理
image2 = image0.copy()  # image2 拿來畫圖上去

image = cv2.GaussianBlur(image1, (3, 3), 0.5)  # 高斯平滑處理    #執行高斯模糊化
canny = cv2.Canny(image, 50, 200)

print("------------------------------")  # 30個

# 公版的 cv2.RETR_LIST 得到1個輪廓
contours, hierarchy = get_image_contours(image1)  # 不要用公版的 可以看到三段

n = len(contours)  # 輪廓數量
for i in range(n):  # 依次繪製輪廓
    dst1 = cv2.drawContours(image1, contours, i, colors[i], 5)  # 畫第i個輪廓

print("------------------------------")  # 30個

# 改用 cv2.RETR_EXTERNAL 得到3個輪廓 依序畫出
contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
get_contours_info(contours)

n = len(contours)  # 輪廓數量
for i in range(n):  # 依次繪製輪廓
    dst2 = cv2.drawContours(image2, contours, i, colors[i], 5)  # 畫第i個輪廓

print("------------------------------")  # 30個

plt.figure(figsize=(10, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("dst1")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("dst2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 findContours")

image0 = cv2.imread(filename_star_white, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
image = image0.copy()

# 第一步：閾值化，生成二值圖
# 圖像平滑
dst = cv2.GaussianBlur(image, (3, 3), 0.5)  # 執行高斯模糊化
# Otsu 閾值分割
OtsuThresh = 0
OtsuThresh, dst = cv2.threshold(dst, OtsuThresh, 255, cv2.THRESH_OTSU)
# --- 形態學開運算(消除細小白點)
# 創建結構元
s = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, s, iterations=2)

contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

get_contours_info(contours)

# 第三步：畫出找到的輪廓并用多邊形擬合輪廓

# 將輪廓畫在該黑板上
print(image.shape)

contoursImg = np.zeros(image.shape, np.uint8)
contoursImg = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    cv2.drawContours(contoursImg, contours, i, 255, 2)  # 繪製輪廓  # 畫第i個輪廓
    print("最小外接圓")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)  # 圓半徑取整數
    cv2.circle(image, center, radius, MAGENTA, 2)  # 畫圓  外接圓
    cv2.circle(image, center, 25, RED, -1)  # 畫實心圓 圓心
    # 多邊形逼近(注意與凸包區別)
    # approxPolyDP 輪廓近似
    approxCurve = cv2.approxPolyDP(cnt, 0.3, True)
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 形狀與結構分析
# 輪廓檢驗

coin_filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"

image0 = cv2.imread(coin_filename, cv2.IMREAD_COLOR)  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

blur = cv2.GaussianBlur(gray, (0, 0), 1.5, 1.5)  # 執行高斯模糊化
canny = cv2.Canny(blur.copy(), 60, 60)
canny_morphologyEx = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, np.ones((3, 3), "uint8"))

"""
輪廓近似方法 的選項 : 取值演算法(4)
cv2.CHAIN_APPROX_SIMPLE
cv2.CHAIN_APPROX_NONE
cv2.CHAIN_APPROX_TC89_L1
cv2.CHAIN_APPROX_TC89_KCOS
"""
for approx in ["NONE", "SIMPLE", "TC89_KCOS", "TC89_L1"]:
    cc = "CHAIN_APPROX_{}".format(approx)
    print(cc)
    approx_flag = getattr(cv2, "CHAIN_APPROX_{}".format(approx))
    print(approx_flag)
    contours, hierarchy = cv2.findContours(
        canny_morphologyEx.copy(), cv2.RETR_EXTERNAL, approx_flag
    )
    print(approx)
    cc = sum(contour.shape[0] for contour in contours)
    print(cc)
    print("{}: {}  ".format(approx, cc))
    print("------------------------------")  # 30個

# NONE: 3179   SIMPLE: 1579   TC89_KCOS: 849   TC89_L1: 802

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

# 顯示所有圓度在0.8到1.2之間的輪廓
contours = [contour for contour in contours if 0.8 < circularity(contour) < 1.2]

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

cv2.drawContours(image, contours, -1, RED, 3)  # 繪製輪廓/-1:全部/紅/線寬

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

filename_cs1 = "C:/_git/vcs/_4.python/opencv/data/cs1.bmp"

image0 = cv2.imread(filename_cs1)  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 100  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# 找出圖像中的輪廓
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找出最大的輪廓
filtered_contours = max(contours, key=cv2.contourArea)  # 取出最大面積

# 輪廓 => 最小外接矩形 => 畫上
rect = cv2.minAreaRect(filtered_contours)  # 最小外接矩形 (中心(x,y), (寬,高), 旋轉角度)
box = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
box = np.intp(box)  # 將頂點轉換為整數座標
cv2.drawContours(image, [box], 0, RED, 10)  # 繪製 最小外接矩形 輪廓

# 取得旋轉矩形的中心點和旋轉角度
(cx, cy), (w, h), angle = rect

center_text = f"Center: ({int(cx)}, {int(cy)})"  # 中心點
angle_text = f"Angle: {int(angle)} degrees"  # 旋轉角度
print(center_text)
print(angle_text)

cv2.circle(image, (int(cx), int(cy)), 10, BLUE, -1)  # 畫實心圓 中心點

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
        points = np.intp(points)  # 將頂點轉換為整數座標
        cv2.drawContours(image, [points], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬


# boxPoints返回四個點順序：右下→左下→左上→右上

image0 = cv2.imread("data/cc.bmp")  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 輪廓 => 最小外接矩形 => 畫上
cnt = contours[0]  # 取得輪廓數據
rect = cv2.minAreaRect(cnt)  # 得到最小外接矩形的(中心(x,y), (寬,高), 旋轉角度)
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
    cv2.circle(image, (int(point[0]), int(point[1])), 10, 255, 5)  # 畫圓

draw_boxpoints(points)  # 畫出四個頂點連線

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

image0 = cv2.imread("data/cc.bmp")  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 輪廓 => 最小外接矩形 => 畫上
cnt = contours[0]  # 取得輪廓數據
rect = cv2.minAreaRect(cnt)  # 得到最小外接矩形的(中心(x,y), (寬,高), 旋轉角度)
print("返回值rect:\n", rect)

points = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
print("\n轉換后的points：\n", points)

draw_boxpoints(points)  # 畫出四個頂點連線

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

W, H = 400, 400

# 根據四個頂點在黑色畫板上畫出該矩形
image = np.zeros((H, W, 3), np.uint8)
image = np.ones((H, W, 3), dtype=np.uint8) * 127  # 新建一個灰圖

cx, cy = 200, 200
w, h = W // 2, H // 4

rotating_angle = 0  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

rotating_angle = 20  # 順時針   # 旋轉矩形
points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
draw_boxpoints(points)  # 畫出四個頂點連線

plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 輸出邊緣和結構信息

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

o = cv2.drawContours(image, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

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

contoursImg = []

n = len(contours)  # 輪廓數量
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    temp = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, RED, 10
    )  # 繪製輪廓/一個/紅/線寬
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
mask = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖

mask = cv2.drawContours(mask, contours, -1, WHITE, -1)  # 繪製輪廓/-1:全部/白/-1:填滿

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

contoursImg = []

n = len(contours)  # 輪廓數量
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    temp = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, 255, 3
    )  # 繪製輪廓/一個/??/線寬
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

# 計算輪廓面積
print("各個輪廓的矩(moments)和面積:")
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    moment = cv2.moments(cnt)  # 影像矩
    # print("第", i, "個輪廓, 矩", moment)
    print("第", i, "個輪廓, 面積", moment["m00"])

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

contoursImg = []

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("第", i, "個輪廓, 面積", con_area)
    temp = np.zeros(image.shape, np.uint8)
    temp = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, WHITE, 3
    )  # 繪製輪廓/一個/白/線寬
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

contoursImg = []

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    temp = np.zeros(image.shape, np.uint8)
    temp = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, WHITE, 3
    )  # 繪製輪廓/一個/白/線寬
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("第", i, "個輪廓, 面積", con_area)
    if con_area > 15000:
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

image = cv2.imread("data/cc.bmp")  # 彩色讀取

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒)")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒)")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)

brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv2.drawContours(image, [brcnt], -1, RED, 2)  # 繪製輪廓/-1:全部/紅/線寬

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒) 紅")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
cv2.rectangle(image, (x, y), (x + w, y + h), RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據

print("最小外接圓")
(x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
center = (int(x), int(y))  # 圓心座標取整數
radius = int(radius)  # 圓半徑取整數
cv2.circle(image, center, radius, MAGENTA, 2)  # 畫圓  外接圓
cv2.circle(image, center, 25, RED, -1)  # 畫實心圓 圓心

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("圓圈圈出來")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據
ellipse = cv2.fitEllipse(cnt)  # 橢圓擬合, 旋轉邊界的內切圓
print("ellipse=", ellipse)
cv2.ellipse(image, ellipse, GREEN, 3)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("橢圓形圈出來")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# some NG
image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  # 取得輪廓數據
area, trgl = cv2.minEnclosingTriangle(cnt)
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

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.1 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

adp = cv2.drawContours(adp, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

plt.subplot(232)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.1")

# ----------------epsilon=0.09*周長-------------------------------
adp = image.copy()

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.09 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

adp = cv2.drawContours(adp, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

plt.subplot(233)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.09")

# ----------------epsilon=0.055*周長-------------------------------
adp = image.copy()

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.055 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

adp = cv2.drawContours(adp, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

plt.subplot(234)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.055")

# ----------------epsilon=0.05*周長-------------------------------
adp = image.copy()

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.05 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

adp = cv2.drawContours(adp, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

plt.subplot(235)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.05")

# ----------------epsilon=0.02*周長-------------------------------
adp = image.copy()

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.02 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

adp = cv2.drawContours(adp, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

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

cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 返回坐標值  # 計算凸包
print("returnPoints為默認值True時返回值hull的值：\n", hull)

cnt = contours[0]  # 取得輪廓數據
hull2 = cv2.convexHull(cnt, returnPoints=False)  # 返回索引值  # 計算凸包
print("returnPoints為False時返回值hull的值：\n", hull2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# --------------提取輪廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------尋找凸包，得到凸包的角點------------------
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包
# --------------繪製凸包------------------
cv2.polylines(o, [hull], True, GREEN, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("顯示凸包")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

# ----------------構造輪廓--------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# ----------------凸包--------------------------
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt, returnPoints=False)  # 計算凸包
defects = cv2.convexityDefects(cnt, hull)  # 獲得凸包缺陷
print("defects=\n", defects)

# 構造凸缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    print("第", i, "個凹點索引 :", defects[i, 0])
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]  # 取得index
    start = tuple(cnt[s][0])  # 由index取得start_point座標
    end = tuple(cnt[e][0])  # 由index取得end_point座標
    far = tuple(cnt[f][0])  # 由index取得far_point座標
    dst = cv2.line(image, start, end, GREEN, 10)  # 凸包連線
    dst = cv2.circle(image, far, 10, BLUE, -1)  # 畫實心圓
    print("start :", start)
    print("end :", end)
    print("far :", far)

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

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
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包
cv2.polylines(image1, [hull], True, GREEN, 2)

# 凸檢測, 是否凸形
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：", cv2.isContourConvex(hull))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("result1")

# ------------逼近多邊形--------------------
image2 = o.copy()

cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似
epsilon = 0.01 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

image2 = cv2.drawContours(image2, [approx], 0, RED, 10)  # 繪製輪廓/一個/紅/線寬

# 凸檢測, 是否凸形
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：", cv2.isContourConvex(approx))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("result2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs1.bmp")  # 彩色讀取

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)

# ----------------內部點A的距離-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)

# ----------------外部點B的距離-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)
# ------------正好處于邊緣上的點C的距離-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的

plt.figure(figsize=(10, 8))
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
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)

# ----------------內部點A與多邊形的關系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), False)
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)

# ----------------外部點B與多邊形的關系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)

# ----------------邊緣線上點C與多邊形的關系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112), False)
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的

plt.figure(figsize=(10, 8))
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

# 構造距離提取算子
sd = cv2.createShapeContextDistanceExtractor()

# 計算距離
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

# 構造距離提取算子
hd = cv2.createHausdorffDistanceExtractor()

# 計算距離
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

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒) 白")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
cv2.rectangle(o, (x, y), (x + w, y + h), WHITE, 3)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒) 藍")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)

cv2.drawContours(o, cnt, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬
cv2.rectangle(o, (x, y), (x + w, y + h), BLUE, 3)

rectArea = w * h

cnt = contours[0]  # 取得輪廓數據
con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

extend = float(con_area) / rectArea
print(extend)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  # 取得輪廓數據
cv2.drawContours(o, cnt, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

cnt = contours[0]  # 取得輪廓數據
con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包

hull_area = cv2.contourArea(hull)  # 計算輪廓面積
print("輪廓面積 :", hull_area)

cv2.polylines(o, [hull], True, GREEN, 2)
solidity = float(con_area) / hull_area
print(solidity)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據
cv2.drawContours(o, cnt, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

cnt = contours[0]  # 取得輪廓數據
con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

equiDiameter = np.sqrt(4 * con_area / np.pi)
print(equiDiameter)
cv2.circle(o, (100, 100), int(equiDiameter / 2), RED, 3)  # 畫圓  # 展示等直徑大小的圓

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

cnt = contours[0]  # 取得輪廓數據
ellipse = cv2.fitEllipse(cnt)  # 橢圓擬合, 旋轉邊界的內切圓
retval = cv2.fitEllipse(cnt)
print("單個返回值形式：")
print("retval=\n", retval)
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
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

o = cv2.imread("data/cc.bmp")  # 彩色讀取

# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  # 取得輪廓數據

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
mask1 = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖
cv2.drawContours(mask1, [cnt], 0, 255, 2)  # 繪製輪廓/一個/??/線寬
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
mask2 = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖
cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製輪廓/一個/??/-1:填滿
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
loc = cv2.findNonZero(a)  # 獲得非0元素座標

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
cnt = contours[0]  # 取得輪廓數據

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
mask1 = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(mask1, [cnt], 0, 255, 2)  # 繪製輪廓/一個/??/線寬
pixelpoints1 = cv2.findNonZero(mask1)  # 獲得非0元素座標
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
mask2 = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製輪廓/一個/??/-1:填滿
pixelpoints2 = cv2.findNonZero(mask2)  # 獲得非0元素座標
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
mask = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

mask = cv2.drawContours(mask, [cnt], -1, 255, -1)  # 繪製輪廓/-1:全部/??/-1:填滿
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray, mask=mask)
print("minVal=", minVal)
print("maxVal=", maxVal)
print("minLoc=", minLoc)
print("maxLoc=", maxLoc)

# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
masko = np.ones(o.shape, dtype=np.uint8) * 127  # 新建一個灰圖

masko = cv2.drawContours(masko, [cnt], -1, WHITE, -1)  # 繪製輪廓/-1:全部/白/-1:填滿
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
mask = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(mask, [cnt], 0, WHITE, -1)  # 繪製輪廓/一個/白/-1:填滿
meanVal = cv2.mean(o, mask=mask)  # mask是區域，所以必須是單通道的
print("meanVal=\n", meanVal)

# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
masko = np.ones(o.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(masko, [cnt], -1, WHITE, -1)  # 繪製輪廓/-1:全部/白/-1:填滿
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
mask = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cnt = contours[0]  # 取得輪廓數據
cv2.drawContours(mask, [cnt], 0, 255, -1)  # 繪製輪廓/一個/??/-1:填滿

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

contours, hierarchy = cv2.findContours(image13, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 開始畫contours
with_contours = cv2.drawContours(image10, contours, -1, RED, -1)  # 繪製輪廓/-1:全部/紅/-1:填滿

cv2.imshow("contours", with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 標示矩形邊框
for cnt in contours:
    # print("最小邊界矩形(包圍盒) 綠")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    image = cv2.rectangle(image10, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("contours", image10)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 根據面積，挑出籃網的部分
required_contour = max(contours, key=cv2.contourArea)  # 取出最大面積
print("最小邊界矩形(包圍盒) 藍")
x, y, w, h = cv2.boundingRect(required_contour)  # 邊界矩形(包圍盒)
image14 = cv2.rectangle(image11, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("largest contour", image14)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.boundingRect# 邊界矩形(包圍盒)
矩形邊框(Bounding Rectangle)是說，用一個最小的矩形，把找到的形狀包起來。
cv2.boundingRect(image)
img是一個二值圖，也就是它的參數；
返回四個值，分別是x，y，w，h( x，y是矩型左上點的坐標，w，h是矩型的寬和高)

cv2.contourArea 計算輪廓面積
cv2.contourArea(contour， oriented=True)
contour：表示某輸入單個輪廓，為array
oriented：表示某個方向上輪廓的面積值，這裡指順時針或者逆時針。
若為True，該函數返回一個帶符號的面積值，正負值取決於輪廓的方向(順時針還是逆時針)，
若為False，表示以絕對值返回

cv2.arcLength 計算輪廓周長
cv2.arcLength(contour， closed=True)
contour：表示某輸入單個輪廓，為array
closed：用於指示曲線是否封閉

cv2.approxPolyDP()函數是輪廓近似函數，是opencv中對指定的點集進行多邊形逼近的函數，其逼近的精度可通過參數設置
cv2.approxPolyDP(curve, epsilon, closed, approxCurve=None)
curve：表示輸入的點集
epsilon：指定的精度，也即原始曲線與近似曲線之間的最大距離，不過這個值我們一般按照周長的大小進行比較
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
# 改 contours
contours_list, hierarchy = cv2.findContours(
    image13, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
for cnt in contours_list:
    # print("最小邊界矩形(包圍盒) 紅")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    cv2.rectangle(image10, (x, y), (x + w, y + h), (0, 0, 255), 2)

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
print("最小邊界矩形(包圍盒)")
x, y, w, h = cv2.boundingRect(required_cnt)  # 邊界矩形(包圍盒)

filename = "data/phrase_handwritten.jpg"
imagecopy = cv2.imread(filename)  # 彩色讀取
cv2.rectangle(imagecopy, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Detected B", imagecopy)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 篩選出大于特定大小的輪廓

image = cv2.imread("data/contours0.bmp")  # 彩色讀取

cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------獲取輪廓--------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------計算各個輪廓的長度和、平均長度--------------------
n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

cntLen = []  # 存儲各個輪廓的長度
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print("第" + str(i) + "個輪廓的長度:%d" % cntLen[i])
cntLenSum = np.sum(cntLen)  # 各個輪廓長度和
cntLenAvr = cntLenSum / n  # 各個輪廓長度平均值
print("各個輪廓的總長度為：%d" % cntLenSum)
print("各個輪廓的平均長度為：%d" % cntLenAvr)

# --------------顯示超過平均值的輪廓--------------------
contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        print(i)
        cv2.imshow("contours[" + str(i) + "]", contoursImg[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立 500 X 500 之白圖
width, height = 305, 400  # 影像寬, 影像高
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# img = cv2.imread(filename1)  # 彩色讀取

N = 10
pts = np.random.randint(50, 300, size=[N, 2])
pts = np.intp(pts)

# minAreaRect 生成最小外接矩形
rect = cv2.minAreaRect(pts)  # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
print(rect)

# 取得旋轉矩形的中心點和旋轉角度
(center_x, center_y), (w, h), angle = rect

box = cv2.boxPoints(rect)  # 获取最小外接矩形的4个顶点坐标
# print(box)

# box = round(box)
box = np.round(box)
# print(box)
# print(type(box))
box = np.intp(box)

for p in pts:
    cv2.circle(img, (p[0], p[1]), 7, BLUE, -1)  # 畫圓


# 画出来
cv2.drawContours(img, [box], 0, RED, 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def drawAxis(img, p_, q_, colour, scale):
    p = list(p_)
    q = list(q_)
    ## [visualization1]
    angle = math.atan2(p[1] - q[1], p[0] - q[0])  # angle in radians
    hypotenuse = math.sqrt(
        (p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0])
    )

    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * math.cos(angle)
    q[1] = p[1] - scale * hypotenuse * math.sin(angle)
    cv2.line(
        img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA
    )

    # create the arrow hooks
    p[0] = q[0] + 9 * math.cos(angle + math.pi / 4)
    p[1] = q[1] + 9 * math.sin(angle + math.pi / 4)
    cv2.line(
        img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA
    )

    p[0] = q[0] + 9 * math.cos(angle - math.pi / 4)
    p[1] = q[1] + 9 * math.sin(angle - math.pi / 4)
    cv2.line(
        img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA
    )
    ## [visualization1]


def getOrientation(pts, img):
    ## [pca]
    # Construct a buffer used by the pca analysis
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
        data_pts[i, 0] = pts[i, 0, 0]
        data_pts[i, 1] = pts[i, 0, 1]

    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv2.PCACompute2(data_pts, mean)

    # Store the center of the object
    cntr = (int(mean[0, 0]), int(mean[0, 1]))
    ## [pca]

    ## [visualization]
    # Draw the principal components
    cv2.circle(img, cntr, 3, MAGENTA, 2)
    p1 = (
        cntr[0] + 0.02 * eigenvectors[0, 0] * eigenvalues[0, 0],
        cntr[1] + 0.02 * eigenvectors[0, 1] * eigenvalues[0, 0],
    )
    p2 = (
        cntr[0] - 0.02 * eigenvectors[1, 0] * eigenvalues[1, 0],
        cntr[1] - 0.02 * eigenvectors[1, 1] * eigenvalues[1, 0],
    )
    drawAxis(img, cntr, p1, GREEN, 1)
    drawAxis(img, cntr, p2, CYAN, 5)

    angle = math.atan2(eigenvectors[0, 1], eigenvectors[0, 0])  # orientation in radians
    ## [visualization]

    return angle


filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image = cv2.imread(filename)  # 彩色讀取

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 二值化處理影像
thresh = 50  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
_, dst_binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Find all the contours in the thresholded image
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print("輪廓數量 :", len(contours))

n = len(contours)  # 輪廓數量
for i in range(n):  # 繪製中心點迴圈
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    # 畫輪廓
    cv2.drawContours(image, contours, i, RED, 5)
    # 畫方向
    getOrientation(cnt, image)

cv2.imshow("output", image)
cv2.waitKey()
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
圖片預處理 1.邊緣檢測 2.閾值處理 生成一張二值圖(閾值分割的二值化)

# 圖片先處理方法一 灰階 模糊 Canny
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray = cv2.GaussianBlur(gray, (13, 13), 0)  # 執行高斯模糊化
canny = cv2.Canny(gray, 50, 150)

# 圖片先處理方法二 灰階 二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)

# 找出輪廓, 模式, 演算法 固定

# 找出輪廓, 模式, 演算法
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

# 找出輪廓, 模式, 演算法
contours, hierarchy = cv2.findContours(
    canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# 畫輪廓方法

# 一起畫
# index = -1 # 指名要繪製的輪廓, -1代表全部
# image2 = cv2.drawContours(image2, contours, index, RED, 10)  # image2為三通道才能顯示輪廓, 用紅框標示出來

# 分開畫
n = len(contours)  # 輪廓數量
for index in range(n):
    image2 = cv2.drawContours(
        image2, contours, index, color[index % 9], 10
    )  # 繪製輪廓  # image2為三通道才能顯示輪廓
"""

# 似無用
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")


filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape01.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
image = image0.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
get_contours_info(contours)

cv2.drawContours(image, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/紅/線寬

plt.figure(figsize=(10, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(canny, cv2.COLOR_BGR2RGB))
plt.title("Canny")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓aaaa")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

contours, hierarchy = cv2.findContours(
    dst_binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1
)

cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, BLUE, 2)  # 藍色字體
cv2.putText(image, text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, BLUE, 2)  # 藍色字體

"""
lineType = cv2.LINE_AA
lineType：绘制线段的线性，默认为 LINE_8
cv2.FILLED：内部填充（实心图形）
cv2.LINE_4：4 邻接线型
cv2.LINE_8：8 邻接线型
cv2.LINE_AA：抗锯齿线型，图像更平滑
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在src_gray影像的mask遮罩區域計算均值

channels = cv2.mean(gray, mask=mask)  # 計算遮罩的均值
print("計算遮罩的均值 :", channels)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在src_gray影像的mask遮罩區域找尋最大像素與最小像素值
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray, mask=mask)
print(f"最小像素值 = {minVal}")
print(f"最小像素值座標 = {minLoc}")
print(f"最大像素值 = {maxVal}")
print(f"最大像素值座標 = {maxLoc}")
cv2.circle(image, minLoc, 20, GREEN, 3)  # 畫圓  # 最小像素值用綠色圓
cv2.circle(image, maxLoc, 20, RED, 3)  # 畫圓  # 最大像素值用紅色圓

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------")  # 30個


dst = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖

# 依次繪製輪廓
n = len(contours)  # 輪廓數量
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(image.shape, np.uint8)  # 建立輪廓影像
    img = np.ones(image.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    dst = cv2.drawContours(dst, contours, i, colors[i], 5)  # 畫第i個輪廓


# 輪廓 => 最小外接矩形 => 畫上
cnt = contours[0]  # 取得輪廓數據
rect = cv2.minAreaRect(cnt)  # 最小外接矩形 (中心(x,y), (寬,高), 旋轉角度)
box = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
box = np.intp(box)  # 將頂點轉換為整數座標
dst = cv2.drawContours(image, [box], 0, GREEN, 10)  # 繪製 最小外接矩形 輪廓


# 最優擬合橢圓框選

cnt = contours[0]  # 取得輪廓數據
# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(cnt)  # 取得最優擬合橢圓數據  # 橢圓擬合, 旋轉邊界的內切圓
print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(image, ellipse, GREEN, 2)  # 繪橢圓


ddddddddddddd


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
