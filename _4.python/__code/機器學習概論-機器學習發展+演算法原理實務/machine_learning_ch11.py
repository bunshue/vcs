"""
machine_learning_ch02

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

print("------------------------------------------------------------")  # 60個

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Hmm.py


def viterbi(obs, states, start_p, trans_p, emit_p):
    """
    :obs:观测序列
    :states:隐状态
    :start_p:初始概率（隐状态）
    :trans_p:转移概率（隐状态）
    :emit_p: 发射概率 （隐状态表现为显状态的概率）
    :return:
    """
    V = [{}]  # 路径概率表 V[时间][隐状态] = 概率
    for y in states:  # 初始化初始状态 (t == 0)
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
    for t in range(1, len(obs)):  # 对 t > 0 跑一遍维特比算法
        V.append({})
        for y in states:
            # 概率 隐状态 =    前状态是y0的概率 * y0转移到y的概率 * y表现为当前状态的概率
            V[t][y] = max(
                [(V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]]) for y0 in states]
            )
    result = []
    for vector in V:
        temp = {}
        temp[vector.keys()[argmax(vector.values())]] = max(vector.values())
        result.append(temp)
    return result


# -------------主程序--------------#

states = ("Sunny", "Cloudy", "Rainy")
obs = ("dry", "dryish", "soggy")
start_p = {"Sunny": 0.63, "Cloudy": 0.17, "Rainy": 0.20}
trans_p = {
    "Sunny": {"Sunny": 0.5, "Cloudy": 0.375, "Rainy": 0.125},
    "Cloudy": {"Sunny": 0.25, "Cloudy": 0.125, "Rainy": 0.625},
    "Rainy": {"Sunny": 0.25, "Cloudy": 0.375, "Rainy": 0.375},
}

emit_p = {
    "Sunny": {"dry": 0.60, "dryish": 0.20, "soggy": 0.05},
    "Cloudy": {"dry": 0.25, "dryish": 0.25, "soggy": 0.25},
    "Rainy": {"dry": 0.05, "dryish": 0.10, "soggy": 0.50},
}
""" NG
result = viterbi(obs,states, start_p, trans_p, emit_p)
print(result)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# hmm01.py

# 起始概率
startP = np.mat([0.63, 0.17, 0.20])
# 状态转移概率[i,j]:i(t),j(t+1)
stateP = np.mat([[0.5, 0.25, 0.25], [0.375, 0.125, 0.375], [0.125, 0.675, 0.375]])
# 发射（混合）概率
# 列向量：emitP[:,i] = 隐含层状态; emitP[j,:] = 显式层状态
emitP = np.mat([[0.6, 0.20, 0.05], [0.25, 0.25, 0.25], [0.05, 0.10, 0.50]])

# 计算概率：干旱－干燥－潮湿
# 初始化概率：干旱：startP*emitP
state1Emit = np.multiply(startP, emitP[:, 0].T)
print(state1Emit)
print("argmax:", state1Emit.argmax())

# 计算干燥的概率:
state2Emit = stateP * state1Emit.T
state2Emit = np.multiply(state2Emit, emitP[:, 1])
print(state2Emit.T)
print("argmax:", state2Emit.argmax())

# 计算潮湿的概率:
state3Emit = stateP * state2Emit
state3Emit = np.multiply(state3Emit, emitP[:, 2])
print(state3Emit.T)
print("argmax:", state3Emit.argmax())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# hmm02.py

# 起始概率
startP = np.mat([0.63, 0.17, 0.20])
# 状态转移概率[i,j]:i(t),j(t+1)
stateP = np.mat([[0.5, 0.375, 0.125], [0.25, 0.125, 0.675], [0.25, 0.375, 0.375]])
# 发射（混合）概率
emitP = np.mat(
    [[0.6, 0.20, 0.15, 0.05], [0.25, 0.25, 0.25, 0.25], [0.05, 0.10, 0.35, 0.50]]
)

# 计算概率：干旱－干燥－潮湿
state1Emit = np.multiply(startP.T, emitP[:, 0])
print(state1Emit)
best = state1Emit.argmax()
print("max", state1Emit.max(), "path1:", state1Emit.argmax())

# 计算干燥的概率:
print(state1Emit[best], stateP)
state2Mat = np.multiply(state1Emit[best], stateP)
print(state2Mat)
state2Mat = np.dot(state2Mat, emitP[:, 1])
print("max", state2Mat.max(), "path1:", state2Mat.argmax())
"""
# 计算潮湿的概率:
state3Mat = np.multiply(state2Mat[best],stateP)
state3Mat = np.dot(state3Mat,emitP[:,1])
print("max",state3Mat.max(),"path1:",state3Mat.argmax())
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# markovtest1.py

A = [[0.8, 0.2], [0.7, 0.3]]
A = np.mat(A)
print(A)
A1 = A * A
print(A1)
A10 = A
for i in range(9):
    A10 = A10 * A
print(A10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# test01.py

# 1:1                            #3.6E                #1.3E-4
A11 = 3.9e-4 + 1.3e-5 + 5.0e-9 + 9.5e-8 + 4.7e-3 + 4.0e-4 + 7.0e-6 + 5.0e-4
print(A11)
# 1:0       #5.7E-6
A10 = 5.1e-5 + 7.0e-6 + 4.9e-7 + 9.4e-6 + 1.6e-3 + 1.7e-4 + 6.9e-4 + 1.3e-2
print(A10)
# 0:1
A01 = 5.8e-3 + 6.5e-4 + 2.9e-7 + 5.6e-6 + 6.1e-4 + 6.8e-5 + 4.8e-4 + 9.2e-3
print(A01)
# 0:0
A00 = 2.5e-3 + 2.8e-4 + 2.9e-5 + 5.5e-4 + 2.6e-4 + 2.9e-5 + 4.8e-2 + 9.1e-1
print(A00)
print(A11 + A10 + A01 + A00)
print(1 - (A11 + A10 + A01 + A00))

print(0.0060101 / (0.01681389 + 0.0060101))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
