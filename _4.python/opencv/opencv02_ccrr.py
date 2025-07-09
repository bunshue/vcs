"""
影像的幾何變換

C : copy
C : cut, crop
R : resize
R : rotate

# 影像縮放 resize
resize() 的 interpolation
INTER_NEAREST	0	最近插值法
INTER_LINEAR	1	雙線性插值法，在插入點選擇4個點進行插值處理，這是預設的方法
INTER_CUBIC	2	雙三次插值法，可以創造更平滑的邊緣影像
INTER_AREA	3	對影像縮小重新採樣的首選方法，但是影像放大時類似最近插值法
INTER_LANCZOS4	4	Lancz的插值方法，這個方法會在x和y的方向分別對8個點進行插值

# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

各種轉換
AffineTransform
PerspectiveTransform
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from opencv_common import *

print("------------------------------------------------------------")  # 60個
# C : copy ST
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# C : copy SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# C : cut, crop ST
print("------------------------------------------------------------")  # 60個

# 裁剪圖片

image = cv2.imread(filename1)

# 裁切區域 x, y, w, h
x, y, w, h = 120, 120, 100, 100

# 裁剪圖片
crop_image = image[y : y + h, x : x + w]  # 取出陣列的範圍

# 建立新圖，貼上裁剪圖片
new_image = np.zeros(image.shape, dtype=np.uint8)
new_image[y : y + h, x : x + w] = crop_image

new_image = np.zeros((360, 480, 3), dtype="uint8")  # 產生黑色畫布
new_image[x : x + w, y : y + h] = crop_image

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# R : rotate
print("------------------------------------------------------------")  # 60個

# 影像旋轉
# 以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

image = cv2.imread(filename1)
H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式
center = (W // 2, H // 2)  # 旋轉中心

print("逆時鐘 旋轉 30 度, 縮放0.7倍")
#                                旋轉中心 旋轉角度 縮放比例
M = cv2.getRotationMatrix2D(center, 30, 0.7)  # 建立 M 矩陣
dsize = (W, H)  # 建立未來影像大小
dst1 = cv2.warpAffine(image, M, dsize)  # 執行仿射

print("順時鐘 旋轉 30 度, 縮放0.7倍")
#                                旋轉中心 旋轉角度 縮放比例
M = cv2.getRotationMatrix2D(center, -30, 0.7)  # 建立 M 矩陣
dst2 = cv2.warpAffine(image, M, dsize)  # 執行仿射

plt.figure("旋轉圖片", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("逆時鐘 30")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("順時鐘 30")


M = cv2.getRotationMatrix2D(center, 30, 0.7)
dst3 = cv2.warpAffine(image, M, dsize, borderValue=125)

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("多了borderValue")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("鏡射 cv2.flip()")

image = cv2.imread(filename1)

print("左右顛倒")
image1 = cv2.flip(image, 1)  # 左右翻轉/水平翻轉

print("上下顛倒")
image0 = cv2.flip(image, 0)  # 上下翻轉/垂直翻轉

print("上下顛倒 + 左右顛倒")
image2 = cv2.flip(image, -1)  # 上下左右翻轉/水平垂直翻轉

plt.figure("鏡射", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("左右顛倒")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("上下顛倒")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("上下顛倒 + 左右顛倒")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# R : resize
print("------------------------------------------------------------")  # 60個
"""
print("縮放圖片 / 倍率縮放 / 各種插植方法")

image = cv2.imread(filename4b)

