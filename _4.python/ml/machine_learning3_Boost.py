"""
机器学习原理与实战系列之提升方法

[1] Boosting提升方法及实现
[2] AdaBoost算法及python实现
[3] GradientBoost及python实现


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
# [1] Boosting提升方法及实现
print("------------------------------------------------------------")  # 60個


"""
Boosting 算法
严格来讲Boosting不是一种算法，而是一族算法，该族算法有一个类似的框架：
    根据当前的数据训练出一个弱模型。
    根据该弱模型的表现调整数据样本的权重，具体调整方法如下：
    1.让该弱模型做错的样本在后续训练中获得更多的关注；
    2.让该弱模型做对的样本在后续训练中获得较少的关注。
    最后再根据该弱模型的表现决定改模型的"话语权"，即投票表决时的"可信度"。表现越好的就越有话语权。
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

style.use("fivethirtyeight")
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate
import scipy.stats as sps

# 加载数据
# Load in the data and define the column labels
dataset = pd.read_csv("data/mushrooms.csv", header=None)
dataset = dataset.sample(frac=1)
dataset.columns = [
    "target",
    "cap-shape",
    "cap-surface",
    "cap-color",
    "bruises",
    "odor",
    "gill-attachment",
    "gill-spacing",
    "gill-size",
    "gill-color",
    "stalk-shape",
    "stalk-root",
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",
    "stalk-color-below-ring",
    "veil-type",
    "veil-color",
    "ring-number",
    "ring-type",
    "spore-print-color",
    "population",
    "habitat",
]
# 由于sklearn DecisionTreeClassifier仅采用数值，因此将字符串中的要素值编码为整数
for label in dataset.columns:
    dataset[label] = LabelEncoder().fit(dataset[label]).transform(dataset[label])


Tree_model = DecisionTreeClassifier(criterion="entropy", max_depth=1)
X = dataset.drop("target", axis=1)
Y = dataset["target"].where(dataset["target"] == 1, -1)
predictions = np.mean(cross_validate(Tree_model, X, Y, cv=100)["test_score"])
print("The accuracy is: ", predictions * 100, "%")

# The accuracy is:  73.0727281302264 %


class Boosting:
    def __init__(self, dataset, T, test_dataset):
        self.dataset = dataset
        self.T = T
        self.test_dataset = test_dataset
        self.alphas = None
        self.models = None
        self.accuracy = []
        self.predictions = None

    def fit(self):
        # Set the descriptive features and the target feature
        X = self.dataset.drop(["target"], axis=1)
        Y = self.dataset["target"].where(self.dataset["target"] == 1, -1)
        # 初始化每个样本的权重 wi = 1/N ，并创建一个计算评估的DataFrame
        Evaluation = pd.DataFrame(Y.copy())
        Evaluation["weights"] = 1 / len(self.dataset)  # 初始化权值为 w = 1/N

        alphas = []
        models = []

        for t in range(self.T):
            # 训练决策树 Stump(s)
            Tree_model = DecisionTreeClassifier(criterion="entropy", max_depth=1)  #

            """
            在加权数据集上训练决策树分类器，其中权重是取决于先前决策树训练的结果，
            为此，这里使用上述创建的评估DataFrame的权重和fit方法的sample_weights参数，
            该参数序列如果为None,则表示样本的权重相等，如果不是None，则表示样本的权重不均等。
            """
            model = Tree_model.fit(X, Y, sample_weight=np.array(Evaluation["weights"]))

            # 将单个弱分类器附加到列表中，该列表稍后用于进行加权决策
            models.append(model)
            predictions = model.predict(X)
            score = model.score(X, Y)
            # 将值添加到评估 DataFrame中
            Evaluation["predictions"] = predictions
            Evaluation["evaluation"] = np.where(
                Evaluation["predictions"] == Evaluation["target"], 1, 0
            )
            Evaluation["misclassified"] = np.where(
                Evaluation["predictions"] != Evaluation["target"], 1, 0
            )
            # 计算误分类率和准确性
            accuracy = sum(Evaluation["evaluation"]) / len(Evaluation["evaluation"])
            misclassification = sum(Evaluation["misclassified"]) / len(
                Evaluation["misclassified"]
            )
            # 计算错误率
            err = np.sum(Evaluation["weights"] * Evaluation["misclassified"]) / np.sum(
                Evaluation["weights"]
            )

            # 计算alpha值
            alpha = np.log((1 - err) / err)
            alphas.append(alpha)
            # 更新权重 wi --> 这些更新后的权重值在sample_weight参数中用于训练写一个决策树分类器
            Evaluation["weights"] *= np.exp(alpha * Evaluation["misclassified"])

        self.alphas = alphas
        self.models = models

    def predict(self):
        X_test = self.test_dataset.drop(["target"], axis=1).reindex(
            range(len(self.test_dataset))
        )
        Y_test = (
            self.test_dataset["target"]
            .reindex(range(len(self.test_dataset)))
            .where(self.dataset["target"] == 1, -1)
        )

        # 对于self.model列表中的每个模型，进行预测
        accuracy = []
        predictions = []

        for alpha, model in zip(self.alphas, self.models):
            prediction = alpha * model.predict(X_test)  # 对列表中的单个决策树分类器模型使用预测方法
            predictions.append(prediction)
            self.accuracy.append(
                np.sum(np.sign(np.sum(np.array(predictions), axis=0)) == Y_test.values)
                / len(predictions[0])
            )

        self.predictions = np.sign(np.sum(np.array(predictions), axis=0))


