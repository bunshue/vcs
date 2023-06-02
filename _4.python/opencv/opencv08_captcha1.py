import cv2

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_opencv/captcha/captcha01.jpg'

image = cv2.imread(filename1)	#讀取本機圖片

cv2.namedWindow("Image")  
cv2.imshow("Image", image) #顯示圖形

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #轉為灰階
_, inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  #轉為反相黑白
for i in range(len(inv)):  #i為每一列
    for j in range(len(inv[i])):  #j為每一行
        if inv[i][j] == 255:  #顏色為白色
            count = 0 
            for k in range(-2, 3):
                for l in range(-2, 3):
                    try:
                        if inv[i + k][j + l] == 255:  #若是白點就將count加1
                            count += 1
                    except IndexError:
                        pass
            if count <= 6:  #週圍少於等於6個白點
                inv[i][j] = 0  #將白點去除

dilation = cv2.dilate(inv, (8,8), iterations=1)  #圖形加粗

filename2 = 'C:/_git/vcs/_1.data/______test_files2/catpcha_after.jpg'
cv2.imwrite(filename2, dilation)  #存檔

