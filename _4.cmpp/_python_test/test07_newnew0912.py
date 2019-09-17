import os
filenames = os.listdir('.')
print('all files:')
print(filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)


import math
nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print(result)

n = 16
r = math.sqrt(n)
print(r)


def f(x):
    return x**2



f(10)


import random
#values = [1,2,3,4,5,6]
values = ['alpha','bravo','charlie','delta','echo','foxtrot']

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))


from datetime import datetime
now = datetime.today()
print(now)



