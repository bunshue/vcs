import math

print("pi = ",math.pi)
print("pi = " + str(math.pi))

for count in range(20):
    print("sin(" + str(count) + ") = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + ") = " + str(math.cos(2*math.pi*count/360)))



import math
nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print(result)

n = 16
r = math.sqrt(n)
print(r)


import math
content = dir(math)
print(content)




