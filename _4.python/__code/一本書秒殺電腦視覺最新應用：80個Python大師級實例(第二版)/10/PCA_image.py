import cv2
import numpy as np

# 创建 eigValPct(eigVals, percentage)
# 函数传入的参数是特征值eigVals和百分比percentage，返回需要降到的维度数num


def eigValPct(eigVals, percentage):
    sortArray = np.sort(eigVals)[::-1]  # 特征值从大到小排序
    pct = np.sum(sortArray) * percentage
    tmp = 0
    num = 0
    for eigVal in sortArray:
        tmp += eigVal
        num += 1
        if tmp >= pct:
            return num


"""
创建 im_PCA(dataMat, percentage=0.9)
函数有两个参数，其中dataMat是已经转换成矩阵matrix形式的数据集，每列表示一个维度；
其中的percentage表示取前多少个特征需要达到的方差占比，默认为0.9
"""


def im_PCA(dataMat, percentage=0.9):
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    # 这里不管是对去中心化数据或原始数据计算协方差矩阵，结果都一样，特征值大小会变，但相对大小不会改变
    # 标准的计算需要除以(dataMat.shape[0]-1)，不算也不会影响结果，理由同上
    covMat = np.dot(np.transpose(meanRemoved), meanRemoved)
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    k = eigValPct(eigVals, percentage)  # 要达到方差的百分比percentage，需要前k个向量
    print("K =", k)
    eigValInd = np.argsort(eigVals)[::-1]  # 对特征值eigVals从大到小排序
    eigValInd = eigValInd[:k]
    redEigVects = eigVects[:, eigValInd]  # 主成分
    lowDDataMat = meanRemoved * redEigVects  # 将原始数据投影到主成分上得到新的低维数据lowDDataMat
    reconMat = (lowDDataMat * redEigVects.T) + meanVals  # 得到重构数据reconMat
    return lowDDataMat, reconMat


def PrintError(data, recdata):
    sum1 = 0
    sum2 = 0
    D_value = data - recdata  # 计算两幅图像之间的差值矩阵
    # 计算两幅图像之间的误差率，即信息丢失率
    for i in range(data.shape[0]):
        sum1 += np.dot(data[i], data[i])
        sum2 += np.dot(D_value[i], D_value[i])
    print("丢失信息量：", sum2)
    print("原始信息量：", sum1)
    print("信息丢失率：", sum2 / sum1)


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = cv2.imread(filename)
blue = img[:, :, 0]
dataMat = np.mat(blue)
lowDDataMat, reconMat = im_PCA(dataMat, 1)
print("原始数据", blue.shape, "降维数据", lowDDataMat.shape)
print(dataMat)
print(reconMat)
# 格式必须转换为uint8格式，这里丢失了很多信息！！！
reconMat = np.array(reconMat, dtype="uint8")

cv2.imshow("blue", blue)
cv2.imshow("reconMat", np.array(reconMat, dtype="uint8"))
cv2.waitKey(0)

# 使用sklearn的PCA方法
from sklearn.decomposition import PCA

pca = PCA(n_components=426).fit(blue)
# 降维
x_new = pca.transform(blue)
# 还原降维后的数据到原空间
recdata = pca.inverse_transform(x_new)
print(recdata)
# 计算误差
PrintError(np.array(blue, dtype="double"), np.array(reconMat, dtype="double"))

cv2.imshow("sklearn-recdata", np.array(recdata, dtype="uint8"))
cv2.waitKey(0)
