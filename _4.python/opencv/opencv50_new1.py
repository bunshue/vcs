"""
opencv 集合 新進1

"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 01")
print("練習組合成一張大圖 picasa效果")

add_filename1 = "C:/_git/vcs/_4.python/_data/elephant.jpg"
add_filename2 = "C:/_git/vcs/_4.python/_data/bear.jpg"
add_filename3 = "C:/_git/vcs/_4.python/_data/panda.jpg"

image1 = cv2.imread(add_filename1)
image2 = cv2.imread(add_filename2)
image3 = cv2.imread(add_filename3)

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
print("------------------------------------------------------------")  # 60個

print("opencv 02")
lena_color_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
)
image1 = cv2.imread(lena_color_filename)

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
lena_color_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
)
o = cv2.imread(lena_color_filename)

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
print("------------------------------------------------------------")  # 60個

print("opencv 04")

lena_color_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
)
o = cv2.imread(lena_color_filename)

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

print("opencv 27")

image = cv2.imread(filename1)

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
print("------------------------------------------------------------")  # 60個

print("opencv 34")
filename1t = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2t = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

bg = cv2.imread(filename1t, cv2.IMREAD_UNCHANGED)  # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA

image = cv2.imread(filename2t, cv2.IMREAD_UNCHANGED)  # 開啟圖片
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

print("opencv 37")

image1 = cv2.imread(filename_lena_color)
image2 = cv2.imread(filename_lena_gray)

h, w = image1.shape[:2]

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

mona = cv2.imread(filename1)

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

image = cv2.imread(filename2)


# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c / 100 + 1) - c + b  # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output


contrast = 0  # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值

cv2.imshow("Image", image)

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
    cv2.imshow("Image", show_image)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 89 將一彩圖做RGB分離")

rgb512_filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(rgb512_filename, cv2.IMREAD_COLOR)

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

plt.subplot(131)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B")

plt.subplot(132)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G")

plt.subplot(133)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 91")

temp = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
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
print("------------------------------------------------------------")  # 60個

print("opencv 92")
"""
#例外的寫法
img = cv2.imread("digits.png", 0)
if img is None:
    raise Exception("we need the digits.png image from samples/data here !")
"""

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
    ax.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
    ax.axis("off")
    ax.set_title("${}$".format(get_latex(expr)))

fig.subplots_adjust(0, 0, 1, 1, 0.02, 0)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 101")

# 使用remap()實現圖形拖曳效果
# 從 (tx,ty) 拖曳到 (sx,sy)

filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
img = cv2.imread(filename3)

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

plt.subplot(121)
cv2.circle(img, (tx, ty), 3, RED, 2)  # 畫圓
cv2.circle(img, (sx, sy), 3, GREEN, 2)  # 畫圓
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")

plt.subplot(122)
cv2.circle(img2, (tx, ty), int(r), RED, 2)  # 畫圓
cv2.circle(img2, (sx, sy), int(r), BLACK, 2)  # 畫圓
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示

"""
plt.Circle((tx, ty), r, fill=None, alpha=0.5, lw=2, ls="dashed")
# plt.add_artist(circle)
plt.Circle((sx, sy), r, fill=None, alpha=0.5, lw=2, color="black")
# plt.add_artist(circle)
"""
plt.axis("off")

plt.title("xxxx效果")

show()

"""
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

ax.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
circle = plt.Circle((tx, ty), r, fill=None, alpha=0.5, lw=2, ls="dashed")
ax.add_artist(circle)
circle = plt.Circle((sx, sy), r, fill=None, alpha=0.5, lw=2, color="black")
ax.add_artist(circle)
ax.axis("off")

show()
"""

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
ax1.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
ax2.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
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

filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
img_gray1 = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)

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

# 建立 500 X 500 之白圖
width, height = 305, 400  # 影像寬, 影像高
img = np.ones((height, width, 3), dtype=np.uint8) * 255
# img = cv2.imread(filename1)

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

print("opencv 117")

cv_img = cv2.imread(filename1)
width = cv_img.shape[1]
height = cv_img.shape[0]
print(width)
print(height)

img = Image.open(filename1)

mask = np.zeros([10, 5, 3], dtype=np.uint8)
# print(mask)
occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)

# print(mask)

# mask[:, :, i] = mask[:, :, i] * occlusion
# occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 圖形處理 二維卷積 使用filter2D()製作的各種圖形處理效果

用不同的卷积核可以得到 各种不同的图像处理效果。
OpenCV提供了 filter2D()来完成图像的卷积运算，调用方式如下：
filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
    anchor参数指定卷积核的锚点位置，当它为默认值(-1，-1)时， 以卷积核的中心为锚点
使用filter2D()制作的各种图像处理效果
"""

filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
src = cv2.imread(filename3)

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
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel1_name)

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel2_name)

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel3_name)

show()

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

# 讀取某點的灰階/RGB值

pt_y = 169
pt_x = 118

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點

print(type(px))
print(f"BGR = {px}")

img = cv2.imread(filename1)
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)

blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 修改影像的RGB值

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)
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

img = cv2.imread(filename1)
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

img = cv2.imread(filename1)
cv2.imshow("Peony", img)

# ROI大小區塊建立馬賽克
w, h = 100, 70
face = np.random.randint(0, 256, size=(h, w, 3))  # 馬賽克效果
img[30 : 30 + h, 180 : 180 + w] = face  # ROI, 先高後寬
cv2.imshow("Face", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

big = cv2.imread(filename2)  # 大圖

small = cv2.imread(filename1)  # 小圖

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


print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 ST
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

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

src = cv2.imread("data/tmp1/hung.jpg")

mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)

""" NG
maskpict = cv2.imread("data/tmp1/hung_mask.jpg")
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

filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
src = cv2.imread(filename3)

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
filename1p = "C:/_git/vcs/_4.python/_data/penguin3.jpg"
filename2p = "C:/_git/vcs/_4.python/_data/penguin4.jpg"
output_filename = "tmp_penguin_all.jpg"
filenames = [filename1p, filename2p]
"""

filename1p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF1.jpg"
filename2p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF2.jpg"
filename3p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF3.jpg"
filename4p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF4.jpg"
filename5p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF5.jpg"
filename6p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF6.jpg"
filename7p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF7.jpg"
filename8p = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF8.jpg"
output_filename = "tmp_SF_all.jpg"
filenames = [
    filename1p,
    filename2p,
    filename3p,
    filename4p,
    filename5p,
    filename6p,
    filename7p,
    filename8p,
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

# 檔案 => cv2影像
image = cv2.imread(filename2)

roi = cv2.selectROI("image", image)
print("選取區域 :", roi)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.selectROI SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# Two Frames ST
print("------------------------------------------------------------")  # 60個

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/billiards_video.avi"

cap = cv2.VideoCapture(video_filename)  # 開啟影片

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
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

        if frameNum >= 2:  # 第2張圖以後
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
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
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
    else:
        print("播放結束")
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# Two Frames SP
print("------------------------------------------------------------")  # 60個

"""
#GaussianBlur
#Canny
"""


def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階
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
        cv2.line(img, (x1, y1), (x2, y2), RED, 3)  # 繪製直線
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

filename_road = "C:/_git/vcs/_4.python/opencv/data/_Hough/road.jpg"

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename_road)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

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

img = cv2.imread(filename_road)

edge = get_edge(img)  # Canny邊緣檢測

cv2.imshow("Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("顯示邊緣圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename_road)

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

img = cv2.imread(filename_road)

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

img = cv2.imread(filename_road)

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

img = cv2.imread(filename_road)

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
video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/road.mp4"

capture = cv2.VideoCapture(video_filename)  # 建立 VideoCapture 物件

if capture.isOpened():
    while True:
        sucess, img = capture.read()
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

# 影像對比與亮度調整
import matplotlib.image as img


# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(image, alpha=1.0, beta=0.0):
    array_alpha = np.array([alpha])  # 對比度
    array_beta = np.array([beta])  # 亮度
    image = cv2.add(image, array_beta)
    image = cv2.multiply(image, array_alpha)
    image = np.clip(image, 0, 255)
    return image


plt.figure(figsize=(12, 8))

image = cv2.imread(filename1)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

modified_image = modify_contrast_and_brightness(image, 1.5, 10.0)

plt.subplot(122)
plt.imshow(cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB))
plt.title("影像對比與亮度調整")

plt.suptitle("影像對比與亮度調整")
show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

rgb_filename = "C:/_git/vcs/_4.python/opencv/data/rgb256X300.bmp"
rgb_filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(rgb_filename)

plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

"""same
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
"""

b, g, r = cv2.split(image)

print(image.shape)
# print(image)

print(b.shape)
# print(b)

print(g.shape)
# print(g)

print(r.shape)
# print(r)

print("顯示 ch2 紅 通道 圖")
plt.subplot(334)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("紅 第2通道")

