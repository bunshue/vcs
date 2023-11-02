'''
圖像金字塔

pyrDown

pyrUp


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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('------------------------------------------------------------')	#60個

print('顯示xxxx')
r1=cv2.pyrDown(o)
r2=cv2.pyrDown(r1)
r3=cv2.pyrDown(r2)
print("o.shape=",o.shape)
print("r1.shape=",r1.shape)
print("r2.shape=",r2.shape)
print("r3.shape=",r3.shape)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)

cv2.waitKey()
cv2.destroyAllWindows()

sys.exit()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_small.bmp'

o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r1=cv2.pyrUp(o)
r2=cv2.pyrUp(r1)
r3=cv2.pyrUp(r2)
print("o.shape=",o.shape)
print("r1.shape=",r1.shape)
print("r2.shape=",r2.shape)
print("r3.shape=",r3.shape)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
down=cv2.pyrDown(o)
up=cv2.pyrUp(down)
diff=up-o   #構造diff圖像，查看up與o的區別
print("o.shape=",o.shape)
print("up.shape=",up.shape)
cv2.imshow("up",up)
cv2.imshow("difference",diff)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
up=cv2.pyrUp(o)
down=cv2.pyrDown(up)
diff=down-o   #構造diff圖像，查看down與o的區別
print("o.shape=",o.shape)
print("down.shape=",down.shape)
cv2.imshow("down",down)
cv2.imshow("difference",diff)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
O=cv2.imread(filename)
print('顯示原圖')

print('顯示xxxx')
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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
O=cv2.imread(filename)
print('顯示原圖')

print('顯示xxxx')
G0=O
G1=cv2.pyrDown(G0)
L0=O-cv2.pyrUp(G1)
RO=L0+cv2.pyrUp(G1)  #通過拉普拉斯圖像復原的原始圖像
print("O.shape=",O.shape)
print("RO.shape=",RO.shape)
result=RO-O  #將o和ro做減法
#計算result的絕對值，避免求和時負負為正3+(-3)=0
result=abs(result)  
#計算result所有元素的和
print("原始圖像O與恢復圖像RO差值的絕對值和：",np.sum(result))   

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
O=cv2.imread(filename)
print('顯示原圖')

print('顯示xxxx')
#=================生成高斯金字塔======================
G0=O
G1=cv2.pyrDown(G0)
G2=cv2.pyrDown(G1)
G3=cv2.pyrDown(G2)
#===============生成拉普拉斯金字塔====================
L0=G0-cv2.pyrUp(G1) #拉普拉斯金字塔第0層
L1=G1-cv2.pyrUp(G2) #拉普拉斯金字塔第1層
L2=G2-cv2.pyrUp(G3) #拉普拉斯金字塔第2層
#=================復原G0======================
RG0=L0+cv2.pyrUp(G1)  #通過拉普拉斯圖像復原的原始圖像G0
print("G0.shape=",G0.shape)
print("RG0.shape=",RG0.shape)
result=RG0-G0  #將RG0和G0做減法
#計算result的絕對值，避免求和時負負為正3+(-3)=0
result=abs(result)  
#計算result所有元素的和
print("原始圖像G0與恢復圖像RG0差值的絕對值和：",np.sum(result))   
#=================復原G1======================
RG1=L1+cv2.pyrUp(G2) #通過拉普拉斯圖像復原G1
print("G1.shape=",G1.shape)
print("RG1.shape=",RG1.shape)
result=RG1-G1  #將o和ro做減法
print("原始圖像G1與恢復圖像RG1差值的絕對值和：",np.sum(abs(result)))
#=================復原G2======================
RG2=L2+cv2.pyrUp(G3) #通過拉普拉斯圖像復原G2
print("G2.shape=",G2.shape)
print("RG2.shape=",RG2.shape)
result=RG2-G2  #將o和ro做減法
print("原始圖像G2與恢復圖像RG2差值的絕對值和：",np.sum(abs(result)))

print('------------------------------------------------------------')	#60個
