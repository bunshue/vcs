# ch12_1.py
import cv2
import numpy as np

src = np.zeros((7, 7), np.uint8)
src[1:6, 1:6] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.erode(src, kernel)  # 腐蝕操作
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Erosion = \n {dst}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_10.py

# ch12_10.py
import cv2
import numpy as np

src = cv2.imread("night.jpg")
kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算

cv2.imshow("src", src)
cv2.imshow("after Opening 9 x 9", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_11.py

# ch12_11.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_12.py

# ch12_12.py
import cv2
import numpy as np

src = cv2.imread("snowman.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算

cv2.imshow("src", src)
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_13.py

# ch12_13.py
import cv2
import numpy as np

src = cv2.imread("snowman1.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算

cv2.imshow("src", src)
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_14.py

# ch12_14.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_15.py

# ch12_15.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_16.py

# ch12_16.py
import cv2
import numpy as np

src = cv2.imread("k.jpg")
kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient

cv2.imshow("src", src)
cv2.imshow("after morpological gradient", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_17.py

# ch12_17.py
import cv2
import numpy as np

src = cv2.imread("hole.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient

cv2.imshow("src", src)
cv2.imshow("after morpological gradient", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_18.py

# ch12_18.py
import cv2
import numpy as np

src = cv2.imread("btree.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)  # tophat

cv2.imshow("src", src)
cv2.imshow("after tophat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_19.py

# ch12_19.py
import cv2
import numpy as np

src = cv2.imread("snowman.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # blackhat

cv2.imshow("src", src)
cv2.imshow("after blackhat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_2.py

# ch12_2.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_20.py

# ch12_20.py
import cv2
import numpy as np

src = cv2.imread("excel.jpg")
kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核
dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # blackhat

cv2.imshow("src", src)
cv2.imshow("after blackhat", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_21.py

# ch12_21.py
import cv2
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(f"MORPH_RECT \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(f"MORPH_ELLIPSE \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(f"MORPH_CROSS \n {kernel}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_22.py

# ch12_22.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_3.py

# ch12_3.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_4.py

# ch12_4.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_5.py

# ch12_5.py
import cv2
import numpy as np

src = np.zeros((7, 7), np.uint8)
src[2:5, 2:5] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.dilate(src, kernel)  # 膨脹操作
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Dilation = \n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_6.py

# ch12_6.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_7.py

# ch12_7.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_8.py

# ch12_8.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch12\ch12_9.py

# ch12_9.py
import cv2
import numpy as np

src = cv2.imread("btree.jpg")
kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)  # 開運算

cv2.imshow("src", src)
cv2.imshow("after Opening 3 x 3", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
