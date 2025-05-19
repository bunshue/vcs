# ch20_1.py
import cv2

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


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_2.py

# ch20_2.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_3.py

# ch20_3.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_4.py

# ch20_4.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_5.py

# ch20_5.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_6.py

# ch20_6.py
import cv2

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_7.py

# ch20_7.py
import cv2
import math

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

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch20\ch20_8.py

# ch20_8.py
import cv2


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
