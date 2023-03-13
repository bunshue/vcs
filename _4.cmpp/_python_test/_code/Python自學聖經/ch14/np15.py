import numpy as np
adata = np.arange(1,17)
print(adata)
bdata = adata.reshape(4,4)
print(bdata)

import numpy as np
na = np.arange(0,6)
print(na)           #[0 1 2 3 4 5]
print(na[0])        #0
print(na[5])        #5
print(na[1:5])      #[1 2 3 4]
print(na[1:5:2])    #[1 3]
print(na[5:1:-1])   #[5 4 3 2]
print(na[:])        #[0 1 2 3 4 5]
print(na[:3])       #[0 1 2]
print(na[3:])       #[3 4 5]

import numpy as np
na = np.arange(1, 17).reshape(4, 4)
print(na[2, 3])			#12
print(na[1, 1:3])		#[6,7]
print(na[1:3, 2])		#[7,11]
print(na[1:3, 1:3])		#[[6,7],[7,11]]
print(na[::2, ::2])		#[[1,3],[9,11]]
print(na[:, 2])			#[3,7,11,15]
print(na[1, :])			#[5,6,7,8]
print(na[:, :])			#矩陣全部

import numpy as np
print('1.產生2x3 0~1之間的隨機浮點數\n',
      np.random.rand(2,3))
print('2.產生2x3常態分佈的隨機浮點數\n',
      np.random.randn(2,3))
print('3.產生0~4(不含5)隨機整數\n',
      np.random.randint(5))
print('4.產生2~4(不含5)5個隨機整數\n',
      np.random.randint(2,5,[5]))
print('5.產生3個 0~1之間的隨機浮點數\n',
      np.random.random(3),'\n',
      np.random.random_sample(3),'\n',
      np.random.sample(3))
print('6.產生0~4(不含5)2x3的隨機整數\n',
      np.random.choice(5,[2,3]))
print('7.產生0~42(不含43)6個不重複的隨機整數\n',
      np.random.choice(43,6,replace=False))

import numpy as np
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('a 陣列內容：\n', a)
print('b 陣列內容：\n', b)
print('a 陣列元素都加值：\n', a + 1)
print('a 陣列元素都平方：\n', a ** 2)
print('a 陣列元素加判斷：\n', a < 5)
print('a 陣列取出第一個row都加1：\n', a[0,:] + 1)
print('a 陣列取出第一個col都加1：\n', a[:,0] + 1)
print('a b 陣列對應元素相加：\n', a + b)
print('a b 陣列對應元素相乘：\n', a * b)
print('a b 陣列點積計算：\n', np.dot(a,b))

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


import numpy as np
a = np.random.randint(100,size=50)
print('陣列的內容：', a)
print('1.標準差：', np.std(a))
print('2.變異數：', np.var(a))
print('3.中位數：', np.median(a))
print('4.百分比值：', np.percentile(a, 80))
print('5.最大最小差值：', np.ptp(a))


import numpy as np
a = np.random.choice(50, size=10, replace=False)
print('排序前的陣列：', a)
print('排序後的陣列：', np.sort(a))
print('排序後的索引：', np.argsort(a))
#用索引到陣列取值
for i in np.argsort(a):
    print(a[i], end=',')


import numpy as np
a = np.random.randint(0,10,(3,5))
print('原陣列內容：')
print(a)
print('將每一直行進行排序：')
print(np.sort(a, axis=0))
print('將每一橫列進行排序：')
print(np.sort(a, axis=1))





