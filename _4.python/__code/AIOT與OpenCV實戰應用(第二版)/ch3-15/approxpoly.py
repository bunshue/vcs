import cv2

filename = 'poly.png'

print('顯示圖片')
image = cv2.imread(filename)	#讀取本機圖片

shape = image.shape
h = shape[0]    #高
w = shape[1]    #寬
h, w, d = image.shape   #d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations = 1)
contours, hierarchy = cv2.findContours(
    edged,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

RECT, HEXAGON = 0, 1

print('=== 處理前')
print('矩形點數量：{}'.format(len(contours[RECT])))
print('六邊形點數量：{}'.format(len(contours[HEXAGON])))

approx_rect = cv2.approxPolyDP(contours[RECT], 30, True)
approx_hex = cv2.approxPolyDP(contours[HEXAGON], 30, True)

print('=== 處理後')
print('矩形點數量：{}'.format(len(approx_rect)))
print('六邊形點數量：{}'.format(len(approx_hex)))

cv2.drawContours(image, [approx_rect], -1, (0, 0, 255), 5)
cv2.drawContours(image, [approx_hex], -1, (0, 0, 255), 5)

cv2.imshow('image', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

