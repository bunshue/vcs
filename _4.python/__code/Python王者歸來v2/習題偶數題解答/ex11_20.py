# ex11_20.py
def upper(func):                # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc
def bold(func):                 # 加粗體字串裝飾器
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper
def italic(func):               # 加斜體字串裝飾器
    def wrapper(args):
        return 'italic' + func(args) + 'italic'
    return wrapper
@italic
@bold                           # 設定加粗體字串裝飾器
@upper                          # 設定大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))







