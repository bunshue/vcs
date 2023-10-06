# 3-1-7 函式的一級物件特性: 內部函式可記住父函式的參數狀態 (2)

def make_adder(n):
    
    def adder(x):
        return x + n
    
    return adder


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))