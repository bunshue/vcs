"""
WebCam 使用
錄影存檔

目前 webcam 僅 x64 電腦可用

視訊編碼的名稱、編碼字串、副檔名

編碼名稱	編碼字串	視訊檔副檔名
YUV		*"I420"		.avi
MPEG-1		*"PIMT"		.avi
MPEG-4		*"XVID"		.avi
MP4		*"MP4V"		.mp4
Ogg Vorbis	*"THEO"		.ogv

編碼格式
VideoWriter_fourcc('I', '4', '2', '0')	.avi	YUV編碼，相容性好，但是需較多記憶體空間 = VideoWriter_fourcc(*"I420")
VideoWriter_fourcc('P', 'I', 'M', 'I')	.avi	MPEG-1編碼
VideoWriter_fourcc('X', 'V', 'I', 'D')	.avi	MPEG-4編碼 = VideoWriter_fourcc(*'XVID')
VideoWriter_fourcc('T', 'H', 'E', 'O')	.ogb	Ogg Vobis編碼
VideoWriter_fourcc('F', 'L', 'V', '1')	.flv	Flash視訊

"""

import cv2
import sys
import time
import datetime

ESC = 27
SPACE = 32
RECORD_TIME_MINUTE = 10  # 分
RECORD_DATA_SIZE = 100  # MB

MODE_0 = 0  # 一直錄
MODE_1 = 1  # 一檔錄固定時間, ex 10分一檔
MODE_2 = 2  # 一檔錄固定檔案容量, ex 500M一檔
MODE_3 = 3  # 縮時錄影 Time-lapse Video

MODE = MODE_3
SPEED = 10  # N 倍速

#'XVID','DIVX','MJPG','I420'

# 第一種
# 用 XVID 格式存 avi 檔
record_filename = (
    "tmp1_webcam_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".avi"
)
ENCODING_TYPE = "XVID"  # 編碼器

