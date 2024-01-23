# List生成式(2)
num = [] #空的List
num = [item for item in range(10, 65)if(item % 13 == 0)]
print('10~65被13整除之數：', num)
