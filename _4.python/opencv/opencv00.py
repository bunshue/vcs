'''
OpenCV 基本使用

顯示圖片

播放檔案

'''
import cv2

#-----------------------------------------------------------------------------
#顯示圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('使用 OpenCV 顯示圖片')
image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Picture Viewer', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
#-----------------------------------------------------------------------------
#播放檔案
video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)
#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    if ret == True:
        #frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))    #調整畫面大小
        cv2.imshow('Video Player', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
#-----------------------------------------------------------------------------
