"""
OpenCV 基本使用

建立影像
	2D全黑/全白/隨機/著色
	3D全黑/全白/隨機/著色
開啟檔案
	彩色/黑白/其他參數
存檔

CV視窗之使用

顯示圖片 / 使用 cv2 顯示圖片 / 使用 matplotlib 顯示圖片

讀取圖片 存圖

以 cv2.imread 讀進來的資料，會儲存成一個 NumPy 的陣列
查看資料型態
print(type(image))
print(type(image_gray))
<class 'numpy.ndarray'>

#此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度
#第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）

h ,w, d = image.shape
print("Image Size: %d x %d, channel = %d" % (w, h, d))

h ,w = image_gray.shape
#print("Image Size: %d x %d, channel = %d" % (w, h, d))

cv2.imshow('Picture Viewer', image) #顯示圖片

此 NumPy 陣列的前兩個維度分別是圖片的高度與寬度，第三個維度則是圖片的 channel（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）。

圖檔格式

OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：

cv2.IMREAD_COLOR
    此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。
cv2.IMREAD_GRAYSCALE
    以灰階的格式來讀取圖片。
cv2.IMREAD_UNCHANGED
    讀取圖片中所有的 channels，包含透明度的 channel。

cv2.IMREAD_COLOR     彩色 + 無透明度 (預設)
cv2.IMREAD_GRAYSCALE 灰階
cv2.IMREAD_UNCHANGED 彩色 + 有透明度

OpenCV 基本使用

opencv + numpy製作資料
"""

from opencv_common import *

W, H = 640, 480
width, height = 640, 480  # 影像寬, 影像高
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("取得 OpenCV 版本")

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split(".")

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
建立影像
	2D全黑/全白/隨機/著色
	3D全黑/全白/隨機/著色
"""
print("二維黑圖")
image = np.zeros((H, W), dtype=np.uint8)

print("三維黑圖")
image = np.zeros((H, W, 3), np.uint8)
image = np.zeros((H, W, 3), dtype="uint8")
image = np.zeros((H, W, 3), dtype=np.uint8)

print("三維白圖")
image = np.ones((H, W, 3), np.uint8) * 255
image = np.ones((H, W, 3), dtype="uint8") * 255

# 灰色背景
image[:] = (128, 128, 128)

# 用(B, G, R) = (255, 255, 255): 白色填滿畫布
image.fill(255)  # 將這個矩陣全部填入255 => 白色, 128 => 灰色

# 將這個矩陣全部填入指定顏色
image[:] = [48, 213, 254]

image1 = np.ones((H, W), dtype=np.uint8) * 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
mask = np.zeros((H, W), dtype=np.uint8)
mask[2:4, 2:4] = 1
image3 = np.ones((H, W), dtype=np.uint8) * 66
image3 = cv2.add(image1, image2, mask=mask)

image1 = np.ones((H, W), dtype=np.uint8) * 3
image2 = np.ones((H, W), dtype=np.uint8) * 5
image3 = cv2.add(image1, image2)

image4 = cv2.add(image1, 6)
image5 = cv2.add(6, image2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image1 = np.ones((H, W), dtype=np.uint8) * 100
image2 = np.ones((H, W), dtype=np.uint8) * 10

# 兩影像用cv2權重gamma相加
gamma = 3
image3 = cv2.addWeighted(image1, 0.6, image2, 5, gamma)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("用np建立一個隨機影像陣列")

W, H = 5, 4
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)

H, W = image.shape

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        # mapx.itemset((i, j), W - 1 - j)
        mapy.itemset((i, j), i)
        # mapy.itemset((i, j), H - 1 - i)

rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("用np建立一個隨機影像陣列")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("用np建立一個隨機影像陣列")
W, H = 6, 4
image = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)

H, W = image.shape

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), i)
        mapy.itemset((i, j), j)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("用np建立一個隨機影像陣列")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Random建立二維陣列為影像 a")
W, H, D = 10, 10, 3
a = np.random.randint(0, 255, (H, W), dtype=np.uint8)
b = np.zeros((H, W), dtype=np.uint8)

# mask
b[2:8, 2:8] = 255

c = cv2.bitwise_and(a, b)

plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
plt.title("影像1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("影像2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))
plt.title("影像3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3

image = np.random.randint(0, 256, size=[H, W, D], dtype=np.uint8)

plt.figure("Random建立二維陣列 深度為3", figsize=(12, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random建立二維陣列 深度為3")

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 5, 4, 3
image = np.random.randint(0, 256, size=[H, W, D], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 10, 10, 3
image = np.zeros((H, W), np.uint8)
image[3:8, 3:8] = 255

plt.figure("侵蝕/擴張", figsize=(10, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

W, H, D = 1, 3, 3
kernel = np.ones((H, W), np.uint8)
erosion = cv2.erode(image, kernel)  # 侵蝕
print("image = \n", image)
print("kernel = \n", kernel)
print("erosion = \n", erosion)

plt.subplot(132)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))
plt.title("侵蝕")

W, H, D = 1, 3, 3
kernel = np.ones((H, W), np.uint8)
dilation = cv2.dilate(image, kernel)
print("image = \n", image)
print("kernel = \n", kernel)
print("dilation\n", dilation)

plt.subplot(133)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))
plt.title("擴張")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image1 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)
image2 = np.random.randint(0, 256, size=[H, W], dtype=np.uint8)

print("兩影像用cv2相加")
image3 = cv2.add(image1, image2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 以上為建立影像陣列 2D 3D


print("------------------------------------------------------------")  # 60個
# 讀取圖片
print("------------------------------------------------------------")  # 60個

""" OK
print('使用 cv2 顯示圖片')

