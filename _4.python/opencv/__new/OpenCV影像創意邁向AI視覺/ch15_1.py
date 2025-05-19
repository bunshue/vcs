# ch15_1.py
import cv2

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


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_1_1.py

# ch15_1_1.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_10.py

# ch15_10.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_11.py

# ch15_11.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_12.py

# ch15_12.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_13.py

# ch15_13.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_14.py

# ch15_14.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_15.py

# ch15_15.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_16.py

# ch15_16.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_17.py

# ch15_17.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_18.py

# ch15_18.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_19.py

# ch15_19.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_2.py

# ch15_2.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_20.py

# ch15_20.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_21.py

# ch15_21.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_22.py

# ch15_22.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_23.py

# ch15_23.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_24.py

# ch15_24.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_3.py

# ch15_3.py
import cv2
import numpy as np

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_4.py

# ch15_4.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_5.py

# ch15_5.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_6.py

# ch15_6.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_7.py

# ch15_7.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_8.py

# ch15_8.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch15\ch15_9.py

# ch15_9.py
import cv2

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
