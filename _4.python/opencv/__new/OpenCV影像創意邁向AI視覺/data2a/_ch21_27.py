# ch21_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 正黑體

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 時間值
water = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 水
sugar = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]  # 糖
grass = [4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0]  # 仙草
pearl = [3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]  # 黑珍珠
plt.plot(seq, water, "-o", label="水")  # 繪含標記的water折線圖
plt.plot(seq, sugar, "-x", label="糖")  # 繪含標記的sugar折線圖
plt.plot(seq, grass, "-s", label="仙草")  # 繪含標記的grass折線圖
plt.plot(seq, pearl, "-p", label="黑珍珠")  # 繪含標記的pearl折線圖
plt.legend(loc="best")
plt.axis([0, 12, 0, 5])  # 建立軸大小
plt.xlabel("時間軸")  # 時間軸
plt.ylabel("份數")  # 份數
plt.show()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_10.py

# ch21_10.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
# 執行逆傅立葉
idftshift = np.fft.ifftshift(dftshift)
tmp = cv2.idft(idftshift)
dst = cv2.magnitude(tmp[:, :, 0], tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊逆傅立葉圖
plt.imshow(dst, cmap="gray")  # 灰階顯示
plt.title("逆傅立葉影像")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_11.py

# ch21_11.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 低通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
mask = np.zeros((rows, cols, 2), np.uint8)
mask[row - 30 : row + 30, col - 30 : col + 30] = 1  # 設定區塊為低頻率分量是1

fshift = dftshift * mask
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("低通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.imshow(src_back)  # 顯示
plt.title("低通濾波影像")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_2.py

# ch21_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 正黑體

copies = [1, 2, 4, 3]  # 份數
N = len(copies)
x = np.arange(N)
width = 0.35
plt.bar(x, copies, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("份數")  # 份數
plt.xticks(x, ("1", "2", "3", "4"))
plt.grid(axis="y")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_3.py

# ch21_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 正黑體
plt.rcParams["axes.unicode_minus"] = False  # 可以顯示負數

start = 0
end = 1
x = np.linspace(start, end, 500)  # x 軸區間
y = np.sin(2 * np.pi * 4 * x)  # 建立正弦曲線
plt.plot(x, y)
plt.xlabel("時間(秒)")  # 時間
plt.ylabel("振幅")  # 振幅
plt.title("正弦曲線", fontsize=16)  # 標題
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_4.py

# ch21_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 正黑體

amplitude = [0, 0, 0, 1, 0, 0, 0]
N = len(amplitude)
x = np.arange(N)
width = 0.3
plt.bar(x, amplitude, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("振幅")  # 振幅
plt.xticks(x, ("1", "2", "3", "4", "5", "6", "7"))
plt.grid(axis="y")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_5.py

# ch21_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 正黑體
plt.rcParams["axes.unicode_minus"] = False  # 可以顯示負數

start = 0
# 起始時間
end = 5
# 結束時間
# 兩個正弦波的訊號頻率
freq1 = 5
# 頻率是 5 Hz
freq2 = 8
# 頻率是 8 Hz
# 建立時間軸的Numpy陣列, 用500個點
time = np.linspace(start, end, 500)
# 建立2個正弦波
amplitude1 = np.sin(2 * np.pi * freq1 * time)
amplitude2 = np.sin(2 * np.pi * freq2 * time)
# 建立子圖
figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
# 時間域的 sin 波 1
axis[0].set_title("頻率是 5 Hz的 sin 波")
axis[0].plot(time, amplitude1)
axis[0].set_xlabel("時間")
axis[0].set_ylabel("振幅")
# 時間域的 sin 波 2
axis[1].set_title("頻率是 8 Hz的 sin 波")
axis[1].plot(time, amplitude2)
axis[1].set_xlabel("時間")
axis[1].set_ylabel("振幅")
# 加總sin波
amplitude = amplitude1 + amplitude2
axis[2].set_title("2個不同頻率正弦波的結果")
axis[2].plot(time, amplitude)
axis[2].set_xlabel("時間")
axis[2].set_ylabel("振幅")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_6.py

# ch21_6.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_6_1.py

# ch21_6_1.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("shape1.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape1.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_6_2.py

# ch21_6_2.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_6_3.py

# ch21_6_3.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
# fshift = np.fft.fftshift(f)            # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(f))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_7.py

# ch21_7.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率頻率移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊逆運算圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("逆變換影像")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_8.py

# ch21_8.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 高通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
fshift[row - 30 : row + 30, col - 30 : col + 30] = 0  # 設定區塊為低頻率分量是0
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("高通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.title("高通濾波影像")
plt.imshow(src_back)  # 顯示影像
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch21\ch21_9.py

# ch21_9.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()


print("------------------------------------------------------------")  # 60個

# ch22_1.py
import cv2
import numpy as np

src = cv2.imread("coin1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_1_1.py

# ch22_1.py
import cv2
import numpy as np

src = cv2.imread("coin2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2.py

# ch22_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2_1.py

# ch22_2_1.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2_2.py

# ch22_2_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("coin1.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_3.py

# ch22_3.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
plt.subplot(141)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(142)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(143)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.subplot(144)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_4.py

# ch22_4.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(133)
plt.title("標記區")
plt.imshow(markers)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_5.py

# ch22_5.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1  # 標記修訂
markers_new[unknown == 255] = 0
plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis("off")
plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_6.py

# ch22_6.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# 正式執行分水嶺函數
dst = rgb_src.copy()
markers = cv2.watershed(dst, markers)
dst[markers == -1] = [255, 0, 0]  # 使用紅色
plt.subplot(121)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(122)
plt.title("分割結果")
plt.imshow(dst)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# ch23_1.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_2.py

# ch23_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
maskpict = cv2.imread("hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
maskpict_rgb = cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB)
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(maskpict_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_3.py

# ch23_3.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("lena.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_4.py

# ch23_4.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("lena.jpg")  # 讀取影像
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
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# ch24_1.py
import cv2
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

lisa = cv2.imread("lisaE1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


# ch24_2.py
import cv2
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

lisa = cv2.imread("lisaE2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


# ch25_1.py
import numpy as np

data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_10.py

# ch25_10.py
import numpy as np

data = np.arange(16).reshape(2, 2, 2, 2)
print(f"data = \n {data}")
print(f"data = \n {np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11.py

# ch25_11.py
import numpy as np

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.hsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_1.py

# ch25_11_1.py
import numpy as np

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)
print(f"After repeat = \n{x}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_2.py

# ch25_11_2.py
import numpy as np

data = np.array([[1, 2], [3, 4]])
print(f"data = \n {data}")
x1 = np.repeat(data, 3, axis=1)
print(f"After axis=1 repeat  = \n{x1}")
x2 = np.repeat(data, 3, axis=0)
print(f"After axis=0 repeat = \n{x2}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_3.py

# ch25_11_3.py
import numpy as np

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)[:, np.newaxis]
print(f"After repeat = \n{x}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_12.py

# ch25_12.py
import cv2
import numpy as np

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_13.py

# ch25_13.py
import cv2
import numpy as np

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")
np.savez("knn_digit.npz", train=train, train_labels=train_labels)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_14.py

# ch25_14.py
import cv2
import numpy as np

# 下載數據
with np.load("knn_digit.npz") as data:
    train = data["train"]
    train_labels = data["train_labels"]
# 讀取數字影像
test_img = cv2.imread("8.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", test_img)
img = cv2.resize(test_img, (20, 20)).reshape((1, 400))
test_data = img.astype(np.float32)  # 將資料轉成foat32
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test_data, k=5)
print(f"識別的數字是 = {int(result[0,0])}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_2.py

# ch25_2.py
import numpy as np

np.random.seed(5)
data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_3.py

# ch25_3.py
import numpy as np

data = np.random.randint(0, 10, size=(5, 1))
print(f"輸出二維陣列 = \n{data}")
print(f"轉成一維陣列 = \n{data.ravel()}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_4.py

# ch25_4.py
import numpy as np

np.random.seed(1)
trains = np.random.randint(0, 10, size=(5, 2))
print(f"列出二維陣列 \n{trains}")
np.random.seed(5)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (5, 1))
print(f"列出顏色分類陣列 \n{labels}")
# 列出 0 代表的紅色
red = trains[labels.ravel() == 0]
print(f"輸出紅色的二維陣列 \n{red}")
print(f"配對取出 \n{red[:,0], red[:,1]}")
# 列出 1 代表的藍色
blue = trains[labels.ravel() == 1]
print(f"輸出藍色的二維陣列 \n{blue}")
print(f"配對取出 \n{blue[:,0], blue[:,1]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_5.py

# ch25_5.py
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
trains = np.random.randint(0, 100, size=(num, 2))
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_6.py

# ch25_6.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
# 建立訓練數據 train, 需轉為 32位元浮點數
trains = np.random.randint(0, 100, size=(num, 2)).astype(np.float32)
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1)).astype(np.float32)
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(10)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_7.py

# ch25_7.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
# 建立 0 - 50 間的訓練數據 train0, 需轉為 32位元浮點數
train0 = np.random.randint(0, 50, (num // 2, 2)).astype(np.float32)
# 建立 50 - 100 間的訓練數據 train1, 需轉為 32位元浮點數
train1 = np.random.randint(50, 100, (num // 2, 2)).astype(np.float32)
trains = np.vstack((train0, train1))  # 合併訓練數據
# 建立分類, 未來 0 代表 red,  1 代表 blue
label0 = np.zeros((num // 2, 1)).astype(np.float32)
label1 = np.ones((num // 2, 1)).astype(np.float32)
labels = np.vstack((label0, label1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(8)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_8.py

# ch25_8.py
import numpy as np

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_9.py

# ch25_9.py
import numpy as np

data = np.arange(8).reshape(2, 2, 2)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個


# ch26_1.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_10.py

# ch26_10.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.namedWindow("myVideo", 0)
        cv2.resizeWindow("myVideo", 300, 200)
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_11.py

# ch26_11.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
print(f"Frame 的寬度 = {width}")  # 輸出Frame 的寬度
print(f"Frame 的高度 = {height}")  # 輸出Frame 的高度
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_12.py

# ch26_12.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    cv2.imshow("Frame", frame)  # 顯示影像
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    video_fps = video.get(cv2.CAP_PROP_FPS)  # 速度
    video_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # 幀數
    c = cv2.waitKey(50)  # 等待時間
    if c == 27:  # 按 Esc 键
        break
print(f"Video 的寬度    = {width}")  # 輸出 Video 的寬度
print(f"Video 的高度    = {height}")  # 輸出 Video 的高度
print(f"Video 的速度    = {video_fps}")  # 輸出 Video 的速度
print(f"Video 的幀數    = {video_frames}")  # 輸出 Video 的幀數
video.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_13.py

# ch26_13.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 設定寬度
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 設定高度
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_14.py

# ch26_14.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 影片高度
counter = 1  # 幀數計數器
font = cv2.FONT_HERSHEY_SIMPLEX  # 字型
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        y = int(height - 50)  # Frames計數器位置
        cv2.putText(
            frame, "Frames  : " + str(counter), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示幀數
        seconds = round(counter / video_fps, 2)  # 計算秒數
        y = int(height - 10)  # Seconds計數器位置
        cv2.putText(
            frame, "Seconds : " + str(seconds), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示秒數
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    counter += 1  # 幀數加 1
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_15.py

# ch26_15.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 寬度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度
# 建立裁剪影片物件
fourcc = cv2.VideoWriter_fourcc(*"I420")  # 編碼
new_video = cv2.VideoWriter("out26_15.avi", fourcc, video_fps, (width, height))
counter = video_fps * 5  # 影片長度
while video.isOpened() and counter >= 0:
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        new_video.write(frame)  # 寫入新影片
        counter -= 1  # 幀數減 1

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_2.py

# ch26_2.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像
    # 轉灰階顯示
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Frame", gray_frame)  # 顯示灰階影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_3.py

# ch26_3.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像

    h_frame = cv2.flip(frame, 1)  # 水平翻轉
    cv2.imshow("Flip Frame", h_frame)  # 顯示水平翻轉
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_4.py

# ch26_4.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 13:  # 按 Enter 鍵
        cv2.imwrite("mypict.png", frame)  # 拍照
        cv2.imshow("My Picture", frame)  # 開視窗顯示
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_5.py

# ch26_5.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MPEG-4
# 建立輸出物件
video_out = cv2.VideoWriter("out26_5.avi", fourcc, 20.0, (640, 480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        video_out.write(frame)  # 寫入影片物件
        cv2.imshow("frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
video_out.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_6.py

# ch26_6.py
import cv2

video = cv2.VideoCapture("out26_5.avi")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_7.py

# ch26_7.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_8.py

# ch26_8.py
import cv2

video = cv2.VideoCapture("iceocean2.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret == True:
        cv2.imshow("frame", frame)  # 顯示彩色影片
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray_frame", gray_frame)  # 顯示灰階影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_9.py

# ch26_9.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
        c = cv2.waitKey(50)  # 可以控制撥放速度
    else:
        break
    if c == 32:  # 是否按 空白鍵
        cv2.waitKey(0)  # 等待按鍵發生
        continue
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch27_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("jk.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_10.py

# ch27_10.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_upperbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_11.py

# ch27_11.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立雙眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_12.py

# ch27_12.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立雙眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_13.py

# ch27_13.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_lefteye_2splits.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測左眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立左眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將左眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_14.py

# ch27_14.py
import cv2

pictPath1 = r"C:\opencv\data\haarcascade_frontalface_default.xml"
pictPath2 = r"C:\opencv\data\haarcascade_righteye_2splits.xml"

face_cascade = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測右眼
eyes_cascade = cv2.CascadeClassifier(pictPath2)  # 建立右眼物件
eyes = eyes_cascade.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將右眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_15.py

# ch27_15.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalcatface.xml"
cat_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("cat1.jpg")  # 讀取影像
faces = cat_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將貓臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住貓臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_16.py

# ch27_16.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalcatface.xml"
cat_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("cat2.jpg")  # 讀取影像
faces = cat_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_17.py

# ch27_17.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_18.py

# ch27_18.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car1.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_19.py

# ch27_19.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_russian_plate_number.xml"
car_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("car2.jpg")  # 讀取影像
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌
cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_2.py

# ch27_2.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("g5.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_3.py

# ch27_3.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_3_1.py

# ch27_3_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_4.py

# ch27_4.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_4_1.py

# ch27_4_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_5.py

# ch27_5.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6.py

# ch27_6.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt_tree.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6_1.py

# ch27_6_1.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.02, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_6_2.py

# ch27_6_2.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_profileface.xml"
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_7.py

# ch27_7.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_fullbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_8.py

# ch27_8.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_fullbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people2.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch27\ch27_9.py

# ch27_9.py
import cv2

pictPath = r"C:\opencv\data\haarcascade_lowerbody.xml"
body_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識物件
img = cv2.imread("people1.jpg")  # 讀取影像
bodies = body_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體
cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
