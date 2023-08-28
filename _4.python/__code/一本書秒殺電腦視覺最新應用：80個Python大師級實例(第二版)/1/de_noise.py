import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import random
import cv2
import scipy.misc
import scipy.signal
import scipy.ndimage
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签

"""中值滤波函数"""
def medium_filter(im, x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]
"""均值滤波函数"""
def mean_filter(im, x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s

def convert_2d(r):
    n = 3
    # 3*3滤波器，每个系数都是1/9
    window = np.ones((n, n)) / n**2
    #使用滤波器卷积图像
    # mode = same 表示输出尺寸等于输入尺寸
    # boundary 表示采用对称边界条件处理图像边缘
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    return s.astype(np.uint8)
"""添加噪声"""
def add_salt_noise(img):
    rows, cols, dims = img.shape 
    R = np.mat(img[:, :, 0])
    G = np.mat(img[:, :, 1])
    B = np.mat(img[:, :, 2])
    Grey_sp = R * 0.299 + G * 0.587 + B * 0.114
    Grey_gs = R * 0.299 + G * 0.587 + B * 0.114
    snr = 0.9
    mu = 0
    sigma = 0.12    
    noise_num = int((1 - snr) * rows * cols)

    for i in range(noise_num):
        rand_x = random.randint(0, rows - 1)
        rand_y = random.randint(0, cols - 1)
        if random.randint(0, 1) == 0:
            Grey_sp[rand_x, rand_y] = 0
        else:
            Grey_sp[rand_x, rand_y] = 255    
    Grey_gs = Grey_gs + np.random.normal(0, 48, Grey_gs.shape)
    Grey_gs = Grey_gs - np.full(Grey_gs.shape, np.min(Grey_gs))
    Grey_gs = Grey_gs * 255 / np.max(Grey_gs)
    Grey_gs = Grey_gs.astype(np.uint8)
    # 中值滤波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))
    Grey_gs_mf = scipy.ndimage.median_filter(Grey_gs, (8, 8))
    # 均值滤波
    n = 3
    window = np.ones((n, n)) / n ** 2
    Grey_sp_me = convert_2d(Grey_sp)
    Grey_gs_me = convert_2d(Grey_gs)
    plt.subplot(231)
    plt.title('椒盐噪声')
    plt.imshow(Grey_sp, cmap='gray')
    plt.subplot(232)
    plt.title('高斯噪声')
    plt.imshow(Grey_gs, cmap='gray')
    plt.subplot(233)
    plt.title('椒盐噪声的中值滤波')
    plt.imshow(Grey_sp_mf, cmap='gray')
    plt.subplot(234)
    plt.title('高斯噪声的中值滤波')
    plt.imshow(Grey_gs_mf, cmap='gray')
    plt.subplot(235)
    plt.title('椒盐噪声的均值滤波')
    plt.imshow(Grey_sp_me, cmap='gray')
    plt.subplot(236)
    plt.title('高斯噪声的均值滤波')
    plt.imshow(Grey_gs_me, cmap='gray')
    plt.show()

def main():
    img = np.array(Image.open('LenaRGB.bmp'))  #导入图片
    add_salt_noise(img)

if __name__ == '__main__':
    main()
