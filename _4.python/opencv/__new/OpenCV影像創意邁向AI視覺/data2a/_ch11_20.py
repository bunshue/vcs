import sys
import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個

# ch11_1.py

src = cv2.imread("hung.jpg")
dst1 = cv2.blur(src, (3, 3))  # 使用 3x3 濾波核
dst2 = cv2.blur(src, (5, 5))  # 使用 5x5 濾波核
dst3 = cv2.blur(src, (7, 7))  # 使用 7x7 濾波核
cv2.imshow("src", src)
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_2.py

src = cv2.imread("hung.jpg")
dst1 = cv2.blur(src, (29, 29))  # 使用 29x29 濾波核
cv2.imshow("src", src)
cv2.imshow("dst 29 x 29", dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_2_1.py

src = cv2.imread("hung.jpg")
dst1 = cv2.boxFilter(src, -1, (2, 2), normalize=0)  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(src, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(src, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核
cv2.imshow("src", src)
cv2.imshow("dst 2 x 2", dst1)
cv2.imshow("dst 3 x 3", dst2)
cv2.imshow("dst 5 x 5", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_3.py

src = np.ones((3, 3), np.float32) * 150
src[1, 1] = 20
print(f"src = \n {src}")
dst = cv2.medianBlur(src, 3)
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch11_4.py

src = cv2.imread("hung.jpg")
dst1 = cv2.medianBlur(src, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(src, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(src, 7)  # 使用邊長是 7 的濾波核
cv2.imshow("src", src)
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_5.py

src = cv2.imread("hung.jpg")
dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 使用 3 x 3 的濾波核
dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)  # 使用 5 x 5 的濾波核
dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)  # 使用 29 x 29 的濾波核
cv2.imshow("src", src)
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 15 x 15", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_6.py

src = cv2.imread("border.jpg")
dst1 = cv2.blur(src, (3, 3))  # 均值濾波器 - 3x3 濾波核
dst2 = cv2.blur(src, (7, 7))  # 均值濾波器 - 7x7 濾波核

dst3 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 高斯濾波器 - 3x3 的濾波核
dst4 = cv2.GaussianBlur(src, (7, 7), 0, 0)  # 高斯濾波器 - 7x7 的濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 7 x 7", dst2)
cv2.imshow("Gauss dst 3 x 3", dst3)
cv2.imshow("Gauss dst 7 x 7", dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_7.py

src = cv2.imread("hung.jpg")
dst1 = cv2.blur(src, (15, 15))  # 均值濾波器
dst2 = cv2.GaussianBlur(src, (15, 15), 0, 0)  # 高斯濾波器
dst2 = cv2.bilateralFilter(src, 15, 100, 100)  # 雙邊濾波器

cv2.imshow("src", src)
cv2.imshow("blur", dst1)
cv2.imshow("GaussianBlur", dst1)
cv2.imshow("bilateralFilter", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch11_8.py

src = cv2.imread("hung.jpg")
kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(src, -1, kernel)  # 自定義濾波器
cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_1.py

src = np.zeros((7, 7), np.uint8)
src[1:6, 1:6] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.erode(src, kernel)  # 腐蝕操作
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Erosion = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch12_10.py

src = cv2.imread("night.jpg")
kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算

cv2.imshow("src", src)
cv2.imshow("after Opening 9 x 9", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_11.py

src = cv2.imread("night.jpg")
kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核
mid = cv2.erode(src, kernel)  # erosion
dst = cv2.dilate(mid, kernel)  # dilation

cv2.imshow("src", src)
cv2.imshow("after erosion 9 x 9", mid)
cv2.imshow("after dilation 9 x 9", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_12.py

src = cv2.imread("snowman.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算

cv2.imshow("src", src)
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_13.py

src = cv2.imread("snowman1.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算

cv2.imshow("src", src)
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_14.py

src = cv2.imread("night.jpg")
kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核
mid = cv2.dilate(src, kernel)  # dilation
dst = cv2.erode(mid, kernel)  # erosion
cv2.imshow("src", src)
cv2.imshow("after dilation 9 x 9", mid)
cv2.imshow("after erosion 9 x 9", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_15.py

src = cv2.imread("k.jpg")
kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst1 = cv2.dilate(src, kernel)  # dilation
dst2 = cv2.erode(src, kernel)  # erosion
cv2.imshow("src", src)
cv2.imshow("after dilation 5 x 5", dst1)
cv2.imshow("after erosion 5 x 5", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_16.py

src = cv2.imread("k.jpg")
kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient

cv2.imshow("src", src)
cv2.imshow("after morpological gradient", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_17.py

src = cv2.imread("hole.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient

cv2.imshow("src", src)
cv2.imshow("after morpological gradient", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_18.py

src = cv2.imread("btree.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)  # tophat

cv2.imshow("src", src)
cv2.imshow("after tophat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_19.py

src = cv2.imread("snowman.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # blackhat

cv2.imshow("src", src)
cv2.imshow("after blackhat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_2.py

src = cv2.imread("bw.jpg")
kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst1 = cv2.erode(src, kernel)  # 腐蝕操作
kerne2 = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst2 = cv2.erode(src, kerne2)  # 腐蝕操作

cv2.imshow("src", src)
cv2.imshow("after erosion 5 x 5", dst1)
cv2.imshow("after erosion 11 x 11", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_20.py

src = cv2.imread("excel.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # blackhat

cv2.imshow("src", src)
cv2.imshow("after blackhat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_21.py

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(f"MORPH_RECT \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(f"MORPH_ELLIPSE \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(f"MORPH_CROSS \n {kernel}")

print("------------------------------------------------------------")  # 60個

# ch12_22.py

src = cv2.imread("bw_circle.jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (39, 39))
dst1 = cv2.dilate(src, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (39, 39))
dst2 = cv2.dilate(src, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (39, 39))
dst3 = cv2.dilate(src, kernel)

cv2.imshow("src", src)
cv2.imshow("MORPH_RECT", dst1)
cv2.imshow("MORPH_ELLIPSE", dst2)
cv2.imshow("MORPH_CROSS", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_3.py

src = cv2.imread("bw_noise.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.erode(src, kernel)  # 腐蝕操作
kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.erode(src, kerne2)  # 腐蝕操作

cv2.imshow("src", src)
cv2.imshow("after erosion 3 x 3", dst1)
cv2.imshow("after erosion 5 x 5", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_4.py

src = cv2.imread("whilster.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.erode(src, kernel)  # 腐蝕操作
kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.erode(src, kerne2)  # 腐蝕操作

cv2.imshow("src", src)
cv2.imshow("after erosion 3 x 3", dst1)
cv2.imshow("after erosion 5 x 5", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_5.py

src = np.zeros((7, 7), np.uint8)
src[2:5, 2:5] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.dilate(src, kernel)  # 膨脹操作
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Dilation = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch12_6.py

src = cv2.imread("bw_dilate.jpg")
kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst1 = cv2.dilate(src, kernel)  # 膨脹操作
kerne2 = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst2 = cv2.dilate(src, kerne2)  # 膨脹操作

cv2.imshow("src", src)
cv2.imshow("after dilation 5 x 5", dst1)
cv2.imshow("after dilation 11 x 11", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_7.py

src = cv2.imread("a.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.dilate(src, kernel)  # 膨脹操作
kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.dilate(src, kerne2)  # 膨脹操作

cv2.imshow("src", src)
cv2.imshow("after dilation 3 x 3", dst1)
cv2.imshow("after dilation 5 x 5", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_8.py

src = cv2.imread("whilster.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.dilate(src, kernel)  # 膨脹操作
kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.dilate(src, kerne2)  # 膨脹操作

cv2.imshow("src", src)
cv2.imshow("after dilation 3 x 3", dst1)
cv2.imshow("after dilation 5 x 5", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch12_9.py

src = cv2.imread("btree.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算

cv2.imshow("src", src)
cv2.imshow("after Opening 3 x 3", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_1.py

src = np.random.randint(-256, 256, size=[3, 5], dtype=np.int16)
print(f"src = \n {src}")
dst = cv2.convertScaleAbs(src)
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# ch13_2.py

src = cv2.imread("map.jpg")
dst = cv2.Sobel(src, -1, 1, 0)  # 計算 x 軸影像梯度
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_3.py

src = cv2.imread("map.jpg")
dst = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_4.py

src = cv2.imread("map.jpg")
dst = cv2.Sobel(src, -1, 0, 1)  # 計算 y 軸影像梯度
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_5.py

src = cv2.imread("map.jpg")
dst = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_6.py

src = cv2.imread("map.jpg")
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_7.py

src = cv2.imread("lena.jpg")
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
cv2.imshow("Src", src)
cv2.imshow("Dstx", dstx)
cv2.imshow("Dsty", dsty)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_8.py

# Sobel()函數
src = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Src", src)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_8_1.py

# Sobel()函數
src = cv2.imread("lena.jpg")  # 彩色讀取
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Src", src)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_9.py

# Sobel()函數
src = cv2.imread("snow.jpg")  # 彩色讀取
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

# 輸出影像梯度
cv2.imshow("Src", src)
cv2.imshow("Scharr X", dstx)
cv2.imshow("Scharr Y", dsty)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_10.py

src = cv2.imread("laplacian.jpg")
dst_tmp = cv2.Laplacian(src, cv2.CV_32F)  # Laplacian邊緣影像
dst = cv2.convertScaleAbs(dst_tmp)  # 轉換為正值
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_11.py

src = cv2.imread("geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
src = cv2.GaussianBlur(src, (3, 3), 0)  # 降低噪音
# Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F, ksize=3)  # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)  # 將負值轉正值
# 輸出影像梯度
cv2.imshow("Src", src)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)
cv2.imshow("Laplacian", dst_lap)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_12.py

src = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
dst1 = cv2.Canny(src, 50, 100)  # minVal=50, maxVal=100
dst2 = cv2.Canny(src, 50, 200)  # minVal=50, maxVal=200
cv2.imshow("Src", src)
cv2.imshow("Dst1", dst1)
cv2.imshow("Dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch13_13.py

src = cv2.imread("geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 黑白讀取
src = cv2.GaussianBlur(src, (3, 3), 0)  # 降低噪音
# Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合
# Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F, ksize=3)  # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)  # 將負值轉正值
# Canny()函數
dst_canny = cv2.Canny(src, 50, 100)  # minVal=50, maxVal=100
# 輸出影像梯度
cv2.imshow("Canny", dst_canny)
cv2.imshow("Sobel", dst_sobel)
cv2.imshow("Scharr", dst_scharr)
cv2.imshow("Laplacian", dst_lap)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_1.py

src = cv2.imread("macau.jpg")  # 讀取影像
dst1 = cv2.pyrDown(src)  # 第 1 次向下採樣
dst2 = cv2.pyrDown(dst1)  # 第 2 次向下採樣
dst3 = cv2.pyrDown(dst2)  # 第 3 次向下採樣
print(f"src.shape = {src.shape}")
print(f"dst1.shape = {dst1.shape}")
print(f"dst2.shape = {dst2.shape}")
print(f"dst3.shape = {dst3.shape}")

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_2.py

src = cv2.imread("macau_small.jpg")  # 讀取影像
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

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_3.py

src1 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
src2 = np.random.randint(256, size=(2, 3), dtype=np.uint8)
dst = src1 + src2
print(f"src1 = \n{src1}")
print(f"src2 = \n{src2}")
print(f"dst = \n{dst}")

print("------------------------------------------------------------")  # 60個

# ch14_4.py

src = cv2.imread("pengiun.jpg")  # 讀取影像
dst1 = src + src  # 影像相加
dst2 = src - src  # 影像相減
cv2.imshow("src", src)
cv2.imshow("dst1 - add", dst1)
cv2.imshow("dst2 - subtraction", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_5.py

src = cv2.imread("pengiun.jpg")  # 讀取影像
print(f"原始影像大小 = \n{src.shape}")
dst_down = cv2.pyrDown(src)  # 向下採樣
print(f"向下採樣大小 = \n{dst_down.shape}")
dst_up = cv2.pyrUp(dst_down)  # 向上採樣, 復原大小
print(f"向上採樣大小 = \n{dst_up.shape}")
dst = dst_up - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("src", src)
cv2.imshow("dst1 - recovery", dst_up)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_6.py

src = cv2.imread("pengiun.jpg")  # 讀取影像
print(f"原始影像大小 = \n{src.shape}")
dst_up = cv2.pyrUp(src)  # 向上採樣
print(f"向上採樣大小 = \n{dst_up.shape}")
dst_down = cv2.pyrDown(dst_up)  # 向下採樣, 復原大小
print(f"向下採樣大小 = \n{dst_down.shape}")
dst = dst_down - src
print(f"結果影像大小 = \n{dst.shape}")

cv2.imshow("src", src)
cv2.imshow("dst1 - recovery", dst_down)
cv2.imshow("dst2 - dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_7.py

src = cv2.imread("pengiun.jpg")  # 讀取影像
G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
G2 = cv2.pyrDown(G1)  # 第 2 次向下採樣

L0 = G0 - cv2.pyrUp(G1)  # 建立第 0 層拉普拉斯金字塔
L1 = G1 - cv2.pyrUp(G2)  # 建立第 1 層拉普拉斯金字塔
print(f"L0.shape = \n{L0.shape}")  # 列印第 0 層拉普拉斯金字塔大小
print(f"L1.shape = \n{L1.shape}")  # 列印第 1 層拉普拉斯金字塔大小
cv2.imshow("Laplacian L0", L0)  # 顯示第 0 層拉普拉斯金字塔
cv2.imshow("Laplacian L1", L1)  # 顯示第 1 層拉普拉斯金字塔

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch14_8.py

src = cv2.imread("pengiun.jpg")  # 讀取影像
G0 = src
G1 = cv2.pyrDown(G0)  # 第 1 次向下採樣
L0 = src - cv2.pyrUp(G1)  # 拉普拉斯影像
dst = L0 + cv2.pyrUp(G1)  # 恢復結果影像

print(f"src.shape = \n{src.shape}")  # 列印原始影像大小
print(f"dst.shape = \n{dst.shape}")  # 列印恢復影像大小
cv2.imshow("Src", src)  # 顯示原始影像
cv2.imshow("Dst", dst)  # 顯示恢復影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_1.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_1_1.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
cv2.imshow("src1", src)  # 再輸出一次原始影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_2.py

src = cv2.imread("easy.jpg")
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print(f"資料類型      : {type(contours)}")
print(f"輪廓數量      : {len(contours)}")

print("------------------------------------------------------------")  # 60個

# ch15_3.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
imgList = []  # 建立輪廓串列
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    imgList.append(img)  # 將預設黑底影像加入串列
    # 繪製輪廓影像
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow("contours" + str(i), imgList[i])  # 顯示輪廓影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_4.py

src = cv2.imread("easy.jpg")
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
for i in range(n):  # 輸出輪廓的屬性
    print(f"編號 = {i}")
    print(f"輪廓點的數量 = {len(contours[i])}")
    print(f"輪廓點的外形 = {contours[i].shape}")

print("------------------------------------------------------------")  # 60個

# ch15_5.py

src = cv2.imread("easy.jpg")
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
print(contours[1])  # 列印編號1的輪廓點

print("------------------------------------------------------------")  # 60個

# ch15_6.py

src = cv2.imread("easy1.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_7.py

src = cv2.imread("easy1.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_8.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 2)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_9.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (255, 255, 255), -1)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_10.py

src = cv2.imread("lake.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", dst_binary)  # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
mask = np.zeros(src.shape, np.uint8)
dst = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)  # 繪製圖形輪廓
dst_result = cv2.bitwise_and(src, mask)
cv2.imshow("dst result", dst_result)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_11.py

src = cv2.imread("easy2.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_12.py

src = cv2.imread("easy2.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_13.py

src = cv2.imread("easy3.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_14.py

src = cv2.imread("easy3.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製圖形輪廓
cv2.imshow("result", dst)  # 顯示結果影像
print(f"列印層級 \n {hierarchy}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_15.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)  # 回傳輪廓數
imgList = []  # 建立輪廓串列
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    imgList.append(img)  # 將預設黑底影像加入串列
    # 繪製輪廓影像
    imgList[i] = cv2.drawContours(imgList[i], contours, i, (255, 255, 255), 5)
    cv2.imshow("contours" + str(i), imgList[i])  # 顯示輪廓影像

for i in range(n):  # 列印輪廓面積
    area = cv2.moments(contours[i])
    print(f"輪廓面積 str(i) = {area['m00']}")

for i in range(n):  # 列印影像矩
    M = cv2.moments(contours[i])
    print(f"列印影像矩 {str(i)} \n {M}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_16.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)  # 繪製圖形輪廓

for c in contours:  # 繪製中心點迴圈
    M = cv2.moments(c)  # 影像矩
    Cx = int(M["m10"] / M["m00"])  # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])  # 質心 y 座標
    cv2.circle(dst, (Cx, Cy), 5, (255, 0, 0), -1)  # 繪製中心點
cv2.imshow("result", dst)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_17.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.contourArea(contours[i])  # 計算輪廓面積
    print(f"輪廓 {i} 面積 = {area}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_18.py

src = cv2.imread("easy.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.arcLength(contours[i], True)  # 計算輪廓周長
    print(f"輪廓 {i} 周長 = {area}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_19.py

src = cv2.imread("heart.jpg")
cv2.imshow("src", src)  # 顯示原始影像

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
M = cv2.moments(src_gray)  # 影像矩
nu20 = M["nu20"]
print(f"歸一化中心矩 nu20 = {nu20}")
nu02 = M["nu02"]
print(f"歸一化中心矩 nu02 = {nu02}")

Hu = cv2.HuMoments(M)  # Hu矩
print(f"Hu \n {Hu}")  # 列印Hu矩

result = Hu[0][0] - (nu20 + nu02)  # 驗證Hu矩 0, h0
print(f"驗證結果 h0 - nu20 - nu02 = {result}")

print("------------------------------------------------------------")  # 60個

# ch15_20.py

src = cv2.imread("3heart.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_21.py

src = cv2.imread("3shapes.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_22.py

src = cv2.imread("myheart.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

match0 = cv2.matchShapes(contours[0], contours[0], 1, 0)  # 輪廓0和0比較
print(f"輪廓0和0比較 = {match0}")
match1 = cv2.matchShapes(contours[0], contours[1], 1, 0)  # 輪廓0和1比較
print(f"輪廓0和1比較 = {match1}")
match2 = cv2.matchShapes(contours[0], contours[2], 1, 0)  # 輪廓0和2比較
print(f"輪廓0和2比較 = {match2}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_23.py

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")
cv2.imshow("mycloud1", src1)
src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]
# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")
cv2.imshow("mycloud2", src2)
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]
# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")
cv2.imshow("explode", src3)
src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
sd = cv2.createShapeContextDistanceExtractor()  # 建立形狀場景運算子
match0 = sd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")
match1 = sd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 = sd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch15_24.py

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")
cv2.imshow("mycloud1", src1)
src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]
# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")
cv2.imshow("mycloud2", src2)
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]
# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")
cv2.imshow("explode", src3)
src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
hd = cv2.createHausdorffDistanceExtractor()  # 建立Hausdorff
match0 = hd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")
match1 = hd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 = hd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 輸出矩形格式使用元組(tuple)
rect = cv2.boundingRect(contours[0])
print(f"元組 rect = {rect}")
# 輸出矩形格式, 列出所有細項
x, y, w, h = cv2.boundingRect(contours[0])
print(f"左上角 x = {x}, 左上角 y = {y}")
print(f"矩形寬度     = {w}")
print(f"矩形高度     = {h}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_3.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_4.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

box = cv2.minAreaRect(contours[0])  # 建構最小矩形
print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)  # 獲取頂點座標
points = np.int0(points)  # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")
dst = cv2.drawContours(src, [points], 0, (0, 255, 0), 2)  # 繪製輪廓
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_5.py

src = cv2.imread("explode3.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_6.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_7.py

src = cv2.imread("cloud.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(contours[0])  # 取得最優擬合橢圓數據
print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(src, ellipse, (0, 255, 0), 2)  # 繪橢圓
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_8.py

src = cv2.imread("heart.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得三角形面積與頂點座標
area, triangle = cv2.minEnclosingTriangle(contours[0])
print(f"三角形面積   = {area}")
print(f"三角形頂點座標資料類型 = {type(triangle)}")
print(f"三角頂點座標 = \n{triangle}")
triangle = np.int0(triangle)  # 轉整數
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_9.py

src = cv2.imread("multiple.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 近似多邊形包圍
n = len(contours)  # 輪廓數量
src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
for i in range(n):
    approx = cv2.approxPolyDP(contours[i], 3, True)  # epsilon=3
    dst1 = cv2.polylines(src1, [approx], True, (0, 255, 0), 2)  # dst1
    approx = cv2.approxPolyDP(contours[i], 15, True)  # epsilon=15
    dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # dst2
cv2.imshow("dst1 - epsilon = 3", dst1)
cv2.imshow("dst2 - epsilon = 15", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_10.py

src = cv2.imread("unregular.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 擬合一條線
rows, cols = src.shape[:2]  # 輪廓大小
vx, vy, x, y = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
print(f"共線正規化向量 = {vx}, {vy}")
print(f"直線經過的點   = {x}, {y}")
lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
dst = cv2.line(src, (0, lefty), (cols - 1, righty), (0, 255, 0), 2)  # 左到右繪線
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_11.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12_1.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
print(f"凸包面積 = {convex_area}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_13.py

src = cv2.imread("hand2.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
n = len(contours)  # 輪廓數量
for i in range(n):
    hull = cv2.convexHull(contours[i])  # 獲得凸包頂點座標
    dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch16_14.py

src = cv2.imread("star.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包 -> 凸包缺陷
contour = contours[0]  # 輪廓
hull = cv2.convexHull(contour, returnPoints=False)  # 獲得凸包
defects = cv2.convexityDefects(contour, hull)  # 獲得凸包缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]
    start = tuple(contour[s][0])  # 取得startPoint座標
    end = tuple(contour[e][0])  # 取得endPoint座標
    far = tuple(contour[f][0])  # 取得farPoint座標
    dst = cv2.line(src, start, end, [0, 255, 0], 2)  # 凸包連線
    dst = cv2.circle(src, far, 3, [0, 0, 255], -1)  # 繪製farPoint
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_15.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
src1 = src.copy()  # 複製src影像
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst1 = cv2.polylines(src1, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst1", dst1)
isConvex = cv2.isContourConvex(hull)  # 是否凸形
print(f"凸包是凸形       = {isConvex}")
# 近似多邊形包圍
src2 = src.copy()  # 複製src影像
approx = cv2.approxPolyDP(contours[0], 10, True)  # epsilon=10
dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # 近似多邊形連線
cv2.imshow("dst2 - epsilon = 10", dst2)
isConvex = cv2.isContourConvex(approx)  # 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_16.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_17.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
aspectratio = w / h  # 計算寬高比
print(f"寬高比 = {aspectratio}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
print(f"資料格式 = {type(cnt)}")
print(f"資料維度 = {cnt.ndim}")
print(f"資料長度 = {len(cnt)}")
for i in range(3):  # 列印 3 個座標點
    print(cnt[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_3.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_4.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_5.py

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")

print("------------------------------------------------------------")  # 60個

# ch17_6.py

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

# ch17_7.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
left = tuple(cnt[cnt[:, :, 0].argmin()][0])  # left
right = tuple(cnt[cnt[:, :, 0].argmax()][0])  # right
top = tuple(cnt[cnt[:, :, 1].argmin()][0])  # top
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])  # bottom
print(f"最左點 = {left}")
print(f"最右點 = {right}")
print(f"最上點 = {top}")
print(f"最下點 = {bottom}")
dst = cv2.circle(src, left, 5, [0, 255, 0], -1)
dst = cv2.circle(src, right, 5, [0, 255, 0], -1)
dst = cv2.circle(src, top, 5, [0, 255, 255], -1)
dst = cv2.circle(src, bottom, 5, [0, 255, 255], -1)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_8.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print(f"Extent = {extent}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_9.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 255), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_10.py

src = cv2.imread("star1.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
dst = cv2.circle(src, (260, 110), int(ed / 2), (0, 255, 0), 3)  # 繪製圓
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_11.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個

# ch17_12.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_13.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = np.transpose(np.nonzero(dst1))
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = np.transpose(np.nonzero(dst2))
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_14.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_15.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = cv2.findNonZero(dst1)
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = cv2.findNonZero(dst2)
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_16.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(256, size=(height, width))  # 建立矩陣
print(f"矩陣內容 = \n{img}")
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# ch17_17.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask", mask)
# 在src_gray影像的mask遮罩區域找尋最大像素與最小像素值
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src_gray, mask=mask)
print(f"最小像素值 = {minVal}")
print(f"最小像素值座標 = {minLoc}")
print(f"最大像素值 = {maxVal}")
print(f"最大像素值座標 = {maxLoc}")
cv2.circle(src, minLoc, 20, [0, 255, 0], 3)  # 最小像素值用綠色圓
cv2.circle(src, maxLoc, 20, [0, 0, 255], 3)  # 最大像素值用紅色圓
# 建立遮罩未來可以顯示此感興趣的遮罩區域
mask1 = np.zeros(src.shape, np.uint8)  # 建立遮罩
mask1 = cv2.drawContours(mask1, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask1", mask1)
dst = cv2.bitwise_and(src, mask1)  # 顯示感興趣區域
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_18.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)
channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_19.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)
channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_20.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
# 在src_gray影像的mask遮罩區域計算均值
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
channels = cv2.mean(src, mask=mask)  # 計算遮罩的均值
print(channels)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_21.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)
mean, std = cv2.meanStdDev(src)  # 計算標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_1.py

src = cv2.imread("calendar.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 繪製綠色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_2.py

src = cv2.imread("lane.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
# cv2.imshow("Canny", edges)                         # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 繪製紅色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_3.py

src = cv2.imread("roadtest.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 50, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
# 繪製檢測到的直線
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 3)  # 繪製藍色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_4.py

src = cv2.imread("shapes.jpg")
cv2.imshow("src", src)
image = cv2.medianBlur(src, 5)  # 過濾雜訊
src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉成灰階
circles = cv2.HoughCircles(
    src_gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=50,
    param2=30,
    minRadius=70,
    maxRadius=200,
)
circles = np.uint(np.around(circles))  # 轉成整數
# 繪製檢測到的直線
for c in circles[0]:
    x, y, r = c
    cv2.circle(src, (x, y), r, (0, 255, 0), 3)  # 綠色繪圓外圈
    cv2.circle(src, (x, y), 2, (0, 0, 255), 2)  # 紅色繪圓中心
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch19_1.py

seq = [1, 2, 3, 4, 5]  # 像素值
times = [2, 1, 2, 1, 3]  # 出現次數
plt.plot(seq, times, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 4])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_2.py

times = [2, 1, 2, 1, 3]  # 出現次數
N = len(times)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, times, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_3.py

seq = [1, 2, 3, 4, 5]  # 像素值
freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
plt.plot(seq, freq, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 0.5])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Frequency")  # 出現頻率
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_4.py

freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
N = len(freq)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, freq, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Freqency")  # 出現頻率
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_5.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_6.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
plt.hist(src.ravel(), 20)  # 降維再繪製直方圖
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_7.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
print(f"資料內容 \n{hist}")

print("------------------------------------------------------------")  # 60個

# ch19_8.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src], [0], None, [256], [0, 258])  # 直方圖統計資料
plt.plot(hist)  # 用plot()繪直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_9.py

src = cv2.imread("macau.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)
b = cv2.calcHist([src], [0], None, [256], [0, 256])  # B 通道統計資料
g = cv2.calcHist([src], [1], None, [256], [0, 256])  # G 通道統計資料
r = cv2.calcHist([src], [2], None, [256], [0, 256])  # R 通道統計資料
plt.plot(b, color="blue", label="B channel")  # 用plot()繪 B 通道
plt.plot(g, color="green", label="G channel")  # 用plot()繪 G 通道
plt.plot(r, color="red", label="R channel")  # 用plot()繪 R 通道
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_10.py

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_11.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)  # And運算
cv2.imshow("After Mask", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_12.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
plt.plot(hist, color="blue", label="Src Image")  # 用plot()繪影像直方圖
plt.plot(hist_mask, color="red", label="Mask")  # 用plot()繪遮罩直方圖
plt.legend(loc="best")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_13.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
# 建立遮罩
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
aftermask = cv2.bitwise_and(src, src, mask=mask)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
# subplot()第一個 2 是代表垂直有 2 張圖, 第二個 2 是代表左右有 2 張圖
# subplot()第三個參數是代表子圖編號
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.imshow(mask, "gray")  # 灰階顯示第2張圖
plt.subplot(223)  # 建立子圖 3
plt.imshow(aftermask, "gray")  # 灰階顯示第3張圖
plt.subplot(224)  # 建立子圖 4
plt.plot(hist, color="blue", label="Src Image")
plt.plot(hist_mask, color="red", label="Mask")
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_14.py

src = cv2.imread("snow1.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_15.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_16.py

src = cv2.imread("highway1.png", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_17.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)
(b, g, r) = cv2.split(src)  # 拆開彩色影像通道
blue = cv2.equalizeHist(b)  # 均衡化 B 通道
green = cv2.equalizeHist(g)  # 均衡化 G 通道
red = cv2.equalizeHist(r)  # 均衡化 R 通道
dst = cv2.merge((blue, green, red))  # 合併通道
cv2.imshow("Dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_18.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
equ = cv2.equalizeHist(src)  # 直方圖均衡化
cv2.imshow("euualizeHist", equ)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_19.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
dst = clahe.apply(src)  # 灰度影像與clahe物件關聯
cv2.imshow("CLAHE", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_1.py

src = cv2.imread("macau_hotel.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)  # 顯示原始影像
H, W = src.shape[:2]
print(f"原始影像高 H = {H}, 寬 W = {W}")
temp1 = cv2.imread("head.jpg")
cv2.imshow("Temp1", temp1)  # 顯示模板影像
h, w = temp1.shape[:2]
print(f"模板影像高 h = {h}, 寬 w = {w}")
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_2.py

src = cv2.imread("shapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)  # 顯示原始影像
temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_3.py

src = cv2.imread("g5.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("face1.jpg", cv2.IMREAD_COLOR)
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_4.py

src = []  # 建立原始影像陣列
src1 = cv2.imread("knight0.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列
src2 = cv2.imread("knight1.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列
temp1 = cv2.imread("knight.jpg", cv2.IMREAD_COLOR)
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
minValue = 1  # 設定預設的最小值
index = -1  # 設定最小值的索引
# 採用歸一化平方匹配法
for i in range(len(src)):
    result = cv2.matchTemplate(src[i], temp1, cv2.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if minValue > minVal:
        minValue = minVal  # 紀錄目前的最小值
        index = i  # 紀錄目前的索引
seq = "knight" + str(index) + ".jpg"
print(f"{seq} 比較類似")
cv2.imshow("Dst", src[index])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_5.py

src = cv2.imread("mutishapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)  # 顯示原始影像
temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(
                src, (col, row), (col + width, row + height), (0, 255, 0), 3
            )
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_6.py

src = cv2.imread("baidu.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("mountain_mark.jpg", cv2.IMREAD_COLOR)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (0, 0, 255), 3)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch20_7.py

start_x = 450  # 目前位置 x
start_y = 180  # 目前位置 y
src = cv2.imread("airport.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("airport_mark.jpg", cv2.IMREAD_COLOR)
dst = cv2.circle(src, (start_x, start_y), 10, (255, 0, 0), -1)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (255, 0, 0), 2)
            ul_x.append(col)  # 加入最佳匹配串列 x
            ul_y.append(row)  # 加入最佳匹配串列 y
# 計算目前位置到台北機場的距離
sub_x = start_x - ul_x[0]  # 計算 x 座標差距
sub_y = start_y - ul_y[0]  # 計算 y 座標差距
start_taipei = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到台北機場的距離 = {start_taipei:8.2f}")
# 計算目前位置到桃園機場的距離
sub_x = start_x - ul_x[1]  # 計算 x 座標差距
sub_y = start_y - ul_y[1]  # 計算 y 座標差距
start_taoyuan = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到桃園機場的距離 = {start_taoyuan:8.2f}")
# 計算最短距離
if start_taipei > start_taoyuan:  # 距離比較
    cv2.line(src, (start_x, start_y), (ul_x[0], ul_y[0]), (255, 0, 0), 2)
else:
    cv2.line(src, (start_x, start_y), (ul_x[1], ul_y[1]), (255, 0, 0), 2)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_8.py


def myMatch(image, tmp):
    """執行匹配"""
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像
temps = []
temp1 = cv2.imread("heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp1)  # 加入匹配串列temps
temp2 = cv2.imread("star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp2)  # 加入匹配串列temps
match = []  # 符合匹配的圖案
for t in temps:
    myMatch(src, t)  # 調用 myMatch
for img in match:
    dst = cv2.rectangle(src, (img[0]), (img[1]), (0, 255, 0), 1)  # 繪外框
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
