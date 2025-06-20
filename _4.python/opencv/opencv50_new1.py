"""
opencv 集合 新進1

"""

from opencv_common import *

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("------------------------------------------------------------")  # 60個

print("opencv 01")
print("練習組合成一張大圖 picasa效果")

filename1 = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename2 = "C:/_git/vcs/_4.python/_data/bear.jpg"
filename3 = "C:/_git/vcs/_4.python/_data/panda.jpg"

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)
image3 = cv2.imread(filename3)

image1 = cv2.resize(image1, (image1.shape[1] // 2, image1.shape[0] // 2))
image2 = cv2.resize(image2, (image2.shape[1] // 2, image2.shape[0] // 2))
image3 = cv2.resize(image3, (image3.shape[1] // 3, image3.shape[0] // 3))

output = np.zeros((768, 1024, 3), dtype="uint8")  # 設定合成的影像為一張全黑的畫布

x_st = 50
y_st = 50
w, h = image1.shape[1], image1.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image1[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 300
y_st = 150
w, h = image2.shape[1], image2.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image2[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 350
y_st = 350
w, h = image3.shape[1], image3.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image3[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

print("opencv 02")
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

image1 = cv2.imread(filename)

# 建立mask
mask = np.zeros(image1.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 400, 400)
cv2.grabCut(image1, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

image3 = image1 * mask2[:, :, np.newaxis]

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(mask)
plt.title("mask")

plt.subplot(223)
plt.imshow(mask2)
plt.title("mask2")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 03")
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

o = cv2.imread(filename)

image2 = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2], np.uint8)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)
cv2.grabCut(o, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)

mask2 = cv2.imread("images/mask.png", 0)

mask2Show = cv2.imread("images/mask.png", -1)

mask[mask2 == 0] = 0
mask[mask2 == 255] = 1
mask, bgd, fgd = cv2.grabCut(o, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
ogc = o * mask[:, :, np.newaxis]

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(mask2Show, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(ogc, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

print("opencv 04")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
o = cv2.imread(filename)

bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)

mask2 = np.zeros(o.shape[:2], np.uint8)
mask2[30:512, 50:400] = 3
mask2[50:300, 150:200] = 1
cv2.grabCut(o, mask2, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask2 == 2) | (mask2 == 0), 0, 1).astype("uint8")
ogc = o * mask2[:, :, np.newaxis]

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(ogc, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 13")
print("去除圖片的雜訊 fastNlMeansDenoisingColored")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = cv2.imread(filename)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image_denoised = cv2.fastNlMeansDenoisingColored(image, h=5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_denoised, cv2.COLOR_BGR2RGB))
plt.title("Denoise")

plt.suptitle("去除圖片的雜訊\nfastNlMeansDenoisingColored")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 15")
print("對比度增強 CLAHE")
print("生成自適應均衡化圖像 createCLAHE")

# 自適應直方圖均衡化（Adaptive Histogram Equalization, AHE）
# 限制對比度 自適應直方圖均衡化(Contrast Limited Adaptive Histogram Equalization, CLAHE)

image = cv2.imread("data/building.png", 0)
# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 創建 CLAHE  對象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 創建 CLAHE  對象
# clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(28, 28))

# 限制對比度的自適應閾值均衡化
cl1 = clahe.apply(image)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原始圖像")

plt.subplot(122)
plt.imshow(cv2.cvtColor(cl1, cv2.COLOR_BGR2RGB))
plt.title("生成自適應均衡化圖像\ncreateCLAHE")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 27")

image = cv2.imread(filename)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

contrast = 200
brightness = 0
output = image * (contrast / 127 + 1) - contrast + brightness  # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

plt.subplot(122)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 28")

image = cv2.imread(filename)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

output = image  # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(image, output, alpha, beta)  # 套用 convertScaleAbs

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 31 漸層色")

w, h = 400, 400
image = np.zeros([h, w, 3])
for i in range(h):
    image[i, :, 1] = int(256 * i / 400)  # 從上往下填入綠色漸層

image = image.astype("float32") / 255  # 轉換內容類型

# NG plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.imshow(image)
plt.title("漸層色")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 32 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 開啟圖片

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

h = image.shape[0]  # 取得圖片高度
w = image.shape[1]  # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("logo處理1")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 33 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

h = image.shape[0]
w = image.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x] = [0, 255, 255, 255]  # 亮色改成黃色

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("logo處理2")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 34")
filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

bg = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)  # 開啟背景圖

bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA

image = cv2.imread(filename2, cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA

h = image.shape[0]  # 取得圖片高度
w = image.shape[1]  # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = image[y, x, 2]  # 取得該像素的紅色值
        g = image[y, x, 1]  # 取得該像素的綠色值
        b = image[y, x, 0]  # 取得該像素的藍色值
        if r > 20 and r < 80 and g < 190 and g > 110 and b < 150 and b > 60:
            image[y, x] = bg[y, x]  # 如果在範圍內的顏色，換成背景圖的像素值


plt.subplot(121)
plt.imshow(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))
plt.title("bg")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("image")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 35 cv2.floodFill()")


def floodFill(
    source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE
):
    result = source.copy()
    cv2.floodFill(
        result,
        mask=mask,
        seedPoint=seedPoint,
        newVal=newVal,
        loDiff=loDiff,
        upDiff=upDiff,
        flags=flags,
    )
    return result


image = cv2.imread(filename)
h, w = image.shape[:2]  # 取得原始影像的長寬

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 製作 mask，長寬都要加上 2
image1 = floodFill(image, mask, (100, 10), RED, (100, 100, 60), (100, 100, 100))

image = cv2.imread(filename)
h, w = image.shape[:2]  # 取得原始影像的長寬

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 全黑遮罩
mask = 255 - mask  # 變成全白遮罩
mask[0:100, 0:200] = 0  # 將左上角長方形變成黑色

# 只處理mask區域
image2 = floodFill(image, mask, (100, 10), RED, (100, 100, 60), (200, 200, 200))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("image1")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("image2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 36 測試 凸透鏡 效果")


def convex(src_image, raw, effect):
    col, row, channel = raw[:]  # 取得圖片資訊
    cx, cy, r = effect[:]  # 取得凸透鏡的範圍
    output = np.zeros([row, col, channel], dtype=np.uint8)  # 產生空白畫布
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5  # 計算每個點與中心點的距離
            if d <= r:
                nx = int((x - cx) * d / r + cx)  # 根據不同的位置，產生新的 nx，越靠近中心形變越大
                ny = int((y - cy) * d / r + cy)  # 根據不同的位置，產生新的 ny，越靠近中心形變越大
                output[y, x, :] = src_image[ny, nx, :]  # 產生新的圖
            else:
                output[y, x, :] = src_image[y, x, :]  # 如果在半徑範圍之外，原封不動複製過去
    return output


image = cv2.imread(filename)
image = convex(image, (300, 400, 3), (150, 130, 100))  # 提交參數數值，進行凸透鏡效果

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("凸透鏡 效果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 37")

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)

w = image1.shape[1]  # 讀取圖片寬度
h = image1.shape[0]  # 讀取圖片高度

for i in range(w):
    image1[:, i, 0] = image1[:, i, 0] * ((300 - i) / 300) + image2[:, i, 0] * (
        i / 300
    )  # 藍色按照比例混合
    image1[:, i, 1] = image1[:, i, 1] * ((300 - i) / 300) + image2[:, i, 1] * (
        i / 300
    )  # 紅色按照比例混合
    image1[:, i, 2] = image1[:, i, 2] * ((300 - i) / 300) + image2[:, i, 2] * (
        i / 300
    )  # 綠色按照比例混合

image = image1.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 38 加上logo")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

mona = cv2.imread(filename)

logo = cv2.imread(
    logo_filename, cv2.IMREAD_UNCHANGED
)  # 使用 cv2.IMREAD_UNCHANGED 讀取 png，保留 alpha 色版

mona_w = mona.shape[1]  # 蒙娜麗莎寬度
mona_h = mona.shape[0]  # 蒙娜麗莎高度
logo_w = logo.shape[1]  # logo 寬度
logo_h = logo.shape[0]  # logo 高度
dh = int((mona_h - logo_h) / 2)  # 如果 logo 要垂直置中，和上方的距離
h = dh + logo_h  # 計算蒙娜麗莎裡，logo 所在的高度位置

# 透過迴圈，根據背景透明度，計算出該像素的顏色
for i in range(logo_w):
    mona[dh:h, i, 0] = mona[dh:h, i, 0] * (1 - logo[:, i, 3] / 255) + logo[:, i, 0] * (
        logo[:, i, 3] / 255
    )
    mona[dh:h, i, 1] = mona[dh:h, i, 1] * (1 - logo[:, i, 3] / 255) + logo[:, i, 1] * (
        logo[:, i, 3] / 255
    )
    mona[dh:h, i, 2] = mona[dh:h, i, 2] * (1 - logo[:, i, 3] / 255) + logo[:, i, 2] * (
        logo[:, i, 3] / 255
    )

image = mona.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("xxxx")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 40 cv讀取鍵盤 按上下調整亮度 按左右調整對比度 按ESC離開")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = cv2.imread(filename)


# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c / 100 + 1) - c + b  # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output


contrast = 0  # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值

cv2.imshow("ImageShow", image)

while True:
    keycode = cv2.waitKey(0)
    if keycode == 0:
        brightness = brightness + 5  # 按下鍵盤的「上」，增加亮度
    if keycode == 1:
        brightness = brightness - 5  # 按下鍵盤的「下」，減少亮度
    if keycode == 2:
        contrast = contrast - 5  # 按下鍵盤的「右」，增加對比度
    if keycode == 3:
        contrast = contrast + 5  # 按下鍵盤的「左」，減少對比度
    if keycode == 113:
        contrast, brightness = 0, 0  # 按下鍵盤的「q」，恢復預設值
    if keycode == 27:
        break
    show_image = image.copy()  # 複製原始圖片
    show_image = adjust(show_image, contrast, brightness)  # 根據亮度和對比度的調整值，輸出新的圖片
    cv2.imshow("ImageShow", show_image)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 46 測試 cv2.linearPolar 空間變換 極座標變換")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

src = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)

# 圖像的極坐標變換
dst = cv2.linearPolar(src, (508, 503), 550, cv2.INTER_LINEAR)

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("極座標變換")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 47 測試 cv2.logPolar 空間變換 極座標變換")

src = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)

# 圖像的極坐標變換
M = 150
dst = cv2.logPolar(src, (400 // 2, 300 // 2), M, cv2.WARP_FILL_OUTLIERS)

# 顯示極坐標變化的結果
print(src.shape)
print(dst.shape)

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("極座標變換")

show()

# 看不出什麼東西

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 48 對比度增強2")


# 分段線性變換
def piecewiseLinear(image, point1, point2):
    # 確保 point1 在 point2的左下角
    x1, y1 = point1
    x2, y2 = point2
    # 0 - point1.x
    a1 = float(y1) / x1
    b1 = 0
    # point1.x - point2.x
    a2 = float(y2 - y1) / float(x2 - x1)
    b2 = y1 - a2 * x1
    print(a2)
    # point2.x - 255
    a3 = float(255 - y2) / (255 - x2)
    b3 = 255 - a3 * 255
    # 輸出圖像
    outPutImage = np.zeros(image.shape, np.uint8)
    # 圖像的寬高
    rows, cols = image.shape
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            if pixel <= x1:
                outPixel = a1 * pixel + b1
            elif pixel > x1 and pixel < x2:
                outPixel = a2 * pixel + b2
            else:
                outPixel = a3 * pixel + b3
            outPixel = round(outPixel)
            outPutImage[r][c] = outPixel
    return outPutImage


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 分段線性變換
outPutImage = piecewiseLinear(image, (100, 50), (150, 230))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(outPutImage, cv2.COLOR_BGR2RGB))
plt.title("分段線性變換")

show()

# 顯示直方圖正規化後圖片的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = outPutImage.shape
histSeq = outPutImage.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 49 對比度增強3 histNormalized")


# 直方圖正規化
# 1、若輸入是 8 位圖 ，一般設置 O_min = 0，O_max = 255
# 2、若輸入的是歸一化的圖像，一般設置 O_min = 0，O_max = 1
def histNormalized(InputImage, O_min=0, O_max=255):
    # 得到輸入圖像的最小灰度值
    I_min = np.min(InputImage)
    # 得到輸入圖像的最大灰度值
    I_max = np.max(InputImage)
    # 得到輸入圖像的寬高
    rows, cols = InputImage.shape
    # 輸出圖像
    OutputImage = np.zeros(InputImage.shape, np.float32)
    # 輸出圖像的映射
    cofficient = float(O_max - O_min) / float(I_max - I_min)
    for r in range(rows):
        for c in range(cols):
            OutputImage[r][c] = cofficient * (InputImage[r][c] - I_min) + O_min
    return OutputImage


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 直方圖正規化
histNormResult = histNormalized(image)
# 數據類型轉換，灰度級顯示
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(histNormResult, cv2.COLOR_BGR2RGB))
plt.title("直方圖正規化的圖片")

show()


"""
#如果輸入圖像是歸一化的圖像
image_0_1 = image/255.0
#直方圖正規化
histNormResult = histNormalized(image_0_1,0,1)
#保存結果
histNormResult = 255.0*histNormResult
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
"""
# 顯示直方圖正規化後圖片的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = image.shape
histNormResultSeq = histNormResult.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histNormResultSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 50 對比度增強5 equalHist")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 直方圖均衡化
def equalHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 計算灰度直方圖
    grayHist = calcGrayHist(image)
    # 計算累積灰度直方圖
    zeroCumuMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p - 1] + grayHist[p]
    # 根據直方圖均衡化得到的輸入灰度級和輸出灰度級的映射
    outPut_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (rows * cols)
    for p in range(256):
        q = cofficient * float(zeroCumuMoment[p]) - 1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
    # 得到直方圖均衡化後的圖像
    equalHistImage = np.zeros(image.shape, np.uint8)
    for r in range(rows):
        for c in range(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]]
    return equalHistImage


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 直方圖均衡化
result = equalHist(image)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化")

show()

# 直方圖均衡話後的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = image.shape
histEqualResultSeq = result.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histEqualResultSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("opencv 51 邊緣擴充/擴充邊界 copyMakeBorder")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image0 = cv2.imread(filename)

# 擴充邊界
top = 50
bottom = 100
left = 150
right = 200
image1 = cv2.copyMakeBorder(image0, top, bottom, left, right, cv2.BORDER_DEFAULT)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("邊緣擴充")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy import signal

print("opencv 52 圖像平滑 sameConv2d")

# 輸入矩陣
I = np.array([[1, 2], [3, 4]], np.float32)
# I 的高和寬
H1, W1 = I.shape[:2]
# 卷積核
K = np.array([[-1, -2], [2, 1]], np.float32)
# K 的高和寬
H2, W2 = K.shape[:2]
# 計算 full 卷積
c_full = signal.convolve2d(I, K, mode="full")
# 指定錨點的位置
kr, kc = 1, 0
# 根據錨點位置，從 full 卷積中截取得到 same 卷積
c_same = c_full[H2 - kr - 1 : H1 + H2 - kr - 1, W2 - kc - 1 : W1 + W2 - kc - 1]
print(c_same)

print("------------------------------------------------------------")  # 60個

print("opencv 53 圖像平滑 sepConv")

from scipy import signal

kernel1 = np.array([[1, 2, 3]], np.float32)
kernel2 = np.array([[4], [5], [6]], np.float32)
# 計算兩個核的全卷積
kernel = signal.convolve2d(kernel1, kernel2, mode="full")

print("------------------------------------------------------------")  # 60個

print("opencv 54 圖像平滑 conv")

from scipy import signal

# 圖像矩陣
"""
I=np.array([[1,2,3,10,12],
            [32,43,12,4,190],
            [12,234,78,0,12],
            [43,90,32,8,90],
            [71,12,4,98,123]],np.float32)
"""
I = np.ones((10, 10), np.float32)
I[1:3, 3:5] = 5
I[3:5, 4:7] = 3

# 卷積核
"""
    kernel = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])
"""

kernel1 = np.array([[1, 3, 4], [9, 10, 2], [-1, 10, 2]], np.float32)
kernel2 = np.array([[-1, 2, 3], [4, 5, 6], [10, 9, 10]], np.float32)
# kernel1 = np.array([[-1,2,3]],np.float32)
# kernel2 = np.array([[10],[43],[1]],np.float32)
kernel = signal.convolve2d(kernel1, kernel2, mode="full")
print(kernel)

# 第一種方式:直接進行卷積運算得到的結果
I_Kernel = signal.convolve2d(I, kernel, mode="same", boundary="symm", fillvalue=0)

# 第二種方式:用可分離卷積核性質得到的結果
I_kernel1 = signal.convolve2d(I, kernel1, mode="same", boundary="wrap", fillvalue=0)
I_kernel1_kernel2 = signal.convolve2d(
    I_kernel1, kernel2, mode="same", boundary="wrap", fillvalue=0
)

# print(I_Kernel)
print("*******************")
print(np.max(np.abs(I_Kernel - I_kernel1_kernel2)))
print("********************")
print(I_Kernel)
print(I_kernel1_kernel2)

print("------------------------------------------------------------")  # 60個

print("opencv 55 圖像平滑 conv2")

from scipy import signal

# 圖像矩陣
I = np.array(
    [
        [1, 2, 3, 10, 12],
        [32, 43, 12, 4, 190],
        [12, 234, 78, 0, 12],
        [43, 90, 32, 8, 90],
        [71, 12, 4, 98, 123],
    ],
    np.float32,
)
# 卷積核
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
# full 卷積
fullConv = signal.convolve2d(I, kernel, mode="full", boundary="fill", fillvalue=0)
# same 卷積
sameConv = signal.convolve2d(I, kernel, mode="same", boundary="symm")
# valid 卷積
validConv = signal.convolve2d(I, kernel, mode="valid")
print(fullConv)
print(sameConv)
print(validConv)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 67 閾值分割 threshold")

src = np.array(
    [[123, 234, 68], [33, 51, 17], [48, 98, 234], [129, 89, 27], [45, 167, 134]],
    np.uint8,
)
# 手動設置閾值
the = 150
maxval = 255
dst = cv2.threshold(src, the, maxval, cv2.THRESH_BINARY)

# Otsu 閾值處理
otsuThe = 0
otsuThe, dst_Otsu = cv2.threshold(src, otsuThe, maxval, cv2.THRESH_OTSU)
print(otsuThe, dst_Otsu)

# TRIANGLE 閾值處理
triThe = 0
triThe, dst_tri = cv2.threshold(src, triThe, maxval, cv2.THRESH_TRIANGLE)
print(triThe, dst_tri)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 68 閾值分割 threshTwoPeaks")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 返回閾值和二值圖
def threshTwoPeaks(image):
    # 計算回復直方圖
    histogram = calcGrayHist(image)
    # 找到灰度直方圖的最大峰值對應的灰度值
    maxLoc = np.where(histogram == np.max(histogram))
    firstPeak = maxLoc[0]
    print(maxLoc[0])
    # 尋找灰度直方圖的 " 第二個峰值 " 對應的灰度值
    measureDists = np.zeros([256], np.float32)
    for k in range(256):
        measureDists[k] = pow(k - firstPeak, 2) * histogram[k]
    maxLoc2 = np.where(measureDists == np.max(measureDists))
    secondPeak = maxLoc2[0]
    # 找到兩個峰值之間的最小值對應的灰度值，作為閾值
    thresh = 0
    if firstPeak > secondPeak:
        temp = histogram[int(secondPeak) : int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0] + 1
    else:
        temp = histogram[int(firstPeak) : int(secondPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = firstPeak + minLoc[0] + 1
    # 找到閾值後進行閾值處理，得到二值圖
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out <= thresh] = 0
    return (thresh, threshImage_out)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

thresh, threshImage_out = threshTwoPeaks(image)
# 輸出直方圖技術得到的閾值
print(thresh)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(threshImage_out, cv2.COLOR_BGR2RGB))
plt.title("threshTwoPeaks 閾值化得到的二值圖")

show()

print("------------------------------------------------------------")  # 60個

print("opencv 69 閾值分割 threshEntroy")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 熵閾值法
def threshEntroy(image):
    rows, cols = image.shape
    # 求灰度直方圖
    grayHist = calcGrayHist(image)
    # 歸一化灰度直方圖
    normGrayHist = grayHist / float(rows * cols)
    # 計算累加直方圖，也稱零階累加矩
    zeroCumuMoment = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k - 1] + normGrayHist[k]
    # 計算各個灰度級的熵
    entropy = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0:
            if normGrayHist[k] == 0:
                entropy[k] = 0
            else:
                entropy[k] = -normGrayHist[k] * math.log10(normGrayHist[k])
        else:
            if normGrayHist[k] == 0:
                entropy[k] = entropy[k - 1]
            else:
                entropy[k] = entropy[k - 1] - normGrayHist[k] * math.log10(
                    normGrayHist[k]
                )
    # 找閾值
    fT = np.zeros([256], np.float32)
    ft1, ft2 = 0.0, 0.0
    totalEntroy = entropy[255]
    for k in range(255):
        # 找最大值
        maxFront = np.max(normGrayHist[0 : k + 1])
        maxBack = np.max(normGrayHist[k + 1 : 256])
        if (
            maxFront == 0
            or zeroCumuMoment[k] == 0
            or maxFront == 1
            or zeroCumuMoment[k] == 1
            or totalEntroy == 0
        ):
            ft1 = 0
        else:
            ft1 = (
                entropy[k]
                / totalEntroy
                * (math.log10(zeroCumuMoment[k]) / math.log10(maxFront))
            )
        if (
            maxBack == 0
            or 1 - zeroCumuMoment[k] == 0
            or maxBack == 1
            or 1 - zeroCumuMoment[k] == 1
        ):
            ft2 = 0
        else:
            if totalEntroy == 0:
                ft2 = math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack)
            else:
                ft2 = (1 - entropy[k] / totalEntroy) * (
                    math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack)
                )
        fT[k] = ft1 + ft2
    # 找最大值的索引，作為得到的閾值
    threshLoc = np.where(fT == np.max(fT))
    thresh = threshLoc[0][0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return (threshold, thresh)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 閾值處理
threshold, thresh = threshEntroy(image)
print(thresh)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(threshold, cv2.COLOR_BGR2RGB))
plt.title("threshEntroy 閾值後的二值化圖像")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 70 閾值分割 otsu")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([1, 256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[0][image[r][c]] += 1
    return grayHist


