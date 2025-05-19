# ch17_1.py
import cv2

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


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_10.py

# ch17_10.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_11.py

# ch17_11.py
import cv2
import numpy as np

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_12.py

# ch17_12.py
import numpy as np

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_13.py

# ch17_13.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_14.py

# ch17_14.py
import cv2
import numpy as np

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_15.py

# ch17_15.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_16.py

# ch17_16.py
import cv2
import numpy as np

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(256, size=(height, width))  # 建立矩陣
print(f"矩陣內容 = \n{img}")
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_17.py

# ch17_17.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_18.py

# ch17_18.py
import cv2

src = cv2.imread("forest.png")
cv2.imshow("src", src)
channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_19.py

# ch17_19.py
import cv2

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)
channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_2.py

# ch17_2.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_20.py

# ch17_20.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_21.py

# ch17_21.py
import cv2

src = cv2.imread("forest.png")
cv2.imshow("src", src)
mean, std = cv2.meanStdDev(src)  # 計算標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_3.py

# ch17_3.py
import numpy as np

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_4.py

# ch17_4.py
import numpy as np

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_5.py

# ch17_5.py
import numpy as np

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_6.py

# ch17_6.py
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_7.py

# ch17_7.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_8.py

# ch17_8.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch17\ch17_9.py

# ch17_9.py
import cv2

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
