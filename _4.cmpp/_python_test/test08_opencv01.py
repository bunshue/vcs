import cv2
import numpy as np

filename = "C:\\______test_files\\picture1.jpg"

img = cv2.imread(filename)

#另存新檔
#cv2.imwrite('aaaa.bmp', img);

shape = img.shape
h = shape[0]    #高
w = shape[1]    #寬
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階

print("寬 = ",w,", 高 = ",h,", D = ",d)


#裁減圖片
import matplotlib.pyplot as plt #匯入模組
import matplotlib.image as img  #匯入模組
image = img.imread(filename)
plt.imshow(image)
plt.show()

x_l, x_r = 100, 200 #保留的部分，由左而右
y_u, y_d = 100, 200 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]
plt.imshow(cut_img)
plt.show()




'''
cv2.imshow('image', img)

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗
'''