def ostu(image):
    rows, cols = image.shape
    # 計算圖像的灰度直方圖
    grayHist = calcGrayHist(image)
    # 歸一化灰度直方圖
    uniformGrayHist = grayHist / float(rows * cols)
    # 計算零階累積矩和一階累積矩
    zeroCumuMoment = np.zeros([1, 256], np.float32)
    oneCumuMoment = np.zeros([1, 256], np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[0][k] = uniformGrayHist[0][0]
            oneCumuMoment[0][k] = (k + 1) * uniformGrayHist[0][0]
        else:
            zeroCumuMoment[0][k] = zeroCumuMoment[0][k - 1] + uniformGrayHist[0][k]
            oneCumuMoment[0][k] = oneCumuMoment[0][k - 1] + k * uniformGrayHist[0][k]
    # 計算類間方差
    variance = np.zeros([1, 256], np.float32)
    for k in range(255):
        if zeroCumuMoment[0][k] == 0:
            variance[0][k] = 0
        else:
            variance[0][k] = math.pow(
                oneCumuMoment[0][255] * zeroCumuMoment[0][k] - oneCumuMoment[0][k], 2
            ) / (zeroCumuMoment[0][k] * (1.0 - zeroCumuMoment[0][k]))
    # 找到閾值
    threshLoc = np.where(variance[0][0:255] == np.max(variance[0][0:255]))
    thresh = threshLoc[0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return threshold


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 閾值算法
ostu_threshold = ostu(image)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(ostu_threshold, cv2.COLOR_BGR2RGB))
plt.title("ostu_threshold 閾值處理的結果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 72 閾值分割 adaptiveThresh")


def adaptiveThresh(I, winSize, ratio=0.15):
    # 第一步：對圖像矩陣進行均值平滑
    I_smooth = cv2.boxFilter(I, cv2.CV_32FC1, winSize)
    # I_smooth = cv2.medianBlur(I,winSize)
    # 第二步：原圖像矩陣與平滑結果做差
    out = I - (1.0 - ratio) * I_smooth
    # 第三步：對 out 進行全局閾值處理，差值大於等於零，輸出值為255，反之為零
    out[out >= 0] = 255
    out[out < 0] = 0
    out = out.astype(np.uint8)
    return out


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

out = adaptiveThresh(image, (31, 31), 0.15)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
plt.title("out")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 76 邊緣檢測 prewitt")

from scipy import signal


# prewtt卷積
def prewitt(
    I,
    _boundary="symm",
):
    # 因為prewitt_X是可分離卷積核,根據卷積運算的結合律,可以分兩次小卷積核運算
    # 1：垂直方向的 " 均值平滑 "
    ones_y = np.array([[1], [1], [1]], np.float32)
    i_conv_pre_x = signal.convolve2d(I, ones_y, mode="same", boundary=_boundary)
    # 2：水平方向的差分
    diff_x = np.array([[1, 0, -1]], np.float32)
    i_conv_pre_x = signal.convolve2d(
        i_conv_pre_x, diff_x, mode="same", boundary=_boundary
    )
    # 因為prewitt_y是可分離卷積核，根據卷積運算的結合律，可以分兩次小卷積核運算
    # 1：水平方向的"均值平滑 "
    ones_x = np.array([[1, 1, 1]], np.float32)
    i_conv_pre_y = signal.convolve2d(I, ones_x, mode="same", boundary=_boundary)
    # 2：垂直方向的差分
    diff_y = np.array([[1], [0], [-1]], np.float32)
    i_conv_pre_y = signal.convolve2d(
        i_conv_pre_y, diff_y, mode="same", boundary=_boundary
    )
    return (i_conv_pre_x, i_conv_pre_y)


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 圖像矩陣 和 兩個 prewitt算子 的卷積
i_conv_pre_x, i_conv_pre_y = prewitt(image)

# 取絕對值,分別得到水平方向和垂直方向的邊緣強度
abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)

