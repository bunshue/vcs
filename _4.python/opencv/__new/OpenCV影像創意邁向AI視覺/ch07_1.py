# ch7_1.py
import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
cv2.imshow("My Draw", img)  # 畫布顯示直線

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_10.py

# ch7_10.py
import cv2
import numpy as np

height = 400  # 畫布高度
width = 600  # 畫布寬度
img = np.zeros((height, width, 3), np.uint8)  # 建立黑底畫布陣列
for i in range(0, 50):
    cx = np.random.randint(0, width)  # 隨機數圓心的 x 軸座標
    cy = np.random.randint(0, height)  # 隨機數圓心的 y 軸座標
    color = np.random.randint(0, 256, size=3).tolist()  # 建立隨機色彩
    r = np.random.randint(5, 100)  # 在5 - 100間的隨機半徑
    cv2.circle(img, (cx, cy), r, color, -1)  # 建立隨機實心圓
cv2.imshow("Random Circle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_11.py

# ch7_11.py
import cv2

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
red = (0, 0, 255)  # 設定紅色
yellow = (0, 255, 255)  # 設定黃色
blue = (255, 0, 0)  # 設定藍色
size = (200, 100)
angle = 0
cv2.ellipse(img, (cx, cy), size, angle, 0, 360, red, 1)  # 繪製橢圓形
angle = 45
cv2.ellipse(img, (cx, cy), size, angle, 0, 360, yellow, 5)  # 繪製橢圓形
cv2.ellipse(img, (cx, cy), size, angle, 45, 135, blue, 3)  # 繪製橢圓弧

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_12.py

# ch7_12.py
import cv2
import numpy as np

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
size = (200, 100)  # 橢圓的x,y軸長度
for i in range(0, 15):
    angle = np.random.randint(0, 361)  # 橢圓偏移的角度
    color = np.random.randint(0, 256, size=3).tolist()  # 橢圓的隨機色彩
    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, color, 1)  # 繪製橢圓形

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_13.py

# ch7_13.py
import cv2
import numpy as np

img1 = np.ones((200, 300, 3), np.uint8) * 255  # 畫布1
pts = np.array([[150, 50], [250, 100], [150, 150], [50, 100]])  # 頂點陣列
cv2.polylines(img1, [pts], True, (255, 0, 0), 5)  # 繪製封閉式多邊形

img2 = np.ones((200, 300, 3), np.uint8) * 255  # 畫布2
cv2.polylines(img2, [pts], False, (0, 0, 255), 3)  # 繪製開放式多邊形

cv2.imshow("isClosed_True", img1)  # 畫布顯示封閉式多邊形
cv2.imshow("isClosed_False", img2)  # 畫布顯示開放式多邊形
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_14.py

# ch7_14.py
import cv2
import numpy as np

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (150, 180), font, 3, (255, 0, 0), 12)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_15.py

# ch7_15.py
import cv2
import numpy as np

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (150, 180), font, 3, (255, 0, 0), 12)
cv2.putText(img, "Python", (150, 180), font, 3, (0, 255, 255), 5)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_16.py

# ch7_16.py
import cv2
import numpy as np

img = np.ones((300, 600, 3), np.uint8) * 255  # 畫布
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Python", (120, 120), font, 3, (255, 0, 0), 12)
cv2.putText(img, "Python", (120, 180), font, 3, (0, 255, 0), 12, cv2.LINE_8, True)

cv2.imshow("Python", img)  # 畫布顯示文字
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_17.py

# ch7_17.py
import cv2

img = cv2.imread("antarctic.jpg")
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Antarctic", (120, 120), font, 3, (255, 0, 0), 12)

cv2.imshow("Antarctic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_17_1.py

# ch7_17_1.py
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def cv2_Chinese_Text(img, text, left, top, textColor, fontSize):
    """建立中文字輸出"""
    # 影像轉成 PIL影像格式
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)  # 建立PIL繪圖物件
    fontText = ImageFont.truetype(  # 建立字型 - 新細明體
        "C:\Windows\Fonts\mingliu.ttc", fontSize, encoding="utf-8"  # 新細明體  # 字型大小
    )  # 編碼方式
    draw.text((left, top), text, textColor, font=fontText)  # 繪製中文字
    # 將PIL影像格式轉成OpenCV影像格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