"""
#第二種
# 用 MP4V 格式存 mp4 檔
record_filename = 'tmp2_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp4'
ENCODING_TYPE = 'MP4V'  # 編碼器

#第三種
# 用 MJPG 格式存 mp4 檔
record_filename = 'tmp3_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp4'
ENCODING_TYPE = 'MJPG'  # 編碼器

#第四種
# 用 MJPG 格式存 mov 檔
record_filename = 'tmp4_webcam_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mov'
ENCODING_TYPE = 'MJPG'  # 編碼器
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
print("最簡錄影, 一直錄, 按 ESC 離開")

if MODE == MODE_3:  # 縮時錄影
    print("縮時錄影,", SPEED, "倍速")

record_filename = (
    "tmp1_webcam_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".avi"
)

cap = cv2.VideoCapture(0)  # 打開攝影機
if not cap.isOpened():
    print("Could not open video device")
    sys.exit()
else:
    print("Video device opened")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 取得播放速率

record_time_st = time.time()
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("開始錄影時間 :", now)

# 建立視訊編碼 fourcc
ENCODING_TYPE = "XVID"  # 編碼器
fourcc = cv2.VideoWriter_fourcc(*ENCODING_TYPE)

# 建立影像寫入器 out
out = cv2.VideoWriter(record_filename, fourcc, fps, (width, height))

cnt = 0
while True:
    ret, frame = cap.read()  # 擷取一張影像
    if ret == False:
        print("無影像, 離開")
        break

    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    cv2.putText(
        frame, now, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA
    )

    cv2.imshow("WebCam2", frame)
    if MODE == MODE_3:  # 縮時錄影
        cnt += 1
        if cnt % SPEED == 0:  # N張存一張 => N倍速
            out.write(frame)  # 影像寫入影片檔
    else:
        out.write(frame)  # 影像寫入影片檔

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:  # ESC
        break

cap.release()  # 關閉攝影機
out.release()  # 關閉寫入器
cv2.destroyAllWindows()  # 關閉視窗

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("\n停止錄影時間 :", now)
record_time_elapsed = time.time() - record_time_st
print("錄影時間 :", int(record_time_elapsed), "秒")
print("存檔檔名 :", record_filename)

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("錄影, 按 SPACE 存圖, 按 ESC 離開")

cap = cv2.VideoCapture(0)  # 打開攝影機
if not cap.isOpened():
    print("Could not open video device")
    sys.exit()
else:
    print("Video device opened")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fps = cap.get(cv2.CAP_PROP_FPS)  # 取得播放速率

record_time_st = time.time()
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("開始錄影時間 :", now)
print("預計錄影時間 :", RECORD_TIME_MINUTE, "分")
print("錄影時間(分) :", end="")

# 建立視訊編碼 fourcc
fourcc = cv2.VideoWriter_fourcc(*ENCODING_TYPE)

# 建立影像寫入器 out
out = cv2.VideoWriter(record_filename, fourcc, fps, (width, height))

show_minitues_info = 0
while True:
    ret, frame = cap.read()  # 擷取一張影像
    if ret == False:
        print("無影像, 離開")
        break

    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    cv2.putText(
        frame, now, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA
    )

    cv2.imshow("WebCam2", frame)
    out.write(frame)  # 影像寫入影片檔

    record_time_elapsed = time.time() - record_time_st
    record_minute = int(record_time_elapsed // 60)
    if record_minute != show_minitues_info:
        show_minitues_info = record_minute
        print(record_minute, end=" ")
    if record_time_elapsed > 60 * RECORD_TIME_MINUTE:
        print("時間到 : ", RECORD_TIME_MINUTE, " 分, 重新錄一檔")
        record_time_st = time.time()
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print("開始錄影時間 :", now)
        print("預計錄影時間 :", RECORD_TIME_MINUTE, "分")
        print("錄影時間(分) :", end="")
        record_filename = (
            "tmp1_webcam_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".avi"
        )
        # 建立視訊編碼 fourcc
        fourcc = cv2.VideoWriter_fourcc(*ENCODING_TYPE)
        # 建立影像寫入器 out
        out = cv2.VideoWriter(record_filename, fourcc, fps, (width, height))

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:  # ESC
        break

cap.release()  # 關閉攝影機
out.release()  # 關閉寫入器
cv2.destroyAllWindows()  # 關閉視窗

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("\n停止錄影時間 :", now)
record_time_elapsed = time.time() - record_time_st
print("錄影時間 :", int(record_time_elapsed), "秒")
print("存檔檔名 :", record_filename)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(1)

# 建立視訊編碼 fourcc
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MPEG-4

# 建立影像寫入器 out
out = cv2.VideoWriter("tmp_movie_a.avi", fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)  # 寫入影片物件
        cv2.imshow("frame", frame)  # 顯示攝影鏡頭的影像
    k = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if k == ESC:  # 按 ESC 鍵, 結束
        break

cap.release()
out.release()
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


# 解析 Fourcc 格式資料的函數
def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print("Codec: " + codec)

# 無效
# 設定影像的尺寸大小
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))


""" 調整影片大小
frame = cv2.resize(frame, (WIDTH, HEIGHT))
frame = cv2.flip(frame, 1)
"""

# 改變圖片大小
# frame = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)

# 彩色轉灰階
# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

"""
elif k == ord('s'): # 若按下 s 鍵則存圖
    image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
    cv2.imwrite(image_filename, frame)
    print('已存圖, 檔案 :', image_filename)

img_1 = frame
img_2 = cv2.flip(img_1, 0)             # 上下翻轉
"""


# 若要錄成黑白影片 要 加上 isColor=False 參數設定
# 建立影像寫入器 out
out = cv2.VideoWriter(record_filename, fourcc, fps, (width, height), isColor=False)
# 且
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
out.write(gray)  # 將圖像寫入影片



"""

#留下錄影部分 比較之

record_filename = 'tmp_screen_recording1_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.avi'

#建立影像寫入器 out
out = cv2.VideoWriter(record_filename, cv2.VideoWriter_fourcc(*'XVID'), 1, ImageGrab.grab().size)  # 幀率為32，可以調節

        for _ in range(10)
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            out.write(imm)

        out.release()
        cv2.destroyAllWindows()
"""
