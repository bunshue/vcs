import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签

# 输入图像，输出提取的边缘信息
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape,dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    # 确定拉普拉斯模板的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # 计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 条件语句为判断模板对应的值是否超出边界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += image[i+ii-1][j+jj-1] * my_model_x[ii][jj]
                        result_y[i][j] += image[i+ii-1][j+jj-1] * my_model_y[ii][jj]
            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            if result[i][j] > 255:
                result[i][j] = 255
    return result


# 将边缘信息按一定比例加到原始图像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result


if __name__ == '__main__':
    '''读取原始图片'''
    original_image_lena= cv.imread('lena.png', 0)
    # 获得图像边界信息
    edge_image_lena = my_sobel_sharpen(original_image_lena)
    # 获得锐化图像
    sharpen_image_lena = my_result_add(original_image_lena, edge_image_lena, -0.5)
    # 显示结果
    plt.subplot(131)
    plt.title('原始图像')
    plt.imshow(original_image_lena)
    plt.subplot(132)
    plt.title('边缘检测')
    plt.imshow(edge_image_lena)
    plt.subplot(133)
    plt.title('梯度处理')
    plt.imshow(sharpen_image_lena)
    plt.show()