image = cv2.imread(filename1)

cv2.imshow('Image', image)  #顯示圖片, 標題不支持中文

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("開啟檔案成灰階影像")
image = cv2.imread(filename1, 0)
print("灰階 圖像屬性：")
print("image.shape=", image.shape)
print("image.size=", image.size)
print("image.dtype=", image.dtype)

print("開啟檔案成彩色影像")
image = cv2.imread(filename1)
# image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)	# -1 讀取本機圖片, 不改變顏色通道
# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#  0 讀取本機圖片, 直接變成灰階
# image = cv2.imread(filename, cv2.IMREAD_COLOR)         #  1 讀取本機圖片, 改為BGR三通道(預設)

# print('cv2.IMREAD_UNCHANGED =', cv2.IMREAD_UNCHANGED)   # -1
# print('cv2.IMREAD_GRAYSCALE =', cv2.IMREAD_GRAYSCALE)   #  0
# print('cv2.IMREAD_COLOR =', cv2.IMREAD_COLOR)           #  1(預設)

print("彩色 圖像屬性：")
print("image.shape=", image.shape)
print("image.size=", image.size)
print("image.dtype=", image.dtype)

print("image.shape格式 :", type(image.shape))
print("image.shape內容 :", image.shape)

h = image.shape[0]  # 高
w = image.shape[1]  # 寬
d = image.shape[2]  # 深
h, w, d = image.shape  # d為dimension d=3 全彩, d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

plt.subplot(121)
# plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示圖片 要轉RGB")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 圖片轉為灰階

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))  # 顯示圖片   #原圖轉黑白
plt.title("先轉灰階 再轉RGB")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取圖片 並顯示")
image = cv2.imread(filename1, 1)  # 讀取本機圖片, 0: 黑白圖片 1: 原色圖片
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image_gray = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 讀取本機圖片, 直接轉為灰階

image_gray = cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB)
plt.imshow(image_gray)
show()

