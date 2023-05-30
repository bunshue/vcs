'''
OpenCV 畫圖

'''
import cv2
import time
import numpy as np

print('OpenCV 畫圖')
#-----------------------------------------------------------------------------
# 無底圖作畫
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
image = np.zeros((H, W, 3))
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), np.uint8)

#有底圖作畫
filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
image = cv2.imread(filename)

#-----------------------------------------------------------------------------
#cv2.namedWindow("plot")
#-----------------------------------------------------------------------------
print('畫直線')
px1 = BORDER
py1 = BORDER
px2 = W - BORDER
py2 = H - BORDER
color = (0, 0, 255)  # 定義直線的顏色(B, G, R)
cv2.line(image, (px1, py1), (px2, py2), color, 2)
cv2.line(image, (px1, py2), (px2, py1), 2)  #無color, 黑色線
#-----------------------------------------------------------------------------
print('畫矩形')
px1 = BORDER
py1 = BORDER
px2 = W - BORDER
py2 = H - BORDER
#空心矩形 2
color = (0, 255, 0)  # 定義矩形的顏色(B, G, R)
cv2.rectangle(image, (px1, py1), (px2, py2), color, 2)
#實心矩形 -1
color = (0, 128, 128)  # 定義矩形的顏色(B, G, R)
cv2.rectangle(image, (px1 + 100, py1 + 100), (px2 - 100, py2 - 100), color, -1)
#-----------------------------------------------------------------------------
print('畫圓')
cx = int(W / 2)
cy = int(H / 2)
r = 100
#空心圓形 2
color = (255, 255, 0)  # 定義圓形的顏色(B, G, R)
cv2.circle(image, (cx, cy), r, color, 2)
#實心圓形 -1
color = (255, 255, 0)  # 定義圓形的顏色(B, G, R)
cv2.circle(image, (cx, cy), int(r / 3), color, -1)
#-----------------------------------------------------------------------------
print('畫橢圓')
cx = int(W / 2)
cy = int(H / 2)
a = 250  #長軸
b = 100  #短軸
cv2.ellipse(image, (cx, cy), (a, b), 0, 0, 360, (255, 255, 0), 2)
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
cv2.polylines(image, [pts], True, (255, 255, 0), 2)   #True表示封口
#-----------------------------------------------------------------------------
'''
pts = np.array([[300, 300], [300, 340], [350,320]], np.int32)
cv2.polylines(image, [pts], True, (0, 255, 255), 2)
'''
#-----------------------------------------------------------------------------
print('畫字')
font = cv2.FONT_HERSHEY_SIMPLEX

x_st = BORDER
y_st = H - 70
cv2.putText(image, 'Only Show English', (x_st, y_st), font, 2, (255, 255, 0), 2)

text = 'Hello, World!'
font_size = 1
line_width = 1
x_st = 20
y_st = 20
cv2.putText(image, text, (x_st, y_st), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 255), line_width, cv2.LINE_AA)


#-----------------------------------------------------------------------------

# Fill image with gray color(set each pixel to gray)
#image[:] = (128, 128, 128)

text = 'Hello, World!'
x_st = 0; #文字[左下角]的位置
y_st = 100;
font = cv2.FONT_HERSHEY_SIMPLEX
font = cv2.FONT_HERSHEY_PLAIN
font = cv2.FONT_HERSHEY_DUPLEX
font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_TRIPLEX
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

font_size = 1 #文字縮放比例
font_color = (0, 0, 255)    #B G R
font_thickness = 1 #文字線條粗細度
line_type = cv2.LINE_AA #文字線條樣式
bottomLeftOrigin = False;   #False: 從左上畫起, True:從左下畫起
cv2.putText(image, text, (x_st, y_st), font, font_size, font_color, font_thickness, line_type, bottomLeftOrigin)
#參數至少要寫到font_color前

#用 putText 繪製顯示系統當前時間
localtime = time.localtime()
text = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
cv2.putText(image, text, (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)

fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 3
thickness = 2
text = '7'
testSize = cv2.getTextSize(text, fontFace, fontScale, thickness)
#print(testSize)
bottomLeftX = 64-int(testSize[0][0]/2)
bottomLeftY = 64+int(testSize[0][1]/2)
cv2.putText(image, text, (bottomLeftX, bottomLeftY), fontFace, fontScale, (0, 255, 255), thickness, cv2.LINE_AA)



#-----------------------------------------------------------------------------
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)
#-----------------------------------------------------------------------------
print('存圖')
filename = 'C:/_git/vcs/_1.data/______test_files2/image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.bmp'
cv2.imwrite(filename, image)
#-----------------------------------------------------------------------------
print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------



