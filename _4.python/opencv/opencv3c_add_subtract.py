"""

cv2.add
cv2.addWeighted
cv2.subtract


"""
from opencv_common import *


ESC = 27

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/_data/picture_add1.bmp"
filename2 = "C:/_git/vcs/_4.python/_data/picture_add2.bmp"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

print("兩圖直接相加")
result1 = image1 + image2

print("兩圖用cv相加")
result2 = cv2.add(image1, image2)

print("兩圖做比例疊加 左1.0 右1.0")
result3 = cv2.addWeighted(image1, 1.0, image2, 1.0, 0)  # 0 為墊高值

plt.figure(
    num="相加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("兩圖直接相加")
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("兩圖用cv相加")
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("兩圖做比例疊加 左1.0 右1.0")
plt.imshow(cv2.cvtColor(result3, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dollar.bmp"

# 檔案 => cv2影像
lena = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/boat.bmp"

# 檔案 => cv2影像
dollar = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="疊加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

print("兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之")
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[160:340, 200:300] = add

plt.subplot(133)
plt.title("兩圖擷取某塊做alpha疊加, 再貼回原圖")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
show()

print("------------------------------------------------------------")  # 60個

print("OpenCV_12 addWeighted 要一樣大的圖")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

output = cv2.addWeighted(image1, 1.0, image2, 1.0, 100)  # 整體墊高100

cvshow("image", output)

print("------------------------------------------------------------")  # 60個

print("測試 淡入淡出 效果")
print("按 ESC 離開")

# 檔案 => cv2影像
image = cv2.imread(filename)  # 開啟圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = image.shape[1]  # 取得寬度
h = image.shape[0]  # 取得高度
white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 建立白色圖
a = 1  # 一開始 a 為 1

while True:
    a = a - 0.001  # a 不斷減少 0.001
    if a < 0:
        a = 0  # a最小為0
    output = cv2.addWeighted(white, a, image, 1 - a, 0)  # 根據 a 套用權重
    cv2.imshow("image", output)  # 顯示圖片
    k = cv2.waitKey(1)
    if k == ESC:
        break

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("兩圖相減")

filename1 = "data/_compare/compare1.jpg"
filename2 = "data/_compare/compare2.jpg"
# filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
# filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

# image3 = math.fabs(image1-image2)
image3 = image1 - image2

image4 = cv2.subtract(image1, image2)  # 相減

fig = plt.figure(
    num="兩圖相減1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減1")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減2")

show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = cv2.add(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 灰階/彩色影像相加, 變得更白/更亮
# 用相加的，像素值會破表

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
# img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony0", img)

res = cv2.add(img, img)
cv2.imshow("Peony_by_cv2.add", res)

res2 = img + img
cv2.imshow("Peony_by_+", res2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

value = 60  # 亮度調整值
img = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("Elephant1", img)

coff = np.ones(img.shape, dtype=np.uint8) * value
res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("Elephant2", res)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 像素質直接相加會破表

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = src1 + src2
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

b = np.zeros((height, width, 3), np.uint8)  # b影像
g = np.zeros((height, width, 3), np.uint8)  # g影像
r = np.zeros((height, width, 3), np.uint8)  # r影像
b[:, :, 0] = 255  # 設定藍色
g[:, :, 1] = 255  # 設定綠色
r[:, :, 2] = 255  # 設定紅色

img1 = cv2.add(b, g)  # b + g影像
img2 = cv2.add(g, r)  # g + r影像
img3 = cv2.add(img1, r)  # b + g + r影像

plt.subplot(231)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B+G")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G+R")
plt.axis("off")

plt.subplot(236)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B+G+R")
plt.axis("off")

show()

""" size error
# 製作mask
# mask = np.zeros((4, 5), dtype=np.uint8)
mask = np.zeros((height, width, 3), np.uint8)
mask[100:300, 100:, -1] = 255  # 設定mask, 先高後寬

img4 = cv2.add(b, g, mask=mask)  # b + g影像 + mask

cv2.imshow("img4", img4)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 影像相加 影像取mask

img1 = np.ones((4, 5), dtype=np.uint8) * 8
img2 = np.ones((4, 5), dtype=np.uint8) * 9

# 製作mask
mask = np.zeros((4, 5), dtype=np.uint8)
mask[1:3, 1:4] = 255  # 設定mask, 先高後寬

print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)

dst = cv2.add(img1, img2, mask=mask)
print("結果值 dst =\n", dst)

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

img1 = np.zeros((height, width, 3), np.uint8)  # 建立img1影像
img1[:, :, 2] = 255  # 紅色

img2 = np.zeros((height, width, 3), np.uint8)  # 建立img2影像
img2[:, :, 1] = 255  # 綠色

# 製作mask
m = np.zeros((height, width, 1), np.uint8)  # 建立mask(m)影像
m[50:350, 100:300, :] = 255  # 建立 ROI, 白色

# 使用cv2.add相加
img3 = cv2.add(img1, img2)  # 不含mask的影像相加

# 使用cv2.add相加, 使用mask
img4 = cv2.add(img1, img2, mask=m)  # 含mask的影像相加

plt.subplot(231)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(m, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("mask")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G by cv2.add")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G+mask by cv2.add")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# 加權和 alpha beta gamma

# 全 10 影像
src1 = np.ones((2, 3), dtype=np.uint8) * 10
print(f"src1 = \n {src1}")

# 全 50 影像
src2 = np.ones((2, 3), dtype=np.uint8) * 50
print(f"src2 = \n {src2}")

alpha = 1
beta = 0.5
gamma = 5
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# 要一樣大的影像才可以做 加權和 addWeighted

filename_rgb_r = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename_rgb_g = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

src1 = cv2.imread(filename_rgb_r)
src2 = cv2.imread(filename_rgb_g)

alpha = 1
beta = 0.2
gamma = 1
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和

plt.subplot(131)
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G")
plt.axis("off")

plt.suptitle("addWeighted")
show()

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
