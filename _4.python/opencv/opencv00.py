'''
OpenCV 基本使用

顯示圖片

播放檔案
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

'''
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

image = cv2.imread(filename)	#讀取本機圖片
#image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)	# -1 讀取本機圖片, 不改變顏色通道
#image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#  0 讀取本機圖片, 直接變成灰階
#image = cv2.imread(filename, cv2.IMREAD_COLOR)         #  1 讀取本機圖片, 改為BGR三通道(預設)

print('cv2.IMREAD_UNCHANGED =', cv2.IMREAD_UNCHANGED)   # -1
print('cv2.IMREAD_GRAYSCALE =', cv2.IMREAD_GRAYSCALE)   #  0
print('cv2.IMREAD_COLOR =', cv2.IMREAD_COLOR)           #  1(預設)

print('image.shape格式 :', type(image.shape))
print('image.shape內容 :', image.shape)

h = image.shape[0]    #高
w = image.shape[1]    #寬
d = image.shape[2]    #深
h, w, d = image.shape   #d為dimension d=3 全彩, d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

cv2.imshow('Picture Viewer', image) #顯示圖片
cv2.namedWindow('Picture Viewer')

#實例化8位圖
image_empty = np.zeros(image.shape, dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列
cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

image_copy = image.copy()
cv2.imshow("copy", image_copy)      #顯示圖片   #原圖拷貝

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階
cv2.imshow("gray", image_gray)      #顯示圖片   #原圖轉黑白

cv2.waitKey()
cv2.destroyAllWindows()

'''
print('------------------------------------------------------------')	#60個

'''
#播放檔案
video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)
#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    if ret == True:
        #frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))    #調整畫面大小
        cv2.imshow('Video Player', frame)
        if cv2.waitKey(1) == 27:
            #cv2.destroyAllWindows()
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
'''
print('------------------------------------------------------------')	#60個

#裁剪圖片

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
image = cv2.imread(filename)	#讀取本機圖片

# 裁切區域的 x 與 y 座標（左上角）
x_st = 100
y_st = 100

# 裁切區域的長度與寬度
w = 250
h = 250

# 裁切圖片
crop_image = image[y_st : y_st + h, x_st : x_st + w]

cv2.imshow("cropped", crop_image)   # 顯示圖片

image_empty = np.zeros(image.shape, dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列

#cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

#將擷取的圖貼到新建的黑圖
image_empty[y_st : y_st + h, x_st : x_st + w] = crop_image
cv2.imshow("cropped+new", image_empty)   # 顯示圖片

# 寫入圖檔, 偽執行
#cv2.imwrite('crop.jpg', crop_image)

cv2.waitKey()
cv2.destroyAllWindows()

import sys
sys.exit()

print('------------------------------------------------------------')	#60個

print('圖片裁剪縮放')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'

image = cv2.imread(filename)	#讀取本機圖片

x = 100
y = 100
w = 100
h = 100

# 寫入圖檔, 偽執行
#cv2.imwrite(filename2, image[y:y + h, x:x + w])

print('------------------------------------------------------------')	#60個

'''
#儲存檔案
image = cv2.imread(filename)	#讀取本機圖片

#寫入圖片檔案
#若要將 NumPy 陣列中儲存的圖片寫入檔案，可以使用 OpenCV 的 cv2.imwrite：
#cv2.imwrite 可透過圖片的副檔名來指定輸出的圖檔格式
# 寫入不同圖檔格式
cv2.imwrite('output.jpg', image)
cv2.imwrite('output.png', image)
cv2.imwrite('output.tiff', image)

#輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 5])
print('用matplotlib顯示圖片')

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
print('------------------------------------------------------------')	#60個

