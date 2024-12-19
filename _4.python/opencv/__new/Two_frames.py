import cv2
import sys
import numpy as np

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# cap = cv2.VideoCapture(video_filename)  # 開啟影片
cap = cv2.VideoCapture("video.avi")  # 開啟影片

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
length = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

print("W :", W)
print("H :", H)
print("frames :", frames)
print("fps :", fps)
print("length :", length)

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

frameNum = 0

while True:
    # 获取一帧
    ret, frame = cap.read()  # 從影片擷取一張影像
    frameNum += 1
    if ret == True:
        frame = cv2.resize(frame, (W//3, H//3))
        tempframe = frame
        if frameNum == 1:  # 第1張圖
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)

        if frameNum >= 2:  # 第2張圖以後
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            currentframe = cv2.absdiff(currentframe, previousframe)
            median = cv2.medianBlur(currentframe, 3)
            ret, threshold_frame = cv2.threshold(
                currentframe, 20, 255, cv2.THRESH_BINARY
            )
            gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)  # 執行高斯模糊化

            cv2.imshow("Original", frame)
            cv2.imshow("Frame", currentframe)
            cv2.imshow("medianBlur", median)

            # 按键盘上的Q键退出
            if cv2.waitKey(33) & 0xFF == ord("q"):
                break
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
    else:
        print('播放結束')
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

