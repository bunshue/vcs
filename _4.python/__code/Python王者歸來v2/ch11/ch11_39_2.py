# ch11_39_2.py
def upper(func):                # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        return newresult
    return newFunc

def greeting(string):           # 問候函數
    return string

mygreeting = upper(greeting)    # 手動裝飾器
print(mygreeting('Hello! iPhone'))