print("顯示 ch1 綠 通道 圖")
plt.subplot(335)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("綠 第1通道")

print("顯示 ch0 藍 通道 圖")
plt.subplot(336)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("藍  第0通道")

print("設定第2通道為0")
image[:, :, 2] = 0
plt.subplot(337)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("設定第2通道為0")

print("再設定第1通道為0")
image[:, :, 1] = 0
plt.subplot(338)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第1通道為0")

print("再設定第0通道為0")
image[:, :, 0] = 0
plt.subplot(339)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第0通道為0")

plt.suptitle("將一圖分解成 藍 綠 紅 三通道")
show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

rgb_filename = "C:/_git/vcs/_4.python/opencv/data/rgb256X300.bmp"
rgb_filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

image = cv2.imread(rgb_filename)

b, g, r = cv2.split(image)

bgr = cv2.merge([b, g, r])
rgb = cv2.merge([r, g, b])

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))  # 照BGR排列 OK
plt.title("B-G-R OK")

plt.subplot(233)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))  # 照RGB排列 錯相
plt.title("R-G-B NG")

plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R分量")

plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G分量")

plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B分量")

plt.suptitle("將一圖分解成 藍 綠 紅 三通道")
show()

print("------------------------------------------------------------")  # 60個

girl_filename = "images/girl.bmp"

image = cv2.imread(girl_filename)
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖BGR OK")

plt.subplot(122)
plt.imshow(cv2.cvtColor(imageRGB, cv2.COLOR_BGR2RGB))
plt.title("原圖RGB NG")

plt.suptitle("顯示結果")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

image = cv2.imread("images/8.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(222)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray_r)

plt.subplot(223)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), cmap="gray")

plt.subplot(224)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), cmap="gray_r")

plt.suptitle("灰度圖像顯示演示")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

girl_filename = "images/girl.bmp"

image = cv2.imread(girl_filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(223)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.suptitle("灰度圖像顯示演示")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

img = cv2.medianBlur(img, 7)  # 模糊化，去除雜訊
# Laplacian
output = cv2.Laplacian(img, -1, 1, 5)  # 偵測邊緣
# Sobel
output = cv2.Sobel(img, -1, 1, 1, 1, 7)  # 偵測邊緣
# Canny
output = cv2.Canny(img, 36, 36)  # 偵測邊緣

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mask = np.zeros((300, 300, 3), dtype="uint8")  # 建立 300x300 的黑色畫布
cv2.circle(mask, (150, 150), 100, WHITE, -1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)  # 進行高斯模糊

cv2.imshow("image", mask)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" TBD
mask = np.zeros((300,300,3), dtype="uint8")
cv2.circle(mask,(150,150),100, WHITE,-1)  # 畫圓
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255                          # 除以 255，計算每個像素的黑白色彩在 255 中所佔的比例

img = cv2.imread(filename1)               # 開啟圖片
bg = np.zeros((300,300,3), dtype="uint8")  # 產生一張黑色背景
bg = 255 - bg                              # 轉換成白色背景
img = img / 255                            # 除以 255，計算每個像素的色彩在 255 中所佔的比例
bg = bg / 255                              # 除以 255，計算每個像素的色彩在 255 中所佔的比例

out  = bg * (1 - mask) + img * mask        # 根據比例混合
out = (out * 255).astype("uint8")          # 乘以 255 之後轉換成整數

cv2.imshow("image", out)
cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

image = cv2.imread(filename_lena_gray)

print("filter2D 效果")
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))
plt.title("filter2D 效果")

plt.suptitle("filter2D 效果")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_barbara, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)  # 水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)  # 垂直值一樣, 偵測垂直的邊緣

print("filter2D 效果")

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))
plt.title("Prewitt_horizon")
# 躺平的書本的邊緣有被強調出來

plt.subplot(133)
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))
plt.title("Prewitt_vertical")
# 直放的書本的邊緣有被強調出來

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("製作毛玻璃效果")

img = cv2.imread(filename2)
result = img.copy()
H, W = result.shape[:2]
print(H, W)

for y in range(H - 5):
    for x in range(W - 5):
        random_num = np.random.randint(0, 5)
        result[y, x] = img[y + random_num, x + random_num]

