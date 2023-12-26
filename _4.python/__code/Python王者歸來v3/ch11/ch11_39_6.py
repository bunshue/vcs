# ch11_39_6.py
def upper(func):                # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc
def bold(func):
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

@upper                          # 設定大寫裝飾器
@bold                           # 設定加粗體字串大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))







