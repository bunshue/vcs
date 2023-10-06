# 7-4-2 dict 鍵值的更新陷阱 - 值相等但雜湊值不相等時

class AlwaysEquals:
    
    def __eq__(self, other):
        return True
    
    def __hash__(self):
        return id(self)


a = AlwaysEquals()
b = AlwaysEquals()
c = AlwaysEquals()

print(a == b == c)

print({a: '是', b: '否', c: '也許'})