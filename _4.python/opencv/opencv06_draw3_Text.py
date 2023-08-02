'''
OpenCV 畫圖

'''
import cv2
import time
import numpy as np

print('----------------------------------------------------------------------')	#70個
print('OpenCV 畫圖')
#-----------------------------------------------------------------------------
W = 512 + 200
H = 512
#建立 512x512 的黑色畫布
image = np.zeros((H, W, 3), dtype = np.uint8)  #H, W
#用(B, G, R) = (255, 255, 255): 白色填滿畫布
image.fill(255) #將這個矩陣全部填入255 => 白色
#image[:] = [48, 213, 254]#將這個矩陣全部填入指定顏色
# Fill image with gray color(set each pixel to gray)
#image[:] = (128, 128, 128)

font = cv2.FONT_HERSHEY_SIMPLEX
line_type = cv2.LINE_AA #文字線條樣式

print('----------------------------------------------------------------------')	#70個
print('畫字')
text = 'Only Show English'
x_st = 100
y_st = H - 70
font_size = 2
color = (255, 255, 0)
line_width = 2
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width)
print('----------------------------------------------------------------------')	#70個
text = 'Hello, World!'
x_st = 20
y_st = 20
font_size = 1
color = (0, 0, 255)
line_width = 1
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)
print('----------------------------------------------------------------------')	#70個
#繪製顯示系統當前時間
localtime = time.localtime()
text = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
x_st = 100
y_st = 50
font_size = 1
color = (0, 255, 255)
line_width = 1
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)
print('----------------------------------------------------------------------')	#70個
text = '777'
x_st = 20
y_st = 20
font = cv2.FONT_HERSHEY_COMPLEX
font_size = 3
color = (0, 255, 255)
line_width = 2
testSize = cv2.getTextSize(text, font, font_size, line_width)
print(testSize)
bottomLeftX = 64-int(testSize[0][0]/2)
bottomLeftY = 64+int(testSize[0][1]/2)
cv2.putText(image, text, (bottomLeftX, bottomLeftY), font, font_size, color, line_width, line_type)
print('----------------------------------------------------------------------')	#70個
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
color = (0, 0, 255)    #B G R
line_width = 1 #文字線條粗細度
bottomLeftOrigin = False;   #False: 從左上畫起, True:從左下畫起
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type, bottomLeftOrigin)

print('----------------------------------------------------------------------')	#70個
fonts = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]

text = 'OpenCV'
x_st = 450
y_st = 50
font_size = 2
color = (0, 0, 0)
line_width = 2
for font in fonts:
    cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)
    y_st += 60
print('----------------------------------------------------------------------')	#70個
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)
#-----------------------------------------------------------------------------
print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------
