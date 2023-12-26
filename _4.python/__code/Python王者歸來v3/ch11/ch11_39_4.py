# ch11_39_4.py
def errcheck(func):             # 裝飾器
    def newFunc(*args):
        if args[1] != 0:
            result = func(*args)
        else:
            result = "除數不可為0"
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        print('執行結果 : ', result)
        return result
    return newFunc
@errcheck                       # 設定裝飾器
def mydiv(x, y):                # 函數
    return x/y 

print(mydiv(6,2))
print(mydiv(6,0))





