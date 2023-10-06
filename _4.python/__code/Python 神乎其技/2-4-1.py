# 2-4-1 變數名稱使用底線與雙底線的效果

class Test:
    
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


t = Test()

print(dir(t))


class ExtendedTest(Test):
    
    def __init__(self):
        super().__init__()
        self.foo = '已覆寫'
        self._bar = '已覆寫'
        self.__baz = '已覆寫'


t2 = ExtendedTest()

print('t2.foo =', t2.foo)
print('t2._bar =', t2._bar)
print('t2.__baz =', t2._ExtendedTest__baz)
print(dir(t2))