cv2.imshow("src", img)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def salt_pepper_noise(image, fraction, salt_vs_pepper):
    img = np.copy(image)
    size = img.size
    num_salt = np.ceil(fraction * size * salt_vs_pepper).astype("int")
    num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype("int")
    row, column = img.shape

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_pepper)
    y = np.random.randint(0, row - 1, num_pepper)
    img[y, x] = 0  # 撒上胡椒

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_salt)
    y = np.random.randint(0, row - 1, num_salt)
    img[y, x] = 255  # 撒上鹽
    return img


fraction = 0.1  # 雜訊佔圖的比例
salt_vs_pepper = 0.5  # 鹽與胡椒的比例

tiger_filename = "C:/_git/vcs/_4.python/_data/tiger.jpg"

image = cv2.imread(tiger_filename, cv2.IMREAD_GRAYSCALE)
noisy = salt_pepper_noise(image, fraction, salt_vs_pepper)

plt.imshow(cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB))
plt.title("胡椒(黑)鹽(白)效果")

show()

# 黑點就好比胡椒，白點就像是鹽，這種加上雜訊的方式，就稱為椒鹽雜訊（Salt & Pepper Noise）

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def saltpepper(image, n):
    m = int((image.shape[0] * image.shape[1]) * n)
    for a in range(m):
        i = int(np.random.random() * image.shape[1])
        j = int(np.random.random() * image.shape[0])
        if image.ndim == 2:
            image[j, i] = 255
        elif image.ndim == 3:
            image[j, i, 0] = 255
            image[j, i, 1] = 255
            image[j, i, 2] = 255
    for b in range(m):
        i = int(np.random.random() * image.shape[1])
        j = int(np.random.random() * image.shape[0])
        if image.ndim == 2:
            image[j, i] = 0
        elif image.ndim == 3:
            image[j, i, 0] = 0
            image[j, i, 1] = 0
            image[j, i, 2] = 0
    return image


# 上面就是椒鹽噪聲函數，下面是使用方法，大家可以愉快的玩耍了

image0 = cv2.imread(filename_lena_gray)
image = cv2.imread(filename_lena_gray)

