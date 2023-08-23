import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

o=cv2.imread("lena.bmp",cv2.IMREAD_GRAYSCALE)
r1=cv2.pyrDown(o)
r2=cv2.pyrDown(r1)
r3=cv2.pyrDown(r2)
print("o.shape=",o.shape)
print("r1.shape=",r1.shape)
print("r2.shape=",r2.shape)
print("r3.shape=",r3.shape)
cv2.imshow("original",o)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread("lenas.bmp")
r1=cv2.pyrUp(o)
r2=cv2.pyrUp(r1)
r3=cv2.pyrUp(r2)
print("o.shape=",o.shape)
print("r1.shape=",r1.shape)
print("r2.shape=",r2.shape)
print("r3.shape=",r3.shape)
cv2.imshow("original",o)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread("lena.bmp")
down=cv2.pyrDown(o)
up=cv2.pyrUp(down)
diff=up-o   #构造diff图像，查看up与o的区别
print("o.shape=",o.shape)
print("up.shape=",up.shape)
cv2.imshow("original",o)
cv2.imshow("up",up)
cv2.imshow("difference",diff)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread("lena.bmp")
up=cv2.pyrUp(o)
down=cv2.pyrDown(up)
diff=down-o   #构造diff图像，查看down与o的区别
print("o.shape=",o.shape)
print("down.shape=",down.shape)
cv2.imshow("original",o)
cv2.imshow("down",down)
cv2.imshow("difference",diff)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

O=cv2.imread("lena.bmp")
G0=O
G1=cv2.pyrDown(G0)
G2=cv2.pyrDown(G1)
G3=cv2.pyrDown(G2)
L0=G0-cv2.pyrUp(G1)
L1=G1-cv2.pyrUp(G2)
L2=G2-cv2.pyrUp(G3)
print("L0.shape=",L0.shape)
print("L1.shape=",L1.shape)
print("L2.shape=",L2.shape)
cv2.imshow("L0",L0)
cv2.imshow("L1",L1)
cv2.imshow("L2",L2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

O=cv2.imread("lena.bmp")
G0=O
G1=cv2.pyrDown(G0)
L0=O-cv2.pyrUp(G1)
RO=L0+cv2.pyrUp(G1)  #通过拉普拉斯图像复原的原始图像
print("O.shape=",O.shape)
print("RO.shape=",RO.shape)
result=RO-O  #将o和ro做减法
#计算result的绝对值，避免求和时负负为正3+(-3)=0
result=abs(result)  
#计算result所有元素的和
print("原始图像O与恢复图像RO差值的绝对值和：",np.sum(result))   

print('------------------------------------------------------------')	#60個

O=cv2.imread("lena.bmp")
#=================生成高斯金字塔======================
G0=O
G1=cv2.pyrDown(G0)
G2=cv2.pyrDown(G1)
G3=cv2.pyrDown(G2)
#===============生成拉普拉斯金字塔====================
L0=G0-cv2.pyrUp(G1) #拉普拉斯金字塔第0层
L1=G1-cv2.pyrUp(G2) #拉普拉斯金字塔第1层
L2=G2-cv2.pyrUp(G3) #拉普拉斯金字塔第2层
#=================复原G0======================
RG0=L0+cv2.pyrUp(G1)  #通过拉普拉斯图像复原的原始图像G0
print("G0.shape=",G0.shape)
print("RG0.shape=",RG0.shape)
result=RG0-G0  #将RG0和G0做减法
#计算result的绝对值，避免求和时负负为正3+(-3)=0
result=abs(result)  
#计算result所有元素的和
print("原始图像G0与恢复图像RG0差值的绝对值和：",np.sum(result))   
#=================复原G1======================
RG1=L1+cv2.pyrUp(G2) #通过拉普拉斯图像复原G1
print("G1.shape=",G1.shape)
print("RG1.shape=",RG1.shape)
result=RG1-G1  #将o和ro做减法
print("原始图像G1与恢复图像RG1差值的绝对值和：",np.sum(abs(result)))
#=================复原G2======================
RG2=L2+cv2.pyrUp(G3) #通过拉普拉斯图像复原G2
print("G2.shape=",G2.shape)
print("RG2.shape=",RG2.shape)
result=RG2-G2  #将o和ro做减法
print("原始图像G2与恢复图像RG2差值的绝对值和：",np.sum(abs(result)))

print('------------------------------------------------------------')	#60個
