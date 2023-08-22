import cv2

filename = 'coin.jpg'

cap = cv2.VideoCapture(filename)    #用VideoCapture讀取本機圖片

ret, frame = cap.read()

print('顯示原圖')
cv2.imshow('Picture Viewer1', frame) #顯示圖片

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (13, 13), 0)
edged = cv2.Canny(gray, 50, 150)

contours, hierarchy = cv2.findContours(
    edged.copy(), 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

out = frame.copy()
cv2.drawContours(out, contours, -1, (0, 0, 255), 3) #用紅框標示出來

frame = cv2.hconcat([frame, out])

cv2.imshow('Picture Viewer2', frame) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

