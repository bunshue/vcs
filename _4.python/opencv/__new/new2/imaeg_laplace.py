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

original_image_test1 = cv.imread('data/lena.png',0)
#用原始图像减去拉普拉斯模板直接计算得到的边缘信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #确定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #条件语句为判断模板对应的值是否超出边界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result

#将计算结果限制为正值
def my_show_edge(model):
    #这里一定要用copy函数，不然会改变原来数组的值
    mid_model = model.copy()
    for i in range(mid_model.shape[0]):
        for j in range(mid_model.shape[1]):
            if mid_model[i][j] < 0:
                mid_model[i][j] = 0
            if mid_model[i][j] > 255:
                mid_model[i][j] = 255
    return mid_model

#调用自定义函数
result = my_laplace_sharpen(original_image_test1, my_type='big')
#绘制结果
fig = plt.figure()
fig.add_subplot(131)
plt.title('原始图像')
plt.imshow(original_image_test1)
fig.add_subplot(132)
plt.title('边缘检测')
plt.imshow(my_show_edge(result))
fig.add_subplot(133)
plt.title('锐化处理')
plt.imshow(my_laplace_result_add(original_image_test1,result))
plt.show()
