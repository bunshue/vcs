# 3-1-8 物件也能像函式一樣被呼叫

class Adder:
    
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)

print(plus_3(4))

print(callable(plus_3))