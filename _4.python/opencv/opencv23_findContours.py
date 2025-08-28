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
    # print("圓度 :", cc)
    return cc


def cv2_Chinese_Text(image, text, left, top, textColor, fontSize):
    # 建立中文字輸出
    # 影像轉成 PIL影像格式
    if isinstance(image, np.ndarray):
        # image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)  # 建立PIL繪圖物件
    fontText = ImageFont.truetype(  # 建立字型 - 新細明體
        "C:\Windows\Fonts\mingliu.ttc", fontSize, encoding="utf-8"  # 新細明體  # 字型大小
    )  # 編碼方式
    draw.text((left, top), text, textColor, font=fontText)  # 繪製中文字
    # 將PIL影像格式轉成OpenCV影像格式
    # return cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    return np.asarray(image)


def draw_grid(image):
    W, H = image.shape[1], image.shape[0]
    nx = W // 100
    ny = H // 100
    for i in range(nx):
        cv2.line(dst, (i * 100, 0), (i * 100, H), RED, 2)  # 垂直線
    for i in range(ny):
        cv2.line(dst, (0, i * 100), (W, i * 100), RED, 2)  # 水平線


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 簡易範本

image0 = cv2.imread(filename_star_white)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)  # 要傳入彩圖

# image1 = dst, 會汙染
dst = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬

plt.figure(figsize=(8, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
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

filename1 = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
filename2 = "D:/_git/vcs/_4.python/opencv/data/_shape/shape02.bmp"
filename3 = "D:/_git/vcs/_4.python/opencv/data/_shape/shape03.png"
filename4 = "D:/_git/vcs/_4.python/opencv/data/_shape/shape04.png"
filename6 = "D:/_git/vcs/_4.python/opencv/data/_shape/star_blue.bmp"
filename7 = "D:/_git/vcs/_4.python/opencv/data/_shape/star_silver.bmp"
# filename5 = "D:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename6 = "D:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
# filename7 = "D:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
# filename8 = "D:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename8 = "D:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"
filename3 = "D:/_git/vcs/_4.python/opencv/data/_Hough/shapes.jpg"


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
    image15 = cv2.drawContours(image11, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01b.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

# 紅外框
image1 = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
# 綠實心
image1 = cv2.drawContours(image1, contours, -1, GREEN, -1)  # 繪製輪廓/-1:全部/綠/-1:填滿

n = len(contours)  # 輪廓數量
print("每個輪廓分別處理:")
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    image1 = cv2.drawContours(image1, contours, i, RED, 3)  # 繪製輪廓/一個/色/線寬
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
    cv2.circle(image1, (cx, cy), 5, BLUE, -1)  # 畫實心圓, 畫質心
    print("第", i, "個輪廓, 質心座標 :", "(" + str(cx) + ", " + str(cy) + ")")
    x_st = cx - 70
    y_st = cy + 100
    cv2.putText(image1, str(i), (x_st, y_st), font, 1, YELLOW, 2)
    y_st += 50
    text = "(" + str(cx) + "," + str(cy) + ")"
    cv2.putText(image1, text, (x_st, y_st), font, 1, YELLOW, 2)
    y_st += 50
    text="A:" + str(int(con_area))
    cv2.putText(image1, text, (x_st, y_st), font, 1, YELLOW, 2)
    y_st += 50
    text="L:" + str(int(perimeter))
    cv2.putText(image1, text, (x_st, y_st), font, 1, YELLOW, 2)

for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    # 計算輪廓面積
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("輪廓面積 :", con_area)
    print("最小邊界矩形(包圍盒) 黃")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    square_area = w * h  # 計算矩形面積
    extent = con_area / square_area  # 計算Extent
    print("真實占比 輪廓面積 佔 最小邊界矩形的 :", extent)
    image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), YELLOW, 2)


for i in range(10):
    cv2.line(image1, (i * 100, 0), (i * 100, 200), GRAY, 2)  # 垂直線

for i in range(3):
    cv2.line(image1, (0, i * 100), (900, i * 100), GRAY, 2)  # 水平線


x_st, y_st = 10, 160
image1 = cv2_Chinese_Text(image1, "序號", x_st, y_st, YELLOW, 40)
y_st += 50
image1 = cv2_Chinese_Text(image1, "中心", x_st, y_st, YELLOW, 40)
y_st += 50
image1 = cv2_Chinese_Text(image1, "面積", x_st, y_st, YELLOW, 40)
y_st += 50
image1 = cv2_Chinese_Text(image1, "周長", x_st, y_st, YELLOW, 40)


plt.figure(figsize=(10, 8))
plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

image1 = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    # 計算輪廓面積
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("輪廓面積 :", con_area)
    ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
    print("等效面積 :", ed)
    (cx, cy) = (250, 250)  # 改成隨contour畫圓
    r = int(ed / 2)
    image1 = cv2.circle(image1, (cx, cy), r, GREEN, 3)  # 畫圓
    hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
    isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
    print(f"凸包是凸形       = {isConvex}")
    image1 = cv2.polylines(image1, [hull], True, BLUE, 2)  # 將凸包連線# 近似多邊形連線
    # 計算輪廓面積
    convex_area = cv2.contourArea(hull)  # 計算輪廓面積  # 凸包面積
    print("凸包面積 :", convex_area)
    extent = con_area / convex_area  # 計算Extent
    print("真實占比 輪廓面積 佔 凸包的 :", extent)


plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測")

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)
get_contours_info(contours)

