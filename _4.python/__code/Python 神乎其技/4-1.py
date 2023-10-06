# 4-1 物件比較: == 與 is

a = [1, 2, 3]
b = a
c = list(a)

print('a == b:', a == b)
print('a is b:', a is b)
print('a == c:', a == c)
print('a is c:', a is c)