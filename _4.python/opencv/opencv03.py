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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

print('------------------------------------------------------------')	#60個

window_name = 'Show Picture'

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片
cv2.imshow(window_name, image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('xxxx')
plt.show()

#cv2.imwrite('aaaaaaa.pgm', image) #無效????

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

print('------------------------------------------------------------')	#60個

print('使用matplotlib顯示圖片')
import matplotlib.pyplot as plt

image = cv2.imread(filename, 1)	  #讀取本機圖片, 0: 黑白圖片 1: 原色圖片

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap = 'gray', interpolation = 'bicubic')

plt.show()

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2a = 'C:/_git/vcs/_1.data/______test_files2/picture1a.jpg'
filename2b = 'C:/_git/vcs/_1.data/______test_files2/picture1b.jpg'

image1 = cv2.imread(filename1)	#讀取本機圖片
#image1 = cv2.imread(filename1, 1)
image2 = cv2.imread(filename1, 0)   #讀取本機圖片, 0: 黑白圖片 1: 原色圖片

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.imshow(image1)
#plt.title('xxxx')
plt.show()

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
plt.imshow(image2)
#plt.title('xxxx')
plt.show()

