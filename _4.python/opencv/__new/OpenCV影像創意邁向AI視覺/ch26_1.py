# ch26_1.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_10.py

# ch26_10.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.namedWindow("myVideo", 0)
        cv2.resizeWindow("myVideo", 300, 200)
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_11.py

# ch26_11.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
print(f"Frame 的寬度 = {width}")  # 輸出Frame 的寬度
print(f"Frame 的高度 = {height}")  # 輸出Frame 的高度
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_12.py

# ch26_12.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    cv2.imshow("Frame", frame)  # 顯示影像
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    video_fps = video.get(cv2.CAP_PROP_FPS)  # 速度
    video_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # 幀數
    c = cv2.waitKey(50)  # 等待時間
    if c == 27:  # 按 Esc 键
        break
print(f"Video 的寬度    = {width}")  # 輸出 Video 的寬度
print(f"Video 的高度    = {height}")  # 輸出 Video 的高度
print(f"Video 的速度    = {video_fps}")  # 輸出 Video 的速度
print(f"Video 的幀數    = {video_frames}")  # 輸出 Video 的幀數
video.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_13.py

# ch26_13.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 設定寬度
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 設定高度
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_14.py

# ch26_14.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 影片高度
counter = 1  # 幀數計數器
font = cv2.FONT_HERSHEY_SIMPLEX  # 字型
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        y = int(height - 50)  # Frames計數器位置
        cv2.putText(
            frame, "Frames  : " + str(counter), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示幀數
        seconds = round(counter / video_fps, 2)  # 計算秒數
        y = int(height - 10)  # Seconds計數器位置
        cv2.putText(
            frame, "Seconds : " + str(seconds), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示秒數
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    counter += 1  # 幀數加 1
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_15.py

# ch26_15.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 寬度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度
# 建立裁剪影片物件
fourcc = cv2.VideoWriter_fourcc(*"I420")  # 編碼
new_video = cv2.VideoWriter("out26_15.avi", fourcc, video_fps, (width, height))
counter = video_fps * 5  # 影片長度
while video.isOpened() and counter >= 0:
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        new_video.write(frame)  # 寫入新影片
        counter -= 1  # 幀數減 1

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_2.py

# ch26_2.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像
    # 轉灰階顯示
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Frame", gray_frame)  # 顯示灰階影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_3.py

# ch26_3.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像

    h_frame = cv2.flip(frame, 1)  # 水平翻轉
    cv2.imshow("Flip Frame", h_frame)  # 顯示水平翻轉
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_4.py

# ch26_4.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 13:  # 按 Enter 鍵
        cv2.imwrite("mypict.png", frame)  # 拍照
        cv2.imshow("My Picture", frame)  # 開視窗顯示
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_5.py

# ch26_5.py
import cv2

capture = cv2.VideoCapture(0)  # 初始化攝影功能
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MPEG-4
# 建立輸出物件
video_out = cv2.VideoWriter("out26_5.avi", fourcc, 20.0, (640, 480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        video_out.write(frame)  # 寫入影片物件
        cv2.imshow("frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
video_out.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_6.py

# ch26_6.py
import cv2

video = cv2.VideoCapture("out26_5.avi")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_7.py

# ch26_7.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_8.py

# ch26_8.py
import cv2

video = cv2.VideoCapture("iceocean2.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret == True:
        cv2.imshow("frame", frame)  # 顯示彩色影片
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray_frame", gray_frame)  # 顯示灰階影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch26\ch26_9.py

# ch26_9.py
import cv2

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
        c = cv2.waitKey(50)  # 可以控制撥放速度
    else:
        break
    if c == 32:  # 是否按 空白鍵
        cv2.waitKey(0)  # 等待按鍵發生
        continue
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