# 水平方向和垂直方向的邊緣強度的灰度級顯示
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)

# 利用 abs_i_conv_pre_x 和 abs_i_conv_pre_y 求最終的邊緣強度
# 求邊緣強度，有多重方式，這里使用的是插值法
edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
# 邊緣強度的灰度級顯示
edge[edge > 255] = 255
edge = edge.astype(np.uint8)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(edge_x, cv2.COLOR_BGR2RGB))
plt.title("edge_x")

plt.subplot(223)
plt.imshow(cv2.cvtColor(edge_y, cv2.COLOR_BGR2RGB))
plt.title("edge_y")

plt.subplot(224)
plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("edge")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("I", I)

# canny 邊緣檢測
edge = cv2.Canny(I, 50, 200)

# 顯示二值化邊緣
cvshow("edge", edge)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.subplot(121)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# canny 邊緣檢測
edge = cv2.Canny(I, 50, 200)

plt.subplot(122)
plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("edge")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 89 將一彩圖做RGB分離")

filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(filename, cv2.IMREAD_COLOR)

# 得到三個顏色通道
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]

# 顯示三個顏色通道
cvshow("B", b)
cvshow("G", g)
cvshow("R", r)

# 8位圖轉換為 浮點型
fimage = image / 255.0
fb = fimage[:, :, 0]
fg = fimage[:, :, 1]
fr = fimage[:, :, 2]

