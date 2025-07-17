"""
cv2之各種影像處理功能

barcode / QR code

captcha

"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
# barcode / QR code ST
print("------------------------------------------------------------")  # 60個

print("二維條碼")

filename = "C:/_git/vcs/_4.python/opencv/data/_qrcode/QR1.png"

image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()  # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(image)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print("data")
    print(data)  # QRCode 的內容
    print("bbox")
    print(bbox)  # QRCode 的邊界
    print("rectified")
    print(rectified)  # 換成垂直 90 度的陣列
else:
    print("無 QR Code")

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_35")

filename = "C:/_git/vcs/_4.python/opencv/data/_qrcode/QR1.png"

image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 取得座標的函式
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)  # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin, ymin, xmax, ymax)


# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), RED, 5)  # 畫矩形

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("OpenCV_36")

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL ( 為了放中文字 )

filename = "C:/_git/vcs/_4.python/opencv/data/_qrcode/QR1.png"

image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 建立放入文字的函式
def putText(x, y, text, color=(0, 0, 0)):
    global image
    # font_filename = "NotoSansTC-Regular.otf"      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(font_filename, 20)  # 設定字型與大小
    imagePil = Image.fromarray(image)  # 將 image 轉換成 PIL 圖片物件
    draw = ImageDraw.Draw(imagePil)  # 建立繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 寫入文字
    image = np.array(imagePil)  # 轉換回 np array


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), RED, 5)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("OpenCV_37")

# many-qr-code
from PIL import ImageFont, ImageDraw, Image

image = cv2.imread("many-qrcode.jpg")


def putText(x, y, text, color=(0, 0, 0)):
    global image
    # font_filename = "NotoSansTC-Regular.otf"
    font = ImageFont.truetype(font_filename, 20)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


qrcode = cv2.QRCodeDetector()
ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(
    image
)  # 改用 detectAndDecodeMulti
# 如果有偵測到
if ok:
    # 使用 for 迴圈取出每個 QRCode 的資訊
    for i in range(len(data)):
        print(data[i])
        print(bbox[i])
        text = data[i]  # QRCode 內容
        box = boxSize(bbox[i])  # QRCode 左上與右下座標
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), RED, 5)  # 標記外框
        putText(box[0], box[3], text)  # 寫出文字

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 一維條碼
filename = "C:/_git/vcs/_4.python/opencv/data/_qrcode/barcode1.png"

image = cv2.imread(filename)

barcode = cv2.barcode_BarcodeDetector()  # 建立 BarCode 偵測器
data, data_type, bbox = barcode.detectAndDecode(image)  # 偵測 BarCode
print("data")
print(data)
print("data_type")
print(data_type)
print("bbox")
print(bbox)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 18 QRCode 偵測器")
print("按 ESC 離開")

cap = cv2.VideoCapture(1)


def putText(x, y, text, color=BLACK):
    global img
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imgPil = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPil)
    draw.text((x, y), text, fill=color, font=font)
    img = np.array(imgPil)


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (640, 480))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 辨識 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]  # QRCode 內容
            box = boxSize(bbox[i])  # QRCode 座標
            cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), RED, 5)  # 繪製外框
            putText(box[0], box[3], text, color=RED)  # 顯示文字

    cv2.imshow("OpenCV 09", img)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 19 QRCode 偵測器")
print("按 ESC 離開")

cap = cv2.VideoCapture(1)


def putText(x, y, text, size=20, color=BLACK):
    global img
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imgPil = Image.fromarray(img)  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 加入文字
    img = np.array(imgPil)  # 轉換成 np.array


# 定義馬賽克函式
def mosaic(image, level):
    size = image.shape  # 取得原始圖片的資訊
    h = int(size[0] / level)  # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
    w = int(size[1] / level)  # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
    output = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)  # 根據縮小尺寸縮小
    output = cv2.resize(
        output, (size[1], size[0]), interpolation=cv2.INTER_NEAREST
    )  # 放大到原本的大小
    return output


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (640, 480))
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(img)  # 辨識 QRCode
    # 如果偵測到 QRCode
    if ok:
        for i in range(len(data)):
            text = data[i]  # 取出內容
            # 如果內容是 a1，套用模糊效果
            if text == "a1":
                img = cv2.blur(img, (20, 20))
                putText(0, 0, "模糊效果", 100, WHITE)
            # 如果內容是 a2，套用馬賽克效果
            elif text == "a2":
                img = mosaic(img, 15)
                putText(0, 0, "馬賽克效果", 100, WHITE)
            # 如果內容是 a2，套用片效果
            elif text == "a3":
                img = 255 - img
                putText(0, 0, "負片效果", 100, BLACK)

    cv2.imshow("OpenCV 10", img)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 20 讀取 QR code 圖檔")
print("按 ESC 離開")

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_qrcode/QR1.png"

image = cv2.imread(filename)


def putText(x, y, text, color=BLACK):
    global image
    font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文
    font_size = 20
    font = ImageFont.truetype(font_filename, font_size)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


qrcode = cv2.QRCodeDetector()  # QRCode 偵測器

status, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)  # 辨識 QRCode
print("OK", status)
print("len", len(data))
print("data", data)
print("bbox", bbox)
print("rectified", rectified)

if status == True:
    for i in range(len(data)):
        text = data[i]  # QRCode 內容

        box = boxSize(bbox[i])  # QRCode 座標
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), RED, 2)  # 繪製外框
        print(box)
        print(text)
        # putText(10,10,"aaa",color=(0,0,255))                     # 顯示文字
        putText(box[0], box[3], text, color=RED)  # 顯示文字

cv2.imshow("OpenCV 11", image)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# barcode / QR code SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# captcha ST
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_captcha/captcha03.png"

image = cv2.imread(filename)  # 讀取本機圖片

plt.figure("影像處理", figsize=(16, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉為灰階

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
plt.title("轉為灰階")

_, image_gray_inv = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白

plt.subplot(223)
plt.imshow(cv2.cvtColor(image_gray_inv, cv2.COLOR_BGR2RGB))
plt.title("轉為反相黑白")

print(image_gray_inv.shape)
print(len(image_gray_inv))
print(len(image_gray_inv[3]))

for i in range(len(image_gray_inv)):  # i為每一列
    for j in range(len(image_gray_inv[i])):  # j為每一行
        if image_gray_inv[i][j] == 255:  # 顏色為白色
            count = 0
            for k in range(-2, 3):
                for l in range(-2, 3):
                    try:
                        if image_gray_inv[i + k][j + l] == 255:  # 若是白點就將count加1
                            count += 1
                    except IndexError:
                        pass
            if count <= 6:  # 週圍少於等於6個白點
                image_gray_inv[i][j] = 0  # 將白點去除

image_dilation = cv2.dilate(image_gray_inv, (8, 8), iterations=1)  # 圖形加粗 擴大使膨脹

plt.subplot(224)
plt.imshow(cv2.cvtColor(image_dilation, cv2.COLOR_BGR2RGB))
plt.title("擴大使膨脹")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# [OpenCV][Python]印出圖像中文字的位置及高寬
# 本文將說明如何去辨識出圖片文字​位置及高寬。


def read_posion(img):
    # 輸入背景黑色，物件白色的圖
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
    components = []
    # boxes_data = []
    for i in range(1, num_labels):  # 跳過背景
        x, y, w, h, _ = stats[i]
        components.append((x, y, w, h))

    components.sort(key=lambda c: c[0])  # 按 x 座標排序

    # 合併 x 軸在正負5範圍內的OCR
    merged_components = []
    current_component = list(components[0])

    for i in range(1, len(components)):
        if abs(components[i][0] - current_component[0]) <= 5:
            current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
            current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
            current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
            current_component[3] = (
                abs(components[i][1] - current_component[1]) + components[i][3]
            )  # h 取 Y2 - Y1 + H2
        else:
            merged_components.append(tuple(current_component[:4]))
            current_component = list(components[i][:4])

    # 合併最後一個OCR結果
    merged_components.append(tuple(current_component[:4]))

    return merged_components


filename = "data/_captcha/captcha04.png"

img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
box = read_posion(gray_img)

for i, data in enumerate(box):
    x, y, h, w = data
    # 印出OCR 位置，高寬
    print(f"第{i}個OCR，x:{x},y:{y},h:{h},w:{w}")


"""
函式詳細說明
函式定義和參數:
read_posion(img) 函式接受一個參數
img：輸入的二值化圖像，背景是黑色，物件是白色。
計算連通域:
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
使用 OpenCV 的 connectedComponentsWithStats 函數計算連通域
num_labels：連通域的數量。
labels：標籤圖，每個連通域有一個唯一的標籤。
stats：每個連通域的統計資料（x, y, w, h, area）。
_:忽略的中心點資料。
提取連通域並存入列表:
components = []
for i in range(1, num_labels):  # 跳過背景
    x, y, w, h, _ = stats[i]
    components.append((x, y, w, h))
遍歷 stats，跳過背景，提取每個連通域的位置信息和尺寸，存入 components 列表。
按 x 座標排序:
components.sort(key=lambda c: c[0])
將 components 按 x 座標進行排序。
合併相鄰的連通域:
merged_components = []
current_component = list(components[0])

for i in range(1, len(components)):
    if abs(components[i][0] - current_component[0]) <= 5:
        current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
        current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
        current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
        current_component[3] = abs(components[i][1] - current_component[1]) + components[i][3]  # h 取 Y2 - Y1 + H2
    else:
        merged_components.append(tuple(current_component[:4]))
        current_component = list(components[i][:4])

merged_components.append(tuple(current_component[:4]))
初始化 merged_components 列表和 current_component。
遍歷 components 列表，如果當前組件與前一組件的 x 座標差值在正負5範圍內，則合併它們。
合併後的結果存入 merged_components。
返回合併後的元件資訊:
return merged_components
返回合併後的元件資訊，這些資訊包括每個連通域的 x, y, w, h（左上角座標和寬高）。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# captcha SP
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
