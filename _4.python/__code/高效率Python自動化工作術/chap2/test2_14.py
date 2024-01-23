def calc(max):
    a = 1
    while a < max:
        a = a * 2
    print("不斷乘以2倍之後，超過",max,"之後的第一個值為",a)

calc(1000)
calc(10000)
calc(100000)