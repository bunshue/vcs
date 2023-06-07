'''
OpenCV 基本使用

顯示圖片

播放檔案

'''
import cv2

#-----------------------------------------------------------------------------
#顯示圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('使用 OpenCV 顯示圖片')
image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Picture Viewer', image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
#-----------------------------------------------------------------------------
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
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
'''
#-----------------------------------------------------------------------------
#裁剪圖片
image = cv2.imread(filename)	#讀取本機圖片


#Python 與 OpenCV 裁切圖片教學
#OpenCV 裁切圖片

import cv2	#導入 OpenCV 模組

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
image = cv2.imread(filename)	#讀取本機圖片

#這裡用 OpenCV 讀取進來的圖片 image 其實就是 NumPy 的陣列，如果想要對圖片進行裁切，就用索引的方式，將指定的區域取出即可：

# 裁切區域的 x 與 y 座標（左上角）
x = 100
y = 100

# 裁切區域的長度與寬度
w = 250
h = 150

# 裁切圖片
crop_image = image[y:y+h, x:x+w]

#接著使用 OpenCV 的 imshow 顯示裁切的結果：

# 顯示圖片
cv2.imshow("cropped", crop_image)

# 若要將裁切的圖片儲存下來，可使用 imwrite 函數：
# 寫入圖檔
cv2.imwrite('crop.jpg', crop_image)

cv2.waitKey(0)



import cv2

print('圖片裁剪縮放')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'

image = cv2.imread(filename)	#讀取本機圖片

x = 100
y = 100
w = 100
h = 100

cv2.imwrite(filename2, image[y:y + h, x:x + w])

print('完成')





#裁剪圖片

import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要

x_l, x_r = 150, 350 #保留的部分，由左而右
y_u, y_d = 150, 400 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要




#-----------------------------------------------------------------------------

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




#-----------------------------------------------------------------------------




