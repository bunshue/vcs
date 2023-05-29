'''
OpenCV 畫圖

'''

import time
import cv2
import numpy as np

print('OpenCV 畫圖')
#-----------------------------------------------------------------------------

filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'

#cv2.namedWindow("plot")
image = cv2.imread(filename)
cv2.line(image, (50, 50), (300, 300), (255, 0, 0), 2)
cv2.rectangle(image, (500, 20), (580, 100), (0, 255, 0), 3)
cv2.rectangle(image, (100, 300), (150, 360), (0, 0, 255), -1)
cv2.circle(image, (500, 300), 40, (255, 255, 0), -1)
pts = np.array([[300, 300], [300, 340], [350,320]], np.int32)
cv2.polylines(image, [pts], True, (0, 255, 255), 2)
cv2.putText(image, "My Bear", (350, 420), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)

filename = 'C:/_git/vcs/_1.data/______test_files2/image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.bmp'

#cv2之存圖
cv2.imwrite(filename, image)


#-----------------------------------------------------------------------------

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------



