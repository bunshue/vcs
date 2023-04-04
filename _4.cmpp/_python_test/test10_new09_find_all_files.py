#撈出一個資料夾下所有檔案
'''
import sys, os, glob
from PIL import Image, ImageDraw

source_dir = 'C:/______test_files/__pic'

print('Processing: {}'.format(source_dir))

allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')

print(allfiles)
'''

'''
#傑卡德相似係數 Jaccard Similarity Coefficient

from numpy import *
import scipy.spatial.distance as dist

mat1 = [1,1,0,1,0,1,0,0,1]
mat2 = [0,1,1,0,0,0,1,1,1]
mat3 = [1,1,0,1,0,1,0,0,1]  #the same as mat1
mat4 = [0,0,1,0,1,0,1,1,0]  #invert of mat1

matV = mat([mat1,mat4])

print('dist.jaccard : ')
print(dist.pdist(matV, 'jaccard'))

'''
'''
import numpy as np
import matplotlib.pyplot as plt

#曲線資料加入雜訊
x = np.linspace(-5,5,200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,yn,c='blue',marker = '.')
ax.plot(x,y+0.75,'r')
plt.show()
'''

'''
cnstr = '中文 test'
print(cnstr, len(cnstr))
#utfstr = unicode(cnstr, 'utf-8')
'''

def plotfigure(X, X_test, y, yp):
    plt.figure()
    plt.scatter(X, y, c = 'k', label = 'data')
    plt.plot(X_test, yp, c = 'r', label = 'max_depth = 5', linewidth = 2)
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Decision Tree Regression')
    plt.legend()
    plt.show()

import numpy as np
from numpy import *
#from sklearn.tree import DecisionTreeRegressor

import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
siny = np.sin(x)

X = mat(x).T
y = siny + np.random.rand(1, len(siny))*1.5 #加入雜訊的點集
y = y.tolist()[0]

plotfigure(X, X_test,y,yp)




