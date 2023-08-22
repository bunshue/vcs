import numpy as np
import cv2
from matplotlib import pyplot as plt

#随机生成两组数组
#生成60粒直径大小在[0,50]之间的xiaoMI
xiaoMI = np.random.randint(0,50,60)
#生成60粒直径大小在[200,250]之间的daMI
daMI = np.random.randint(200,250,60)
#将xiaoMI和daMI组合为MI
MI = np.hstack((xiaoMI,daMI))
#使用reshape函数将其转换为(120,1)
MI = MI.reshape((120,1))
#将MI的数据类型转换为float32
MI = np.float32(MI)
#调用kmeans模块
#设置参数criteria的值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#设置参数flags的值
flags = cv2.KMEANS_RANDOM_CENTERS
#调用函数kmeans
retval,bestLabels,centers = cv2.kmeans(MI,2,None,criteria,10,flags)
'''
#打印返回值
print(retval)
print(bestLabels)
print(centers)
'''
#获取分类结果
XM = MI[bestLabels==0]
DM = MI[bestLabels==1]
#绘制分类结果
#绘制原始数据
plt.plot(XM,'ro')
plt.plot(DM,'bs')
#绘制中心点
plt.plot(centers[0],'rx')
plt.plot(centers[1],'bx')
plt.show()