# 顯示三個顏色
cvshow("f B", fb)
cvshow("f G", fg)
cvshow("f R", fr)

plt.subplot(231)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B")

plt.subplot(232)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G")

plt.subplot(233)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R")

plt.subplot(234)
plt.imshow(cv2.cvtColor(fb, cv2.COLOR_BGR2RGB))
plt.title("b")

plt.subplot(235)
plt.imshow(cv2.cvtColor(fg, cv2.COLOR_BGR2RGB))
plt.title("g")

plt.subplot(236)
plt.imshow(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB))
plt.title("r")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 91")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

temp = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(temp.shape)

tempHt, tempWd = temp.shape
print(tempHt, tempWd)

height, width = temp.shape[:2]

array = temp.reshape(1, -1)

print(array.shape)

EM_sum = np.double(np.sum(array[0]))
print(EM_sum)

square_arr = np.square(array[0])
EM2_sum = np.double(np.sum(square_arr))
print(EM2_sum)

product_array = temp.reshape(1, -1)
_sum = np.double(np.sum(product_array[0]))

print("------------------------------------------------------------")  # 60個

print("opencv 92")
"""
#例外的寫法
img = cv2.imread('digits.png',0)
if img is None:
    raise Exception("we need the digits.png image from samples/data here !")
"""
print("------------------------------------------------------------")  # 60個

print("opencv 93")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image0 = cv2.imread(filename)

image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)  # 灰階

