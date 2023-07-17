import numpy as np
a = np.arange(1,10).reshape(3,3)
print('陣列的內容：\n', a)
print('1.最小值與最大值：\n',
      np.min(a), np.max(a))
print('2.每一直行最小值與最大值：\n',
      np.min(a, axis=0), np.max(a, axis=0))
print('3.每一橫列最小值與最大值：\n',
      np.min(a, axis=1), np.max(a, axis=1))
print('4.加總、乘積及平均值：\n',
      np.sum(a), np.prod(a), np.mean(a))
print('5.每一直行加總、乘積與平均值：\n',
      np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
print('6.每一橫列加總、乘積與平均值：\n',
      np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))