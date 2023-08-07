import cv2

filename = 'star.png'

print('顯示圖片')
image = cv2.imread(filename)	#讀取本機圖片

shape = image.shape
h = shape[0]    #高
w = shape[1]    #寬
h, w, d = image.shape   #d為dimension d = 3 全彩 d = 1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations = 1)
contours, hierarchy = cv2.findContours(
    edged, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cnt = cv2.approxPolyDP(cnt, 30, True)
hull = cv2.convexHull(cnt, returnPoints = False)
defects = cv2.convexityDefects(cnt, hull)
print('凸點數量：{}'.format(len(hull)))
print('凹點數量：{}'.format(len(defects)))

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(image, start, end, (0, 255, 0), 2)
    cv2.circle(image, far, 5, (0, 0, 255), -1)

cv2.imshow('image', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


