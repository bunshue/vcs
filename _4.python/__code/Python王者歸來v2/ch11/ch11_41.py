# ch11_41.py
def isPrime(num):
    """ 測試num是否質數 """
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

num = int(input("請輸入大於1的整數做質數測試 = "))
if isPrime(num):                   
    print("%d是質數" % num)
else:                                   
    print("%d不是質數" % num)


