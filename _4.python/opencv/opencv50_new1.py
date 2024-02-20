"""


"""

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print('使用 cv2 顯示圖片')

image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('取兩圖的影像差異 diff')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/compare/compare1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/compare/compare2.jpg'

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

print('image1.shape內容 :', img1.shape)
print('image2.shape內容 :', img2.shape)


# 比較並顯示差異影像
diff = cv2.absdiff(img1, img2)

cv2.imshow('Difference', diff)

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread(filename)	#讀取本機圖片



# 畫圓
cv2.circle(image, (100, 100), 100, (0, 0, 255))

# 寫字
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(image, "AAAAAA", (10, 25), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

# 畫線
cv2.line(image, (0,0), (200,200), (0, 255, 0), 5, lineType=cv2.LINE_AA)


cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('疊合')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/ims02.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/ims03.bmp'

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)


blended = cv2.addWeighted(img1, 1, img2, 1, 0)

cv2.imshow('Surveyed', blended)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


