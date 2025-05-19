# ch11_1.py
import cv2

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


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_2.py

# ch11_2.py
import cv2

src = cv2.imread("hung.jpg")
dst1 = cv2.blur(src, (29, 29))  # 使用 29x29 濾波核
cv2.imshow("src", src)
cv2.imshow("dst 29 x 29", dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_2_1.py

# ch11_2_1.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_3.py

# ch11_3.py
import cv2
import numpy as np

src = np.ones((3, 3), np.float32) * 150
src[1, 1] = 20
print(f"src = \n {src}")
dst = cv2.medianBlur(src, 3)
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_4.py

# ch11_4.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_5.py

# ch11_5.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_6.py

# ch11_6.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_7.py

# ch11_7.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch11\ch11_8.py

# ch11_8.py
import cv2
import numpy as np

src = cv2.imread("hung.jpg")
kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(src, -1, kernel)  # 自定義濾波器
cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
