import cv2 as cv
import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#高斯滤波函数
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*math.pi*sigma**2)
#产生高斯滤波矩阵
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根据尺寸和sigma值计算高斯矩阵
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    #将高斯矩阵归一化
    blur_retric = blur_retric / blur_retric[0][0]
    #将高斯矩阵转换为整数
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩阵
    return blur_retric
#计算灰度图像的高斯滤波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #条件语句为判断模板对应的值是否超出边界
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data += image[i+ii-sizepart][j+jj-sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0
    #返回变换后的图像矩阵
    return image

#计算彩色图像的高斯滤波
def my_gaussion_blur_RGB(image, size, sigma):
    (b ,r, g) = cv.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv.merge((blur_b, blur_r, blur_g))
    return result

if __name__ == '__main__':
    image_test1 = cv.imread('lena.png')
    #进行高斯滤波器比较
    my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
    computer_image_blur_gaussion = cv.GaussianBlur(image_test1, (5, 5), 0.75)
    fig = plt.figure()
    fig.add_subplot(131)
    plt.title('原始图像')
    plt.imshow(image_test1)
    fig.add_subplot(132)
    plt.title('自定义高斯滤波器')
    plt.imshow(my_image_blur_gaussion)
    fig.add_subplot(133)
    plt.title('库高斯滤波器')
    plt.imshow(computer_image_blur_gaussion)
    plt.show()
