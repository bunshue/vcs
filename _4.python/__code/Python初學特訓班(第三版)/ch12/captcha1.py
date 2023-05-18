import cv2
import subprocess

img = cv2.imread("media\\bank.jpg")  #讀圖
cv2.namedWindow("Image")  
cv2.imshow("Image", img) #顯示圖形
cv2.waitKey (0) 
cv2.destroyWindow("Image")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉為灰階
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
cv2.imwrite("media\\bank_t.jpg", dilation)  #存檔
child = subprocess.Popen('tesseract media\\bank_t.jpg result', shell=True)  #OCR辨識
child.wait()
text = open('result.txt').read().strip()
print("驗證碼為 " + text)
