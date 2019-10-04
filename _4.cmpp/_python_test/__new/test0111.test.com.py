import time
t = time.localtime()
print(t)
print("年" , t.tm_year)
print("月" , t.tm_mon)
print("日" , t.tm_mday)
print("星" , t.tm_wday)
print("時" , t.tm_hour)
print("分" , t.tm_min)
print("秒" , t.tm_sec)


import sys
print("目前路徑 : ", sys.path)


import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

#countdown(1)


def add(x,y):
    return x+y

z = add(1234,5678)
print(z)




        


