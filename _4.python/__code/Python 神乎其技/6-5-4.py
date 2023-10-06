# 6-5-4 產生器 method: throw

import random

def Infinite():
    while True:
        yield random.randrange(0, 100)


infinite = Infinite()

for num in infinite:
    print(num)
    if num == 13:
        infinite.throw(ValueError('13 不吉利!'))
