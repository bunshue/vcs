import cv2

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
