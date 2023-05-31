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

