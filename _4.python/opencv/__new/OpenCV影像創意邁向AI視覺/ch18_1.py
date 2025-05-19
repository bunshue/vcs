# ch18_1.py
import cv2
import numpy as np

src = cv2.imread("calendar.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 繪製綠色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch18\ch18_2.py

# ch18_2.py
import cv2
import numpy as np

src = cv2.imread("lane.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
# cv2.imshow("Canny", edges)                         # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
# 繪製直線
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 繪製紅色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch18\ch18_3.py

# ch18_3.py
import cv2
import numpy as np

src = cv2.imread("roadtest.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 50, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
# 繪製檢測到的直線
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 3)  # 繪製藍色線條
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch18\ch18_4.py

# ch18_4.py
import cv2
import numpy as np

src = cv2.imread("shapes.jpg")
cv2.imshow("src", src)
image = cv2.medianBlur(src, 5)  # 過濾雜訊
src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉成灰階
circles = cv2.HoughCircles(
    src_gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=50,
    param2=30,
    minRadius=70,
    maxRadius=200,
)
circles = np.uint(np.around(circles))  # 轉成整數
# 繪製檢測到的直線
for c in circles[0]:
    x, y, r = c
    cv2.circle(src, (x, y), r, (0, 255, 0), 3)  # 綠色繪圓外圈
    cv2.circle(src, (x, y), 2, (0, 0, 255), 2)  # 紅色繪圓中心
cv2.imshow("dst", src)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