# 根据使用的模型数量绘制模型精度
number_of_base_learners = 50
fig = plt.figure(figsize=(10, 10))
ax0 = fig.add_subplot(111)
for i in range(number_of_base_learners):
    model = Boosting(dataset, i, dataset)
    model.fit()
    model.predict()
ax0.plot(range(len(model.accuracy)), model.accuracy, "-b")
ax0.set_xlabel("# models used for Boosting ")
ax0.set_ylabel("accuracy")
print(
    "With a number of ",
    number_of_base_learners,
    "base models we receive an accuracy of ",
    model.accuracy[-1] * 100,
    "%",
)
print(
    "数量为 ",
    number_of_base_learners,
    "base models ，获得的精度为 ",
    model.accuracy[-1] * 100,
    "%",
)

plt.show()

# With a number of  50 base models we receive an accuracy of  98.67076923076922 %


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# [2] AdaBoost算法及python实现
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
提升方法(boosting)

提升方法是一种常见的统计学习方法
"""

# from __future__ import print_function
from numpy import *


# 加载文件并解析数据
def loadDataSet(fileName):
    # get number of fields
    numFeat = len(open(fileName).readline().split("\t"))
    dataArr = []
    labelArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataArr.append(lineArr)
        labelArr.append(float(curLine[-1]))
    return dataArr, labelArr


def stumpClassify(dataMat, dimen, threshVal, threshIneq):
    """stumpClassify(将数据集，按照feature列的value进行 二分法切分比较来赋值分类)
    Args:
        dataMat    Matrix数据集
        dimen      特征列
        threshVal  特征列要比较的值
    Returns:
        retArray 结果集
    """
    # 默认都是1
    retArray = ones((shape(dataMat)[0], 1))
    # dataMat[:, dimen] 表示数据集中第dimen列的所有值
    # threshIneq == 'lt'表示修改左边的值，gt表示修改右边的值
    if threshIneq == "lt":
        retArray[dataMat[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMat[:, dimen] > threshVal] = -1.0
    return retArray


def buildStump(dataArr, labelArr, D):
    """buildStump(得到决策树的模型)
    Args:
        dataArr   特征标签集合
        labelArr  分类标签集合
        D         最初的样本的所有特征权重集合
    Returns:
        bestStump    最优的分类器模型
        minError     错误率
        bestClasEst  训练后的结果集
    """
    # 转换数据
    dataMat = mat(dataArr)
    labelMat = mat(labelArr).T
    # m行 n列
    m, n = shape(dataMat)

    # 初始化数据
    numSteps = 10.0
    bestStump = {}
    bestClasEst = mat(zeros((m, 1)))
    # 初始化的最小误差为无穷大
    minError = inf

    # 循环所有的feature列，将列切分成 若干份，每一段以最左边的点作为分类节点
    for i in range(n):
        rangeMin = dataMat[:, i].min()
        rangeMax = dataMat[:, i].max()
        # print 'rangeMin=%s, rangeMax=%s' % (rangeMin, rangeMax)
        # 计算每一份的元素个数
        stepSize = (rangeMax - rangeMin) / numSteps
        # 例如： 4=(10-1)/2   那么  1-4(-1次)   1(0次)  1+1*4(1次)   1+2*4(2次)
        # 所以： 循环 -1/0/1/2
        for j in range(-1, int(numSteps) + 1):
            # go over less than and greater than
            for inequal in ["lt", "gt"]:
                # 如果是-1，那么得到rangeMin-stepSize; 如果是numSteps，那么得到rangeMax
                threshVal = rangeMin + float(j) * stepSize
                # 对单层决策树进行简单分类，得到预测的分类值
                predictedVals = stumpClassify(dataMat, i, threshVal, inequal)
                # print predictedVals
                errArr = mat(ones((m, 1)))
                # 正确为0，错误为1
                errArr[predictedVals == labelMat] = 0
                # 计算 平均每个特征的概率0.2*错误概率的总和为多少，就知道错误率多高
                # 例如： 一个都没错，那么错误率= 0.2*0=0 ， 5个都错，那么错误率= 0.2*5=1， 只错3个，那么错误率= 0.2*3=0.6
                weightedError = D.T * errArr
                """
                dim            表示 feature列
                threshVal      表示树的分界值
                inequal        表示计算树左右颠倒的错误率的情况
                weightedError  表示整体结果的错误率
                bestClasEst    预测的最优结果
                """
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump["dim"] = i
                    bestStump["thresh"] = threshVal
                    bestStump["ineq"] = inequal

    # bestStump 表示分类器的结果，在第几个列上，用大于／小于比较，阈值是多少
    return bestStump, minError, bestClasEst


def adaBoostTrainDS(dataArr, labelArr, numIt=40):
    """adaBoostTrainDS(adaBoost训练过程放大)
    Args:
        dataArr   特征标签集合
        labelArr  分类标签集合
        numIt     实例数
    Returns:
        weakClassArr  弱分类器的集合
        aggClassEst   预测的分类结果值
    """
    weakClassArr = []
    m = shape(dataArr)[0]
    # 初始化 D，设置每行数据的样本的所有特征权重集合，平均分为m份
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        # 得到决策树的模型
        bestStump, error, classEst = buildStump(dataArr, labelArr, D)

        # alpha 目的主要是计算每一个分类器实例的权重(加和就是分类结果)
        # 计算每个分类器的 alpha 权重值
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump["alpha"] = alpha
        # store Stump Params in Array
        weakClassArr.append(bestStump)

        # print "alpha=%s, classEst=%s, bestStump=%s, error=%s " % (alpha, classEst.T, bestStump, error)
        # 分类正确：乘积为1，不会影响结果，-1主要是下面求e的-alpha次方
        # 分类错误：乘积为 -1，结果会受影响，所以也乘以 -1
        expon = multiply(-1 * alpha * mat(labelArr).T, classEst)
        # 判断正确的，就乘以-1，否则就乘以1， 为什么？ 书上的公式。
        # print '(-1取反)预测值expon=', expon.T
        # 计算e的expon次方，然后计算得到一个综合的概率的值
        # 结果发现： 判断错误的样本，D对于的样本权重值会变大。
        D = multiply(D, exp(expon))
        D = D / D.sum()
        # print "D: ", D.T
        # print '\n'

        # 预测的分类结果值，在上一轮结果的基础上，进行加和操作
        aggClassEst += alpha * classEst
        # print "叠加后的分类结果aggClassEst: ", aggClassEst.T
        # sign 判断正为1， 0为0， 负为-1，通过最终加和的权重值，判断符号。
        # 结果为：错误的样本标签集合，因为是 !=,那么结果就是0 正, 1 负
        aggErrors = multiply(sign(aggClassEst) != mat(labelArr).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        if errorRate == 0.0:
            break
    return weakClassArr, aggClassEst


def adaClassify(datToClass, classifierArr):
    dataMat = mat(datToClass)
    m = shape(dataMat)[0]
    aggClassEst = mat(zeros((m, 1)))

    # 循环 多个分类器
    for i in range(len(classifierArr)):
        # 前提： 我们已经知道了最佳的分类器的实例
        # 通过分类器来核算每一次的分类结果，然后通过alpha*每一次的结果 得到最后的权重加和的值。
        classEst = stumpClassify(
            dataMat,
            classifierArr[i]["dim"],
            classifierArr[i]["thresh"],
            classifierArr[i]["ineq"],
        )
        aggClassEst += classifierArr[i]["alpha"] * classEst
    return sign(aggClassEst)


import matplotlib.pyplot as plt


def plotROC(predStrengths, classLabels):
    """plotROC(打印ROC曲线，并计算AUC的面积大小)
    Args:
        predStrengths  最终预测结果的权重值
        classLabels    原始数据的分类结果集
    """

    # 计算AUC
    ySum = 0.0
    # 对正样本的进行求和
    numPosClas = sum(array(classLabels) == 1.0)
    # 正样本的概率
    yStep = 1 / float(numPosClas)
    # 负样本的概率
    xStep = 1 / float(len(classLabels) - numPosClas)
    # argsort函数返回的是数组值从小到大的索引值
    # get sorted index, it's reverse
    sortedIndicies = predStrengths.argsort()

    # 开始创建模版对象
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    # cursor光标值
    cur = (1.0, 1.0)
    # 循环并绘制所有点
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0
            delY = yStep
        else:
            delX = xStep
            delY = 0
            ySum += cur[1]
        # draw line from cur to (cur[0]-delX, cur[1]-delY)
        # 画点连线 (x1, x2, y1, y2)
        if index < 10:
            print(cur[0], cur[0] - delX, cur[1], cur[1] - delY)
        ax.plot([cur[0], cur[0] - delX], [cur[1], cur[1] - delY], c="b")
        cur = (cur[0] - delX, cur[1] - delY)
    # 画对角的虚线线
    ax.plot([0, 1], [0, 1], "b--")
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.title("ROC curve for AdaBoost horse colic detection system")
    # 设置画图的范围区间 (x1, x2, y1, y2)
    ax.axis([0, 1, 0, 1])
    plt.show()
    """
    参考说明：http://blog.csdn.net/wenyusuran/article/details/39056013
    为了计算 AUC ，我们需要对多个小矩形的面积进行累加。
    这些小矩形的宽度是xStep，因此可以先对所有矩形的高度进行累加，最后再乘以xStep得到其总面积。
    所有高度的和(ySum)随着x轴的每次移动而渐次增加。
    """
    print("曲线之下的面积: ", ySum * xStep)


# 马疝病数据集
# 训练集合
dataArr, labelArr = loadDataSet("data/horseColicTraining2.txt")
weakClassArr, aggClassEst = adaBoostTrainDS(dataArr, labelArr, 40)
# 计算ROC下面的AUC的面积大小
plotROC(aggClassEst.T, labelArr)

# 曲线之下的面积:  0.8918191104095092

# 测试集合
dataArrTest, labelArrTest = loadDataSet("data/horseColicTest2.txt")
m = shape(dataArrTest)[0]
predicting10 = adaClassify(dataArrTest, weakClassArr)
errArr = mat(ones((m, 1)))
# 测试：计算总样本数，错误样本数，错误率
print(
    m,
    errArr[predicting10 != mat(labelArrTest).T].sum(),
    errArr[predicting10 != mat(labelArrTest).T].sum() / m,
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# [3] GradientBoost及python实现
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
