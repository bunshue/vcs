import cv2 as cv
from matplotlib import pyplot as plt

# 用原始图像减去拉普拉斯模板直接计算得到的边缘信息
def my_laplace_result_add(image, model):
    result = image-model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

original_image_test1 = cv.imread('data/lena.png',0)
# 函数中的参数ddepth为输出图像的深度，也就是每个像素点是多少位的。
# CV_16S表示16位有符号数
computer_result = cv.Laplacian(original_image_test1,ksize=3,ddepth=cv.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

plt.show()
