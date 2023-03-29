import cv2
filename = 'C:/______test_files/_video/鹿港.mp4'

video = cv2.VideoCapture(filename);
     
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
if int(major_ver)  < 3 :
    print(int(major_ver))   #XXXXX
    fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    print(int(major_ver))   #here
    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    print("data video.get(cv2.CAP_PROP_FPS) : {0}".format(video.get(cv2.CAP_PROP_FPS)))
    print("data video.get(cv2.CAP_PROP_POS_MSEC) : {0}".format(video.get(cv2.CAP_PROP_POS_MSEC)))#Current position of the video file in milliseconds.
    print("data video.get(cv2.CAP_PROP_POS_FRAMES) : {0}".format(video.get(cv2.CAP_PROP_POS_FRAMES)))#0-based index of the frame to be decoded/captured next.
    print("data video.get(cv2.CAP_PROP_POS_AVI_RATIO) : {0}".format(video.get(cv2.CAP_PROP_POS_AVI_RATIO)))#Relative position of the video file: 0=start of the film, 1=end of the film.
    print("data video.get(cv2.CAP_PROP_FRAME_WIDTH) : {0}".format(video.get(cv2.CAP_PROP_FRAME_WIDTH)))#Width of the frames in the video stream.
    print("data video.get(cv2.CAP_PROP_FRAME_HEIGHT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))#Height of the frames in the video stream.
    print("data video.get(cv2.CAP_PROP_FPS) : {0}".format(video.get(cv2.CAP_PROP_FPS)))#Frame rate.
    print("data video.get(cv2.CAP_PROP_FOURCC) : {0}".format(video.get(cv2.CAP_PROP_FOURCC)))#4-character code of codec. see VideoWriter::fourcc .
    print("data video.get(cv2.CAP_PROP_FRAME_COUNT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_COUNT)))#Number of frames in the video file.
    print("data video.get(cv2.CAP_PROP_FORMAT) : {0}".format(video.get(cv2.CAP_PROP_FORMAT)))#Format of the Mat objects returned by VideoCapture::retrieve().
    print("data video.get(cv2.CAP_PROP_MODE) : {0}".format(video.get(cv2.CAP_PROP_MODE)))#Backend-specific value indicating the current capture mode.
    video.release();



'''
import cv2

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)


while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 顯示圖片
  cv2.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()

'''

'''

import cv2
import time

 

cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print('Could not open video device')
else:
    print('Video device opened')

 

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

 

while(True):
  ret, frame = cap.read()

  # 將圖片轉為灰階
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #cv2.imwrite('test.jpg', frame)
 

  cv2.imshow('frame', frame )

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

 

cap.release()
cv2.destroyAllWindows()
'''

'''
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv2.namedWindow("live", cv2.WINDOW_AUTOSIZE); # 命名一個視窗，可不寫

while(True):
    # 擷取影像
    ret, frame = cap.read()
    print(ret)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顯示圖片
    cv2.imshow('live', frame)
    #cv2.imshow('live', gray)

    # 按下 q 鍵離開迴圈
    if cv2.waitKey(1) == ord('q'):
        break

# 釋放該攝影機裝置
cap.release()
cv2.destroyAllWindows()
'''

'''
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#cv2.namedWindow("live", cv2.WINDOW_AUTOSIZE); # 命名一個視窗，可不寫
while(True):
    # 擷取影像
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顯示圖片
    cv2.imshow('live', frame)
    #cv2.imshow('live', gray)

    # 按下 q 鍵離開迴圈
    if cv2.waitKey(1) == ord('q'):
        break

# 釋放該攝影機裝置
cap.release()
cv2.destroyAllWindows()

'''

import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()


