import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

#输出边缘和结构信息

image = cv2.imread('contours.bmp')  
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
o=cv2.drawContours(image, contours, -1, (0, 0, 255), 5)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('contours.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
n=len(contours)
contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(
            contoursImg[i],contours,i,(255,255,255),5) 
    cv2.imshow("contours[" + str(i)+"]",contoursImg[i])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('loc3.jpg')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask=np.zeros(image.shape, np.uint8)
mask=cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)
cv2.imshow("mask", mask)
loc=cv2.bitwise_and(image, mask)    
cv2.imshow("location", loc)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('moments.bmp')
cv2.imshow("original", image) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
n=len(contours)
contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],contours,i,255,3) 
    cv2.imshow("contours[" + str(i)+"]",contoursImg[i]) 
print("观察各个轮廓的矩（moments）:")
for i in range(n):
    print("轮廓"+str(i)+"的矩:\n",cv2.moments(contours[i]))
print("观察各个轮廓的面积:")
for i in range(n):
    print("轮廓"+str(i)+"的面积:%d" %cv2.moments(contours[i])['m00'])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('contours.bmp')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  

cv2.imshow("original", image)
n=len(contours)
contoursImg=[]
for i in range(n):
    print("contours["+str(i)+"]面积=",cv2.contourArea(contours[i]))
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],
                                   contours,
                                   i,
                                   (255,255,255),
                                   3)
    cv2.imshow("contours[" + str(i)+"]",contoursImg[i])   

cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

#筛选出大于特定大小的轮廓

image = cv2.imread('contours.bmp')

cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
n=len(contours)
contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],
               contours,i,(255,255,255),3)
    if cv2.contourArea(contours[i])>15000:
        cv2.imshow("contours[" + str(i)+"]",contoursImg[i])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#筛选出大于特定大小的轮廓

#--------------读取及显示原始图像--------------------
image = cv2.imread('contours0.bmp')  
cv2.imshow("original", image)

#--------------获取轮廓--------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#--------------计算各个轮廓的长度和、平均长度--------------------
n=len(contours)   #获取轮廓个数
cntLen=[]           #存储各个轮廓的长度
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i],True))
    print("第"+str(i)+"个轮廓的长度:%d"%cntLen[i])
cntLenSum=np.sum(cntLen)  #各个轮廓长度和
cntLenAvr=cntLenSum/n    #各个轮廓长度平均值
print("各个轮廓的总长度为：%d"%cntLenSum)
print("各个轮廓的平均长度为：%d"%cntLenAvr)

#--------------显示超过平均值的轮廓--------------------
contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],
               contours,i,(255,255,255),3)
    if cv2.arcLength(contours[i],True)>cntLenAvr:
        cv2.imshow("contours[" + str(i)+"]",contoursImg[i])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cs1.bmp')  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
HuM1=cv2.HuMoments(cv2.moments(gray)).flatten()

print("cv2.moments(gray)=\n",cv2.moments(gray))
print("\nHuM1=\n",HuM1)
print("\ncv2.moments(gray)['nu20']+cv2.moments(gray)['nu02']=%f+%f=%f\n" 
      %(cv2.moments(gray)['nu20'],cv2.moments(gray)['nu02'],
        cv2.moments(gray)['nu20']+cv2.moments(gray)['nu02']))
print("HuM1[0]=",HuM1[0])
print("\nHu[0]-(nu02+nu20)=",
      HuM1[0]-(cv2.moments(gray)['nu20']+cv2.moments(gray)['nu02']))

print('------------------------------------------------------------')	#60個

#----------------计算图像1的Hu矩-------------------
image1 = cv2.imread('cs1.bmp')  
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)  
HuM1=cv2.HuMoments(cv2.moments(gray1)).flatten()
#----------------计算图像2的Hu矩-------------------
image2 = cv2.imread('cs3.bmp')  
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)  
HuM2=cv2.HuMoments(cv2.moments(gray2)).flatten()
#----------------计算图像3的Hu矩-------------------
image3 = cv2.imread('lena.bmp')  
gray3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)  
HuM3=cv2.HuMoments(cv2.moments(gray3)).flatten()

