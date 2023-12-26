# ch12_23.py
class Myclass:
    '''文件字串實例
Myclass類別的應用'''
    def __init__(self, x):
        self.x = x
    def printMe(self):
        '''文字檔字串實例
Myclass類別內printMe方法的應用'''
        print("Hi", self.x)

data = Myclass(100)
data.printMe()
print(data.__doc__)             # 列印Myclass文件字串docstring
print(data.printMe.__doc__)     # 列印printMe文件字串docstring