print("saltpepper(胡椒鹽)效果")
saltImage = saltpepper(image, 0.02)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(saltImage, cv2.COLOR_BGR2RGB))
plt.title("saltpepper(胡椒鹽)效果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("圖像平滑 salt")


# 模擬椒鹽噪聲，number 指添加椒鹽噪聲的數量
def salt(image, number):
    # 圖像的寬高
    rows, cols = image.shape
    # 加入椒鹽噪聲後的圖像
    saltImage = np.copy(image)
    for i in range(number):
        randR = random.randint(0, rows - 1)
        randC = random.randint(0, cols - 1)
        saltImage[randR][randC] = 0
    return saltImage


tiger_filename = "C:/_git/vcs/_4.python/_data/tiger.jpg"

image = cv2.imread(tiger_filename, cv2.IMREAD_GRAYSCALE)

cv2.imshow("image", image)

# 添加椒鹽噪聲
saltImage = salt(image, 2000)
cv2.imshow("saltImage", saltImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image1 = cv2.imread(filename2)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

# image2 = cv2.cvtColor(image1, 6)  # 也可以用數字對照 6 表示轉換成灰階
# 套用 medianBlur() 中值模糊
image3 = cv2.medianBlur(image2, 7)  # 模糊化，去除雜訊 7, 25 彩色黑白皆可
image4 = cv2.Canny(image3, 36, 36)  # 偵測邊緣

# 套用自適應二值化黑白影像
image5 = cv2.adaptiveThreshold(
    image3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("轉成灰階")

plt.subplot(233)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("模糊化，去除雜訊")

plt.subplot(234)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("偵測邊緣")

plt.subplot(235)
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))
plt.title("自適應二值化黑白影像")

plt.subplot(236)
plt.title("")

plt.suptitle("相加")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" ok
# cv2 製作圖像影片檔案

W, H = 180, 180

def make_image(offset, dtype="uint8"):
    W, H = 180, 180
    cx, cy = W//2, H//2
    image = np.zeros((H, W, 3), np.uint8)
    for i in range(90+30):
        # print(i, end=" ")
        # c = np.sin(((i+offset)%180)*np.pi/180)*256
        c = int(np.sin(((i+offset)%180)*np.pi/180)*256)
        cv2.circle(image, (cx, cy), i, (c, c, c), 1)  # 畫圓
    return image


def make_image(r, dtype="uint8"):
    image = np.zeros((H, W, 3), np.uint8)
    cx, cy = W // 2, H // 2
    cv2.circle(image, (cx, cy), r, RED, 1)  # 畫圓
    return image


def test_avi_output(video_filename, fourcc):
    # fourcc = cv2.FOURCC(*fourcc)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    vw = cv2.VideoWriter(video_filename, fourcc, 15, (W, H), True)
    if not vw.isOpened():
        return
    for r in range(0, 2000, 1):
        img = make_image(r)
        vw.write(img)
    vw.release()


test_avi_output("tmp_fmp4.avi", "fmp4")
# test_avi_output("tmp_x264.avi", "x264")
"""
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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 新進 與 測試

# image = image[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

print("------------------------------------------------------------")  # 60個

cvshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 存圖以比較之
# cv2.imwrite("tmp_filename.png", image)

image = cv2.imread(filenamexxx, cv2.IMREAD_GRAYSCALE)
cvshow("image", image)

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
    # font_filename = "NotoSansTC-Regular.otf"
    font = ImageFont.truetype(font_filename, 20)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)


cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), RED, 5)  # 繪製外框
putText(box[0], box[3], text, color=RED)  # 放入文字

cv2.circle(
    I, (int(circles[i][2]), int(circles[i][1])), int(circles[i][0]), (255), 2
)  # 畫圓

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

cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png

# ------------------------------------------------------------

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img = cv2.imread(filename1)  # 彩色讀取

# 影像的屬性
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

# ------------------------------------------------------------

"""
陣列垂直合併 vstack()
陣列水平合併 hstack()
"""

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
img = cv2.imread(filenamexxx, cv2.IMREAD_GRAYSCALE)
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

#cv2.imwrite("test.jpg", img) 偽寫入

read
    img = cv2.imread("car.jpg")

resize
    img_small = cv2.resize(img, (300, 100))  # 改變尺寸

save
        cv2.imwrite("small.jpg", img_small)  # 儲存影像

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

image = cv2.resize(image,(640//2,480//2))

------------------------------------------------------------

image = cv2.imread(filename2)  # 預設為彩色 1號
image = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)  # 灰階 2號
image = cv2.imread(filename2, 2)  # 也可使用數字代表模式

print(image.shape)  # 得到 shape
print(image.dtype)  # uint8

image1 = cv2.imread(filenamexx, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread("test.png", cv2.IMREAD_UNCHANGED)

print(image1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(image2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

image = cv2.imread(filenamexx, cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式

print(image.shape)                             # (400, 300, 4)  第三個數值變成 4

    # 轉換為 8 位圖，保存結果
    imageAbstraction = 255 * imageAbstraction
    imageAbstraction = np.round(imageAbstraction)
    imageAbstraction = imageAbstraction.astype(np.uint8)

"""

# 組數
numberBins = 256
histogram, bins, patch_image = plt.hist(
    histSeq, numberBins, facecolor="black", histtype="bar"
)

# 組數
numberBins = 256
histogram, bins, patch_image = plt.hist(
    histNormResultSeq, numberBins, facecolor="black", histtype="bar"
)

# 組數
numberBins = 256
histogram, bins, patch_image = plt.hist(
    histEqualResultSeq, numberBins, facecolor="black", histtype="bar"
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from os import path

fsize = path.getsize(filename)
print("size = {:07d} bytes".format(fsize))

# 將同一張圖片存成不同品質圖片

filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
img = cv2.imread(filename3)

for quality in [90, 60, 30]:
    cv2.imwrite(
        "tmp_lena_q{:02d}.jpg".format(quality), img, [cv2.IMWRITE_JPEG_QUALITY, quality]
    )


x1, y1 = 100, 100
x2, y2 = 300, 200
x3, y3 = 200, 300
x4, y4 = 50, 250
cnt = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])  # 必须是array数组的形式
print(cnt)
print(type(cnt))

r = 10
cv2.circle(img, (x1, y1), r, BLUE, -1)  # 畫圓
cv2.circle(img, (x2, y2), r, BLUE, -1)  # 畫圓
cv2.circle(img, (x3, y3), r, BLUE, -1)  # 畫圓
cv2.circle(img, (x4, y4), r, BLUE, -1)  # 畫圓

plt.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

img = cv2.imread(filenamexx, 0)  # 0 黑白图片；1 原色图片

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

src = cv2.imread("data/edge_detection/geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
src = cv2.GaussianBlur(src, (3, 3), 0)  # 降低噪音

# Canny()函數
dst_canny = cv2.Canny(src, 50, 100)  # minVal=50, maxVal=100

plt.imshow(cv2.cvtColor(dst_canny, cv2.COLOR_BGR2RGB))
plt.title("Canny")
