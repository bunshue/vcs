"""




"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個

R_MIN = 0
R_MAX = 255
G_MIN = 50
G_MAX = 120
B_MIN = 50
B_MAX = 120

R_CENTER = 180
G_CENTER = 80
B_CENTER = 50

DD = 30

R_MIN = R_CENTER - DD
R_MAX = R_CENTER + DD
G_MIN = G_CENTER - DD
G_MAX = G_CENTER + DD
B_MIN = B_CENTER - DD
B_MAX = B_CENTER + DD

#                B下限 G下限 R下限
lower = np.array(
    [B_MIN, G_MIN, R_MIN]
)  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )

#                B上限 G上限 R上限
upper = np.array(
    [B_MAX, G_MAX, R_MAX]
)  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_77 抓取影像的特定顏色 設定範圍")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()
    mask = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    output = cv2.bitwise_and(img, img, mask=mask)  # 套用影像遮罩

    cv2.imshow("Original", img)
    cv2.imshow("WebCam", output)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_78")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    mask = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(mask, kernel)  # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)  # 縮小影像，還原大小

    cv2.imshow("WebCam", output)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_79")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    mask = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(mask, kernel)  # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)  # 縮小影像，還原大小

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列
    # cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    """
    # 使用 for 迴圈印出座標長相
    for contour in contours:
        print(contour)
    """

    cv2.imshow("WebCam", output)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_80")

lower = np.array([30, 40, 200])
upper = np.array([90, 100, 255])

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    mask = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(mask, kernel)  # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)  # 縮小影像，還原大小

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列
    # cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)  # 取得範圍內的面積
        # 如果面積大於 300 再標記，避免標記到背景中太小的東西
        if area > 300:
            for i in range(len(contour)):
                if i > 0 and i < len(contour) - 1:
                    # 從第二個點開始畫線
                    img = cv2.line(
                        img,
                        (contour[i - 1][0][0], contour[i - 1][0][1]),
                        (contour[i][0][0], contour[i][0][1]),
                        RED,
                        3,
                    )
                elif i == len(contour) - 1:
                    # 如果是最後一個點，與第一個點連成一線
                    img = cv2.line(
                        img,
                        (contour[i][0][0], contour[i][0][1]),
                        (contour[0][0][0], contour[0][0][1]),
                        RED,
                        3,
                    )

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_81")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    output = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列
    # cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)  # 取得座標與長寬尺寸
            img = cv2.rectangle(img, (x, y), (x + w, y + h), RED, 3)  # 繪製四邊形

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_82")

lower = np.array([30, 40, 200])
upper = np.array([90, 100, 255])

blue_lower = np.array([90, 100, 0])  # 設定藍色最低值範圍
blue_upper = np.array([200, 160, 100])  # 設定藍色最高值範圍

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()
    # img = cv2.resize(img, (640//2, 480//2))

    output = cv2.inRange(img, lower, upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列
    # cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), RED, 3)

    # 設定選取藍色的程式
    blue_output = cv2.inRange(img, blue_lower, blue_upper)  # 使用 inRange 設定影像顏色範圍
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    blue_output = cv2.dilate(blue_output, kernel)
    blue_output = cv2.erode(blue_output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列
    # cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        blue_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 3)

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# img = cv2.resize(img, (640//2, 480//2))  # 縮小尺寸，加快處理速度
# img = cv2.resize(img, (640//2, 480//2))
# img = cv2.resize(img, (640//2, 480//2))
