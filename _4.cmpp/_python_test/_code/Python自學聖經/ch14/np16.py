import numpy as np
a = np.random.randint(100,size=50)
print('陣列的內容：', a)
print('1.標準差：', np.std(a))
print('2.變異數：', np.var(a))
print('3.中位數：', np.median(a))
print('4.百分比值：', np.percentile(a, 80))
print('5.最大最小差值：', np.ptp(a))