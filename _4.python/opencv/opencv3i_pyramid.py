"""
圖像金字塔
影像金字塔

pyrDown 这里的down是指图像变小，所以原始图像在金字塔的底部。
pyrUp   这里的up是指将图像的尺寸变大，所以原始图像位于图像金字塔的顶层。
"""
import cv2

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

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

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("顯示原圖")
cv2.imshow("original", o)

print("------------------------------------------------------------")  # 60個

# 连续3次进行pyrDown

print("cv2.__version__:", cv2.__version__)

img = cv2.imread(filename)
img_down = cv2.pyrDown(img, dstsize=(img.shape[1] // 2, img.shape[0] // 2))
img_down2 = cv2.pyrDown(
    img_down, dstsize=(img_down.shape[1] // 2, img_down.shape[0] // 2)
)
img_down3 = cv2.pyrDown(
    img_down2, dstsize=(img_down2.shape[1] // 2, img_down2.shape[0] // 2)
)
print("img.shape", img.shape)
print("img_down.shape", img_down.shape)
print("img_down2.shape", img_down2.shape)
print("img_down3.shape", img_down3.shape)
cv2.imshow("img", img)
cv2.imshow("img_down", img_down)
cv2.imshow("img_down2", img_down2)
cv2.imshow("img_down3", img_down3)

cv2.waitKey()
cv2.destroyAllWindows()

print("cv2.__version__:", cv2.__version__)

img = cv2.imread(filename)
img = cv2.resize(img, None, fx=0.15, fy=0.15)  # 为了观察方便缩小原图
img_up = cv2.pyrUp(img, dstsize=(2 * img.shape[1], 2 * img.shape[0]))
img_up2 = cv2.pyrUp(img_up, dstsize=(2 * img_up.shape[1], 2 * img_up.shape[0]))
img_up3 = cv2.pyrUp(img_up2, dstsize=(2 * img_up2.shape[1], 2 * img_up2.shape[0]))
print("img.shape", img.shape)
print("img_up.shape", img_up.shape)
print("img_up2.shape", img_up2.shape)
print("img_up3.shape", img_up3.shape)
cv2.imshow("img", img)
cv2.imshow("img_up", img_up)
cv2.imshow("img_up2", img_up2)
cv2.imshow("img_up3", img_up3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("顯示原圖")
cv2.imshow("original", o)

print("------------------------------------------------------------")  # 60個

print("顯示xxxx")
r1 = cv2.pyrDown(o)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_small.bmp"

o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
r1 = cv2.pyrUp(o)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up - o  # 構造diff圖像，查看up與o的區別
print("o.shape=", o.shape)
print("up.shape=", up.shape)
cv2.imshow("up", up)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
o = cv2.imread(filename)
print("顯示原圖")
cv2.imshow("original", o)

print("顯示xxxx")
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down - o  # 構造diff圖像，查看down與o的區別
print("o.shape=", o.shape)
print("down.shape=", down.shape)
cv2.imshow("down", down)
cv2.imshow("difference", diff)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
G0 = O
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)
print("L0.shape=", L0.shape)
print("L1.shape=", L1.shape)
print("L2.shape=", L2.shape)
cv2.imshow("L0", L0)
cv2.imshow("L1", L1)
cv2.imshow("L2", L2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
G0 = O
G1 = cv2.pyrDown(G0)
L0 = O - cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)  # 通過拉普拉斯圖像復原的原始圖像
print("O.shape=", O.shape)
print("RO.shape=", RO.shape)
result = RO - O  # 將o和ro做減法
# 計算result的絕對值，避免求和時負負為正3+(-3)=0
result = abs(result)
# 計算result所有元素的和
print("原始圖像O與恢復圖像RO差值的絕對值和：", np.sum(result))

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
O = cv2.imread(filename)
print("顯示原圖")

print("顯示xxxx")
# =================生成高斯金字塔======================
G0 = O
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
# ===============生成拉普拉斯金字塔====================
L0 = G0 - cv2.pyrUp(G1)  # 拉普拉斯金字塔第0層
L1 = G1 - cv2.pyrUp(G2)  # 拉普拉斯金字塔第1層
L2 = G2 - cv2.pyrUp(G3)  # 拉普拉斯金字塔第2層
# =================復原G0======================
RG0 = L0 + cv2.pyrUp(G1)  # 通過拉普拉斯圖像復原的原始圖像G0
print("G0.shape=", G0.shape)
print("RG0.shape=", RG0.shape)
result = RG0 - G0  # 將RG0和G0做減法
# 計算result的絕對值，避免求和時負負為正3+(-3)=0
result = abs(result)
# 計算result所有元素的和
print("原始圖像G0與恢復圖像RG0差值的絕對值和：", np.sum(result))
# =================復原G1======================
RG1 = L1 + cv2.pyrUp(G2)  # 通過拉普拉斯圖像復原G1
print("G1.shape=", G1.shape)
print("RG1.shape=", RG1.shape)
result = RG1 - G1  # 將o和ro做減法
print("原始圖像G1與恢復圖像RG1差值的絕對值和：", np.sum(abs(result)))
# =================復原G2======================
RG2 = L2 + cv2.pyrUp(G3)  # 通過拉普拉斯圖像復原G2
print("G2.shape=", G2.shape)
print("RG2.shape=", RG2.shape)
result = RG2 - G2  # 將o和ro做減法
print("原始圖像G2與恢復圖像RG2差值的絕對值和：", np.sum(abs(result)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/macau.jpg")
cv2.imshow("src", src)

dst1 = cv2.pyrDown(src)  # 第 1 次向下採樣
dst2 = cv2.pyrDown(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrDown(dst2)  # 第 3 次向下採樣
print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/macau_small.jpg")

dst1 = cv2.pyrUp(src)  # 第 1 次向下採樣
dst2 = cv2.pyrUp(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrUp(dst2)  # 第 3 次向下採樣

print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")
cv2.imshow("drc", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src1 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
src2 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
dst = src1 + src2
print(f"src1 = \n{src1}")
print(f"src2 = \n{src2}")
print(f"dst = \n{dst}")

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減

cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_down = cv2.pyrDown(src)  # 向下採樣
print(f"向下採樣大小 = \n{dst_down.shape}")
dst_up = cv2.pyrUp(dst_down)  # 向上採樣, 復原大小
print(f"向上採樣大小 = \n{dst_up.shape}")
dst = dst_up - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_up)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("src", src)

print(f"原始影像大小 = \n{src.shape}")
dst_up = cv2.pyrUp(src)  # 向上採樣
print(f"向上採樣大小 = \n{dst_up.shape}")
dst_down = cv2.pyrDown(dst_up)  # 向下採樣, 復原大小
print(f"向下採樣大小 = \n{dst_down.shape}")
dst = dst_down - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("dst1 - recovery", dst_down)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
G2 = cv2.pyrDown(G1)  # 第 2 次向下採樣

L0 = G0 - cv2.pyrUp(G1)  # 建立第 0 層拉普拉斯金字塔
L1 = G1 - cv2.pyrUp(G2)  # 建立第 1 層拉普拉斯金字塔
print(f"L0.shape = \n{L0.shape}")  # 列印第 0 層拉普拉斯金字塔大小
print(f"L1.shape = \n{L1.shape}")  # 列印第 1 層拉普拉斯金字塔大小
cv2.imshow("Laplacian L0", L0)  # 顯示第 0 層拉普拉斯金字塔
cv2.imshow("Laplacian L1", L1)  # 顯示第 1 層拉普拉斯金字塔

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("影像金字塔")

src = cv2.imread("data/pyramid/pengiun.jpg")
cv2.imshow("Src", src)

G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
L0 = src - cv2.pyrUp(G1)  # 拉普拉斯影像
dst = L0 + cv2.pyrUp(G1)  # 恢復結果影像

print(f"src.shape = \n{src.shape}")  # 列印原始影像大小
print(f"dst.shape = \n{dst.shape}")  # 列印恢復影像大小
cv2.imshow("Dst", dst)  # 顯示恢復影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
