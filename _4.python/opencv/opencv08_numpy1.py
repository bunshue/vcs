"""
opencv + numpy製作資料

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

import sys

W = 300
H = 300

print('------------------------------------------------------------')	#60個

image = np.random.randint(0, 256, size = [2, 4, 3], dtype = np.uint8)
print(image.shape)
rst=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(rst.shape)
#print("image = \n", image)
print("rst=\n",rst)
print("像素點(1,0)直接計算得到的值=", image[1,0,0] * 0.114 + image[1,0,1]*0.587 + image[1,0,2]*0.299)
print("像素點(1,0)使用公式cv2.cvtColor()轉換值=",rst[1,0])
"""
print(image[1,0,0])
print(image[1,0,1])
print(image[1,0,2])
"""

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[2,4],dtype=np.uint8)
print(img.shape)
rst=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(rst.shape)
#print("img=\n",img)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
#print("img=\n",img)
print("rgb=\n",rgb)
print("bgr=\n",bgr)

print('------------------------------------------------------------')	#60個

img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)

img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img2=\n",img2)

img3=cv2.add(img1,img2)
print("cv2.add(img1,img2)=\n",img3)

print('------------------------------------------------------------')	#60個

a=np.random.randint(0,255,(5,5),dtype=np.uint8)
b=np.zeros((5,5),dtype=np.uint8)
b[0:3,0:3]=255
b[4,4]=255
c=cv2.bitwise_and(a,b)
print("a=\n",a)
print("b=\n",b)
print("c=\n",c)

print('------------------------------------------------------------')	#60個

img1=np.ones((4,4),dtype=np.uint8)*3
print("img1=\n",img1)

img2=np.ones((4,4),dtype=np.uint8)*5
print("img2=\n",img2)

mask=np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4]=1
print("mask=\n",mask)

img3=np.ones((4,4),dtype=np.uint8)*66
print("初始值img3=\n",img3)

img3=cv2.add(img1,img2,mask=mask)
print("求和后img3=\n",img3)

print('------------------------------------------------------------')	#60個

img1=np.ones((4,4),dtype=np.uint8)*3
print("img1=\n",img1)

img2=np.ones((4,4),dtype=np.uint8)*5
print("img2=\n",img2)

img3=cv2.add(img1,img2)
print("cv2.add(img1,img2)=\n",img3)

img4=cv2.add(img1,6)
print("cv2.add(img1,6)\n",img4)

img5=cv2.add(6,img2)
print("cv2.add(6,img2)=\n",img5)

print('------------------------------------------------------------')	#60個

img1=np.ones((3,4),dtype=np.uint8)*100
img2=np.ones((3,4),dtype=np.uint8)*10
gamma=3
img3=cv2.addWeighted(img1,0.6,img2,5,gamma)
print(img3)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
print(img.shape)
cv2.imshow("demo",img)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#=========測試下OpenCV中藍色的HSV模式值=============
imgBlue=np.zeros([1,1,3],dtype=np.uint8)
imgBlue[0,0,0]=255
Blue=imgBlue
BlueHSV=cv2.cvtColor(Blue,cv2.COLOR_BGR2HSV)
print("Blue=\n",Blue)
print("BlueHSV=\n",BlueHSV)
#=========測試下OpenCV中綠色的HSV模式值=============
imgGreen=np.zeros([1,1,3],dtype=np.uint8)
imgGreen[0,0,1]=255
Green=imgGreen
GreenHSV=cv2.cvtColor(Green,cv2.COLOR_BGR2HSV)
print("Green=\n",Green)
print("GreenHSV=\n",GreenHSV)
#=========測試下OpenCV中紅色的HSV模式值=============
imgRed=np.zeros([1,1,3],dtype=np.uint8)
imgRed[0,0,2]=255
Red=imgRed
RedHSV=cv2.cvtColor(Red,cv2.COLOR_BGR2HSV)
print("Red=\n",Red)
print("RedHSV=\n",RedHSV)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[5,5],dtype=np.uint8)
min=100
max=200
mask = cv2.inRange(img, min, max)
print("img=\n",img)
print("mask=\n",mask)

print('------------------------------------------------------------')	#60個

img=np.ones([5,5],dtype=np.uint8)*9
mask =np.zeros([5,5],dtype=np.uint8)
mask[0:3,0]=1
mask[2:5,2:4]=1
roi=cv2.bitwise_and(img,img, mask= mask)
print("img=\n",img)
print("mask=\n",mask)
print("roi=\n",roi)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[2,3,3],dtype=np.uint8)
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print("img=\n",img)
print("bgra=\n",bgra)
b,g,r,a=cv2.split(bgra)
print("a=\n",a)
a[:,:]=125
bgra=cv2.merge([b,g,r,a])
print("bgra=\n",bgra)

print('------------------------------------------------------------')	#60個

img=np.random.randint(-256,256,size=[4,5],dtype=np.int16)
rst=cv2.convertScaleAbs(img)
print("img=\n",img)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img=np.zeros((5,5),np.uint8)
img[1:4,1:4]=1
kernel = np.ones((3,1),np.uint8)
erosion = cv2.erode(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("erosion=\n",erosion)

print('------------------------------------------------------------')	#60個

img=np.zeros((5,5),np.uint8)
img[2:3,1:4]=1
kernel = np.ones((3,1),np.uint8)
dilation = cv2.dilate(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("dilation\n",dilation)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

img = np.zeros((5,5),dtype=np.uint8)
img[0:6,0:6]=123
img[2:6,2:6]=126
print("img=\n",img)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("thd=\n",thd)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("otsu=\n",otsu)

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
(centerX,centerY) = (round(img.shape[1] / 2),round(img.shape[0] / 2))
#將圖像的中心作為圓心,實際值為=d/2
red = (0,0,255)#設置白色變量
for r in range(5,round(d/2),12):
    cv2.circle(img,(centerX,centerY),r,red,3)
    #circle(載體圖像，圓心，半徑，顏色)
cv2.imshow("Demo19.3",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
for i in range(0,100):
    centerX = np.random.randint(0,high = d)
    #生成隨機圓心X,確保在畫布img內
    centerY = np.random.randint(0,high = d)
    #生成隨機圓心Y,確保在畫布img內
    radius = np.random.randint(5,high = d/5)
    #生成隨機半徑，值范圍：[5,d/5)，最大半徑是d/5
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成隨機顏色，3個[0,256)的隨機數    
    cv2.circle(img,(centerX,centerY),radius,color,-1)
    #使用上述隨機數，在畫布img內畫圓
cv2.imshow("demo19.4",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
center=(round(d/2),round(d/2))
#注意數值類型，center=(d/2,d/2)不可以
size=(100,200)
#軸的長度
for i in range(0,10):
    angle = np.random.randint(0,361)
    #偏移角度    
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成隨機顏色，3個[0,256)的隨機數    
    thickness = np.random.randint(1,9)
    cv2.ellipse(img, center, size, angle, 0, 360, color,thickness)
cv2.imshow("demo19.5",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
pts=np.array([[200,50],[300,200],[200,350],[100,200]], np.int32)
#生成各個頂點,注意數據類型為int32
pts=pts.reshape((-1,1,2))
#第1個參數為-1, 表明這一維的長度是根據后面的維度的計算出來的。
cv2.polylines(img,[pts],True,(0,255,0),8)
#調用函數polylines完成多邊形繪圖，注意第3個參數控制多邊形封閉
# cv2.polylines(img,[pts],False,(0,255,0),8)  #不閉合的的多邊形
cv2.imshow("demo19.6",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,255,0),5)
cv2.imshow("demo19.7",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,150),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,250),font, 3,(0,255,0),15,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv2.imshow("demo19.7",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

def Demo(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("單擊了鼠標左鍵")
    elif event==cv2.EVENT_RBUTTONDOWN :
        print("單擊了鼠標右鍵")
    elif flags==cv2.EVENT_FLAG_LBUTTON:
        print("按住左鍵拖動了鼠標")
    elif event==cv2.EVENT_MBUTTONDOWN :
        print("單擊了中間鍵")
#創建名稱為Demo的響應（回調）函數OnMouseAction
#將回調函數Demo與窗口“Demo19.9”建立連接
img = np.ones((H, W, 3),np.uint8)*255
cv2.namedWindow('Demo19.9')
cv2.setMouseCallback('Demo19.9',Demo)     
cv2.imshow('Demo19.9',img)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p1x=x
        p1y=y
        p2x=np.random.randint(1,d-50)
        p2y=np.random.randint(1,d-50)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,2)
img = np.ones((d,d,3),dtype="uint8")*255
cv2.namedWindow('Demo19.10')
cv2.setMouseCallback('Demo19.10',draw)
while(1):
    cv2.imshow('Demo19.10',img)
    if cv2.waitKey(20)==27:
        break

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

def changeColor(x):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    img[:]=[b,g,r]
img=np.zeros((100,700,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',100,255,changeColor)
cv2.createTrackbar('G','image',0,255,changeColor)
cv2.createTrackbar('B','image',0,255,changeColor)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break   

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

Type=0  #閾值處理類型值
Value=0 #使用的閾值
def onType(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value,255, Type) 
    cv2.imshow(windowName,dst)
 
def onValue(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type) 
    cv2.imshow(windowName,dst)

o = cv2.imread("images/lena512.bmp",0)
windowName = "Demo19.13"  #窗體名
cv2.namedWindow(windowName)
cv2.imshow(windowName,o)
#創建兩個滑動條
tType = "Type"  #用來選取閾值處理類型的滾動條
tValue = "Value"    #用來選取閾值的滾動條
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tValue, windowName,0, 255, onValue) 

if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

"""
d=400
global thickness
thickness=-1
def fill(x):
    pass
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p1x=x
        p1y=y
        p2x=np.random.randint(1,d-50)
        p2y=np.random.randint(1,d-50)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,thickness)

img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
cv2.createTrackbar('R','image',0,1,fill)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        thickness=-1
    else:
        thickness=2        
    if k==27:
        break   

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

def changeColor(x):
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        img[:]=0
    else:
        img[:]=255
img=np.zeros((100,1000,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,1,changeColor)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break   

cv2.destroyAllWindows()
"""
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
