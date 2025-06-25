"""
影像的幾何變換

C : cut
C : copy
R : resize
R : rotate

resize() 的 interpolation
INTER_NEAREST	0	最近插值法
INTER_LINEAR	1	雙線性插值法，在插入點選擇4個點進行插值處理，這是預設的方法
INTER_CUBIC	2	雙三次插值法，可以創造更平滑的邊緣影像
INTER_AREA	3	對影像縮小重新採樣的首選方法，但是影像放大時類似最近插值法
INTER_LENCZOS4	4	Lencz的插值方法，這個方法會在x和y的方向分別對8個點進行插值


AffineTransform
PerspectiveTransform

"""

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

from opencv_common import *

print("------------------------------------------------------------")  # 60個

# 裁剪圖片

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
# 檔案 => cv2影像
image = cv2.imread(filename)  # 讀取本機圖片

# 裁切區域的 x 與 y 座標（左上角）
x_st, y_st = 100, 100

# 裁切區域的長度與寬度
w, h = 250, 250

# 裁切圖片
crop_image = image[y_st : y_st + h, x_st : x_st + w]

cv2.imshow("cropped", crop_image)  # 顯示圖片

image_empty = np.zeros(image.shape, dtype=np.uint8)  # 依照原圖大小建立一個圖像的二維陣列

# cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

# 將擷取的圖貼到新建的黑圖
image_empty[y_st : y_st + h, x_st : x_st + w] = crop_image
cv2.imshow("cropped+new", image_empty)  # 顯示圖片

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖片裁剪縮放")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)  # 讀取本機圖片

x = 100
y = 100
w = 100
h = 100

print("------------------------------------------------------------")  # 60個


print("旋轉圖片")

# 影像旋轉
# 以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

# 檔案 => cv2影像
image = cv2.imread(filename)  # 讀取本機圖片
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
show()

h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w // 2, h // 2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.7)

rotate_image = cv2.warpAffine(image, P, (w, h))

rotate_image = cv2.cvtColor(rotate_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotate_image)

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
img = cv2.imread(filename)

x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)

plt.figure("鏡射", figsize=(16, 12))
plt.subplot(221)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(x, cv2.COLOR_BGR2RGB))
plt.title("x鏡射")

plt.subplot(223)
plt.imshow(cv2.cvtColor(y, cv2.COLOR_BGR2RGB))
plt.title("y鏡射")

plt.subplot(224)
plt.imshow(cv2.cvtColor(xy, cv2.COLOR_BGR2RGB))
plt.title("xy鏡射")

show()

print("------------------------------------------------------------")  # 60個

"""

resize


"""

print("------------------------------------------------------------")  # 60個

print("縮放圖片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
print("原圖大小 :", img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 2, H // 2))  # .resize 改變圖片大小W,H
print("縮放後大小 :", img_resize.shape)

plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB))
plt.title("縮放 W兩倍 H一半")

show()

print("------------------------------------------------------------")  # 60個

dH, dW = 480, 480


def resizeimg(image):
    # 將影像改變到寬高最大為480等比例縮放
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (dW, math.floor(h / (w / dW))))
    else:
        img = cv2.resize(image, (math.floor(w / (h / dH)), dH))
    return img


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image1 = cv2.imread(filename)
print("原圖大小 : ", image1.shape)

image2 = resizeimg(cv2.imread(filename))
print("將影像改變到寬高最大為480等比例縮放")
print("縮放後大小 : ", image2.shape)

plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("等比例縮放 至 480")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

# 檔案 => cv2影像
image_original = cv2.imread(filename)  # 讀取本機圖片

# 縮放的倍率 fx fy
image_resized = cv2.resize(
    image_original, None, fx=1.50, fy=1.00, interpolation=cv2.INTER_LINEAR
)  # .resize 改變圖片大小W,H

plt.figure(figsize=(10, 6))
plt.subplot(121)
image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
plt.imshow(image_original)
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

plt.subplot(122)
image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(image_resized)
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("倍率縮放")

show()

print("------------------------------------------------------------")  # 60個

print("用np建立一個影像陣列")

W = 640
H = 480
D = 3

# 建立陣列
image = np.ones([H, W, D], dtype=np.uint8) * 128  # 填滿 128

# 改變陣列內容
image[:, :, 0] = 0
# 第0通道 B
image[:, :, 1] = 255
# 第1通道 G
image[:, :, 2] = 255
# 第2通道 R

# 做resize
size = H, W
print(size)
rst = cv2.resize(image, size)  # .resize 改變圖片大小W,H

print("原圖大小 :", image.shape)
print("縮放後大小 :", rst.shape)

plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.xlim(0, 700)  # x軸顯示邊界
plt.ylim(700, 0)  # y軸顯示邊界
plt.title("原圖 640X480")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.xlim(0, 700)  # x軸顯示邊界
plt.ylim(700, 0)  # y軸顯示邊界
plt.title("resize 480X640")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape

print("原圖大小 :", image.shape)
print("W = ", W)
print("H = ", H)
print("D = ", D)

size = (int(W * 0.9), int(H * 1.1))  # 變瘦變高
image2 = cv2.resize(image, size)  # .resize 改變圖片大小W,H
print("縮放後大小 :", image2.shape)

plt.figure("resize", figsize=(12, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("resize 變瘦1成變高1成")

image3 = cv2.resize(image, None, fx=1.5, fy=0.5)  # .resize 改變圖片大小W,H
print("縮放後大小 :", image3.shape)

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("resize x變1.5倍, y變一半")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y : y + h, x : x + w]

output = np.zeros((360, 480, 3), dtype="uint8")  # 產生黑色畫布
output[x : x + w, y : y + h] = crop_img

# 檔案 => cv2影像
img = cv2.imread(filename)
output_1 = cv2.resize(img, (200, 200))  # 產生 200x200 的圖
output_2 = cv2.resize(img, (100, 300))  # 產生 100x300 的圖

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
size = img.shape  # 取得原始圖片的資訊
level = 15  # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0] / level)  # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1] / level)  # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)  # 根據縮小尺寸縮小
mosaic = cv2.resize(
    mosaic, (size[1], size[0]), interpolation=cv2.INTER_NEAREST
)  # 放大到原本的大小

cv2.imshow("image", mosaic)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("馬賽克")
# 檔案 => cv2影像
img = cv2.imread(filename)

x = 135  # 剪裁區域左上 x 座標
y = 90  # 剪裁區域左上 y 座標
cw = 100  # 剪裁區域寬度
ch = 120  # 剪裁區域高度
mosaic = img[y : y + ch, x : x + cw]  # 取得剪裁區域
level = 15  # 馬賽克程度
h = int(ch / level)  # 縮小的高度 ( 使用 int 去除小數點 )
w = int(cw / level)  # 縮小的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_LINEAR)
mosaic = cv2.resize(mosaic, (cw, ch), interpolation=cv2.INTER_NEAREST)
img[y : y + ch, x : x + cw] = mosaic  # 將圖片的剪裁區域，換成馬賽克的圖

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

rotate


"""
print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename, 1)

print("旋轉")
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape
print("原圖大小 :", image.shape)
print("W = ", W)
print("H = ", H)
print("D = ", D)

M = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 0.6)
rotate = cv2.warpAffine(image, M, (W, H))

plt.figure("rotate", figsize=(16, 12))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB))
plt.title("rotate")

show()

print("------------------------------------------------------------")  # 60個

print("圖片旋轉")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)

H = img.shape[0]
W = img.shape[1]

aff_matrix = cv2.getRotationMatrix2D((W / 2, H / 2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (W, H))

cv2.imshow("image", img_rotate)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖片旋轉")
img_rotate = cv2.rotate(img, 1)

cv2.imshow("image", img_rotate)
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

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y : y + h, x : x + w]  # 取出陣列的範圍

cv2.imshow("image", crop_img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


# flip

# 檔案 => cv2影像
img = cv2.imread(filename)  # 開啟圖片
output_0 = cv2.flip(img, 0)  # 上下翻轉
output_1 = cv2.flip(img, 1)  # 左右翻轉
output_2 = cv2.flip(img, -1)  # 上下左右翻轉

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
output = cv2.transpose(img)  # 逆時針旋轉 90 度。

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
output_ROTATE_90_CLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
output_ROTATE_90_COUNTERCLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
output_ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180)

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
M = np.float32([[1, 0, 100], [0, 1, 100]])  # 2x3 矩陣，x 軸平移 100，y 軸平移 100
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
M = cv2.getRotationMatrix2D((240, 180), 45, 1)  # 中心點 (240, 180)，旋轉 45 度，尺寸 1
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
p1 = np.float32([[100, 100], [480, 0], [0, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360]])
M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

p1 = np.float32([[100, 100], [480, 0], [0, 360], [480, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360], [480, 360]])
m = cv2.getPerspectiveTransform(p1, p2)

# 檔案 => cv2影像
img = cv2.imread(filename)
output = cv2.warpPerspective(img, m, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 原图的高宽
h, w = image.shape[:2]
# 仿射变换矩阵，缩小两倍
A1 = np.array([[0.5, 0, 0], [0, 0.5, 0]], np.float32)
d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)
# 先缩小两倍，再平移
A2 = np.array([[0.5, 0, w / 4], [0, 0.5, h / 4]], np.float32)
d2 = cv2.warpAffine(image, A2, (w, h), borderValue=125)
# 在 d2 的基础上，绕图像的中心点旋转
A3 = cv2.getRotationMatrix2D((w / 2, h / 2), 30, 1)
d3 = cv2.warpAffine(d2, A3, (w, h), borderValue=125)
# 在
A4 = np.array([[math.cos(math.pi / 4), 0, 0], [math.sin(math.pi / 3), 1, 0]])
d4 = cv2.warpAffine(image, A4, (2 * w, 2 * h), borderValue=125)

cv2.imshow("image", image)
cv2.imshow("d1", d1)
cv2.imshow("d2", d2)
cv2.imshow("d3", d3)
cv2.imshow("d4", d4)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 第3章：空間變換\3.2-投影變換\perspective.py

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image = cv2.imread(filename)

# 原图的宽高
h, w, d = image.shape
# 将原图的四个顶点投影到一个不规则的四边形中
src = np.array([[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]], np.float32)
dst = np.array([[20, 50], [w / 2, 150], [50, h / 2], [w - 40, h - 40]], np.float32)
# 计算投影矩阵
p = cv2.getPerspectiveTransform(src, dst)
# 利用计算出的投影矩阵进行头像的投影变换
r = cv2.warpPerspective(image, p, (w, h), borderValue=0)

# 显示原图和投影效果
cv2.imshow("image", image)
cv2.imshow("warpPerspective", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("flip")

# 檔案 => cv2影像
I = cv2.imread(filename)

O = I.copy()

# 旋轉
O = cv2.flip(O, 1)

# 顯示原圖和輸出圖像
cv2.imshow("I", I)
cv2.imshow("O", O)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# 新進
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.resize()")

src = cv2.imread(filename1)

print("圖片拉成 640 X 480")
width, height = 640, 480  # 影像寬, 影像高
dsize = (width, height)

dst1 = cv2.resize(src, dsize)  # 重設影像大小

print("圖片拉成 寬度2倍，高度一半")
dst2 = cv2.resize(src, None, fx=2.0, fy=0.5)  # 重設影像大小

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原始影像")

plt.subplot(312)
plt.imshow(dst1)
plt.title("圖片拉成 640 X 480")

plt.subplot(313)
plt.imshow(dst2)
plt.title("圖片拉成 寬度2倍，高度一半")

show()

print("------------------------------------------------------------")  # 60個

print("cv2.flip()")

src = cv2.imread(filename1)

print("上下顛倒")
dst1 = cv2.flip(src, 0)  # 垂直翻轉

print("左右顛倒")
dst2 = cv2.flip(src, 1)  # 水平翻轉


print("上下顛倒 + 左右顛倒")
dst3 = cv2.flip(src, -1)  # 水平與垂直翻轉

plt.subplot(221)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("上下顛倒")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("左右顛倒")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("上下顛倒 + 左右顛倒")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 20 Y對稱一張圖片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

D = 20
output = np.zeros((h + D * 2, w * 2 + D * 2, 3), dtype="uint8")  # 產生 2W x H 的黑色背景

image1 = image1[:h, :w]  # 取出 WxH 的影像 全部 也可只取部分

print("左右翻轉影像")
image12 = cv2.flip(image1, 1)

# 左半
output[D : h + D, D : w + D] = image1  # 將 output 左邊內容換成 image1

# 右半
output[D : h + D, w + D : w * 2 + D] = image12  # 將 output 右邊內容換成 image2

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

print("opencv 21 XY對稱一張圖片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

output = np.zeros((h * 2, w * 2, 3), dtype="uint8")  # 產生 2W x 2H 的黑色背景

img = image1[:h, :w]  # 取出 WxH 的影像 全部 也可只取部分
img2 = cv2.flip(img, 1)  # 左右翻轉
img3 = cv2.flip(img, 0)  # 上下翻轉
img4 = cv2.flip(img, -1)  # 上下左右翻轉

# 左上
output[:h, :w] = img
# 右上
output[:h, w : w * 2] = img2
# 左下
output[h : h * 2, :w] = img3
# 右下
output[h : h * 2, w : w * 2] = img4

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.warpAffine() 平移")

src = cv2.imread(filename1)

height, width = src.shape[0:2]  # 獲得影像大小
dsize = (width, height)  # 建立未來影像大小
x = 30  # 平移 x = 30
y = 80  # 平移 y = 80
M = np.float32([[1, 0, x], [0, 1, y]])  # 建立 M 矩陣
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("平移 (30, 80)")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

print("旋轉")

src = cv2.imread(filename1)

height, width = src.shape[0:2]  # 獲得影像大小

print("逆時鐘 旋轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)  # 建立 M 矩陣
dsize = (width, height)  # 建立未來影像大小
dst1 = cv2.warpAffine(src, M, dsize)  # 執行仿射

print("順時鐘 旋轉 30 度")
M = cv2.getRotationMatrix2D((width / 2, height / 2), -30, 1)  # 建立 M 矩陣
dst2 = cv2.warpAffine(src, M, dsize)  # 執行仿射

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("逆時鐘 30")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("順時鐘 30")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1)

print("仿射 歪折 折向右")
height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst1 = cv2.warpAffine(src, M, dsize)  # 執行仿射

print("仿射 歪折 折向左")
height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # src的A,B,C三個點
dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst2 = cv2.warpAffine(src, M, dsize)  # 執行仿射

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("仿射 歪折 折向右")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("仿射 歪折 折向左")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

src = cv2.imread(filename1)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.2]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("仿射 歪折 轉置")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

src = cv2.imread(filename1)

height, width = src.shape[0:2]  # 獲得影像大小
srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.4]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)  # 執行仿射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("仿射 歪折 轉置")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename3)

height, width = src.shape[0:2]  # 獲得影像大小
a1 = [0, 0]  # 原始影像的 A
b1 = [width, 0]  # 原始影像的 B
c1 = [0, height]  # 原始影像的 C
d1 = [width - 1, height - 1]  # 原始影像的 D

srcp = np.float32([a1, b1, c1, d1])
a2 = [150, 0]  # dst的 A
b2 = [width - 150, 0]  # dst的 B
c2 = [0, height - 1]  # dst的 C
d2 = [width - 1, height - 1]  # dst的 D

dstp = np.float32([a2, b2, c2, d2])
M = cv2.getPerspectiveTransform(srcp, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpPerspective(src, M, dsize)  # 執行透視

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("顯示透視影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

src = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
rows, cols = src.shape
mapx = np.ones(src.shape, np.float32) * 3  # 設定 mapx
mapy = np.ones(src.shape, np.float32) * 2  # 設定 mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1)

rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("執行映射")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1)

rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("執行映射")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename1)

rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("執行映射")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            mapx.itemset((r, c), 2 * (c - cols * 0.25))  # 計算對應的 x
            mapy.itemset((r, c), 2 * (r - rows * 0.25))  # 計算對應的 y
        else:
            mapx.itemset((r, c), 0)  # 取x座標為 0
            mapy.itemset((r, c), 0)  # 取y座標為 0
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("執行映射")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)
        mapy.itemset((r, c), 2 * r)
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("執行映射")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# AffineTransform
# PerspectiveTransform
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 08")
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename)

H, W, D = image.shape

x = 50
y = 50
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))
plt.title("影像移動")

plt.suptitle("影像移動")
show()

print("------------------------------------------------------------")  # 60個

print("opencv 09")
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

image = cv2.imread(filename)

H, W, D = image.shape

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("Affine(仿射的)Transform")

plt.suptitle("Affine(仿射的)Transform")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 10")
filename = r"data/PerspectiveTransform/PerspectiveTransform.jpg"

image = cv2.imread(filename)

H, W, D = image.shape

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])

pts1 = np.float32([[200, 0], [300, 0], [100, 600], [200, 600]])
pts2 = np.float32([[100, 0], [200, 0], [100, 600], [200, 600]])


pts1 = np.float32([[100, 0], [600, 0], [0, 600], [500, 600]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])


M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖是歪圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("把歪圖拉正")

plt.suptitle("PerspectiveTransform")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 98")

# 圖形變換
# 幾何變換

# 對圖形進行仿射變換
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
src = np.array([[0, 0], [w - 1, 0], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 300], [873, 78], [161, 923]], dtype=np.float32)

m = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()


print("------------------------------")  # 30個

print("opencv 99")

# 對圖形進行透視變換
src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 350], [800, 300], [900, 923], [161, 923]], dtype=np.float32)

m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# AffineTransform
# PerspectiveTransform
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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

#image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)


#图像旋转 ： cv2.ROTATE_180  cv2.ROTATE_90_COUNTERCLOCKWISE
rImg = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imwrite("lsImg.jpg",lsImg)

"""

image = cv2.flip(image, 1)  # 翻轉影像，使其如同鏡子
