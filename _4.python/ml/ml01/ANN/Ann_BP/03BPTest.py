# 03BPTest.py

from numpy import *
import operator
import Untils
import BackPropgation
import matplotlib.pyplot as plt

# 數據集
dataSet = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
classLabels = [0, 1, 1, 0]
expected = mat(classLabels)

# 繪製數據點
# 重構dataSet數據集
dataMat = mat(ones((shape(dataSet)[0], shape(dataSet)[1])))
dataMat[:, 1] = mat(dataSet)[:, 0]
dataMat[:, 2] = mat(dataSet)[:, 1]

# 繪製數據集散點圖
Untils.drawClassScatter(dataMat, transpose(expected), False)

# BP神經網絡進行數據分類
errRec, WEX, wex = BackPropgation.bpNet(dataSet, classLabels)

print(errRec, WEX, wex)

# 計算和繪製分類線
x = linspace(-0.2, 1.2, 30)
xx = mat(ones((30, 30)))
xx[:, 0:30] = x
yy = xx.T
z = ones((len(xx), len(yy)))
for i in range(len(xx)):
    for j in range(len(yy)):
        xi = []
        tauex = []
        tautemp = []
        mat(xi.append([xx[i, j], yy[i, j], 1]))
        hp = wex * (mat(xi).T)
        tau = BackPropgation.logistic(hp)
        taumrow, taucol = shape(tau)
        tauex = mat(ones((1, taumrow + 1)))
        tauex[:, 0:taumrow] = (tau.T)[:, 0:taumrow]
        HM = WEX * (mat(tauex).T)
        out = BackPropgation.logistic(HM)
        z[i, j] = out

Untils.classfyContour(x, x, z)

# 餅秶昫船⑻盄
X = linspace(0, 1000, 1000)
Y = log2(errRec) + 1.0e-10
Untils.TrendLine(X, Y)
