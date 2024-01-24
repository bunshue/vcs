import cv2

original_img0 = cv2.imread('data/lena.png')
original_img = cv2.imread('data/lena.png',0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))                  #定义矩形结构元素
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)     #顶帽运算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel) #黒帽运算

#显示图像
cv2.imshow("original_img0", original_img0)
cv2.imshow("original_img", original_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
