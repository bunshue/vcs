a, b = 3, 4
c = a < b
d = a == b 
# 測試關係運算子
print("小於:( 3 < 4 )=", a < b)
print("大於:( 3 > 4 )=", a > b)
print("小於等於:( 3 <= 4 )=", a <= b)
print("大於等於:( 3 >= 4 )=", a >= b)
print("等於:( 3 == 4 )=", a == b)
print("不等於:( 3 != 4 )=", a != b)
print("a =", str(a), " b =", str(b))
print("( 2 <= a <= 5 )=", 2 <= a <= 5)
print("( 12 >= b >= 5 )=", 12 >= b >= 5)
# 測試邏輯運算子
print("c條件運算式(a < b)=", c)
print("d條件運算式(a == b)=", d)
print("NOT邏輯運算子: (not c)=", (not c))
print("AND邏輯運算子: (c and d)=", (c and d))
print("OR邏輯運算子: (c or d)=", (c or d))
