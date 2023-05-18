'''
OpenCV 畫圖

'''

#用 putText 繪製物件偵測的標籤

import cv2
import numpy as np

def drawBoundingBox(img, bboxs):
    for box in bboxs:
        x1,y1,x2,y2 = (box['x1'], box['y1'], box['x2'], box['y2'])
        label = box['label']
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 6)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        thickness = 1
        labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
        _x1 = x1 # bottomleft x of text
        _y1 = y1 # bottomleft y of text
        _x2 = x1+labelSize[0][0] # topright x of text
        _y2 = y1-labelSize[0][1] # topright y of text
        cv2.rectangle(img, (_x1,_y1), (_x2,_y2), (0,255,0), cv2.FILLED) # text background
        cv2.putText(img, label, (x1,y1), fontFace, fontScale, (0,0,0), thickness)
    return img

print('OpenCV 畫圖')
#-----------------------------------------------------------------------------
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), np.uint8)
#-----------------------------------------------------------------------------

image[:] = (128, 128, 128)

bboxs = []
box = {}
box['label'] = 'object 1'
box['x1'] = 40
box['y1'] = 40
box['x2'] = 180
box['y2'] = 180
bboxs.append(box)
box2 = {'label': 'object 2', 'x1': 300, 'y1': 200, 'x2': 600, 'y2': 440}
bboxs.append(box2)
drawBoundingBox(image, bboxs)


#-----------------------------------------------------------------------------
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------



