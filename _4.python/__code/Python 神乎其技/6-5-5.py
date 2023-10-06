# 6-5-4 產生器 method: throw

import random

def Infinite():
    i = 0
    while True:
        signal = (yield i)
        if signal is not None:
            if signal == 99:
                print('停止輸出')
                break
            i += 1
        

infinite = Infinite()

for num in infinite:
    print(num)
    try:
        infinite.send(random.randrange(0, 100))
    except:
        pass
