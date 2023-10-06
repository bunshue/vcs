# 6-5-3 產生器 method: close

import random

def Infinite():
    while True:
        yield random.randrange(1000)


infinite = Infinite()

for num in infinite:
    print(num)
    if num >= 900:
        infinite.close()