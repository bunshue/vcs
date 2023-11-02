'''
OpenCV 畫圖

'''

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import time

print('------------------------------------------------------------')	#60個

n = 300
image = np.zeros((n+1,n+1,3), np.uint8)
image = cv2.line(image,(0,0),(n,n),(255,0,0),3)
image = cv2.line(image,(0,100),(n,100),(0,255,0),1)
image = cv2.line(image,(100,0),(100,n),(0,0,255),6)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
#plt.title('xxxx')
plt.show()

print('------------------------------------------------------------')	#60個

n = 300
image = np.ones((n,n,3), np.uint8)*255
image = cv2.rectangle(image,(50,50),(n-100,n-50),(0,0,255),-1)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
#plt.title('xxxx')
plt.show()

print('------------------------------------------------------------')	#60個

thickness=-1
mode=1
d=400
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        a=np.random.randint(1,d-50)
        r=np.random.randint(1,d/5)
        angle = np.random.randint(0,361)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        if mode==1:
            cv2.rectangle(img,(x,y),(a,a),color,thickness)
        elif mode==2:
            cv2.circle(img,(x,y),r,color,thickness)
        elif mode==3:
            cv2.line(img,(a,a),(x,y),color,3)  
        elif mode==4:
            cv2.ellipse(img, (x,y), (100,150), angle, 0, 360,color,thickness)                  
        elif mode==5:
            cv2.putText(img,'OpenCV',(0,round(d/2)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2,color,5)    
img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('r'):
        mode=1
    elif k==ord('c'):
        mode=2
    elif k==ord('l'):
        mode=3
    elif k==ord('e'):
        mode=4
    elif k==ord('t'):
        mode=5
    elif k==ord('f'):
        thickness=-1
    elif k==ord('u'):
        thickness=3
    elif k==27:
        break   

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

