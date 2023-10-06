# 2-4-2 前雙底線名稱也會修飾 method 與其他名稱

_MangledMethod__mangled2 = 23

class MangledMethod:
    
    def __mangled(self):
        return 42
    
    def call_it(self):
        return self.__mangled()

    def test(self):
        return __mangled2


t = MangledMethod()

print(t.call_it())
print(t._MangledMethod__mangled())
print(t.test())