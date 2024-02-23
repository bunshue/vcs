# ex12_4.py   
def fun(n):
    if n == 1:
        return 1.0 / 2
    else:
        return fun(n - 1) + (n * 1.0) / (n + 1)

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print('f({}) = {}'.format(i, fun(i)))           