_, image2 = cv2.threshold(image1, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白

cvshow("image0", image0)
cvshow("image1", image1)
cvshow("image2", image2)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("灰階")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("反白")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 97")

# 圖形型態

from matplotlib import cm
from itertools import product


def func(x, y):
    return (x + y) * np.exp(-5.0 * (x**2 + y**2))


y, x = np.mgrid[-1:1:100j, -1:1:100j]
z = func(x, y)
zabs = np.abs(z)
alpha = cm.ScalarMappable(cmap="gray").to_rgba(zabs)[:, :, 0].copy()
z1 = cm.ScalarMappable(cmap="gray").to_rgba(z)[:, :, 0].copy()
z4 = cm.ScalarMappable(cmap="jet").to_rgba(z)
z3 = z4[:, :, 2::-1].copy()
z4[:, :, -1] = alpha
z4[:, :, :3] = z3

for dtype, img in product(["uint8", "uint16"], [z1, z3, z4]):
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    img = (img * np.iinfo(dtype).max).astype(dtype)
    fn = "tmp_{}_{}.png".format(dtype, nchannel)
    cv2.imwrite(fn, img)

from glob import glob

files = glob("uint*.png")
flags = ["ANYCOLOR", "ANYDEPTH", "COLOR", "GRAYSCALE", "UNCHANGED"]


def f(fn, flag):
    _flag = getattr(cv2, "IMREAD_" + flag)
    img = cv2.imread(fn, _flag)
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    return "{}, {}ch".format(img.dtype, nchannel)


# 圖形輸出

img = cv2.imread("data/lena.jpg")
for quality in [90, 60, 30]:
    cv2.imwrite(
        "tmp_lena_q{:02d}.jpg".format(quality), img, [cv2.IMWRITE_JPEG_QUALITY, quality]
    )

from matplotlib.cm import ScalarMappable


def func(x, y, a):
    return (x * x - y * y) * np.sin((x + y) / a) / (x * x + y * y)


def make_image(x, y, a, dtype="uint8"):
    z = func(x, y, a)
    img_rgba = ScalarMappable(cmap="jet").to_rgba(z)
    img = (img_rgba[:, :, 2::-1] * np.iinfo(dtype).max).astype(dtype)
    return img


y, x = np.ogrid[-10:10:250j, -10:10:500j]
img_8bit = make_image(x, y, 0.5, dtype="uint8")
img_16bit = make_image(x, y, 0.5, dtype="uint16")

cv2.imwrite("tmp_img_8bit.jpg", img_8bit)
cv2.imwrite("tmp_img_16bit.jpg", img_16bit)
cv2.imwrite("tmp_img_8bit.png", img_8bit)
cv2.imwrite("tmp_img_16bit.png", img_16bit)

# 位元組序列與圖形相互轉換

with open("tmp_img_8bit.png", "rb") as f:
    png_str = f.read()

png_data = np.frombuffer(png_str, np.uint8)
img = cv2.imdecode(png_data, cv2.IMREAD_UNCHANGED)
res, jpg_data = cv2.imencode(".jpg", img)
jpg_str = jpg_data.tobytes()

# 使用`Image`將`imencode()`解碼的結果直接內嵌到Notebook中
res, jpg_data = cv2.imencode(".jpg", img_8bit)

"""
from IPython.display import Image
Image(data=jpg_data.tobytes())  # 用IPython顯示圖片
"""

# 視訊輸出


def test_avi_output(fn, fourcc):
    # fourcc = cv2.FOURCC(*fourcc)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    vw = cv2.VideoWriter(fn, fourcc, 15, (500, 250), True)
    if not vw.isOpened():
        return
    for a in np.linspace(0.1, 2, 100):
        img = make_image(x, y, a)
        vw.write(img)
    vw.release()


test_avi_output("tmp_fmp4.avi", "fmp4")

from os import path

for quantizer in [1, 10, 20, 30, 40]:
    fn = "tmp_x264_q{:02d}.avi".format(quantizer)
    test_avi_output(fn, "x264")
    fsize = path.getsize(fn)
    print("quantizer = {:02d}, size = {:07d} bytes".format(quantizer, fsize))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 100")

"""
    scpy2.opencv.warp_demo：仿射變換和透視變換的示範程式，
    可以透過滑鼠拖曳圖中藍色三角形和四邊形的頂點，
    進一步決定原始圖形各個頂角經由變換之後的座標。
"""

"""
#重映射-remap

mapy, mapx = np.mgrid[0:h * 3:3, 0:w * 2:2]
img2 = cv2.remap(img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
x, y = 12, 40 #用於驗證映射公式的座標點
assert np.all(img[mapy[y, x], mapx[y, x]] == img2[y, x])

#使用3D曲面和remap()對圖片進行變形
def make_surf_map(func, r, w, h, d0):
    #計算曲面函數func在[-r:r]範圍之上的值，並進行透視投影。
    #視點高度為曲面高度的d0倍+1
    y, x = np.ogrid[-r:r:h * 1j, -r:r:w * 1j]
    z = func(x, y) + 0 * (x + y)  
    d = d0 * np.ptp(z) + 1.0  
    map1 = x * (d - z) / d  
    map2 = y * (d - z) / d
    return (map1 / (2 * r) + 0.5) * w, (map2 / (2 * r) + 0.5) * h  

def make_func(expr_str):
    def f(x, y):
        return eval(expr_str, np.__dict__, locals())
    return f

def get_latex(expr_str):
    import sympy
    x, y = sympy.symbols("x, y")
    env = {"x": x, "y": y}
    expr = eval(expr_str, sympy.__dict__, env)
    return sympy.latex(expr)

settings = [
    ("sqrt(8 - x**2 - y**2)", 2, 1),
    ("sin(6*sqrt(x**2+y**2))", 10, 10),
    ("sin(sqrt(x**2+y**2))/sqrt(x**2+y**2)", 20, 0.5)
]
fig, axes = plt.subplots(1, len(settings), figsize=(12, 12.0 / len(settings)))

for ax, (expr, r, height) in zip(axes, settings):
    mapx, mapy = make_surf_map(make_func(expr), r, w, h, height)
    img2 = cv2.remap(
        img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
    ax.imshow(img2[:, :, ::-1])
    ax.axis("off")
    ax.set_title("${}$".format(get_latex(expr)))

fig.subplots_adjust(0, 0, 1, 1, 0.02, 0)

show()
"""
print("------------------------------------------------------------")  # 60個

print("opencv 101")

"""
    scpy2.opencv.remap_demo：示範remap()的拖曳效果。
    在圖形上按住滑鼠左鍵進行拖曳，每次拖曳完成之後，都將修改原始圖形，
    可以按滑鼠右鍵取消上次的拖曳動作。
"""

# 使用remap()實現圖形拖曳效果
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
gridy, gridx = np.mgrid[:h, :w]
tx, ty = 313, 316
sx, sy = 340, 332
r = 40.0
sigma = 20

mask = ((gridx - sx) ** 2 + (gridy - sy) ** 2) < r**2
offsetx = np.zeros((h, w))
offsety = np.zeros((h, w))
offsetx[mask] = tx - sx
offsety[mask] = ty - sy
offsetx_blur = cv2.GaussianBlur(offsetx, (0, 0), sigma)
offsety_blur = cv2.GaussianBlur(offsety, (0, 0), sigma)
img2 = cv2.remap(
    img,
    (offsetx_blur + gridx).astype("f4"),
    (offsety_blur + gridy).astype("f4"),
    cv2.INTER_LINEAR,
)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax.imshow(img2[:, :, ::-1])
circle = plt.Circle((tx, ty), r, fill=None, alpha=0.5, lw=2, ls="dashed")
ax.add_artist(circle)
circle = plt.Circle((sx, sy), r, fill=None, alpha=0.5, lw=2, color="black")
ax.add_artist(circle)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 103")
# 直方圖比對


def histogram_match(src, dst):
    res = np.zeros_like(dst)
    cdf_src = np.zeros((3, 256))
    cdf_dst = np.zeros((3, 256))
    cdf_res = np.zeros((3, 256))
    kw = dict(bins=256, range=(0, 256), density=True)  # normed 改成 density

    for ch in (0, 1, 2):
        hist_src, _ = np.histogram(src[:, :, ch], **kw)
        hist_dst, _ = np.histogram(dst[:, :, ch], **kw)
        cdf_src[ch] = np.cumsum(hist_src)
        cdf_dst[ch] = np.cumsum(hist_dst)
        index = np.searchsorted(cdf_src[ch], cdf_dst[ch], side="left")
        np.clip(index, 0, 255, out=index)
        res[:, :, ch] = index[dst[:, :, ch]]
        hist_res, _ = np.histogram(res[:, :, ch], **kw)
        cdf_res[ch] = np.cumsum(hist_res)

    return res, (cdf_src, cdf_dst, cdf_res)


src = cv2.imread("data/autumn.jpg")
dst = cv2.imread("data/summer.jpg")

res, cdfs = histogram_match(src, dst)

# %figonly=直方圖比對結果
fig = plt.figure(figsize=(10, 6))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax1 = plt.subplot2grid((5, 6), (0, 0), 3, 3)
ax2 = plt.subplot2grid((5, 6), (0, 3), 3, 3)
ax1.imshow(dst[:, :, ::-1])
ax2.imshow(res[:, :, ::-1])
ax1.axis("off")
ax2.axis("off")
axb = plt.subplot2grid((5, 6), (3, 0), 2, 2)
axg = plt.subplot2grid((5, 6), (3, 2), 2, 2)
axr = plt.subplot2grid((5, 6), (3, 4), 2, 2)

axg.set_yticklabels([])
axr.set_yticklabels([])

for ax, cdf in zip((axb, axg, axr), zip(*cdfs)):
    ax.plot(cdf[0], alpha=0.6, label="src", ls="--")
    ax.plot(cdf[1], alpha=0.6, label="dst", ls=":")
    ax.plot(cdf[2], alpha=0.6, label="res")
    ax.set_xlim(0, 256)
    ax.set_ylim(0, 1.1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 106")

# 圖形識別
# 用Hough變換檢驗直線和圓

# scpy2.opencv.hough_demo：霍夫變換示範程式，可透過界面調節函數的所有參數。

# 檢驗線段
# %figonly=用r和θ表示的直線

x = [-2, 5]
y = [5, -1]

from sympy import Point
from sympy import Line

line = Line(Point(x[0], y[0]), Point(x[1], y[1]))
seg = line.perpendicular_segment(Point(0, 0))

plt.plot([seg.p1.x, seg.p2.x], [seg.p1.y, seg.p2.y], "--o", color="gray")

from matplotlib.patches import Wedge

angle = np.rad2deg(np.arctan2(float(seg.p2.y), float(seg.p2.x)))
theta = Wedge((0, 0), 1, 0, angle, alpha=0.3)
# plt.add_patch(theta)
plt.text(1, 0.5, r"$\theta$", fontsize="large")
plt.text(0.8, 1.1, r"$r$", fontsize="large")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 107")

# %figonly=霍夫變換示意圖
k = 1.2
b = 3

xn, yn = 4, 3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
xs = np.linspace(0, 5, 4)
ys = xs * k + b

for x0, y0 in zip(xs, ys):
    ax1.plot(x0, y0, "o")

ax1.plot(xn, yn, ">")
ax1.margins(0.1, 0.1)

theta = np.linspace(0, np.pi, 100)
for x0, y0 in zip(xs, ys):
    r = x0 * np.cos(theta) + y0 * np.sin(theta)
    ax2.plot(theta, r)

r = xn * np.cos(theta) + yn * np.sin(theta)
ax2.plot(theta, r, "--")
ax2.set_xlim(0, np.max(theta))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 110")

"""
# 無 SURF() 函數
#SURF特征比對

#SURF()找到的關鍵點和每個關鍵點的局部圖形
img_gray1 = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)
surf = cv2.SURF(2000, 2)
key_points1 = surf.detect(img_gray1)
key_points1.sort(key=lambda kp:kp.size, reverse=True)

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
cv2.drawKeypoints(img_color1, key_points1[:25], img_color1, color=BLUE,
                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

from scpy2.utils.image import concat_keypoints

img_keypoints = concat_keypoints(img_gray1, key_points1[:25], 5, 5, scale=2)
#%array_image img_color1; img_keypoints

print("------------------------------")  # 30個

_, features1 = surf.compute(img_gray1, key_points1)
cc = features1.shape
print(cc)

#(145, 128)

img_gray2 = cv2.imread("dat/lena2.jpg", cv2.IMREAD_GRAYSCALE)
img_color2 = cv2.cvtColor(img_gray2, cv2.COLOR_GRAY2RGB)
surf2 = cv2.SURF(2000, 2)  
key_points2, features2 = surf2.detectAndCompute(img_gray2, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)   

fbm = cv2.FlannBasedMatcher(index_params, search_params)
match_list = fbm.knnMatch(features1, features2, k=1)

m = match_list[0][0]

#%C m.distance; m.queryIdx; m.trainIdx

#請讀者思考如何利用下面程式得到的matrix矩陣將變形之後的圖形復原成原始圖形。

key_positions1 = np.array([kp.pt for kp in key_points1])
key_positions2 = np.array([kp.pt for kp in key_points2])

index1 = np.array([m[0].queryIdx for m in match_list])
index2 = np.array([m[0].trainIdx for m in match_list])

distances = np.array([m[0].distance for m in match_list])

best_index = np.argsort(distances)[:50]
matched_positions1 = key_positions1[index1[best_index]]
matched_positions2 = key_positions2[index2[best_index]]

matrix, mask = cv2.findHomography(matched_positions1, matched_positions2, cv2.RANSAC)

#scpy2.opencv.surf_demo：SURF圖形比對示範程式。
#用滑鼠修改右側圖形的四個角的位置計算出透視變換之後的圖形，
#然後在原始圖形和變換之後的圖形之間搜尋比對點，並計算透視變換的矩陣。
"""

""" no module
#%figonly=顯示特征比對的關鍵點

from matplotlib.collections import LineCollection
from scpy2.utils.image import concat_images

COLORS = np.array([[0, 0.0, 0.5], [1, 0, 0]])

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
merged_img = concat_images([img_color1, img_color2], margin=0)

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")
plt.imshow(merged_img)
lines = np.concatenate([matched_positions1, matched_positions2], axis=1)
lines[:, 2] += img_color2.shape[1]
line_collection = LineCollection(lines.reshape(-1, 2, 2), 
                                 colors=COLORS[mask.ravel()], lw=1, alpha=0.5)
ax.add_collection(line_collection);

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 114")

# 型態轉換

points = np.random.rand(20, 2).astype(np.float32)
(x, y), (w, h), angle = cv2.minAreaRect(points)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 116")

# [Python]使用NumPy 進行影像黑白反轉

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 讀取影像（灰階模式）
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 黑白反轉
inverted_image = 255 - image

# 顯示原影像和反轉後的影像
cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 117")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
cv_img = cv2.imread(filename)
width = cv_img.shape[1]
height = cv_img.shape[0]
print(width)
print(height)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = Image.open(filename)

mask = np.zeros([10, 5, 3], dtype=np.uint8)
# print(mask)
occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)

# print(mask)

# mask[:, :, i] = mask[:, :, i] * occlusion
# occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 118")

"""
# 圖形處理
# 二維卷冊積
# 使用filter2D()製作的各種圖形處理效果

二维卷积

用不同的卷积核可以得到 各种不同的图像处理效果。
OpenCV提供了 filter2D()来完成图像的卷积运算，调用方式如下：
filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
    anchor参数指定卷积核的锚点位置，当它为默认值(-1，-1)时， 以卷积核的中心为锚点
使用filter2D()制作的各种图像处理效果
"""
filename = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
src = cv2.imread(filename)

kernels = [
    ("低通濾波器", np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) * 0.1),
    ("高通濾波器", np.array([[0.0, -1, 0], [-1, 5, -1], [0, -1, 0]])),
    ("邊緣檢驗", np.array([[-1.0, -1, -1], [-1, 8, -1], [-1, -1, -1]])),
]

fig, axes = plt.subplots(1, 3, figsize=(12, 5))
for ax, (name, kernel) in zip(axes, kernels):
    dst = cv2.filter2D(src, -1, kernel)
    # 由於matplotlib的彩色順序和OpenCV的順序相反
    ax.imshow(dst[:, :, ::-1])
    ax.set_title(name)
    ax.axis("off")
fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

show()

kernel1_name = "低通濾波器"
kernel1 = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) * 0.1
kernel2_name = "高通濾波器"
kernel2 = np.array([[0.0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel3_name = "邊緣檢驗"
kernel3 = np.array([[-1.0, -1, -1], [-1, 8, -1], [-1, -1, -1]])

dst1 = cv2.filter2D(src, -1, kernel1)
dst2 = cv2.filter2D(src, -1, kernel2)
dst3 = cv2.filter2D(src, -1, kernel3)

plt.figure(figsize=(12, 5))

plt.subplot(131)
plt.imshow(dst1[:, :, ::-1])
plt.title(kernel1_name)

plt.subplot(132)
plt.imshow(dst2[:, :, ::-1])
plt.title(kernel2_name)

plt.subplot(133)
plt.imshow(dst3[:, :, ::-1])
plt.title(kernel3_name)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 119")

"""
有些特殊的卷积核可以表示成一个列矢量和一个行矢量的乘积，
这时只需要将原始图像按 顺序与这两个矢量进行卷积，
所得到的最终结果和直接与卷积核进行卷积的结果相同。
对于较大的卷积核能大幅度地提高 计算速度。

OpenCV提供了 sepFilter2D()来进行这种分步卷积，调用参数如下：
sepFilter2D(src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]])
比较filter2D()和sepFilter2D() 的计算速度：
"""

img = np.random.rand(1000, 1000)

row = cv2.getGaussianKernel(7, -1)
col = cv2.getGaussianKernel(5, -1)

kernel = np.dot(col[:], row[:].T)

img2 = cv2.filter2D(img, -1, kernel)
img3 = cv2.sepFilter2D(img, -1, row, col)
print("error=", np.max(np.abs(img2[:] - img3[:])))

"""
OpenCV提供了一些高级函数数来直接完成与某种特定卷积核的 卷积计算。

