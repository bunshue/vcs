def check(a,b):
    try:
        return a/b
    except ZeroDivisionError: #除數為0的處理程序
        print('除數不可為0')

a=int(input('請輸入被除數:'))
b=int(input('請輸入除數:'))
print(check(a,b))
