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
