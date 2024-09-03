import cv2

def split_picture(filename):
    # 以灰度模式读取图片
    gray = cv2.imread(filename, 0)
    # 将图片的边缘变为白色
    height, width = gray.shape
    for i in range(width):
        gray[0, i] = 255
        gray[height-1, i] = 255
    for j in range(height):
        gray[j, 0] = 255
        gray[j, width-1] = 255
    # 中值滤波
    blur = cv2.medianBlur(gray, 3) #模板大小3*3   
    # 二值化
    ret,thresh1 = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)  
    contours, hierarchy = cv2.findContours(thresh1, 2, 2)
    flag = 1
    for cnt in contours:
        # 最小的外接矩形
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w*h >= 100:
            print((x,y,w,h))
            # 显示图片
            cv2.imwrite('tmp_char%s.jpg'%flag, thresh1[y:y+h, x:x+w])
            flag += 1

filename = 'data/captcha.jpg'
split_picture(filename)
