# List生成式 找出10~65之間被7整除的數字

num = [] #建立空的List

for item in range(10, 65):
    if(item % 13 == 0):
        num.append(item) #整除的數放入List中
print('10~65被13整除之數：', num)

