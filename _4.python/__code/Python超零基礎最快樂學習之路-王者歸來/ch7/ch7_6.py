# ch7_6.py
n = 5
for number in range(n):         # 列印可迭代物件
    print(number)
    
numlist = list(range(n))        # 將可迭代物件轉為串列
print("當n值是%d時的range( )串列 = " % n, numlist)
for num in numlist:             # 列印串列
    print(num)

for num in list(range(n)):      # 將可迭代物件轉為串列再列印串列
    print(num)


