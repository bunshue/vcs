import cv2

original_img = cv2.imread('data/lena.png',0)
gray_img = cv2.resize(original_img,None,fx=0.8, fy=0.8,
                 interpolation = cv2.INTER_CUBIC) #图形太大了缩小一点

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))              #定义矩形结构元素(核大小为3效果好)
TOPHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_TOPHAT, kernel)     #顶帽运算
BLACKHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, kernel) #黒帽运算

bitwiseXor_gray = cv2.bitwise_xor(gray_img,TOPHAT_img)

#显示如下腐蚀后的图像
cv2.imshow("gray_img", gray_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)
cv2.imshow("bitwiseXor_gray",bitwiseXor_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