image_resize0 = cv2.resize(image, None, fx=4.00, fy=4.00, interpolation=cv2.INTER_NEAREST)
image_resize1 = cv2.resize(image, None, fx=4.00, fy=4.00, interpolation=cv2.INTER_LINEAR)
image_resize2 = cv2.resize(image, None, fx=4.00, fy=4.00, interpolation=cv2.INTER_CUBIC)
image_resize3 = cv2.resize(image, None, fx=4.00, fy=4.00, interpolation=cv2.INTER_AREA)
image_resize4 = cv2.resize(image, None, fx=4.00, fy=4.00, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("image", image)
cv2.imshow("image0", image_resize0)
cv2.imshow("image1", image_resize1)
cv2.imshow("image2", image_resize2)
cv2.imshow("image3", image_resize3)
cv2.imshow("image4", image_resize4)
cv2.waitKey()
cv2.destroyAllWindows()
"""
print("縮放圖片 / 倍率縮放")

image = cv2.imread(filename1)

plt.figure("縮放", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

print("------------------------------")  # 30個

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

print("圖片拉成特定大小")
width, height = 640, 480  # 影像寬, 影像高
width, height = W * 2, H // 2  # 影像寬, 影像高
width, height = int(W * 0.9), int(H * 1.1)  # 變瘦變高
dsize = (width, height)

image_resize1 = cv2.resize(image, dsize)  # .resize 改變圖片大小 至 dsize
# image_resize1 = cv2.resize(image, (640, 480))  # resize 成 640x480 的圖

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_resize1, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("縮放")

print("------------------------------")  # 30個

print("倍率縮放")

# 縮放的倍率 fx fy
image_resize2 = cv2.resize(
    image, None, fx=2.00, fy=0.50, interpolation=cv2.INTER_LINEAR
)

plt.subplot(223)
plt.imshow(cv2.cvtColor(image_resize2, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("倍率縮放 W兩倍 H一半")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("等比例縮放")

dH, dW = 480, 480


def resize_image(image0):
    # 將影像改變到寬高最大為480等比例縮放
    h, w = image0.shape[:2]
    if h < w:
        image = cv2.resize(image0, (dW, math.floor(h / (w / dW))))
    else:
        image = cv2.resize(image0, (math.floor(w / (h / dH)), dH))
    return image


image1 = cv2.imread(filename1)

image2 = resize_image(cv2.imread(filename1))
print("將影像改變到寬高最大為480等比例縮放")
print("縮放後大小 : ", image2.shape)

plt.figure(figsize=(8, 6))
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
print("------------------------------------------------------------")  # 60個

print("馬賽克 縮小放大法 全圖")
image = cv2.imread(filename2)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

level = 15  # 馬賽克程度, 縮小比例 ( 可當作馬賽克的等級 )
h = H // level
w = W // level

# 先縮小N倍
mosaic1 = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)

# 再放大N倍
mosaic2 = cv2.resize(mosaic1, (W, H), interpolation=cv2.INTER_NEAREST)

cv2.imshow("image", mosaic2)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("馬賽克 縮小放大法 部分")
image = cv2.imread(filename2)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

x = 160  # 剪裁區域左上 x 座標
y = 80  # 剪裁區域左上 y 座標
cw = 180  # 剪裁區域寬度
ch = 300  # 剪裁區域高度
mosaic1 = image[y : y + ch, x : x + cw]  # 取得剪裁區域

level = 15  # 馬賽克程度, 縮小比例 ( 可當作馬賽克的等級 )
w = cw // level
h = ch // level

mosaic2 = cv2.resize(mosaic1, (w, h), interpolation=cv2.INTER_LINEAR)
mosaic3 = cv2.resize(mosaic2, (cw, ch), interpolation=cv2.INTER_NEAREST)

image[y : y + ch, x : x + cw] = mosaic3  # 將圖片的剪裁區域，換成馬賽克的圖

cv2.rectangle(image, (x, y), (x + cw, y + ch), RED, 3)

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

"""
    level = 15  # 馬賽克程度
    mh = int(h / level)  # 根據馬賽克程度縮小的高度
    mw = int(w / level)  # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)  # 先縮小
    mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)  # 然後放大

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
rotate
#图像旋转 ： cv2.ROTATE_180  cv2.ROTATE_90_COUNTERCLOCKWISE
cv2.ROTATE_90_CLOCKWISE：顺时针旋转 90 度
cv2.ROTATE_180： 旋转 180 度
cv2.ROTATE_90_COUNTERCLOCKWISE：逆时针旋转 90 度
"""
image = cv2.imread(filename1, 1)

print("旋轉, 直角旋轉(3)")
image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image2 = cv2.rotate(image, cv2.ROTATE_180)  # 1
image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.figure("旋轉", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("順90")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("180")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("逆90")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

output = cv2.transpose(image)  # 逆時針旋轉 90 度

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("transpose 逆時針旋轉 90 度")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("cv2.warpAffine() 平移")

image = cv2.imread(filename1)
height, width = image.shape[0:2]  # 獲得影像大小
dsize = (width, height)  # 建立未來影像大小

xx = 30  # 平移 xx = 30
yy = 80  # 平移 yy = 80

# 建立 M 矩陣, 2x3 矩陣，x 軸平移 xx，y 軸平移 yy
M = np.float32([[1, 0, xx], [0, 1, yy]])
dst = cv2.warpAffine(image, M, dsize)  # 執行仿射

plt.figure("平移", figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("平移 (30, 80)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.warpAffine() 仿射1")

image = cv2.imread(filename1)

p1 = np.float32([[100, 100], [480, 0], [0, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360]])

M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(image, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.warpAffine() 仿射2")

image = cv2.imread(filename1)

p1 = np.float32([[100, 100], [480, 0], [0, 360], [480, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360], [480, 360]])

M = cv2.getPerspectiveTransform(p1, p2)
output = cv2.warpPerspective(image, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

# 仿射变换矩阵，缩小两倍
A1 = np.array([[0.5, 0, 0], [0, 0.5, 0]], np.float32)
d1 = cv2.warpAffine(image, A1, (W, H), borderValue=125)

# 先缩小两倍，再平移
A2 = np.array([[0.5, 0, W / 4], [0, 0.5, H / 4]], np.float32)
d2 = cv2.warpAffine(image, A2, (W, H), borderValue=125)

# 在
A4 = np.array([[math.cos(math.pi / 4), 0, 0], [math.sin(math.pi / 3), 1, 0]])
d4 = cv2.warpAffine(image, A4, (2 * W, 2 * H), borderValue=125)

plt.figure("仿射", figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(d1, cv2.COLOR_BGR2RGB))
plt.title("d1")

plt.subplot(223)
plt.imshow(cv2.cvtColor(d2, cv2.COLOR_BGR2RGB))
plt.title("d2")

plt.subplot(224)
plt.imshow(cv2.cvtColor(d4, cv2.COLOR_BGR2RGB))
plt.title("d4")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第3章：空間變換\3.2-投影變換\perspective.py

image = cv2.imread(filename1)
H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

# 将原图的四个顶点投影到一个不规则的四边形中
src = np.array([[0, 0], [W - 1, 0], [0, H - 1], [W - 1, H - 1]], np.float32)
dst = np.array([[20, 50], [W / 2, 150], [50, H / 2], [W - 40, H - 40]], np.float32)

# 计算投影矩阵
p = cv2.getPerspectiveTransform(src, dst)
# 利用计算出的投影矩阵进行头像的投影变换
r = cv2.warpPerspective(image, p, (W, H), borderValue=0)

# 显示原图和投影效果
cv2.imshow("image", image)
cv2.imshow("warpPerspective", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# 新進

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)
# H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

print("仿射 歪折 折向右")
height, width = image.shape[0:2]  # 獲得影像大小

imagep = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # image的A,B,C三個點
dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(imagep, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst1 = cv2.warpAffine(image, M, dsize)  # 執行仿射

print("仿射 歪折 折向左")
height, width = image.shape[0:2]  # 獲得影像大小
imagep = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])  # image的A,B,C三個點
dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])  # dst的A,B,C三個點
M = cv2.getAffineTransform(imagep, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst2 = cv2.warpAffine(image, M, dsize)  # 執行仿射

plt.figure("仿射", figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("仿射 歪折 折向右")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("仿射 歪折 折向左")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

image = cv2.imread(filename1)

height, width = image.shape[0:2]  # 獲得影像大小

imagep = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.2]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(imagep, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(image, M, dsize)  # 執行仿射

plt.figure("仿射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("仿射 歪折 轉置")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("仿射 歪折 轉置")

image = cv2.imread(filename1)
height, width = image.shape[0:2]  # 獲得影像大小

imagep = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
a = [0, height * 0.4]  # A
b = [width * 0.8, height * 0.2]  # B
c = [width * 0.1, height * 0.9]  # C
dstp = np.float32([a, b, c])  # dst的 A, B, C
M = cv2.getAffineTransform(imagep, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(image, M, dsize)  # 執行仿射

plt.figure("仿射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("仿射 歪折 轉置")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)
height, width = image.shape[0:2]  # 獲得影像大小

a1 = [0, 0]  # 原始影像的 A 左上
b1 = [width, 0]  # 原始影像的 B 右上
c1 = [0, height]  # 原始影像的 C 左下
d1 = [width - 1, height - 1]  # 原始影像的 D 右下
imagep = np.float32([a1, b1, c1, d1])

dd1 = 60
dd2 = 20
a2 = [dd1, 0]  # dst的 A 左上
b2 = [width - dd1, 0]  # dst的 B 右上
c2 = [0 + dd2, height - dd2]  # dst的 C 左下
d2 = [width - dd2, height - dd2]  # dst的 D 右下
dstp = np.float32([a2, b2, c2, d2])

M = cv2.getPerspectiveTransform(imagep, dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpPerspective(image, M, dsize)  # 執行透視

plt.figure("", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("顯示透視影像")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
rows, cols = image.shape
mapx = np.ones(image.shape, np.float32) * 3  # 設定 mapx
mapy = np.ones(image.shape, np.float32) * 2  # 設定 mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)

for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)  # 設定mapx
        mapy.itemset((r, c), rows - 1 - r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
rows, cols = image.shape
mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols - 1 - c)  # 設定mapx
        mapy.itemset((r, c), r)  # 設定mapy
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            mapx.itemset((r, c), 2 * (c - cols * 0.25))  # 計算對應的 x
            mapy.itemset((r, c), 2 * (r - rows * 0.25))  # 計算對應的 y
        else:
            mapx.itemset((r, c), 0)  # 取x座標為 0
            mapy.itemset((r, c), 0)  # 取y座標為 0
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)

rows, cols = image.shape[:2]
mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for r in range(rows):  # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), c)
        mapy.itemset((r, c), 2 * r)
dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

plt.figure("映射", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("執行映射")

show()

print("------------------------------------------------------------")  # 60個
# AffineTransform
# PerspectiveTransform
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

x = 50
y = 50
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.figure("影像移動", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))
plt.title("影像移動")

plt.suptitle("影像移動")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 09")

image = cv2.imread(filename_lena_gray)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.figure("仿射", figsize=(12, 8))
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

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

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
image = cv2.imread(filename3)

H, W, D = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式
h, w = image.shape[:2]
src = np.array([[0, 0], [w - 1, 0], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 300], [873, 78], [161, 923]], dtype=np.float32)

m = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(image, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(12, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(image[:, :, ::-1], alpha=0.4)
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
result = cv2.warpPerspective(image, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(12, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(image[:, :, ::-1], alpha=0.4)
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

# 撈出一層圖檔, resize 另存新檔

import glob

srcDir = "src_pic"
width = 320
height = 240

# 圖片調整成相同大小(單層)
pics = glob.glob(srcDir + "/*.jpg")

print(pics)

index = 1
for pic in pics:
    print(pic)
    img_pic = cv2.imread(pic, cv2.IMREAD_COLOR)
    img_pic_resize = cv2.resize(img_pic, (width, height))
    pic_name = "tmp_pic" + str(index) + ".jpg"
    # cv2.imwrite(pic_name, img_pic_resize)
    index += 1

print("OK")

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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個

print("A圖抓一塊貼到B圖上")
face = lena[220:400, 250:350]
peony[160:340, 200:300] = face


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import shutil

dstDir = "dst_pic"
# 刪除資料夾並重建之
if os.path.isdir(dstDir):
    shutil.rmtree(dstDir)  # 刪除資料夾
    time.sleep(3)  # 休息讓系統處理
os.mkdir(dstDir)  # 建立資料夾