形态学运算
dilate
()对图像进行膨胀处理，而erode
()则对图像进行腐蚀处理。

mpiphologyEx()使用膨胀和收缩实现一些更高级的形态学处理。
这 些函数都可以对多值图像进行操作，对于多通道图像，它们将对每个通道进行相同的运算。

dilate()和erode()的调用参数相同：
dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

膨胀运算可以用下面的公式描述：
将结构元素kernel的锚点与原始图像中的每个像素(x,y)对齐之后，计算所有结构元素值不为0 的像素的最大值，写入目标图像的(x,y)像素点。而腐蚀运算则是计算所有结构元素不为0的像 素的最小值。
morphologyEx()的参数如下：
morphologyEx(src, op, kernel[, dst[, anchoriterationsborderType[, borderValue]]]]])
op参数，用于指定运算的类型。
moiphologyEx()的高级运算包括：
• MORPH_OPEN:开运算，可以用来区分两个靠得很近的区域。算法为先腐蚀再膨胀: dst=dilate(erode(src))
• MORPH_CLOSE:闭运算，可以用来连接两个靠得很近的区域。算法为先膨胀再腐蚀： dst=erode(dilate(src))
• MORPH_GRADIENT:形态梯度，能够找出图像区域的边缘。算法为膨胀减去腐蚀： dst=dilate(src)- erode(src)
• MORPH_TOPHAT:顶帽运算，算法为原始图像减去开运算：dst = src-open(src)。
• MORPH_BLACKHAT:黑帽运算，算法为闭运算减去原始图像：dst=close(src)-src。

    填充-floodFill

填充函数floodFill()在图像处理中经常用于标识或分离图像中的某些特定部分。它的调用方 式为:
floodFill(image, mask, seedPoint, newVal[, loDiff[, upDiff[, flags]]])
seedPoint参数为填充的起始点，为种子点； newVal参数为填充所使用的颜色值；loDiff和upDiff参数是填充的下限和上限容差；flags参数 是填充的算法标志。
填充从seedPoint指定的种子坐标开始，图像中与当前的填充区域颜色相近的点将被添加进 填充区域，从而逐步扩大填充区域，直到没有新的点能添加进填充区域为止。
颜色相近的判断 方法有两种：
    默认使用相邻点为基点进行判断。
•如果开启了 flags中的FL00DFILL_F1XED_RANGE标志位，则以种子点为基点进行判断。
假设图像中某个点(x,y)的颜色为C(x,y), C0为基点颜色，则下面的条件满足时，（x,y)将 被添加进填充区域：
C0 — loDiff < C(x，y) < C0 + hiDiff
此外还可以通过flags指定相邻点的定义：四连通或八连通。
当mask参数不为None时，它是一个宽和高比image都大两个像素的单通道8位图像
。image 图像中的像素(x,y)与mask中的(x + 1,y + 1)对应。填充只针对mask中的值为0的像素进行。 进行填充之后，mask中所有被填充的像素将被赋值为1。如果只希望修改mask,而不对原始图 像进行填充，可以开启flags标志中FLOODFTLL_MASK_ONLY。
#floodFill()的填充效果
"""
# 形態學運算
#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。
# 填充-floodFill
# 示範floodFill()的填充效果
#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。
# 去瑕疵-inpaint
#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。

filename = "C:/_git/vcs/_4.python/opencv/data/coins.png"

img = cv2.imread(filename)
seed1 = 344, 188
seed2 = 152, 126
diff = (13, 13, 13)
h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(img, mask, seed1, BLACK, diff, diff, cv2.FLOODFILL_MASK_ONLY)
cv2.floodFill(img, None, seed2, RED, diff, diff)
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(~mask, cmap="gray")
axes[1].imshow(img)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Covex效果")


def convex(src_img, raw, effect):
    col, row, channel = raw[:]
    cx, cy, r = effect[:]
    output = np.zeros([row, col, channel], dtype=np.uint8)
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5
            if d <= r:
                nx = int((x - cx) * d / r + cx)
                ny = int((y - cy) * d / r + cy)
                output[y, x, :] = src_img[ny, nx, :]
            else:
                output[y, x, :] = src_img[y, x, :]
    return output


image = cv2.imread(filename1)  # 彩色讀取

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")

w, h = 305, 400
cw, ch = int(w / 2), int(h / 2)  # 取得中心點
image2 = convex(image, (w, h, 3), (cw, ch, 100))

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Covex效果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 01loadimg.py

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

img = cv2.imread(filename, 0)  # 0 黑白图片；1 原色图片

cv2.imshow(win_name, img)  # 显示图片

cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁创建的对象

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" no file
# 02opencvmatplotlib.py

# 读取图片
img = cv2.imread("tmp_picture1.mono.pgm", 0)  # 黑白图片

plt.imshow(img, cmap="gray", interpolation="bicubic")

plt.xticks([]), plt.yticks([])  # 隐藏 X Y 坐标
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03drawrectangle.py

# Create a black image
img = np.zeros((512, 512, 3))

# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色: BLUE，宽度:2
cv2.line(img, (0, 0), (511, 511), BLUE, 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04drawGeometry.py

img = np.zeros((512, 512, 3))
cv2.rectangle(img, (384, 0), (510, 128), GREEN, 3)  # 矩形
cv2.circle(img, (447, 63), 63, RED, -1)  # 圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)  # 椭圆

# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, YELLOW, 1)

# 写入文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, WHITE, 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05drawcirlcle.py

img = np.zeros((512, 512, 3))

# 绘制圆：圆心(255, 255), 半径60, 颜色 YELLOW, 像素1
cv2.circle(img, (255, 150), 60, YELLOW, 2)  # 圆

# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100
# 360表示整个椭圆；颜色 CYAN；像素2；
cv2.ellipse(img, (255, 350), (100, 50), 0, 0, 360, CYAN, 2)  # 椭圆

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt_tree.xml"
picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
)

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("製作影像")

width, height = 640, 480  # 影像寬, 影像高

# 建立 640 X 480 之黑圖
fig = np.zeros((height, width), dtype=np.uint8)

# 建立 640 X 480 之白圖
fig = np.ones((height, width), dtype=np.uint8) * 255

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

print("某些塗為白色")

for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)

# R
red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值

# G
green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值

# B
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值

# Y
yellow_image = image.copy()
yellow_image[:, :, 2] = 255  # 建立 R 通道像素值
yellow_image[:, :, 1] = 255  # 建立 G 通道像素值

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("製作隨機影像")

# 使用random.randint()建立GRAY影像陣列
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)  # 灰階, 1維
# src = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)  # 彩色, 3維

cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

src = np.random.randint(256, size=(height, width))  # 建立矩陣
# print(f"矩陣內容 = \n{src}")

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# 製作隨機影像
width, height = 64, 48  # 影像寬, 影像高
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個
# OpenCV_05_建立空影像
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.ones((height, width), np.uint8) * 255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩

cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("-------------------- ----------------------------------------")  # 60個
# OpenCV 運算
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

channels = cv2.mean(src)  # 計算影像各通道的均值
print(f"均值   = \n{channels}")

mean, std = cv2.meanStdDev(src)  # 計算影像各通道的標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("Peony")  # 關閉視窗

print("------------------------------------------------------------")  # 60個
"""
# 設定 cv 視窗
cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小

img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
# img2 = cv2.imread(filename1, 0)  # 灰色讀取 same

cv2.imshow("Peony1", img1)
cv2.imshow("Peony2", img2)

cv2.waitKey()
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取某點的灰階/RGB值

pt_y = 169
pt_x = 118

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點

print(type(px))
print(f"BGR = {px}")

