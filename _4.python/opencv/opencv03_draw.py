"""
OpenCV 畫圖

cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.polylines()  # 空心多邊形
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

cv2.FONT_HERSHEY_SIMPLEX	sans-serif字型正常大小
cv2.FONT_HERSHEY_PLAIN		sans-serif字型較小字型
cv2.FONT_HERSHEY_DUPLEX		sans-serif字型正常大小，但是比較複雜
cv2.FONT_HERSHEY_COMPLEX	serif字型正常大小
cv2.FONT_HERSHEY_TRIPLEX	serif字型正常大小，但是比較複雜
cv2.FONT_HERSHEY_COMPLEX_SMALL	serif字型較小字型
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX	手寫風格的字型
cv2.FONT_HERSHEY_SCRIPT_COMPLEX	手寫風格的字型，但是比較複雜
cv2.FONT_ITALIC			italic字型(斜體字)

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
from opencv_common import *

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename3 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立黑圖")
W, H = 1200, 800
image = np.zeros((H, W, 3), dtype="uint8")  # 三維(彩色) 空白影像

print("畫直線")
line_width = 10  # 線寬
x1, y1 = 50, 50
x2, y2 = 250, 50
# 畫直線 起 終 色 寬
cv2.line(image, (x1, y1), (x2, y2), RED, line_width)
cv2.line(image, (x1, y1), (x2, y2), 30)  # 無color, 即 黑色線 1 點
cv2.line(image, (x1, y1 + 30), (x2, y2 + 30), GREEN, 15, lineType=cv2.LINE_AA)

print("畫箭頭")
# 畫箭頭 起 終 色 寬
cv2.arrowedLine(image, (x1, y1 + 60), (x2, y2 + 60), BLUE, 5)

print("畫矩形 空心")
line_width = 5
# 畫矩形 左上 右下 色 寬
w, h = 150, 100
# 矩形之左上點
x1, y1 = 50, 150
# 矩形之右下點
x2, y2 = x1 + w, y1 + h
cv2.rectangle(image, (x1, y1), (x2, y2), RED, line_width)

print("畫矩形 實心")
line_width = -1  # -1, 填滿
# 畫矩形 左上 右下 色 寬(-1, 填滿)
w, h = 150 - 50, 100 - 50
# 矩形之左上點
x1, y1 = 50 + 25, 150 + 25
# 矩形之右下點
x2, y2 = x1 + w, y1 + h
cv2.rectangle(image, (x1, y1), (x2, y2), RED, line_width)  # 線條寬度為負數 代表實心

print("畫圓形 空心")
cx, cy = 60, 320  # 圓心
radius = 50  # 半徑
line_width = 2  # 線寬
cv2.circle(image, (cx, cy), radius, YELLOW, line_width)  # 繪製圓形

print("畫圓形 實心")
line_width = -1  # 線寬 負值代表實心
cv2.circle(image, (cx, cy), radius // 2, YELLOW, line_width)  # 設定 -1

print("畫橢圓形")
cx, cy = 220, 320  # 橢心
AA, BB = 100, 50  # 長軸 短軸
angle = 0  # 順時鐘旋轉角度
line_width = 5  # 線條寬度, 負數代表實心

# 畫橢圓             中心   長軸 短軸  旋轉 開始 結束角度 顏色 線寬
cv2.ellipse(image, (cx, cy), (AA, BB), angle, 0, 360, RED, line_width)  # 空心
cv2.ellipse(image, (cx, cy), (AA // 2, BB // 2), angle, 0, 360, RED, -1)  # 實心
# 畫藍色半橢圓
cv2.ellipse(image, (cx, cy + 70), (100, 50), 0, 0, 180, 255, -1)  # 藍色半橢圓

print("改一塊顏色")
image[170:250, 220:300] = [BLUE]

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

# 空心多邊形
cv2.polylines(image, [pts], True, RED, line_width)  # True表示封口
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

# 空心多邊形
# cv2.polylines(image,[pts],True, GREEN, line_width)   # 繪製多邊形

# 實心多邊形
cv2.fillPoly(image, [pts], GREEN)

print("畫多邊形 保留測試reshape")
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, BLUE)  # 空心多邊形

pts1 = np.array([[500, 50], [600, 100], [500, 150], [400, 100]])  # 頂點陣列
pts2 = np.array([[500, 150], [600, 200], [500, 250], [400, 200]])  # 頂點陣列

cv2.polylines(image, [pts1], True, BLUE, 5)  # 封閉式 空心多邊形
cv2.polylines(image, [pts2], False, RED, 3)  # 開放式 空心多邊形

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立黑圖")
W, H = 1200, 800
image = np.zeros((H, W, 3), np.uint8)

image[:] = (128, 128, 128)  # 灰色背景

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 2  # 字體大小
font_color = YELLOW
line_width = 2  # 字體粗細, 線寬
line_type = cv2.LINE_AA  # 文字線條樣式

x_st, y_st = 10, 50

cv2.putText(
    image,
    "Welcome 1111",
    (x_st, y_st),
    font,
    font_size,
    font_color,
    line_width,
    line_type,
)

y_st += 60
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

y_st += 40
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
y_st += 110
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
# cv2.putText(image, "Welcome 4444", (x_st, y_st), font, font_size, font_color, line_width, line_type, False)    #False: 從左上畫起(v)
# cv2.putText(image, "Welcome 4444", (x_st, y_st), font, font_size, font_color, line_width, line_type, True)     #True:  從左下畫起
cv2.rectangle(image, (x_st, y_st), (x_st + w, y_st - h), RED, 2)

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

y_st += 30
# font_filename = "NotoSansTC-Regular.otf"          # 設定字型路徑
font = ImageFont.truetype(font_filename, 50)  # 設定字型與文字大小
imagePil = Image.fromarray(image)  # 將 image 轉換成 PIL 影像
draw = ImageDraw.Draw(imagePil)  # 準備開始畫畫
draw.text((x_st, y_st), "歡迎來到美國", fill=CYAN, font=font)  # 畫入文字
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
x_st, y_st = 500, 50
for font in fonts:
    cv2.putText(
        image, text, (x_st, y_st), font, font_size, font_color, line_width, line_type
    )
    y_st += 60

x_st, y_st = 10, 430

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Python", (x_st, y_st), font, 3, BLUE, 12)  # 大小3, 線寬12

y_st += 100
cv2.putText(image, "Python", (x_st, y_st), font, 3, BLUE, 12)
cv2.putText(image, "Python", (x_st, y_st), font, 3, YELLOW, 5)

font = cv2.FONT_HERSHEY_SIMPLEX
y_st += 120
cv2.putText(image, "Python", (x_st, y_st), font, 3, BLUE, 12)

y_st += 60
cv2.putText(image, "Python", (x_st, y_st), font, 3, GREEN, 12, cv2.LINE_8, True)

font = cv2.FONT_HERSHEY_SIMPLEX
x_st, y_st = 400, 520
cv2.putText(image, "Peony", (x_st, y_st), font, 2, BLUE, 6)

from PIL import Image, ImageDraw, ImageFont


def cv2_Chinese_Text(image, text, left, top, textColor, fontSize):
    # 建立中文字輸出
    # 影像轉成 PIL影像格式
    if isinstance(image, np.ndarray):
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)  # 建立PIL繪圖物件
    fontText = ImageFont.truetype(  # 建立字型 - 新細明體
        "C:\Windows\Fonts\mingliu.ttc", fontSize, encoding="utf-8"  # 新細明體  # 字型大小
    )  # 編碼方式
    draw.text((left, top), text, textColor, font=fontText)  # 繪製中文字
    # 將PIL影像格式轉成OpenCV影像格式
    return cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)


x_st, y_st = 400, 550
image = cv2_Chinese_Text(image, "牡丹亭", x_st, y_st, RED, 50)

y_st += 150
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "OpenCV", (x_st, y_st), font, 4, WHITE, 2)

# 黃底藍字 # 標註右下角底色是黃色
cv2.rectangle(
    image,
    (image.shape[1] - 105, image.shape[0] - 20),
    (image.shape[1], image.shape[0]),
    YELLOW,
    -1,
)
# 標註文字
cv2.putText(
    image,
    "Open CV",
    (image.shape[1] - 100, image.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    BLUE,
    1,
)


x_st, y_st = 700, 500

font = cv2.FONT_HERSHEY_SIMPLEX
loc = (10, 40)
cv2.putText(image, "Python", (x_st, y_st), font, 1, RED, 2, cv2.LINE_AA)
cv2.putText(
    image, "Python", (x_st, y_st + 80), cv2.FONT_HERSHEY_PLAIN, 5.0, BLUE, cv2.LINE_AA
)

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立黑圖")
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
        cv2.rectangle(image, (x1, y1), (x2, y2), GREEN, 6)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        thickness = 1
        labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
        _x1 = x1  # bottomleft x of text
        _y1 = y1  # bottomleft y of text
        _x2 = x1 + labelSize[0][0]  # topright x of text
        _y2 = y1 - labelSize[0][1]  # topright y of text
        cv2.rectangle(
            image, (_x1, _y1), (_x2, _y2), GREEN, cv2.FILLED
        )  # text background
        cv2.putText(image, label, (x1, y1), fontFace, fontScale, BLACK, thickness)
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
box["label"] = "object 1"
box["x1"] = 40
box["y1"] = 40
box["x2"] = 180
box["y2"] = 180
bboxs.append(box)
box2 = {"label": "object 2", "x1": 300, "y1": 200, "x2": 600, "y2": 440}
bboxs.append(box2)
drawBoundingBox(image, bboxs)

draw_line(image)

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1)  # 使用影像當畫布
cx, cy = 150, 150  # 中心點座標
size = (200, 100)  # 橢圓的x,y軸長度
for i in range(0, 15):
    angle = np.random.randint(0, 361)  # 橢圓偏移的角度
    color = np.random.randint(0, 256, size=3).tolist()  # 橢圓的隨機色彩
    cv2.ellipse(image, (cx, cy), size, angle, 0, 360, color, 1)  # 繪製橢圓形

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 400  # 畫布高度
width = 600  # 畫布寬度
width, height = 640, 480  # 影像寬, 影像高

print("建立黑圖")
image = np.zeros((height, width, 3), np.uint8)  # 建立黑底畫布陣列
for i in range(0, 50):
    cx = np.random.randint(0, width)  # 隨機數圓心的 x 軸座標
    cy = np.random.randint(0, height)  # 隨機數圓心的 y 軸座標
    color = np.random.randint(0, 256, size=3).tolist()  # 建立隨機色彩
    r = np.random.randint(5, 100)  # 在5 - 100間的隨機半徑
    cv2.circle(image, (cx, cy), r, color, -1)  # 建立隨機實心圓

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立黑圖")
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
    cv2.circle(image, (ptx), 10, RED, -1)

print("畫連線")

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        corner1 = tuple(points[i])
        corner2 = tuple(points[j])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(image, corner1, corner2, color, 1)


cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
width, height = 640, 480  # 影像寬, 影像高

r = 15  # 反彈球半徑
speed = 0.01  # 反彈球移動速度
x = int(width / 2) - r  # 反彈球的最初 x 位置
y = 50  # 反彈球的最初 y 位置
y_step = 5  # 反彈球移動 y 步伐

while cv2.waitKey(1) == -1:
    if y > height - r or y < r:  # 反彈球超出畫布下邊界或是上邊界
        y_step = -y_step
    y += y_step  # 新的反彈球 y 位置
    image = np.ones((height, width, 3), np.uint8) * 255  # 建立白圖
    cv2.circle(image, (x, y), r, BLUE, -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", image)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
width, height = 640, 480  # 影像寬, 影像高

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
    image = np.ones((height, width, 3), np.uint8) * 255  # 建立白圖
    cv2.circle(image, (x, y), r, BLUE, -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", image)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from random import *

width = 640  # 反彈球畫布寬度
height = 480  # 反彈球畫布高度
width, height = 640, 480  # 影像寬, 影像高

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
    image = np.ones((height, width, 3), np.uint8) * 255  # 建立白圖
    cv2.circle(image, (x, y), r, BLUE, -1)  # 繪製反彈球
    cv2.imshow("Bouncing Ball", image)
    time.sleep(speed)  # 依speed設定休息

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 2
thickness = 2
text = "Peony"
testSize = cv2.getTextSize(text, fontFace, fontScale, thickness)
print("字體大小 : ", testSize)

w = testSize[0][0]
h = testSize[0][1]
print(w)
print(h)

cx, cy = 305 // 2, 400 // 2  # 中心點座標

x_st = cx - int(testSize[0][0] / 2)
y_st = cy + int(testSize[0][1] / 2)

x_st = 0
y_st = 0
print(x_st)
print(y_st)

image = cv2.imread(filename1)

# cv2.putText(image, text, (x_st, y_st), font, font_size, font_color, line_width, line_type, False)    #False: 從左上畫起(v)
# cv2.putText(image, text, (x_st, y_st), font, font_size, font_color, line_width, line_type, True)     #True:  從左下畫起
cv2.putText(
    image, text, (x_st, y_st + h), fontFace, fontScale, RED, thickness, cv2.LINE_AA
)
cv2.rectangle(image, (x_st, y_st), (x_st + w, y_st + h), BLUE)  # 繪製矩形

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立黑圖")
W, H = 400, 400
image = np.zeros((H, W, 3), np.uint8)

R = 150

points = list()

N = 5
for i in range(N):
    px = R * math.cos(math.pi * i * 360 / N / 180)
    py = R * math.sin(math.pi * i * 360 / N / 180)
    points.append((W // 2 + int(px), H // 2 + int(py)))

print(points)

for p in points:
    print(p)
    cv2.circle(image, (p[0], p[1]), 10, GREEN, -1)  # 繪製圓形

points = np.int0(points)  # 取整數
cv2.drawContours(image, [points], 0, RED, 2)

cv2.imshow("OpenCV", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 生成隨機顏色，3個[0, 256)的隨機數
color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
print(color)

# 畫多邊形
pts = np.array([[200, 50], [300, 200], [200, 350], [100, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 第1個參數為-1, 表明這一維的長度是根據后面的維度的計算出來的。
cv2.polylines(image, [pts], True, GREEN, 8)  # 空心多邊形
# 調用函數polylines完成多邊形繪圖，注意第3個參數控制多邊形封閉
# cv2.polylines(image, [pts], False, GREEN, 8)  #不閉合的的多邊形

# 255 就是藍色
cv2.rectangle(image, (100, 100), (200, 200), 255, 2)  # 255 藍色


# cv2.fillPoly
mask = np.zeros_like(edge)  # 全黑遮罩
points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊座標
# 畫實心多邊形
cv2.fillPoly(mask, points, 255)  # 畫實心多邊形


# cv2.line 畫 直線
cv2.line(image, (1, 1), (300, 1), BLUE)  # 上方水平直線
cv2.line(image, (300, 1), (300, 300), BLUE)  # 右邊垂直直線
cv2.line(image, (300, 300), (1, 300), BLUE)  # 下邊水平直線
cv2.line(image, (1, 300), (1, 1), BLUE)  # 左邊垂直直線

for x in range(150, 300, 10):
    cv2.line(image, (x, 1), (300, x - 150), BLUE)
for y in range(150, 300, 10):
    cv2.line(image, (1, y), (y - 150, 300), BLUE)


# cv2.line 畫 圓
cx, cy = 100, 100  # 中心點座標
cv2.circle(image, (cx, cy), 30, RED, -1)  # 繪製實心圓形

for r in range(40, 200, 20):  # 繪製系列空心圓形
    cv2.circle(image, (cx, cy), r, GREEN, 2)


# cv2.line 畫 橢圓
cx, cy = 150, 100  # 中心點座標
size = (200, 100)
angle = 0
cv2.ellipse(image, (cx, cy), size, angle, 0, 360, RED, 1)  # 繪製橢圓形
angle = 45
cv2.ellipse(image, (cx, cy), size, angle, 0, 360, GREEN, 5)  # 繪製橢圓形
cv2.ellipse(image, (cx, cy), size, angle, 45, 135, BLUE, 3)  # 繪製橢圓弧

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 任意顏色
color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
cv2.rectangle(image, (p1x, p1y), (p2x, p2y), color, 2)
color = np.random.randint(0, high=256, size=(3,)).tolist()  # np.random之randint不含尾
cv2.rectangle(image, (p1x, p1y), (p2x, p2y), color, thickness)


a = np.random.randint(1, d - 50)
r = np.random.randint(1, d / 5)
angle = np.random.randint(0, 361)
color = np.random.randint(0, high=256, size=(3,)).tolist()
if mode == 1:
    cv2.rectangle(image, (x, y), (a, a), color, thickness)
elif mode == 2:
    cv2.circle(image, (x, y), r, color, thickness)
elif mode == 3:
    cv2.line(image, (a, a), (x, y), color, 3)
elif mode == 4:
    cv2.ellipse(image, (x, y), (100, 150), angle, 0, 360, color, thickness)
elif mode == 5:
    cv2.putText(
        image, "OpenCV", (0, round(d / 2)), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 5
    )


# cv2.line(image, (0, 0), (x, y), CYAN, 2)#畫直線連線
cv2.circle(image, (x, y), 10, (255), -1)  # 畫點
cv2.rectangle(image, (x1, y1), (x, y), GREEN, 5)


cv2.line(image, (10, 300), (250, 300), BLUE, 5)  # 輸出線條
cv2.rectangle(image, (20, 20), (240, 250), RED, 2)  # 輸出矩陣
cv2.putText(image, "OpenCV", (10, 250), cv2.FONT_ITALIC, 3, BLUE, 8)  # 輸出文字
