import cv2

# 開啟影片檔案
filename = 'C:/dddddddddd/____download/V000000119.mp4'
cap = cv2.VideoCapture(filename)

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
  ret, frame = cap.read()

  cv2.imshow('frame',frame)

  c = cv2.waitKey(1)
  if c == 27:     #ESC
    break
  elif c == ord('q'): # 若按下 q 鍵則離開迴圈
    break
  elif c == ord('s'): # 若按下 s 鍵則存圖
    cv2.imwrite('test.jpg', frame)

cap.release()
cv2.destroyAllWindows()