img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個

# 修改影像的RGB值

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_06_影像處理
print("------------------------------------------------------------")  # 60個

print("修改圖片的像素值 灰階")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = 127

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階")
plt.axis("off")

print("修改圖片的像素值 彩色")

img = cv2.imread(filename1)  # 彩色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = [255, 0, 0]

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("彩色")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立紅色red底的彩色影像陣列
red_image = np.zeros((height, width, 3), np.uint8)
red_image[:, :, 2] = 255  # 填滿紅色

# 建立綠色green底的彩色影像陣列
green_image = np.zeros((height, width, 3), np.uint8)
green_image[:, :, 1] = 255  # 填滿綠色

# 建立藍色blue底的彩色影像陣列
blue_image = np.zeros((height, width, 3), np.uint8)
blue_image[:, :, 0] = 255  # 填滿藍色

# 建立黃色yellow底的彩色影像陣列
yellow_image = np.zeros((height, width, 3), np.uint8)
yellow_image[:, :, 2] = 255  # 填滿紅色
yellow_image[:, :, 1] = 255  # 填滿綠色

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

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

# 取出像素值, 修改之

img = cv2.imread(filename1)  # 彩色讀取

print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")

# 紫色長條
img[115:125, 110:210] = [255, 0, 255]

# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代

# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代

cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("修改alpha通道值 255=>127")

# 4通道的PNG圖
filename5 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"

img = cv2.imread(filename5, cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(img.shape)
print(f"修改前img[210,150] = {img[210,150]}")
print(f"修改前img[250,199] = {img[250,199]}")

for z in range(0, img.shape[1]):  # 一次一個修改alpha通道值
    for y in range(0, img.shape[0]):
        img[z, y, 3] = 127  # 修改alpha通道值

img[0:200, 0:200, 3] = 127  # 修改alpha通道值

print(f"修改後img[210,150] = {img[210,150]}")
print(f"修改後img[250,199] = {img[250,199]}")

cv2.imshow("After", img)  # 顯示修改前影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")

image.itemset((1, 3), 255)  # 修訂內容為 255

print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個

print("灰階讀取, 部分塗成灰色")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img

for y in range(30, 100):  # 修改影像
    for x in range(180, 280):
        img.itemset((y, x), 127)
cv2.imshow("After", img)  # 顯示修改後影像img

cv2.waitKey()
cv2.destroyAllWindows()

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

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {img.item(115,110,1)}")
print(f"修改前img[125,110,1] = {img.item(125,110,1)}")
print(f"修改前img[135,110,1] = {img.item(135,110,1)}")

# 白色長條
for z in range(30, 100):  # 修改影像:一次一個通道值
    for y in range(180, 280):
        for x in range(0, 3):  # 一次一個通道值
            img.itemset((z, y, x), 127)  # 白色取代
cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110,1] = {img.item(115,110,1)}")
print(f"修改後img[125,110,1] = {img.item(125,110,1)}")
print(f"修改後img[135,110,1] = {img.item(135,110,1)}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)

# ROI大小區塊建立馬賽克
w, h = 100, 70
face = np.random.randint(0, 256, size=(h, w, 3))  # 馬賽克效果
img[30 : 30 + h, 180 : 180 + w] = face  # ROI, 先高後寬
cv2.imshow("Face", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

big = cv2.imread(filename2)  # 彩色讀取, 大圖

small = cv2.imread(filename1)  # 彩色讀取, 小圖

roi = small[110:200, 130:220]  # ROI, 先高後寬

big[110:200, 70:160] = roi  # 小圖貼到大圖上

cv2.imshow("Image", big)

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)

plt.subplot(331)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(result[:, :, i], cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
    plt.title(str(i))
    plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# cv2.bitwise_and

src = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)
row, column = src.shape  # 取得列高和欄寬

h100 = np.ones((row, column), dtype=np.uint8) * 100  # 建立像素值是100的影像

new_src = cv2.bitwise_and(src, h100)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(h100, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階100")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(new_src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖取出灰階100")
plt.axis("off")

plt.suptitle("cv2.bitwise_and")
show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
opencv 集合 新進3

"""

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

maxval = 255  # 定義像素最大值, 閾值
width, height = 640, 480  # 影像寬, 影像高

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# Character_recognition.py

img = cv2.imread("data/brain.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

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

cv2.imshow("p", sure_fg)

plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(221)
plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(223)
plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(224)
plt.imshow(cv2.cvtColor(sure_fg, cv2.COLOR_BGR2RGB))
plt.title("")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

"""
print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 ST
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)  # 讀取影像

mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (150, 50, 200, 480)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1

# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)

# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

dst = cv2.rectangle(dst, rect, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/tmp1/hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)

""" NG
maskpict = cv2.imread("data/tmp1/hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("data/tmp1/hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/tmp1/lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 全景圖 ST
print("------------------------------------------------------------")  # 60個

"""
filename1 = 'C:/_git/vcs/_4.python/_data/penguin3.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/penguin4.jpg'
output_filename = 'tmp_penguin_all.jpg'
filenames = [filename1, filename2]
"""

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF2.jpg"
filename3 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF3.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF4.jpg"
filename5 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF5.jpg"
filename6 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF6.jpg"
filename7 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF7.jpg"
filename8 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF8.jpg"
output_filename = "tmp_SF_all.jpg"
filenames = [
    filename1,
    filename2,
    filename3,
    filename4,
    filename5,
    filename6,
    filename7,
    filename8,
]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)

stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", pano)
    cv2.imwrite(output_filename, pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")
else:
    print("error: {}".format(status))

print("------------------------------------------------------------")  # 60個
# 全景圖 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.selectROI ST
print("------------------------------------------------------------")  # 60個

print("OpenCV selectROI 之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

roi = cv2.selectROI("image", image)
print("選取區域 :", roi)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.selectROI SP
print("------------------------------------------------------------")  # 60個

"""
print("------------------------------------------------------------")  # 60個
# Two Frames ST
print("------------------------------------------------------------")  # 60個

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# cap = cv2.VideoCapture(video_filename)  # 開啟影片
cap = cv2.VideoCapture("video.avi")  # 開啟影片

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
length = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

print("W :", W)
print("H :", H)
print("frames :", frames)
print("fps :", fps)
print("length :", length)

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

frameNum = 0

