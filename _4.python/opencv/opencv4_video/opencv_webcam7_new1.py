"""

新進  未歸類

"""

from opencv_common import *

from PIL import ImageSequence

print("------------------------------------------------------------")  # 60個

"""
print("OpenCV VideoCapture 04 兩個camera")
print("按 ESC 離開")

ratio = 3
border = 30
W = 640
H = 480

w = W // ratio
h = H // ratio
x_st = W - w - border
y_st = H - h - border

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap1.isOpened():
    print("開啟攝影機1失敗")
    exit()
if not cap2.isOpened():
    print("開啟攝影機2失敗")
    exit()

while True:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    img1 = cv2.resize(img1, (w, h))  # 縮小尺寸 小圖
    # img2 = cv2.resize(img2,(W, H))  # 縮小尺寸 大圖

    img2[y_st : y_st + h, x_st : x_st + w] = img1  # 將 img2 的特定區域換成 img1

    cv2.rectangle(
        img2, (x_st, y_st), (x_st + w, y_st + h), WHITE, 5
    )  # 繪製子影片的外框

    cv2.imshow("OpenCV 01", img2)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 05 N X N")
print("按 ESC 離開")

N = 3  # 設定要分成幾格, N X N
W = 640 * 1
H = 480 * 1

cap = cv2.VideoCapture(1)
output = np.zeros((H, W, 3), dtype="uint8")  # 產生 WxH 的黑色背景

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

w = W // N  # 計算分格之後的影像寬度
h = H // N  # 計算分格之後的影像高度
img_list = []  # 設定空串列，記錄每一格的影像
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (w, h))  # 縮小尺寸
    """ 2X2的寫法
    output[0:h, 0:w] = frame             # 將 output 的特定區域置換為 frame, 左上
    output[0:h, w:w*2] = frame             # 將 output 的特定區域置換為 frame, 右上
    output[h:h*2, 0:w] = frame             # 將 output 的特定區域置換為 frame, 左下
    output[h:h*2, w:w*2] = frame             # 將 output 的特定區域置換為 frame, 右下

    frame = cv2.flip(frame, 1)  # 左右相反
    """
    img_list.append(frame)  # 每次擷取影像時，將影像存入串列
    if len(img_list) > N * N:
        del img_list[0]  # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i % N  # 根據串列計算影像的 x 座標
        y = i // N  # 根據串列計算影像的 y 座標
        output[h * y : h * y + h, w * x : w * x + w] = img_list[i]  # 更新畫面

    cv2.imshow("OpenCV 02", output)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[: height // 2, : width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, : width // 2] = smaller_frame
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, width // 2 :] = smaller_frame

    cv2.imshow("OpenCV 12", image)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 11 按 SPACE 製作一個閃光燈拍照的效果")
print("按 ESC 離開")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h, w, 4), dtype="uint8")

a = 0  # 開始時 a 等於 0
while True:
    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break
    elif k == SPACE:
        a = 1  # 如果按下空白鍵，讓 a 等於 1

    if a == 0:
        output = img.copy()  # 如果 a 等於 0，複製來源圖片為 output
    else:
        # 111
        output = cv2.addWeighted(white, a, img, 1 - a, 0)  # 如果 a 等於 1，根據 a 套用權重
        a = a - 0.01  # a 不斷減少 0.01
        if a < 0:
            a = 0  # 如果 a 小於 0 就讓 a 等於 0

    cv2.imshow("OpenCV 04", output)  # 顯示圖片

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 12 存圖 按 SPACE 製作一個閃光燈拍照的效果")
print("按 ESC 離開")

cap = cv2.VideoCapture(1)

a = 0  # 白色圖片透明度

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")  # 如果讀取錯誤，印出訊息
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA
    w = frame.shape[1]
    h = frame.shape[0]
    frame = cv2.resize(frame, (w, h))  # 縮放尺寸
    white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 產生全白圖片

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break
    elif k == SPACE:  # 按下空白將 a 等於 1
        a = 1

    if a == 0:
        output = frame.copy()  # 如果 a 為 0，設定 output 變數為來源圖片的拷貝
    else:
        photo = frame.copy()  # 如果 a 不為 0，設定 photo 變數為來源圖片的拷貝
        # 222
        output = cv2.addWeighted(white, a, photo, 1 - a, 0)  # 計算權重，產生白色慢慢消失效果
        a = a - 0.1
        if a < 0:
            a = 0
            image_filename = (
                "tmp3_Image_"
                + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                + ".jpg"
            )
            cv2.imwrite(image_filename, photo)
            print("已存圖, 檔案 :", image_filename)

    cv2.imshow("OpenCV 05", output)  # 顯示圖片

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 13 存圖 按 SPACE 製作一個閃光燈拍照的效果 + 倒數三秒")
print("按 ESC 離開")

cap = cv2.VideoCapture(1)


def putText(source, x, y, text, scale=2.5, color=WHITE):
    org = (x, y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)


a = 0

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    w = frame.shape[1]
    h = frame.shape[0]
    frame = cv2.resize(frame, (w, h))
    white = 255 - np.zeros((h, w, 4), dtype="uint8")

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break
    elif k == SPACE:
        a = 1
        sec = 4  # 加入倒數秒數

    if a == 0:
        output = frame.copy()
    else:
        output = frame.copy()  # 設定 output 和 photo 變數
        photo = frame.copy()
        sec = sec - 0.05  # sec 不斷減少 0.05 ( 根據個人電腦效能設定，使其搭配 while 迴圈看起來像倒數一秒 )
        putText(output, 10, 70, str(int(sec)))  # 加入文字
        # 如果秒數小於 1
        if sec < 1:
            output = cv2.addWeighted(white, a, photo, 1 - a, 0)
            a = a - 0.1
            if a < 0:
                a = 0
                image_filename = (
                    "tmp4_Image_"
                    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                    + ".jpg"
                )
                cv2.imwrite(image_filename, photo)
                print("已存圖, 檔案 :", image_filename)

    cv2.imshow("OpenCV 06", output)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 14 加 logo")
print("按 ESC 離開")

W, H = 640, 480

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

logo_filename = "C:/_git/vcs/_4.python/_data/logo1.png"  # 400X400

logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (logo.shape[0]//4, logo.shape[1]//4))

size = logo.shape
print(size)
img = np.zeros((H, W, 3), dtype="uint8")
img[0:H, 0:W] = "255"

print('製作mask')
x_st, y_st = 10, 50  # logo貼上位置
img[y_st : y_st + size[0], x_st : x_st + size[1]] = logo
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask1 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask=mask1)
ret, mask2 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

print(mask2.shape)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整圖片尺寸
    bg = cv2.bitwise_and(frame, frame, mask=mask2)
    output = cv2.add(bg, logo)

    # output = cv2.bitwise_not(frame, mask=mask1)  # 套用 not 和遮罩
    # output = cv2.bitwise_not(output, mask=mask1)  # 再次套用 not 和遮罩，將色彩轉成原來的顏色

    cv2.imshow("OpenCV 07", output)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" many
print("OpenCV VideoCapture 16 Webcam影像轉成gif")
print("按 ESC 離開")

output = []  # 建立輸出的空串列

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整影片大小

    gif = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)  # 轉換顏色
    gif = Image.fromarray(gif)  # 轉換成 PIL 格式
    gif = gif.convert("RGB")  # 轉換顏色
    output.append(gif)  # 添加到 output

    cv2.imshow("OpenCV 08", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()

# 儲存為 gif 動畫
output[0].save(
    "tmp_webcam_image.gif",
    save_all=True,
    append_images=output[1:],
    duration=250,
    loop=0,
    disposal=2,
)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV VideoCapture 17 處理影片")
print("按 ESC 離開")

cap = cv2.VideoCapture(video_filename)  # 開啟影片

source = []  # 建立 source 空串列，記錄影格內容
cnt = 0

# 以迴圈從影片檔案讀取影格，並顯示出來
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Video Player", frame)
        if cnt % 30 == 0:  # 每 30 格取一格
            frame = cv2.resize(frame, (400, 300))  # 改變尺寸，加快處理效率
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 修改顏色為 RGBA
            source.append(frame)  # 記錄該圖片
        cnt = cnt + 1
    else:
        break

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("轉換成 gif")

for i in range(len(source)):
    for x in range(400):
        for y in range(300):
            r = source[i][y, x, 0]  # 該像素的紅色數值
            g = source[i][y, x, 1]  # 該像素的綠色數值
            b = source[i][y, x, 2]  # 該像素的藍色數值
            if r > 35 and r < 100 and g > 110 and g < 200 and b > 60 and b < 130:
                source[i][y, x, 3] = 0  # 如果在顏色範圍內，將透明度設為 0

print("frame 轉 gif")

n = 0
for i in source:
    frame = Image.fromarray(i)
    # frame.save(f"tmp_gif{n}.gif")
    n = n + 1

print("讀取 gif")

output = []
for i in range(n):
    frame = Image.open(f"tmp_gif{i}.gif")
    frame = frame.convert("RGBA")
    output.append(frame)

print("儲存 gif")

output[0].save(
    "tmp_test2.gif",
    save_all=True,
    append_images=output[1:],
    duration=100,
    loop=0,
    disposal=2,
)
print("OK")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_72 追蹤功能 按a開始 選取ROI, 按Enter確定")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"
video_filename = "D:/tennis.mp4"

tracker = cv2.TrackerCSRT_create()  # 創建追蹤器
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

    # 按下 a 開始選取
    if k == ord("a"):
        # 選取區域
        area = cv2.selectROI("ImageShow", frame, showCrosshair=False, fromCenter=False)
        print("選取區域 :", area)
        tracker.init(frame, area)  # 初始化追蹤器
        tracking = True  # 設定可以開始追蹤
    if tracking:
        success, point = tracker.update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
        if success:
            p1 = [int(point[0]), int(point[1])]
            p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
            cv2.rectangle(frame, p1, p2, RED, 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

    cv2.imshow("OpenCV 14", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
"""
print("OpenCV_ai_74 影片")

