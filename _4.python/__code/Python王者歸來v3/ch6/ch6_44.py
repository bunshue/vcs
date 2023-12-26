# ch6_44.py
# 比較兩個指向相同物件的變數
a = [1, 2, 3]
b = a
print(a is b)               # 輸出: True

# 比較兩個指向不同物件的變數, 即使它們的值相等
c = [1, 2, 3]
print(a is c)               # 輸出: False

# 比較兩個指向不同物件的變數
d = [4, 5, 6]
e = [4, 5, 6]
print(d is not e)           # 輸出: True

# 比較兩個指向相同物件的變數
f = d
print(d is not f)           # 輸出: False


