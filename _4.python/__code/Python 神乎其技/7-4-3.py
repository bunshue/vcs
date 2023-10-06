# 7-4-3 dict 鍵值的更新陷阱 - 值不相等但雜湊值相等時

class SameHash:
    
    def __eq__(self, other):
        return False
    
    def __hash__(self):
        return 1


a = SameHash()
b = SameHash()
c = SameHash()

print(hash(a) == hash(b) == hash(c))

print({a: '是', b: '否', c: '也許'})
