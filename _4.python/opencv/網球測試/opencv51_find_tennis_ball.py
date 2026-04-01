"""
找網球


"""
print("------------------------------------------------------------")  # 60個

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
import cv2
import numpy as np

# 讀取圖片
img = cv2.imread("leaves.jpg")

# 轉換到 HSV 色彩空間
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定義網球顏色範圍 (亮綠/黃綠)
lower_green = np.array([25, 80, 80])   # 下界
upper_green = np.array([45, 255, 255]) # 上界

# 建立遮罩
mask = cv2.inRange(hsv, lower_green, upper_green)

# 去除雜訊
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

# 找輪廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # 找最小外接圓
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    if radius > 20:  # 過小的忽略
        center = (int(x), int(y))
        radius = int(radius)
        # 在原圖上畫出網球
        cv2.circle(img, center, radius, (0,0,255), 3)
        cv2.putText(img, "Tennis Ball", (int(x)-40, int(y)-radius-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# 顯示結果
cv2.imshow("Detected Ball", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



import cv2
import numpy as np

# 讀取圖片
img = cv2.imread("leaves.jpg")

# 確認圖片是否成功讀取
if img is None:
    print("圖片讀取失敗，請確認檔案路徑")
    exit()

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 模糊處理，降低雜訊
gray = cv2.medianBlur(gray, 5)

# 使用 HoughCircles 偵測圓形
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1,              # 累積器解析度
    minDist=50,        # 圓心之間的最小距離
    param1=100,        # Canny 邊緣檢測高閾值
    param2=30,         # 圓心檢測閾值 (越小越容易檢測到假圓)
    minRadius=20,      # 最小半徑
    maxRadius=80       # 最大半徑
)

# 如果有找到圓形
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 畫出圓形
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 3)
        # 畫出圓心
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3)
        # 標示文字
        cv2.putText(img, "Tennis Ball", (i[0]-40, i[1]-i[2]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# 顯示結果
cv2.imshow("Detected Ball with HoughCircles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
