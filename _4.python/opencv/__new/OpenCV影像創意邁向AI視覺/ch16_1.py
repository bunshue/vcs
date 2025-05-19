# ch16_1.py
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


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_10.py

# ch16_10.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_11.py

# ch16_11.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_12.py

# ch16_12.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_12_1.py

# ch16_12_1.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_13.py

# ch16_13.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_14.py

# ch16_14.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_15.py

# ch16_15.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_16.py

# ch16_16.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_17.py

# ch16_17.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_2.py

# ch16_2.py
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

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_3.py

# ch16_3.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_4.py

# ch16_4.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_5.py

# ch16_5.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_6.py

# ch16_6.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_7.py

# ch16_7.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_8.py

# ch16_8.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch16\ch16_9.py

# ch16_9.py
import cv2
import numpy as np

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
