import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 图像锐化函数
def my_not_sharpen(image, k, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv.GaussianBlur(image, blur_size, blured_sigma) 
    # 注意不能直接用减法，对于图像格式结果为负时会自动加上256
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    # 两个矩阵中有一个不是图像格式，则结果就不会转换为图像格式
    sharpen_image = image + k * model   
    sharpen_image = cv.convertScaleAbs(sharpen_image)
    return sharpen_image

# 提取图像边界信息函数
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv.GaussianBlur(image, blur_size, blured_sigma)
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv.convertScaleAbs(model)
    return model

if __name__ == '__main__':
    '''读取原始图片'''
    original_image_lena = cv.imread('lena.png', 0)
    # 获得图像边界信息
    edge_image_lena = my_get_model(original_image_lena)
    # 获得锐化图像
    sharpen_image_lena = my_not_sharpen(original_image_lena, 3)
    # 显示结果
    plt.subplot(131)
    plt.title('原始图像')
    plt.imshow(original_image_lena)
    plt.subplot(132)
    plt.title('边缘检测')
    plt.imshow(edge_image_lena)
    plt.subplot(133)
    plt.title('非锐化')
    plt.imshow(sharpen_image_lena)
    plt.show()
