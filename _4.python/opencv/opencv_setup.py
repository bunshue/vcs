
'''
OpenCV 基本設定

'''

import cv2

print('------------------------------------------------------------')	#60個
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'




'''

#保存圖片 質量為5 和 100
print('存圖, 質量為5')
cv2.imwrite("./1.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
print('存圖, 質量為100')
cv2.imwrite("./2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#png壓縮大小
print('存圖, 壓縮為0')
cv2.imwrite("./3.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
print('存圖, 壓縮為9')
cv2.imwrite("./4.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])



cv2.imwrite(filename2a, image1)
cv2.imwrite(filename2b, image2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
'''

#保存检测结果
#cv2.imwrite("re.jpg",image)





print('------------------------------------------------------------')	#60個
