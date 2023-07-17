import numpy as np
a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')