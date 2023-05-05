'''
OpenCV 畫圖

'''
import cv2
import numpy as np

print('OpenCV 畫圖')
#-----------------------------------------------------------------------------
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
img = np.zeros((H, W, 3))
#-----------------------------------------------------------------------------
print('畫直線')
px1 = BORDER
py1 = BORDER
px2 = W - BORDER
py2 = H - BORDER
cv2.line(img, (px1, py1), (px2, py2), 2)
cv2.line(img, (px1, py2), (px2, py1), 2)
#-----------------------------------------------------------------------------
print('畫矩形')
px1 = BORDER
py1 = BORDER
px2 = W - BORDER
py2 = H - BORDER
cv2.rectangle(img, (px1, py1), (px2, py2), (255, 255, 0), 2)
#-----------------------------------------------------------------------------
print('畫圓')
cx = int(W / 2)
cy = int(H / 2)
r = 100
cv2.circle(img, (cx, cy), r, (255, 255, 0), 2)
#-----------------------------------------------------------------------------
print('畫橢圓')
cx = int(W / 2)
cy = int(H / 2)
a = 250  #長軸
b = 100  #短軸
cv2.ellipse(img, (cx, cy), (a, b), 0, 0, 360, (255, 255, 0), 2)
#-----------------------------------------------------------------------------
print('畫多邊形')
px1 = int(W / 2)
py1 = 0
px2 = BORDER
py2 = BORDER
px3 = 0
py3 = int(H / 2)
px4 = BORDER
py4 = H - BORDER
px5 = int(W / 2)
py5 = H
px6 = W - BORDER
py6 = H - BORDER
px7 = W
py7 = int(H / 2)
px8 = W - BORDER
py8 = BORDER
pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6], [px7, py7], [px8, py8]])
cv2.polylines(img, [pts], True, (255, 255, 0), 2)   #True表示封口
#-----------------------------------------------------------------------------
print('畫字')
font = cv2.FONT_HERSHEY_SIMPLEX
x_st = BORDER
y_st = H - 70
cv2.putText(img, 'Only Show English', (x_st, y_st), font, 2, (255, 255, 0), 2)
#-----------------------------------------------------------------------------
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', img)

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------