tracker_list = []
for i in range(3):
    tracker = cv2.TrackerCSRT_create()  # 創建三組追蹤器
    tracker_list.append(tracker)
colors = [RED, YELLOW, CYAN]  # 設定三個外框顏色
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(video_filename)  # 開啟影片

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

a = 0  # 刪減影片影格使用

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

    # 為了避免影片影格太多，所以採用 10 格取一格，加快處理速度
    if a % 10 == 0:
        if tracking == False:
            # 如果尚未開始追蹤，就開始標記追蹤物件的外框
            for i in tracker_list:
                area = cv2.selectROI(
                    "ImageShow", frame, showCrosshair=False, fromCenter=False
                )
                i.init(frame, area)  # 初始化追蹤器
            tracking = True  # 設定可以開始追蹤
        if tracking:
            for i in range(len(tracker_list)):
                success, point = tracker_list[i].update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
                if success:
                    p1 = [int(point[0]), int(point[1])]
                    p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
                    cv2.rectangle(frame, p1, p2, colors[i], 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

        cv2.imshow("OpenCV 15", frame)
    a = a + 1

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_75")

multiTracker = cv2.legacy.MultiTracker_create()  # 建立多物件追蹤器
tracking = False  # 設定追蹤尚未開始
colors = [RED, YELLOW]  # 建立外框色彩清單

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸加快速度

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

    # 按下 a 的時候開始標記物件外框
    if k == ord("a"):
        for i in range(2):
            area = cv2.selectROI(
                "ImageShow", frame, showCrosshair=False, fromCenter=False
            )
            # 標記外框後設定該物件的追蹤演算法
            tracker = cv2.legacy.TrackerCSRT_create()
            # 將該物件加入 multiTracker
            multiTracker.add(tracker, frame, area)
        # 設定 True 開始追蹤
        tracking = True
    if tracking:
        # 更新 multiTracker
        success, points = multiTracker.update(frame)
        a = 0
        if success:
            for i in points:
                p1 = (int(i[0]), int(i[1]))
                p2 = (int(i[0] + i[2]), int(i[1] + i[3]))
                # 標記物件外框
                cv2.rectangle(frame, p1, p2, colors[a], 3)
                a = a + 1
    cv2.imshow("OpenCV 16", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# simple color
"""
色彩辨識與追蹤
"""
color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(1)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

ratio = w / h
WIDTH = 320
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

    #### 在while中
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)  # 執行高斯模糊化

    #### 在while中
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #### 在while中
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt) < 100:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (x - 2, y - 2)
        p2 = (x + w + 4, y + h + 4)

        out = cv2.bitwise_and(hsv, hsv, mask=mask)

        cv2.rectangle(frame, p1, p2, RED, 2)
        cv2.rectangle(hsv, p1, p2, GREEN, 2)
        cv2.rectangle(out, p1, p2, BLUE, 2)

        frame = cv2.hconcat([frame, hsv, out])

    #### 在while中
    cv2.imshow("OpenCV 17", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按 ESC 離開")

cap = cv2.VideoCapture(1)

logo_filename = "C:/_git/vcs/_4.python/_data/panda.jpg"
logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (640, 480))  # 改變影像尺寸，符合疊加的圖片

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")  # 如果讀取錯誤，印出訊息
        break
    # cv2.imshow("OpenCV 18", img) 原圖顯示

    # addWeighted
    output = cv2.addWeighted(img, 0.6, logo, 0.4, 50)  # 疊加圖片
    cv2.imshow("OpenCV 19", output)

    k = cv2.waitKey(1)
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 背景移除

bs = cv2.bgsegm.createBackgroundSubtractorGMG()

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #### 在while內
    gray = bs.apply(frame)
    mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=10)

    #### 在while內
    cnts, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 200:
            continue
        # 畫出輪廓
        cv2.drawContours(frame, cnts, -1, YELLOW, 2)
        # 畫出矩型
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)

    #### 在while內
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    frame = cv2.hconcat([frame, mask])
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

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

# 設定參數 無效~~~~
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 設定寬度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 設定高度


ret, frame = cap.read()
# width = int(cap.get(3))
# height = int(cap.get(4))

print(width)
print(height)
print(cap.get(0))
print(cap.get(1))
print(cap.get(2))
print(cap.get(3))
print(cap.get(4))
