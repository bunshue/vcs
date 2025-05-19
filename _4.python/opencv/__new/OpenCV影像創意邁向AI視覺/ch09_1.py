# ch9_1.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_10.py

# ch9_10.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_11.py

# ch9_11.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_12.py

# ch9_12.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_13.py

# ch9_13.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_14.py

# ch9_14.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_15.py

# ch9_15.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_16.py

# ch9_16.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_17.py

# ch9_17.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TOZERO_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_18.py

# ch9_18.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_19.py

# ch9_19.py
import cv2
import numpy as np

thresh = 0  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.ones((3, 4), dtype=np.uint8) * 120  # 設定陣列是 120
src[0:2, 0:2] = 108  # 設定陣列區間為 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_2.py

# ch9_2.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_20.py

# ch9_20.py
import cv2

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
thresh = 127  # 定義閾值 = 127
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src - 127", dst)  # threshold = 127
thresh = 0  # 定義閾值 = 0
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Dst - Otsu", dst)  # Otsu
print(f"threshold = {ret}")

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_21.py

# ch9_21.py
import cv2

src = cv2.imread("school.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
thresh = 127  # 閾值
maxval = 255  # 定義像素最大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
# 自適應閾值計算方法為ADAPTIVE_THRESH_MEAN_C
dst_mean = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)
# 自適應閾值計算方法為ADAPTIVE_THRESH_GAUSSIAN_C
dst_gauss = cv2.adaptiveThreshold(
    src, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)
cv2.imshow("src", src)  # 顯示原始影像
cv2.imshow("THRESH_BINARY", dst)  # 顯示二值化處理影像
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", dst_mean)  # 顯示自適應閾值結果
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", dst_gauss)  # 顯示自適應閾值結果

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_22.py

# ch9_22.py
import cv2
import numpy as np

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", img)

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2**i  # 填上權重
result = np.zeros((row, column, 8), dtype=np.uint8)
for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    cv2.imshow(str(i), result[:, :, i])  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_23.py

# ch9_23.py
import cv2
import numpy as np

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
cv2.imshow("254", h7)  # 顯示像素值是254的影像
new_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_24.py

# ch9_24.py
import cv2
import numpy as np

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0
watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Copy Right", watermark)  # 顯示浮水印影像
ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)
# 浮水印影像嵌入最低有效位元是 0的原始影像
new_jk = cv2.bitwise_or(tmp_jk, wm)
cv2.imshow("New JK", new_jk)  # 顯示新影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_25.py

# ch9_25.py
import cv2
import numpy as np

jk = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("JK Hung", jk)  # 顯示原始影像

row, column = jk.shape  # 取得列高和欄寬
h7 = np.ones((row, column), dtype=np.uint8) * 254  # 建立像素值是254的影像
tmp_jk = cv2.bitwise_and(jk, h7)  # 原始影像最低有效位元是 0

watermark = cv2.imread("copyright.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original watermark", watermark)  # 顯示浮水印影像
ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

new_jk = cv2.bitwise_or(tmp_jk, wm)  # 浮水印影像嵌入原始影像
cv2.imshow("New JK", new_jk)  # 顯示新影像
# 擷取浮水印
h0 = np.ones((row, column), dtype=np.uint8)
wm = cv2.bitwise_and(new_jk, h0)
ret, dst = cv2.threshold(wm, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("result Watermark", dst)  # 顯示浮水印

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_3.py

# ch9_3.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_4.py

# ch9_4.py
import cv2

src = cv2.imread("numbers.jpg")
thresh = 127  # 閾值 = 10
maxval = 255  # 二值化的極大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow("Dst - 10", dst)  # threshold = 10

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_5.py

# ch9_5.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_6.py

# ch9_6.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_7.py

# ch9_7.py
import cv2

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = cv2.imread("jk.jpg")
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 80  # 修訂所定義的閾值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 80", dst)  # threshold = 80

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_8.py

# ch9_8.py
import cv2

src = cv2.imread("numbers.jpg")
thresh = 127  # 閾值 = 10
maxval = 255  # 二值化的極大值
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Src", src)
cv2.imshow("Dst - 127", dst)  # threshold = 127
thresh = 10  # 更改閾值 = 10
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY_INV)
cv2.imshow("Dst - 10", dst)  # threshold = 10

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch09\ch9_9.py

# ch9_9.py
import cv2
import numpy as np

thresh = 127  # 定義閾值
maxval = 255  # 定義像素最大值
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
ret, dst = cv2.threshold(src, thresh, maxval, cv2.THRESH_TRUNC)
print(f"src =\n {src}")
print(f"threshold = {ret}")
print(f"dst =\n {dst}")


print("------------------------------------------------------------")  # 60個
