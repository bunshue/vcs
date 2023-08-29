import cv2 as cv
import matplotlib.pyplot as plt
import math
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def get_median(data):
    data.sort()
    half = len(data) // 2
    return data[half]

#计算灰度图像的中值滤波
def my_median_blur_gray(image, size):
    data = []
    sizepart = int(size/2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #首先判断所以是否超出范围，也可以事先对图像进行零填充
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data.append(image[i+ii-sizepart][j+jj-sizepart])
            #取每个区域内的中位数
            image[i][j] = int(get_median(data))
            data=[]
    return image

#计算彩色图像的中值滤波
def my_median_blur_RGB(image, size):
    (b ,r, g) = cv.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv.merge((blur_b, blur_r, blur_g))
    return result

if __name__ == '__main__':
    image_test1 = cv.imread('worm.jpg')
    #调用自定义函数
    my_image_blur_median = my_median_blur_RGB(image_test1, 5)
    #调用库函数
    computer_image_blur_median = cv.medianBlur(image_test1, 5)
    fig = plt.figure()
    fig.add_subplot(131)
    plt.title('原图')
    plt.imshow(image_test1)
    fig.add_subplot(132)
    plt.title('自定义函数滤波')
    plt.imshow(my_image_blur_median)
    fig.add_subplot(133)
    plt.title('库函数滤波')
    plt.imshow(computer_image_blur_median)
    plt.show()
