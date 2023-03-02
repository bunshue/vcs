import math

print("圓周率 : ", math.pi)
print("圓周率 : " + str(math.pi))

for count in range(20):
    print("sin(" + str(count) + "度) = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + "度) = " + str(math.cos(2*math.pi*count/360)))

nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print("1加到10 為 : " + str(result))

n = 16
r = math.sqrt(n)
print("16的平方根 為 : "+str(r))


#使用dir()內置函數返回一個包含一個模塊中定義名稱的字符串的排序列表。
#該列表包含在一個模塊中定義的所有模塊，變量和函數的名稱。
content = dir(math)
print("math模組所支援的指令 : " + str(content))