image1 = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    print("最小外接圓")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)  # 圓半徑取整數
    cv2.circle(image1, center, radius, MAGENTA, 2)  # 畫圓  外接圓
    cv2.circle(image1, center, 10, RED, -1)  # 畫實心圓 圓心
    print("最小邊界矩形(包圍盒) 藍")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    cv2.rectangle(image1, (x, y), (x + w, y + h), BLUE, 3)
    print("最小外接的旋轉矩形")
    hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
    isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
    print(f"凸包是凸形       = {isConvex}")
    image1 = cv2.polylines(image1, [hull], True, CYAN, 2)  # 將凸包連線# 近似多邊形連線
    print("凸點數量：{}".format(len(hull)))

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("幾何形狀的檢測")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 findContours")

# image0 = cv2.imread(filename_star_white, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)
get_contours_info(contours)

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    cv2.drawContours(image1, contours, i, 255, 2)  # 繪製輪廓  # 畫第i個輪廓
    print("最小外接圓")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)  # 圓半徑取整數
    cv2.circle(image1, center, radius, MAGENTA, 2)  # 畫圓  外接圓
    cv2.circle(image1, center, 10, RED, -1)  # 畫實心圓 圓心
    # 多邊形逼近(注意與凸包區別)
    # approxPolyDP 輪廓近似
    approxCurve = cv2.approxPolyDP(cnt, 0.3, True)
    # 多邊形頂點個數
    k = approxCurve.shape[0]
    # 頂點連接，繪制多邊形
    for i in range(k - 1):
        cv2.line(
            image1,
            (approxCurve[i, 0, 0], approxCurve[i, 0, 1]),
            (approxCurve[i + 1, 0, 0], approxCurve[i + 1, 0, 1]),
            0,
            5,
        )
    # 首尾相接
    cv2.line(
        image1,
        (approxCurve[k - 1, 0, 0], approxCurve[k - 1, 0, 1]),
        (approxCurve[0, 0, 0], approxCurve[0, 0, 1]),
        0,
        5,
    )

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("顯示擬合的多邊形")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 三角形框選

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    # 取得三角形面積與頂點座標
    area, triangle = cv2.minEnclosingTriangle(cnt)
    print(f"三角形面積   = {area}")
    print(f"三角形頂點座標資料類型 = {type(triangle)}")
    print(f"三角頂點座標 = \n{triangle}")
    triangle = np.intp(triangle)  # 轉為整數
    dst = cv2.line(image1, tuple(triangle[0][0]), tuple(triangle[1][0]), GREEN, 2)
    dst = cv2.line(image1, tuple(triangle[1][0]), tuple(triangle[2][0]), GREEN, 2)
    dst = cv2.line(image1, tuple(triangle[0][0]), tuple(triangle[2][0]), GREEN, 2)

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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()
image2 = image0.copy()
image3 = image0.copy()

contours, hierarchy = get_image_contours(image0)

# approxPolyDP 輪廓近似, epsilon=3/15/30, 做 近似多邊形包圍

