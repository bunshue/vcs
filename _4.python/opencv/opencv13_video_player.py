import cv2

# 開啟影片檔案
filename = 'C:/dddddddddd/____download/V000000119.mp4'

'''
cap = cv2.VideoCapture(filename)

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
  ret, frame = cap.read()

  cv2.imshow('frame',frame)

  k = cv2.waitKey(1)
  if k == 27:     #ESC
    break
  elif k == ord('q'): # 若按下 q 鍵則離開迴圈
    break
  elif k == ord('s'): # 若按下 s 鍵則存圖
    cv2.imwrite('video_snapshot.jpg', frame)

cap.release()
cv2.destroyAllWindows()
'''


#播放视频，并把每帧保存成图片：

import cv2
#cap = cv2.VideoCapture(filename,'utf-8')
cap = cv2.VideoCapture(filename)

fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

success, frame = cap.read()
i = 0
'''
while success:
    cv2.imshow("video",frame)
    #cv2.waitKey(1000/int(fps))
    #cv2.imwrite("./img/%d.jpg" % i,frame)
    i = i + 1
    success, frame = cap.read()
'''


'''
filename = 'C:/_git/vcs/_1.data/______test_files1/_video/鹿港.mp4'

import cv2

video = cv2.VideoCapture(filename)   #, 'utf-8')

fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

success, frame = video.read()
i = 0
while success:
    cv2.imshow("video",frame)
    #cv2.waitKey(1000/int(fps))
    #cv2.waitKey(20)
    cv2.imwrite("C:/_git/vcs/_1.data/______test_files2/%05d.jpg" % i, frame)
    i = i + 1
    success, frame = video.read()
video.release();

print('共有' + str(i) + '張圖片')
'''



