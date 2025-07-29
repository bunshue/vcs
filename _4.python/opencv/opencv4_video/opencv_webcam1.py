"""
WebCam 使用

一般使用

目前 webcam 僅 win10/x64 電腦可用
"""

import datetime
from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("最簡易, 按 ESC 離開")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 取得影像寬度
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 取得影像高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 取得播放速率
print("Image Size: %d x %d, %d fps" % (w, h, fps))

# 更改視訊的解析度
# Webcam有支援的模式 以下的設定才會有用
# 設定影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    ret, frame = cap.read()

    if ret == False:
        print("無影像, 離開")
        break

    # 影像處理 ST 對稱 旋轉 裁切 灰階 邊緣 模糊 ...
    # frame = cv2.resize(frame, (WIDTH, HEIGHT))  # 調整影像大小
    # frame = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)
    # frame = cv2.flip(frame, 0)  # 上下顛倒
    # frame = cv2.flip(frame, 1)  # 左右相反
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # frame = cv2.Canny(frame, 50, 100)  # minVal=50, maxVal=100
    # frame = cv2.GaussianBlur(frame, (13, 13), 15)  # 高斯模糊
    # 影像處理 SP

    # 加上文字 ST
    current_time = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
    x_st, y_st = 50, 70
    cv2.rectangle(
        frame, (x_st - 12, y_st - 35), (x_st + 360, y_st + 15), GREEN, -1
    )  # 黑底
    text = current_time  # "English Only"
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.8
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(
        frame, text, (x_st, y_st), fontFace, fontScale, WHITE, thickness, lineType
    )
    # 加上文字 SP

    """
    # 裁出一塊, 另外顯示之 ST
    x_st, y_st, W, H = 0, 0, 320, 240
    frame2 = frame[y_st : y_st + H, x_st : x_st + W]  # 取出一塊
    cv2.imshow("WebCam_Cut", frame2)
    # 裁出一塊, 另外顯示之 SP
    """

    # 加 mask ST
    mask = np.zeros(frame.shape, dtype=np.uint8)  # 建立mask
    dd = 30
    mask[dd : int(h - dd), dd : int(w - dd)] = 255  # 設定mask, 先高後寬
    frame = cv2.bitwise_and(frame, mask)  # 執行AND運算
    # 加 mask SP

    # 將影像顯示出來
    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break
    elif k == ord("S") or k == ord("s"):  # 按下 S, 存圖
        filename = (
            "tmp_Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
        )
        cv2.imwrite(filename, frame)
        print("已存圖, 檔案 :", filename)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按 ESC 離開, 影像處理, fps")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    ret, frame = cap.read()

    if ret == False:
        print("無影像, 離開")
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
        frame_blur_pre = cv2.GaussianBlur(gray, (13, 13), 15)  # 高斯模糊

time_old = time.time()
while True:
    # begin_time = time.time()  # 計算fps
    ret, frame = cap.read()

    if ret == False:
        print("無影像, 離開")
        break

    # 原圖
    cv2.imshow("WebCam1", frame)

    # 灰階處理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
    cv2.imshow("WebCam2", gray)

    # 高斯模糊
    frame_blur = cv2.GaussianBlur(gray, (13, 13), 15)
    cv2.imshow("WebCam3", frame_blur)

    # 比較影像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
    frame_blur_now = cv2.GaussianBlur(gray, (13, 13), 15)  # 高斯模糊
    diff = cv2.absdiff(frame_blur_now, frame_blur_pre)  # 現在影像與前影像相減
    cv2.imshow("WebCam4", diff)  # 顯示相減後的影像
    frame_blur_pre = frame_blur_now.copy()  # 將現在影像設為前影像

    time_new = time.time()

    fps = 1 / (time_new - time_old)
    # print("{:.1f}".format(fps))
    time_old = time_new

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def image_process(roi):
    W = roi.shape[1]
    H = roi.shape[0]
    for j in range(H):
        for i in range(W):
            b = roi[j][i][0]
            g = roi[j][i][1]
            r = roi[j][i][2]
            gray = ((np.int16)(b) + (np.int16)(g) + (np.int16)(r)) // 3
            roi[j][i][2] = gray  # R
            roi[j][i][1] = gray  # G
            roi[j][i][0] = gray  # B
    return roi


