# 哈尔小波变换

import cv2
import numpy as np

imgA = cv2.imread("data/a.tif")  # 载入图片A
imgB = cv2.imread("data/b.tif")  # 载入图片B
heigh, wide, channel = imgA.shape  # 获取图像的高、宽、通道数

"""临时变量、存储哈尔小波处理后的数据"""
tempA1 = []
tempA2 = []
tempB1 = []
tempB2 = []
waveImgA = np.zeros((heigh, wide, channel), np.float32)  # 存储A图片小波处理后数据的变量
waveImgB = np.zeros((heigh, wide, channel), np.float32)  # 存储B图片小波处理后数据的变量
# 水平方向的哈尔小波处理，对图片的B、G、R三个通道分别遍历进行
for c in range(channel):
    for x in range(heigh):
        for y in range(0, wide, 2):
            # 将图片A小波处理后的低频存储在tempA1中
            tempA1.append((float(imgA[x, y, c]) + float(imgA[x, y + 1, c])) / 2)
            # 将图片A小波处理后的高频存储在tempA2中
            tempA2.append(
                (float(imgA[x, y, c]) + float(imgA[x, y + 1, c])) / 2
                - float(imgA[x, y, c])
            )
            # 将图片B小波处理后的低频存储在tempB1中
            tempB1.append((float(imgB[x, y, c]) + float(imgB[x, y + 1, c])) / 2)
            # 将图片B小波处理后的高频存储在tempB2中
            tempB2.append(
                (float(imgB[x, y, c]) + float(imgB[x, y + 1, c])) / 2
                - float(imgB[x, y, c])
            )
        # 小波处理完图片A每一个水平方向数据统一保存在tempA1中
        tempA1 = tempA1 + tempA2
        # 小波处理完图片B每一个水平方向数据统一保存在tempB1中
        tempB1 = tempB1 + tempB2
        for i in range(len(tempA1)):
            # 图片A水平方向前半段存储低频，后半段存储高频
            waveImgA[x, i, c] = tempA1[i]
            # 图片B水平方向前半段存储低频，后半段存储高频
            waveImgB[x, i, c] = tempB1[i]
        tempA1 = []  # 当前水平方向数据处理完之后，临时变量重置
        tempA2 = []
        tempB1 = []
        tempB2 = []
# 垂直方向哈尔小波处理，与水平方向同理
for c in range(channel):
    for y in range(wide):
        for x in range(0, heigh - 1, 2):
            tempA1.append((float(waveImgA[x, y, c]) + float(waveImgA[x + 1, y, c])) / 2)
            tempA2.append(
                (float(waveImgA[x, y, c]) + float(waveImgA[x + 1, y, c])) / 2
                - float(waveImgA[x, y, c])
            )
            tempB1.append((float(waveImgB[x, y, c]) + float(waveImgB[x + 1, y, c])) / 2)
            tempB2.append(
                (float(waveImgB[x, y, c]) + float(waveImgB[x + 1, y, c])) / 2
                - float(waveImgB[x, y, c])
            )
        tempA1 = tempA1 + tempA2
        tempB1 = tempB1 + tempB2
        for i in range(len(tempA1)):
            waveImgA[i, y, c] = tempA1[i]
            waveImgB[i, y, c] = tempB1[i]
        tempA1 = []
        tempA2 = []
        tempB1 = []
        tempB2 = []
# 求以x,y为中心的5x5矩阵的方差，  “//”在python3中表示整除，没有小数，“/”在python3中会有小数，  python2中“/”即可，“//”也行都表示整除
varImgA = np.zeros((heigh // 2, wide // 2, channel), np.float32)  # 将图像A中低频数据求方差之后存储的变量
varImgB = np.zeros((heigh // 2, wide // 2, channel), np.float32)  # 将图像B中低频数据求方差之后存储的变量
for c in range(channel):
    for x in range(heigh // 2):
        for y in range(wide // 2):
            # 对图片边界(或临近)的像素点进行处理
            if x - 3 < 0:
                up = 0
            else:
                up = x - 3
            if x + 3 > heigh // 2:
                down = heigh // 2
            else:
                down = x + 3
            if y - 3 < 0:
                left = 0
            else:
                left = y - 3
            if y + 3 > wide // 2:
                right = wide // 2
            else:
                right = y + 3
            # 求图片A以x,y为中心的5x5矩阵的方差，mean表示平均值，var表示方差
            meanA, varA = cv2.meanStdDev(waveImgA[up:down, left:right, c])
            # 求图片B以x,y为中心的5x5矩阵的方差，
            meanB, varB = cv2.meanStdDev(waveImgB[up:down, left:right, c])
            varImgA[x, y, c] = varA  # 将图片A对应位置像素的方差存储在变量中
            varImgB[x, y, c] = varB  # 将图片B对应位置像素的方差存储在变量中
# 求两图的权重
weightImgA = np.zeros((heigh // 2, wide // 2, channel), np.float32)  # 图像A存储权重的变量
# 图像B存储权重的变量
weightImgB = np.zeros((heigh // 2, wide // 2, channel), np.float32)
for c in range(channel):
    for x in range(heigh // 2):
        for y in range(wide // 2):
            # 分别求得图片A与图片B的权重
            weightImgA[x, y, c] = varImgA[x, y, c] / (
                varImgA[x, y, c] + varImgB[x, y, c] + 0.00000001
            )
            # “0.00000001”防止零除
            weightImgB[x, y, c] = varImgB[x, y, c] / (
                varImgA[x, y, c] + varImgB[x, y, c] + 0.00000001
            )

# 进行融合，高频————系数绝对值最大化，低频————局部方差准则
reImgA = np.zeros((heigh, wide, channel), np.float32)  # 图像融合后的存储数据的变量
reImgB = np.zeros((heigh, wide, channel), np.float32)  # 临时变量
for c in range(channel):
    for x in range(heigh):
        for y in range(wide):
            if x < heigh // 2 and y < wide // 2:
                # 对两张图片低频的地方进行权值融合数据
                reImgA[x, y, c] = (
                    weightImgA[x, y, c] * waveImgA[x, y, c]
                    + weightImgB[x, y, c] * waveImgB[x, y, c]
                )
            else:
                # 对两张图片高频的进行绝对值系数最大规则融合
                reImgA[x, y, c] = (
                    waveImgA[x, y, c]
                    if abs(waveImgA[x, y, c]) >= abs(waveImgB[x, y, c])
                    else waveImgB[x, y, c]
                )

# 由于是先进行水平方向小波处理，因此重构是先进行垂直方向
# 垂直方向进行重构
for c in range(channel):
    for y in range(wide):
        for x in range(heigh):
            if x % 2 == 0:
                # 根据哈尔小波原理，将重构后的数据存储在临时变量中
                reImgB[x, y, c] = (
                    reImgA[x // 2, y, c] - reImgA[x // 2 + heigh // 2, y, c]
                )
            else:
                # 图片的前半段是低频后半段是高频，除以2余数为0相减，不为0相加
                reImgB[x, y, c] = (
                    reImgA[x // 2, y, c] + reImgA[x // 2 + heigh // 2, y, c]
                )

# 水平方向进行重构，与垂直方向同理
for c in range(channel):
    for x in range(heigh):
        for y in range(wide):
            if y % 2 == 0:
                reImgA[x, y, c] = (
                    reImgB[x, y // 2, c] - reImgB[x, y // 2 + wide // 2, c]
                )
            else:
                reImgA[x, y, c] = (
                    reImgB[x, y // 2, c] + reImgB[x, y // 2 + wide // 2, c]
                )

cv2.imshow("reImg", reImgA.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
