"""
OpenCV 畫圖

cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.polylines()
cv2.drawContours() #多點頭尾連線

cv2.putText()

cv之繪圖之順序
建立畫布
直線	.line
矩形	.rectangle
圓形	.circle
橢圓形	.ellipse
多邊形	.polylines
文字	.putText

未指明line_width就是1點

"""

import cv2

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
print("建立畫布(黑色)")
W, H = 640, 480
image = np.zeros((H, W, 3), dtype="uint8")

print("畫直線")
color = (0, 0, 255)  # B G R
line_width = 10  # 線寬
x1, y1 = 50, 50
x2, y2 = 250, 50
# 畫直線 起 終 色 寬
cv2.line(image, (x1, y1), (x2, y2), color, line_width)
cv2.line(image, (x1, y1), (x2, y2), 30)  # 無color, 即 黑色線 1 點
cv2.line(image, (x1, y1 + 30), (x2, y2 + 30), (0, 255, 0), 15, lineType=cv2.LINE_AA)

print("畫箭頭")
# 畫箭頭 起 終 色 寬
cv2.arrowedLine(image, (x1, y1 + 60), (x2, y2 + 60), (255, 0, 0), 5)

print("畫矩形 空心")
color = (0, 0, 255)  # B G R
line_width = 5
# 畫矩形 左上 右下 色 寬
w, h = 150, 100
# 矩形之左上點
x1, y1 = 50, 150
# 矩形之右下點
x2, y2 = x1 + w, y1 + h
cv2.rectangle(image, (x1, y1), (x2, y2), color, line_width)

print("畫矩形 實心")
color = (0, 255, 0)  # B G R
line_width = -1  # -1, 填滿
# 畫矩形 左上 右下 色 寬(-1, 填滿)
w, h = 150 - 50, 100 - 50
# 矩形之左上點
x1, y1 = 50 + 25, 150 + 25
# 矩形之右下點
x2, y2 = x1 + w, y1 + h
cv2.rectangle(image, (x1, y1), (x2, y2), color, line_width)  # 線條寬度為負數 代表實心

print("畫圓形 空心")
cx, cy = 60, 320  # 圓心
radius = 50  # 半徑
color = (0, 255, 255)  # 顏色
line_width = 2  # 線寬
cv2.circle(image, (cx, cy), radius, color, line_width)  # 繪製圓形

print("畫圓形 實心")
line_width = -1  # 線寬 負值代表實心
cv2.circle(image, (cx, cy), radius // 2, color, line_width)  # 設定 -1

print("畫橢圓形")
cx, cy = 220, 320  # 橢心
AA, BB = 100, 50  # 長軸 短軸
angle = 0  # 順時鐘旋轉角度
color = (0, 0, 255)
line_width = 5  # 線條寬度, 負數代表實心

# 畫橢圓              中心  長軸 短軸 旋轉  開始 結束角度 顏色 線寬
cv2.ellipse(image, (cx, cy), (AA, BB), angle, 0, 360, color, line_width)  # 空心
cv2.ellipse(image, (cx, cy), (AA // 2, BB // 2), angle, 0, 360, color, -1)  # 實心

cv2.ellipse(image, (cx, cy + 70), (100, 50), 0, 0, 180, 255, -1)  # 藍色半橢圓

print("改一塊顏色")
image[170:250, 220:300] = [255, 0, 0]

print("畫多邊形")

# 設定頂點座標
x_st, y_st = 320, 20
dd = 50
px1, py1 = x_st, y_st
px2, py2 = x_st - dd, y_st + dd
px3, py3 = x_st - dd, y_st + dd * 2
px4, py4 = x_st, y_st + dd * 3
px5, py5 = x_st + dd, y_st + dd * 2
px6, py6 = x_st + dd, y_st + dd

line_width = 3  # 線寬

pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6]])
# pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6]], np.int32)

cv2.polylines(image, [pts], True, (0, 0, 255), line_width)  # True表示封口
# True: 頭尾相連, False: 頭尾不相連

x_st, y_st = 320, 20 + 20
dd = 40
px1, py1 = x_st, y_st
px2, py2 = x_st - dd, y_st + dd
px3, py3 = x_st - dd, y_st + dd * 2
px4, py4 = x_st, y_st + dd * 3
px5, py5 = x_st + dd, y_st + dd * 2
px6, py6 = x_st + dd, y_st + dd

pts = np.array(
    [[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6]]
)  # 產生座標陣列

# 畫多邊形 空心
# cv2.polylines(image,[pts],True,(0,255,0), line_width)   # 繪製多邊形

# 畫多邊形 實心
cv2.fillPoly(image, [pts], (0, 255, 0))

print("畫多邊形 保留測試reshape")
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, (255, 0, 0))

