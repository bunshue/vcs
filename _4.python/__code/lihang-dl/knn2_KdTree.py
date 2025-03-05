"""
KdTree

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
print("------------------------------------------------------------")  # 60個

#k近邻算法的实现: kd树

#kd树代码实现

#定义kd树，设计kd树的数据结构

#构建结点对象
class KdNode(object):
    def __init__(self, dom_elt, dim=0, left=None, right=None):
        self.dom_elt = dom_elt  # k维向量节点(k维空间中的一个样本点)
        self.dim = dim  # 整数（进行分割维度的序号）
        self.left = left  # 该结点分割超平面左子空间构成的kd-tree
        self.right = right  # 该结点分割超平面右子空间构成的kd-tree

class KdTree(object):
    def __init__(self, data):
        k = len(data[0])  # 数据维度

        # 按第dim维划分数据集exset创建KdNode
        def _CreateNode(dim, data_set):
            if not data_set:  # 数据集为空
                return None
            
            # 按要进行分割的那一维数据排序
            data_set.sort(key=lambda x: x[dim])
            split_pos = len(data_set) // 2  
            median = data_set[split_pos]  # 中位数分割点
            split_next = (dim + 1) % k  # cycle coordinates

            # 递归的创建kd树
            return KdNode(
                median,
                dim,
                _CreateNode(split_next, data_set[:split_pos]),  # 创建左子树
                _CreateNode(split_next, data_set[split_pos + 1:]))  # 创建右子树

        self.root = _CreateNode(0, data)  # 从第0维分量开始构建kd树,返回根节点


# kdTree的前序遍历
def preorder(root):
    print(root.dom_elt)
    if root.left:  # 节点不为空
        preorder(root.left)
    if root.right:
        preorder(root.right)

data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
kd = KdTree(data)
cc = preorder(kd.root)
print(cc)

from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))

def kdtree(point_list, depth=0):
    if not point_list:
        return None

    k = len(point_list[0]) # 假定所有点的尺寸相同
    # 根据深度选择轴
    axis = depth % k
 
    # 根据轴对点的列表进行排序，并选择中间值作为轴元素
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2
 
    # 创建结点并构建子树
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1:], depth + 1)
    )

def main():
    """构建kd树-案例"""
    point_list = [(7,2), (5,4), (9,6), (4,7), (8,1), (2,3)]
    tree = kdtree(point_list)
    print(tree)

if __name__ == '__main__':
    main()

#scikit-learn中的 k-d-tree案例

#scikit-learn是一个机器学习类库，里面实现了KDTree。

#下面例子，构建一个二维空间的kd树，然后对其作k近邻搜索以及指定半径的搜索。

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from sklearn.neighbors import KDTree

np.random.seed(0)

# 随机产生150个二维数据
points = np.random.random((150, 2))
tree = KDTree(points)
point = points[0]
# k近邻发搜索
dists, indices = tree.query([point], k=4)

# q指定半径搜索
indices = tree.query_radius([point], r=0.2)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(Circle(point, 0.2, color='g', fill=False))
X, Y = [p[0] for p in points], [p[1] for p in points]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c='r')
plt.show()

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
