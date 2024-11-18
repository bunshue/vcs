"""

cv2之工具

cv2.setMouseCallback


"""
import sys
import cv2
import numpy as np

W = 640
H = 480

ESC = 27
SPACE = 32

print("------------------------------------------------------------")  # 60個
"""
print("Trackbar之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

cv2.imshow("ImageShow", image)

def apply_function(val):
    print('數值 :', val, end = " ")


# cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式
# 加入滑桿 0 ~ 200, 預設 100
cv2.createTrackbar("TrackbarName", "ImageShow", 0, 200, apply_function)
cv2.setTrackbarPos("TrackbarName", "ImageShow", 100)

#取得Trackbar數值
value = cv2.getTrackbarPos("TrackbarName", "ImageShow")

apply_function(value) #套用一次設定值

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

def setup_bg_color(x):
  r = cv2.getTrackbarPos('R','image')
  g = cv2.getTrackbarPos('G','image')
  b = cv2.getTrackbarPos('B','image')
  s = cv2.getTrackbarPos(switch,'image')

  if s == 0:
   img[:] = 0
  else:
   img[:] = [b,g,r]
  cv2.imshow('image',img)

# Create a black image, a window
img = np.zeros((240,180,3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,setup_bg_color)
cv2.createTrackbar('G','image',0,255,setup_bg_color)
cv2.createTrackbar('B','image',0,255,setup_bg_color)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,setup_bg_color)
cv2.setTrackbarPos(switch, "image", 1)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
print("------------------------------------------------------------")  # 60個

THRESHOLD = 127
print("二值化範例, 只能處理灰階圖")
print("二值化圖, 閥值 = " + str(THRESHOLD) + ", 小於變全黑, 大於變全白")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("opencv", image)


def get_trackbar_value(val):
    print(val, end=" ")
    #        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
    t, rst = cv2.threshold(image, val, 255, cv2.THRESH_BINARY)
    # t, rst = cv2.threshold(image, val, 255, cv2.THRESH_BINARY_INV)
    # t, rst = cv2.threshold(image, val, 255, cv2.THRESH_TRUNC)
    # t, rst = cv2.threshold(image, val, 255, cv2.THRESH_TOZERO_INV)
    # t, rst = cv2.threshold(image, val, 255, cv2.THRESH_TOZERO)
    cv2.imshow("opencv", rst)


cv2.createTrackbar("Trackbar", "opencv", 0, 255, get_trackbar_value)
cv2.setTrackbarPos("Trackbar", "opencv", THRESHOLD)  # 預設

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV之控件 Trackbar")
print("滑桿 ( Trackbar ) 又稱作滑動條、Slider bar，是一種可以用滑鼠調整數值的 UI 介面")

print("測試cv2視窗的Trackbar")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# image = cv2.imread(filename)

# 調整對比度後，圖像的效果顯示窗口
cv2.namedWindow("TrackbarTest", cv2.WND_PROP_AUTOSIZE)

cv2.imshow("TrackbarTest", image)

MAX_VALUE = 80
MIN_VALUE = 30  # 無效，看起來最小值一定要0
initial_value = 40


def callback_trackbar_test(_value):
    print(_value, end=" ")


callback_trackbar_test(initial_value)  # 做一次

cv2.createTrackbar(
    "value", "TrackbarTest", MIN_VALUE, MAX_VALUE, callback_trackbar_test
)  # callback function
cv2.setTrackbarPos("value", "TrackbarTest", initial_value)  # 預設

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("Trackbar之使用")

# HSL即色相、飽和度、亮度（英語：Hue, Saturation, Lightness）

filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# 顯示原圖
cv2.imshow("image", image)

# 圖像歸一化，且轉換為浮點型
fImg = image.astype(np.float32)
fImg = fImg / 255.0

# 顏色空間轉換
hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
lightness = 100
saturation = 100
MAX_VALUE = 100

cv2.namedWindow("RGB_HLS", cv2.WINDOW_AUTOSIZE)


def nothing(*arg):
    pass


cv2.createTrackbar("Lightness", "RGB_HLS", lightness, MAX_VALUE, nothing)
cv2.createTrackbar("Saturation", "RGB_HLS", saturation, MAX_VALUE, nothing)

# 調整飽和度和亮度後的效果
lsImg = np.zeros(image.shape, np.float32)

# 調整飽和度和亮度
while True:
    hlsCopy = np.copy(hlsImg)  # 複製原始影像
    # 得到 亮度 和 飽和度 的值
    lightness = cv2.getTrackbarPos("Lightness", "RGB_HLS")
    saturation = cv2.getTrackbarPos("Saturation", "RGB_HLS")
    # print(lightness, saturation)

    # 調整亮度和飽和度（線性變換）
    hlsCopy[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1

    hlsCopy[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1

    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)

    # 顯示調整後的效果
    cv2.imshow("RGB_HLS", lsImg)

    # 保存結果
    lsImg = lsImg * 255
    lsImg = lsImg.astype(np.uint8)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)
cv2.imshow("ImageProcessing", image)

contrast = 0  # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow("ImageProcessing", image)


# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c / 100 + 1) - c + b  # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.imshow("ImageProcessing", output)


# 定義調整亮度函式
def brightness_fn(val):
    # print('取得 亮度 :', val)
    global image, contrast, brightness
    brightness = val - 100
    adjust(image, contrast, brightness)


# 定義調整對比度函式
def contrast_fn(val):
    # print('取得 對比度 :', val)
    global image, contrast, brightness
    contrast = val - 100
    adjust(image, contrast, brightness)


# 加入亮度調整滑桿 0 ~ 200, 預設 100
cv2.createTrackbar("brightness", "ImageProcessing", 0, 200, brightness_fn)
cv2.setTrackbarPos("brightness", "ImageProcessing", 100)

# 加入對比度調整滑桿 0 ~ 200, 預設 100
cv2.createTrackbar("contrast", "ImageProcessing", 0, 200, contrast_fn)
cv2.setTrackbarPos("contrast", "ImageProcessing", 100)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("對比度增強1")

# 檔案 => cv2影像
image = cv2.imread(filename)

MAX_VALUE = 120
value = 120

# 調整對比度後，圖像的效果顯示窗口
cv2.namedWindow("contrast", cv2.WND_PROP_AUTOSIZE)


# 調整系數，觀察圖像的變化
def callback_contrast(_value):
    # 通過線性運算，調整圖像對比度
    a = float(_value) / 40.0
    contrastImage = a * image
    contrastImage[contrastImage > 255] = 255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)
    cv2.imshow("contrast", contrastImage)


callback_contrast(value)  # 套用一次設定值

cv2.createTrackbar("value", "contrast", value, MAX_VALUE, callback_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強4 gamma")

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename)

MAX_VALUE = 200
value = 40
segValue = float(value)
# 伽馬調整需要先將圖像歸一化
image_0_1 = image / 255.0
# 伽馬調整後的圖像顯示窗口
cv2.namedWindow("gamma_contrast", cv2.WND_PROP_AUTOSIZE)


# 調整 gamma 值，觀察圖像的變換
def callback_contrast(_value):
    gamma = float(_value) / segValue
    contrastImage = np.power(image_0_1, gamma)
    cv2.imshow("gamma_contrast", contrastImage)
    # 保存伽馬調整的結果
    contrastImage *= 255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)


callback_contrast(value)  # 套用一次設定值

cv2.createTrackbar("value", "gamma_contrast", value, MAX_VALUE, callback_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 meanBlur")

from scipy import signal


# 均值平滑
def meanBlur(image, H, W, _boundary="fill", _fillvalue=0):
    # H、W均不為零
    if H == 0 or W == 0:
        print("W or H is not zero")
        return image

    # -------沒有對均值平滑算子進行分離
    # meanKernel = 1.0/(H*W)*np.ones([H,W],np.float32)
    # result = signal.convolve2d(image,meanKernel,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    # -----卷積後進行數據類型轉換,得到均值平滑的結果
    # result = result.astype(np.uint8)
    # return result

    # 因為均值算子是可分離的卷積核，根據卷積運算的結合律
    # 可以先進行水平方向的卷積，
    # 再進行垂直方向的卷積
    # 首先水平方向的均值平滑
    meanKernel_x = 1.0 / W * np.ones([1, W], np.float32)
    i_conv_mk_x = signal.convolve2d(
        image, meanKernel_x, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    # 然後對得到的水平卷積的結果再進行垂直方向的卷積
    meanKernel_y = 1.0 / H * np.ones([H, 1], np.float32)
    i_conv_xy = signal.convolve2d(
        i_conv_mk_x, meanKernel_y, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    i_conv_xy = np.round(i_conv_xy)
    # 卷積後的結果進行數據類型轉換，得到均值平滑的結果
    result = i_conv_xy.astype(np.uint8)
    return result


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 均值濾波卷積核的寬高均設為 2*halfWinSize+1
halfWinSize = 1
MAX_HALFWINSIZE = 20
cv2.namedWindow("meanBlur", 1)


# 回調函數，均值濾波
def callback_meanBlur(_halfWinSize):
    result = meanBlur(
        image,
        2 * _halfWinSize + 1,
        2 * _halfWinSize + 1,
        _boundary="symm",
        _fillvalue=0,
    )
    cv2.imshow("meanBlur", result)


callback_meanBlur(halfWinSize)
cv2.createTrackbar(
    "winSize/2", "meanBlur", halfWinSize, MAX_HALFWINSIZE, callback_meanBlur
)

latexImage = meanBlur(image, 29, 29, "symm")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 scharr")

from scipy import signal


def scharr(I, _boundary="symm"):
    # I 與 scharr_x 的 same 卷積
    scharr_x = np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]], np.float32)
    I_x = signal.convolve2d(I, scharr_x, mode="same", boundary="symm")
    # I 與 scharr_y 的same 卷積
    scharr_y = np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]], np.float32)
    I_y = signal.convolve2d(I, scharr_y, mode="same", boundary="symm")
    return (I_x, I_y)


filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 求卷積
# i_conv_sch_x = scharr(image,1,0,_boundary='symm') 改掉
# i_conv_sch_y = scharr(image,0,1,_boundary='symm') 改掉
i_conv_sch_x, i_conv_sch_y = scharr(image)

# 取絕對值,分別得到水平方向和垂直方向的邊緣強度
abs_i_conv_sch_x = np.abs(i_conv_sch_x)
abs_i_conv_sch_y = np.abs(i_conv_sch_y)

# 水平方向和垂直方向的邊緣強度的灰度級顯示
edge_x = abs_i_conv_sch_x.copy()
edge_y = abs_i_conv_sch_y.copy()
edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x", edge_x)
cv2.imshow("edge_y", edge_y)

# 根據水平方向和垂直方向的邊緣強度,求最終的邊緣強度
# 有多種方式，這里使用平方根形式
edge = np.sqrt(np.power(abs_i_conv_sch_x, 2) + np.power(abs_i_conv_sch_y, 2))
# 最終的邊緣強度的灰度級顯示
edge[edge > 255] = 255
edge = np.round(edge)
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
# 經過閾值處理的邊緣顯示
cv2.namedWindow("thresh_edge", 1)
MAX_THRESH = 255
thresh = 255


# 回調函數，閾值處理
def callback_thresh(_thresh):
    threshEdge = edge.copy()
    threshEdge[threshEdge < _thresh] = 0
    threshEdge[threshEdge >= _thresh] = 255
    cv2.imshow("thresh_edge", threshEdge)


callback_thresh(thresh)
cv2.createTrackbar("thresh", "thresh_edge", thresh, MAX_THRESH, callback_thresh)

# 模擬鉛筆素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch < 100] = 100
cv2.imshow("pencilSketch", pencilSketch)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Kirsch")

"""
Krisch邊緣檢測算法:
krisch(image,_boundary='fill',_fillvalue=0)
其中:邊緣處理的方式_boundary包括：'symm','wrap','fill',
且當__boundary='fill'時,填充值默認為零_fillvalue=0
"""

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

from scipy import signal


def krisch(image, _boundary="fill", _fillvalue=0):
    # 第一步:8個krisch邊緣卷積算子分別和圖像矩陣進行卷積,然後分別取絕對值得到邊緣強度
    # 存儲8個方向的邊緣強度
    list_edge = []
    # 圖像矩陣和k1進行卷積,然後取絕對值（即:得到邊緣強度）
    k1 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
    image_k1 = signal.convolve2d(
        image, k1, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k1))
    # 圖像矩陣和k2進行卷積,然後取絕對值（即:得到邊緣強度）
    k2 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
    image_k2 = signal.convolve2d(
        image, k2, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k2))
    # 圖像矩陣和k3進行卷積,然後取絕對值（即:得到邊緣強度）
    k3 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
    image_k3 = signal.convolve2d(
        image, k3, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k3))
    # 圖像矩陣和k4進行卷積,然後取絕對值（即:得到邊緣強度）
    k4 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
    image_k4 = signal.convolve2d(
        image, k4, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k4))
    # 圖像矩陣和k5進行卷積,然後取絕對值（即:得到邊緣強度）
    k5 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
    image_k5 = signal.convolve2d(
        image, k5, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k5))
    # 圖像矩陣和k6進行卷積,然後取絕對值（即:得到邊緣強度）
    k6 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
    image_k6 = signal.convolve2d(
        image, k6, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k6))
    # 圖像矩陣和k7進行卷積,然後取絕對值（即:得到邊緣強度）
    k7 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
    image_k7 = signal.convolve2d(
        image, k7, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k7))
    # 圖像矩陣和k8進行卷積,然後取絕對值（即:得到邊緣強度）
    k8 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
    image_k8 = signal.convolve2d(
        image, k8, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k8))
    # 第二步：對上述8個方向的邊緣強度,對應位置取最大值，作為圖像最後的邊緣強度
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge * (edge >= list_edge[i]) + list_edge[i] * (edge < list_edge[i])
    return edge


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
edge = krisch(image, _boundary="symm")
# 邊緣強度的灰度級顯示
rows, cols = edge.shape
for r in range(rows):
    for c in range(cols):
        if edge[r][c] > 255:
            edge[r][c] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
# 經過閾值處理的邊緣顯示
cv2.namedWindow("thresh_edge", 1)
MAX_THRESH = 255
thresh = 255


# 回調函數，閾值處理
def callback_thresh(_thresh):
    threshEdge = edge.copy()
    threshEdge[threshEdge < _thresh] = 0
    threshEdge[threshEdge >= _thresh] = 255
    cv2.imshow("thresh_edge", threshEdge)


callback_thresh(thresh)
cv2.createTrackbar("thresh", "thresh_edge", thresh, MAX_THRESH, callback_thresh)

# 模擬素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch < 50] = 50
cv2.imshow("pencilSketch", pencilSketch)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