print("擷取畫面的某一塊 做灰階處理 再貼回主畫面")

x_st, y_st = 640 - 100 - 10, 480 - 100 - 10
w, h = 100, 100
RECT = ((x_st, y_st), (x_st + w, y_st + h))
(left, top), (right, bottom) = RECT

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()

    # 取出子畫面
    roi1 = frame[top:bottom, left:right]
    roi2 = image_process(roi1)  # 對子畫面做影像處理
    # 貼回原畫面
    frame[top:bottom, left:right] = roi2

    # 標示出來
    cv2.rectangle(frame, RECT[0], RECT[1], GREEN, 2)

    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("移動偵測1")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

frame_pre = None  # 前影像, 預設是空的

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
        frame_now = cv2.GaussianBlur(gray, (13, 13), 5)  # 高斯模糊
        if frame_pre is not None:  # ←如果前影像不是空的, 就和前影像比對
            diff = cv2.absdiff(frame_now, frame_pre)  # 此影格與前影格的差異值
            ret, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)  # 門檻值
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  # 找到輪廓
            )
            if contours:  # 如果有偵測到輪廓
                # print(type(contours))
                print(contours)
                cv2.drawContours(frame, contours, -1, RED, 2)
                print("偵測到移動")
            else:
                print(".", end="")
                pass

        cv2.imshow("WebCam", frame)
        frame_pre = frame_now.copy()

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("移動偵測2")

cap = cv2.VideoCapture(0)

skip = 1  # 設定不比對的次數, 由於前影像是空的, 略過一次比對

while cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
        img_now = cv2.GaussianBlur(gray, (13, 13), 5)  # 高斯模糊
        if skip > 0:  # ←如果 skip 大於 0 就略過不和前影像比對
            skip -= 1  # 將 skip 次數減 1
        else:  # ←如果 skip==0 就和前影像比對
            diff = cv2.absdiff(img_now, img_pre)  # 此影格與前影格的差異值

            # 設定門檻值
            ret, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            # 找輪廓
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            # 如果有偵測到輪廓
            if contours:
                cv2.drawContours(img, contours, -1, RED, 2)
                print("偵測到移動")
                skip = 10  # ←略過 N 次不比對
            else:
                print(".", end="")
        cv2.imshow("WebCam", img)
        img_pre = img_now.copy()

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cv2.destroyAllWindows()
cap.release()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 新進
print("------------------------------------------------------------")  # 60個

from PIL import ImageSequence