cv2.imshow("OpenCV Draw 1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("建立畫布")
W, H = 1000, 800

image = np.zeros((H, W, 3), np.uint8)
# 灰色背景
image[:] = (128, 128, 128)

"""
cv2.putText參數
cv2.putText(image, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
圖片影像/繪製的文字/左上角坐標/字體/字體大小/顏色/字體粗細/字體線條種類

image – 要繪製文字的影像
text – 要繪製的文字
org – 文字左下角在影像中的座標位置
fontFace – 文字字體, 
fontScale – 文字縮放比例
color – 文字顏色
thickness – 文字線條粗細度
lineType – 文字線條樣式
bottomLeftOrigin – When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

"""

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 2  # 字體大小
font_color = (0, 255, 255)  # B G R
line_width = 2  # 字體粗細, 線寬
line_type = cv2.LINE_AA  # 文字線條樣式

x_st, y_st = 10, 100

cv2.putText(
    image, "Welcome 1111", (x_st, y_st), font, font_size, font_color, line_width, line_type
)

y_st += 80
cv2.putText(
    image,
    "Welcome 2222",
    (x_st, y_st),
    font,
    font_size,
    font_color,
    line_width,
    line_type,
)  # 加文字線條樣式

y_st += 80
cv2.putText(
    image,
    "Welcome 3333",
    (x_st, y_st),
    font,
    font_size,
    font_color,
    line_width,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    True,
)

text_size = cv2.getTextSize("Welcome 4444", font, font_size, line_width)
print("字體大小 : ", text_size)
w = text_size[0][0]
h = text_size[0][1]
y_st += 140
cv2.putText(
    image,
    "Welcome 4444",
    (x_st, y_st),
    font,
    font_size,
    font_color,
    line_width,
    line_type,
)  # 預設, False
# cv2.putText(image, "Welcome 4444", (x_st, y_st), font, font_size, font_color, line_width, line_type, False)    #False: 從左上畫起
# cv2.putText(image, "Welcome 4444", (x_st, y_st), font, font_size, font_color, line_width, line_type, True)     #True:  從左下畫起
cv2.rectangle(image, (x_st, y_st), (x_st + w, y_st - h), (0, 0, 255), 2)

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

y_st += 40
# font_filename = 'NotoSansTC-Regular.otf'          # 設定字型路徑
font = ImageFont.truetype(font_filename, 50)  # 設定字型與文字大小
imagePil = Image.fromarray(image)  # 將 image 轉換成 PIL 影像
draw = ImageDraw.Draw(imagePil)  # 準備開始畫畫
draw.text((x_st, y_st), "歡迎來到美國", fill=(255, 255, 0), font=font)  # 畫入文字
image = np.array(imagePil)  # 將 PIL 影像轉換成 numpy 陣列

print("畫全部內建字型")
fonts = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
]

text = "Welcome"
x_st, y_st = 500, 100
for font in fonts:
    cv2.putText(
        image, text, (x_st, y_st), font, font_size, font_color, line_width, line_type
    )
    y_st += 60

cv2.imshow("OpenCV Draw 2", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
print("------------------------------------------------------------")  # 60個

print("建立畫布(黑色)")

W, H = 800, 600
# image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), dtype=np.uint8)
image[:] = (200, 200, 200)  # 將所有點著色

print("畫標示頁箋")

# 用 putText 繪製物件偵測的標籤
def drawBoundingBox(image, bboxs):
    for box in bboxs:
        x1, y1, x2, y2 = (box["x1"], box["y1"], box["x2"], box["y2"])
        label = box["label"]
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 6)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        thickness = 1
        labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
        _x1 = x1  # bottomleft x of text
        _y1 = y1  # bottomleft y of text
        _x2 = x1 + labelSize[0][0]  # topright x of text
        _y2 = y1 - labelSize[0][1]  # topright y of text
        cv2.rectangle(
            image, (_x1, _y1), (_x2, _y2), (0, 255, 0), cv2.FILLED
        )  # text background
        cv2.putText(image, label, (x1, y1), fontFace, fontScale, (0, 0, 0), thickness)
    return image