"""
這裡 cv2.waitKey 函數是用來等待與讀取使用者按下的按鍵，而其參數是等待時間（單位為毫秒），
若設定為 0 就表示持續等待至使用者按下按鍵為止，
這樣當我們按下任意按鍵之後，就會呼叫 cv2.destroyAllWindows 關閉所有 OpenCV 的視窗。

如果在程式中有許多的 OpenCV 視窗，而我們只要關閉特定的視窗時，可以改用 cv2.destroyWindow 加上視窗名稱，關閉指定的視窗：

# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')

在預設的狀況下，以 cv2.imshow 所開啟的視窗會依據圖片來自動調整大小，但若是圖片太大、佔滿整個螢幕時，我們會希望可以自由縮放視窗的大小，這時候就可以使用 cv2.namedWindow 將視窗設定為 cv2.WINDOW_NORMAL：

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

cv2.imshow('My Image', image)

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)  # 0 : 持續等待至使用者按下按鍵為止
cv2.destroyAllWindows() # 關閉所有 OpenCV 的視窗

# 關閉 'My Image' 視窗
# cv2.destroyWindow('My Image') 指名關閉某視窗

使用 OpenCV 開啟的圖形視窗會類似這樣：

OpenCV 顯示圖片視窗

灰階的圖片也可以顯示，用法都相同：
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image_bgr = cv2.imread(filename1)

# 將 OpenCV 讀入的 BGR 格式轉為 Matplotlib 用的 RGB 格式，再交給 Matplotlib 顯示
image_rgb = image_bgr[:, :, ::-1]  # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(image_rgb)
show()

image_gray = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 讀取本機圖片, 直接轉為灰階

# 使用 Matplotlib 顯示圖片
plt.imshow(image_gray, cmap="gray")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("像素操作 底片效果 半張負片")

image = cv2.imread(filename1)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

rows = image.shape[0]  # 取得高度的總像素
cols = image.shape[1]  # 取得寬度的總像素

for row in range(int(rows / 2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        image[row, col, 0] = 255 - image[row, col, 0]  # 255 - 藍色
        image[row, col, 1] = 255 - image[row, col, 1]  # 255 - 綠色
        image[row, col, 2] = 255 - image[row, col, 2]  # 255 - 紅色

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("半張負片")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("像素操作 全張負片")

image = cv2.imread(filename1)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image = 255 - image  # 使用 255 減去陣列中所有數值

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("全張負片")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image_bgr = cv2.imread(filename1)
image_rgb = image_bgr[:, :, ::-1]  # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用 OpenCV 讀取並顯示圖片


# 等同於 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #BGR轉RGB再交由matplotlib顯示之
def aidemy_imshow(name, image):
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    plt.title(name)
    plt.imshow(image)
    show()


cv2.imshow = aidemy_imshow

cv2.waitKey()
cv2.destroyAllWindows()

print("-----------------------------")

print("並列一圖")

image1 = cv2.imread(filename1)
image2 = cv2.hconcat([image1, image1, image1, image1, image1, image1])

plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("並列一圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp"

image = cv2.imread(filename)  # cv2讀取圖片, 自動轉成array

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 轉換為RGB

plt.subplot(121)
plt.imshow(rgb)
plt.title("cv影像轉RGB")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # 轉換為HSV

plt.subplot(122)
plt.imshow(hsv)
plt.title("cv影像轉HSV")

show()

print("coordinate")
coordinate = rgb[131, 81]  # 輸入要取得顏色的指定座標
print(coordinate)

# print('取得cv影像陣列中的資料')
# print(array([255, 219,  79], dtype=uint8))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試CV視窗 : 全螢幕顯示一圖")

image = cv2.imread(filename1)

window_name = "Full-screen"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("測試CV視窗 : 設定視窗大小並依視窗縮放影像")

image = cv2.imread(filename1)

window_name = window_name
cv2.namedWindow(window_name, 0)
cv2.resizeWindow(window_name, 640, 480)

# 設定視窗位置
x_st, y_st = 300, 100
cv2.moveWindow(window_name, x_st, y_st)

# 顯示圖片
cv2.imshow(window_name, image)

cv2.waitKey()
cv2.destroyAllWindows()

# 設定視窗參數, 若不設定, 即是 圖片滿框、不可調整大小
# 預設 flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO |WINDOW_GUI_EXPANDED

# 可調整大小
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# WINDOW_FREERATIO 不 保持比例
# WINDOW_KEEPRATIO    保持比例

# 可調整大小 並 保持比例
# cv2.namedWindow('image', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_03")

image_r = cv2.imread(filename1)
image_g = cv2.imread(filename1)
image_b = cv2.imread(filename1)

image_r[:, :, 0] = 0  # 將藍色設為 0
image_r[:, :, 1] = 0  # 將綠色設為 0

image_g[:, :, 0] = 0  # 將藍色設為 0
image_g[:, :, 2] = 0  # 將紅色設為 0

image_b[:, :, 1] = 0  # 將綠色設為 0
image_b[:, :, 2] = 0  # 將紅色設為 0

plt.subplot(131)
plt.imshow(cv2.cvtColor(image_r, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image_g, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image_b, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)
image_b = cv2.imread(filename2)
image_g = cv2.imread(filename2)
image_r = cv2.imread(filename2)

image_b[:, :, 1] = 0  # 將綠色設為 0
image_b[:, :, 2] = 0  # 將紅色設為 0
image_g[:, :, 0] = 0  # 將藍色設為 0
image_g[:, :, 2] = 0  # 將紅色設為 0
image_r[:, :, 0] = 0  # 將藍色設為 0
image_r[:, :, 1] = 0  # 將綠色設為 0

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_r, cv2.COLOR_BGR2RGB))
plt.title("R")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image_g, cv2.COLOR_BGR2RGB))
plt.title("G")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image_b, cv2.COLOR_BGR2RGB))
plt.title("B")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

print("原圖 彩色 轉 灰階1通道")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # cv2影像 轉 灰階

print("灰階 轉 BGR3通道")
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # 轉灰階
print("rgb.shape=", rgb.shape)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖 彩色")

plt.subplot(132)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("灰階1通道")

plt.subplot(133)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))
plt.title("BGR3通道")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("原圖 BGR 轉 RGB")

image = cv2.imread(filename1)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖 B-G-R OK")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))
plt.title("原圖 BGR 轉 RGB NG")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 灰階讀取
image = cv2.imread(filename1, 0)

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("修改一部份資料 1")
for i in range(20, 60):  # y
    for j in range(20, 100):  # x
        image[i, j] = 255

print("修改一部份資料 2")
# 測試讀取、修改單個像素值
print("讀取像素點image.item(3,2)=", image.item(3, 2))
image.itemset((3, 2), 255)
print("修改後像素點image.item(3,2)=", image.item(3, 2))
# 測試修改一個區域的像素值
for i in range(100, 200):  # y
    for j in range(20, 60):  # x
        image.itemset((i, j), 220)

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("修改後的圖")

print("------------------------------")  # 30個

# 彩色讀取
image = cv2.imread(filename1)

plt.subplot(223)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("讀取image[0,0]=", image[0, 0])
print("讀取image[0,0,0]=", image[0, 0, 0])
print("讀取image[0,0,1]=", image[0, 0, 1])
print("讀取image[0,0,2]=", image[0, 0, 2])
print("讀取image[50,0]=", image[50, 0])
print("讀取image[100,0]=", image[100, 0])
# 區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            image[i, j, k] = 255  # 白色
# 區域2
for i in range(50, 100):
    for j in range(0, 100):
        image[i, j] = [128, 128, 128]  # 灰色
# 區域3
for i in range(100, 150):
    for j in range(0, 100):
        image[i, j] = 0  # 黑色
# 區域4
print("讀取image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("讀取image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("讀取image.item(0, 0, 2) = ", image.item(0, 0, 2))
for i in range(200, 250):
    for j in range(0, 100):
        for k in range(0, 3):
            image.itemset((i, j, k), 255)  # 白色

print("修改後image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("修改後image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("修改後image.item(0, 0, 2) = ", image.item(0, 0, 2))
print("修改後image[0, 0] = ", image[0, 0])
print("修改後image[0, 0, 0] = ", image[0, 0, 0])
print("修改後image[0, 0, 1] = ", image[0, 0, 1])
print("修改後image[0, 0, 2] = ", image[0, 0, 2])
print("修改後image[50, 0] = ", image[50, 0])
print("修改後image[100, 0] = ", image[100, 0])

plt.subplot(224)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("修改後的圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lena_color_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
)

a = cv2.imread(lena_color_filename, cv2.IMREAD_UNCHANGED)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("擷取一塊出來, 並顯示之")
face = a[200:400, 200:380]  # h, w

plt.subplot(132)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.title("擷取一塊出來")

print("將其中一塊亂碼化, 並顯示之")
x_st, y_st, w, h = 50, 50, 100, 180
face = np.random.randint(0, 256, (h, w, 3))
a[y_st : y_st + h, x_st : x_st + w] = face

plt.subplot(133)
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
plt.title("將其中一塊亂碼化")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("漸層色")

w, h = 400, 400
image = np.zeros([h, w, 3])
for i in range(h):
    for j in range(w):
        image[i, j, 0] = int(256 * (j + i) / (w + h))
        image[i, j, 2] = int(256 * (j + i) / (w + h))

image = image.astype("float32") / 255

cvshow("image", image)

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

w, h = 400, 400

image = np.zeros([h, w, 4])  # 第三個值為 4
for i in range(h):
    image[i, :, 3] = int(256 * i / 400)  # 設定第四個值 ( 透明度 )

image = image.astype("float32") / 255

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

W, H, D = 640, 480, 3

print("初始化 H X W X D 陣列")
W, H, D = 640, 480, 3
image = np.zeros((H, W, D), dtype="uint8") * 255

# print(image)
print(image.shape)

print("---------------")

# image[0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3] = 10   #x方向
# image[0 : 3, 0 : 3, 0 : 3] = 10   #x方向

print("將所有點著色 著紅色")
image[:] = RED
# print(image)

# image[0 : 50, 0 : 50] = 123 #前x, 後y
# image[2 : 6, 2 : 6] = 126

print("顯示原圖 BGR 排列")
cv2.imshow("image original B-G-R arrangement", image)

print("BGR轉RGB")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("R-G-B arrangement, wrong", rgb)

print("RGB轉BGR")
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
cv2.imshow("B-G-R arrangement", bgr)

# print("image = \n", image)
# print("rgb = \n", rgb)
# print("bgr = \n", bgr)

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')

plt.figure("建立圖檔 RGB與BGR排列", figsize=(12, 6))
plt.subplot(121)
plt.imshow(rgb)
plt.title("R-G-B 排列")

plt.subplot(122)
plt.imshow(bgr)
plt.title("B-G-R 排列")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

w = int(640 / 20)
h = int(480 / 20)
W, H, D = 640, 480, 3

image = np.random.randint(0, 256, size=[h, w, D], dtype=np.uint8)
print(image.shape)
rst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(rst.shape)
# print("image = \n", image)
print("rst = \n", rst)
print(
    "像素點 (1, 0) 直接計算得到的值 = ",
    image[1, 0, 0] * 0.114 + image[1, 0, 1] * 0.587 + image[1, 0, 2] * 0.299,
)
print("像素點 (1, 0) 使用公式cv2.cvtColor()轉換值 = ", rst[1, 0])
"""
print(image[1, 0, 0])
print(image[1, 0, 1])
print(image[1, 0, 2])
"""

# BGR排列轉RGB排列
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# RGB排列轉BGR排列
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
"""
print("image = \n", image)
print("rgb = \n", rgb)
print("bgr = \n", bgr)
"""

plt.figure("Random建立二維陣列 深度為3 轉灰階", figsize=(12, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Random 二維陣列")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.title("轉灰階")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# =========測試下OpenCV中藍色的HSV模式值=============

W, H, D = 1, 1, 3
imageBlue = np.zeros([H, W, D], dtype=np.uint8)
imageBlue[0, 0, 0] = 255
Blue = imageBlue
BlueHSV = cv2.cvtColor(Blue, cv2.COLOR_BGR2HSV)
print("Blue = \n", Blue)
print("BlueHSV = \n", BlueHSV)

# =========測試下OpenCV中綠色的HSV模式值=============
W, H, D = 1, 1, 3
imageGreen = np.zeros([H, W, D], dtype=np.uint8)
imageGreen[0, 0, 1] = 255
Green = imageGreen
GreenHSV = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)
print("Green = \n", Green)
print("GreenHSV = \n", GreenHSV)

# =========測試下OpenCV中紅色的HSV模式值=============
W, H, D = 1, 1, 3
imageRed = np.zeros([H, W, D], dtype=np.uint8)
imageRed[0, 0, 2] = 255
Red = imageRed
RedHSV = cv2.cvtColor(Red, cv2.COLOR_BGR2HSV)
print("Red = \n", Red)
print("RedHSV = \n", RedHSV)

plt.figure("BGR轉HSV", figsize=(12, 6))
plt.subplot(231)
plt.imshow(cv2.cvtColor(Red, cv2.COLOR_BGR2RGB))
plt.title("Red")

plt.subplot(232)
plt.imshow(cv2.cvtColor(Green, cv2.COLOR_BGR2RGB))
plt.title("Green")

plt.subplot(233)
plt.imshow(cv2.cvtColor(Blue, cv2.COLOR_BGR2RGB))
plt.title("Blue")

plt.subplot(234)
plt.imshow(cv2.cvtColor(RedHSV, cv2.COLOR_BGR2RGB))
plt.title("RedHSV")

plt.subplot(235)
plt.imshow(cv2.cvtColor(GreenHSV, cv2.COLOR_BGR2RGB))
plt.title("GreenHSV")

plt.subplot(236)
plt.imshow(cv2.cvtColor(BlueHSV, cv2.COLOR_BGR2RGB))
plt.title("BlueHSV")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


W, H, D = 5, 5, 3
image = np.ones([H, W], dtype=np.uint8) * 9

mask = np.zeros([H, W], dtype=np.uint8)
mask[0:3, 0] = 1
mask[2:5, 2:4] = 1

roi = cv2.bitwise_and(image, image, mask=mask)
print("image = \n", image)
print("mask = \n", mask)
print("roi = \n", roi)

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

print("製作影像")

width, height = 640, 480  # 影像寬, 影像高

# 建立 640 X 480 之黑圖
image = np.zeros((height, width), dtype=np.uint8)

# 建立 640 X 480 之白圖
image = np.ones((height, width), dtype=np.uint8) * 255

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
print("------------------------------------------------------------")  # 60個

# 取出像素值, 修改之

img = cv2.imread(filename1)

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
print("------------------------------------------------------------")  # 60個

print("修改alpha通道值 255=>127")

# 4通道的PNG圖
filename_RGB_R = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"

img = cv2.imread(filename_RGB_R, cv2.IMREAD_UNCHANGED)  # PNG讀取
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

img = cv2.imread(filename1)
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


print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)
img[0, 0] = [0, 0, 255]
img[10:100, 10:100] = [0, 255, 0]
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


# 灰階讀取
image = cv2.imread(filename1, 0)


output = np.zeros([row, col, channel], dtype=np.uint8)  # 產生空白畫布


print("讀取圖片 並顯示")
image = cv2.imread(filename1, 1)  # 讀取本機圖片, 0: 黑白圖片 1: 原色圖片
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()


rst = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # 轉灰階

rst = cv2.convertScaleAbs(image)