#---------打印图像1、图像2、图像3的特征值------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
print("cv2.moments(gray1)=\n",cv2.moments(gray1))
print("cv2.moments(gray2)=\n",cv2.moments(gray2))
print("cv2.moments(gray3)=\n",cv2.moments(gray3))
print("\nHuM1=\n",HuM1)
print("\nHuM2=\n",HuM2)
print("\nHuM3=\n",HuM3)
#---------计算图像1与图像2、图像3的Hu矩之差----------------
print("\nHuM1-HuM2=",HuM1-HuM2)
print("\nHuM1-HuM3=",HuM1-HuM3)
#---------显示图像----------------
cv2.imshow("original1", image1)
cv2.imshow("original2", image2)
cv2.imshow("original3", image3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#--------------读取3幅原始图像--------------------
image1 = cv2.imread('cs1.bmp')
image2 = cv2.imread('cs2.bmp')
image3 = cv2.imread('cc.bmp') 
#----------打印3幅原始图像的shape属性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
#--------------色彩空间转换-------------------- 
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY) 
#-------------进行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1,gray1,1,0.0)
ret1 = cv2.matchShapes(gray1,gray2,1,0.0)
ret2 = cv2.matchShapes(gray1,gray3,1,0.0)
#--------------打印差值--------------------
print("相同图像的matchShape=",ret0)
print("相似图像的matchShape=",ret1)
print("不相似图像的matchShape=",ret2)
#--------------显示3幅原始图像--------------------
cv2.imshow("original1", image1)
cv2.imshow("original2", image2)
cv2.imshow("original3", image3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#---------------读取并显示原始图像------------------ 
image = cv2.imread('cc.bmp')  
#---------------提取图像轮廓------------------ 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#---------------返回顶点及边长------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
print("顶点及长宽的点形式:")
print("x=",x)
print("y=",y)
print("w=",w)
print("h=",h)
#---------------仅有一个返回值的情况------------------
rect = cv2.boundingRect(contours[0])
print("\n顶点及长宽的元组（tuple）形式：")
print("rect=",rect)

print('------------------------------------------------------------')	#60個

#---------------读取并显示原始图像------------------
image = cv2.imread('cc.bmp')  
cv2.imshow("original", image)

#---------------提取图像轮廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#---------------构造矩形边界------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
cv2.drawContours(image, [brcnt], -1, (0, 0,255), 2)

#---------------显示矩形边界------------------
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#---------------读取并显示原始图像------------------ 
image = cv2.imread('cc.bmp')
cv2.imshow("original", image)

#---------------提取图像轮廓------------------ 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#---------------构造矩形边界------------------
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(image, (x,y), (x+w,y+h), (0, 0, 255), 2)

#---------------显示矩形边界------------------
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cc.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n",rect)
points = cv2.boxPoints(rect)
print("\n转换后的points：\n",points)
points = np.int0(points)  #取整
image=cv2.drawContours(image, [points], 0, (0, 0,255),2)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cc.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(x,y),radius = cv2.minEnclosingCircle(contours[0])
center = (int(x),int(y))
radius = int(radius)
cv2.circle(image,center,radius, (0, 0, 255),2)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cc.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original", image)
ellipse = cv2.fitEllipse(contours[0])
print("ellipse=",ellipse)
cv2.ellipse(image, ellipse,(0,255,0),3)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cc.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rows,cols = image.shape[:2]
[vx,vy,x,y] = cv2.fitLine(contours[0], cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(image, (cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('cc.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area,trgl = cv2.minEnclosingTriangle(contours[0])
print("area=",area)
print("trgl:",trgl)
for i in range(0, 3):
    print('x')
    #cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), (255,255,255), 2)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------读取并显示原始图像-------------------------------
image = cv2.imread('cc.bmp')
cv2.imshow("original", image)

#----------------获取轮廓-------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#----------------epsilon=0.1*周长-------------------------------
adp = image.copy()
epsilon = 0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.1",adp)

#----------------epsilon=0.09*周长-------------------------------
adp = image.copy()
epsilon = 0.09*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.09",adp)

#----------------epsilon=0.055*周长-------------------------------
adp = image.copy()
epsilon = 0.055*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.055",adp)

#----------------epsilon=0.05*周长-------------------------------
adp = image.copy()
epsilon = 0.05*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.05", adp)

#----------------epsilon=0.02*周长-------------------------------
adp = image.copy()
epsilon = 0.02*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.02",adp)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('contours.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])   #返回坐标值
print("returnPoints为默认值True时返回值hull的值：\n",hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False) #返回索引值
print("returnPoints为False时返回值hull的值：\n",hull2)

print('------------------------------------------------------------')	#60個

# --------------读取并绘制原始图像------------------
o = cv2.imread('hand.bmp')  
cv2.imshow("original",o)
# --------------提取轮廓------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
# --------------寻找凸包，得到凸包的角点------------------
hull = cv2.convexHull(contours[0])
# --------------绘制凸包------------------
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
# --------------显示凸包------------------
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------原图--------------------------
img = cv2.imread('hand.bmp')
cv2.imshow('original',img)
#----------------构造轮廓--------------------------
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255,0)
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_TREE,
                                             cv2.CHAIN_APPROX_SIMPLE)  
#----------------凸包--------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
print("defects=\n",defects)
#----------------构造凸缺陷--------------------------
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,0,255],2)
    cv2.circle(img,far,5,[255,0,0],-1)
#----------------显示结果--------------------------
cv2.imshow('result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('hand.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
#--------------凸包----------------------
image1=o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, (0, 255, 0), 2)
print("使用函数cv2.convexHull()构造的多边形是否是凸包：",
      cv2.isContourConvex(hull))
cv2.imshow("result1",image1)
#------------逼近多边形--------------------
image2=o.copy()
epsilon = 0.01*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
image2=cv2.drawContours(image2,[approx],0,(0,0,255),2)
print("使用函数cv2.approxPolyDP()构造的多边形是否是凸包：",
      cv2.isContourConvex(approx))
cv2.imshow("result2",image2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------原始图像-------------------------
o = cv2.imread('cs.bmp')
cv2.imshow("original",o)
#----------------获取凸包------------------------  
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
#----------------内部点A的距离-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部点B的距离-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#------------正好处于边缘上的点C的距离-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #测试边缘到底在哪里，然后再使用确定位置的
#----------------显示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------原始图像-------------------------
o = cv2.imread('cs.bmp')
cv2.imshow("original",o)
#----------------获取凸包------------------------ 
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
#----------------内部点A与多边形的关系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部点B与多边形的关系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#----------------边缘线上点C与多边形的关系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #测试边缘到底在哪里，然后再使用确定位置的
#----------------显示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#-----------原始图像o1边缘--------------------
o1 = cv2.imread('cs.bmp')
cv2.imshow("original1",o1)
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY) 
ret, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY) 
image,contours1, hierarchy = cv2.findContours(binary1,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE) 
cnt1 = contours1[0]
#-----------原始图像o2边缘--------------------
o2 = cv2.imread('cs3.bmp') 
cv2.imshow("original2",o2) 
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY) 
ret, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY) 
image,contours2, hierarchy = cv2.findContours(binary2,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt2 = contours2[0]
#-----------原始图像o3边缘--------------------
o3 = cv2.imread('hand.bmp') 
cv2.imshow("original3",o3) 
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY) 
ret, binary3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY) 
image,contours3, hierarchy = cv2.findContours(binary3,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt3 = contours3[0]
#-----------构造距离提取算子--------------------
sd = cv2.createShapeContextDistanceExtractor()
#-----------计算距离--------------------
d1 = sd.computeDistance(cnt1,cnt1)
print("自身距离d1=", d1)
d2 = sd.computeDistance(cnt1,cnt2)
print("旋转缩放后距离d2=", d2)
d3 = sd.computeDistance(cnt1,cnt3)
print("不相似对象距离d3=", d3)
#-----------显示距离--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#-----------读取原始图像--------------------
o1 = cv2.imread('cs.bmp')
o2 = cv2.imread('cs3.bmp') 
o3 = cv2.imread('hand.bmp') 
cv2.imshow("original1",o1)
cv2.imshow("original2",o2) 
cv2.imshow("original3",o3) 
#-----------色彩转换--------------------
gray1 = cv2.cvtColor(o1,cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(o2,cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(o3,cv2.COLOR_BGR2GRAY) 
#-----------阈值处理--------------------
ret, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY) 
ret, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY) 
ret, binary3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY) 
#-----------提取轮廓--------------------
image,contours1, hierarchy = cv2.findContours(binary1,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
image,contours2, hierarchy = cv2.findContours(binary2,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
image,contours3, hierarchy = cv2.findContours(binary3,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
#-----------构造距离提取算子--------------------
hd = cv2.createHausdorffDistanceExtractor()
#-----------计算距离--------------------
d1 = hd.computeDistance(cnt1,cnt1)
print("自身Hausdorff距离d1=", d1)
d2 = hd.computeDistance(cnt1,cnt2)
print("旋转缩放后Hausdorff距离d2=", d2)
d3 = hd.computeDistance(cnt1,cnt3)
print("不相似对象Hausdorff距离d3=", d3)
#-----------显示距离--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(o,(x,y),(x+w,y+h),(255,255,255),3)
aspectRatio = float(w)/h
print(aspectRatio)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
x,y,w,h = cv2.boundingRect(contours[0])
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cv2.rectangle(o,(x,y),(x+w,y+h),(255,0,0),3)
rectArea=w*h
cntArea=cv2.contourArea(contours[0])
extend=float(cntArea)/rectArea
print(extend)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('hand.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cntArea=cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
solidity=float(cntArea)/hullArea
print(solidity)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cntArea=cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4*cntArea/np.pi)
print(equiDiameter)
cv2.circle(o,(100,100),int(equiDiameter/2),(0,0,255),3) #展示等直径大小的圆
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('cc.bmp')
cv2.imshow("original",o)  
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
ellipse = cv2.fitEllipse(contours[0])
retval=cv2.fitEllipse(contours[0])
print("单个返回值形式：")
print("retval=\n",retval)
(x,y),(MA,ma),angle = cv2.fitEllipse(contours[0])
print("三个返回值形式：")
print("(x,y)=(",x,y,")")
print("(MA,ma)=(",MA,ma,")")
print("angle=",angle)
cv2.ellipse(o,ellipse,(0,0,255),2)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#------------生成一个都是0值的a-------------------
a=np.zeros((5,5),dtype=np.uint8)
#-------随机将其中10个位置上的数值设置为1------------
#---times控制次数
#---i,j是随机生成的行、列位置
#---a[i,j]=1,将随机挑选出来的位置上的值设置为1
for times in range(10):
    i=np.random.randint(0,5)
    j=np.random.randint(0,5)
    a[i,j]=1
#-------打印a，观察a内值的情况-----------
print("a=\n",a)
#------查找a内非零值的位置信息------------
loc=np.transpose(np.nonzero(a))
#-----将a内非零值的位置信息输出------------
print("a内非零值位置:\n",loc)

print('------------------------------------------------------------')	#60個

#-----------------读取原始图像----------------------
o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
#-----------------获取轮廓------------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[0]
#-----------------绘制空心轮廓------------------------
mask1 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask1,[cnt],0,255,2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=",pixelpoints1.shape)
print("pixelpoints1=\n",pixelpoints1)
cv2.imshow("mask1",mask1)
#-----------------绘制实心轮廓---------------------
mask2 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask2,[cnt],0,255,-1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=",pixelpoints2.shape)
print("pixelpoints2=\n",pixelpoints2)
cv2.imshow("mask2",mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#------------生成一个都是0值的a-------------------
a=np.zeros((5,5),dtype=np.uint8)
#-------随机将其中10个位置上的数值设置为1------------
#---times控制次数
#---i,j是随机生成的行、列位置
#---a[i,j]=1,将随机挑选出来的位置上的值设置为1
for times in range(10):
    i=np.random.randint(0,5)
    j=np.random.randint(0,5)
    a[i,j]=1
#-------打印a，观察a内值的情况-----------
print("a=\n",a)
#------查找a内非零值的位置信息------------
loc = cv2.findNonZero(a)
#-----将a内非零值的位置信息输出------------
print("a内非零值位置:\n",loc)

print('------------------------------------------------------------')	#60個

#-----------------读取原始图像----------------------
o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
#-----------------获取轮廓------------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[0]
#-----------------绘制空心轮廓------------------------
mask1 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask1,[cnt],0,255,2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=",pixelpoints1.shape)
print("pixelpoints1=\n",pixelpoints1)
cv2.imshow("mask1",mask1)
#-----------------绘制实心轮廓---------------------
mask2 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask2,[cnt],0,255,-1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=",pixelpoints2.shape)
print("pixelpoints2=\n",pixelpoints2)
cv2.imshow("mask2",mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('ct.png')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2]   #coutours[0]、coutours[1]是左侧字母R
#--------使用掩膜获取感兴趣区域的最值-----------------
#需要注意minMaxLoc处理的对象为灰度图像，本例中处理对象为灰度图像gray
#如果希望获取彩色图像的，需要提取各个通道，将每个通道独立计算最值
mask = np.zeros(gray.shape,np.uint8)
mask=cv2.drawContours(mask,[cnt],-1,255,-1)   
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray,mask = mask)
print("minVal=",minVal)
print("maxVal=",maxVal)
print("minLoc=",minLoc)
print("maxLoc=",maxLoc)
#--------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape,np.uint8)
masko=cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko) 
cv2.imshow("mask",loc)
#显示灰度结果
#loc=cv2.bitwise_and(gray,mask) 
#cv2.imshow("mask",loc)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#--------读取并显示原始图像-----------------
o = cv2.imread('ct.png')  
cv2.imshow("original",o)
#--------获取轮廓-----------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2] 
#--------使用掩膜获取感兴趣区域的均值----------------- 
mask = np.zeros(gray.shape,np.uint8)#构造mean所使用的掩膜，必须是单通道的
cv2.drawContours(mask,[cnt],0,(255,255,255),-1)
meanVal = cv2.mean(o,mask = mask)  #mask是区域，所以必须是单通道的
print("meanVal=\n",meanVal)
#--------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape,np.uint8)
cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko)
cv2.imshow("mask",loc)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('cs.bmp')  
#--------获取并绘制轮廓-----------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
mask = np.zeros(gray.shape,np.uint8)
cnt=contours[0] 
cv2.drawContours(mask,[cnt],0,255,-1)
#--------计算极值----------------- 
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
#--------计算极值----------------- 
print("leftmost=",leftmost)
print("rightmost=",rightmost)
print("topmost=",topmost)
print("bottommost=",bottommost)
#--------绘制说明文字----------------- 
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',leftmost, font, 1,(0,0,255),2)
cv2.putText(o,'B',rightmost, font, 1,(0,0,255),2)
cv2.putText(o,'C',topmost, font, 1,(0,0,255),2)
cv2.putText(o,'D',bottommost, font, 1,(0,0,255),2)
#--------绘制图像----------------- 
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