def draw_line(image):
    H = image.shape[0]
    W = image.shape[1]
    print(image.shape)
    print(H // 100)
    print(W // 100)
    for i in range(H // 100 + 1):
        cv2.line(image, (0, 100 * i), (W, 100 * i), (0, 0, 100), 2)  # 畫線 水平線 R

    for i in range(W // 100 + 1):
        cv2.line(
            image, (100 * i, 0), (100 * i, H), (0, 100, 0), 2, lineType=cv2.LINE_AA
        )  # 畫線 垂直線 G


bboxs = []
box = {}
box['label'] = 'object 1'
box['x1'] = 40
box['y1'] = 40
box['x2'] = 180
box['y2'] = 180
bboxs.append(box)
box2 = {'label' : 'object 2', 'x1' : 300, 'y1' : 200, 'x2' : 600, 'y2' : 440}
bboxs.append(box2)
drawBoundingBox(image, bboxs)

draw_line(image)

cv2.imshow('OpenCV Draw 3', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
#有底圖作畫
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
image = cv2.imread(filename)	#讀取本機圖片
"""

# cv2.namedWindow("plot")


# 直接改寫image的內容
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename)

for i in range(20, 80):
    image[i, 180] = [0, 0, 255]  # 紅色一點

#     H          x
image[10:100, 200:290] = [0, 0, 255]  # 紅色 一塊 90X90

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個


"""
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 3
thickness = 2
text = '7'
testSize = cv2.getTextSize(text, fontFace, fontScale, thickness)
print(testSize)

bottomLeftX = 64-int(testSize[0][0]/2)
bottomLeftY = 64+int(testSize[0][1]/2)
cv2.putText(image, text, (bottomLeftX, bottomLeftY), fontFace,
  fontScale, (0, 255, 255), thickness, cv2.LINE_AA)

cv2.imshow('OpenCV Draw 4', image)

"""

print("------------------------------------------------------------")  # 60個

W, H, D = 400, 400, 3
image = np.ones((H, W, 3), dtype="uint8") * 255
(centerX, centerY) = (round(image.shape[1] / 2), round(image.shape[0] / 2))
# 將圖像的中心作為圓心,實際值為 d / 2
red = (0, 0, 255)  # 設置白色變量
for r in range(5, round(400 / 2), 12):
    cv2.circle(image, (centerX, centerY), r, red, 3)
    # circle(載體圖像，圓心，半徑，顏色)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 1")
plt.show()

cv2.imshow("OpenCV Draw 5", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

W, H, D = 400, 400, 3
image = np.ones((H, W, 3), dtype="uint8") * 255
# 生成白色背景
for i in range(0, 100):
    centerX = np.random.randint(0, high=400)  # np.random之randint不含尾
    # 生成隨機圓心X,確保在畫布image內
    centerY = np.random.randint(0, high=400)  # np.random之randint不含尾
    # 生成隨機圓心Y,確保在畫布image內
    radius = np.random.randint(5, high=400 / 5)  # np.random之randint不含尾
    # 生成隨機半徑，值范圍：[5, d/5)，最大半徑是 d / 5
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
    # 生成隨機顏色，3個[0, 256)的隨機數
    cv2.circle(image, (centerX, centerY), radius, color, -1)
    # 使用上述隨機數，在畫布image內畫圓


plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 2")
plt.show()

cv2.imshow("OpenCV Draw 6", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

W, H, D = 400, 400, 3
image = np.ones((H, W, 3), dtype="uint8") * 255
# 生成白色背景
center = (round(400 / 2), round(400 / 2))
# 注意數值類型，center = (d / 2, d / 2)不可以
size = (100, 200)
# 軸的長度
for i in range(0, 10):
    angle = np.random.randint(0, 361)  # np.random之randint不含尾
    # 偏移角度
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
    # 生成隨機顏色，3個[0, 256)的隨機數
    thickness = np.random.randint(1, 9)  # np.random之randint不含尾
    cv2.ellipse(image, center, size, angle, 0, 360, color, thickness)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 3")
plt.show()

cv2.imshow("OpenCV Draw 7", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

W, H, D = 400, 400, 3
image = np.ones((H, W, 3), dtype="uint8") * 255
# 生成白色背景
pts = np.array([[200, 50], [300, 200], [200, 350], [100, 200]], np.int32)
# 生成各個頂點,注意數據類型為int32
pts = pts.reshape((-1, 1, 2))
# 第1個參數為-1, 表明這一維的長度是根據后面的維度的計算出來的。
cv2.polylines(image, [pts], True, (0, 255, 0), 8)
# 調用函數polylines完成多邊形繪圖，注意第3個參數控制多邊形封閉
# cv2.polylines(image, [pts], False, (0, 255, 0), 8)  #不閉合的的多邊形

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("畫圖 4")
plt.show()

cv2.imshow("OpenCV Draw 8", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("建立畫布(黑色)")
W, H = 600, 600
image = np.zeros((H, W, 3), dtype="uint8")

R = 250

points = list()

N = 10
for i in range(N):
    px, py = R * math.cos(math.pi * i * 360 / N / 180), R * math.sin(
        math.pi * i * 360 / N / 180
    )
    points.append((W // 2 + int(px), H // 2 + int(py)))

print(points)

for ptx in points:
    cv2.circle(image, (ptx), 10, (0, 0, 255), -1)

print("畫連線")

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        corner1 = tuple(points[i])
        corner2 = tuple(points[j])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(image, corner1, corner2, color, 1)


cv2.imshow("OpenCV Draw 1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("drawContours")

W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)  # 黑色畫板

MIN = 100
MAX = W - 100
N = 4  # 隨機生成 N 個坐標點，每一行存儲一個坐標
# 隨機生成 橫縱坐標均在 MIN 至 MAX 的坐標點
points = np.random.randint(MIN, MAX, (N, 2), np.int32)
# print(points)

# points = np.int0(points)  # 取整數
cv2.drawContours(image, [points], 0, (0, 0, 255), 3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