print("------------------------------------------------------------")  # 60個
"""
print("兩個camera")
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

    cv2.rectangle(img2, (x_st, y_st), (x_st + w, y_st + h), WHITE, 5)  # 繪製子影片的外框

    cv2.imshow("OpenCV 01", img2)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("VideoCapture N X N")
print("按 ESC 離開")

N = 3  # 設定要分成幾格, N X N
W = 640 * 1
H = 480 * 1

cap = cv2.VideoCapture(0)

output = np.zeros((H, W, 3), dtype="uint8")  # 產生 WxH 的黑色背景

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

w = W // N  # 計算分格之後的影像寬度
h = H // N  # 計算分格之後的影像高度
img_list = []  # 設定空串列，記錄每一格的影像
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (w, h))  # 調整影像大小
    """ 2X2的寫法
    output[0:h, 0:w] = frame  # 將 output 的特定區域置換為 frame, 左上
    output[0:h, w:w*2] = frame  # 將 output 的特定區域置換為 frame, 右上
    output[h:h*2, 0:w] = frame  # 將 output 的特定區域置換為 frame, 左下
    output[h:h*2, w:w*2] = frame  # 將 output 的特定區域置換為 frame, 右下
    """
    img_list.append(frame)  # 每次擷取影像時，將影像存入串列
    if len(img_list) > N * N:
        del img_list[0]  # 如果串列長度超過可容納的影像數量，移除第一個項目
    for i in range(len(img_list)):
        x = i % N  # 根據串列計算影像的 x 座標
        y = i // N  # 根據串列計算影像的 y 座標
        output[h * y : h * y + h, w * x : w * x + w] = img_list[i]  # 更新畫面

    cv2.imshow("OpenCV 02", output)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("VideoCapture 2 X 2")
print("按 ESC 離開")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # 調整影像大小
    image[: height // 2, : width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, : width // 2] = smaller_frame
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, width // 2 :] = smaller_frame

    cv2.imshow("OpenCV 12", image)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按 SPACE 製作一個閃光燈拍照的效果")
print("按 ESC 離開")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
w = img.shape[1]
h = img.shape[0]
white = 255 - np.zeros((h, w, 4), dtype="uint8")

a = 0  # 開始時 a 等於 0
while True:
    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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

print("存圖 按 SPACE 製作一個閃光燈拍照的效果")
print("按 ESC 離開")

cap = cv2.VideoCapture(0)

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
    frame = cv2.resize(frame, (w, h))  # 調整影像大小
    white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 產生全白圖片

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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
            filename = (
                "tmp3_Image_"
                + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                + ".jpg"
            )
            cv2.imwrite(filename, photo)
            print("已存圖, 檔案 :", filename)

    cv2.imshow("OpenCV 05", output)  # 顯示圖片

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("存圖 按 SPACE 製作一個閃光燈拍照的效果 + 倒數三秒")
print("按 ESC 離開")

cap = cv2.VideoCapture(0)


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
    frame = cv2.resize(frame, (w, h))  # 調整影像大小
    white = 255 - np.zeros((h, w, 4), dtype="uint8")

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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
                filename = (
                    "tmp4_Image_"
                    + time.strftime("%Y%m%d_%H%M%S", time.localtime())
                    + ".jpg"
                )
                cv2.imwrite(filename, photo)
                print("已存圖, 檔案 :", filename)

    cv2.imshow("OpenCV 06", output)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("加 logo")
print("按 ESC 離開")

W, H = 640, 480  # 大圖
w, h = 100, 120  # 小圖
logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv.png"

logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (w, h))  # 調整影像大小

img = np.zeros((H, W, 3), dtype="uint8")
img[0:H, 0:W] = "255"

print("製作mask")
x_st, y_st = W - w - 20, H - h - 20  # logo貼上位置
img[y_st : y_st + h, x_st : x_st + w] = logo
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
ret, mask1 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
logo = cv2.bitwise_and(img, img, mask=mask1)
ret, mask2 = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

print(mask2.shape)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整影像大小
    bg = cv2.bitwise_and(frame, frame, mask=mask2)
    output = cv2.add(bg, logo)

    cv2.imshow("OpenCV 07", output)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" many
print("VideoCapture Webcam影像轉成gif")
print("按 ESC 離開")

output = []  # 建立輸出的空串列

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (640, 480))  # 調整影像大小

    gif = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)  # 轉換顏色
    gif = Image.fromarray(gif)  # 轉換成 PIL 格式
    gif = gif.convert("RGB")  # 轉換顏色
    output.append(gif)  # 添加到 output

    cv2.imshow("OpenCV 08", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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

print("處理影片, 按 ESC 離開")

cap = cv2.VideoCapture(video_filename)  # 開啟影片

source = []  # 建立 source 空串列，記錄影格內容
cnt = 0

# 以迴圈從影片檔案讀取影格，並顯示出來
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Video Player", frame)
        if cnt % 30 == 0:  # 每 30 格取一格
            frame = cv2.resize(frame, (400, 300))  # 改變尺寸，加快處理效率  # 調整影像大小
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 修改顏色為 RGBA
            source.append(frame)  # 記錄該圖片
        cnt = cnt + 1
    else:
        break

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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

# cv2 物體移動追蹤

# 開啟影片檔案
# video_filename = "D:/Carreno Busta vs Kei Nishikori Final Set Tie Break HD.mp4"
video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

cap = cv2.VideoCapture(video_filename)

tracker = cv2.TrackerCSRT_create()

xx, yy, ww, hh = 350, 50, 200, 250  # 設定追蹤物體

roi = None
while True:
    ret, frame = cap.read()

    # 指定追蹤物體
    if roi is None:
        roi = (xx, yy, ww, hh)
        tracker.init(frame, roi)

    """
    # 人為設定追蹤物體
    if roi is None:
        roi = cv2.selectROI("frame", frame)
        if roi != (0, 0, 0, 0):
            tracker.init(frame, roi)
            print(roi)
    """

    success, rect = tracker.update(frame)
    if success:
        (x, y, w, h) = [int(i) for i in rect]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 紅框

    xx, yy, ww, hh
    cv2.rectangle(frame, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 1)  # 綠框

    cv2.imshow("OpenCV", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_72 追蹤功能 按a開始 選取ROI, 按Enter確定")

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"
video_filename = "D:/tennis.mp4"

tracker = cv2.TrackerCSRT_create()  # 創建追蹤器
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度  # 調整影像大小

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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
print("------------------------------------------------------------")  # 60個

# 背景移除

# 開啟影片檔案
video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/vtest.avi"
# video_filename = "D:/Carreno Busta vs Kei Nishikori Final Set Tie Break HD.mp4"
# video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

cap = cv2.VideoCapture(video_filename)

bg = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17, 17), 0)  # 執行高斯模糊化

    if bg is None:
        bg = gray
        continue

    diff = cv2.absdiff(gray, bg)
    diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.erode(diff, None, iterations=2)
    diff = cv2.dilate(diff, None, iterations=2)

    cv2.imshow("OpenCV 2", diff)

    cnts, hierarchy = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow("OpenCV 1", frame)

    k = cv2.waitKey(100)  # 等待按鍵輸入 100 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
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
    #frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，加快速度  # 調整影像大小

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸加快速度  # 調整影像大小

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
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
# 色彩辨識與追蹤

color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 取得影像寬度
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 取得影像高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 取得播放速率
print("Image Size: %d x %d, %d fps" % (w, h, fps))

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()

ratio = w / h
WIDTH = 320
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))  # 調整影像大小
    frame = cv2.flip(frame, 1)  # 左右相反

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

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按 ESC 離開")

cap = cv2.VideoCapture(0)

logo_filename = "C:/_git/vcs/_4.python/_data/panda.jpg"
logo = cv2.imread(logo_filename)
logo = cv2.resize(logo, (640, 480))  # 改變影像尺寸，符合疊加的圖片  # 調整影像大小

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

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 背景移除

bs = cv2.bgsegm.createBackgroundSubtractorGMG()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 左右相反

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
    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入 1 msec
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 06 在影像上畫圖 按ESC離開")

cap = cv2.VideoCapture(0)

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像寬度
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

image = np.zeros((H, W, 4), dtype="uint8")

if not cap.isOpened():
    print("Cannot open camera")
    exit()


def OnMouseAction(event, x, y, flags, param):
    global dots, image  # 定義全域變數
    if flags == 1:  # 左鍵點擊
        if event == 1:
            dots.append([x, y])
        if event == 4:
            dots = []
        if event == 0 or event == 4:
            dots.append([x, y])
            x1 = dots[len(dots) - 2][0]
            y1 = dots[len(dots) - 2][1]
            x2 = dots[len(dots) - 1][0]
            y2 = dots[len(dots) - 1][1]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255, 255), 2)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

dots = []

while True:
    ret, frame = cap.read()  # 讀取影片的每一個影格
    if not ret:
        print("Cannot receive frame")
        break

    # 透過 for 迴圈合成影像
    for i in range(W):
        frame[:, i, 0] = frame[:, i, 0] * (1 - image[:, i, 3] / 255) + image[
            :, i, 0
        ] * (image[:, i, 3] / 255)
        frame[:, i, 1] = frame[:, i, 1] * (1 - image[:, i, 3] / 255) + image[
            :, i, 1
        ] * (image[:, i, 3] / 255)
        frame[:, i, 2] = frame[:, i, 2] * (1 - image[:, i, 3] / 255) + image[
            :, i, 2
        ] * (image[:, i, 3] / 255)

    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k == ord("r"):
        image = np.zeros((H, W, 4), dtype="uint8")  # Reset

    cv2.imshow("OpenCV", frame)

cap.release()  # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 07 擦亮影片 按ESC離開")

W = 640  # 定義影片寬度
H = 480  # 定義影像高度

dots = []  # 記錄座標
mask_b = np.zeros((H, W, 3), dtype="uint8")  # 產生黑色遮罩 -> 套用清楚影像
mask_w = np.zeros((H, W, 3), dtype="uint8")  # 產生白色遮罩 -> 套用模糊影像
mask_w[0:H, 0:W] = 255  # 白色遮罩背景為白色


# 滑鼠繪圖函式
def OnMouseAction(event, x, y, flags, param):
    global dots, mask  # 定義全域變數
    if flags == 1:  # 左鍵點擊
        if event == 1:
            dots.append([x, y])
        if event == 4:
            dots = []
        if event == 0 or event == 4:
            dots.append([x, y])
            x1 = dots[len(dots) - 2][0]
            y1 = dots[len(dots) - 2][1]
            x2 = dots[len(dots) - 1][0]
            y2 = dots[len(dots) - 1][1]
            cv2.line(mask_w, (x1, y1), (x2, y2), BLACK, 50)  # 在白色遮罩上畫出黑色線條
            cv2.line(mask_b, (x1, y1), (x2, y2), WHITE, 50)  # 在黑色遮罩上畫出白色線條


cv2.imshow("OpenCV", mask_b)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    frame = cv2.resize(frame, (W, H))  # 縮小尺寸，加快速度
    frame = cv2.flip(frame, 1)  # 翻轉影像
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
    frame2 = frame.copy()  # 複製影像
    frame2 = cv2.blur(frame, (55, 55))  # 套用模糊

    mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    frame = cv2.bitwise_and(frame, frame, mask=mask1)  # 清楚影像套用黑遮罩
    mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    frame2 = cv2.bitwise_and(frame2, frame2, mask=mask2)  # 模糊影像套用白遮罩

    output = cv2.add(frame, frame2)  # 合併影像

    cv2.imshow("OpenCV", output)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()


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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 取得影像寬度
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 取得影像高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 取得播放速率
print("Image Size: %d x %d, %d fps" % (w, h, fps))


# 無效
# 設定影像的尺寸大小
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)


## Capture the background in range of 60
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)


## Open and Dilate the mask image
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

## Create an inverted mask to segment out the red color from the frame
mask2 = cv2.bitwise_not(mask1)

## Segment the red color part out of the frame using bitwise and with the inverted mask
res1 = cv2.bitwise_and(image, image, mask=mask2)

# frame = np.flip(frame, axis=1)  #左右顛倒

res2 = cv2.bitwise_and(background, background, mask=mask1)
finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)

# W = int(cap.get(3))
# H = int(cap.get(4))

output = cv2.bitwise_not(frame, mask=mask1)  # 套用 not 和遮罩
output = cv2.bitwise_not(output, mask=mask1)  # 再次套用 not 和遮罩，將色彩轉成原來的顏色
