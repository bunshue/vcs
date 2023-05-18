'''
OpenCV 畫圖

'''
import cv2
import numpy as np
import time

print('OpenCV 畫圖')
#-----------------------------------------------------------------------------
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), np.uint8)
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# Fill image with gray color(set each pixel to gray)
image[:] = (128, 128, 128)

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
cv2.putText(image, text, (100, 50), cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 3
thickness = 2
text = '7'
testSize = cv2.getTextSize(text, fontFace, fontScale, thickness)
#print(testSize)
bottomLeftX = 64-int(testSize[0][0]/2)
bottomLeftY = 64+int(testSize[0][1]/2)
cv2.putText(image, text, (bottomLeftX, bottomLeftY), fontFace,
  fontScale, (0, 255, 255), thickness, cv2.LINE_AA)


#-----------------------------------------------------------------------------
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------



