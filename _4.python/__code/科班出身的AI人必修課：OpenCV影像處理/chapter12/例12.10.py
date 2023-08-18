import cv2

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