while True:
    # 获取一帧
    ret, frame = cap.read()  # 從影片擷取一張影像
    frameNum += 1
    if ret == True:
        frame = cv2.resize(frame, (W // 3, H // 3))
        tempframe = frame
        if frameNum == 1:  # 第1張圖
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)

        if frameNum >= 2:  # 第2張圖以後
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            currentframe = cv2.absdiff(currentframe, previousframe)
            median = cv2.medianBlur(currentframe, 3)
            ret, threshold_frame = cv2.threshold(
                currentframe, 20, 255, cv2.THRESH_BINARY
            )
            gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)  # 執行高斯模糊化

            cv2.imshow("Original", frame)
            cv2.imshow("Frame", currentframe)
            cv2.imshow("medianBlur", median)

            # 按键盘上的Q键退出
            if cv2.waitKey(33) & 0xFF == ord("q"):
                break
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
    else:
        print("播放結束")
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# Two Frames SP
print("------------------------------------------------------------")  # 60個
"""

"""
#GaussianBlur
#Canny
"""


def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階處理
    blur = cv2.GaussianBlur(gray, (13, 13), 0)  # 高斯模糊
    canny = cv2.Canny(blur, 50, 150)  # 邊緣偵測
    return canny


def get_roi(img):
    mask = np.zeros_like(img)  # 全黑遮罩
    points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊形座標
    cv2.fillPoly(mask, points, 255)  # 多邊三角形
    roi = cv2.bitwise_and(img, mask)
    return roi


def draw_lines(img, lines):  # 建立自訂函式
    for line in lines:
        points = line.reshape(
            4,
        )  # 降成一維 shape = (4,)
        x1, y1, x2, y2 = points  # 取出直線座標
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)  # 繪製直線
    return img  # 回傳繪製直線後的影像


def get_avglines(lines):
    if lines is None:  # 如果有找到線段
        print("偵測不到直線線段")
        return None
    # -----↓先依斜率分到左組或右組↓
    lefts = []
    rights = []
    for line in lines:
        points = line.reshape(
            4,
        )
        x1, y1, x2, y2 = points
        slope, b = np.polyfit((x1, x2), (y1, y2), 1)  # y = slope*x + b
        # print(f'y = {slope} x + {b}')  #若有需要可將斜率與截距印出
        if slope > 0:  # 斜率 > 0, 右邊的直線函數
            rights.append([slope, b])  # 以 list 存入
        else:  # 斜率 < 0, 左邊的直線函數
            lefts.append([slope, b])  # 以 list 存入

    # -----↓再計算左組與右組的平圴線↓
    if rights and lefts:  # 必須同時有左右兩邊的直線函數
        right_avg = np.average(rights, axis=0)  # 取得右邊的平均直線
        left_avg = np.average(lefts, axis=0)  # 取得左邊的平均直線
        return np.array([right_avg, left_avg])
    else:
        print("無法同時偵測到左右邊緣")
        return None


def get_sublines(img, avglines):
    sublines = []  # 用於儲存線段座標
    for line in avglines:  # 一一取出所有直線函數
        slope, b = line  # y = slope*x + b
        y1 = img.shape[0]  # 影像高度 (即影像的最底部位
        y2 = int(y1 * (3 / 5))  # 取影像高度的 3/5 位置為線段
        x1 = int((y1 - b) / slope)  # x = (y-b/m), 取得線段 x 座標
        x2 = int((y2 - b) / slope)
        sublines.append([x1, y1, x2, y2])  # 座標存入串列中
    return np.array(sublines)  # 將串列轉為陣列回傳


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/tmp1/road.jpg"

print("------------------------------------------------------------")  # 60個

# 彩色讀取
img = cv2.imread(filename)  # 讀取圖片

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (3, 3), 0)

plt.figure(figsize=(12, 8))
plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(312)
plt.title("灰階")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(313)
plt.title("高斯模糊")
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

cv2.imshow("Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("顯示邊緣圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

mask = np.zeros_like(edge)  # 全黑遮罩
points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊座標
cv2.fillPoly(mask, points, 255)  # 繪製三角形
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("顯示mask圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("顯示ROI圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
print(lines)
if lines is not None:  # 如果有找到線段
    img = draw_lines(img, lines)  # 在原圖繪製線段
else:
    print("偵測不到直線線段")
cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("顯示直線線段圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
if avglines is not None:
    lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
    img = draw_lines(img, lines)  # 畫出線段
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("顯示直線圖")
    show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

video_filename = (
    "C:/_git/__大檔與暫存區/GRENZEL 雲創 E3W WiFi 行車記錄器 1080 30fps 日間測試 高速公路 - Mobile01.mp4"
)
video_filename = "C:/_git/__大檔與暫存區/DOD行車記錄器-LS300W 日間高速公路實拍.mp4"
video_filename = "C:/_git/__大檔與暫存區/響尾蛇行車記錄器高解析度1080P - 高速公路白天行駛記錄 -.mp4"
video_filename = "road.mp4"

capture = cv2.VideoCapture(video_filename)  # 建立 VideoCapture 物件
if capture.isOpened():
    while True:
        sucess, img = capture.read()  # 讀取影像
        if sucess:
            edge = get_edge(img)  # 邊緣偵測
            roi = get_roi(edge)  # 取得 ROI
            lines = cv2.HoughLinesP(
                image=roi,  # Hough 轉換
                rho=3,
                theta=np.pi / 180,
                threshold=30,
                minLineLength=50,
                maxLineGap=40,
            )
            avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
            if avglines is not None:
                lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
                img = draw_lines(img, lines)  # 畫出線段
            cv2.imshow("Frame", img)  # 顯示影像
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ord("q") or k == ord("Q"):  # 按下 Q(q) 結束迴圈
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break
else:
    print("開啟攝影機失敗")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.inpaint 影像修復 ST
print("------------------------------------------------------------")  # 60個

# 修復影像 inpaint

fail_filename = "C:/_git/vcs/_4.python/opencv/data/elephant_fail.jpg"

lisa = cv2.imread("data/mona_fail1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lisa = cv2.imread("data/mona_fail2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# cv2.inpaint 影像修復 SP
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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# 新進 與 測試

"""
    image = image[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形
"""

print("------------------------------------------------------------")  # 60個

cvshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 存圖以比較之
# cv2.imwrite('building.png', image)
# cv2.imwrite('building_clahe.png', cl1)
# cv2.imwrite('tmp_image.png', image1)
# cv2.imwrite('tmp_image.png', mona)


# dddddddddddddddddddddddddddddddddddddddddddd


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cvshow("image", image)

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cvshow("image", image)


# sobel 邊緣檢測
def sobel(image, winSize):
    rows, cols = image.shape


"""
去瑕疵-inpaint

inpaint

()可以从图像上去除指定区域中的物体，可以用于去除图像上的水印、划痕、 污渍等瑕疵。
它的调用参数如下：
inpaint(src, inpaintMask, inpaintRadius, flags[, dst])
inpainlMask参数是大小和src相同的单通道8位图像，其中不 为0的像素表示需要去除的区域。
inpaintRange参数是处理半径， 半径越大处理时间越长，结果越平滑。
flags参数选择inpaint的算法，目前有两个候选算法： INPAINT_NS 和 INPIANT_TELEA。
用鼠标绘制需要去瑕疵的区域:
"""


def putText(x, y, text, color=(0, 0, 0)):
    global image
    # font_filename = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(font_filename, 20)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)


cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 5)  # 繪製外框
putText(box[0], box[3], text, color=(0, 0, 255))  # 放入文字


# 畫圓
cv2.circle(I, (int(circles[i][2]), int(circles[i][1])), int(circles[i][0]), (255), 2)


# cv2.imwrite("_tmp_face1.jpg", img)  # 存圖


# 存成pgm檔
cv2.imwrite("tmp_picture1.mono.pgm", img)

# cv2.imwrite("_tmp_face2.jpg", img)  # 存圖


# 取出圖片的一塊
face = img[70:220, 90:240]  # ROI, 先高後寬
cv2.imshow("Face", face)

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
src = cv2.imread(filename2)

cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()

ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
cv2.imwrite("a32.png", a32_image)  # 儲存alpha=32影像

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img = cv2.imread(filename1)  # 彩色讀取

# 影像的屬性

print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

"""
陣列垂直合併 vstack()
陣列水平合併 hstack()
"""

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Peony", img)

# ------------------------------------------------------------

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

# ------------------------------------------------------------

"""
仿射轉換（Affine transformation），又稱仿射映射，是指在幾何中，對一個向量空間進行一次線性轉換並接上一個平移，轉換為另一個向量空間。

"""
# ------------------------------------------------------------

result = cv2.calcHist([img_hsv], [0, 1], None, [40, 40], [0, 256, 0, 256])
print(result)
result /= np.max(result) / 255
print(result)
print(result.shape)

# ------------------------------------------------------------

# cv2 之讀檔 存檔 (轉換檔案格式) 直接改副檔名即可
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("aaaa.png", img)

# ------------------------------------------------------------


# ------------------------------------------------------------


# ------------------------------------------------------------


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

meanBlurImage = np.round(meanBlurImage)

image_0_1 = image/255.0


# 將灰度值歸一化
image = image / 255.0


# 將圖像歸一化
image_0_1 = image / 255.0
# 將圖像歸一化
image_0_1 = I / 255.0
p = p / 255.0
# 顯示原圖
cvshow("image", image)

# 導向濾波
result = guidedFilter(image_0_1, image_0_1, (17, 17), pow(0.2, 2.0))
cvshow("guidedFilter", result)

# 保存導向濾波的結果
result = result * 255
result[result > 255] = 255
result = np.round(result)
result = result.astype(np.uint8)

# 二值化邊緣，對 imageDoG 閾值處理
edge = np.copy(imageDoG)
edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = edge.astype(np.uint8)


# 保存導向濾波的結果
result = result * 255
result[result > 255] = 255
result = np.round(result)
result = result.astype(np.uint8)



    # 縮小圖像
    small_I = cv2.resize(
        I,
        dsize=(int(round(s * cols)), int(round(s * rows))),
        interpolation=cv2.INTER_CUBIC,
    )
    small_p = cv2.resize(
        p,
        dsize=(int(round(s * cols)), int(round(s * rows))),
        interpolation=cv2.INTER_CUBIC,
    )


    # 放大 small_a 和 small_b
    mean_a = cv2.resize(
        mean_small_a, dsize=(cols, rows), interpolation=cv2.INTER_LINEAR
    )
    mean_b = cv2.resize(
        mean_small_b, dsize=(cols, rows), interpolation=cv2.INTER_LINEAR
    )


result = 255 - result

#cv2.imwrite('test.jpg',img) 偽寫入

read
    img = cv2.imread('car.jpg')             # 讀取圖片

resize
    img_small = cv2.resize(img, (300, 100))  # 改變尺寸

save
        cv2.imwrite('small.jpg', img_small)  # 儲存影像


OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：


數值 1
cv2.IMREAD_COLOR
    此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。

數值 0
cv2.IMREAD_GRAYSCALE
    以灰階的格式來讀取圖片。
數值 -1
cv2.IMREAD_UNCHANGED
    讀取圖片中所有的 channels，包含透明度的 channel。 
    
------------------------------------------------------------

# cv2.namedWindow("Video Player", 0) # 設定視窗名稱
# cv2.resizeWindow("Video Player", 300, 200) # 重設定視窗大小

# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# h_frame = cv2.flip(frame, 1)  # 水平翻轉

------------------------------------------------------------

image = cv2.flip(image,1) #左右反轉
image = cv2.resize(image,(640//2,480//2))

------------------------------------------------------------


image = cv2.imread(filename)  # 預設為彩色 1號
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階 2號
image = cv2.imread(filename, 2)  # 也可使用數字代表模式

print(image.shape)  # 得到 shape
print(image.dtype)  # uint8

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)

print(image1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(image2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式

print(image.shape)                             # (400, 300, 4)  第三個數值變成 4



    # 轉換為 8 位圖，保存結果
    imageAbstraction = 255 * imageAbstraction
    imageAbstraction = np.round(imageAbstraction)
    imageAbstraction = imageAbstraction.astype(np.uint8)

"""
