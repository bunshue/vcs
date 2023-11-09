import cv2
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

#第1步 准备数据
# A等级的笔试、面试分数
a = np.random.randint(95, 100, (20, 2)).astype(np.float32)
# B等级的笔试、面试分数
b = np.random.randint(90, 95, (20, 2)).astype(np.float32)

#合并数据
data = np.vstack((a, b))
data = np.array(data,dtype = 'float32')

#第2步 建立分组标签，0代表A等级，1代表B等级
#aLabel对应着a的标签，为类型0-等级A
aLabel = np.zeros((20, 1))
#bLabel对应着b的标签，为类型1-等级B
bLabel = np.ones((20, 1))
#合并标签
label = np.vstack((aLabel, bLabel))
label = np.array(label, dtype = 'int32')

#第3步 训练
# ml 机器学习模块 SVM_create() 创建
svm = cv2.ml.SVM_create() 
# 属性设置，直接采用默认值即可。
#svm.setType(cv2.ml.SVM_C_SVC) # svm type
#svm.setKernel(cv2.ml.SVM_LINEAR) # line
#svm.setC(0.01)
# 训练
result = svm.train(data, cv2.ml.ROW_SAMPLE,label)

#第4步 预测
#生成两个随机的(笔试成绩、面试成绩)，可以用随机数生成
test = np.vstack([[99, 90], [90, 99]]) #0-A级 1-B级
test = np.array(test, dtype = 'float32')
#预测
(p1, p2) = svm.predict(test)

#第5步 观察结果
#可视化
plt.scatter(a[:, 0], a[:, 1], 80, 'g', 'o')
plt.scatter(b[:, 0], b[:, 1], 80, 'b', 's')
plt.scatter(test[:, 0], test[:, 1], 80, 'r', '*')
plt.show()

#打印原始测试数据test，预测结果
print(test)
print(p2)

print('------------------------------------------------------------')	#60個
