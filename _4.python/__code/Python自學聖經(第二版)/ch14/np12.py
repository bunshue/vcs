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