n = len(contours)  # 輪廓數量
epsilon = 3  # 指定輪廓近似的精度
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    # print("處理前, 輪廓邊點數量：{}".format(len(cnt)))
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # print("處理後, 輪廓邊點數量：{}".format(len(approx)))
    image1 = cv2.drawContours(image1, [approx], -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
    image1 = cv2.polylines(image1, [approx], True, GREEN, 2)  # 近似多邊形連線

epsilon = 15  # 指定輪廓近似的精度
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    # print("處理前, 輪廓邊點數量：{}".format(len(cnt)))
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # print("處理後, 輪廓邊點數量：{}".format(len(approx)))
    image2 = cv2.drawContours(image2, [approx], -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
    image2 = cv2.polylines(image2, [approx], True, GREEN, 2)  # 近似多邊形連線

epsilon = 30  # 指定輪廓近似的精度
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    # print("處理前, 輪廓邊點數量：{}".format(len(cnt)))
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # print("處理後, 輪廓邊點數量：{}".format(len(approx)))
    image3 = cv2.drawContours(image3, [approx], -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
    image3 = cv2.polylines(image3, [approx], True, GREEN, 2)  # 近似多邊形連線


plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("輪廓近似 epsilon=3")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("輪廓近似 epsilon=15")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("輪廓近似 epsilon=30")
plt.axis("off")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 近似多邊形包圍

filename = "data/findContours/heart1.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()
image2 = image0.copy()
image3 = image0.copy()

contours, hierarchy = get_image_contours(image0)

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
    image1 = cv2.polylines(image1, [hull], True, GREEN, 2)  # 將凸包連線# 近似多邊形連線
    isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
    print(f"凸包是凸形       = {isConvex}")

# approxPolyDP 輪廓近似, epsilon=10/30, 做 近似多邊形包圍

epsilon = 10  # 指定輪廓近似的精度
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    image2 = cv2.polylines(image2, [approx], True, GREEN, 2)  # 近似多邊形連線
    isConvex = cv2.isContourConvex(approx)  # 凸檢測, 是否凸形
    print(f"近似多邊形是凸形 = {isConvex}")

epsilon = 30  # 指定輪廓近似的精度
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    image3 = cv2.polylines(image3, [approx], True, GREEN, 2)  # 近似多邊形連線
    isConvex = cv2.isContourConvex(approx)  # 凸檢測, 是否凸形
    print(f"近似多邊形是凸形 = {isConvex}")

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("凸包")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("近似多邊形包圍 epsilon=10")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("近似多邊形包圍 epsilon=30")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

n = len(contours)  # 輪廓數量
for i in range(n):
    cnt = contours[i]  # 取得輪廓數據
    dst = cv2.drawContours(image1, cnt, -1, RED, 5)
    hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
    dst = cv2.polylines(image1, [hull], True, GREEN, 2)  # 將凸包連線# 近似多邊形連線
    isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
    print(f"凸包是凸形       = {isConvex}")
    # 計算輪廓面積(凸包)
    convex_area = cv2.contourArea(hull)  # 計算輪廓面積(凸包)
    print(f"凸包面積 = {convex_area}")
    # 計算輪廓面積
    con_area = cv2.contourArea(cnt)  # 計算輪廓面積
    print("輪廓面積 :", con_area)
    extent = con_area / convex_area  # 計算Extent
    print("真實占比 輪廓面積 佔 凸包的 :", extent)


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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()  # 畫凸點
image2 = image0.copy()  # 畫凹點

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 50, 150)
canny = cv2.dilate(canny, None, iterations=1)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
get_contours_info(contours)

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據

    # approxPolyDP 輪廓近似, epsilon=3
    epsilon = 3  # 指定輪廓近似的精度
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    dst1 = cv2.polylines(image1, [approx], True, RED, 3)  # 近似多邊形連線
    dst2 = cv2.polylines(image2, [approx], True, RED, 3)  # 近似多邊形連線

    # 凸包
    hull = cv2.convexHull(cnt, returnPoints=False)  # 計算凸包, 返回凸包頂點索引值
    print("凸點數量 :", len(hull))
    n = hull.shape[0]  # 凸點數量
    print("凸點數量 :", n)
    for i in range(n):
        print("第", i, "個凸點索引 :", hull[i, 0], ", 座標 :", cnt[hull[i, 0]])
        dst1 = cv2.circle(dst1, cnt[hull[i, 0]][0], 10, BLUE, -1)  # 畫實心圓

    # 凸包缺陷, 凹點
    defects = cv2.convexityDefects(cnt, hull)  # 獲得凸包缺陷
    print("凹點數量 :", len(defects))
    # 每一个Vec4i由四个整型数据构成，
    # 这四个整型数据的名称分别为：start_index, end_index, farthest_pt_index, fixpt_depth
    n = defects.shape[0]  # 缺陷數量
    print("凹點數量 :", n)
    for i in range(n):
        print("第", i, "個凹點索引 :", defects[i, 0])
        # s是startPoint, e是endPoint, f是farPoint, d是depth
        s, e, f, d = defects[i, 0]  # 取得index
        start = tuple(cnt[s][0])  # 由index取得start_point座標
        end = tuple(cnt[e][0])  # 由index取得end_point座標
        far = tuple(cnt[f][0])  # 由index取得far_point座標
        dst2 = cv2.line(dst2, start, end, colors[i], 10)  # 凸包連線
        dst2 = cv2.circle(dst2, far, 10, colors[i], -1)  # 畫實心圓
        print("start :", start)
        print("end :", end)
        print("far :", far)

plt.figure(figsize=(8, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("凸點")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("凹點")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檢測凸包距離

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/star_silver.png"  # 五角銀星
filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
filename = "data/findContours/heart1.jpg"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

n = len(contours)  # 輪廓數量
for i in range(n):
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據

    hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
    isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
    print(f"凸包是凸形       = {isConvex}")

    dst = cv2.polylines(image1, [hull], True, GREEN, 2)  # 將凸包連線# 近似多邊形連線
    # print(hull)   可以用這個指令了解凸包座標點

    # 檢測凸包距離

    pt = (50, 100)
    dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
    dist = cv2.pointPolygonTest(hull, pt, True)  # 檢測距離, True:距離
    print("距離 :", dist)
    dist = cv2.pointPolygonTest(hull, pt, False)  # 檢測距離, False:是否
    print("距離 :", dist)

    pt = (135, 100)
    dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
    dist = cv2.pointPolygonTest(hull, pt, True)  # 檢測距離, True:距離
    print("距離 :", dist)
    dist = cv2.pointPolygonTest(hull, pt, False)  # 檢測距離, False:是否
    print("距離 :", dist)

    pt = (200, 100)
    dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
    dist = cv2.pointPolygonTest(hull, pt, True)  # 檢測距離, True:距離
    print("距離 :", dist)
    dist = cv2.pointPolygonTest(hull, pt, False)  # 檢測距離, False:是否
    print("距離 :", dist)

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

# 檢測凸包距離

filename = "data/cs1.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
print(f"凸包是凸形       = {isConvex}")

filename = "data/cs1.bmp"
image0 = cv2.imread(filename, 0)  # 灰階讀取
image1 = image0.copy()

image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
cv2.polylines(image1, [hull], True, GREEN, 2)  # 近似多邊形連線

# ----------------內部點A的距離-------------------------
pt = (300, 150)
dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
dist = cv2.pointPolygonTest(hull, pt, True)
print("距離 :", dist)
dist = cv2.pointPolygonTest(hull, pt, False)  # 關係
print("距離 :", dist)  # 關係

# ----------------外部點B的距離-------------------------
pt = (300, 250)
dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
dist = cv2.pointPolygonTest(hull, pt, True)
print("距離 :", dist)
dist = cv2.pointPolygonTest(hull, pt, False)  # 關係
print("距離 :", dist)  # 關係

# ------------正好處于邊緣上的點C的距離-----------------
pt = (423, 112)
dst = cv2.circle(image1, pt, 5, RED, -1)  # 畫實心圓
dist = cv2.pointPolygonTest(hull, pt, True)
print("距離 :", dist)
dist = cv2.pointPolygonTest(hull, pt, False)  # 關係
print("距離 :", dist)  # 關係

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("邊緣")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# OpenCV_17_輪廓的特徵
print("------------------------------------------------------------")  # 60個

# 形狀與結構分析
# 輪廓檢驗

coin_filename = "D:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
# coin_filename = "D:/_git/vcs/_4.python/opencv/data/findContours/coin1.jpg"
# coin_filename = "D:/_git/vcs/_4.python/opencv/data/findContours/coin2.jpg"

image0 = cv2.imread(coin_filename, cv2.IMREAD_COLOR)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
blur = cv2.GaussianBlur(gray, (0, 0), 1.5, 1.5)  # 執行高斯模糊化
canny = cv2.Canny(blur.copy(), 60, 60)
canny_morphologyEx = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, np.ones((3, 3), "uint8"))

# cv2.RETR_EXTERNAL # 只取外輪廓。
contours, hierarchy = cv2.findContours(
    canny_morphologyEx.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

cv2.drawContours(image1, contours, -1, GREEN, 5)  # 繪製輪廓/-1:全部/色/線寬

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

# 多找到了兩個錯誤輪廓，要過濾掉
# 顯示所有圓度在0.8到1.2之間的輪廓
contours = [contour for contour in contours if 0.8 < circularity(contour) < 1.2]

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

cv2.drawContours(image1, contours, -1, RED, 2)  # 繪製輪廓/-1:全部/色/線寬

plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(canny_morphologyEx, cv2.COLOR_BGR2RGB))
plt.title("影像處理")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("輪廓檢驗")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直線擬合

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

# shape05.png 500X500黑圖正中央有一個斜30度的400X100白色長方形
# 故質心在 (250, 250), 面積 400*100, 周長 2*(400+100)=1000
print("真實質心 : (250, 250)")
print("真實面積", 400 * 100)
print("真實周長", 2 * (400 + 100))

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

n = len(contours)  # 輪廓數量
print("每個輪廓分別處理:")
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    # 直線擬合 ST
    rows, cols = image1.shape[:2]  # 輪廓大小
    vx, vy, x, y = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)  # 直線擬合
    print(f"共線正規化向量 = {vx}, {vy}")
    print(f"直線經過的點   = {x}, {y}")
    lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
    righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
    dst = cv2.line(image1, (0, lefty), (cols - 1, righty), GREEN, 10)  # 左到右繪線

draw_grid(dst)

# plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("直線擬合")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

# 紅外框
image1 = cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬
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
    # cv2.line(image1, (0, lefty), (cols - 1, righty), RED, 5)  # 左到右繪線

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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

contours, hierarchy = get_image_contours(image1)

n = len(contours)  # 輪廓數量
print("每個輪廓分別處理:")
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據

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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 100  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

# 找出圖像中的輪廓
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找出最大的輪廓
filtered_contours = max(contours, key=cv2.contourArea)  # 取出最大面積

# 輪廓 => 最小外接矩形
rect = cv2.minAreaRect(filtered_contours)  # 最小外接矩形 (中心(x,y), (寬,高), 旋轉角度)
(cx, cy), (w, h), angle = rect  # 取得旋轉矩形的中心點和旋轉角度
"""
print("最小外接矩形 :", rect)
print("中心點 :", cx, cy)
print("中心點 :", rect[0])
print("寬高 :", rect[1])
print("旋轉角度 :", angle)
print("旋轉角度 :", rect[2])
W = rect[1][0] * 2
H = rect[1][1] * 2
print("W = ", W, "H = ", H)
"""
box = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
box = np.intp(box)  # 將頂點轉換為整數座標
cv2.drawContours(image1, [box], 0, RED, 10)  # 繪製 最小外接矩形 輪廓

cv2.circle(image1, (int(cx), int(cy)), 10, BLUE, -1)  # 畫實心圓 中心點

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("輪廓檢驗")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# boxPoints 帶有旋轉的矩形框座標

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 輪廓 => 最小外接矩形
cnt = contours[0]  # 取得輪廓數據
rect = cv2.minAreaRect(cnt)  # 得到最小外接矩形的(中心(x,y), (寬,高), 旋轉角度)
(cx, cy), (w, h), angle = rect  # 取得旋轉矩形的中心點和旋轉角度
"""
print("最小外接矩形 :", rect)
print("中心點 :", cx, cy)
print("中心點 :", rect[0])
print("寬高 :", rect[1])
print("旋轉角度 :", angle)
print("旋轉角度 :", rect[2])
W = rect[1][0] * 2
H = rect[1][1] * 2
print("W = ", W, "H = ", H)
"""

points = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
print("最小外接矩形頂點座標 :\n", points)

# 最小外接矩形頂點
p0 = (int(points[0][0]), int(points[0][1]))
p1 = (int(points[1][0]), int(points[1][1]))
p2 = (int(points[2][0]), int(points[2][1]))
p3 = (int(points[3][0]), int(points[3][1]))

# 最小外接矩形頂點 畫出來
cv2.circle(image1, p0, 10, RED, -1)  # 畫實心圓 圓心
cv2.circle(image1, p1, 10, RED, -1)  # 畫實心圓 圓心
cv2.circle(image1, p2, 10, RED, -1)  # 畫實心圓 圓心
cv2.circle(image1, p3, 10, RED, -1)  # 畫實心圓 圓心

# 畫出直線
cv2.line(image1, p0, p1, GREEN, 3, lineType=cv2.LINE_AA)
cv2.line(image1, p1, p2, GREEN, 3, lineType=cv2.LINE_AA)
cv2.line(image1, p2, p3, GREEN, 3, lineType=cv2.LINE_AA)
cv2.line(image1, p3, p0, GREEN, 3, lineType=cv2.LINE_AA)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
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

for i in range(5):
    rotating_angle = 20 * i  # 順時針   # 旋轉矩形
    points = cv2.boxPoints(((cx, cy), (w, h), rotating_angle))
    p0, p1, p2, p3 = points[0], points[1], points[2], points[3]
    # 畫出四個頂點連線
    cv2.line(image, (int(p0[0]), int(p0[1])), (int(p1[0]), int(p1[1])), RED, 5)
    cv2.line(image, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), RED, 5)
    cv2.line(image, (int(p2[0]), int(p2[1])), (int(p3[0]), int(p3[1])), RED, 5)
    cv2.line(image, (int(p3[0]), int(p3[1])), (int(p0[0]), int(p0[1])), RED, 5)
    # 畫出來, 另法, 用drawContours
    points = np.intp(points)  # 將頂點轉換為整數座標
    cv2.drawContours(image, [points], 0, GREEN, 2)  # 繪製輪廓/一個/色/線寬

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("旋轉矩形")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

# 一個輪廓一個輪廓畫
for i in range(n):
    image1 = cv2.drawContours(image1, contours, i, RED, 10)  # 繪製輪廓/一個/色/線寬

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/loc3.jpg"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image1.shape, np.uint8)
mask = np.ones(image1.shape, dtype=np.uint8) * 127  # 新建一個灰圖

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

mask = cv2.drawContours(mask, contours, -1, RED, -1)  # 繪製輪廓/-1:全部/白/-1:填滿

loc = cv2.bitwise_and(image1, mask)

plt.subplot(311)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(312)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(313)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("location")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("計算圖像的Hu矩")

filename1 = "data/cs1.bmp"
filename2 = "data/cs2.bmp"
filename3 = "data/cs3.bmp"

image1 = cv2.imread(filename1)  # 彩色讀取
image2 = cv2.imread(filename2)  # 彩色讀取
image3 = cv2.imread(filename3)  # 彩色讀取

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 計算圖像的Hu矩
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

# ---------打印圖像1、圖像2、圖像3的特征值------------
print("image1.shape :", image1.shape)
print("image2.shape :", image2.shape)
print("image3.shape :", image3.shape)

# print("cv2.moments(gray1)['nu20'] =",cv2.moments(gray1)["nu20"])
# print("cv2.moments(gray1)['nu02'] =", cv2.moments(gray1)["nu02"])
# print("cv2.moments(gray1) :\n", cv2.moments(gray1))
# print("cv2.moments(gray2) :\n", cv2.moments(gray2))
# print("cv2.moments(gray3) :\n", cv2.moments(gray3))
# print("HuM1=\n", HuM1)
# print("HuM2=\n", HuM2)
# print("HuM3=\n", HuM3)
# print("HuM1[0]=\n", HuM1[0])

# 計算各圖像的Hu矩之差
# print("HuM1-HuM2=", HuM1 - HuM2)
# print("HuM1-HuM3=", HuM1 - HuM3)
# print("HuM2-HuM3=", HuM2 - HuM3)

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

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 構造矩形邊界
print("最小邊界矩形(包圍盒)")

n = len(contours)  # 輪廓數量
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
    cv2.drawContours(image1, [brcnt], -1, RED, 2)  # 繪製輪廓/-1:全部/色/線寬

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.subplot(211)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 構造矩形邊界

n = len(contours)  # 輪廓數量
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    print("最小邊界矩形(包圍盒) 紅")
    x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
    cv2.rectangle(image1, (x, y), (x + w, y + h), RED, 2)

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.subplot(211)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 輪廓數量
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    print("最小外接圓")
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 最小外接圓
    center = (int(x), int(y))  # 圓心座標取整數
    radius = int(radius)  # 圓半徑取整數
    cv2.circle(image1, center, radius, MAGENTA, 2)  # 畫圓  外接圓
    cv2.circle(image1, center, 10, RED, -1)  # 畫實心圓 圓心

plt.subplot(212)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("圓圈圈出來")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 橢圓框選

filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 輪廓數量
for i in range(n):
    # 共同
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    ellipse = cv2.fitEllipse(cnt)  # 橢圓擬合, 旋轉邊界的內切圓
    print("ellipse=", ellipse)
    cv2.ellipse(image1, ellipse, GREEN, 3)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("橢圓框選")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# approxPolyDP 輪廓近似

print("cv2.approxPolyDP() 輪廓近似 多邊形框選")

filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()
image2 = image0.copy()
image3 = image0.copy()
image4 = image0.copy()
image5 = image0.copy()
image6 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]  # 取得輪廓數據
perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似, epsilon=0.1*周長
epsilon = 0.1 * perimeter  # 指定輪廓近似的精度, 0.1*周長
approx = cv2.approxPolyDP(cnt, epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

# approxPolyDP 輪廓近似, epsilon=0.09*周長
epsilon = 0.09 * perimeter  # 指定輪廓近似的精度, 0.09*周長
approx = cv2.approxPolyDP(cnt, epsilon, True)
image3 = cv2.drawContours(image3, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

# approxPolyDP 輪廓近似, epsilon=0.055*周長
epsilon = 0.055 * perimeter  # 指定輪廓近似的精度, 0.055*周長
approx = cv2.approxPolyDP(cnt, epsilon, True)
image4 = cv2.drawContours(image4, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

# approxPolyDP 輪廓近似, epsilon=0.05*周長
epsilon = 0.05 * perimeter  # 指定輪廓近似的精度, 0.05*周長
approx = cv2.approxPolyDP(cnt, epsilon, True)
image5 = cv2.drawContours(image5, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

# approxPolyDP 輪廓近似, epsilon=0.02*周長
epsilon = 0.02 * perimeter  # 指定輪廓近似的精度, 0.02*周長
approx = cv2.approxPolyDP(cnt, epsilon, True)
image6 = cv2.drawContours(image6, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("0.1周長")

plt.subplot(233)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("0.09周長")

plt.subplot(234)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("0.055周長")

plt.subplot(235)
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))
plt.title("0.05周長")

plt.subplot(236)
plt.imshow(cv2.cvtColor(image6, cv2.COLOR_BGR2RGB))
plt.title("0.02周長")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/contours.bmp"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image1 = cv2.drawContours(image1, contours, 0, RED, 3)  # 繪製輪廓/-1:全部/色/線寬

cnt = contours[0]  # 取得輪廓數據

# cv2.convexHull()  # 計算凸包, 返回凸包頂點 坐標值/索引值
# 計算凸包1, True返回凸包頂點 坐標值
hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
print("計算凸包1, True返回凸包頂點 坐標值")
print(hull)

print("凸點數量 :", len(hull))
n = hull.shape[0]  # 凸點數量
print("凸點數量 :", n)
for i in range(n):
    print(hull[i])
    print(hull[i][0])
    print(hull[i, 0])
    # print("第", i, "個凸點索引 :", hull[i, 0], ", 座標 :", cnt[hull[i, 0]])
    # image1 = cv2.circle(image1, cnt[hull[i, 0]][0], 10, BLUE, -1)  # 畫實心圓
    # image1 = cv2.circle(image1, (hull[i][0], hull[i][1]), 10, BLUE, -1)  # 畫實心圓

# cv2.convexHull()  # 計算凸包, 返回凸包頂點 坐標值/索引值
# 計算凸包2, False返回凸包頂點 索引值
hull = cv2.convexHull(cnt, returnPoints=False)  # 計算凸包, 返回凸包頂點索引值
print("計算凸包2, False返回凸包頂點 索引值")
print(hull)

"""
cv2.imshow("image0", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/hand.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 尋找凸包，得到凸包的角點
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
print(f"凸包是凸形       = {isConvex}")

# 繪製凸包
cv2.polylines(image1, [hull], True, GREEN, 2)  # 近似多邊形連線

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("顯示凸包aaaa")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/hand.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 凸包
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt, returnPoints=False)  # 計算凸包, 返回凸包頂點索引值
# isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
# print(f"凸包是凸形       = {isConvex}")

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
    dst = cv2.line(image1, start, end, GREEN, 10)  # 凸包連線
    dst = cv2.circle(image1, far, 10, BLUE, -1)  # 畫實心圓
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

filename = "data/hand.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()
image2 = image0.copy()

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------凸包----------------------
cnt = contours[0]  # 取得輪廓數據
hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
print(f"凸包是凸形       = {isConvex}")

cv2.polylines(image1, [hull], True, GREEN, 2)  # 近似多邊形連線

# 凸檢測, 是否凸形
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：", cv2.isContourConvex(hull))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("result1")

# 逼近多邊形
cnt = contours[0]  # 取得輪廓數據

perimeter = cv2.arcLength(cnt, True)  # 計算輪廓周長

# approxPolyDP 輪廓近似, epsilon=0.01*周長
epsilon = 0.01 * perimeter  # 指定輪廓近似的精度
approx = cv2.approxPolyDP(cnt, epsilon, True)

image2 = cv2.drawContours(image2, [approx], 0, RED, 10)  # 繪製輪廓/一個/色/線寬

# 凸檢測, 是否凸形
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：", cv2.isContourConvex(approx))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("result2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename1 = "data/cs1.bmp"
filename2 = "data/cs3.bmp"
filename3 = "data/hand.bmp"

o1 = cv2.imread(filename1)  # 彩色讀取
o2 = cv2.imread(filename2)  # 彩色讀取
o3 = cv2.imread(filename3)  # 彩色讀取

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours1[0]
cnt2 = contours2[0]
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

filename1 = "data/cs1.bmp"
filename2 = "data/cs3.bmp"
filename3 = "data/hand.bmp"
o1 = cv2.imread(filename1)  # 彩色讀取
o2 = cv2.imread(filename2)  # 彩色讀取
o3 = cv2.imread(filename3)  # 彩色讀取
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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

# filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
filename = "data/hand.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image1, contours, -1, GREEN, 10)  # 繪製輪廓/-1:全部/色/線寬

cnt = contours[0]  # 取得輪廓數據

print("最小邊界矩形(包圍盒) 紅")
x, y, w, h = cv2.boundingRect(cnt)  # 邊界矩形(包圍盒)
cv2.rectangle(image1, (x, y), (x + w, y + h), RED, 3)
rectArea = w * h

con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

extend = float(con_area) / rectArea
print(extend)

hull = cv2.convexHull(cnt)  # 計算凸包, 返回凸包頂點坐標值
isConvex = cv2.isContourConvex(hull)  # 凸檢測, 是否凸形
print(f"凸包是凸形       = {isConvex}")

hull_area = cv2.contourArea(hull)  # 計算輪廓面積
print("輪廓面積 :", hull_area)

cv2.polylines(image1, [hull], True, GREEN, 2)  # 近似多邊形連線

solidity = float(con_area) / hull_area
print(solidity)

# extent = con_area / convex_area  # 計算Extent
# print("真實占比 輪廓面積 佔 凸包的 :", extent)

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("最小邊界矩形")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬

cnt = contours[0]  # 取得輪廓數據

con_area = cv2.contourArea(cnt)  # 計算輪廓面積
print("輪廓面積 :", con_area)

equiDiameter = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print("等效面積 :", equiDiameter)

(cx, cy) = (100, 100)
r = int(equiDiameter / 2)

cv2.circle(image1, (cx, cy), r, RED, 3)  # 畫圓  # 展示等直徑大小的圓

plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("等效面積")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 橢圓擬合

filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
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
cv2.ellipse(image1, ellipse, RED, 2)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("橢圓擬合")
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

filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
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
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
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

filename = "data/cc.bmp"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
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
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
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

filename = "data/ct.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
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
masko = np.zeros(image1.shape, np.uint8)
masko = np.ones(image1.shape, dtype=np.uint8) * 127  # 新建一個灰圖

masko = cv2.drawContours(masko, [cnt], -1, WHITE, -1)  # 繪製輪廓/-1:全部/白/-1:填滿
loc = cv2.bitwise_and(image1, masko)

# 顯示灰度結果
# loc=cv2.bitwise_and(gray,mask)
# cv2.imshow("mask",loc)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/ct.png"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]

# --------使用掩膜獲取感興趣區域的均值-----------------
mask = np.zeros(gray.shape, np.uint8)  # 構造mean所使用的掩膜，必須是單通道的
mask = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(mask, [cnt], 0, WHITE, -1)  # 繪製輪廓/一個/白/-1:填滿
meanVal = cv2.mean(image1, mask=mask)  # mask是區域，所以必須是單通道的
print("meanVal=\n", meanVal)

# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(image1.shape, np.uint8)
masko = np.ones(image1.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cv2.drawContours(masko, [cnt], -1, WHITE, -1)  # 繪製輪廓/-1:全部/白/-1:填滿
loc = cv2.bitwise_and(image1, masko)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/cs1.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
mask = np.ones(gray.shape, dtype=np.uint8) * 127  # 新建一個灰圖

cnt = contours[0]  # 取得輪廓數據
cv2.drawContours(mask, [cnt], 0, 255, -1)  # 繪製輪廓/一個/??/-1:填滿

# 計算極值
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])  # 最左
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])  # 最右
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])  # 最上
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])  # 最下

cv2.putText(image1, "L", leftmost, font, 1, RED, 2)  # 最左
cv2.putText(image1, "R", rightmost, font, 1, RED, 2)  # 最右
cv2.putText(image1, "T", topmost, font, 1, RED, 2)  # 最上
cv2.putText(image1, "B", bottommost, font, 1, RED, 2)  # 最下

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("計算極值")

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

filename = "data/contours0.bmp"
image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

cv2.imshow("original", image0)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------計算各個輪廓的長度和、平均長度--------------------
n = len(contours)  # 獲取輪廓個數
print("輪廓數量 :", n)

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
    temp = np.zeros(image1.shape, np.uint8)
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
(cx, cy), (w, h), angle = rect  # 取得旋轉矩形的中心點和旋轉角度

# 取得旋轉矩形的中心點和旋轉角度
(center_x, center_y), (w, h), angle = rect

box = cv2.boxPoints(rect)  # 获取最小外接矩形的4个顶点坐标
print("最小外接矩形頂點座標 :\n", box)

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


filename1 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape05.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

cv2.imshow("original", image0)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 二值化處理影像
thresh = 50  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
_, dst_binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Find all the contours in the thresholded image
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)

for i in range(n):  # 繪製中心點迴圈
    print("第", i, "個輪廓")
    cnt = contours[i]  # 取得輪廓數據
    # 畫輪廓
    cv2.drawContours(image1, contours, i, RED, 5)
    # 畫方向
    getOrientation(cnt, image1)

cv2.imshow("output", image1)
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
# filename = "D:/_git/vcs/_4.python/opencv/data/dilate_erode1.png"

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
print("輪廓數量 :", n)
for index in range(n):
    image2 = cv2.drawContours(
        image2, contours, index, color[index % 9], 10
    )  # 繪製輪廓  # image2為三通道才能顯示輪廓
"""

# 似無用
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")


filename = "D:/_git/vcs/_4.python/opencv/data/morphology/coin.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
filename = "D:/_git/vcs/_4.python/opencv/data/morphology/moon.jpg"
filename = "D:/_git/vcs/_4.python/opencv/data/_mask/cloud.jpg"
# filename = "D:/_git/vcs/_4.python/opencv/data/_shape/shape01.png"

image0 = cv2.imread(filename)  # 彩色讀取
image1 = image0.copy()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
get_contours_info(contours)

cv2.drawContours(image1, contours, -1, RED, 10)  # 繪製輪廓/-1:全部/色/線寬

plt.figure(figsize=(10, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(canny, cv2.COLOR_BGR2RGB))
plt.title("Canny")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓aaaa")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

contours, hierarchy = cv2.findContours(
    dst_binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在_gray影像的mask遮罩區域計算均值

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
cv2.circle(image1, minLoc, 20, GREEN, 3)  # 畫圓  # 最小像素值用綠色圓
cv2.circle(image1, maxLoc, 20, RED, 3)  # 畫圓  # 最大像素值用紅色圓

cv2.imshow("Image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------")  # 30個


dst = np.ones(image1.shape, dtype=np.uint8) * 127  # 新建一個灰圖

# 依次繪製輪廓
n = len(contours)  # 輪廓數量
print("輪廓數量 :", n)
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(image1.shape, np.uint8)  # 建立輪廓影像
    img = np.ones(image1.shape, dtype=np.uint8) * 127  # 新建一個灰圖
    dst = cv2.drawContours(dst, contours, i, colors[i], 5)  # 畫第i個輪廓


# 輪廓 => 最小外接矩形 => 畫上
cnt = contours[0]  # 取得輪廓數據
rect = cv2.minAreaRect(cnt)  # 最小外接矩形 (中心(x,y), (寬,高), 旋轉角度)
(cx, cy), (w, h), angle = rect  # 取得旋轉矩形的中心點和旋轉角度

box = cv2.boxPoints(rect)  # 獲取最小外接矩形的4個頂點坐標
box = np.intp(box)  # 將頂點轉換為整數座標
dst = cv2.drawContours(image1, [box], 0, GREEN, 10)  # 繪製 最小外接矩形 輪廓

# 最優擬合橢圓框選

cnt = contours[0]  # 取得輪廓數據
# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(cnt)  # 取得最優擬合橢圓數據  # 橢圓擬合, 旋轉邊界的內切圓
print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(image1, ellipse, GREEN, 2)  # 繪橢圓

ddddddddddddd

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


gray = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(gray, 50, 150)
canny = cv2.dilate(canny, None, iterations=1)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.GaussianBlur(image1, (3, 3), 0.5)  # 高斯平滑處理    #執行高斯模糊化
canny = cv2.Canny(image, 50, 200)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 可刪除
filename = "data/findContours/multiple.jpg"
filename = "data/moments.bmp"
filename = "data/contours.bmp"
filename = "data/cc.bmp"


gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

