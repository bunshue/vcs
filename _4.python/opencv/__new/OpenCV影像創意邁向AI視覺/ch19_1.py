# ch19_1.py
import matplotlib.pyplot as plt

seq = [1, 2, 3, 4, 5]  # 像素值
times = [2, 1, 2, 1, 3]  # 出現次數
plt.plot(seq, times, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 4])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.show()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_10.py

# ch19_10.py
import cv2
import numpy as np

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_11.py

# ch19_11.py
import cv2
import numpy as np

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)  # And運算
cv2.imshow("After Mask", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_12.py

# ch19_12.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_13.py

# ch19_13.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_14.py

# ch19_14.py
import cv2
import matplotlib.pyplot as plt

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_15.py

# ch19_15.py
import cv2
import matplotlib.pyplot as plt

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_16.py

# ch19_16.py
import cv2
import matplotlib.pyplot as plt

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_17.py

# ch19_17.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_18.py

# ch19_18.py
import cv2

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
equ = cv2.equalizeHist(src)  # 直方圖均衡化
cv2.imshow("euualizeHist", equ)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_19.py

# ch19_19.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
dst = clahe.apply(src)  # 灰度影像與clahe物件關聯
cv2.imshow("CLAHE", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_2.py

# ch19_2.py
import matplotlib.pyplot as plt
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_3.py

# ch19_3.py
import matplotlib.pyplot as plt

seq = [1, 2, 3, 4, 5]  # 像素值
freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
plt.plot(seq, freq, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 0.5])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Frequency")  # 出現頻率
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_4.py

# ch19_4.py
import matplotlib.pyplot as plt
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_5.py

# ch19_5.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_6.py

# ch19_6.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
plt.hist(src.ravel(), 20)  # 降維再繪製直方圖
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_7.py

# ch19_7.py
import cv2

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
print(f"資料內容 \n{hist}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_8.py

# ch19_8.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src], [0], None, [256], [0, 258])  # 直方圖統計資料
plt.plot(hist)  # 用plot()繪直方圖
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch19\ch19_9.py

# ch19_9.py
import cv2
import matplotlib.pyplot as plt

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