img = cv2.imread("antarctic.jpg")
img = cv2_Chinese_Text(img, "我在南極", 220, 100, (0, 0, 255), 50)

cv2.imshow("Antarctic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_18.py

# ch7_18.py
import cv2
import numpy as np
from random import *
import time

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = int(width / 2) - r  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_19.py

# ch7_19.py
import cv2
import numpy as np
from random import *
import time

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = 50  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
x_step = 5  # 反彈球移動 x 步伐
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if x > width - r or x < r:  # 反彈球超出畫布右邊界或是左邊界
        x_step = -x_step
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    x += x_step  # 新的反彈球 x 位置
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_2.py

# ch7_2.py
import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_20.py

# ch7_20.py
import cv2
import numpy as np
from random import *
import time

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = 50  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
random_step = [3, 4, 5, 6, 7]  # x 步伐串列
shuffle(random_step)  # 隨機產生 x 步伐串列
x_step = random_step[0]  # 反彈球移動 x 步伐
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if x > width - r or x < r:  # 反彈球超出畫布右邊界或是左邊界
        x_step = -x_step
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    x += x_step  # 新的反彈球 x 位置
    y += y_step  # 新的反彈球 y 位置
    img = np.ones((height, width, 3), np.uint8) * 255
    cv2.circle(img, (x, y), r, (255, 0, 0), -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", img)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_21.py

# ch7_21.py
import cv2

events = [i for i in dir(cv2) if "EVENT" in i]
for e in events:
    print(e)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_22.py

# ch7_22.py
import cv2
import numpy as np


def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        print(f"在x={x}, y={y}, 按一下滑鼠左鍵")
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        print(f"在x={x}, y={y}, 按一下滑鼠右鍵_")
    elif event == cv2.EVENT_MBUTTONDOWN:  # 按一下滑鼠中間鍵
        print(f"在x={x}, y={y}, 按一下滑鼠中間鍵")
    elif flags == cv2.EVENT_FLAG_LBUTTON:  # 按住滑鼠左鍵拖曳
        print(f"在x={x}, y={y}, 按住滑鼠左鍵拖曳")
    elif flags == cv2.EVENT_FLAG_RBUTTON:  # 按住滑鼠右鍵拖曳
        print(f"在x={x}, y={y}, 按住滑鼠右鍵拖曳")


image = np.ones((200, 300, 3), np.uint8) * 255
cv2.namedWindow("OpenCV Mouse Event")
cv2.setMouseCallback("OpenCV Mouse Event", OnMouseAction)
cv2.imshow("OpenCV Mouse Event", image)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_23.py

# ch7_23.py
import cv2
import numpy as np


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        cv2.circle(image, (x, y), r, color, 3)  # 隨機的空心圓


height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", OnMouseAction)
while 1:
    cv2.imshow("Draw Circle", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_24.py

# ch7_24.py
import cv2
import numpy as np


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
        if key == ord("s"):
            cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
        else:
            cv2.circle(image, (x, y), r, color, 3)  # 隨機的線寬是 3 的圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        px = np.random.randint(10, 100)
        py = np.random.randint(10, 100)
        if key == ord("s"):
            cv2.rectangle(image, (x, y), (px, py), color, -1)  # 實心矩形
        else:
            cv2.rectangle(image, (x, y), (px, py), color, 3)  # 空心矩形


height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("MyDraw")
cv2.setMouseCallback("MyDraw", OnMouseAction)
while 1:
    cv2.imshow("MyDraw", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_25.py

# ch7_25.py
import cv2
import numpy as np


def onChange(x):
    b = cv2.getTrackbarPos("B", "canvas")  # 建立B通道顏色
    g = cv2.getTrackbarPos("G", "canvas")  # 建立G通道顏色
    r = cv2.getTrackbarPos("R", "canvas")  # 建立R通道顏色
    canvas[:] = [b, g, r]  # 設定背景色


canvas = np.ones((200, 640, 3), np.uint8) * 255  # 寬640,高200
cv2.namedWindow("canvas")
cv2.createTrackbar("B", "canvas", 0, 255, onChange)  # 藍色通道控制
cv2.createTrackbar("G", "canvas", 0, 255, onChange)  # 綠色通道控制
cv2.createTrackbar("R", "canvas", 0, 255, onChange)  # 紅色通道控制
while 1:
    cv2.imshow("canvas", canvas)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    if key == 27:  # Esc 則結束
        break

cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_26.py

# ch7_26.py
import cv2
import numpy as np


def onChange(x):
    pass


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        cv2.circle(image, (x, y), r, color, thickness)  # 隨機的圓


thickness = -1  # 預設寬度是 0
height = 400  # 視窗高度
width = 600  # 視窗寬度
image = np.ones((height, width, 3), np.uint8) * 255
cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", OnMouseAction)
cv2.createTrackbar("Thickness", "Draw Circle", 0, 1, onChange)
while 1:
    cv2.imshow("Draw Circle", image)
    key = cv2.waitKey(100)  # 0.1秒檢查一次
    num = cv2.getTrackbarPos("Thickness", "Draw Circle")
    if num == 0:
        thickness = -1  # 實心設定
    else:
        thickness = 3  # 寬度是 3
    if key == ord("Q") or key == ord("q"):  # Q或q則結束
        break
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_3.py

# ch7_3.py
import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
img[1:300, 1:300] = (0, 255, 255)  # 設定黃色底

cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_4.py

# ch7_4.py
import cv2


img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
img[1:300, 1:300] = (0, 255, 255)  # 設定黃色底

cv2.line(img, (1, 1), (300, 1), (255, 0, 0))  # 上方水平直線
cv2.line(img, (300, 1), (300, 300), (255, 0, 0))  # 右邊垂直直線
cv2.line(img, (300, 300), (1, 300), (255, 0, 0))  # 下邊水平直線
cv2.line(img, (1, 300), (1, 1), (255, 0, 0))  # 左邊垂直直線
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_5.py

# ch7_5.py
import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.rectangle(img, (1, 1), (300, 300), (255, 0, 0))  # 繪製矩形
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_6.py

# ch7_6.py
import cv2
import numpy as np

img = np.ones((350, 500, 3), np.uint8) * 255  # 建立白色底的畫布
cv2.rectangle(img, (1, 1), (300, 300), (0, 255, 255), -1)  # 設定黃色底
cv2.rectangle(img, (1, 1), (300, 300), (255, 0, 0))  # 繪製矩形
for x in range(150, 300, 10):
    cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
for y in range(150, 300, 10):
    cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_7.py

# ch7_7.py
import cv2

img = cv2.imread("antarctic.jpg")  # 使用影像當畫布
cy = int(img.shape[0] / 2)  # 中心點 y 座標
cx = int(img.shape[1] / 2)  # 中心點 x 座標
red = (0, 0, 255)  # 設定紅色
yellow = (0, 255, 255)  # 設定黃色
cv2.circle(img, (cx, cy), 30, red, -1)  # 繪製實心圓形
for r in range(40, 200, 20):  # 繪製系列空心圓形
    cv2.circle(img, (cx, cy), r, yellow, 2)

cv2.imshow("My Draw", img)  # 畫布顯示結果
cv2.waitKey(0)
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_8.py

# ch7_8.py
import numpy as np

print("回傳單3個元素的陣列, 值是0(含)至256(不含)的隨機數")
arr = np.random.randint(0, 256, size=3)
print(type(arr))
print(arr)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch07\ch7_9.py

# ch7_9.py
import numpy as np

print("回傳單3個元素的陣列, 值是0(含)至256(不含)的隨機數")
arr = np.random.randint(0, 256, size=3)
print(type(arr))
print(arr)
print("將陣列改為串列")
print(arr.tolist())


print("------------------------------------------------------------")  # 60個
